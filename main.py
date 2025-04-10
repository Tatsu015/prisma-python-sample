from fastapi import FastAPI, HTTPException
from prisma import Prisma
from prisma.models import User
from db import DB
from contextlib import asynccontextmanager

prisma = Prisma()
db = DB(prisma)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/users/{email}', response_model=User)
async def get_user(email: str):
    user = await db.get_user(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post('/users', response_model=User)
async def create_user(email: str, name: str):
    try:
        user = await db.add_user(email, name)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put('/users/{email}', response_model=User)
async def update_user(email: str, new_name: str):
    existing_user = await db.get_user(email)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await prisma.user.update(
        where={'email': email},
        data={'name': new_name}
    )
    return updated_user


@app.delete('/users/{email}')
async def delete_user(email: str):
    existing_user = await db.get_user(email)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = await prisma.user.delete(
        where={'email': email}
    )
    return {"message": f"User with email {email} deleted successfully"}
