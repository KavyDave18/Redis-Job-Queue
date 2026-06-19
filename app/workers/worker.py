import asyncio

from app.config.redis import redis_client

from app.services.worker_service import (
    process_job
)


QUEUE_NAME = "job_queue"


async def worker():

    print(
        "Worker Started..."
    )

    while True:

        job = await redis_client.brpop(
            QUEUE_NAME
        )

        payload = job[1]

        job_id, task = payload.split(
            "|",
            1
        )

        await process_job(
            job_id,
            task
        )


if __name__ == "__main__":
    asyncio.run(
        worker()
    )