# Generator: Protocol 10 – Pre-Deployment Validation & Staging Readiness

## 1. Purpose
Provide AI agents with instructions to convert `protocol-input-form-10-staging.yaml` into `10-pre-deployment-staging.md`, ensuring staging rehearsals, rollback readiness, and security validation are documented before production deployment.

## 2. Required Inputs
- Completed `protocol-input-form-10-staging.yaml`
- Upstream artifacts: Protocol 4 quality audit approvals, Protocol 9 integration evidence, Protocol 7 environment baselines
- Deployment automation scripts: `scripts/deploy_backend.sh`, `scripts/rollback_backend.sh`, service-specific deployers
- Validation scripts: `scripts/compare_environments.py`, `scripts/run_smoke_tests.py`, `scripts/run_security_audit.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Release Engineer safeguarding production readiness
- Guardrail: No go/no-go package without staging success, rollback rehearsal, and approvals
- Dependencies: Inputs from Protocols 4, 9, 7; outputs to Protocols 11, 12, 13

### Layer 2 – Behavioral Control
- Gates: Intake confirmation, deployment rehearsal, rollback & security, readiness approval
- Halt conditions: Missing approvals, parity drift, rehearsal failures, security blockers
- Prompts: Drift alert remediation, readiness review approval

### Layer 3 – Procedural Logic
- Phases: Intake validation → Deployment rehearsal → Rollback & security → Final readiness review
- Evidence: Intake report, parity report, deployment log, test results, rollback verification, security report, manifest, approvals
- Automation: Environment comparison, staging deploy script, smoke tests, rollback scripts, security audit

### Layer 4 – Communication Grammar
- Status announcements for each phase
- Automation status messages for environment compare, smoke tests, rollback
- Error handling for parity mismatch, rehearsal failure, security blocker

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 10: ... (RELEASE COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail
3. Section **2. PRE-DEPLOYMENT WORKFLOW** containing four steps aligned with form phases and `[MUST]/[GUIDELINE]` actions
4. Section **3. INTEGRATION POINTS** enumerating inputs (Protocols 4,9,7) and outputs (Protocols 11,12,13)
5. Section **4. QUALITY GATES** covering Intake Confirmation, Deployment Rehearsal, Rollback & Security, Readiness Approval
6. Section **5. COMMUNICATION PROTOCOLS** with status announcements, validation prompts, error handling entries
7. Section **6. AUTOMATION HOOKS** referencing compare, deploy, smoke test, rollback, and security scripts
8. Section **7. HANDOFF CHECKLIST** matching completion items from form

## 5. Automation Hook Rules
- Provide commands with environment flags (e.g., `--env staging`, `--target production`)
- All evidence stored under `.artifacts/pre-deployment/`
- Mention that deploy/rollback scripts may have service-specific variants; instruct AI to note this in `[GUIDELINE]` actions when applicable

## 6. Quality Acceptance Criteria
- Every `[MUST]` action references a concrete evidence artifact
- Quality gates cite exact filenames from the form
- Communication prompts retain `[DRIFT ALERT]` and `[READINESS REVIEW]` phrasing
- Integration outputs include `PRE-DEPLOYMENT-PACKAGE.zip`, `pre-deployment-manifest.json`, `readiness-approval.json`
- Guardrail text matches form statement about staging/rollback success before approvals

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite references
2. Translate each phase into Markdown with ordered steps using `[MUST]/[GUIDELINE]`
3. Populate integration and quality gate sections from structured form data
4. Insert communication templates and error handling exactly as specified
5. Confirm automation hooks mention all scripts listed in the form
6. Save output to `.cursor/ai-driven-workflow/10-pre-deployment-staging.md`

## 8. Output & Post-Generation Actions
- Encourage running staging rehearsal logs through QA review before production
- Recommend meta-analysis validation for circular compliance
- Prompt teams to notify Protocol 11 owner once readiness approval is archived
