# Protocol 12 Generator Instructions — Post-Deployment Monitoring & Observability

## 1. Purpose
Translate `protocol-input-form-12-monitoring.yaml` into `.cursor/ai-driven-workflow/12-monitoring-observability.md`, ensuring SRE workflows follow governor communication and evidence standards.

## 2. Input Dependencies
- Form file for protocol 12.
- References to deployment outputs (monitoring handoff package, release logs) for integration accuracy.
- Knowledge of incident response protocol numbering (Protocol 13) for downstream links.

## 3. Output Layout Checklist
- Title includes `(Reliability Governance Compliant)`.
- Six sections: Role & Mission, Workflow, Integration Points, Quality Gates, Communication Protocols, Handoff Checklist.
- Workflow must present three phases exactly as in the form with nested numbered steps.

## 4. Mapping the Four Layers
| Layer | Data | Implementation Notes |
|-------|------|----------------------|
| L1 | `ai_role`, `purpose`, `primary_guardrail` | Compose mission statement referencing dashboards/alerts sign-off. |
| L2 | `quality_gate`, `halt_condition`, `prerequisites` | Render Observability Coverage, Telemetry Validation, Monitoring Readiness gates with evidence & failure handling. |
| L3 | `phases.steps`, `evidence_collection`, `automation_hooks` | Provide instrumentation steps, automation commands, evidence storage paths. |
| L4 | `communication_template`, `outputs_to`, `inputs_from` | Build status messages, validation prompts, error handling, and checklist narrative. |

## 5. Rendering Guidance
- Include automation commands `validate_ingestion.py`, `synth_check_runner.py`, `generate_slo_review.py` within relevant steps.
- Evidence bullet lines should match `.artifacts/monitoring/...` paths verbatim.
- Update runbook step should reference `.cursor/context-kit/monitoring-runbook.md`.
- Communication block requires start/complete lines for each phase.
- Validation prompts: telemetry ingestion approval and monitoring readiness approval.

## 6. Integration Section
- Inputs: Protocol 11 artifacts plus architecture guardrails when referenced.
- Outputs: Protocol 13 artifacts and retrospective notes; ensure file extensions match YAML form.

## 7. Quality Checklist
- [ ] Guardrail warns against declaring monitoring complete before validation.
- [ ] Three quality gates named exactly as in the form.
- [ ] Error handling items cover MissingHandoff, TelemetryGap, SLOFailure.
- [ ] Handoff checklist includes five bullet items culminating in readiness message for Protocol 13.
- [ ] Status announcements mention observability alignment, telemetry validation, SLO review.

## 8. Circular Validation Notes
- Ensure meta-analysis can identify SLO review artifacts for incident response integration.
- Confirm evidence references appear in both Workflow and Quality Gates for redundancy.
- Keep markdown free of trailing spaces and maintain numbering continuity.
