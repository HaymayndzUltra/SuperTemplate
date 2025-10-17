# Generator: Protocol 16 – Documentation & Knowledge Transfer

## 1. Purpose
Guide AI agents to transform `protocol-input-form-16-documentation.yaml` into `16-documentation-knowledge-transfer.md`, ensuring documentation scope, drafting, validation, and publication steps match the knowledge management guardrails and evidence paths.

## 2. Required Inputs
- Completed `protocol-input-form-16-documentation.yaml`
- Upstream artifacts: PRD updates (Protocol 1), architecture & integration decisions (Protocol 6 & 9), deployment/operations outputs (Protocols 11–14), UAT closure assets (Protocol 15)
- Tooling references: documentation templates, knowledge base platform, collaboration suite, recording tools
- Automation scripts: `scripts/audit_doc_gaps.py`, `scripts/generate_doc_portal.py`, `scripts/verify_doc_accuracy.py`, `scripts/schedule_enablement.py`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Technical Documentation Lead coordinating multi-stakeholder knowledge transfer
- Guardrail: No completion without peer approvals and confirmed stakeholder access to published materials
- Dependencies: Inputs from Protocols 1,3,6,11–15; outputs to Protocols 17,18,5

### Layer 2 – Behavioral Control
- Gates: Source inventory, draft completion, review validation, publication enablement
- Halt conditions: Missing artifacts, unapproved reviews, access failures
- Prompts: Inventory check, publish readiness confirmation

### Layer 3 – Procedural Logic
- Phases: Inventory confirmation → Drafting & tooling → Review & validation → Publication & enablement
- Evidence: Inventory matrix, audience matrix, draft folder, review log, validation report, publication manifest, enablement summary, feedback backlog
- Automation: Gap audit, portal generation, accuracy verification, enablement scheduling

### Layer 4 – Communication Grammar
- Phase announcements for inventory, drafting, review, publication
- Validation prompts for inventory completeness and publish readiness
- Error messages for missing sources, review rejection, and access failures

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 16: DOCUMENTATION & KNOWLEDGE TRANSFER (KNOWLEDGE MANAGEMENT COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail text emphasizing approvals and access evidence
3. Section **2. DOCUMENTATION & KNOWLEDGE TRANSFER WORKFLOW** with four STEP blocks aligning to phases and `[MUST]/[GUIDELINE]` markers
4. Section **3. INTEGRATION POINTS** listing inputs (Protocols 1,3,6,11–15) and outputs (Protocols 17,18,5)
5. Section **4. QUALITY GATES** covering source inventory, draft completion, review/validation, publication & enablement
6. Section **5. COMMUNICATION PROTOCOLS** with announcements, prompts, and error handling tokens from the form
7. Section **6. AUTOMATION HOOKS** referencing the four scripts with correct parameters
8. Section **7. HANDOFF CHECKLIST** matching checklist requirements from the input form

## 5. Automation Hook Rules
- Use `.artifacts/documentation/` as default storage namespace
- Ensure `audit_doc_gaps.py`, `generate_doc_portal.py`, and `verify_doc_accuracy.py` commands include explicit input/output arguments
- Mention `schedule_enablement.py` as optional automation for enablement summary creation

## 6. Quality Acceptance Criteria
- All `[MUST]` items link to evidence artifacts defined in the form
- Quality gates cite specific filenames (`source-inventory.json`, `audience-matrix.csv`, `gap-analysis.json`, etc.)
- Communication prompts retain `[INVENTORY CHECK]` and `[PUBLISH READY]` tokens
- Integration outputs explicitly mention publication manifest, enablement summary, and feedback backlog
- Guardrail language mirrors form directive about approvals and stakeholder access

## 7. Generation Workflow for the AI
1. Validate form completeness and prerequisite references
2. Translate each phase into Markdown step sections with numbered actions
3. Map evidence_collection items to Evidence bullet lists and gate criteria
4. Insert communication templates and error handling exactly as provided
5. Confirm automation hooks capture gap audit, portal generation, accuracy verification, and enablement scheduling
6. Save final protocol to `.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md`

## 8. Output & Post-Generation Actions
- Recommend running meta-analysis validation to confirm 4-layer coverage
- Suggest notifying Protocol 17 owner once publication manifest generated
- Encourage documenting lessons learned for Protocol 5 retrospectives
