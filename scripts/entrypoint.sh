#!/usr/bin/env bash

# https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425
set -euxo pipefail

# Correr migraciones
alembic upgrade head

# Iniciar servidor
python main.py --processes=2 --workers=2
