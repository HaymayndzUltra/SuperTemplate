---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 10: PRE-DEPLOYMENT VALIDATION & STAGING READINESS (RELEASE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `QUALITY-AUDIT-PACKAGE.zip` from Protocol 19 – audit readiness evidence
- [ ] `integration-evidence-bundle.zip` from Protocol 15 – integration validation summary
- [ ] `UAT-CLOSURE-PACKAGE.zip` from Protocol 20 – stakeholder acceptance proof (if available)
- [ ] `.artifacts/pre-deployment/release-manifest.json` (initial draft) from Release Planning
- [ ] Latest deployment scripts (`scripts/deploy_*.sh`, `scripts/rollback_*.sh`) from repository

### Required Approvals
- [ ] Quality Audit readiness recommendation signed by Senior Quality Engineer (Protocol 19)
- [ ] Product Owner confirmation that release scope is fixed (Protocol 06/15)
- [ ] Security and compliance lead clearance for staging deployment rehearsals

### System State Requirements
- [ ] Staging environment mirrors production configuration (infrastructure, secrets, feature flags)
- [ ] Access to deployment automation credentials and secret stores for staging
- [ ] Monitoring dashboards accessible for baseline capture

---

## 10. AI ROLE AND MISSION

You are a **Release Engineer**. Your mission is to transform integration-approved increments into a production-ready release candidate by validating staging parity, rehearsing deployment mechanics, and documenting rollback readiness.

**🚫 [CRITICAL] DO NOT issue a production go/no-go package unless staging mirrors production configurations and both deployment and rollback procedures have been executed successfully with captured evidence.**

---

## 10. PRE-DEPLOYMENT VALIDATION WORKFLOW

### STEP 1: Intake Validation and Staging Alignment

1. **`[MUST]` Confirm Upstream Approvals:**
   * **Action:** Validate required artifacts and approvals from Protocols 4, 9, and 15 before staging rehearsal begins.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating upstream approvals and artifact completeness..."
   * **Halt condition:** Stop if any prerequisite artifact missing or expired.
   * **Evidence:** `.artifacts/pre-deployment/intake-validation-report.json` summarizing status.

2. **`[MUST]` Validate Staging Parity:**
   * **Action:** Compare staging vs production configurations, secrets, and infrastructure components for drift detection.
   * **Communication:** 
     > "[PHASE 1] Staging parity check underway. Reporting drift if detected..."
   * **Halt condition:** Pause if drift exists without remediation plan.
   * **Evidence:** `.artifacts/pre-deployment/staging-parity-report.json` including diff details.

3. **`[GUIDELINE]` Refresh Test Data & Feature Flags:**
   * **Action:** Sync staging datasets, feature flags, and service stubs to align with release candidate requirements.
   * **Example:**
     ```bash
     python scripts/refresh_staging_data.py --env staging --output .artifacts/pre-deployment/staging-data-refresh.md
     ```

### STEP 2: Deployment Rehearsal and Verification

1. **`[MUST]` Execute Staging Deployment Rehearsal:**
   * **Action:** Run deployment scripts in staging replicating production sequencing with logging enabled.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Rehearsing deployment on staging environment..."
   * **Halt condition:** Stop if automation fails or unexpected errors occur.
   * **Evidence:** `.artifacts/pre-deployment/staging-deployment-run.log` capturing commands and results.

2. **`[MUST]` Validate Smoke & Acceptance Tests:**
   * **Action:** Execute smoke, end-to-end, and targeted regression suites against staging release candidate.
   * **Communication:** 
     > "[PHASE 2] Staging test suites executing. Monitoring pass/fail status..."
   * **Halt condition:** Pause if critical tests fail without mitigation.
   * **Evidence:** `.artifacts/pre-deployment/staging-test-results.json` with coverage metrics.

3. **`[GUIDELINE]` Capture Observability Baseline:**
   * **Action:** Record monitoring dashboards and metrics post-rehearsal for Protocol 19 reference.
   * **Example:**
     ```markdown
     - Metric: API latency (p95) – 320ms
     - Metric: Error rate – 0.2%
     ```

### STEP 3: Rollback, Security, and Operational Readiness

1. **`[MUST]` Rehearse Rollback Procedure:**
   * **Action:** Execute rollback automation or blue/green switchback to validate recovery path.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Verifying rollback and recovery procedures..."
   * **Halt condition:** Stop if rollback fails or exceeds recovery time objective.
   * **Evidence:** `.artifacts/pre-deployment/rollback-verification-report.json` detailing steps and timings.

2. **`[MUST]` Complete Security & Compliance Checks:**
   * **Action:** Run required security scans, license audits, and compliance validations pre-production.
   * **Communication:** 
     > "[PHASE 3] Executing security and compliance scans for release candidate..."
   * **Halt condition:** Pause if blocking findings identified.
   * **Evidence:** `.artifacts/pre-deployment/security-compliance-report.json` with findings and approvals.

3. **`[GUIDELINE]` Validate Runbooks & Support Coverage:**
   * **Action:** Confirm operational runbooks, on-call rotations, and escalation matrices updated for release.
   * **Example:**
     ```markdown
     - Runbook: api-service.md – updated 2024-05-30
     - On-call: Primary SRE (Alex), Backup (Jordan)
     ```

### STEP 4: Final Readiness Review and Handoff

1. **`[MUST]` Assemble Go/No-Go Package:**
   * **Action:** Bundle parity report, deployment and rollback evidence, test results, and security findings into `PRE-DEPLOYMENT-PACKAGE.zip`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Compiling pre-deployment readiness package for release approval..."
   * **Halt condition:** Stop if package contents incomplete or checksum invalid.
   * **Evidence:** `.artifacts/pre-deployment/pre-deployment-manifest.json` indexing artifacts.

2. **`[MUST]` Conduct Readiness Review:**
   * **Action:** Present findings to Release Manager and stakeholders; capture approvals, risks, and action items.
   * **Communication:** 
     > "[PHASE 4] Readiness review in progress. Recording decisions and risk mitigations..."
   * **Halt condition:** Pause if approvals withheld or risks unresolved.
   * **Evidence:** `.artifacts/pre-deployment/readiness-approval.json` with signatures.

3. **`[GUIDELINE]` Publish Deployment Checklist Updates:**
   * **Action:** Update production deployment checklist and communication plan based on rehearsal learnings.
   * **Example:**
     ```bash
     python scripts/update_deployment_checklist.py --source .artifacts/pre-deployment/staging-deployment-run.log --output .artifacts/pre-deployment/deployment-checklist.md
     ```

---

## 10. INTEGRATION POINTS

### Inputs From:
- **Protocol 19**: `QUALITY-AUDIT-PACKAGE.zip`, readiness recommendation – informs release gate
- **Protocol 23**: `script-compliance.json` – assures automation readiness
- **Protocol 15**: `integration-evidence-bundle.zip` – verifies integrated functionality
- **Protocol 20**: `UAT-CLOSURE-PACKAGE.zip`, `uat-approval-record.json` – confirms user acceptance

### Outputs To:
- **Protocol 15**: `PRE-DEPLOYMENT-PACKAGE.zip`, `readiness-approval.json`, `deployment-checklist.md`
- **Protocol 19**: `observability-baseline.md`, `staging-test-results.json`
- **Protocol 20**: `rollback-verification-report.json` for incident response readiness
- **Protocol 21**: `staging-parity-report.json` supporting performance baseline alignment

### Artifact Storage Locations:
- `.artifacts/pre-deployment/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 10. QUALITY GATES

### Gate 1: Intake Confirmation Gate
- **Criteria**: All upstream approvals verified; staging parity report free of critical drift.
- **Evidence**: `intake-validation-report.json`, `staging-parity-report.json`.
- **Pass Threshold**: Completeness score = 100%; drift severity ≤ low.
- **Failure Handling**: Halt; remediate configuration drift or obtain missing approvals.
- **Automation**: `python scripts/validate_gate_10_intake.py --drift-threshold low`

### Gate 2: Deployment Rehearsal Gate
- **Criteria**: Deployment rehearsal successful; smoke/regression tests pass with acceptable coverage.
- **Evidence**: `staging-deployment-run.log`, `staging-test-results.json`.
- **Pass Threshold**: 0 blocking errors; coverage ≥ 90% of targeted suites.
- **Failure Handling**: Rollback staging, fix issues, rerun rehearsal before proceeding.
- **Automation**: `python scripts/validate_gate_10_rehearsal.py --coverage 0.90`

### Gate 3: Rollback & Security Gate
- **Criteria**: Rollback rehearsal completes within RTO; security/compliance scans cleared.
- **Evidence**: `rollback-verification-report.json`, `security-compliance-report.json`.
- **Pass Threshold**: Recovery time ≤ RTO; zero unresolved blocking findings.
- **Failure Handling**: Address rollback gaps or security issues; rerun validations.
- **Automation**: `python scripts/validate_gate_10_security.py --rto 10`

### Gate 4: Readiness Approval Gate
- **Criteria**: Go/no-go package complete; readiness approvals signed; deployment checklist updated.
- **Evidence**: `pre-deployment-manifest.json`, `readiness-approval.json`, `deployment-checklist.md`.
- **Pass Threshold**: Manifest completeness ≥ 95%; approvals 100% recorded.
- **Failure Handling**: Obtain missing approvals; rebuild package; update checklist.
- **Automation**: `python scripts/validate_gate_10_readiness.py --threshold 0.95`

---

## 10. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Validating upstream approvals and artifact completeness...
[MASTER RAY™ | PHASE 1 COMPLETE] - Intake validation succeeded. Evidence: intake-validation-report.json.
[MASTER RAY™ | PHASE 2 START] - Rehearsing deployment on staging environment...
[MASTER RAY™ | PHASE 3 START] - Verifying rollback and recovery procedures...
[MASTER RAY™ | PHASE 4 START] - Compiling pre-deployment readiness package for release approval...
[MASTER RAY™ | PHASE 4 COMPLETE] - Pre-deployment package ready. Evidence: PRE-DEPLOYMENT-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Pre-deployment validation complete. Evidence prepared:
> - PRE-DEPLOYMENT-PACKAGE.zip
> - readiness-approval.json
>
> Confirm readiness to transition to Protocol 15?"
```

### Error Handling:
```
[RAY GATE FAILED: Deployment Rehearsal Gate]
> "Quality gate 'Deployment Rehearsal Gate' failed.
> Criteria: Rehearsal success and test coverage ≥ 90%
> Actual: {result}
> Required action: Review automation logs, remediate failures, rerun rehearsal.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 10. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_10.py

# Quality gate automation
python scripts/validate_gate_10_intake.py --drift-threshold low
python scripts/validate_gate_10_readiness.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_10.py --output .artifacts/pre-deployment/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 21 Validation
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 21 Gates
        run: python scripts/run_protocol_10_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review staging parity via infrastructure dashboards and log results.
2. Manually confirm deployment rehearsal steps using runbooks.
3. Document results in `.artifacts/protocol-21/manual-validation-log.md`

---

## 10. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 15:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 15: Production Deployment & Release Management

**Evidence Package:**
- `PRE-DEPLOYMENT-PACKAGE.zip` - Comprehensive readiness evidence
- `readiness-approval.json` - Stakeholder go/no-go decision record

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/15-production-deployment.md
```

---

## 10. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `intake-validation-report.json` | `.artifacts/pre-deployment/` | Confirms prerequisite readiness | Protocol 21 Gates |
| `staging-parity-report.json` | `.artifacts/pre-deployment/` | Documents config parity | Protocol 21 |
| `staging-test-results.json` | `.artifacts/pre-deployment/` | Captures rehearsal test outcomes | Protocol 15/12 |
| `rollback-verification-report.json` | `.artifacts/pre-deployment/` | Validates rollback readiness | Protocol 20 |
| `PRE-DEPLOYMENT-PACKAGE.zip` | `.artifacts/pre-deployment/` | Final readiness package | Protocol 15 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 2 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
