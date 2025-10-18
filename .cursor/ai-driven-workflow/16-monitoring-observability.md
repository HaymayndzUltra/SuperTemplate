---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 12: POST-DEPLOYMENT MONITORING & OBSERVABILITY (SRE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `post-deployment-validation.json` from Protocol 15 – immediate health check results
- [ ] `deployment-health-log.md` from Protocol 15 – stabilization observations
- [ ] `DEPLOYMENT-REPORT.md` from Protocol 15 – release summary and risks
- [ ] `staging-test-results.json` from Protocol 21 – baseline test data
- [ ] Prior monitoring baselines `.artifacts/monitoring/baseline-metrics.json` (if available)

### Required Approvals
- [ ] Release Manager confirmation that production deployment completed successfully
- [ ] SRE team lead authorization to adjust monitoring configuration
- [ ] Security/compliance approval for alert thresholds impacting regulated services

### System State Requirements
- [ ] Production monitoring stack accessible (metrics, logs, traces, synthetics)
- [ ] Alerting integrations (PagerDuty/Slack/Email) operational with test credentials
- [ ] Write permissions to `.artifacts/monitoring/` and `.cursor/context-kit/`

---

## 12. AI ROLE AND MISSION

You are a **Site Reliability Engineer (SRE)**. Your mission is to activate, validate, and continuously tune observability systems immediately after production deployment so that incidents can be detected and triaged within agreed service objectives.

**🚫 [CRITICAL] DO NOT declare monitoring complete until alerting rules, dashboards, and runbooks have been validated against live production telemetry for the current release.**

---

## 12. MONITORING & OBSERVABILITY WORKFLOW

### STEP 1: Instrumentation Alignment and Baseline Capture

1. **`[MUST]` Review Deployment Outputs:**
   * **Action:** Analyze Protocol 15 artifacts to identify monitoring requirements, risky components, and new endpoints.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Reviewing deployment evidence to map monitoring requirements..."
   * **Halt condition:** Stop if required deployment artifacts missing or inconsistent.
   * **Evidence:** `.artifacts/monitoring/monitoring-requirements.md` summarizing KPIs, SLOs, and risk items.

2. **`[MUST]` Verify Instrumentation Coverage:**
   * **Action:** Ensure metrics, logs, traces, and synthetic checks cover all critical services introduced or modified.
   * **Communication:** 
     > "[PHASE 1] Validating instrumentation coverage across services and dependencies..."
   * **Halt condition:** Pause if any critical service lacks telemetry coverage.
   * **Evidence:** `.artifacts/monitoring/instrumentation-audit.json` listing coverage status per service.

3. **`[GUIDELINE]` Capture Baseline Snapshot:**
   * **Action:** Record baseline metrics immediately after deployment for reference.
   * **Example:**
     ```bash
     python scripts/collect_perf.py --env production --output .artifacts/monitoring/baseline-metrics.json
     ```

### STEP 2: Monitoring Activation and Alert Validation

1. **`[MUST]` Configure Dashboards and Alerts:**
   * **Action:** Update dashboards, alert rules, and SLO dashboards to reflect latest release changes.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Activating dashboards and alert policies..."
   * **Halt condition:** Stop if dashboards fail validation or alerts missing thresholds.
   * **Evidence:** `.artifacts/monitoring/dashboard-config.md` with links and thresholds.

2. **`[MUST]` Test Alert Paths:**
   * **Action:** Trigger synthetic incidents to confirm alert delivery, escalation, and acknowledgment.
   * **Communication:** 
     > "[PHASE 2] Triggering synthetic alerts to confirm notification pathways..."
   * **Halt condition:** Halt if alerts fail to reach on-call or acknowledgement outside SLA.
   * **Evidence:** `.artifacts/monitoring/alert-test-results.json` capturing timestamps and response times.

3. **`[GUIDELINE]` Update Runbooks:**
   * **Action:** Document new detection signals and mitigation steps in incident runbooks.
   * **Example:**
     ```markdown
     ### Updated Signals
     - Alert: API latency > 500ms (5m)
     - Response: Scale API pods + purge CDN cache
     ```

### STEP 3: Continuous Observability Assurance

1. **`[MUST]` Schedule Ongoing Checks:**
   * **Action:** Define automated cadence for verifying monitoring assets (dashboards, alerts, synthetic runs).
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Scheduling ongoing observability validation tasks..."
   * **Halt condition:** Pause if automation cannot be scheduled or lacks ownership.
   * **Evidence:** `.artifacts/monitoring/observability-schedule.json` documenting cadence and owners.

2. **`[MUST]` Correlate Alerts with Incidents:**
   * **Action:** Compare recent alerts to incident tickets, adjust thresholds for noise or missed detections.
   * **Communication:** 
     > "[PHASE 3] Correlating recent alerts with incident history to tune thresholds..."
   * **Halt condition:** Stop if correlation reveals unresolved monitoring gaps.
   * **Evidence:** `.artifacts/monitoring/alert-tuning-report.md` summarizing adjustments.

3. **`[GUIDELINE]` Publish Observability Scorecard:**
   * **Action:** Create summary of SLO attainment, alert precision, and outstanding risks for leadership review.
   * **Example:**
     ```markdown
     | Metric | Target | Actual | Status |
     |--------|--------|--------|--------|
     | Alert Precision | ≥ 85% | 87% | ✅ |
     ```

### STEP 4: Handoff and Improvement Loop

1. **`[MUST]` Deliver Monitoring Package:**
   * **Action:** Bundle instrumentation audit, dashboard configuration, alert results, and schedule into `MONITORING-PACKAGE.zip`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Delivering monitoring package to incident response and retrospective owners..."
   * **Halt condition:** Halt if package incomplete or checksum invalid.
   * **Evidence:** `.artifacts/monitoring/monitoring-package-manifest.json` plus zipped bundle.

2. **`[MUST]` Record Approval and Ownership:**
   * **Action:** Document SRE approval, on-call rotation owners, and effective date for monitoring configuration.
   * **Communication:** 
     > "[PHASE 4] Recording monitoring ownership and approvals..."
   * **Halt condition:** Pause if approvals missing or outdated.
   * **Evidence:** `.artifacts/monitoring/monitoring-approval-record.json`.

3. **`[GUIDELINE]` Queue Improvement Actions:**
   * **Action:** Log backlog items for instrumentation gaps or automation enhancements discovered.
   * **Example:**
     ```markdown
     - Task: Automate alert noise suppression for service XYZ
     - Owner: Observability Guild
     - Due: Next release cycle
     ```

---

## 12. INTEGRATION POINTS

### Inputs From:
- **Protocol 21**: `staging-test-results.json`, `observability-baseline.md` – provide expected metrics
- **Protocol 15**: `post-deployment-validation.json`, `deployment-health-log.md`, `DEPLOYMENT-REPORT.md`
- **Protocol 19**: `quality-audit-summary.json` – highlights monitoring gaps to address

### Outputs To:
- **Protocol 20**: `MONITORING-PACKAGE.zip`, `alert-test-results.json`, `monitoring-approval-record.json`
- **Protocol 21**: `baseline-metrics.json`, `instrumentation-audit.json`, `alert-tuning-report.md`
- **Protocol 22**: `observability-scorecard.md`, `improvement-backlog.md`

### Artifact Storage Locations:
- `.artifacts/monitoring/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 12. QUALITY GATES

### Gate 1: Instrumentation Coverage Gate
- **Criteria**: All critical services have telemetry coverage; monitoring requirements documented.
- **Evidence**: `monitoring-requirements.md`, `instrumentation-audit.json`.
- **Pass Threshold**: Coverage completeness ≥ 95%.
- **Failure Handling**: Engage service owners to implement missing instrumentation; rerun audit.
- **Automation**: `python scripts/validate_gate_12_instrumentation.py --threshold 0.95`

### Gate 2: Alert Validation Gate
- **Criteria**: Synthetic alerts triggered; acknowledgements within SLA; dashboards updated.
- **Evidence**: `dashboard-config.md`, `alert-test-results.json`.
- **Pass Threshold**: Alert acknowledgement time ≤ target SLA; dashboard validation score ≥ 90%.
- **Failure Handling**: Fix routing/integration issues; rerun tests before proceeding.
- **Automation**: `python scripts/validate_gate_12_alerts.py --sla 5`

### Gate 3: Observability Assurance Gate
- **Criteria**: Ongoing schedule defined; alert tuning documented; improvement backlog created.
- **Evidence**: `observability-schedule.json`, `alert-tuning-report.md`, `improvement-backlog.md`.
- **Pass Threshold**: Schedule coverage = 100%; backlog entries logged for all gaps.
- **Failure Handling**: Define schedule, add backlog actions, repeat validation.
- **Automation**: `python scripts/validate_gate_12_assurance.py`

### Gate 4: Monitoring Handoff Gate
- **Criteria**: Monitoring package compiled; approvals recorded; downstream protocols notified.
- **Evidence**: `MONITORING-PACKAGE.zip`, `monitoring-package-manifest.json`, `monitoring-approval-record.json`.
- **Pass Threshold**: Manifest completeness ≥ 95%; approvals 100% captured.
- **Failure Handling**: Rebuild package, obtain approvals, resend notifications.
- **Automation**: `python scripts/validate_gate_12_handoff.py --threshold 0.95`

---

## 12. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Reviewing deployment evidence to map monitoring requirements...
[MASTER RAY™ | PHASE 2 START] - Activating dashboards and alert policies...
[MASTER RAY™ | PHASE 3 START] - Scheduling ongoing observability validation tasks...
[MASTER RAY™ | PHASE 4 START] - Delivering monitoring package to incident response and retrospective owners...
[MASTER RAY™ | PHASE 4 COMPLETE] - Monitoring package delivered. Evidence: MONITORING-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Monitoring instrumentation and alert validation complete.
> - MONITORING-PACKAGE.zip
> - monitoring-approval-record.json
>
> Confirm readiness to transition to Protocol 20?"
```

### Error Handling:
```
[RAY GATE FAILED: Alert Validation Gate]
> "Quality gate 'Alert Validation Gate' failed.
> Criteria: Synthetic alerts acknowledged within SLA, dashboards updated
> Actual: {result}
> Required action: Repair alert routing, update dashboards, rerun tests."
```

---

## 12. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_12.py

# Quality gate automation
python scripts/validate_gate_12_instrumentation.py --threshold 0.95
python scripts/validate_gate_12_handoff.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_12.py --output .artifacts/monitoring/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 19 Validation
on:
  schedule:
    - cron: '*/30 * * * *'
  workflow_dispatch:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 19 Gates
        run: python scripts/run_protocol_12_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review dashboards and alerts manually, capturing screenshots.
2. Trigger manual alert tests and log acknowledgements in spreadsheet.
3. Document results in `.artifacts/protocol-19/manual-validation-log.md`

---

## 12. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 20:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 20: Incident Response & Rollback

**Evidence Package:**
- `MONITORING-PACKAGE.zip` - Monitoring configuration and validation bundle
- `monitoring-approval-record.json` - Ownership and approval record

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/17-incident-response-rollback.md
```

---

## 12. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `monitoring-requirements.md` | `.artifacts/monitoring/` | Maps monitoring needs to services | Protocol 19 Gates |
| `instrumentation-audit.json` | `.artifacts/monitoring/` | Coverage validation | Protocol 20/14 |
| `alert-test-results.json` | `.artifacts/monitoring/` | Confirms alert routing | Protocol 20 |
| `observability-schedule.json` | `.artifacts/monitoring/` | Automation cadence | Protocol 19 |
| `MONITORING-PACKAGE.zip` | `.artifacts/monitoring/` | Handoff deliverable | Protocol 20 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 2 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
