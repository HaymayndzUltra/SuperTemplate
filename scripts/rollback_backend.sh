#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${1:-staging}"
REVISION="${2:-previous}"
APP_NAME="${APP_NAME:-portfolio-dashboard}"
AWS_REGION="${AWS_REGION:?AWS_REGION is required}"
AWS_PROFILE="${AWS_PROFILE:-}"
CLUSTER_NAME="${ECS_CLUSTER_NAME:-${APP_NAME}-${ENVIRONMENT}}"
SERVICE_NAME="${ECS_SERVICE_NAME:-${APP_NAME}-backend}"
FAMILY="${ECS_TASK_FAMILY:-${APP_NAME}-${ENVIRONMENT}}"

AWS_BASE_CMD=(aws --region "${AWS_REGION}")
if [[ -n "${AWS_PROFILE}" ]]; then
  AWS_BASE_CMD+=(--profile "${AWS_PROFILE}")
fi

resolve_revision() {
  local revision="${1}"
  if [[ "${revision}" == "previous" ]]; then
    local listing
    listing="$(${AWS_BASE_CMD[@]} ecs list-task-definitions --family-prefix "${FAMILY}" --sort DESC --max-items 2)"
    python - <<'PY' "${listing}"
import json
import sys
payload = json.loads(sys.argv[1])
defs = payload.get("taskDefinitionArns", [])
if len(defs) < 2:
    raise SystemExit("No previous task definition available for rollback")
print(defs[1])
PY
  else
    if [[ "${revision}" == arn:* ]]; then
      echo "${revision}"
    else
      echo "${FAMILY}:${revision}"
    fi
  fi
}

main() {
  local target
  if ! target="$(resolve_revision "${REVISION}")"; then
    echo "Unable to resolve task definition for revision ${REVISION}" >&2
    exit 1
  fi

  echo "Rolling back ECS service ${SERVICE_NAME} on cluster ${CLUSTER_NAME} to ${target}"
  ${AWS_BASE_CMD[@]} ecs update-service \
    --cluster "${CLUSTER_NAME}" \
    --service "${SERVICE_NAME}" \
    --task-definition "${target}" \
    --force-new-deployment

  echo "Waiting for rollback to stabilize"
  ${AWS_BASE_CMD[@]} ecs wait services-stable --cluster "${CLUSTER_NAME}" --services "${SERVICE_NAME}"
  echo "Rollback completed for ${SERVICE_NAME} (${ENVIRONMENT})"
}

main "$@"
