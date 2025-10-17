#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${1:-staging}"
APP_NAME="${APP_NAME:-portfolio-dashboard}"
AWS_REGION="${AWS_REGION:?AWS_REGION is required}"
AWS_PROFILE="${AWS_PROFILE:-}"
BACKEND_IMAGE="${BACKEND_IMAGE:?BACKEND_IMAGE is required}"
TEMPLATE_PATH="${TASK_DEFINITION_TEMPLATE:-deploy/aws/task-definition.json}"
CLUSTER_NAME="${ECS_CLUSTER_NAME:-${APP_NAME}-${ENVIRONMENT}}"
SERVICE_NAME="${ECS_SERVICE_NAME:-${APP_NAME}-backend}"
DESIRED_COUNT="${ECS_DESIRED_COUNT:-1}"

AWS_BASE_CMD=(aws --region "${AWS_REGION}")
if [[ -n "${AWS_PROFILE}" ]]; then
  AWS_BASE_CMD+=(--profile "${AWS_PROFILE}")
fi

register_task_definition() {
  local template="${1}"
  local image="${2}"
  local environment="${3}"
  local family="${4}"

  if [[ ! -f "${template}" ]]; then
    echo "No task definition template found at ${template}; skipping registration" >&2
    return 0
  fi

  if [[ -z "${TASK_EXECUTION_ROLE_ARN:-}" ]] || [[ -z "${TASK_ROLE_ARN:-}" ]]; then
    echo "TASK_EXECUTION_ROLE_ARN and TASK_ROLE_ARN must be set to register a new task definition. Skipping registration." >&2
    return 0
  fi

  local rendered
rendered=$(python - "$template" "$image" "$environment" "$family" "$AWS_REGION" <<'PY'
import json
import os
import sys
from pathlib import Path

template_path = Path(sys.argv[1])
image = sys.argv[2]
environment = sys.argv[3]
family = sys.argv[4]
execution_role = os.environ["TASK_EXECUTION_ROLE_ARN"]
task_role = os.environ["TASK_ROLE_ARN"]
aws_region = sys.argv[5]

raw = template_path.read_text(encoding="utf-8")
raw = raw.replace("__CONTAINER_IMAGE__", image)
raw = raw.replace("__ENVIRONMENT__", environment)
raw = raw.replace("__TASK_FAMILY__", family)
raw = raw.replace("__TASK_EXECUTION_ROLE_ARN__", execution_role)
raw = raw.replace("__TASK_ROLE_ARN__", task_role)
raw = raw.replace("__AWS_REGION__", aws_region)

data = json.loads(raw)
print(json.dumps(data))
PY
)

  local tmp_file
  tmp_file=$(mktemp)
  echo "${rendered}" > "${tmp_file}"
  echo "Registering task definition family ${family}"
  local output
  if ! output="$(${AWS_BASE_CMD[@]} ecs register-task-definition --cli-input-json "file://${tmp_file}")"; then
    echo "Failed to register task definition" >&2
    rm -f "${tmp_file}"
    return 1
  fi
  rm -f "${tmp_file}"
  python - <<'PY' "${output}"
import json
import sys
payload = json.loads(sys.argv[1])
print(payload["taskDefinition"]["taskDefinitionArn"])
PY
}

main() {
  local family="${ECS_TASK_FAMILY:-${APP_NAME}-${ENVIRONMENT}}"
  local new_td=""
  if new_td=$(register_task_definition "${TEMPLATE_PATH}" "${BACKEND_IMAGE}" "${ENVIRONMENT}" "${family}"); then
    if [[ -n "${new_td}" ]]; then
      echo "Registered new task definition: ${new_td}"
      TD_ARG=(--task-definition "${new_td}")
    else
      TD_ARG=()
    fi
  else
    echo "Task definition registration failed" >&2
    exit 1
  fi

  echo "Updating ECS service ${SERVICE_NAME} on cluster ${CLUSTER_NAME}"
  if [[ ${#TD_ARG[@]} -gt 0 ]]; then
    ${AWS_BASE_CMD[@]} ecs update-service \
      --cluster "${CLUSTER_NAME}" \
      --service "${SERVICE_NAME}" \
      --desired-count "${DESIRED_COUNT}" \
      --force-new-deployment \
      "${TD_ARG[@]}"
  else
    ${AWS_BASE_CMD[@]} ecs update-service \
      --cluster "${CLUSTER_NAME}" \
      --service "${SERVICE_NAME}" \
      --desired-count "${DESIRED_COUNT}" \
      --force-new-deployment
  fi

  echo "Waiting for service stability"
  ${AWS_BASE_CMD[@]} ecs wait services-stable --cluster "${CLUSTER_NAME}" --services "${SERVICE_NAME}"
  echo "Backend deployment completed for ${ENVIRONMENT}"
}

main "$@"
