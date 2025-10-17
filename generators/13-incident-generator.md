# Generator: Protocol 13 – Incident Response & Rollback

## 1. Purpose
Provide AI agents with instructions to transform `protocol-input-form-13-incident.yaml` into `13-incident-response-rollback.md`, delivering an operations resilience protocol that governs incident mitigation and rollback workflows.

## 2. Required Inputs
- Completed `protocol-input-form-13-incident.yaml`
- Monitoring assets: `monitoring-package-manifest.json`, `alert-test-results.json`, `monitoring-approval-record.json`
- Deployment artifacts: `rollback-plan.md`, `production-deployment-report.json`
- Script availability: `rollback_backend.sh`, `rollback_frontend.sh`, `validate_workflows.py`, `restore_workflows.py`, `retrospective_evidence_report.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Incident Commander managing live incidents
- Guardrail: No rollback without confirmed severity, scope, and stakeholder alignment
- Dependencies: Inputs from Protocols 11 & 12; outputs to Protocol 5 and context kit

### Layer 2 – Behavioral Control
- Gates: Severity alignment, mitigation readiness, recovery validation, resolution & documentation
- Halt conditions: Unconfirmed severity, missing rollback prerequisites, failed recovery validation, incomplete documentation
- Validation prompts: Severity confirmation, mitigation approval, resolution confirmation

### Layer 3 – Procedural Logic
- Phases: Detection & assessment → Containment planning → Execution & verification → Resolution & documentation
- Evidence artifacts: Intake log, severity assessment, mitigation plan, rollback checklist, execution report, recovery validation, incident report
- Automation hooks: rollback scripts, `validate_workflows.py --mode recovery`, `restore_workflows.py`, `retrospective_evidence_report.py`

### Layer 4 – Communication Grammar
- Phase announcements per step
- Automation status messages referencing executed scripts
- Validation prompts `[SEVERITY CONFIRMATION]`, `[MITIGATION APPROVAL]`, `[RESOLUTION CONFIRMATION]`
- Error handling messages for false positives, rollback failures, documentation gaps

## 4. Protocol Template Structure
The generated markdown must include:
1. H1 heading with protocol name and compliance domain
2. Section **1. AI ROLE AND MISSION** with guardrail statement
3. Section **2. INCIDENT RESPONSE WORKFLOW** with four steps aligned to form phases and `[MUST]/[GUIDELINE]` markers
4. Section **3. INTEGRATION POINTS** connecting monitoring, deployment, retrospective, performance, and context kit
5. Section **4. QUALITY GATES** covering severity, mitigation readiness, recovery validation, resolution documentation
6. Section **5. COMMUNICATION PROTOCOLS** (status announcements, prompts, error handling)
7. Section **6. AUTOMATION HOOKS** linking scripts to phases with expected outputs
8. Section **7. HANDOFF CHECKLIST** ensuring closure actions and next protocol reference

## 5. Automation Hook Guidelines
- Specify environment flags for rollback scripts
- Recovery validation must call `validate_workflows.py --mode recovery`
- Evidence outputs must be stored under `.artifacts/incidents/`
- Mention optional retrospective evidence script for postmortem support

## 6. Quality Acceptance Criteria
- Steps must emphasize evidence capture and communication logging
- Quality gates align with form criteria and include failure handling instructions
- Integration points mention Protocols 12, 11 as inputs; Protocol 5 as primary output
- Communications maintain consistent bracket notation and incident terminology
- No placeholder language; incident report referenced as `INCIDENT-REPORT.md`

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite artifacts
2. Convert form phases into Markdown subsections with `[MUST]/[GUIDELINE]` markers
3. Populate evidence, automation, integration, and communication sections using form data
4. Insert validation prompts and error handling exactly as provided
5. Confirm quality gates reference correct evidence artifacts
6. Output markdown file at `.cursor/ai-driven-workflow/13-incident-response-rollback.md`

## 8. Output & Post-Generation Actions
- Save protocol to workflow directory
- Recommend meta-analysis validation to confirm structural compliance
- Notify governance team to update incident runbooks and context kit with new instructions
