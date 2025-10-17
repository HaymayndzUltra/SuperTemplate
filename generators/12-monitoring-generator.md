# Protocol 12 Generator - Post-Deployment Monitoring & Observability

## 🎯 Purpose
Transform `protocol-input-form-12-monitoring.yaml` into `.cursor/ai-driven-workflow/12-monitoring-observability.md`. The generated protocol must establish observability coverage, alert validation, and monitoring handoff.

## 📥 Required Inputs
- Completed `protocol-input-form-12-monitoring.yaml`
- Monitoring artifacts from Protocol 11 (deployment logs, health metrics)
- Architecture component inventory from Protocol 6
- Access to monitoring scripts (collect_perf.py, workflow_automation.py, evidence_report.py)

## 🧠 4-Layer Mapping Blueprint
1. **Layer 1 – System-Level Decisions**
   - Persona: Site Reliability Engineer enabling post-release observability
   - Guardrail: Monitoring cannot complete without validated dashboards, alerts, and runbooks
   - Dependencies: Protocol 11 release data + architecture mapping
2. **Layer 2 – Behavioral Control**
   - Gates: Observability Coverage, Alert Readiness, Monitoring Validation
   - Halt conditions: telemetry gaps, alert routing failures, unstable metrics
   - Approval prompts for alert testing and handoff
3. **Layer 3 – Procedural Logic**
   - Phases: Observability Baseline → Alerting & Runbook Validation → Continuous Monitoring & Reporting
   - Evidence: telemetry coverage map, alert policy catalog, observation log, handoff package
   - Automation: collect_perf.py, workflow_automation.py (alert-tests), evidence_report.py
4. **Layer 4 – Communication Grammar**
   - Phase announcements, validation prompts, and error templates (TelemetryGap, AlertRoutingFailure, UnstableMetrics)

## 🏗️ Template Blueprint
```
# PROTOCOL 12: POST-DEPLOYMENT MONITORING & OBSERVABILITY (SITE RELIABILITY COMPLIANT)

## 1. AI ROLE AND MISSION
[Persona + mission + guardrail]

## 2. MONITORING ACTIVATION WORKFLOW
### STEP 1: Observability Baseline Activation
[Steps, evidence, automation]

### STEP 2: Alerting & Runbook Validation
[Alert configuration, routing tests, runbook updates]

### STEP 3: Continuous Monitoring & Reporting
[Stabilization monitoring, reporting, handoff]

## 3. INTEGRATION POINTS
[Inputs from Protocols 11 & 6; outputs to 13 & 5]

## 4. QUALITY GATES
[Observability Coverage Gate, Alert Readiness Gate, Monitoring Validation Gate]

## 5. COMMUNICATION PROTOCOLS
[Announcements, validation prompts, error handling]

## 6. AUTOMATION HOOKS
[Collect_perf, workflow_automation alert-tests, evidence_report]

## 7. HANDOFF CHECKLIST
[Checklist + completion command targeting Protocol 13]
```
- Ensure evidence storage paths use `.artifacts/monitoring/` directories.
- Include notes for synthetic monitoring optional steps.
- Reference stabilization observation period explicitly.

## 🤖 Automation & Evidence Integration
- Describe expected outputs for each automation command and how they feed into gates.
- Mention when stakeholder approval is required (SLO sign-off, alert testing, handoff approval).
- Explain packaging of monitoring artifacts for incident response.

## ✅ Quality Acceptance Checklist
**Structural**
- [ ] Sections 1–7 present and properly titled
- [ ] Steps labeled with `[MUST]`/`[GUIDELINE]` markers and include communication templates
- [ ] Evidence descriptions align with storage paths

**Content**
- [ ] Integration section references deployment artifacts and architecture map
- [ ] Quality gates use measurable criteria (coverage, alert routing success, stabilization log)
- [ ] Automation hooks match scripts named in the form
- [ ] Error handling includes TelemetryGap, AlertRoutingFailure, UnstableMetrics

**Validation**
- [ ] Handoff checklist references monitoring handoff package and observability report
- [ ] Completion command routes to Protocol 13
- [ ] Communication prompts cover alert testing approval and handoff approval

## 🔁 Circular Validation Workflow
1. Generate protocol at `.cursor/ai-driven-workflow/12-monitoring-observability.md`.
2. Execute Meta-Analysis Generator to confirm all layers and subsystems detected.
3. If coverage or communications missing, adjust protocol and re-run analysis.

## ⚠️ Failure Handling Guidance
- **Incomplete form data** → Request missing telemetry coverage or alert details.
- **Script unavailability** → Substitute with available monitoring commands; update form and generator instructions.
- **Integration mismatches** → Verify artifact names/paths from Protocol 11 and adjust accordingly.
- **Gate ambiguity** → Clarify criteria (e.g., “all critical services covered”, “alert tests deliver notifications within SLA”).
