import pytest
from httpx import AsyncClient, ASGITransport
from main import app

required_keys = ["status", "title", "description", "uuid"]

@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.post("/tasks/", json={
            "title": "test_title",
            "description": "test_description",
            "status": "создано"
        })
        assert response.status_code == 200
        data = response.json()
        for key in required_keys:
            assert key in data, f"Ключ '{key}' отсутствует в ответе"

@pytest.mark.asyncio
async def test_get_tasks_status():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.get("/tasks/")
        assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_tasks():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        response = await ac.get("/tasks/")

        data = response.json()
        assert len(data) == 1

@pytest.mark.asyncio
async def test_get_task():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
    ) as ac:
        response = await ac.get("/tasks/")
        data = response.json()
        response_task = await ac.get(f"/task/{data[0]["uuid"]}")
        data_task = response_task.json()
        for key in required_keys:
            assert key in data_task, f"Ключ '{key}' отсутствует в ответе"


@pytest.mark.asyncio
async def test_delete_task():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
    ) as ac:
        response = await ac.get("/tasks/")
        data = response.json()
        print(data)
        response_delete = await ac.delete(f"/task/{data[0]['uuid']}")
        assert response_delete.status_code == 200

