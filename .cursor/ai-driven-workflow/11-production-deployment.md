---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 11: PRODUCTION DEPLOYMENT & RELEASE MANAGEMENT (RELIABILITY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PRE-DEPLOYMENT-PACKAGE.zip` from Protocol 10 – readiness evidence bundle
- [ ] `readiness-approval.json` from Protocol 10 – stakeholder go decision
- [ ] `rollback-verification-report.json` from Protocol 10 – validated rollback plan
- [ ] `UAT-CLOSURE-PACKAGE.zip` from Protocol 15 – customer acceptance proof
- [ ] Latest release manifest `.artifacts/pre-deployment/deployment-checklist.md`

### Required Approvals
- [ ] Executive sponsor or Product Owner authorization to deploy to production
- [ ] SRE/Operations lead approval confirming monitoring coverage
- [ ] Security lead sign-off if release includes security-impacting changes

### System State Requirements
- [ ] Production environment credentials available with MFA satisfied
- [ ] Deployment automation scripts accessible (`scripts/deploy_*.sh`, `scripts/rollback_*.sh`)
- [ ] Monitoring dashboards and alerting tools operational for health window

---

## 11. AI ROLE AND MISSION

You are a **Release Manager**. Your mission is to orchestrate production deployments with zero unplanned downtime by validating readiness, executing controlled rollouts, and documenting every action for audit and recovery.

**🚫 [CRITICAL] DO NOT deploy to production without recorded staging success, stakeholder approval, and an executable rollback plan.**

---

## 11. PRODUCTION DEPLOYMENT WORKFLOW

### STEP 1: Readiness Verification and Approval

1. **`[MUST]` Validate Pre-Deployment Evidence:**
   * **Action:** Confirm Protocol 10 and 15 artifacts are complete, current, and free of blocking issues.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Verifying deployment readiness artifacts..."
   * **Halt condition:** Stop if any prerequisite artifact missing or outdated.
   * **Evidence:** `.artifacts/deployment/deployment-readiness-checklist.json` capturing status per artifact.

2. **`[MUST]` Confirm Release Scope and Stakeholders:**
   * **Action:** Review release manifest, impacted services, rollback procedures, and stakeholder list.
   * **Communication:** 
     > "[PHASE 1] Release scope and stakeholder confirmations underway..."
   * **Halt condition:** Pause if approvals list incomplete or scope unclear.
   * **Evidence:** `.artifacts/deployment/release-manifest.md` annotated with confirmations.

3. **`[GUIDELINE]` Schedule Deployment Window:**
   * **Action:** Coordinate release window, communications, and on-call coverage.
   * **Example:**
     ```markdown
     - Deployment window: 2024-06-01 02:00-04:00 UTC
     - Communication channels: #release-war-room
     - On-call: SRE (Alex), Product (Taylor)
     ```

### STEP 2: Staging Verification Confirmation

1. **`[MUST]` Reconfirm Staging Health:**
   * **Action:** Review Protocol 10 staging run logs and optionally rerun quick validation to ensure nothing drifted.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Reconfirming staging health prior to production launch..."
   * **Halt condition:** Stop if staging validation fails or environment drift detected.
   * **Evidence:** `.artifacts/deployment/staging-validation-results.json` (refreshed if rerun).

2. **`[MUST]` Freeze Change Window:**
   * **Action:** Communicate code freeze start, lock deployment branch, and ensure no conflicting changes queued.
   * **Communication:** 
     > "[PHASE 2] Change freeze in effect. All teams acknowledge?"
   * **Halt condition:** Pause until freeze confirmed across stakeholders.
   * **Evidence:** `.artifacts/deployment/change-freeze-confirmation.md` with acknowledgements.

3. **`[GUIDELINE]` Conduct Final Dry Run:**
   * **Action:** Execute dry-run of production scripts using `--dry-run` or staging flag to confirm command readiness.
   * **Example:**
     ```bash
     bash scripts/deploy_backend.sh --env production --release ${TAG} --dry-run
     ```

### STEP 3: Production Deployment & Immediate Validation

1. **`[MUST]` Request Production Approval:**
   * **Action:** Present readiness checklist, staging evidence, and rollback plan to approvers; capture go/no-go decision.
   * **Communication:** 
     > "[APPROVAL REQUEST] All readiness gates passed. Approve production deployment? (yes/no)"
   * **Halt condition:** Do not continue without recorded approval.
   * **Evidence:** `.artifacts/deployment/production-approval.json` with timestamps and approvers.

2. **`[MUST]` Execute Production Deployment:**
   * **Action:** Perform deployment according to rollout strategy (blue/green, canary, rolling) while logging commands.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Executing production deployment sequence..."
   * **Halt condition:** Trigger rollback if critical errors encountered.
   * **Evidence:** `.artifacts/deployment/production-deployment-report.json` capturing actions and durations.

3. **`[MUST]` Run Immediate Post-Deployment Checks:**
   * **Action:** Execute smoke tests, health checks, and service verifications within minutes of deployment completion.
   * **Communication:** 
     > "[PHASE 3] Running post-deployment validation checks..."
   * **Halt condition:** Initiate rollback if checks fail beyond tolerances.
   * **Evidence:** `.artifacts/deployment/post-deployment-validation.json` including metrics snapshot.

4. **`[GUIDELINE]` Notify Stakeholders of Deployment Progress:**
   * **Action:** Provide updates at key milestones (start, 50%, completion) in designated channels.
   * **Example:**
     ```markdown
     [RAY ANNOUNCEMENT] Production deployment 50% complete. No errors observed. Next update in 10 minutes.
     ```

### STEP 4: Stabilization Window and Documentation

1. **`[MUST]` Monitor Health Window:**
   * **Action:** Track metrics during agreed soak period, documenting anomalies and decisions.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Monitoring post-deployment health window..."
   * **Halt condition:** Escalate to Protocol 13 if thresholds breached.
   * **Evidence:** `.artifacts/deployment/deployment-health-log.md` summarizing observations.

2. **`[MUST]` Compile Release Report:**
   * **Action:** Consolidate readiness checklist, deployment logs, validation results, and monitoring data into `DEPLOYMENT-REPORT.md`.
   * **Communication:** 
     > "[PHASE 4] Compiling final release report and evidence bundle..."
   * **Halt condition:** Delay handoff until report and attachments complete.
   * **Evidence:** `.artifacts/deployment/DEPLOYMENT-REPORT.md` plus zipped evidence package `DEPLOYMENT-EVIDENCE.zip`.

3. **`[GUIDELINE]` Trigger Retrospective Inputs:**
   * **Action:** Provide summary and improvement items to Protocol 5 and log follow-up actions.
   * **Example:**
     ```markdown
     - Improvement: Automate canary rollback trigger thresholds
     - Owner: Release Engineering
     ```

---

## 11. INTEGRATION POINTS

### Inputs From:
- **Protocol 7**: `environment-validation-report.json` – baseline infrastructure readiness
- **Protocol 10**: `PRE-DEPLOYMENT-PACKAGE.zip`, `readiness-approval.json`, `deployment-checklist.md`
- **Protocol 15**: `UAT-CLOSURE-PACKAGE.zip`, `uat-approval-record.json`

### Outputs To:
- **Protocol 12**: `post-deployment-validation.json`, `deployment-health-log.md`, updated monitoring notes
- **Protocol 13**: `production-deployment-report.json`, `rollback-plan.md` (if triggered)
- **Protocol 5**: `DEPLOYMENT-REPORT.md`, `retrospective-inputs.json`
- **Protocol 14**: Metrics snapshot for performance baseline adjustments

### Artifact Storage Locations:
- `.artifacts/deployment/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 11. QUALITY GATES

### Gate 1: Readiness Confirmation Gate
- **Criteria**: All prerequisite artifacts validated; approvals recorded; rollback plan verified.
- **Evidence**: `deployment-readiness-checklist.json`, `release-manifest.md`.
- **Pass Threshold**: Checklist completion = 100%.
- **Failure Handling**: Halt deployment; resolve missing items; reschedule if necessary.
- **Automation**: `python scripts/validate_gate_11_readiness.py --checklist .artifacts/deployment/deployment-readiness-checklist.json`

### Gate 2: Approval & Change Freeze Gate
- **Criteria**: Staging health reconfirmed; change freeze acknowledged by all stakeholders.
- **Evidence**: `staging-validation-results.json`, `change-freeze-confirmation.md`.
- **Pass Threshold**: Freeze acknowledgements = 100% of required stakeholders.
- **Failure Handling**: Delay deployment; obtain acknowledgements; repeat freeze confirmation.
- **Automation**: `python scripts/validate_gate_11_freeze.py --stakeholders config/release-approvers.yaml`

### Gate 3: Production Launch Gate
- **Criteria**: Production approval recorded; deployment completed; immediate checks passed.
- **Evidence**: `production-approval.json`, `production-deployment-report.json`, `post-deployment-validation.json`.
- **Pass Threshold**: 0 blocking incidents; validation success rate ≥ 95%.
- **Failure Handling**: Execute rollback, notify stakeholders, transition to Protocol 13.
- **Automation**: `python scripts/validate_gate_11_launch.py --validation-threshold 0.95`

### Gate 4: Stabilization & Reporting Gate
- **Criteria**: Health window metrics within thresholds; release report compiled; retrospective inputs documented.
- **Evidence**: `deployment-health-log.md`, `DEPLOYMENT-REPORT.md`, `retrospective-inputs.json`.
- **Pass Threshold**: Metrics within SLO tolerances; report completeness ≥ 95%.
- **Failure Handling**: Extend monitoring window; escalate to Protocol 12/13; update report before handoff.
- **Automation**: `python scripts/validate_gate_11_reporting.py --threshold 0.95`

---

## 11. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Verifying deployment readiness artifacts...
[MASTER RAY™ | PHASE 2 START] - Reconfirming staging health prior to production launch...
[MASTER RAY™ | PHASE 3 START] - Executing production deployment sequence...
[MASTER RAY™ | PHASE 4 START] - Monitoring post-deployment health window...
[MASTER RAY™ | PHASE 4 COMPLETE] - Deployment report compiled. Evidence: DEPLOYMENT-REPORT.md.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Production deployment executed. Evidence ready:
> - production-deployment-report.json
> - post-deployment-validation.json
>
> Confirm readiness to transition to Protocol 12?"
```

### Error Handling:
```
[RAY GATE FAILED: Production Launch Gate]
> "Quality gate 'Production Launch Gate' failed.
> Criteria: Approval recorded, deployment successful, immediate checks passed
> Actual: {result}
> Required action: Initiate rollback per plan, notify stakeholders, engage Protocol 13."
```

---

## 11. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_11.py

# Quality gate automation
python scripts/validate_gate_11_readiness.py --checklist .artifacts/deployment/deployment-readiness-checklist.json
python scripts/validate_gate_11_launch.py --validation-threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_11.py --output .artifacts/deployment/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 11 Validation
on:
  workflow_dispatch:
  release:
    types: [created]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 11 Gates
        run: python scripts/run_protocol_11_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review readiness checklist and approvals manually via documented evidence.
2. Observe deployment via war-room call, logging commands in spreadsheet.
3. Document results in `.artifacts/protocol-11/manual-validation-log.md`

---

## 11. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 12:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 12: Monitoring & Observability

**Evidence Package:**
- `DEPLOYMENT-REPORT.md` - Comprehensive deployment summary
- `post-deployment-validation.json` - Initial monitoring evidence

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/12-monitoring-observability.md
```

---

## 11. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `deployment-readiness-checklist.json` | `.artifacts/deployment/` | Validates prerequisites | Protocol 11 Gates |
| `production-deployment-report.json` | `.artifacts/deployment/` | Deployment execution log | Protocol 12/13 |
| `post-deployment-validation.json` | `.artifacts/deployment/` | Immediate health check results | Protocol 12 |
| `deployment-health-log.md` | `.artifacts/deployment/` | Stabilization monitoring notes | Protocol 12/13 |
| `DEPLOYMENT-REPORT.md` | `.artifacts/deployment/` | Final release report | Protocol 5 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 3 Pass Rate | ≥ 98% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
