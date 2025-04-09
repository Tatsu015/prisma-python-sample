from prisma import Prisma
from prisma.models import User


class DB:
    def __init__(self, provider: Prisma) -> None:
        self.provider: Prisma = provider

    async def add_user(self, email: str, name: str) -> User:
        user = await self.provider.user.create(
            data={"email": email, "name": name}
        )
        return user

    async def get_user(self, email: str) -> User:
        user = await self.provider.user.find_first(
            where={
                'email': email
            }
        )
        return user
