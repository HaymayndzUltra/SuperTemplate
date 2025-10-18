---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 9: INTEGRATION TESTING & SYSTEM VALIDATION (QUALITY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `integration-scope-matrix.json` or equivalent feature summary from Protocol 21 (if previously generated)
- [ ] `TECHNICAL-DESIGN.md`, `contract-validation-config.json` from Protocol 07
- [ ] `validation-suite-report.json`, `environment-approval-record.json` from Protocol 09
- [ ] `execution-artifact-manifest.json`, `task-state.json` from Protocol 21

### Required Approvals
- [ ] Quality orchestrator authorization to commence integration testing
- [ ] Environment owner confirmation that integration environment matches baseline

### System State Requirements
- [ ] Access to integration environment credentials, seeded datasets, and observability tooling
- [ ] Automation scripts `validate_environment.py`, `run_contract_tests.py`, integration test runner available
- [ ] Storage for evidence bundle under `.artifacts/protocol-15/`

---

## 9. AI ROLE AND MISSION

You are an **Integration Test Engineer**. Your mission is to validate cross-service workflows, interfaces, and data flows using production-like conditions, ensuring the system is ready for quality audit and staging deployment.

**🚫 [CRITICAL] Do not grant integration readiness unless all critical paths and contracts pass with evidence logged.**

---

## 9. INTEGRATION WORKFLOW

### STEP 1: Scope & Environment Alignment

1. **`[MUST]` Define Integration Scope:**
   * **Action:** Consolidate completed features, architectural interfaces, and dependencies from Protocols 3 and 6; produce `integration-scope-matrix.json` if not already created.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Aligning integration scope across delivery and architecture artifacts."
   * **Halt condition:** Stop if required artifacts missing or inconsistent.
   * **Evidence:** `.artifacts/protocol-15/integration-scope-matrix.json`

2. **`[MUST]` Validate Environment Parity:**
   * **Action:** Run `python scripts/validate_environment.py --env integration --output .artifacts/protocol-15/environment-validation-report.json` to confirm environment matches baseline configuration.
   * **Communication:** 
     > "Validating integration environment parity and service connectivity."
   * **Evidence:** `.artifacts/protocol-15/environment-validation-report.json`

3. **`[GUIDELINE]` Refresh Test Data Inventory:**
   * **Action:** Update dataset catalog with sources, refresh cadence, and anonymization notes in `test-data-inventory.md`.

### STEP 2: Test Design & Instrumentation

1. **`[MUST]` Assemble Test Plan:**
   * **Action:** Map integration scenarios to automated suites, specifying entry/exit conditions, observability hooks, and rollback steps in `integration-test-plan.md`.
   * **Communication:** 
     > "[PHASE 2] - Building integration scenarios and automation plan."
   * **Evidence:** `.artifacts/protocol-15/integration-test-plan.md`

2. **`[MUST]` Configure Contract Validation:**
   * **Action:** Execute `python scripts/run_contract_tests.py --env integration --output .artifacts/protocol-15/contract-validation-results.json` and record configuration in `contract-validation-config.json`.
   * **Evidence:** `.artifacts/protocol-15/contract-validation-results.json`

3. **`[GUIDELINE]` Verify Observability:**
   * **Action:** Ensure logging, tracing, and metrics coverage for scenarios; document in `observability-readiness.md`.

### STEP 3: Execution & Defect Management

1. **`[MUST]` Run Integration Suites:**
   * **Action:** Execute automated tests (API, workflow, migration) using commands defined in test plan; store consolidated results in `test-execution-report.json`.
   * **Communication:** 
     > "[PHASE 3] - Executing integration test suites across critical paths."
   * **Evidence:** `.artifacts/protocol-15/test-execution-report.json`

2. **`[MUST]` Log and Triage Defects:**
   * **Action:** Capture failures, create tickets, assign owners, and document remediation status in `defect-log.csv`.
   * **Halt condition:** Pause progression until critical defects receive mitigation plan.
   * **Evidence:** `.artifacts/protocol-15/defect-log.csv`

3. **`[GUIDELINE]` Perform Regression Spot-Checks:**
   * **Action:** Rerun targeted suites around resolved defects; record coverage in `regression-summary.md`.

### STEP 4: Evidence Packaging & Sign-Off

1. **`[MUST]` Compile Evidence Bundle:**
   * **Action:** Package scope matrix, environment validation, test results, defects, and regression logs into `INTEGRATION-EVIDENCE.zip`; generate manifest `integration-evidence-manifest.json`.
   * **Communication:** 
     > "[PHASE 4] - Compiling integration evidence bundle for quality audit."
   * **Evidence:** `.artifacts/protocol-15/integration-evidence-manifest.json`

2. **`[MUST]` Record Integration Sign-Off:**
   * **Action:** Capture approval details (approver, timestamp, scope) in `integration-signoff.json`.
   * **Halt condition:** Do not transition to Protocol 19 without sign-off or documented waiver.
   * **Evidence:** `.artifacts/protocol-15/integration-signoff.json`

3. **`[GUIDELINE]` Provide Forward Recommendations:**
   * **Action:** Document monitoring improvements, deployment checks, or automation gaps for Protocols 4, 10, and 12 in `forward-recommendations.md`.

---

## 9. INTEGRATION POINTS

### Inputs From:
- **Protocol 21**: `execution-artifact-manifest.json`, `task-state.json` - Completed feature and evidence references.
- **Protocol 07**: `TECHNICAL-DESIGN.md`, `architecture-boundaries.json`, `contract-validation-config.json` - Interface contracts.
- **Protocol 09**: `validation-suite-report.json`, `environment-approval-record.json` - Environment baseline validation.

### Outputs To:
- **Protocol 19**: `INTEGRATION-EVIDENCE.zip`, `integration-test-plan.md`, `defect-log.csv`, `integration-signoff.json` - Quality audit inputs.
- **Protocol 21**: `environment-validation-report.json`, `contract-validation-results.json`, `observability-readiness.md` - Pre-deployment validation.
- **Protocol 19**: `forward-recommendations.md` - Monitoring and observability guidance.

### Artifact Storage Locations:
- `.artifacts/protocol-15/` - Primary evidence storage
- `.cursor/context-kit/` - Updates to integration readiness context

---

## 9. QUALITY GATES

### Gate 1: Scope Alignment Gate
- **Criteria**: Scope matrix reconciled with architecture and execution outputs; environment validation completed.
- **Evidence**: `integration-scope-matrix.json`, `environment-validation-report.json`
- **Pass Threshold**: All services accounted for; environment parity confirmed.
- **Failure Handling**: Resolve discrepancies, rerun environment validation, update scope matrix.
- **Automation**: `python scripts/validate_environment.py --env integration --output .artifacts/protocol-15/environment-validation-report.json`

### Gate 2: Contract Assurance Gate
- **Criteria**: Contract tests executed with 100% pass or documented mitigations; observability readiness documented.
- **Evidence**: `contract-validation-results.json`, `observability-readiness.md`
- **Pass Threshold**: All critical contracts pass; instrumentation coverage ≥ 95%.
- **Failure Handling**: Coordinate fixes with component owners, rerun tests, update documentation.
- **Automation**: `python scripts/run_contract_tests.py --env integration --output .artifacts/protocol-15/contract-validation-results.json`

### Gate 3: Execution Integrity Gate
- **Criteria**: Integration suites completed; critical defects resolved or waived; regressions captured.
- **Evidence**: `test-execution-report.json`, `defect-log.csv`, `regression-summary.md`
- **Pass Threshold**: No open critical defects; regression reruns successful.
- **Failure Handling**: Block sign-off, remediate defects, rerun suites.
- **Automation**: `pytest -m integration --json-report --json-report-file .artifacts/protocol-15/test-execution-report.json`

### Gate 4: Sign-Off & Handoff Gate
- **Criteria**: Evidence bundle packaged, sign-off recorded, recommendations shared with downstream protocols.
- **Evidence**: `integration-evidence-manifest.json`, `integration-signoff.json`, `forward-recommendations.md`
- **Pass Threshold**: Approval status `approved`; bundle accessible to stakeholders.
- **Failure Handling**: Update evidence, re-request sign-off, ensure recommendations completed.
- **Automation**: `python scripts/generate_artifact_manifest.py --input .artifacts/protocol-15/ --output .artifacts/protocol-15/integration-evidence-manifest.json`

---

## 9. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Aligning integration scope and validating environment readiness."
[MASTER RAY™ | PHASE 2 START] - "Configuring contract validation and integration test plan."
[MASTER RAY™ | PHASE 3 START] - "Executing integration suites and managing defects."
[MASTER RAY™ | PHASE 4 START] - "Packaging integration evidence and seeking sign-off."
[PHASE COMPLETE] - "Integration validation complete; evidence archived in .artifacts/protocol-15/."
[RAY ERROR] - "Integration testing halted due to [issue]; refer to defect log."
```

### Validation Prompts:
```
[DEFECT REVIEW]
> "Critical integration failures detected:
> - {summary}
> Mitigation plan documented? (yes/no)"

[SIGN-OFF REQUEST]
> "Integration evidence bundle ready:
> - integration-scope-matrix.json
> - test-execution-report.json
> - defect-log.csv
> - integration-signoff.json
>
> Approve handoff to Protocol 19?"
```

### Error Handling:
```
[RAY GATE FAILED: Execution Integrity Gate]
> "Quality gate 'Execution Integrity' failed.
> Criteria: All critical defects resolved or waived.
> Actual: Defect #{ID} remains open without mitigation.
> Required action: Assign owner, document mitigation, rerun affected suites.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 9. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_9.py

# Quality gate automation
python scripts/validate_environment.py --env integration --output .artifacts/protocol-15/environment-validation-report.json
python scripts/run_contract_tests.py --env integration --output .artifacts/protocol-15/contract-validation-results.json
pytest -m integration --json-report --json-report-file .artifacts/protocol-15/test-execution-report.json
python scripts/generate_artifact_manifest.py --input .artifacts/protocol-15/ --output .artifacts/protocol-15/integration-evidence-manifest.json

# Evidence aggregation
python scripts/aggregate_evidence_9.py --output .artifacts/protocol-15/
```

### CI/CD Integration:
```yaml
name: Protocol 15 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 15 Gates
        run: python scripts/run_protocol_9_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual environment verification; log in `manual-environment-check.md`.
2. Run integration smoke tests manually; store results in `.artifacts/protocol-15/manual-test-report.md`.
3. Capture manual sign-off evidence in `.artifacts/protocol-15/manual-approval-log.md`.

---

## 9. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 19:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 19: Quality Audit

**Evidence Package:**
- `INTEGRATION-EVIDENCE.zip` - Comprehensive integration validation bundle
- `integration-signoff.json` - Approval record for downstream audits

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/12-quality-audit.md
```

---

## 9. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `integration-scope-matrix.json` | `.artifacts/protocol-15/` | Scope alignment record | Protocol 19 |
| `environment-validation-report.json` | `.artifacts/protocol-15/` | Environment parity evidence | Protocol 21 |
| `contract-validation-results.json` | `.artifacts/protocol-15/` | Contract validation report | Protocol 21 |
| `test-execution-report.json` | `.artifacts/protocol-15/` | Integration suite results | Protocol 19 |
| `defect-log.csv` | `.artifacts/protocol-15/` | Defect tracking | Protocol 19 |
| `integration-signoff.json` | `.artifacts/protocol-15/` | Approval evidence | Protocol 19 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
