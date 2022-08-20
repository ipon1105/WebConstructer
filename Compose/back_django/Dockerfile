FROM python:3.10.0-slim

ENV PYTHONDONTWRITEBYTECODE ]
ENV PYTHONUNBUFFERED]

ARG PROJ_DIR=/webconstructer

RUN mkdir -p ${PROJ_DIR}
COPY ./constructer ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN python -m pip install install -U pip \
    python -m pip install install -r requirements.txt

COPY ./compose/back_django/entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]