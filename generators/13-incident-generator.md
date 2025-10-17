# Generator Playbook: Protocol 13 – Incident Response & Rollback

## 1. Mission Alignment
- **Goal:** Generate `13-incident-response-rollback.md` covering detection, mitigation, and postmortem activities.
- **Inputs:** `generators/protocol-input-form-13-incident.yaml`, artifacts from Protocols 12 & 11.
- **Guardrail Highlight:** Emphasize prohibition on closing incidents without RCA and action assignments.

## 2. 4-Layer Architecture Mapping
| Layer | Key Elements |
|-------|--------------|
| **L1** | Incident Commander persona, mission, CRITICAL guardrail |
| **L2** | Gates for Incident Confirmation, Containment & Recovery, Postmortem Completion |
| **L3** | Procedural steps for detection, mitigation/rollback, RCA & communication with evidence capture |
| **L4** | Status announcements, validation prompts, error handling messages |

## 3. Template Blueprint
- Follow standard numbering (Sections 1–6).
- Section 2 should include three `### STEP` phases.
- Each phase must list `[MUST]` actions with Action/Communication entries and `[GUIDELINE]` optional steps.
- Provide Evidence Collection bullet list and Quality Gate description within each phase.
- Integration section references inputs from Protocols 12 & 11, outputs to Protocols 05 & 02.
- Communication section includes fenced code block for announcements/prompts and bullet list for errors.

## 4. Automation & Documentation
- Mention automation scripts: `incident_bridge.py`, `rollback_executor.py`, `postmortem_compiler.py` when relevant.
- Evidence directories use `.artifacts/incidents/` plus `.artifacts/deployment/` for rollback references.
- Ensure outputs feed retrospective and backlog updates.

## 5. Acceptance Criteria
- All MUST steps from form explicitly included.
- Evidence collection lists include trigger report, mitigation log, postmortem artifacts.
- Quality gate names identical in Section 2 and Section 4.
- Error handling covers FalsePositive, MitigationFailure, IncompletePostmortem.
- Handoff checklist references Protocol 05 and Protocol 02 outputs.

## 6. Validation Checklist
- [ ] Guardrail bolded with `[CRITICAL]` statement.
- [ ] Integration section contains both inputs and outputs with protocol numbers.
- [ ] Communication prompts exactly match validation requests defined in form.
- [ ] Checklist ensures follow-up tasks handed to downstream protocols.
- [ ] Evidence paths valid (`.artifacts/incidents/`).
