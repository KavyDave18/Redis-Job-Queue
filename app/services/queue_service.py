import uuid

from app.config.redis import redis_client

QUEUE_NAME = "job_queue"

async def create_job(task:str):

    job_id= str(uuid.uuid4())

    await redis_client.set(f"job:{job_id}","PENDING")

    await redis_client.lpush(QUEUE_NAME,job_id)

    return {
        "job_id":job_id,
        "status":"PENDING"
    }

async def get_job_status(job_id:str):

    status = await redis_client.get(f"job:{job_id}")

    if not status:
        return None

    return{
        "job_id":job_id,
        "status":status
    }

async def update_job_status(job_id:str,status:str):

    await redis_client.set(f"job:{job_id}",status)