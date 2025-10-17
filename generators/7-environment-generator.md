# Protocol 7 Generator Instructions — Development Environment Setup & Validation

## 1. Mission
- Convert `protocol-input-form-7-environment.yaml` into `.cursor/ai-driven-workflow/7-environment-setup-validation.md`.
- Produce a DevOps-focused protocol that hands validated environments to Protocol 3 while honoring governance style.

## 2. Inputs
- Required form: `protocol-input-form-7-environment.yaml`
- Architecture guardrails from Protocol 6 for reference of tooling names.
- Task backlog artifacts for persona mapping references (do not embed content, only reference).

## 3. Output Structure
Maintain the canonical ordering:
1. Title with `(DevOps Compliance Compliant)` suffix.
2. `## 1. AI ROLE AND MISSION`
3. `## 2. ENVIRONMENT SETUP WORKFLOW`
4. `## 3. INTEGRATION POINTS`
5. `## 4. QUALITY GATES`
6. `## 5. COMMUNICATION PROTOCOLS`
7. `## 6. HANDOFF CHECKLIST`

## 4. Layer Mapping Blueprint
| Layer | Source Fields | Rendering Notes |
|-------|---------------|-----------------|
| L1 | `ai_role`, `purpose`, `primary_guardrail` | Compose mission paragraph + guardrail. |
| L2 | `quality_gate`, `halt_condition`, `prerequisites` | Articulate gates (Access, Toolchain, Reproducibility) with evidence + recovery. |
| L3 | `phases.steps`, `evidence_collection`, `automation_hooks` | Build 3-step workflow with `[MUST]` emphasis and automation commands. |
| L4 | `communication_template`, `outputs_to` | Generate status announcements, validation prompts, error handling, and checklist narrative. |

## 5. Rendering Rules
- Use present tense and action verbs (`Gather`, `Confirm`, `Run`).
- Include automation commands as inline code in bullet lists when form provides `command` values.
- Evidence bullet format: `* **Evidence:** ...` so meta-analysis can detect data lineage.
- Halt conditions from the form become sentences beginning with `* **Halt condition:**` when specified.
- When optional containerization appears, mark corresponding step as `[GUIDELINE]`.

## 6. Integration Guidance
- **Inputs From:** Protocol 2 (task backlog) and Protocol 6 (guardrails). Reference artifacts exactly as form lists.
- **Outputs To:** Protocol 3 with environment evidence plus support playbook. Ensure filenames include `.artifacts/environment/...` or `.cursor/context-kit/...`.

## 7. Communication Grammar
- Status announcements must include `[PHASE N START]` and `[PHASE N COMPLETE]` lines for each phase.
- Validation prompts should follow the pattern `Approve ...? (yes/no)`.
- Error handling bullets must describe recovery paths for access, toolchain, and validation failures.

## 8. Quality Checklist
- [ ] Three phases rendered with numbered steps preserving `[MUST]` / `[GUIDELINE]`.
- [ ] Automation hooks `collect_inventory.py`, `bootstrap_toolchain.py`, `validate_environment.py` appear once with full command.
- [ ] Quality gate names exactly: `Access & Inventory Gate`, `Toolchain Readiness Gate`, `Reproducibility Gate`.
- [ ] Outputs reference `.artifacts/environment/validation-report.json` and `.cursor/context-kit/environment-support.md`.
- [ ] Handoff checklist contains five checkboxes matching form intent plus completion code block.

## 9. Circular Validation Prep
- Ensure Step 3 references reproducibility & support playbook so meta-analysis identifies resilience pattern.
- Confirm communication block contains both start and complete announcements for each phase (6 lines total).
- Review final markdown for heading hierarchy compliance and absence of trailing whitespace.
