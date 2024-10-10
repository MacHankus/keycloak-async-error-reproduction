FROM python:3.11.9-slim-bullseye


WORKDIR /app
RUN apt-get update
RUN apt-get install libpq-dev gcc -y
RUN apt-get install libmagic1 libmagic-dev -y

COPY src src
COPY tests tests
COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --with dev
ENTRYPOINT export PYTHONPATH=$PYTHONPATH:/app/src && python -m pytest tests -vv
