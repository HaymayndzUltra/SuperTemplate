#!/usr/bin/env bash
set -euo pipefail

# install_and_test.sh
# Stack-aware install/build/test runner for generated projects.
# Detects FE/BE directories and runs appropriate package managers/tests.

if [[ -n "${PROJECT_ROOT:-}" ]]; then
  ROOT_DIR="$PROJECT_ROOT"
else
  ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
fi
cd "$ROOT_DIR"

FRONTEND_DIR=${FRONTEND_DIR:-frontend}
BACKEND_DIR=${BACKEND_DIR:-backend}

log() {
  echo "[INSTALL_TEST] $*"
}

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

run_in_dir() {
  local dir="$1"
  shift
  if [[ ! -d "$dir" ]]; then
    log "Skip: directory '$dir' not found"
    return 0
  fi
  log "Running in $dir: $*"
  (cd "$dir" && "$@")
}

PYTHON_BIN=""
ensure_python() {
  local purpose="$1"
  if [[ -n "$PYTHON_BIN" ]]; then
    return 0
  fi
  if command_exists python; then
    PYTHON_BIN=python
  elif command_exists python3; then
    PYTHON_BIN=python3
  else
    log "ERROR: Python is required for $purpose but was not found on PATH." >&2
    exit 1
  fi
}

package_has_script() {
  local dir="$1"
  local script="$2"
  if [[ ! -f "$dir/package.json" ]]; then
    return 1
  fi
  if ! command_exists node; then
    return 1
  fi
  node <<'NODE' "$dir/package.json" "$script"
const fs = require('fs');
const path = process.argv[2];
const scriptName = process.argv[3];
try {
  const pkg = JSON.parse(fs.readFileSync(path, 'utf8'));
  if (pkg.scripts && Object.prototype.hasOwnProperty.call(pkg.scripts, scriptName)) {
    process.exit(0);
  }
} catch (err) {
  process.exit(1);
}
process.exit(1);
NODE
}

NODE_PM_REASON=""
choose_node_pm() {
  local dir="$1"
  NODE_PM_REASON=""
  local has_pnpm_lock="false"

  if [[ -f "$dir/pnpm-lock.yaml" ]]; then
    has_pnpm_lock="true"
    if command_exists pnpm; then
      NODE_PM_REASON="pnpm-lock.yaml detected"
      printf '%s' pnpm
      return 0
    fi
    if command_exists npm; then
      NODE_PM_REASON="pnpm-lock.yaml detected but pnpm missing; falling back to npm"
      printf '%s' npm
      return 0
    fi
  fi

  if [[ -f "$dir/package-lock.json" ]] && command_exists npm; then
    NODE_PM_REASON="package-lock.json detected"
    printf '%s' npm
    return 0
  fi

  if [[ -f "$dir/yarn.lock" ]] && command_exists yarn; then
    NODE_PM_REASON="yarn.lock detected"
    printf '%s' yarn
    return 0
  fi

  if [[ "$has_pnpm_lock" == "false" ]] && command_exists npm; then
    NODE_PM_REASON="pnpm-lock.yaml not found; defaulting to npm"
    printf '%s' npm
    return 0
  fi

  for candidate in npm pnpm yarn; do
    if command_exists "$candidate"; then
      NODE_PM_REASON="fallback to available package manager ($candidate)"
      printf '%s' "$candidate"
      return 0
    fi
  done

  NODE_PM_REASON="no supported package manager found"
  return 1
}

maybe_run_package_script() {
  local dir="$1"
  local pm="$2"
  local script="$3"
  if [[ "$dir" == "$FRONTEND_DIR" ]]; then
    if [[ "$script" == "build" && "${SKIP_FRONTEND_BUILD:-0}" == "1" ]]; then
      log "Skipping '$script' script in $dir (SKIP_FRONTEND_BUILD=1)"
      return 0
    fi
    if [[ "$script" == "test" && "${SKIP_FRONTEND_TESTS:-0}" == "1" ]]; then
      log "Skipping '$script' script in $dir (SKIP_FRONTEND_TESTS=1)"
      return 0
    fi
  fi
  if [[ "$dir" == "$BACKEND_DIR" ]]; then
    if [[ "$script" == "build" && "${SKIP_BACKEND_BUILD:-0}" == "1" ]]; then
      log "Skipping '$script' script in $dir (SKIP_BACKEND_BUILD=1)"
      return 0
    fi
    if [[ "$script" == "test" && "${SKIP_BACKEND_TESTS:-0}" == "1" ]]; then
      log "Skipping '$script' script in $dir (SKIP_BACKEND_TESTS=1)"
      return 0
    fi
  fi
  case "$pm" in
    pnpm)
      log "Executing '$script' script with pnpm (if present)"
      run_in_dir "$dir" pnpm run --if-present "$script"
      ;;
    npm)
      log "Executing '$script' script with npm (if present)"
      if package_has_script "$dir" "$script"; then
        run_in_dir "$dir" npm run --if-present "$script"
      else
        log "Skip: package.json has no '$script' script in $dir"
      fi
      ;;
    yarn)
      if package_has_script "$dir" "$script"; then
        log "Executing '$script' script with yarn"
        run_in_dir "$dir" yarn run "$script"
      else
        log "Skip: package.json has no '$script' script in $dir"
      fi
      ;;
    *)
      log "ERROR: Unsupported package manager '$pm' for $dir" >&2
      exit 1
      ;;
  esac
}

run_node_workflow() {
  local dir="$1"
  local pm="$2"
  local skip_install="false"
  local skip_reason=""

  if [[ "$dir" == "$FRONTEND_DIR" && "${SKIP_FRONTEND_INSTALL:-0}" == "1" ]]; then
    skip_install="true"
    skip_reason="SKIP_FRONTEND_INSTALL=1"
  elif [[ "$dir" == "$BACKEND_DIR" && "${SKIP_BACKEND_INSTALL:-0}" == "1" ]]; then
    skip_install="true"
    skip_reason="SKIP_BACKEND_INSTALL=1"
  fi

  if [[ "$skip_install" == "true" ]]; then
    log "Skipping dependency install in $dir ($skip_reason)"
  else
    case "$pm" in
      pnpm)
        log "Installing Node dependencies in $dir with pnpm"
        local install_args=(install)
        if [[ -f "$dir/pnpm-lock.yaml" ]]; then
          install_args+=(--frozen-lockfile)
        fi
        run_in_dir "$dir" pnpm "${install_args[@]}"
        ;;
      npm)
        log "Installing Node dependencies in $dir with npm"
        if [[ -f "$dir/package-lock.json" ]]; then
          if ! (cd "$dir" && npm ci); then
            log "npm ci failed in $dir; falling back to npm install"
            run_in_dir "$dir" npm install
          fi
        else
          run_in_dir "$dir" npm install
        fi
        ;;
      yarn)
        log "Installing Node dependencies in $dir with yarn"
        local install_args=(install)
        if [[ -f "$dir/yarn.lock" ]]; then
          install_args+=(--frozen-lockfile)
        fi
        run_in_dir "$dir" yarn "${install_args[@]}"
        ;;
      *)
        log "ERROR: Unsupported package manager '$pm' for $dir" >&2
        exit 1
        ;;
    esac
  fi

  maybe_run_package_script "$dir" "$pm" build
  maybe_run_package_script "$dir" "$pm" test
}

handle_frontend() {
  if [[ ! -d "$FRONTEND_DIR" ]]; then
    log "Skip: frontend directory '$FRONTEND_DIR' not found"
    return 0
  fi
  log "Detected frontend workspace at '$FRONTEND_DIR'"
  local pm
  if ! pm="$(choose_node_pm "$FRONTEND_DIR")"; then
    log "ERROR: Unable to determine package manager for $FRONTEND_DIR (${NODE_PM_REASON})" >&2
    exit 1
  fi
  log "Frontend package manager: $pm (${NODE_PM_REASON})"
  run_node_workflow "$FRONTEND_DIR" "$pm"
}

handle_backend_python() {
  local has_manifest="false"
  if [[ -f "$BACKEND_DIR/requirements.txt" ]]; then
    has_manifest="true"
    if [[ "${SKIP_BACKEND_INSTALL:-0}" == "1" ]]; then
      log "Skipping Python dependency install in $BACKEND_DIR (SKIP_BACKEND_INSTALL=1)"
    else
      ensure_python "installing backend dependencies"
      log "Installing Python dependencies from requirements.txt in $BACKEND_DIR"
      run_in_dir "$BACKEND_DIR" "$PYTHON_BIN" -m pip install -r requirements.txt
    fi
  elif [[ -f "$BACKEND_DIR/pyproject.toml" ]]; then
    has_manifest="true"
    if [[ "${SKIP_BACKEND_INSTALL:-0}" == "1" ]]; then
      log "Skipping Python project install in $BACKEND_DIR (SKIP_BACKEND_INSTALL=1)"
    else
      ensure_python "installing backend project"
      log "Installing Python project defined by pyproject.toml in $BACKEND_DIR"
      run_in_dir "$BACKEND_DIR" "$PYTHON_BIN" -m pip install .
    fi
  fi

  local pytest_trigger="false"
  if [[ -d "$BACKEND_DIR/tests" || -d "$BACKEND_DIR/test" || -f "$BACKEND_DIR/pytest.ini" ]]; then
    pytest_trigger="true"
  fi

  if [[ "$pytest_trigger" == "true" ]]; then
    if [[ "${SKIP_BACKEND_TESTS:-0}" == "1" ]]; then
      log "Skipping backend pytest suite (SKIP_BACKEND_TESTS=1)"
    else
      ensure_python "running backend tests"
      log "Running backend pytest suite"
      run_in_dir "$BACKEND_DIR" "$PYTHON_BIN" -m pytest -q
    fi
  elif [[ "$has_manifest" == "true" ]]; then
    log "Skip: no pytest configuration detected in $BACKEND_DIR"
  fi
}

handle_backend_node() {
  if [[ ! -f "$BACKEND_DIR/package.json" ]]; then
    return 0
  fi
  log "Detected Node backend workspace at '$BACKEND_DIR'"
  local pm
  if ! pm="$(choose_node_pm "$BACKEND_DIR")"; then
    log "ERROR: Unable to determine package manager for $BACKEND_DIR (${NODE_PM_REASON})" >&2
    exit 1
  fi
  log "Backend package manager: $pm (${NODE_PM_REASON})"
  run_node_workflow "$BACKEND_DIR" "$pm"
}

handle_backend_go() {
  if [[ ! -f "$BACKEND_DIR/go.mod" ]]; then
    return 0
  fi
  if ! command_exists go; then
    log "ERROR: Go is required for backend tests but was not found on PATH." >&2
    exit 1
  fi
  log "Installing Go modules in $BACKEND_DIR"
  run_in_dir "$BACKEND_DIR" go mod download
  log "Running Go tests"
  run_in_dir "$BACKEND_DIR" go test ./... -count=1
}

handle_backend() {
  if [[ ! -d "$BACKEND_DIR" ]]; then
    log "Skip: backend directory '$BACKEND_DIR' not found"
    return 0
  fi
  log "Detected backend workspace at '$BACKEND_DIR'"
  handle_backend_python
  handle_backend_node
  handle_backend_go
}

handle_frontend
handle_backend

log "Completed install_and_test pipeline"
