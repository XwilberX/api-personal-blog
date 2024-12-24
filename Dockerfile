# syntax=docker.io/docker/dockerfile:1.7-labs

##
# Etapa 1: Builder
# - Usa la imagen de Astral con uv preinstalado
# - Instala dependencias de sistema y de Python
##
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS builder

ARG GIT_SHA
LABEL org.opencontainers.image.maintainer="Wilber Alegria <wilber.alegria99@gmail.com>" \
    org.opencontainers.image.revision=$GIT_SHA

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Si requieres compilaciones, instalamos dependencias (ej. build-essential, libpq-dev, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Env uv
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# Instala las dependencias usando el lockfile y pyproject
# en modo congelado, sin dev, sin instalar el proyecto aún
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Luego copia el resto del proyecto a /app
ADD . /app

# Vuelve a sincronizar para instalar el proyecto
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


##
# Etapa 2: Imagen final
# - Copia /app (ya con .venv y dependencias) desde el builder
# - No incluye uv
##
FROM python:3.11-slim-bookworm AS final

# (Opcional) Si necesitas algo del sistema en producción, instálalo aquí.
# RUN apt-get update && apt-get install -y --no-install-recommends <lo-necesario>

# Copiamos todo /app (código + .venv) desde la etapa builder
COPY --from=builder /app /app

# Ubicamos la .venv en el PATH
ENV PATH="/app/.venv/bin:$PATH"

# Exponer puerto si tu app corre en 8080
EXPOSE 8080

WORKDIR /app

# Comando de arranque; ajusta según tu app
# - Ejemplo: un script "entrypoint.sh" o "python main.py"
CMD ["scripts/entrypoint.sh"]
