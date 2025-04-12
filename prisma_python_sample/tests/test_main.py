import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from prisma_python_sample.main import router, get_prisma
from fastapi import FastAPI
from prisma import Prisma


@pytest_asyncio.fixture
async def prisma() -> Prisma:
    prisma = get_prisma()
    await prisma.connect()

    yield prisma

    await prisma.disconnect()


@pytest_asyncio.fixture
async def app() -> AsyncClient:
    app = FastAPI()
    app.include_router(router)

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get(prisma: Prisma, app: AsyncClient):
    await prisma.user.create(
        data={
            "email": "test@gmail.com",
            "name": "testuser",
        }
    )

    response = await app.get("/users")
    assert response.status_code == 200
    j = response.json()
    assert len(j) == 1
