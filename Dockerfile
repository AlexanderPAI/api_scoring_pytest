FROM python:3.13-slim AS base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential tree curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry==2.1.2
RUN poetry config virtualenvs.create false && poetry install --no-root

FROM base AS build

COPY src/ src/
COPY tests/ tests/
COPY scripts/ scripts/

CMD ["python3", "-m", "src.api"]
