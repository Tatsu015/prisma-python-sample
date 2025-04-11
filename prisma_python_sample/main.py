from fastapi import FastAPI
from prisma_python_sample.prisma import get_prisma
from prisma_python_sample.roter import router

__prisma = get_prisma()


async def lifespan(app: FastAPI):
    await __prisma.connect()
    yield
    await __prisma.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(router)
