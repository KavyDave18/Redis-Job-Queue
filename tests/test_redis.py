import asyncio
from app.config.redis import redis_client

async def main():
    await redis_client.set("name","kavy")

    value = await redis_client.get("name")

    print(value)

asyncio.run(main())

