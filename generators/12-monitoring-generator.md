# Generator Playbook: Protocol 12 – Post-Deployment Monitoring & Observability

## 1. Mission Alignment
- **Goal:** Produce `12-post-deployment-monitoring-observability.md` for SRE-driven monitoring activation.
- **Inputs:** `generators/protocol-input-form-12-monitoring.yaml`, telemetry from Protocol 11, instrumentation references from Protocols 06 & 07.
- **Guardrail Emphasis:** Alerts cannot be silenced without approval; maintain linkage to incident response.

## 2. 4-Layer Architecture Mapping
| Layer | Required Output |
|-------|-----------------|
| **L1** | SRE persona, mission, CRITICAL guardrail |
| **L2** | Observability Coverage, Alert Readiness, Monitoring Stability gates with halt conditions |
| **L3** | Three-phase workflow with instrumentation, alerting, monitoring session steps and evidence |
| **L4** | Status announcements, validation prompts, error handling codes |

## 3. Template Blueprint
- Use standard protocol heading/section numbering (1–6).
- Section 2 should include three `### STEP` subsections reflecting enablement, alerting, monitoring.
- Each phase requires Evidence Collection list and Quality Gate paragraph.
- Integration section must call out inputs from Protocol 11 and outputs to Protocol 13 & 05.
- Communication section must include fenced blocks for announcements/prompts and bullet list for errors.

## 4. Automation & Evidence Guidance
- Mention `observability_validator.py`, `alert_tester.py`, `monitoring_session_recorder.py` when referencing automation.
- Evidence stored under `.artifacts/monitoring/` except cross-protocol outputs.
- Connect monitoring outputs to incident response triggers explicitly.

## 5. Acceptance Criteria
- All MUST steps from form represented; each `[MUST]` includes Action + Communication.
- SLO register, alert policy, synthetic results present in evidence lists.
- Quality gate names identical in phases and Section 4.
- Error handling includes MissingTelemetry, AlertRoutingFailure, UnresolvedAnomaly.
- Handoff checklist states readiness for Protocol 13.

## 6. Validation Checklist
- [ ] Guardrail bolded with `[CRITICAL]` and phrased as prohibition on silencing alerts.
- [ ] Evidence paths use `.artifacts/monitoring/`.
- [ ] Outputs mention Protocol 13 and Protocol 05.
- [ ] Communication prompts match template strings.
- [ ] Checklist references incident escalation when needed.
