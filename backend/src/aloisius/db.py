## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

from sqlmodel import SQLModel, create_engine, Session
from .model import *



engine = create_engine("sqlite:///database.db", echo=True)
SQLModel.metadata.create_all(engine)

def get_db_session():
	with Session(engine) as session:
		yield session
