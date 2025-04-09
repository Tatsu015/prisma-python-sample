import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    read_user = await prisma.user.find_first(
        where={
            'email': 'robert@craigie.dev'
        }
    )

    if read_user:
        print(f'read user:{read_user}')

    else:
        add_user = await prisma.user.create(
            data={
                'name': 'Robert',
                'email': 'robert@craigie.dev'
            },
        )
    
        print(f"add user:{add_user}")


    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())