import uuid

from app.config.redis import redis_client


QUEUE_NAME = "job_queue"


async def create_job(task: str):

    job_id = str(uuid.uuid4())

    await redis_client.set(
        f"job:{job_id}:status",
        "PENDING"
    )

    await redis_client.lpush(
        QUEUE_NAME,
        f"{job_id}|{task}"
    )

    return {
        "job_id": job_id,
        "status": "PENDING"
    }


async def get_job_status(job_id: str):

    status = await redis_client.get(
        f"job:{job_id}:status"
    )

    if not status:
        return None

    result = await redis_client.get(
        f"job:{job_id}:result"
    )

    return {
        "job_id": job_id,
        "status": status,
        "result": result
    }


async def update_job_status(
    job_id: str,
    status: str
):

    await redis_client.set(
        f"job:{job_id}:status",
        status
    )


async def save_job_result(
    job_id: str,
    result: str
):

    await redis_client.set(
        f"job:{job_id}:result",
        result
    )