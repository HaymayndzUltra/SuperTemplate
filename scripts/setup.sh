#!/usr/bin/env bash
set -euo pipefail

copy_env() {
  local dir="$1"
  if [ -f "$dir/.env" ]; then
    echo "$dir/.env already exists; skipping"
    return
  fi
  if [ -f "$dir/.env.example" ]; then
    cp "$dir/.env.example" "$dir/.env"
    echo "Copied $dir/.env.example -> $dir/.env"
  else
    echo "No .env.example in $dir; skipping"
  fi
}

copy_env "/workspace/template-packs/backend/fastapi/base"
copy_env "/workspace/template-packs/backend/django/base"

echo "Setup complete."
