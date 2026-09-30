import pytest

from httpx import (
    ASGITransport,
    AsyncClient,
)

import main


@pytest.fixture
def client():

    return AsyncClient(
        transport=ASGITransport(
            app=main.app
        ),
        base_url="http://test",
    )


@pytest.mark.asyncio
async def test_health(client):

    async with client as ac:

        response = await ac.get(
            "/health"
        )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "ok"
    )


@pytest.mark.asyncio
async def test_qa_endpoint(
    monkeypatch,
    client,
):

    async def fake_answer(
        question
    ):

        return (
            f"Answer: {question}"
        )


    monkeypatch.setattr(
        main,
        "answer_question",
        fake_answer,
    )


    async with client as ac:

        response = await ac.post(
            "/qa",
            json={
                "question":
                    "What is Python?"
            },
        )


    assert (
        response.status_code
        == 200
    )


    assert (
        response.json()["answer"]
        ==
        "Answer: What is Python?"
    )


@pytest.mark.asyncio
async def test_explain_endpoint(
    monkeypatch,
    client,
):

    async def fake_explain(
        topic,
        level,
    ):

        return (
            f"{level}: {topic}"
        )


    monkeypatch.setattr(
        main,
        "explain_topic",
        fake_explain,
    )


    async with client as ac:

        response = await ac.post(
            "/explain",
            json={
                "topic": "gravity",
                "level": "beginner",
            },
        )


    assert (
        response.status_code
        == 200
    )


    assert (
        response.json()[
            "explanation"
        ]
        ==
        "beginner: gravity"
    )


@pytest.mark.asyncio
async def test_quiz_validation(
    client
):

    async with client as ac:

        response = await ac.post(
            "/quiz",
            json={
                "text": "too short"
            },
        )


    assert (
        response.status_code
        == 422
    )