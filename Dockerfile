## This file is part of aloisius <https://github.com/skruppy/aloisius>
## Copyright (c) Skruppy <skruppy@onmars.eu>
## SPDX-License-Identifier: Apache-2.0

## docker build -t aloisius:latest .

## ==== Frontend stage
FROM node:23.1.0-alpine3.19 AS frontend
WORKDIR /app
COPY frontend/ .
RUN set -ex ;\
    npm install ;\
    npm run build


## ==== Backend stage
FROM python:3.11.10-alpine3.20 AS backend
ENV PDM_CHECK_UPDATE=false
WORKDIR /opt/aloisius/
COPY backend/ .
COPY --from=frontend /app/dist src/aloisius/statics
RUN set -ex ;\
    pip install --disable-pip-version-check -U pdm==2.20.1 ;\
    pdm install --check --prod --no-editable


## ==== Final stage
FROM python:3.11.10-alpine3.20

## Create at user to store local SQLite DB
RUN set -ex ;\
    adduser -Sh /srv/aloisius aloisius
WORKDIR /srv/aloisius/
USER aloisius

## Setup app (not in home, so it can't be modified)
COPY --from=backend /opt/aloisius/.venv/ /opt/aloisius/.venv
ENV PATH="/opt/aloisius/.venv/bin:$PATH"
EXPOSE 8080/tcp
ENTRYPOINT ["aloisius"]
