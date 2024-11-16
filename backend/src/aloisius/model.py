## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

from typing import Optional
from sqlmodel import Field, SQLModel
from enum import StrEnum


JobStatus = StrEnum('JobStatus', [
	'draft',
	'ready',
	'active',
	'completed',
	'cancled',
])



class CreateJob(SQLModel):
	location: str
	initial_caller: str ## Source GURU | None
	on_site_contact: str ## Source GURU | None
	angels: str ## nr? from-to?
	task_prepareation: str
	task_description: str ## Git commit style: first line = title
	notes: str ## Internal

class ShortJob(SQLModel):
	id: int
	status: JobStatus = JobStatus.draft
	location: str
	angels: str ## nr? from-to?
	task_description: str ## Git commit style: first line = title

class Job(CreateJob, table=True):
	id: int = Field(default=None, primary_key=True)
	status: JobStatus = JobStatus.draft

class UpdateJob(SQLModel):
	location: str | None = None
	initial_caller: str | None = None
	on_site_contact: str | None = None
	angels: str | None = None
	task_prepareation: str | None = None
	task_description: str | None = None
	notes: str | None = None
	status: JobStatus | None = None
