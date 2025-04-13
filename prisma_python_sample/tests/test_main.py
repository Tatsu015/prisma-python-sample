import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from prisma_python_sample.main import router, get_prisma
from fastapi import FastAPI
from prisma import Prisma


async def __delete_all(prisma: Prisma):
    await prisma.user.delete_many()
    await prisma.post.delete_many()


@pytest_asyncio.fixture
async def prisma() -> Prisma:
    p = get_prisma()
    await p.connect()

    yield p

    await __delete_all(p)
    await p.disconnect()


@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    a = FastAPI()
    a.include_router(router)

    async with AsyncClient(
        transport=ASGITransport(app=a), base_url="http://test"
    ) as ac:
        yield ac


@pytest.mark.asyncio
async def test_get(prisma: Prisma, async_client: AsyncClient):
    await prisma.user.create(
        data={
            "email": "test@gmail.com",
            "name": "testuser",
        }
    )

    res = await async_client.get("/users")
    assert res.status_code == 200
    j = res.json()
    assert len(j) == 1
