from functools import lru_cache

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    app_name: str = "EduGenie"

    # Google Gemini API key
    gemini_api_key: str = ""

    # Use a valid Gemini model name
    gemini_model: str = "gemini-3.8-flash"

    use_local_explainer: bool = False

    local_explainer_model: str = (
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    max_input_chars: int = 30000
    request_timeout_seconds: int = 90

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()