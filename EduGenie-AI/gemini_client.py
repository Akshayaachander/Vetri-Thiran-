
import asyncio

from google import genai
from google.genai import types

from config import settings


_client = None


def get_client():
    global _client

    if _client is None:

        if not settings.gemini_api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is missing. "
                "Please add your Gemini API key to the .env file."
            )

        _client = genai.Client(
            api_key=settings.gemini_api_key
        )

    return _client


def _generate(
    prompt: str,
    temperature: float = 0.7,
    max_output_tokens: int = 1000,
    response_schema=None,
) -> str:

    client = get_client()

    config_kwargs = {
        "temperature": temperature,
        "max_output_tokens": max_output_tokens,
    }

    if response_schema is not None:

        config_kwargs["response_mime_type"] = (
            "application/json"
        )

        config_kwargs["response_schema"] = (
            response_schema
        )

    try:

        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                **config_kwargs
            ),
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as exc:

        error_text = str(exc).upper()

        if (
            "429" in error_text
            or "RESOURCE_EXHAUSTED" in error_text
            or "QUOTA" in error_text
        ):

            raise RuntimeError(
                "GEMINI_QUOTA_EXCEEDED"
            ) from exc

        if (
            "503" in error_text
            or "UNAVAILABLE" in error_text
        ):

            raise RuntimeError(
                "GEMINI_TEMPORARILY_UNAVAILABLE"
            ) from exc

        raise RuntimeError(
            f"Gemini API error: {exc}"
        ) from exc


async def generate_text(
    prompt: str,
    temperature: float = 0.7,
    max_output_tokens: int = 1000,
    response_schema=None,
) -> str:

    return await asyncio.to_thread(
        _generate,
        prompt,
        temperature,
        max_output_tokens,
        response_schema,
    )


async def generate_json(
    prompt: str,
    response_schema=None,
) -> str:

    return await generate_text(
        prompt,
        temperature=0.5,
        max_output_tokens=2200,
        response_schema=response_schema,
    )

