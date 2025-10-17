#!/usr/bin/env bash
set -euo pipefail

# build_submission_pack.sh
# Assemble dist/<NAME>-submission with manifest, SUBMISSION.md, checksums, and evidence copies.

if [[ -n "${PROJECT_ROOT:-}" ]]; then
  ROOT_DIR="$PROJECT_ROOT"
else
  ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
fi
cd "$ROOT_DIR"

NAME="${NAME:-$(jq -r .name workflow.config.json 2>/dev/null || echo project)}"
OUT_DIR="dist/${NAME}-submission"

mkdir -p "$OUT_DIR" "$OUT_DIR/opa" "$OUT_DIR/evidence"

# Manifest skeleton
cat >"$OUT_DIR/manifest.json" <<JSON
{
  "name": "${NAME}",
  "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "artifacts": [
    "SUBMISSION.md",
    "CHECKSUMS.sha256"
  ]
}
JSON

# Submission summary
cat >"$OUT_DIR/SUBMISSION.md" <<'MD'
# Submission Pack

## Contents
- manifest.json
- CHECKSUMS.sha256
- evidence/*

## Notes
- Generated automatically from workflow pipeline.
MD

# Copy evidence if exists
rsync -a --delete --ignore-missing-args evidence/ "$OUT_DIR/evidence/" 2>/dev/null || true

# Checksums
( cd "$OUT_DIR" && find . -type f ! -name CHECKSUMS.sha256 -print0 | xargs -0 sha256sum > CHECKSUMS.sha256 )

echo "[SUBMISSION] Pack created at $OUT_DIR"
