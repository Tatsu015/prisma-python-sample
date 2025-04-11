from prisma import Prisma

__prisma_instance = Prisma()


def get_prisma():
    return __prisma_instance
