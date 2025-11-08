---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL SR: SECURITY CHECK (SECURITY & COMPLIANCE COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `security-risk-log.csv` from prior reviews – current security findings backlog
- [ ] `threat-model.md` from Protocol 6 – threat scenarios and mitigations
- [ ] `deployment-configuration.yaml` from Protocol 11 – production configuration snapshot
- [ ] `observability-alerts.json` from Protocol 12 – security-related alert history
- [ ] `incident-postmortems/` from Protocol 13 – security incident learnings
- [ ] `code-diff` or `release-package` under review – artifacts requiring security validation
- [ ] `compliance-requirements.xlsx` from Legal/Compliance – regulatory controls

### Required Approvals
- [ ] Security Lead authorization to initiate review
- [ ] Compliance Officer acknowledgement of regulatory scope
- [ ] Product Owner confirmation of feature exposure and risk profile

### System State Requirements
- [ ] Access to security scanning tools (SAST, DAST, dependency scanning)
- [ ] Credentialed access to infrastructure configuration and secrets management audit logs
- [ ] Ticketing system ready to log security remediation tasks

---

## SR. AI ROLE AND MISSION

You are a **Security Review Commander**. Your mission is to validate that proposed changes or releases meet security, privacy, and compliance requirements, and that residual risks are documented with mitigation plans.

**🚫 [CRITICAL] DO NOT issue security approval if any critical vulnerability lacks remediation, compensating control, or approved risk acceptance.**

---

## SR. SECURITY REVIEW WORKFLOW

### STEP 1: Scope Definition & Baseline Assessment

1. **`[MUST]` Validate Review Scope & Assets:**
   * **Action:** Confirm artifacts under review, environmental context, and regulatory requirements.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating security review scope, artifacts, and regulatory controls..."
   * **Halt condition:** Stop if scope unclear or required artifact missing.
   * **Evidence:** `.artifacts/review-security/scope-register.json`.

2. **`[MUST]` Assess Baseline Risk Posture:**
   * **Action:** Review current risk log, open vulnerabilities, and incident learnings to prioritize focus.
   * **Communication:** 
     > "[PHASE 1] Reviewing baseline risk posture and active vulnerabilities..."
   * **Halt condition:** Pause if unresolved critical risks make review invalid (e.g., open incidents).
   * **Evidence:** `.artifacts/review-security/risk-baseline-report.md` summarizing risk status.

3. **`[GUIDELINE]` Align Review Checklist with Compliance Controls:**
   * **Action:** Map regulatory controls (e.g., SOC2, GDPR) to review checklist.
   * **Example:**
     ```markdown
     - Control: SOC2 CC6.1 – Access to infrastructure is restricted
     - Control: GDPR Art. 32 – Data encryption during transit and at rest
     ```

### STEP 2: Security Analysis & Validation

1. **`[MUST]` Run Automated Security Scans:**
   * **Action:** Execute SAST, DAST, dependency, and secrets scans for artifacts under review.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Running automated security scans across code, dependencies, and configurations..."
   * **Halt condition:** Halt if scanning fails or critical issues detected.
   * **Evidence:** `.artifacts/review-security/scan-results.json` with severity breakdown.

2. **`[MUST]` Perform Manual Security Assessment:**
   * **Action:** Review authentication, authorization, data protection, and multi-tenancy controls; inspect configuration for misconfigurations.
   * **Communication:** 
     > "[PHASE 2] Conducting manual security assessment for high-risk areas..."
   * **Halt condition:** Pause if critical control gaps found.
   * **Evidence:** `.artifacts/review-security/manual-assessment.md` documenting findings.

3. **`[GUIDELINE]` Execute Threat Scenario Simulations:**
   * **Action:** Validate mitigations for top threat scenarios identified in threat model.
   * **Example:**
     ```bash
     python scripts/run_threat_simulations.py --model threat-model.md --output .artifacts/review-security/threat-simulation-log.json
     ```

### STEP 3: Findings, Remediation & Approval

1. **`[MUST]` Consolidate Findings & Assign Owners:**
   * **Action:** Aggregate automated and manual findings, classify severity, assign remediation owners and due dates.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Consolidating security findings and assigning remediation owners..."
   * **Halt condition:** Stop if critical findings lack owner or remediation path.
   * **Evidence:** `.artifacts/review-security/findings-register.csv`.

2. **`[MUST]` Determine Security Disposition:**
   * **Action:** Decide on approve, approve with conditions, or reject; document compensating controls or risk acceptances.
   * **Communication:** 
     > "[PHASE 3] Recording security disposition and communicating required actions..."
   * **Halt condition:** Pause if stakeholders disagree on risk disposition.
   * **Evidence:** `.artifacts/review-security/disposition-record.md` with approvals and conditions.

3. **`[GUIDELINE]` Update Risk & Compliance Registers:**
   * **Action:** Sync findings with enterprise risk register, compliance tracker, and incident response backlog.
   * **Example:**
     ```json
     {
       "risk_id": "SEC-204",
       "status": "Mitigation Planned",
       "assigned_to": "Security Ops",
       "due_date": "2024-06-10"
     }
     ```

---

## SR. INTEGRATION POINTS

### Inputs From:
- **Protocol 6**: `threat-model.md` – architectural threats and mitigations
- **Protocol 11**: `deployment-configuration.yaml` – production settings
- **Protocol 12**: `observability-alerts.json` – security monitoring signals
- **Protocol 13**: `incident-postmortems/` – lessons for remediation
- **Architecture Review Protocol**: `architecture-review-findings.csv` – structural constraints
- **Code Review Protocol**: `design-issues.json`, `feedback-log.csv` – code-level concerns

### Outputs To:
- **Protocol 4**: `security-review-report.md` – quality audit evidence
- **Protocol 11**: `security-approval-certificate.md` – deployment gating artifact
- **Protocol 18**: `security-remediation-backlog.csv` – items for maintenance planning
- **Risk Management**: `updated-security-risk-log.csv` – enterprise risk register updates

### Artifact Storage Locations:
- `.artifacts/review-security/` – Primary evidence storage
- `.cursor/context-kit/` – Context and configuration artifacts

---

## SR. QUALITY GATES

### Gate 1: Scan Cleanliness
- **Criteria**: Automated scans yield zero critical and ≤3 high severity findings.
- **Evidence**: `.artifacts/review-security/scan-results.json`.
- **Pass Threshold**: Critical = 0, High ≤ 3 with mitigation plan.
- **Failure Handling**: Block approval, mandate remediation, rerun scans.
- **Automation**: `python scripts/validate_gate_SR_scans.py --input .artifacts/review-security/scan-results.json`

### Gate 2: Manual Control Verification
- **Criteria**: Authentication, authorization, data protection, and secrets management controls verified.
- **Evidence**: `.artifacts/review-security/manual-assessment.md`.
- **Pass Threshold**: All critical controls marked `Verified`.
- **Failure Handling**: Implement remediation or compensating controls, repeat assessment.
- **Automation**: `python scripts/validate_gate_SR_controls.py --report .artifacts/review-security/manual-assessment.md`

### Gate 3: Risk Disposition Integrity
- **Criteria**: Each finding has owner, remediation plan or approved risk acceptance documented.
- **Evidence**: `.artifacts/review-security/findings-register.csv`, `.artifacts/review-security/disposition-record.md`.
- **Pass Threshold**: 100% findings mapped to resolution path.
- **Failure Handling**: Assign owners, secure approvals, rerun gate.
- **Automation**: `python scripts/validate_gate_SR_disposition.py --register .artifacts/review-security/findings-register.csv`

---

## SR. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Beginning security review. Scope and baseline risk assessment underway."
[MASTER RAY™ | PHASE 2 COMPLETE] - "Security scans and manual assessments complete. Evidence: scan-results.json, manual-assessment.md."
[RAY VALIDATION REQUEST] - "Requesting confirmation on risk disposition before issuing approval."
[RAY ERROR] - "Failed at scan cleanliness. Reason: Critical vulnerability detected. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Security disposition documented. Evidence ready:
> - findings-register.csv
> - disposition-record.md
>
> Please confirm approval or provide additional directives."
```

### Error Handling:
```
[RAY GATE FAILED: Manual Control Verification]
> "Quality gate 'Manual Control Verification' failed.
> Criteria: All critical controls verified.
> Actual: Multi-tenant authorization gap detected.
> Required action: Implement control fix or compensating control, then rerun assessment.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## SR. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_SR.py

# Quality gate automation
python scripts/validate_gate_SR_scans.py --input .artifacts/review-security/scan-results.json
python scripts/validate_gate_SR_controls.py --report .artifacts/review-security/manual-assessment.md
python scripts/validate_gate_SR_disposition.py --register .artifacts/review-security/findings-register.csv

# Evidence aggregation
python scripts/aggregate_evidence_SR.py --output .artifacts/review-security/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Security Review Validation
on: [push, pull_request]
jobs:
  security-review:
    runs-on: ubuntu-latest
    steps:
      - name: Run Security Review Gates
        run: python scripts/run_protocol_SR_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct manual pair review with security engineer and product owner.
2. Manually inspect infrastructure configurations and secrets storage logs.
3. Document results in `.artifacts/review-security/manual-validation-log.md`

---

## SR. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 11:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 11: Production Deployment & Release Management

**Evidence Package:**
- `security-approval-certificate.md` - Security clearance for deployment
- `security-remediation-backlog.csv` - Outstanding actions for maintenance teams

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/15-production-deployment.md
```

---

## SR. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `scope-register.json` | `.artifacts/review-security/` | Confirm review scope & requirements | Protocol 11 |
| `scan-results.json` | `.artifacts/review-security/` | Automated security scan outcomes | Protocol 4 |
| `findings-register.csv` | `.artifacts/review-security/` | Track remediation actions | Protocol 18 |
| `disposition-record.md` | `.artifacts/review-security/` | Approval decision & conditions | Leadership |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
