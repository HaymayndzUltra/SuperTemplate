# PROTOCOL 7: ENVIRONMENT SETUP & VALIDATION (DEVOPS COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` from Protocol 6
- [ ] `tasks-{feature}.md`, `task-automation-matrix.json` from Protocol 2
- [ ] `.cursor/context-kit/governance-status.md` and `bootstrap-manifest.json` from Protocol 00

### Required Approvals
- [ ] DevOps lead authorization to provision environments
- [ ] Security team confirmation for credential handling and secret storage

### System State Requirements
- [ ] Access to infrastructure credentials, repositories, and artifact storage
- [ ] Clean workstation or container image available for validation
- [ ] Automation scripts `doctor.py`, `scaffold_phase_artifacts.py`, and validation suites accessible

---

## 7. AI ROLE AND MISSION

You are a **DevOps Environment Engineer**. Your mission is to provision, validate, and document a consistent development environment aligned with technical design requirements so teams can execute tasks reliably.

**🚫 [CRITICAL] Do not declare the environment ready until validation passes on a clean baseline and credentials are verified.**

---

## 7. ENVIRONMENT WORKFLOW

### STEP 1: Requirement Alignment

1. **`[MUST]` Extract Environment Requirements:**
   * **Action:** Review `TECHNICAL-DESIGN.md`, `task-generation-input.json`, and `tasks-{feature}.md` to identify runtime tooling, services, and configuration needs; capture in `environment-requirements.md`.
   * **Communication:** 
     > "[PHASE 1 START] - Consolidating environment requirements from design and task plans."
   * **Halt condition:** Stop if requirements conflict or remain undefined.
   * **Evidence:** `.artifacts/protocol-7/environment-requirements.md`

2. **`[MUST]` Validate Credentials & Access:**
   * **Action:** Confirm repository access, secret storage workflow, API keys, and external service credentials; record in `access-readiness-checklist.json`.
   * **Communication:** 
     > "Validating credentials and secret storage readiness."
   * **Evidence:** `.artifacts/protocol-7/access-readiness-checklist.json`

3. **`[GUIDELINE]` Capture Risk Flags:**
   * **Action:** Log environment risks (e.g., license limits, dependency volatility) in `environment-risk-log.md`.

### STEP 2: Provisioning & Tooling Verification

1. **`[MUST]` Execute Environment Doctor:**
   * **Action:** Run `python scripts/doctor.py --strict --output .artifacts/protocol-7/environment-diagnostics.json` to verify required tooling.
   * **Communication:** 
     > "[PHASE 2] - Running environment diagnostics for tooling compliance."
   * **Halt condition:** Pause if diagnostics fail.
   * **Evidence:** `.artifacts/protocol-7/environment-diagnostics.json`

2. **`[MUST]` Provision Scaffold & Dependencies:**
   * **Action:** Clone repository, install dependencies, and execute bootstrap scripts (e.g., `bash scripts/setup.sh --non-interactive`); document in `provision-log.md`.
   * **Evidence:** `.artifacts/protocol-7/provision-log.md`

3. **`[GUIDELINE]` Validate Container/Image:**
   * **Action:** Build/pull required dev containers or VM images; store metadata in `runtime-images.json`.

### STEP 3: Configuration & Validation

1. **`[MUST]` Apply Configuration Templates:**
   * **Action:** Populate environment variables, secret placeholders, and configuration files; run `python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-7/env-configuration-report.json`.
   * **Communication:** 
     > "[PHASE 3] - Applying configuration templates and documenting outcomes."
   * **Evidence:** `.artifacts/protocol-7/env-configuration-report.json`

2. **`[MUST]` Run Validation Suite:**
   * **Action:** Execute smoke tests, linting, migrations, and sample automation hooks from `task-automation-matrix.json`; store outputs in `validation-suite-report.json`.
   * **Evidence:** `.artifacts/protocol-7/validation-suite-report.json`

3. **`[GUIDELINE]` Record Performance Baseline:**
   * **Action:** Capture setup duration and validation runtimes in `provision-log.md`.

### STEP 4: Documentation & Handoff

1. **`[MUST]` Create Environment Handbook:**
   * **Action:** Assemble `ENVIRONMENT-README.md` with setup steps, commands, validation expectations, troubleshooting, and automation references.
   * **Communication:** 
     > "[PHASE 4] - Drafting environment handbook for contributors."
   * **Evidence:** `.artifacts/protocol-7/ENVIRONMENT-README.md`

2. **`[MUST]` Record Approval & Distribution Plan:**
   * **Action:** Log validation status, approver, distribution channels in `environment-approval-record.json`.
   * **Halt condition:** Do not proceed without approval.
   * **Evidence:** `.artifacts/protocol-7/environment-approval-record.json`

3. **`[GUIDELINE]` Package Onboarding Assets:**
   * **Action:** Bundle scripts, env templates, and handbook into `environment-onboarding.zip`; update manifest `environment-artifact-manifest.json`.

---

## 7. INTEGRATION POINTS

### Inputs From:
- **Protocol 6**: `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` - Define infrastructure and sequencing requirements.
- **Protocol 2**: `tasks-{feature}.md`, `task-automation-matrix.json` - Automation references and execution expectations.
- **Protocol 00**: `.cursor/context-kit/governance-status.md`, `bootstrap-manifest.json` - Baseline tooling and governance.

### Outputs To:
- **Protocol 3**: `ENVIRONMENT-README.md`, `environment-onboarding.zip`, `validation-suite-report.json` - Execution environment package.
- **Protocol 11**: `environment-approval-record.json`, `environment-diagnostics.json` - Deployment readiness baseline.

### Artifact Storage Locations:
- `.artifacts/protocol-7/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration updates

---

## 7. QUALITY GATES

### Gate 1: Requirements Confirmation Gate
- **Criteria**: Environment requirements documented, credential checklist complete, risk log updated.
- **Evidence**: `environment-requirements.md`, `access-readiness-checklist.json`, `environment-risk-log.md`
- **Pass Threshold**: Requirements coverage ≥ 95%, no unresolved critical credentials.
- **Failure Handling**: Coordinate with stakeholders to resolve gaps, rerun validation.
- **Automation**: `python scripts/validate_environment_requirements.py --input .artifacts/protocol-7/environment-requirements.md`

### Gate 2: Tooling Health Gate
- **Criteria**: Environment diagnostics succeed with compliant versions, provisioning log free of failures.
- **Evidence**: `environment-diagnostics.json`, `provision-log.md`
- **Pass Threshold**: Diagnostics status `pass` and dependency installs successful.
- **Failure Handling**: Fix tooling gaps, update scripts, rerun diagnostics.
- **Automation**: `python scripts/doctor.py --strict --output .artifacts/protocol-7/environment-diagnostics.json`

### Gate 3: Validation Suite Gate
- **Criteria**: Configuration report complete, smoke tests and automation hooks pass.
- **Evidence**: `env-configuration-report.json`, `validation-suite-report.json`
- **Pass Threshold**: All required checks `pass`; automation coverage ≥ 80% of high-level tasks.
- **Failure Handling**: Investigate failing tests, adjust configs, rerun suite.
- **Automation**: `bash scripts/install_and_test.sh --smoke`

### Gate 4: Onboarding Package Gate
- **Criteria**: Handbook, approval record, and onboarding package finalized and distributed.
- **Evidence**: `ENVIRONMENT-README.md`, `environment-approval-record.json`, `environment-onboarding.zip`, `environment-artifact-manifest.json`
- **Pass Threshold**: Approval status `approved`, package accessible to team.
- **Failure Handling**: Update docs/assets, obtain approval, rerun packaging.
- **Automation**: `python scripts/package_environment_assets.py --output .artifacts/protocol-7/environment-onboarding.zip`

---

## 7. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[PHASE 1 START] - "Extracting environment requirements and verifying credentials."
[PHASE 2 START] - "Provisioning environment and validating tooling."
[PHASE 3 START] - "Applying configuration templates and running validation suite."
[PHASE 4 START] - "Compiling environment handbook and packaging onboarding assets."
[PHASE COMPLETE] - "Environment setup validated; artifacts archived in .artifacts/protocol-7/."
[ERROR] - "Issue encountered during [phase]; see associated evidence report."
```

### Validation Prompts:
```
[USER CONFIRMATION REQUIRED]
> "Environment validation suite succeeded. Evidence ready:
> - environment-diagnostics.json
> - env-configuration-report.json
> - validation-suite-report.json
>
> Approve packaging onboarding assets and recording final sign-off?"
```

### Error Handling:
```
[GATE FAILED: Tooling Health Gate]
> "Quality gate 'Tooling Health' failed.
> Criteria: doctor.py must report compliant tooling versions.
> Actual: Docker version below minimum.
> Required action: Upgrade Docker to required version, rerun doctor.py, update diagnostics.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 7. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_7.py

# Quality gate automation
python scripts/doctor.py --strict --output .artifacts/protocol-7/environment-diagnostics.json
python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-7/env-configuration-report.json
bash scripts/install_and_test.sh --smoke
python scripts/package_environment_assets.py --output .artifacts/protocol-7/environment-onboarding.zip

# Evidence aggregation
python scripts/aggregate_evidence_7.py --output .artifacts/protocol-7/
```

### CI/CD Integration:
```yaml
name: Protocol 7 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 7 Gates
        run: python scripts/run_protocol_7_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual tooling checklist; record in `manual-tooling-review.md`.
2. Run smoke tests manually; capture logs in `.artifacts/protocol-7/manual-validation-suite.md`.
3. Document manual approvals in `.artifacts/protocol-7/manual-validation-log.md`.

---

## 7. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 3:
**[PROTOCOL COMPLETE]** Ready for Protocol 3: Controlled Task Execution

**Evidence Package:**
- `ENVIRONMENT-README.md` - Contributor onboarding guide
- `validation-suite-report.json` - Verified environment validation results

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/3-process-tasks.md
```

---

## 7. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `environment-requirements.md` | `.artifacts/protocol-7/` | Tooling and service checklist | Protocol 3 |
| `environment-diagnostics.json` | `.artifacts/protocol-7/` | Tooling validation evidence | Protocol 11 |
| `validation-suite-report.json` | `.artifacts/protocol-7/` | Smoke test results | Protocols 3 & 11 |
| `ENVIRONMENT-README.md` | `.artifacts/protocol-7/` | Setup documentation | Protocol 3 |
| `environment-approval-record.json` | `.artifacts/protocol-7/` | Approval evidence | Protocol 11 |
| `environment-onboarding.zip` | `.artifacts/protocol-7/` | Distribution package | Protocol 3 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
