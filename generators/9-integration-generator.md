# Generator: Protocol 9 – Integration Testing & System Validation

## 1. Purpose
Guide AI agents in transforming `protocol-input-form-9-integration.yaml` into `9-integration-testing.md`, enforcing cross-component validation, contract assurance, and evidence packaging required before Quality Audit and Pre-Deployment protocols.

## 2. Required Inputs
- Completed `protocol-input-form-9-integration.yaml`
- Upstream artifacts: Protocol 3 feature outputs, Protocol 6 architecture contracts, Protocol 7 environment baselines
- Tooling access: Integration environment credentials, contract testing frameworks, observability dashboards
- Automation scripts: `scripts/validate_environment.py`, `scripts/run_contract_tests.py`, integration test runner command (e.g., `pytest -m integration`)

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: Integration Test Engineer validating end-to-end workflows prior to audit
- Guardrail: No readiness certification without production-representative evidence for critical paths
- Dependencies: Inputs from Protocols 3, 6, 7; outputs to Protocols 4, 10, 12

### Layer 2 – Behavioral Control
- Gates: Scope alignment, contract assurance, execution integrity, sign-off
- Halt conditions: Missing artifacts, unresolved critical defects, absent approvals
- Prompts: Defect remediation confirmation, sign-off approval request

### Layer 3 – Procedural Logic
- Phases: Scope alignment → Test design → Execution & defect management → Validation & handoff
- Evidence: Scope matrix, environment validation, test plan, execution report, defect log, evidence manifest
- Automation: Environment validation script, contract tests, integration test runner, artifact manifest generator

### Layer 4 – Communication Grammar
- Phase announcements for each stage
- Automation status messages for validation and test executions
- Error messages for missing artifacts, environment mismatches, test failures

## 4. Protocol Template Structure
Generated markdown must include:
1. H1 heading `# PROTOCOL 9: ... (QUALITY COMPLIANT)`
2. Section **1. AI ROLE AND MISSION** with guardrail statement
3. Section **2. INTEGRATION TESTING WORKFLOW** with four steps; each contains `[MUST]/[GUIDELINE]` actions, communications, evidence, automation/halt details
4. Section **3. INTEGRATION POINTS** describing inputs (Protocols 3,6,7) and outputs (Protocols 4,10,12)
5. Section **4. QUALITY GATES** covering Scope Alignment, Contract Assurance, Execution Integrity, Sign-Off
6. Section **5. COMMUNICATION PROTOCOLS** with status announcements, validation prompts, and error handling entries from the form
7. Section **6. AUTOMATION HOOKS** listing scripts/commands and their purposes
8. Section **7. HANDOFF CHECKLIST** mirroring checklist items from the form

## 5. Automation Hook Rules
- Ensure command strings include paths (`python scripts/...`, `pytest -m integration ...`)
- Default evidence storage under `.artifacts/integration/`
- Mention optional manifest generator if referenced in form

## 6. Quality Acceptance Criteria
- Every workflow step ties to evidence locations defined in the form
- Quality gates explicitly cite associated evidence filenames
- Communication templates use bracketed tags `[PHASE ...]`, `[DEFECT REVIEW]`, `[SIGN-OFF REQUEST]`
- Integration outputs mention `INTEGRATION-EVIDENCE.zip` and downstream artifacts
- Guardrail text must match form language regarding production-representative evidence

## 7. Generation Workflow for the AI
1. Validate that all form phases include mandatory `[MUST]` actions and evidence entries
2. Map each phase to a `STEP` section with ordered actions, communications, and automation notes
3. Populate integration/quality gate sections from `integration_inputs`, `integration_outputs`, and `quality_gates_summary`
4. Insert communication templates exactly as provided (status, prompts, error handling)
5. Confirm checklist items align with evidence artifacts before rendering Markdown
6. Write output to `.cursor/ai-driven-workflow/9-integration-testing.md`

## 8. Output & Post-Generation Actions
- Recommend running meta-analysis validation to confirm 4-layer extraction
- Advise teams to refresh integration environment snapshots when scope matrix changes
- Suggest syncing with Protocol 4 owner before declaring handoff complete
