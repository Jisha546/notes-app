from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str
    posted_at: datetime

jobs_db: List[Job] = []

@app.get("/jobs")
def get_jobs():
    return jobs_db

@app.post("/jobs")
def create_job(job: Job):
    jobs_db.append(job)
    return {"message": "Job posted successfully"}

@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    global jobs_db
    jobs_db = [job for job in jobs_db if job.id != job_id]
    return {"message": "Job deleted"}
