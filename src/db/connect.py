import asyncpg
from src.logger import logger
from fastapi_asyncpg import configure_asyncpg
from src.db.query import Query

class Database:
    _instance = None
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pool = None
        return cls._instance

    async def connect(self):
        self.pool = await asyncpg.create_pool(dsn=self.DATABASE_URL)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute_many(self, queries):
        async with self.pool.acquire() as connection:
            logger.info(queries)
            async with connection.transaction():
                print(queries)
                for query, args in queries:
                    print(f"query: {query}, Args: {args}")
                    await connection.execute(query, *args)

                print("transaction succesful")

    async def rollback_transaction(self):
        async with self.pool.acquire() as connection:
            await connection.rollback()

    @classmethod
    async def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            await cls._instance.connect()  # Await connect method here
        return cls._instance
