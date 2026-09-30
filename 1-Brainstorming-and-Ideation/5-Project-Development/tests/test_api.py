import pytest

from httpx import ASGITransport, AsyncClient

import main


@pytest.fixture
def client():
    return AsyncClient(
        transport=ASGITransport(app=main.app),
        base_url="http://test",
    )


@pytest.mark.asyncio
async def test_health(client):

    async with client as ac:
        response = await ac.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_home(client):

    async with client as ac:
        response = await ac.get("/")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_empty_explanation_request(client):

    async with client as ac:
        response = await ac.post(
            "/explain",
            json={"topic": ""},
        )

    assert response.status_code == 422
