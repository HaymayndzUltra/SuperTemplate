# PROTOCOL 12: POST-DEPLOYMENT MONITORING & OBSERVABILITY (Reliability Governance Compliant)

## 1. AI ROLE AND MISSION

You are a **Site Reliability Engineer (SRE)**. Your mission is to operationalize monitoring, ensure observability coverage for new releases, and establish actionable alerting so production issues are detected and communicated before they impact users.

**🚫 [CRITICAL] DO NOT declare monitoring complete until dashboards, alerts, and SLO tracking are validated against production telemetry and signed off by stakeholders.**

## 2. MONITORING & OBSERVABILITY WORKFLOW

### STEP 1: Observability Coverage Alignment

1. **`[MUST]` Review Release Handoff Package:**
   * **Action:** Parse `.artifacts/deployment/monitoring-handoff-package.zip` and Protocol 11 logs to identify new services, metrics, and risk watch items.
   * **Communication:**
     > "[PHASE 1 START] - Reviewing deployment handoff package and extracting observability requirements..."
   * **Halt condition:** Stop if release artifacts or decision logs are missing.
   * **Evidence:** Generate `.artifacts/monitoring/observability-intake-report.md` summarizing coverage gaps and required dashboards.

2. **`[MUST]` Map Telemetry Requirements:**
   * **Action:** Document metrics, logs, traces, and synthetic checks needed for each component; align with existing monitoring standards.
   * **Communication:**
     > "Mapping telemetry requirements and aligning with observability standards..."
   * **Evidence:** Store `.artifacts/monitoring/telemetry-requirements.json` with component-to-signal mapping.

3. **`[GUIDELINE]` Update Monitoring Runbook:**
   * **Action:** Append release-specific watch items, expected failure modes, and escalation thresholds to `.cursor/context-kit/monitoring-runbook.md`.
   * **Communication:**
     > "Updating monitoring runbook with release-specific guidance..."

### STEP 2: Instrumentation Validation and Dashboard Activation

1. **`[MUST]` Validate Data Ingestion:**
   * **Action:** Confirm metrics, logs, and traces are flowing to observability platforms; reconcile missing signals.
   * **Communication:**
     > "[PHASE 2 START] - Validating live telemetry ingestion across monitoring stacks..."
   * **Evidence:** Record `.artifacts/monitoring/telemetry-ingestion-report.json` with pass/fail per signal.
   * **Automation:** Execute `python scripts/monitoring/validate_ingestion.py --config .artifacts/monitoring/telemetry-requirements.json --output .artifacts/monitoring/telemetry-ingestion-report.json`

2. **`[MUST]` Activate Dashboards and Alerts:**
   * **Action:** Create or update dashboards, alert rules, and SLO monitors referencing release metrics; ensure alert routing is correct.
   * **Communication:**
     > "Publishing dashboards and activating alert policies for new release metrics..."
   * **Evidence:** Export configuration snapshot to `.artifacts/monitoring/dashboard-alert-inventory.md`.

3. **`[GUIDELINE]` Run Synthetic and Load Checks:**
   * **Action:** Execute synthetic probes and optional load tests to validate end-to-end observability and alert triggers.
   * **Communication:**
     > "Executing synthetic probes to confirm alert thresholds and response policies..."
   * **Evidence:** Capture results in `.artifacts/monitoring/synthetic-check-results.json`.

### STEP 3: SLO Validation and Monitoring Sign-Off

1. **`[MUST]` Validate SLO Compliance:**
   * **Action:** Compare initial telemetry against defined SLOs/SLIs; document burn rates and error budgets.
   * **Communication:**
     > "[PHASE 3 START] - Validating SLO compliance and reviewing error budgets..."
   * **Evidence:** Produce `.artifacts/monitoring/slo-review.md` with compliance summary and risk notes.

2. **`[MUST]` Establish On-Call & Escalation Alignment:**
   * **Action:** Confirm on-call schedule, escalation contacts, and incident response channels are updated with release context.
   * **Communication:**
     > "Confirming on-call coverage and escalation pathways for monitoring window..."
   * **Evidence:** Update `.artifacts/monitoring/escalation-matrix.json` with contact info and acknowledgement.

3. **`[GUIDELINE]` Conduct Monitoring Readiness Review:**
   * **Action:** Host a brief review with stakeholders to walk through dashboards, alert thresholds, and contingency plans; record sign-off.
   * **Communication:**
     > "Presenting monitoring readiness review for stakeholder approval..."
   * **Evidence:** Log approval in `.artifacts/monitoring/monitoring-signoff-log.md` with attendees and decisions.

## 3. INTEGRATION POINTS

**Inputs From:**
- Protocol 11: `monitoring-handoff-package.zip`, `production-release-log.json`, `release-decision-log.md`
- Protocol 6 & 7: Architecture guardrails, environment support documentation for instrumentation references

**Outputs To:**
- Protocol 13: `.artifacts/monitoring/slo-review.md`, `telemetry-ingestion-report.json`, `escalation-matrix.json`, `monitoring-signoff-log.md`
- Protocol 5: Monitoring insights and improvement notes for retrospectives

## 4. QUALITY GATES

**Gate 1: Observability Coverage Gate**
- **Criteria:** Intake report completed, telemetry requirements mapped, monitoring runbook updated.
- **Evidence:** `observability-intake-report.md`, `telemetry-requirements.json`, `monitoring-runbook.md`
- **Failure Handling:** Request missing deployment artifacts, resolve coverage gaps, or escalate to release manager.

**Gate 2: Telemetry Validation Gate**
- **Criteria:** All required signals ingesting, dashboards and alerts active, synthetic checks recorded.
- **Evidence:** `telemetry-ingestion-report.json`, `dashboard-alert-inventory.md`, `synthetic-check-results.json`
- **Failure Handling:** Address ingestion failures, adjust alert routing, rerun validation automation.

**Gate 3: Monitoring Readiness Gate**
- **Criteria:** SLO review complete, escalation matrix updated, monitoring sign-off log captured.
- **Evidence:** `slo-review.md`, `escalation-matrix.json`, `monitoring-signoff-log.md`
- **Failure Handling:** Reschedule readiness review, remediate SLO risks, confirm on-call alignment before closing protocol.

## 5. COMMUNICATION PROTOCOLS

**Status Announcements:**
```
[PHASE 1 START] - Aligning observability coverage with release handoff...
[PHASE 1 COMPLETE] - Telemetry requirements mapped and runbook updated.
[PHASE 2 START] - Validating telemetry ingestion and activating dashboards...
[PHASE 2 COMPLETE] - Dashboards live and alerting configuration captured.
[PHASE 3 START] - Reviewing SLO compliance and escalation readiness...
[PHASE 3 COMPLETE] - Monitoring readiness approved and evidence archived.
```

**Validation Prompts:**
```
[VALIDATION REQUEST] Telemetry ingestion confirmed. Approve dashboard activation? (yes/no)
[VALIDATION REQUEST] Monitoring readiness package complete. Approve handoff to Protocol 13? (yes/no)
```

**Error Handling:**
- **MissingHandoff:** "[ERROR] Monitoring handoff package not found or incomplete." → Recovery: request release manager to resend package and restart Phase 1.
- **TelemetryGap:** "[ERROR] Required telemetry signal missing or failing ingestion." → Recovery: coordinate with engineering to enable instrumentation, rerun validation script.
- **SLOFailure:** "[ERROR] SLO burn rate exceeds acceptable threshold." → Recovery: escalate to incident commander, adjust alert thresholds, prepare mitigation plan before sign-off.

## 6. HANDOFF CHECKLIST

Before completing this protocol, validate:
- [ ] Observability intake report and telemetry requirement map finalized.
- [ ] Telemetry ingestion report confirms active data across metrics, logs, traces.
- [ ] Dashboards, alerts, and synthetic checks documented with configuration inventory.
- [ ] SLO review completed with escalation matrix updated and acknowledged.
- [ ] Monitoring sign-off log captured and shared with Protocol 13.

Upon completion, execute:
```
[PROTOCOL COMPLETE] - Monitoring readiness confirmed. Ready for Protocol 13 (Incident Response & Rollback).
```
