import pytest
from httpx import ASGITransport, AsyncClient
from prisma_python_sample.main import router, get_prisma
from fastapi import FastAPI


@pytest.mark.anyio
async def test_root():
    prisma = get_prisma()
    await prisma.connect()

    app = FastAPI()

    app.include_router(router)

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/users")
    assert response.status_code == 200

    await prisma.disconnect()
