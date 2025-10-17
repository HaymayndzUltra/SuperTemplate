# Generator: Protocol 17 – Project Closure & Handover

## 1. Purpose
Instruct AI agents to convert `protocol-input-form-17-closure.yaml` into `17-project-closure.md`, ensuring closure readiness, stakeholder alignment, approval capture, and transition confirmation are documented with enforceable gates.

## 2. Required Inputs
- Completed `protocol-input-form-17-closure.yaml`
- Upstream artifacts: Retrospective actions (Protocol 5), staging/deployment evidence (Protocols 10–11), operational outputs (Protocols 12–14), UAT and documentation packages (Protocols 15–16)
- Tooling references: financial/contract systems, stakeholder registry, PM tools, communication templates
- Automation scripts: `scripts/package_handover_assets.py`, `scripts/track_approvals.py`, `scripts/notify_stakeholders.py`, `scripts/archive_project_assets.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Project Closure Director responsible for sign-off, financial reconciliation, and ownership transfer
- Guardrail: No closure without signed acceptance, resolved financials, and documented ownership transitions
- Dependencies: Inputs from Protocols 5,10–16; outputs to Protocol 18, PMO systems, context archives

### Layer 2 – Behavioral Control
- Gates: Readiness verification, handover package, acceptance approvals, transition confirmation
- Halt conditions: Outstanding deliverables, missing approvals, ownership gaps
- Prompts: Financial check, approval status confirmation

### Layer 3 – Procedural Logic
- Phases: Readiness assessment → Stakeholder planning → Approval execution → Transition follow-up
- Evidence: Completion checklist, financial reconciliation, governance validation, ownership matrix, handover manifest, acceptance records, transition confirmation, closure communications, lessons learned
- Automation: Asset packaging, approval tracking, stakeholder notifications, asset archiving

### Layer 4 – Communication Grammar
- Announcements for readiness, alignment, approval, transition phases
- Validation prompts for financial reconciliation and final approval issuance
- Error handling for outstanding deliverables, missing approvals, ownership gaps

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 17: PROJECT CLOSURE & HANDOVER (PROGRAM DELIVERY COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail referencing acceptance, financials, and ownership transfer
3. Section **2. PROJECT CLOSURE & HANDOVER WORKFLOW** with four STEP sections and `[MUST]/[GUIDELINE]` directives from the form
4. Section **3. INTEGRATION POINTS** listing inputs (Protocols 5,10–16) and outputs (Protocol 18, PMO/finance, context kit)
5. Section **4. QUALITY GATES** defining readiness, handover package, acceptance, and transition confirmation gates
6. Section **5. COMMUNICATION PROTOCOLS** with announcements, validation prompts, and error cases provided
7. Section **6. AUTOMATION HOOKS** referencing four automation scripts with proper parameters
8. Section **7. HANDOFF CHECKLIST** reflecting closure validation requirements

## 5. Automation Hook Rules
- Include manifest path for `package_handover_assets.py` and zipped output `HANDOVER-PACKAGE.zip`
- Ensure `track_approvals.py` uses `acceptance-records.json`
- `notify_stakeholders.py` must reference the communication plan
- Archive script should reuse the handover manifest for completeness

## 6. Quality Acceptance Criteria
- `[MUST]` items cite evidence artifacts such as `completion-checklist.json`, `financial-reconciliation.csv`, `acceptance-records.json`
- Gates list failure handling consistent with halt conditions in the form
- Communication prompts retain `[FINANCIAL CHECK]` and `[APPROVAL STATUS]` tokens
- Integration outputs mention Protocol 18 transition inputs and organizational system updates
- Guardrail text aligns with form statement on acceptance, financials, and ownership transfer

## 7. Generation Workflow for the AI
1. Validate form completeness and cross-reference upstream protocol dependencies
2. Expand each phase into Markdown step list with numbered `[MUST]/[GUIDELINE]` actions and evidence storage
3. Populate integration and quality gate sections using form data
4. Inject communication templates and error handling verbatim
5. Confirm automation hooks cover packaging, approvals, stakeholder notifications, and archiving
6. Save output to `.cursor/ai-driven-workflow/17-project-closure.md`

## 8. Output & Post-Generation Actions
- Recommend distributing generated handover manifest to Protocol 18 owners
- Suggest updating PMO dashboards with closure evidence
- Encourage running meta-analysis validation for circular compliance
