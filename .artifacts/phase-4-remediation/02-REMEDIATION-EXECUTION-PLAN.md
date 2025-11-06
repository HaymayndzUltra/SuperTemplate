# Phase 4 Remediation Execution Plan

## 1. Objectives
- Eliminate **all FAIL** statuses in cognitive reasoning, meta-reflection, and master validation summaries.
- Lift every validator’s **average score to ≥ 0.90**.
- Align updated protocol content with governance gates (`gates_config.yaml`) and roadmap (`plano.md`).

## 2. Workstream Breakdown & Acceptance Criteria

| Workstream | Description | Acceptance Criteria | Evidence |
| --- | --- | --- | --- |
| R1 – Protocol 01 Rehabilitation | Rewrite Protocol 01 workflow, quality gates, evidence, and handoff sections to reintroduce explicit reasoning logic and planning | 1. Protocol 01 score ≥ 0.90 in both reasoning and reflection validators<br>2. No FAIL/WARN items for Protocol 01 in master summary | Updated markdown diff<br>Validator outputs @.artifacts/validation/*protocol-01*.json |
| R2 – Reasoning Pattern Uplift | Inject named patterns, decision criteria, and mitigation logging into all FAIL/WARN protocols (reasoning validator) | 1. All protocols show `status: pass` in cognitive reasoning summary<br>2. Reasoning dimension averages ≥ 0.90 | `protocol_reasoning-summary.json` with zero FAIL/WARN |
| R3 – Future Planning Enhancements | Add roadmap, priority, resource, and timeline bullets where future planning dimension flagged WARN/FAIL | 1. Future planning dimension average ≥ 0.90<br>2. No protocols flagged WARN/FAIL for reflection validator | `protocol_reflection-summary.json` with zero WARN/FAIL |
| R4 – Governance Alignment | Document enforcement linkage between updated protocols and `gates_config.yaml` thresholds; update registry if new scripts introduced | 1. Governance note added to each touched protocol referencing lint/security/coverage thresholds<br>2. `script-registry.json` stays consistent (no missing scripts)<br>3. Governance summary committed to `.artifacts/phase-4-remediation/03-GOVERNANCE-NOTES.md` | Governance notes file + diff against registry |
| R5 – Validation Tracker & Reporting | Maintain per-protocol remediation tracker and summarize uplift after reruns | 1. `02-VALIDATION-TRACKER.md` records pre/post scores with status column<br>2. Final uplift summary shared in `.artifacts/phase-4-remediation/04-UPLIFT-SUMMARY.md` | Tracker & summary files |
| R6 – Final Validator Reruns | Execute reasoning, reflection, and master orchestrator scripts post-remediation | 1. All three summaries show **zero FAIL** and per-validator averages ≥ 0.90<br>2. CLI runs exit with status code 0 | Fresh JSON summaries + terminal logs |

## 3. Dependencies & Sequence
1. Complete R1 before R2–R3 (Protocol 01 content is foundation sample).
2. R4 runs parallel with R2–R3 but must finish before R6.
3. R5 updates continuously while R1–R4 execute; finalize after R6.

## 4. Communication Cadence
- Daily remediation checkpoint logged in tracker.
- Notify governance board once R6 acceptance criteria met.

## 5. Rollback Strategy
- Back up modified protocol files in `.artifacts/phase-4-remediation/backups/` prior to edits.
- If validator rerun introduces new FAIL, revert latest change and reassess dimension-specific guidance.
