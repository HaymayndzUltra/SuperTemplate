# Protocol 7 Generator - Development Environment Setup & Validation

## 🎯 Purpose
Provide detailed generation instructions for transforming `protocol-input-form-7-environment.yaml` into `.cursor/ai-driven-workflow/7-environment-setup-validation.md`. The generated protocol must ensure reproducible developer workspaces and align with architectural decisions.

## 📥 Required Inputs
- Completed `protocol-input-form-7-environment.yaml`
- TASK-PLAN.md, dependency matrix, and tooling requirements from Protocol 2
- Architecture spec and technology selections from Protocol 6
- Access to environment provisioning scripts located in `/scripts`

## 🧠 4-Layer Mapping Blueprint
1. **Layer 1 – System-Level Decisions**
   - Persona: DevOps Engineer safeguarding environment consistency
   - Guardrail: Environment cannot be approved without evidence
   - Dependencies: Task plan + architecture artifacts drive configuration scope
2. **Layer 2 – Behavioral Control**
   - Gates: Baseline Readiness, Provisioning Integrity, Environment Validation
   - Halt logic: provisioning failures, missing prerequisites, validation failures
   - Approval prompt for developer handoff
3. **Layer 3 – Procedural Logic**
   - Phases: Baseline Assessment → Provisioning → Validation & Handoff
   - Evidence: inventory, gap report, provisioning log, validation report
   - Automation: doctor.py, setup.sh, validate_workflows.py, test_workflow_integration.sh
4. **Layer 4 – Communication Grammar**
   - Standard phase announcements
   - Validation prompts for approvals and retry decisions
   - Error templates covering prerequisites, provisioning, validation

## 🏗️ Template Blueprint
```
# PROTOCOL 7: DEVELOPMENT ENVIRONMENT SETUP & VALIDATION (DEVOPS COMPLIANT)

## 1. AI ROLE AND MISSION
[Persona + mission + guardrail]

## 2. ENVIRONMENT SETUP WORKFLOW
### STEP 1: Baseline Assessment & Prerequisites
[Steps with required communications, halt conditions, evidence]

### STEP 2: Provisioning & Configuration
[Include automation commands and documentation requirements]

### STEP 3: Validation & Developer Handoff
[Describe validation suite, onboarding dry run, evidence capture]

## 3. INTEGRATION POINTS
[Protocols 2 & 6 inputs; outputs to Protocols 3 & 4]

## 4. QUALITY GATES
[Three gates with criteria/evidence/failure handling]

## 5. COMMUNICATION PROTOCOLS
[Announcements, validation prompts, error handling]

## 6. AUTOMATION HOOKS
[doctor.py, setup.sh, validate_workflows.py, test_workflow_integration.sh]

## 7. HANDOFF CHECKLIST
[Completion checklist + command transitioning to Protocol 3]
```
- Highlight evidence storage locations for each phase.
- Present automation commands in fenced code blocks with expected outputs.
- Mention onboarding dry run explicitly.

## 🤖 Automation & Evidence Integration
- Place automation commands adjacent to the steps that invoke them.
- Clarify where output artifacts live (`.artifacts/environment/...`).
- For validation outputs, describe key pass criteria (tests/lint/build).

## ✅ Quality Acceptance Checklist
**Structural**
- [ ] All sections 1–7 present and correctly ordered
- [ ] Steps labelled with `[MUST]` / `[GUIDELINE]` markers and include communication templates
- [ ] Halt conditions included for mandatory steps

**Content**
- [ ] Evidence collection items match storage paths defined in the form
- [ ] Integration section lists both upstream and downstream protocols with artifact usage
- [ ] Automation hooks align with specified scripts
- [ ] Completion checklist references validation evidence and approvals

**Validation**
- [ ] Environment validation gate references `environment-validation-report.json`
- [ ] Handoff command routes to Protocol 3
- [ ] Error handling covers missing prerequisites, provisioning failure, and validation failure

## 🔁 Circular Validation Workflow
1. Generate protocol file at `.cursor/ai-driven-workflow/7-environment-setup-validation.md`.
2. Run Meta-Analysis Generator; confirm all four layers are present (persona, gates, steps, communications).
3. If any layer missing or misaligned (e.g., missing automation context), update protocol and re-run analysis.

## ⚠️ Failure Handling Guidance
- **Incomplete form** → Request additional details (e.g., missing evidence items or automation commands).
- **Script references invalid** → Verify script existence or adjust commands to available tooling.
- **Integration ambiguity** → Ensure outputs to Protocol 3 & 4 include specific artifact names.
- **Communication gaps** → Add explicit prompts for environment approval and retry decisions.
