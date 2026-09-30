import json
import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from google import genai
from pydantic import BaseModel, Field


load_dotenv()

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


class LearningRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=10000)


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured.",
        )

    return genai.Client(api_key=api_key)


def get_model():
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def clean_json_text(text: str) -> str:
    text = text.strip()

    if text.startswith("```"):
        lines = text.splitlines()

        if lines and lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        text = "\n".join(lines).strip()

    return text


def generate_text(prompt: str) -> str:
    try:
        client = get_client()

        response = client.models.generate_content(
            model=get_model(),
            contents=prompt,
        )

        text = getattr(response, "text", None)

        if not text:
            raise HTTPException(
                status_code=502,
                detail="Gemini returned an empty response.",
            )

        return text.strip()

    except HTTPException:
        raise

    except Exception as exc:
        message = str(exc)

        if "quota" in message.lower() or "429" in message:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again later.",
            )

        raise HTTPException(
            status_code=502,
            detail=f"AI service error: {message}",
        )


def generate_json(prompt: str) -> Any:
    text = generate_text(prompt)
    cleaned = clean_json_text(text)

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=502,
            detail="The AI returned an invalid JSON response.",
        )


@app.get("/")
async def home():
    return FileResponse("static/index.html")


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "EduGenie",
    }


@app.post("/explain")
async def explain(request: LearningRequest):
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in simple language for a student:

Topic:
{request.topic}

Requirements:
- Give a clear definition.
- Explain the main concept.
- Give important points.
- Give a simple example.
- Keep the explanation educational and easy to understand.
"""

    return {
        "topic": request.topic,
        "explanation": generate_text(prompt),
    }


@app.post("/summarize")
async def summarize(request: LearningRequest):
    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following educational content:

{request.topic}

Return:
1. A short summary.
2. Important points.
3. Key terms.

Use simple student-friendly language.
"""

    return {
        "summary": generate_text(prompt),
    }


@app.post("/quiz")
async def quiz(request: LearningRequest):
    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 5 multiple-choice questions about:

{request.topic}

Return ONLY valid JSON.

Use exactly this structure:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "One exact option from the options",
    "explanation": "Short explanation"
  }}
]

Do not include Markdown or code fences.
"""

    data = generate_json(prompt)

    if not isinstance(data, list):
        raise HTTPException(
            status_code=502,
            detail="Invalid quiz format returned by AI.",
        )

    return {
        "topic": request.topic,
        "quiz": data,
    }


@app.post("/questions")
async def questions(request: LearningRequest):
    prompt = f"""
You are EduGenie, an educational question generator.

Generate 5 useful practice questions about:

{request.topic}

Return ONLY valid JSON using this structure:

[
  {{
    "question": "Question",
    "answer": "Answer",
    "difficulty": "Easy"
  }}
]

Difficulty must be one of:
Easy, Medium, Hard

Do not include Markdown or code fences.
"""

    data = generate_json(prompt)

    if not isinstance(data, list):
        raise HTTPException(
            status_code=502,
            detail="Invalid question format returned by AI.",
        )

    return {
        "topic": request.topic,
        "questions": data,
    }


@app.post("/learning-path")
async def learning_path(request: LearningRequest):
    prompt = f"""
You are EduGenie, an educational learning-path generator.

Create a beginner-friendly learning path for:

{request.topic}

Return ONLY valid JSON using this structure:

{{
  "topic": "Topic",
  "steps": [
    {{
      "step": 1,
      "title": "Step title",
      "description": "What the student should learn"
    }}
  ]
}}

Create 5 to 7 learning steps.

Do not include Markdown or code fences.
"""

    data = generate_json(prompt)

    if not isinstance(data, dict):
        raise HTTPException(
            status_code=502,
            detail="Invalid learning path format returned by AI.",
        )

    return data
