# Protocol 11 Generator - Production Deployment & Release Management

## 🎯 Purpose
Convert the filled requirements form (`protocol-input-form-11-deployment.yaml`) into `.cursor/ai-driven-workflow/11-production-deployment.md`. The protocol must orchestrate go/no-go approvals, controlled rollout, and post-release evidence capture.

## 📥 Required Inputs
- Completed `protocol-input-form-11-deployment.yaml`
- Release artifacts from Protocol 10 (staging validation, readiness checklist, rollback plan)
- Quality audit approvals from Protocol 4
- Access to deployment/rollback scripts in `/scripts`

## 🧠 4-Layer Mapping Blueprint
1. **Layer 1 – System-Level Decisions**
   - Persona: Release Manager controlling production deployments
   - Guardrail: No production deployment without approvals & rollback readiness
   - Dependencies: Protocol 10 + Protocol 4 outputs
2. **Layer 2 – Behavioral Control**
   - Gates: Go/No-Go, Deployment Success, Post-Release Validation
   - Halt conditions: missing prerequisites, failed health checks, failing validation
   - Approval prompts for go/no-go and monitoring handoff
3. **Layer 3 – Procedural Logic**
   - Phases: Release Readiness → Controlled Deployment → Post-Release Validation
   - Evidence: readiness audit, deployment logs, health metrics, communications bundle
   - Automation: validation_gates.py, deploy_backend.sh, rollback_backend.sh, collect_perf.py
4. **Layer 4 – Communication Grammar**
   - Announcements for each phase
   - Validation prompts for go/no-go and post-release confirmation
   - Error templates for missing prerequisites, deployment failure, validation failure

## 🏗️ Template Blueprint
```
# PROTOCOL 11: PRODUCTION DEPLOYMENT & RELEASE MANAGEMENT (RELEASE MANAGEMENT COMPLIANT)

## 1. AI ROLE AND MISSION
[Persona + mission + guardrail]

## 2. RELEASE EXECUTION WORKFLOW
### STEP 1: Release Readiness Confirmation
[Steps, evidence, go/no-go approvals]

### STEP 2: Controlled Production Deployment
[Deployment preparations, execution, monitoring, automation commands]

### STEP 3: Post-Release Validation & Communication
[Validation checks, communications, evidence archiving]

## 3. INTEGRATION POINTS
[Inputs from Protocol 10 & 4; outputs to 12, 13, and 5]

## 4. QUALITY GATES
[Go/No-Go Gate, Deployment Success Gate, Post-Release Validation Gate]

## 5. COMMUNICATION PROTOCOLS
[Announcements, validation prompts, error handling]

## 6. AUTOMATION HOOKS
[List commands with expected outputs]

## 7. HANDOFF CHECKLIST
[Checklist + completion command routing to Protocol 12]
```
- Include evidence storage paths using `.artifacts/deployment/`.
- Present automation commands inside fenced code blocks.
- Document rollback procedures and when to trigger them.

## 🤖 Automation & Evidence Integration
- Align each automation hook to a step; explain expected output file and purpose.
- Highlight when rollback scripts are conditional (triggered on failure).
- Ensure evidence bundle references include zipped archive for downstream protocols.

## ✅ Quality Acceptance Checklist
**Structural**
- [ ] Correct header naming and domain tag
- [ ] Sections 1–7 present and ordered
- [ ] Steps marked with `[MUST]`/`[GUIDELINE]` and include communication + halt details

**Content**
- [ ] Integration points cover upstream (10, 4) and downstream (12, 13, 5)
- [ ] Evidence and gates align with form content
- [ ] Automation commands reference existing scripts and produce expected artifact names
- [ ] Communications include go/no-go and post-release prompts

**Validation**
- [ ] Deployment Success gate references health metrics + rollback readiness
- [ ] Handoff checklist states evidence archive and communications delivered
- [ ] Completion command transitions to Protocol 12

## 🔁 Circular Validation Workflow
1. Generate protocol at `.cursor/ai-driven-workflow/11-production-deployment.md`.
2. Run Meta-Analysis Generator and verify all layers (mission, gates, procedures, communications) are captured.
3. If missing, refine sections (especially communication/error handling) and re-run analysis.

## ⚠️ Failure Handling Guidance
- **Form omissions** → Request additional detail for phases, evidence, or automation.
- **Script mismatch** → Confirm availability of deployment/rollback scripts and adjust names if necessary.
- **Gate ambiguity** → Ensure criteria are measurable (e.g., “zero critical alerts”, “validation report PASS”).
- **Integration conflicts** → Validate artifact names and protocol numbers before finalizing.
