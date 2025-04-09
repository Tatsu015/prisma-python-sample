import asyncio
from prisma import Prisma
from db import DB


async def main() -> None:
    prisma = Prisma()
    await prisma.connect()
    db = DB(prisma)

    read_user = await db.get_user('robert@craigie.dev')
    if read_user:
        print(f'read user:{read_user}')

    else:
        add_user = await db.add_user(name='Robert', email='robert@craigie.dev')
        print(f"add user:{add_user}")

    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
