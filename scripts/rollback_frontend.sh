#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${1:-staging}"
TARGET="${2:-}"
TOKEN="${VERCEL_TOKEN:?VERCEL_TOKEN must be exported for frontend rollback}"
SCOPE_FLAG=()
if [[ -n "${VERCEL_ORG_ID:-}" ]]; then
  SCOPE_FLAG=(--scope "${VERCEL_ORG_ID}")
fi

if [[ -z "${TARGET}" ]]; then
  # Allow environment specific overrides such as VERCEL_ROLLBACK_TARGET_STAGING
  UPPER_ENV=${ENVIRONMENT^^}
  TARGET_VAR="VERCEL_ROLLBACK_TARGET_${UPPER_ENV}"
  TARGET="${!TARGET_VAR:-${VERCEL_ROLLBACK_TARGET:-}}"
fi

if [[ -z "${TARGET}" ]]; then
  echo "A deployment identifier or alias must be provided for rollback" >&2
  exit 1
fi

echo "Rolling back Vercel deployment ${TARGET} for ${ENVIRONMENT}"
npx vercel rollback "${TARGET}" --token "${TOKEN}" --yes "${SCOPE_FLAG[@]}"
echo "Frontend rollback triggered"
