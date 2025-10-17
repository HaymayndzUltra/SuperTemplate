# Generator: Protocol 7 – Development Environment Setup & Validation

## 1. Purpose
Guide AI agents in converting `protocol-input-form-7-environment.yaml` into `7-environment-setup-validation.md`, ensuring environment provisioning instructions remain consistent with technical design outputs and downstream execution requirements.

## 2. Required Inputs
- Completed `protocol-input-form-7-environment.yaml`
- Artifacts from Protocol 6: `TECHNICAL-DESIGN.md`, `design-validation-report.json`
- Bootstrap assets: `.cursor/context-kit/`, `.artifacts/bootstrap/`
- Script availability: `doctor.py`, `setup.sh`, `scaffold_phase_artifacts.py`, `install_and_test.sh`

## 3. 4-Layer Architecture Mapping
### Layer 1 – System-Level Decisions
- Role: DevOps Environment Engineer establishing consistent developer workspace
- Guardrail: Environment cannot be approved without full validation on clean setup
- Dependencies: Protocol 6 outputs, bootstrap governance

### Layer 2 – Behavioral Control
- Gates: Requirements confirmation, tooling health, validation suite, onboarding package
- Halt conditions: Missing credentials, failing diagnostics/tests, absent approval
- Validation prompts: Packaging approval, onboarding release confirmation

### Layer 3 – Procedural Logic
- Phases: Requirements extraction → Provisioning → Configuration & validation → Documentation & distribution
- Evidence artifacts: Requirements summary, diagnostics, configuration report, validation suite report, approval record
- Automation hooks: `doctor.py`, `setup.sh`, `scaffold_phase_artifacts.py`, `install_and_test.sh`

### Layer 4 – Communication Grammar
- Phase announcements for each stage
- Automation status messages using `[AUTOMATION] {script} executed: {status}`
- Validation prompts `[VALIDATION REQUEST]`, `[APPROVAL CONFIRMATION]`
- Error messages for credentials, tooling, validation failures

## 4. Protocol Template Structure
Ensure the generated protocol includes:
1. H1 heading with protocol title and compliance domain
2. Section **1. AI ROLE AND MISSION** with guardrail emphasis
3. Section **2. ENVIRONMENT SETUP WORKFLOW** containing four steps mirroring form phases with `[MUST]/[GUIDELINE]` markers
4. Section **3. INTEGRATION POINTS** (inputs from design/bootstrap, outputs to execution/deployment)
5. Section **4. QUALITY GATES** matching form gate definitions
6. Section **5. COMMUNICATION PROTOCOLS** (status messages, prompts, error handling)
7. Section **6. AUTOMATION HOOKS** mapping scripts to phases
8. Section **7. HANDOFF CHECKLIST** with environment readiness checks and closing command

## 5. Automation Hook Guidelines
- Commands must reflect repo structure and include required flags
- Evidence directories should live under `.artifacts/environment/`
- Mention alternative bootstrap commands if project overrides `setup.sh`

## 6. Quality Acceptance Criteria
- Each phase contains explicit evidence outputs with storage paths
- Quality gates align with provided criteria and include failure handling instructions
- Communications use consistent bracket notation and reference environment context
- Integration points clearly connect to Protocols 3 and 11
- No placeholder text; environment handbook referenced explicitly

## 7. Generation Workflow for the AI
1. Validate form fields and prerequisite artifact references
2. Translate each form phase into Markdown subsections with numbered steps and `[MUST]/[GUIDELINE]` markers
3. Populate evidence lists, automation commands, and communications from form data
4. Cross-verify quality gate definitions with evidence artifacts
5. Add validation prompts and error handling exactly as specified
6. Produce final markdown at `.cursor/ai-driven-workflow/7-environment-setup-validation.md`

## 8. Output & Post-Generation Actions
- Save protocol file in workflow directory
- Recommend running meta-analysis generator to confirm structural compliance
- Notify maintainers to refresh onboarding package when design artifacts change
