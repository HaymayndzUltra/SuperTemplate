# Generator: Protocol 12 – Post-Deployment Monitoring & Observability

## 1. Purpose
Instruct AI agents on converting `protocol-input-form-12-monitoring.yaml` into `12-monitoring-observability.md`, producing an SRE-focused protocol that activates and validates observability capabilities after deployment.

## 2. Required Inputs
- Completed `protocol-input-form-12-monitoring.yaml`
- Deployment artifacts: `post-deployment-validation.json`, `deployment-health-log.md`, `DEPLOYMENT-REPORT.md`
- Quality audit references for monitoring requirements
- Script inventory: `collect_perf.py`, `workflow_automation.py`, `aggregate_coverage.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Site Reliability Engineer managing observability
- Guardrail: No completion until alerts/dashboards/runbooks validated against live telemetry
- Dependencies: Protocol 11 outputs, Protocol 12 handoff to Protocols 13, 5, 14

### Layer 2 – Behavioral Control
- Gates: Instrumentation coverage, alert validation, observability assurance, handoff package
- Halt conditions: Telemetry gaps, failed alert tests, missing approvals
- Validation prompts: Alert test activation, monitoring package delivery

### Layer 3 – Procedural Logic
- Phases: Instrumentation alignment → Monitoring activation → Continuous assurance → Handoff & improvement
- Evidence artifacts: Monitoring requirements, instrumentation audit, alert test results, observability schedule, package manifest
- Automation hooks: `collect_perf.py`, `workflow_automation.py`, `aggregate_coverage.py`

### Layer 4 – Communication Grammar
- Phase announcements `[PHASE {N} START]`
- Automation status notifications
- Validation prompts `[VALIDATION REQUEST]`, `[HANDOFF CONFIRMATION]`
- Error messages for instrumentation gaps, alert failures, missing approvals

## 4. Protocol Template Structure
Generated protocol must include:
1. H1 heading with protocol name and compliance domain
2. Section **1. AI ROLE AND MISSION** stating mission and critical guardrail
3. Section **2. MONITORING & OBSERVABILITY WORKFLOW** with four steps aligned to form phases and `[MUST]/[GUIDELINE]` markers
4. Section **3. INTEGRATION POINTS** (inputs from deployment/quality, outputs to incident response/retrospective/performance)
5. Section **4. QUALITY GATES** reflecting gate definitions and failure handling
6. Section **5. COMMUNICATION PROTOCOLS** with announcements, prompts, error handling
7. Section **6. AUTOMATION HOOKS** describing commands and expected outputs
8. Section **7. HANDOFF CHECKLIST** summarizing completion tasks and handoff command

## 5. Automation Hook Guidelines
- Commands must reference `.artifacts/monitoring/` for outputs
- Alert testing should explicitly mention `--workflow alert-test`
- Aggregate coverage command should use `--scope monitoring`

## 6. Quality Acceptance Criteria
- Evidence items correspond to directories defined in form
- Quality gates enforce coverage, alert validation, assurance, handoff
- Communications maintain consistent bracketed format
- Integration points highlight downstream dependencies (Protocols 13, 5, 14)
- No placeholders; runbook updates referenced explicitly

## 7. Generation Workflow for the AI
1. Validate form completeness and artifact references
2. Map each phase to workflow subsections with appropriate `[MUST]/[GUIDELINE]` markers
3. Fill evidence, automation, and communication sections using form data
4. Cross-check gate names/criteria/failure handling with input
5. Insert validation prompts and error handling messages exactly as provided
6. Output markdown file at `.cursor/ai-driven-workflow/12-monitoring-observability.md`

## 8. Output & Post-Generation Actions
- Save protocol to workflow directory
- Suggest running meta-analysis validation
- Encourage synchronizing runbook updates with context kit after generation
