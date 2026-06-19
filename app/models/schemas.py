from pydantic import BaseModel

class JobRequest(BaseModel):
    task:str

class JobResponse(BaseModel):
    job_id:str
    status:str