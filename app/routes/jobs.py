from fastapi import APIRouter,HTTPException
from app.models.schemas import JobRequest,JobResponse
from app.services.queue_service import create_job,get_job_status

router = APIRouter(
        prefix="/jobs",
        tags=["Jobs"]
    )

@router.post("",response_model=JobResponse)
async def create_new_job(request:JobRequest):
    return await create_job(request.task)

@router.get("/{job_id}",response_model=JobResponse)
async def fetch_job_status(job_id:str):
    job = await get_job_status(job_id)

    if not job:
        raise HTTPException(status_code=404,detail="Job Not Found")

    return job


