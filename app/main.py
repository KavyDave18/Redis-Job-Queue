from app.routes.jobs import router
from fastapi import FastAPI

app = FastAPI(title="Redis Job Queue")

app.include_router(router)