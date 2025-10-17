# Protocol 13 Generator - Incident Response & Rollback

## 🎯 Purpose
Generate `.cursor/ai-driven-workflow/13-incident-response-rollback.md` from `protocol-input-form-13-incident.yaml`. The protocol must codify detection, triage, mitigation, and post-incident learning with strict rollback governance.

## 📥 Required Inputs
- Completed `protocol-input-form-13-incident.yaml`
- Monitoring handoff artifacts from Protocol 12
- Release and rollback assets from Protocol 11
- Access to incident automation scripts (`workflow_automation.py`, rollback scripts, validate_workflow_integration.py`)

## 🧠 4-Layer Mapping Blueprint
1. **Layer 1 – System-Level Decisions**
   - Persona: Incident Commander orchestrating response lifecycle
   - Guardrail: Incident cannot close without validated RCA and rollback verification
   - Dependencies: Monitoring handoff + deployment evidence
2. **Layer 2 – Behavioral Control**
   - Gates: Triage Confirmation, Stabilization, Incident Closure
   - Halt conditions: missing monitoring artifacts, rollback readiness not confirmed, restoration metrics failing
   - Decision prompts: rollback confirmation, incident closure approval
3. **Layer 3 – Procedural Logic**
   - Phases: Detection & Triage → Containment & Mitigation → Recovery & Post-Incident Analysis
   - Evidence: incident record, timeline, mitigation logs, RCA, post-incident report
   - Automation: workflow_automation incident template, rollback scripts, validate_workflow_integration (incident mode)
4. **Layer 4 – Communication Grammar**
   - Phase start/complete announcements
   - Prompts for rollback execution and closure
   - Error templates (MissingMonitoringArtifacts, RollbackFailure, RCAIncomplete) with recovery steps

## 🏗️ Template Blueprint
```
# PROTOCOL 13: INCIDENT RESPONSE & ROLLBACK (OPERATIONS COMPLIANT)

## 1. AI ROLE AND MISSION
[Persona + mission + guardrail]

## 2. INCIDENT RESPONSE WORKFLOW
### STEP 1: Detection & Triage
[Incident record creation, team assembly, impact assessment]

### STEP 2: Containment & Mitigation
[Containment actions, rollback/hotfix execution, communications]

### STEP 3: Recovery & Post-Incident Analysis
[Service restoration validation, RCA, post-incident report]

## 3. INTEGRATION POINTS
[Inputs from Protocols 12 & 11; outputs to 5, 6, 7]

## 4. QUALITY GATES
[Triage Confirmation Gate, Stabilization Gate, Incident Closure Gate]

## 5. COMMUNICATION PROTOCOLS
[Announcements, validation prompts, error handling]

## 6. AUTOMATION HOOKS
[workflow_automation incident, rollback scripts, validate_workflow_integration]

## 7. HANDOFF CHECKLIST
[Checklist + completion command routing to Protocol 5]
```
- Highlight evidence directories `.artifacts/incidents/` for each artifact.
- Emphasize conditional rollback execution and stakeholder communications.

## 🤖 Automation & Evidence Integration
- Describe outputs for each automation hook and their role in evidence capture.
- Mention optional dual rollback commands (backend & frontend) with logs.
- Ensure mitigation evidence aligns with stabilization gate requirements.

## ✅ Quality Acceptance Checklist
**Structural**
- [ ] Header, section ordering, and numbering comply with workflow conventions
- [ ] Steps include `[MUST]`/`[GUIDELINE]` markers and communication templates
- [ ] Halt conditions defined for mandatory steps

**Content**
- [ ] Integration points map to Protocols 12, 11, 5, 6, and 7 with artifact names
- [ ] Evidence collection lists match form-specified files under `.artifacts/incidents/`
- [ ] Error handling covers monitoring gaps, rollback failures, and incomplete RCA
- [ ] Quality gates provide criteria, evidence, and failure handling

**Validation**
- [ ] Handoff checklist mentions RCA, post-incident report, corrective actions
- [ ] Completion command routes to Protocol 5
- [ ] Communication prompts include rollback confirmation and closure check

## 🔁 Circular Validation Workflow
1. Generate protocol file and save to `.cursor/ai-driven-workflow/13-incident-response-rollback.md`.
2. Run Meta-Analysis Generator to confirm four-layer representation (mission, gates, procedures, communications).
3. If gaps detected (e.g., missing mitigation evidence), refine protocol and re-run analysis.

## ⚠️ Failure Handling Guidance
- **Missing prerequisites** → Request monitoring handoff or deployment evidence before generation.
- **Rollback script discrepancies** → Validate script names/paths; adjust if front/back-end scripts differ per project.
- **Gate ambiguity** → Clarify success criteria (e.g., “alerts cleared”, “rollback log success”).
- **Communication omissions** → Add explicit prompts for stakeholder updates and closure confirmations.
