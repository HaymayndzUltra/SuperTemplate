# Generator Playbook: Protocol 7 – Development Environment Setup & Validation

## 1. Mission Alignment
- **Goal:** Generate `7-development-environment-setup-validation.md` aligned with DevOps enablement scope.
- **Source Inputs:** `generators/protocol-input-form-7-environment.yaml`, outputs from Protocols 02 & 06.
- **Guardrails:** Never introduce secrets; emphasize reproducibility and onboarding deliverables.

## 2. 4-Layer Architecture Mapping
| Layer | Required Focus |
|-------|----------------|
| **L1** | Role (DevOps Enablement Engineer), mission, guardrail against storing secrets |
| **L2** | Baseline/Provisioning/Validation gates, halt conditions, approval prompts |
| **L3** | Procedural steps for inventory, provisioning, validation; evidence & automation hooks |
| **L4** | Status announcements, validation prompts, error handling messages |

## 3. Template Blueprint
1. H1 protocol title.
2. `## 1. AI ROLE AND MISSION` with mission & guardrail.
3. `## 2. ENVIRONMENT ENABLEMENT WORKFLOW` with three `### STEP` sections mirroring phases.
   - Each step lists ordered actions with `[MUST]`/`[GUIDELINE]` markers, action/communication/optional halt bullets.
   - Append **Evidence Collection** and **Quality Gate** blocks per phase.
4. `## 3. INTEGRATION POINTS`
5. `## 4. QUALITY GATES`
6. `## 5. COMMUNICATION PROTOCOLS`
7. `## 6. HANDOFF CHECKLIST`

## 4. Automation & Tooling Hooks
- Reference `env_diagnostics.py`, `env_provisioner.py`, `env_validator.py` in communications where applicable.
- Evidence paths must land in `.artifacts/environment/` except onboarding handbook (documentation/).
- Highlight outputs feeding Protocols 03 and 04.

## 5. Quality Acceptance Criteria
- All three phases include at least two evidence artifacts.
- Quality gates in Section 4 match names from Phase detail.
- Communication section provides fenced code block for announcements and prompts.
- Error handling list covers MissingRequirements, ProvisioningFailure, ValidationFailure.
- Handoff checklist includes onboarding handbook publication.

## 6. Validation Checklist for Generator
- [ ] Guardrail explicitly states no secrets stored.
- [ ] Automation hooks align with form commands.
- [ ] Outputs mention Protocol 03 and Protocol 04.
- [ ] Validation gate names consistent between sections.
- [ ] All `[MUST]` steps from form present.
