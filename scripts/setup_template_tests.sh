#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/setup_template_tests.sh fastapi|django|next|angular

TEMPLATE=${1:-}
REPO_ROOT=$(cd "$(dirname "$0")/.." && pwd)

case "$TEMPLATE" in
  fastapi)
    cd "$REPO_ROOT/template-packs/backend/fastapi/base"
    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    # Generate a simple lock from installed set (best effort)
    python -m pip freeze | sort > requirements-lock.txt
    # Run tests
    pytest -q tests -vv || { echo "[WARN] FastAPI tests failed"; exit 1; }
    ;;
  django)
    cd "$REPO_ROOT/template-packs/backend/django/base"
    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    python -m pip freeze | sort > requirements-lock.txt
    # Run tests (noinput)
    python manage.py test --noinput || { echo "[WARN] Django tests failed"; exit 1; }
    ;;
  next)
    cd "$REPO_ROOT/template-packs/frontend/nextjs/base"
    # Create lock if missing, then use ci
    if [ ! -f package-lock.json ]; then
      npm install --package-lock-only --no-fund --no-audit
    fi
    npm ci --no-fund --no-audit
    npm test --silent || { echo "[WARN] Next.js tests failed"; exit 1; }
    ;;
  angular)
    cd "$REPO_ROOT/template-packs/frontend/angular/base"
    if [ ! -f package-lock.json ]; then
      npm install --package-lock-only --no-fund --no-audit
    fi
    npm ci --no-fund --no-audit
    # Try headless; if Chrome not present, fall back to typecheck
    if command -v google-chrome >/dev/null 2>&1 || command -v chromium >/dev/null 2>&1; then
      npm run test -- --watch=false --browsers=ChromeHeadless || { echo "[WARN] Angular tests failed"; exit 1; }
    else
      echo "[INFO] Chrome not found; running TypeScript typecheck instead"
      npx tsc -p tsconfig.spec.json
    fi
    ;;
  *)
    echo "Usage: $0 fastapi|django|next|angular" >&2
    exit 2
    ;;
esac

echo "[OK] $TEMPLATE template setup and tests completed"

