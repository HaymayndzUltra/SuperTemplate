# Generator: Protocol 15 – User Acceptance Testing (UAT) Coordination

## 1. Purpose
Instruct AI agents to transform `protocol-input-form-15-uat.yaml` into `15-uat-coordination.md`, ensuring customer-facing validation cycles are orchestrated with clear evidence, stakeholder approvals, and deployment-ready handoffs.

## 2. Required Inputs
- Completed `protocol-input-form-15-uat.yaml`
- Upstream artifacts: Protocol 1 PRD acceptance criteria, Protocol 4 quality audit approvals, Protocol 9 integration evidence, Protocol 10 staging readiness outputs
- Tooling: Communication templates, scheduling tools, ticketing system, release notes generator
- Automation scripts: `scripts/send_uat_invites.py`, `scripts/collect_uat_results.py`, `scripts/generate_release_notes.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: UAT Coordinator aligning stakeholders before deployment
- Guardrail: No UAT closure without approvals, resolved critical feedback, and aligned release documentation
- Dependencies: Inputs from Protocols 1,4,9,10; outputs to Protocols 10,11,5

### Layer 2 – Behavioral Control
- Gates: UAT entry, execution integrity, defect resolution, acceptance
- Halt conditions: Missing participant access, unresolved critical feedback, absent approvals
- Prompts: Entry check confirmation, sign-off request

### Layer 3 – Procedural Logic
- Phases: Preparation → Orientation & execution → Defect management → Acceptance & handoff
- Evidence: Entry checklist, roster, toolkit manifest, kickoff notes, execution log, feedback notebook, defect register, retest results, release notes, approval record, closure manifest, handoff brief
- Automation: Invitation script, results collector, release notes generator

### Layer 4 – Communication Grammar
- Phase announcements for preparation, kickoff, triage, acceptance
- Validation prompts for entry readiness and sign-off
- Error messages for access issues, critical feedback, documentation gaps

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 15: ... (CUSTOMER VALIDATION COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail statement
3. Section **2. UAT COORDINATION WORKFLOW** containing four steps with `[MUST]/[GUIDELINE]` actions, communications, evidence, automation/halt notes
4. Section **3. INTEGRATION POINTS** listing inputs (Protocols 1,4,9,10) and outputs (Protocols 10,11,5)
5. Section **4. QUALITY GATES** covering UAT Entry, Execution Integrity, Defect Resolution, Acceptance
6. Section **5. COMMUNICATION PROTOCOLS** with status announcements, validation prompts, error handling entries
7. Section **6. AUTOMATION HOOKS** referencing invite, results, and release note scripts
8. Section **7. HANDOFF CHECKLIST** aligned with completion checks in the form

## 5. Automation Hook Rules
- Include command parameters (e.g., `--config config/uat-participants.yaml`, `--output .artifacts/uat/...`)
- Evidence storage should default to `.artifacts/uat/`
- Note optional release notes generation as `[GUIDELINE]` action when referencing script

## 6. Quality Acceptance Criteria
- Each `[MUST]` action ties to evidence artifacts defined in the form
- Quality gates mention exact filenames (`uat-entry-checklist.json`, `execution-log.json`, `uat-defect-register.csv`, `uat-approval-record.json`)
- Communication prompts preserve `[ENTRY CHECK]` and `[SIGN-OFF REQUEST]` tokens
- Integration outputs include `UAT-CLOSURE-PACKAGE.zip`, `handoff-brief.md`, `feedback-notebook.md`
- Guardrail text mirrors form language about approvals and release documentation

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite references
2. Map each phase to Markdown `STEP` sections with numbered actions
3. Populate integration and quality gate sections using `integration_inputs`, `integration_outputs`, and `quality_gates_summary`
4. Insert communication templates and error handling verbatim from the form
5. Confirm automation hooks cover invite dispatch, result collection, and release note generation
6. Save final output to `.cursor/ai-driven-workflow/15-uat-coordination.md`

## 8. Output & Post-Generation Actions
- Recommend syncing with Protocol 10 owner to coordinate handoff timing
- Encourage running meta-analysis validation for circular compliance
- Suggest capturing lessons learned for Protocol 5 retrospective inputs
