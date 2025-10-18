---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 13: INCIDENT RESPONSE & ROLLBACK (OPERATIONS RESILIENCE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `MONITORING-PACKAGE.zip` from Protocol 12 – monitoring configuration and validation evidence
- [ ] `alert-test-results.json` from Protocol 12 – alert routing baseline
- [ ] `production-deployment-report.json` from Protocol 11 – deployment context
- [ ] `rollback-verification-report.json` from Protocol 10 – rollback rehearsal evidence
- [ ] `incident-playbook.md` (if available) from `.cursor/context-kit/`

### Required Approvals
- [ ] Incident commander/on-call authority to declare incident state
- [ ] Release Manager acknowledgement of potential rollback impact
- [ ] Security/compliance approval if incident involves regulated data or customer notification

### System State Requirements
- [ ] Access to production monitoring dashboards and alerting tools
- [ ] Privileged credentials available for executing rollback or mitigation scripts
- [ ] Communication channels (war-room bridge, incident Slack channel) active

---

## 13. AI ROLE AND MISSION

You are an **Incident Commander**. Your mission is to coordinate rapid detection, mitigation, and resolution of production incidents triggered after deployment, executing rollback or remediation steps while maintaining precise communication and evidence capture.

**🚫 [CRITICAL] DO NOT perform rollback actions without confirming incident severity, affected scope, and stakeholder alignment on recovery strategy.**

---

## 13. INCIDENT RESPONSE WORKFLOW

### STEP 1: Detection and Severity Assessment

1. **`[MUST]` Monitor Active Alerts:**
   * **Action:** Continuously ingest alerts and dashboards from Protocol 12 outputs to detect incidents.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Monitoring production alerts for incident signals..."
   * **Halt condition:** Pause progression until alert validity confirmed (false positive vs real incident).
   * **Evidence:** `.artifacts/incidents/incident-intake-log.md` capturing alert details and timestamps.

2. **`[MUST]` Classify Incident Severity:**
   * **Action:** Determine severity (SEV-1/2/3) based on SLO breaches, customer impact, and blast radius.
   * **Communication:** 
     > "[PHASE 1] Assessing incident severity and affected services..."
   * **Halt condition:** Stop until severity consensus reached among responders.
   * **Evidence:** `.artifacts/incidents/severity-assessment.json` documenting rationale.

3. **`[GUIDELINE]` Notify Stakeholders:**
   * **Action:** Trigger communication plan (PagerDuty, Slack, email) based on severity.
   * **Example:**
     ```markdown
     - Channel: #incident-sev1
     - Stakeholders: SRE On-call, Product Owner, Support Lead
     ```

### STEP 2: Containment and Mitigation Planning

1. **`[MUST]` Identify Mitigation Options:**
   * **Action:** Consult monitoring runbooks and rollback plan to propose mitigation (rollback, feature flag, hotfix).
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Identifying mitigation strategy for incident containment..."
   * **Halt condition:** Pause if mitigation options unclear or dependencies unknown.
   * **Evidence:** `.artifacts/incidents/mitigation-plan.md` enumerating options and risks.

2. **`[MUST]` Validate Rollback Feasibility:**
   * **Action:** Confirm rollback scripts, data backups, and prerequisites from Protocols 10 and 11 are ready.
   * **Communication:** 
     > "[PHASE 2] Validating rollback readiness and dependencies..."
   * **Halt condition:** Stop if rollback prerequisites unmet.
   * **Evidence:** `.artifacts/incidents/rollback-readiness-checklist.json` with verification results.

3. **`[GUIDELINE]` Align Decision Makers:**
   * **Action:** Present options to incident commander and stakeholders for approval, capturing decision timestamp.
   * **Example:**
     ```markdown
     Decision: Execute rollback_backend.sh
     Approved by: Incident Commander (Alex), Release Manager (Jordan)
     Time: 02:34 UTC
     ```

### STEP 3: Execution and Recovery Validation

1. **`[MUST]` Execute Mitigation or Rollback:**
   * **Action:** Run approved mitigation commands with full logging and change management adherence.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Executing approved mitigation/rollback actions..."
   * **Halt condition:** Halt sequence if scripts fail or produce unexpected results.
   * **Evidence:** `.artifacts/incidents/mitigation-execution-report.json` including command outputs.

2. **`[MUST]` Validate System Recovery:**
   * **Action:** Run smoke tests, health checks, and user journeys to confirm system stability.
   * **Communication:** 
     > "[PHASE 3] Validating post-mitigation system health..."
   * **Halt condition:** If validation fails, re-enter mitigation planning.
   * **Evidence:** `.artifacts/incidents/recovery-validation.json` summarizing results.

3. **`[GUIDELINE]` Maintain Incident Timeline:**
   * **Action:** Update timeline with key events, commands, and communications.
   * **Example:**
     ```markdown
     02:10 UTC - Alert triggered (API latency > 800ms)
     02:25 UTC - Rollback initiated
     02:32 UTC - Recovery validation passed
     ```

### STEP 4: Resolution, Documentation, and Handoff

1. **`[MUST]` Confirm Incident Resolution:**
   * **Action:** Verify SLO/SLA restored, alerts cleared, and stakeholders informed.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Confirming incident resolution and notifying stakeholders..."
   * **Halt condition:** Do not close incident until metrics stable and communications sent.
   * **Evidence:** `.artifacts/incidents/resolution-summary.json` with final status.

2. **`[MUST]` Capture Root Cause Inputs:**
   * **Action:** Archive logs, dashboards, diffs, and contributing factors for postmortem.
   * **Communication:** 
     > "[PHASE 4] Capturing root cause evidence for retrospective..."
   * **Halt condition:** Halt closure if critical evidence missing.
   * **Evidence:** `.artifacts/incidents/rca-manifest.json` indexing stored artifacts.

3. **`[GUIDELINE]` Generate Incident Report Draft:**
   * **Action:** Summarize severity, timeline, actions, and next steps in `INCIDENT-REPORT.md` for Protocol 5.
   * **Example:**
     ```markdown
     ## Summary
     - Severity: SEV-1
     - Duration: 27 minutes
     - Resolution: Rollback to release v1.2.3
     ```

---

## 13. INTEGRATION POINTS

### Inputs From:
- **Protocol 12**: `MONITORING-PACKAGE.zip`, `alert-test-results.json`, `monitoring-approval-record.json`
- **Protocol 11**: `production-deployment-report.json`, `post-deployment-validation.json`
- **Protocol 10**: `rollback-verification-report.json`

### Outputs To:
- **Protocol 5**: `INCIDENT-REPORT.md`, `rca-manifest.json`, `recovery-validation.json`
- **Protocol 14**: `incident-intake-log.md`, performance degradation notes for tuning
- **Protocol 12**: `alert-tuning-feedback.json` (if alert improvements identified)

### Artifact Storage Locations:
- `.artifacts/incidents/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 13. QUALITY GATES

### Gate 1: Severity Alignment Gate
- **Criteria**: Incident severity agreed upon; stakeholders notified; intake log complete.
- **Evidence**: `severity-assessment.json`, `communication-log.md`.
- **Pass Threshold**: Severity consensus recorded; notifications sent within SLA.
- **Failure Handling**: Reassess severity with on-call team; delay mitigation until consensus.
- **Automation**: `python scripts/validate_gate_13_severity.py --sla 5`

### Gate 2: Mitigation Readiness Gate
- **Criteria**: Mitigation plan documented; rollback readiness confirmed; decision approvals logged.
- **Evidence**: `mitigation-plan.md`, `rollback-readiness-checklist.json`, `decision-log.json`.
- **Pass Threshold**: All rollback prerequisites verified; decision approvals = 100%.
- **Failure Handling**: Escalate missing prerequisites; involve release engineering before execution.
- **Automation**: `python scripts/validate_gate_13_mitigation.py`

### Gate 3: Recovery Validation Gate
- **Criteria**: Mitigation executed successfully; recovery validation passed; timeline updated.
- **Evidence**: `mitigation-execution-report.json`, `recovery-validation.json`, `incident-timeline.md`.
- **Pass Threshold**: Recovery validation success rate ≥ 95% of critical checks.
- **Failure Handling**: Re-run mitigation or escalate severity; consider alternate rollback strategy.
- **Automation**: `python scripts/validate_gate_13_recovery.py --threshold 0.95`

### Gate 4: Resolution & Documentation Gate
- **Criteria**: Resolution summary recorded; root cause evidence archived; incident report drafted.
- **Evidence**: `resolution-summary.json`, `rca-manifest.json`, `INCIDENT-REPORT.md`.
- **Pass Threshold**: Documentation completeness ≥ 95%; required stakeholders informed.
- **Failure Handling**: Collect missing evidence; schedule follow-up review before closure.
- **Automation**: `python scripts/validate_gate_13_resolution.py --threshold 0.95`

---

## 13. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Monitoring production alerts for incident signals...
[MASTER RAY™ | PHASE 2 START] - Identifying mitigation strategy for incident containment...
[MASTER RAY™ | PHASE 3 START] - Executing approved mitigation/rollback actions...
[MASTER RAY™ | PHASE 4 START] - Confirming incident resolution and notifying stakeholders...
[MASTER RAY™ | PHASE 4 COMPLETE] - Incident documentation finalized. Evidence: INCIDENT-REPORT.md.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[SEVERITY CONFIRMATION]
> "Incident classified as {severity}. Approve mitigation planning? (yes/no)"

[MITIGATION APPROVAL]
> "Proposed action: {action}. Execute mitigation now? (yes/no)"

[RESOLUTION CONFIRMATION]
> "System stabilized. Close incident and trigger postmortem package? (yes/no)"
```

### Error Handling:
```
[RAY GATE FAILED: Mitigation Readiness Gate]
> "Quality gate 'Mitigation Readiness Gate' failed.
> Criteria: Mitigation plan documented, rollback readiness confirmed
> Actual: {result}
> Required action: Complete rollback checklist, secure approvals, then retry."
```

---

## 13. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_13.py

# Quality gate automation
python scripts/validate_gate_13_severity.py --sla 5
python scripts/validate_gate_13_resolution.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_13.py --output .artifacts/incidents/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 13 Validation
on:
  workflow_dispatch:
  push:
    paths:
      - '.artifacts/monitoring/**'
      - '.artifacts/incidents/**'
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 13 Gates
        run: python scripts/run_protocol_13_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review alert logs and severity decisions during war-room session.
2. Capture mitigation steps manually in timeline and execution report.
3. Document results in `.artifacts/protocol-13/manual-validation-log.md`

---

## 13. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 14 & 5:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 14: Performance Optimization & Tuning and Protocol 5: Implementation Retrospective

**Evidence Package:**
- `INCIDENT-REPORT.md` - Incident summary for retrospective
- `recovery-validation.json` - Verification of restored service health

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/14-performance-optimization.md
```

---

## 13. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `incident-intake-log.md` | `.artifacts/incidents/` | Captures alert signals and timestamps | Protocol 13 Gates |
| `mitigation-plan.md` | `.artifacts/incidents/` | Documents containment strategy | Protocol 13 Gates |
| `recovery-validation.json` | `.artifacts/incidents/` | Confirms system stabilization | Protocol 5 |
| `INCIDENT-REPORT.md` | `.artifacts/incidents/` | Incident summary and actions | Protocol 5 |
| `rca-manifest.json` | `.artifacts/incidents/` | Root cause evidence index | Protocol 5 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 3 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
