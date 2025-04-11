from fastapi import HTTPException, Depends, APIRouter
from prisma import Prisma
from prisma.models import User
from prisma_python_sample.prisma import get_prisma

router = APIRouter()


@router.get('/users', response_model=list[User])
async def get_users(prisma: Prisma = Depends(get_prisma)):
    users = await prisma.user.find_many()
    return users


@router.get('/users/{email}', response_model=User)
async def get_user(email: str, prisma: Prisma = Depends(get_prisma)):
    user = await prisma.user.find_first(
        where={
            'email': email
        }
    )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post('/users', response_model=User)
async def create_user(email: str, name: str, prisma: Prisma = Depends(get_prisma)):
    try:
        user = await prisma.user.create(
            data={"email": email, "name": name}
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put('/users/{email}', response_model=User)
async def update_user(email: str, new_name: str, prisma: Prisma = Depends(get_prisma)):
    existing_user = await prisma.user.find_first(
        where={
            'email': email
        }
    )
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await prisma.user.update(
        where={'email': email},
        data={'name': new_name}
    )
    return updated_user


@router.delete('/users/{email}')
async def delete_user(email: str, prisma: Prisma = Depends(get_prisma)):
    existing_user = await prisma.user.find_first(
        where={
            'email': email
        }
    )
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = await prisma.user.delete(
        where={'email': email}
    )
    return {"message": f"User with email {deleted_user} deleted success"}
