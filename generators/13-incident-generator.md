# Protocol 13 Generator Instructions — Incident Response & Rollback

## 1. Goal
Produce `.cursor/ai-driven-workflow/13-incident-response-rollback.md` from `protocol-input-form-13-incident.yaml`, ensuring the incident command workflow aligns with resilience governance standards.

## 2. Source Requirements
- Filled YAML form for Protocol 13.
- Awareness of upstream artifacts from Protocols 11 & 12 for integration references.
- Retrospective and backlog links (Protocols 5 and 2) for outputs.

## 3. Output Blueprint
- Title suffix: `(Resilience Governance Compliant)`.
- Sections: Role/Mission, Incident Response Workflow, Integration Points, Quality Gates, Communication Protocols, Handoff Checklist.
- Workflow must contain three phases with numbered steps and `[MUST]` emphasis where indicated.

## 4. Layer Alignment Table
| Layer | Source | Implementation Guidance |
|-------|--------|-------------------------|
| L1 | `ai_role`, `purpose`, `primary_guardrail` | Mission must highlight authorization before mitigation. |
| L2 | `quality_gate`, `halt_condition` | Render Intake, Mitigation Execution, Post-Incident Closure gates with failure handling referencing telemetry, SME escalation, and communications. |
| L3 | `phases.steps`, `evidence_collection`, `automation_hooks` | Document activation, mitigation, recovery, and postmortem steps including automation commands (`run_rollback.py`). |
| L4 | `communication_template`, `outputs_to`, `error handling` | Provide status announcements, validation prompts, error codes (TelemetryMissing, RollbackFailure, PostmortemDelay). |

## 5. Rendering Directives
- Evidence bullets must use `.artifacts/incidents/...` paths.
- Automation commands displayed inline for mitigation step.
- Halt conditions: convert to bullet lines starting `* **Halt condition:**` when present.
- Communication code block should include six lines (start/complete for each phase).
- Validation prompts ask for approval before mitigation and before closure.

## 6. Integration & Outputs
- Inputs: cite Protocol 12 telemetry artifacts and Protocol 11 rollback report exactly as in the form.
- Outputs: mention Protocol 5 retrospective and Protocol 2 backlog updates with file names from the form.

## 7. Quality Checklist
- [ ] Guardrail mentions authorization before mitigation/rollback.
- [ ] Mitigation phase includes automation command `python scripts/incidents/run_rollback.py ...`.
- [ ] Quality gates labelled `Incident Intake Gate`, `Mitigation Execution Gate`, `Post-Incident Closure Gate`.
- [ ] Error handling section covers TelemetryMissing, RollbackFailure, PostmortemDelay.
- [ ] Handoff checklist contains five items concluding with completion message referencing Protocol 5.

## 8. Circular Validation Notes
- Ensure meta-analysis can trace artifact flow `.artifacts/incidents/` to Protocol 5/2 outputs.
- Verify communication grammar uses `[PHASE N START]` and `[PHASE N COMPLETE]` lines.
- Maintain consistent numbering and indentation to support ASCII diagrams during validation.
