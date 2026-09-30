from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings

from schemas import (
    ExplainRequest,
    QARequest,
    QuizRequest,
    SummaryRequest,
    LearningPathRequest,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="EduGenie - Gemini Powered Learning Assistant",
    version="1.0.0",
    description=(
        "AI-powered educational assistant for Q&A, concept explanation, "
        "quizzes, summaries, and learning paths."
    ),
    lifespan=lifespan,
)


# -----------------------------
# Static files
# -----------------------------

app.mount(
    "/static",
    StaticFiles(
        directory=str(BASE_DIR / "static"),
        html=False,
    ),
    name="static",
)


# -----------------------------
# Templates
# -----------------------------

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# -----------------------------
# Global error handler
# -----------------------------

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    print(
        f"ERROR on {request.method} {request.url.path}:",
        repr(exc),
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc)
        },
    )


# -----------------------------
# Frontend
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.app_name
        },
    )


# -----------------------------
# Health
# -----------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "app": settings.app_name,
        "gemini_configured": bool(
            settings.gemini_api_key
        ),
        "model": settings.gemini_model,
        "local_explainer_enabled": (
            settings.use_local_explainer
        ),
    }


# -----------------------------
# Q&A
# -----------------------------

@app.post("/qa")
async def qa(payload: QARequest):

    answer = await answer_question(
        payload.question
    )

    return {
        "answer": answer
    }


# -----------------------------
# Explanation
# -----------------------------

@app.post("/explain")
async def explain(payload: ExplainRequest):

    explanation = await explain_topic(
        payload.topic,
        payload.level,
    )

    return {
        "explanation": explanation
    }


# -----------------------------
# Quiz
# -----------------------------

@app.post("/quiz")
async def quiz(payload: QuizRequest):

    quiz_data = await generate_quiz(
        payload.text,
        payload.question_count,
    )

    return {
        "quiz": quiz_data
    }


# -----------------------------
# Summary
# -----------------------------

@app.post("/summarize")
async def summarize(payload: SummaryRequest):

    summary = await summarize_text(
        payload.text,
        payload.max_words,
    )

    return {
        "summary": summary
    }


# -----------------------------
# Learning Path
# -----------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(
    payload: LearningPathRequest,
):

    recommendations = await get_learning_recommendations(
        payload.topic,
        payload.level,
        payload.timeline,
    )

    return {
        "recommendations": recommendations
    }