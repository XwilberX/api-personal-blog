# syntax=docker.io/docker/dockerfile:1.7-labs

# Stage 1: Build the application
FROM python:3.11-slim-bookworm AS base

ARG GIT_SHA

LABEL org.opencontainers.image.authors="Wilber Alegria <wilber.alegria99@gmail.com>" \
    org.opencontainers.image.vendor="Wilber Alegria" \
    org.opencontainers.image.title="Blog API" \
    org.opencontainers.image.description="A simple blog API" \
    org.opencontainers.image.revision=$GIT_SHA

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # user
    USER=app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    # apt clean up
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Stage 2: builder
FROM base AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /usr/local/bin/uv

# env variables for uv
ENV UV_LINK_MODE=copy \
    UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local \
    UV_CONCURRENT_DOWNLOADS=4 \
    UV_CONCURRENT_BUILDS=4 \
    UV_CONCURRENT_INSTALLS=10 \
    UV_NO_PROGRESS=1

# copy the requirements file
COPY pyproject.toml uv.lock /_lock/

# workdir
WORKDIR /app

# install dependencies with uv in mount cache mode
RUN --mount=type=cache,target=/root/.cache <<EOT
cd /_lock
uv sync \
    --frozen \
    --no-dev \
    --no-install-project
EOT

# copy the rest of the files
COPY . /app

# re sync to install the project
RUN --mount=type=cache,target=/root/.cache <<EOT
cd /app
uv sync \
    --frozen \
    --no-dev
EOT


# Stage 3: Final image
FROM base AS final

# copy the user from the builder
COPY --from=builder /app /app

# Start the application server
WORKDIR /app
EXPOSE 8080
CMD ["scripts/entrypoint.sh"]
