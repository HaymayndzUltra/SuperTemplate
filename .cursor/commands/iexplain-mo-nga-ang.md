---
title: "Protocol Verification Meta-Instructions (v2)"
version: "2025-10-21"
checksum_required: true
---

## 0. Execution Controls
1. Abort on missing inputs, malformed Markdown, or unreadable artifacts.
2. Record `execution_id`, timestamp, tool versions; include in report.

## 1. Required Inputs
- `protocol_path`
- `expected_inputs[]`
- `expected_outputs[]`
- `workspace_root`
- Optional: `prev_protocol_path`, `next_protocol_path`

## 2. Multi-Layer Validation
### 2.1 Syntactic Pass
- Parse Markdown via AST.
- Check numbering, heading hierarchy, fenced blocks.
- Emit `syntax_checks` entries with pass/fail and evidence.

### 2.2 Semantic Pass
- For each instruction: extract verb/actor/object, classify (`Action|Decision|Validation|Documentation`), rate clarity with rubric and justification.
- For artifacts: cross-reference expected lists, verify existence, capture `sha256`, size, schema compliance.
- For gates: classify (`AI_AUTOMATED|HUMAN_APPROVAL|CONDITIONAL_BRANCH`), require measurable criterion, log parsed metric.

### 2.3 Contextual Pass
- Compare adjacent protocol artifacts for format alignment.
- Reconcile instructions with `config/protocol_gates/XX.yaml`.
- Check consistency against `.artifacts/scripts/script-index.json`.

## 3. Deviation Detection
- Maintain `issues` array with severity (`critical|major|minor`), evidence, remediation hint.
- Auto-raise `critical` when syntactic or artifact checks fail.

## 4. JSON Output Schema
```json
{
  "execution_id": "<uuid>",
  "protocol_id": "<string>",
  "file_path": "<string>",
  "syntax_checks": [...],
  "step_analysis": [...],
  "artifact_verification": {...},
  "gate_analysis": [...],
  "context_alignment": {
    "previous_protocol": {...},
    "next_protocol": {...},
    "gate_config": {...},
    "script_registry": {...}
  },
  "issues": [...],
  "recommendations": [...],
  "evidence_manifest": [
    {"type": "file_hash", "path": "<rel_path>", "sha256": "<hash>"}
  ]
}

5. Compliance Guardrails
Reject run if JSON fails schema (documentation/sample-manifests/protocol-verification.schema.json).
Compute checksum diff versus prior execution; include machine-readable delta.
Persist report into documentation/pr-reviews/<execution_id>.json and append summary to documentation/MASTER-VALIDATOR-COMPLETE-SPEC.md.
6. Post-Execution Duties
Summarize critical issues with remediation order.
Trigger telemetry via scripts/emit_gate_violation.py when blockers appear.
