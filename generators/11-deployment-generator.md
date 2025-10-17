# Generator: Protocol 11 – Production Deployment & Release Management

## 1. Purpose
Enable AI agents to convert `protocol-input-form-11-deployment.yaml` into `11-production-deployment.md`, ensuring the deployment protocol enforces readiness checks, controlled release execution, and comprehensive evidence capture.

## 2. Required Inputs
- Completed `protocol-input-form-11-deployment.yaml`
- Upstream artifacts: Protocol 10 staging reports, Protocol 7 validation suite report, Protocol 4 quality audit approvals
- Deployment scripts: `deploy_backend.sh`, `rollback_backend.sh`, service-specific scripts
- Monitoring scripts: `validate_workflows.py`, `collect_perf.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Release Manager coordinating production deployment
- Guardrail: No production deployment without approvals, staging success, rollback plan
- Dependencies: Protocols 7, 10, 4; downstream protocols 12, 13, 5

### Layer 2 – Behavioral Control
- Gates: Readiness confirmation, staging validation, production launch, stabilization
- Halt conditions: Missing artifacts, failed deployment, health degradation
- Validation prompts: Production approval, rollback decision, release completion

### Layer 3 – Procedural Logic
- Phases: Readiness verification → Staging deployment → Production deployment → Release review
- Evidence artifacts: Readiness checklist, staging report, production approval, post-deployment validation, release report
- Automation hooks: `deploy_backend.sh`, `validate_workflows.py`, `collect_perf.py`, `rollback_backend.sh`

### Layer 4 – Communication Grammar
- Phase announcements for each deployment stage
- Automation status messages for each script invocation
- Validation prompts and error messages referencing release context

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading with protocol name and compliance domain
2. Section **1. AI ROLE AND MISSION** with critical guardrail
3. Section **2. DEPLOYMENT WORKFLOW** subdivided into four steps with `[MUST]/[GUIDELINE]` actions, communications, evidence, automation
4. Section **3. INTEGRATION POINTS** describing upstream/downstream artifacts
5. Section **4. QUALITY GATES** listing four gates with criteria, evidence, failure handling
6. Section **5. COMMUNICATION PROTOCOLS** (status announcements, prompts, error handling)
7. Section **6. AUTOMATION HOOKS** detailing scripts and usage
8. Section **7. HANDOFF CHECKLIST** summarizing completion requirements

## 5. Automation Hook Rules
- Provide exact commands with environment flags (staging/production)
- Include fallback instructions for rollback scripts
- Ensure evidence files are stored under `.artifacts/deployment/`

## 6. Quality Acceptance Criteria
- Each workflow step ties to evidence artifacts listed in the form
- Quality gates directly reference readiness, staging, production, stabilization criteria
- Communication templates use bracketed format and align with release process
- Integration points mention Protocols 12, 13, 5 as outputs
- No placeholder text; release report named `DEPLOYMENT-REPORT.md`

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite artifact references
2. Translate form phases to Markdown steps with `[MUST]/[GUIDELINE]`
3. Populate evidence, automation, and communication sections from form data
4. Insert validation prompts (approval, rollback, release completion) exactly as specified
5. Confirm quality gate descriptions align with evidence artifacts
6. Output markdown file at `.cursor/ai-driven-workflow/11-production-deployment.md`

## 8. Output & Post-Generation Actions
- Save protocol to workflow directory
- Recommend running meta-analysis validation
- Advise maintainers to refresh deployment playbooks if scripts or environments change
