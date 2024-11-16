## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

from fastapi import APIRouter, Depends, FastAPI
from sqlmodel import SQLModel, create_engine
from .db import get_db_session
from .model import *
from typing import List
from sqlalchemy import select
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
	## Check OpenAPI schema (fka swagger) with http://localhost:8080/api/1/redoc or
	## http://localhost:8080/api/1/docs
	title = 'Aloisius Programming Interface (API)',
	version = '1.0.0', ## API version, not Package version
	description = 'Web tool to manage standby angel deployments on chaos events',
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=False,
	allow_methods =['GET', 'POST', 'PATCH', 'DELETE'],
)


## http -j POST 127.0.0.1:8080/api/1/jobs location="Lager" initial_caller="BOC" on_site_contact="Aloisius (1234)" angels="2-3" task_prepareation="Handschuhe holen" task_description="Kästen stapeln" notes="YOLO"
@app.post('/jobs')
def create_job(job_req: CreateJob, db=Depends(get_db_session)) -> Job:
	job = Job.model_validate(job_req)

	db.add(job)
	db.flush()
	job = Job.model_validate(job)
	db.commit()

	return job


## http -j GET 127.0.0.1:8080/api/1/jobs/1
@app.get('/jobs/{id}')
def read_job(id: int, db = Depends(get_db_session)) -> Job:
	job = db.get(Job, id)
	return job


## http -j PATCH 127.0.0.1:8080/api/1/jobs/1 angels=$RANDOM
@app.patch('/jobs/{id}')
def update_job(id: int, job_req: UpdateJob, db=Depends(get_db_session)) -> Job:
	job = db.get(Job, id)
	for key, value in job_req.model_dump(exclude_unset=True).items():
		setattr(job, key, value)
	db.flush()
	job = Job.model_validate(job)
	db.commit()

	return job


## http -j GET 127.0.0.1:8080/api/1/jobs
@app.get('/jobs')
def list_jobs(db = Depends(get_db_session)) -> List[ShortJob]:
	print('there')
	jobs = [x[0] for x in db.execute(select(Job))]
	return jobs
