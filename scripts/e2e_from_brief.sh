#!/usr/bin/env bash
set -euo pipefail

# e2e_from_brief.sh
# Non-interactive, stop-the-line workflow from approved brief to delivery.
# Reads configuration from workflow.config.json in the repo root unless env overrides are provided.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
cd "$ROOT_DIR"

# Ensure local package imports (project_generator) are resolvable
export PYTHONPATH="$ROOT_DIR:${PYTHONPATH:-}"

CONFIG_FILE="${CONFIG_FILE:-workflow.config.json}"

# Select Python interpreter
if command -v python >/dev/null 2>&1; then
  PY_BIN=python
elif command -v python3 >/dev/null 2>&1; then
  PY_BIN=python3
else
  echo "[E2E] Python is not installed. Please install python3." >&2
  exit 127
fi

read_cfg() {
  local cfg_path="$1"; shift
  local key="$1"
  "$PY_BIN" - "$cfg_path" "$key" <<'PY'
import json,sys
cfg_path=sys.argv[1]
key=sys.argv[2]
try:
  with open(cfg_path,'r',encoding='utf-8') as f:
    cfg=json.load(f)
  v=cfg
  for part in key.split('.'):
    v=v.get(part,{}) if isinstance(v,dict) else None
  if isinstance(v,dict):
    print(json.dumps(v))
  elif v is not None:
    print(v)
except FileNotFoundError:
  pass
PY
}

NAME="${NAME:-$(read_cfg "$CONFIG_FILE" name || true)}"
INDUSTRY="${INDUSTRY:-$(read_cfg "$CONFIG_FILE" industry || true)}"
PROJECT_TYPE="${PROJECT_TYPE:-$(read_cfg "$CONFIG_FILE" project_type || true)}"
FE="${FE:-${FRONTEND:-$(read_cfg "$CONFIG_FILE" frontend || true)}}"
BE="${BE:-${BACKEND:-$(read_cfg "$CONFIG_FILE" backend || true)}}"
DB="${DB:-${DATABASE:-$(read_cfg "$CONFIG_FILE" database || true)}}"
AUTH="${AUTH:-$(read_cfg "$CONFIG_FILE" auth || true)}"
DEPLOY="${DEPLOY:-$(read_cfg "$CONFIG_FILE" deploy || true)}"
COMPLIANCE="${COMPLIANCE:-$(read_cfg "$CONFIG_FILE" compliance || true)}"

required=(NAME INDUSTRY PROJECT_TYPE FE BE DB)
for var in "${required[@]}"; do
  if [[ -z "${!var:-}" ]]; then
    echo "[E2E] Missing required config: $var (set env or workflow.config.json)" >&2
    exit 1
  fi
done

DEFAULT_OUTPUT_ROOT="$ROOT_DIR/../_generated"
OUTPUT_ROOT_RAW="${OUTPUT_ROOT:-${OUTPUT_DIR:-$DEFAULT_OUTPUT_ROOT}}"
# trim trailing slash to avoid duplicate path separators
OUTPUT_ROOT="${OUTPUT_ROOT_RAW%/}"
PROJECT_DIR="${PROJECT_DIR:-$OUTPUT_ROOT/$NAME}"

FORCE_FLAG_VALUE="${E2E_FORCE_OUTPUT:-${FORCE_OUTPUT:-${FORCE_GENERATION:-${FORCE:-}}}}"
FORCE_FLAG_NORMALIZED="$(printf '%s' "${FORCE_FLAG_VALUE:-}" | tr '[:upper:]' '[:lower:]')"
case "$FORCE_FLAG_NORMALIZED" in
  1|true|yes|on)
    FORCE_ENABLED=true
    ;;
  *)
    FORCE_ENABLED=false
    ;;
esac

echo "[E2E] Provision project output root: $OUTPUT_ROOT"
mkdir -p "$OUTPUT_ROOT"

if [[ -e "$PROJECT_DIR" && ! -d "$PROJECT_DIR" ]]; then
  echo "[E2E] Project path exists but is not a directory: $PROJECT_DIR" >&2
  exit 1
fi

if [[ -d "$PROJECT_DIR" ]]; then
  if [[ "$FORCE_ENABLED" == true ]]; then
    echo "[E2E] FORCE enabled; cleaning existing project directory $PROJECT_DIR"
    rm -rf "$PROJECT_DIR"
  else
    if [[ -n "$(ls -A "$PROJECT_DIR" 2>/dev/null)" ]]; then
      echo "[E2E] Project directory already exists and is not empty: $PROJECT_DIR" >&2
      echo "      Set FORCE_OUTPUT=1 (or E2E_FORCE_OUTPUT/ FORCE_GENERATION) to overwrite." >&2
      exit 1
    fi
  fi
fi

mkdir -p "$PROJECT_DIR" "$PROJECT_DIR/evidence"
PLAN_PATH="$PROJECT_DIR/PLAN.md"
PLAN_TASKS_PATH="$PROJECT_DIR/PLAN.tasks.json"
TASKS_PATH="$PROJECT_DIR/tasks.json"
SELECTION_PATH="$PROJECT_DIR/selection.json"
SELECTION_SUMMARY="$PROJECT_DIR/evidence/stack-selection.md"

GENERATOR_COMMON_ARGS=(
  --name "$NAME"
  --industry "$INDUSTRY"
  --project-type "$PROJECT_TYPE"
  --frontend "$FE"
  --backend "$BE"
  --database "$DB"
  --auth "${AUTH:-}"
  --deploy "${DEPLOY:-}"
  --workers 8
  --output-dir "$OUTPUT_ROOT"
  --yes
)

if [[ -n "${COMPLIANCE:-}" ]]; then
  GENERATOR_COMMON_ARGS+=(--compliance "$COMPLIANCE")
fi

if [[ "$FORCE_ENABLED" == true ]]; then
  GENERATOR_COMMON_ARGS+=(--force)
fi

echo "[E2E] Bootstrap"
"$PY_BIN" scripts/doctor.py --strict || true
./scripts/generate_client_project.py --list-templates \
  --name "${NAME:-demo}" --industry "${INDUSTRY:-healthcare}" --project-type "${PROJECT_TYPE:-fullstack}" | cat

echo "[E2E] Plan from brief"
"$PY_BIN" scripts/plan_from_brief.py --brief "docs/briefs/${NAME}/brief.md" --out "$PLAN_PATH"

echo "[E2E] Validate tasks graph"
"$PY_BIN" scripts/validate_tasks.py --input "$PLAN_TASKS_PATH"

echo "[E2E] Generate PRD & architecture"
"$PY_BIN" scripts/generate_prd_assets.py \
  --name "$NAME" \
  --plan "$PLAN_PATH" \
  --tasks "$PLAN_TASKS_PATH" \
  --output-dir "$PROJECT_DIR" \
  --frontend "$FE" \
  --backend "$BE" \
  --database "$DB" \
  --auth "${AUTH:-}" \
  --deploy "${DEPLOY:-}" \
  --industry "${INDUSTRY:-}" \
  --project-type "${PROJECT_TYPE:-}"

echo "[E2E] Validate PRD gate"
"$PY_BIN" scripts/validate_prd_gate.py \
  --prd "$PROJECT_DIR/PRD.md" \
  --architecture "$PROJECT_DIR/ARCHITECTURE.md"

echo "[E2E] Preflight selection gate"
selection_cmd=(
  "$PY_BIN" scripts/select_stacks.py
  --industry "$INDUSTRY"
  --project-type "$PROJECT_TYPE"
  --frontend "$FE"
  --backend "$BE"
  --database "$DB"
  --output "$SELECTION_PATH"
  --summary "$SELECTION_SUMMARY"
)

if [[ -n "${COMPLIANCE:-}" ]]; then
  selection_cmd+=(--compliance "$COMPLIANCE")
fi

if [[ -n "${NESTJS_ORM:-}" ]]; then
  selection_cmd+=(--nestjs-orm "$NESTJS_ORM")
fi

ENGINE_SUBSTITUTIONS_CFG="${ENGINE_SUBSTITUTIONS_CFG:-}" 
if [[ -z "$ENGINE_SUBSTITUTIONS_CFG" ]]; then
  ENGINE_SUBSTITUTIONS_CFG="$(read_cfg "$CONFIG_FILE" engine_substitutions || true)"
fi

if [[ -n "$ENGINE_SUBSTITUTIONS_CFG" ]]; then
  selection_cmd+=(--engine-substitutions-json "$ENGINE_SUBSTITUTIONS_CFG")
  echo "[E2E] Engine substitutions from config detected." >&2
fi

if [[ -n "${STACK_ENGINE_SUBSTITUTIONS_FILE:-}" ]]; then
  if [[ -f "$STACK_ENGINE_SUBSTITUTIONS_FILE" ]]; then
    selection_cmd+=(--engine-substitutions-file "$STACK_ENGINE_SUBSTITUTIONS_FILE")
    echo "[E2E] Using engine substitutions file: $STACK_ENGINE_SUBSTITUTIONS_FILE" >&2
  else
    echo "[E2E] STACK_ENGINE_SUBSTITUTIONS_FILE not found: $STACK_ENGINE_SUBSTITUTIONS_FILE" >&2
  fi
fi

ENGINE_SUBSTITUTIONS_ENV="${STACK_ENGINE_SUBSTITUTIONS_JSON:-${ENGINE_SUBSTITUTIONS_JSON:-}}"
if [[ -z "$ENGINE_SUBSTITUTIONS_ENV" ]]; then
  ENGINE_SUBSTITUTIONS_ENV="${STACK_ENGINE_SUBSTITUTIONS:-${ENGINE_SUBSTITUTIONS:-}}"
fi

if [[ -n "$ENGINE_SUBSTITUTIONS_ENV" ]]; then
  trimmed_env="$(printf '%s' "$ENGINE_SUBSTITUTIONS_ENV" | sed -e 's/^\s*//' -e 's/\s*$//')"
  if [[ "${trimmed_env:0:1}" == "{" || "${trimmed_env:0:1}" == "[" ]]; then
    selection_cmd+=(--engine-substitutions-json "$ENGINE_SUBSTITUTIONS_ENV")
  else
    IFS=',' read -r -a _engine_sub_pairs <<< "$ENGINE_SUBSTITUTIONS_ENV"
    for pair in "${_engine_sub_pairs[@]}"; do
      if [[ -n "$pair" ]]; then
        selection_cmd+=(--engine-substitution "$pair")
      fi
    done
    unset _engine_sub_pairs
  fi
  echo "[E2E] Engine substitutions from environment applied." >&2
fi

if ! "${selection_cmd[@]}"; then
  sel_status=$?
  if [[ $sel_status -eq 3 ]]; then
    echo "[E2E] Stack selection failed: unmet engine requirements" >&2
  fi
  exit "$sel_status"
fi

echo "[E2E] Generator dry-run"
./scripts/generate_client_project.py \
  "${GENERATOR_COMMON_ARGS[@]}" \
  --dry-run

echo "[E2E] Generate"
./scripts/generate_client_project.py \
  "${GENERATOR_COMMON_ARGS[@]}"

echo "[E2E] Install & test"
chmod +x scripts/install_and_test.sh
PROJECT_ROOT="$PROJECT_DIR" ./scripts/install_and_test.sh

echo "[E2E] Sync & validate"
"$PY_BIN" scripts/sync_from_scaffold.py --input "$PLAN_TASKS_PATH" --root "$PROJECT_DIR"
"$PY_BIN" scripts/sync_from_scaffold.py --input "$PLAN_TASKS_PATH" --root "$PROJECT_DIR" --output "$TASKS_PATH" --apply
"$PY_BIN" scripts/validate_tasks.py --input "$TASKS_PATH"

echo "[E2E] QC metrics & gates"
PROJECT_ROOT="$PROJECT_DIR" "$PY_BIN" scripts/collect_coverage.py || true
PROJECT_ROOT="$PROJECT_DIR" "$PY_BIN" scripts/collect_perf.py || true
PROJECT_ROOT="$PROJECT_DIR" "$PY_BIN" scripts/scan_deps.py || true
PROJECT_ROOT="$PROJECT_DIR" "$PY_BIN" scripts/enforce_gates.py

echo "[E2E] Build Submission Pack"
chmod +x scripts/build_submission_pack.sh
PROJECT_ROOT="$PROJECT_DIR" NAME="$NAME" ./scripts/build_submission_pack.sh || true

echo "[E2E] Validate compliance assets"
mkdir -p "$PROJECT_DIR/evidence"
compliance_validate_cmd=("$PY_BIN" scripts/validate_compliance_assets.py)
if [[ -n "${VALIDATE_COMPLIANCE_WRITE:-}" ]]; then
  compliance_validate_cmd+=(--write)
fi
if ! "${compliance_validate_cmd[@]}" | tee "$PROJECT_DIR/evidence/validate_compliance_assets.log"; then
  validate_status=${PIPESTATUS[0]}
  echo "[E2E] Compliance asset validation failed." >&2
  exit "${validate_status:-1}"
fi

echo "[E2E] Compliance docs (optional)"
"$PY_BIN" scripts/check_compliance_docs.py || true

echo "[E2E] Done. See $PROJECT_DIR"

