from typing import Literal

from pydantic import (
    BaseModel,
    Field,
    field_validator,
)


def clean_text(value: str) -> str:

    value = value.strip()

    if not value:
        raise ValueError(
            "Input cannot be empty."
        )

    return value


# -----------------------------
# Q&A request
# -----------------------------

class QARequest(BaseModel):

    question: str = Field(
        ...,
        min_length=2,
        max_length=30000,
    )

    @field_validator("question")
    @classmethod
    def validate_question(
        cls,
        value: str
    ) -> str:

        return clean_text(value)


# -----------------------------
# Explanation request
# -----------------------------

class ExplainRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=2,
        max_length=30000,
    )

    level: Literal[
        "beginner",
        "intermediate",
        "advanced",
    ] = "beginner"

    @field_validator("topic")
    @classmethod
    def validate_topic(
        cls,
        value: str
    ) -> str:

        return clean_text(value)


# -----------------------------
# Quiz request
# -----------------------------

class QuizRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=20,
        max_length=30000,
    )

    question_count: int = Field(
        default=3,
        ge=1,
        le=10,
    )

    @field_validator("text")
    @classmethod
    def validate_text(
        cls,
        value: str
    ) -> str:

        return clean_text(value)


# -----------------------------
# Summary request
# -----------------------------

class SummaryRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=20,
        max_length=30000,
    )

    max_words: int = Field(
        default=120,
        ge=30,
        le=500,
    )

    @field_validator("text")
    @classmethod
    def validate_text(
        cls,
        value: str
    ) -> str:

        return clean_text(value)


# -----------------------------
# Learning path
# -----------------------------

class LearningPathRequest(BaseModel):

    topic: str = Field(
        ...,
        min_length=2,
        max_length=30000,
    )

    level: Literal[
        "beginner",
        "intermediate",
        "advanced",
    ] = "beginner"

    timeline: str = Field(
        default="6 weeks",
        min_length=2,
        max_length=100,
    )

    @field_validator(
        "topic",
        "timeline",
    )
    @classmethod
    def validate_text(
        cls,
        value: str
    ) -> str:

        return clean_text(value)