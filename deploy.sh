#!/bin/sh
set -eu
cd "$(dirname "$0")"
SAM_EXECUTABLE="$(command -v sam)"
SAM_PYTHON="$(head -n 1 "$SAM_EXECUTABLE" | cut -c 3-)"
exec "$SAM_PYTHON" deploy.py "$@"
