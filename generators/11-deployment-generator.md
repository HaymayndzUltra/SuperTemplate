# Generator Playbook: Protocol 11 – Production Deployment & Release Management

## 1. Mission Alignment
- **Goal:** Create `11-production-deployment-release-management.md` orchestrating release readiness, deployment, and stabilization.
- **Input Sources:** `generators/protocol-input-form-11-deployment.yaml`, artifacts from Protocols 10, 04, 09, and outputs to Protocol 12.
- **Critical Guardrail:** Highlight explicit go-live approval requirement and rollback readiness.

## 2. 4-Layer Architecture Mapping
| Layer | Focus Elements |
|-------|----------------|
| **L1** | Release Manager persona, mission, CRITICAL approval guardrail |
| **L2** | Gates: Release Authorization, Production Deployment, Stabilization & Handoff; halt conditions for approvals |
| **L3** | Three phases covering readiness, execution, stabilization with evidence, telemetry, automation |
| **L4** | Communication templates for approvals, status, error handling |

## 3. Template Blueprint
1. Title heading with numbering and compliance.
2. `## 1. AI ROLE AND MISSION`.
3. `## 2. RELEASE MANAGEMENT WORKFLOW` with 3 `### STEP` sections.
   - Each step lists `[MUST]` actions with Action/Communication/Halt bullets; `[GUIDELINE]` for optional tasks.
   - Provide Evidence Collection list and Quality Gate statement per phase.
4. Integration points referencing Protocols 10/04/09 inputs and Protocols 12/05 outputs.
5. Quality gates summarizing criteria/evidence/failure handling.
6. Communication protocols with fenced blocks for status + prompts; include `[APPROVAL REQUEST]` per form.
7. Handoff checklist linking to Protocol 12.

## 4. Automation & Telemetry Requirements
- Mention `release_gatekeeper.py`, `deployment_executor.py`, `stabilization_monitor.py` in automation context.
- Evidence files stored under `.artifacts/deployment/`.
- Ensure telemetry handoff to Protocol 12.

## 5. Acceptance Criteria
- All MUST steps from form reflected verbatim.
- Release Authorization gate includes approvals and rollback plan references.
- Approval prompt text matches `[APPROVAL REQUEST]` string.
- Evidence lists include readiness checklist, deployment reports, telemetry.
- Error handling covers MissingApproval, DeploymentFailure, HealthDegradation.

## 6. Validation Checklist
- [ ] Guardrail present and bolded with `[CRITICAL]` marker.
- [ ] Three phases each include evidence collection + quality gate.
- [ ] Integration section explicitly mentions Protocols 10, 04/09 inputs and 12, 05 outputs.
- [ ] Quality gate names consistent across sections.
- [ ] Communication section uses fenced code blocks.
- [ ] Handoff checklist references Protocol 12.
