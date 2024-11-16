## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from .router import app as api_v1_app



def create_app():
	app = FastAPI(debug=True)

	## The order is important here. Put the more specitic pathes at first.
	app.mount('/api/1', api_v1_app, name='api')
	app.mount('/', StaticFiles(packages=['aloisius'], html=True), name='static')

	return app
