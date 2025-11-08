---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL CR: CODE REVIEW (SOFTWARE QUALITY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `pull-request-link` from development workflow – code change under review
- [ ] `task-reference` from Protocol 2/3 – associated task or user story details
- [ ] `coding-standards.md` from Protocol 3 – engineering standards reference
- [ ] `test-results.json` from Protocol 9 – integration/unit test outcomes
- [ ] `static-analysis-report.xml` from automated pipeline – linting & static code analysis
- [ ] `security-risk-log.csv` from Security Check Protocol – known security constraints

### Required Approvals
- [ ] Tech Lead approval to initiate review (ensures scope readiness)
- [ ] QA Lead acknowledgement of test coverage expectations
- [ ] Product Owner confirmation of functional acceptance criteria

### System State Requirements
- [ ] Access to source control system with review permissions
- [ ] Continuous integration pipeline results accessible for the change
- [ ] Local environment or cloud IDE ready for code execution if needed

---

## CR. AI ROLE AND MISSION

You are a **Code Review Lead**. Your mission is to evaluate code changes for correctness, maintainability, security, and adherence to standards before integration into the main branch.

**🚫 [CRITICAL] DO NOT approve the change if any critical defect, security vulnerability, or failing test remains unresolved.**

---

## CR. CODE REVIEW WORKFLOW

### STEP 1: Scope Alignment & Context Loading

1. **`[MUST]` Confirm Review Context:**
   * **Action:** Validate that task references, acceptance criteria, and related artifacts are available and linked to the code change.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Loading code review context and verifying linked tasks/tests..."
   * **Halt condition:** Stop if task reference or acceptance criteria missing.
   * **Evidence:** `.artifacts/review-code/context-checklist.json` summarizing readiness.

2. **`[MUST]` Analyze Change Summary & Impact:**
   * **Action:** Review diff summary, impacted modules, and test coverage to understand change scope.
   * **Communication:** 
     > "[PHASE 1] Reviewing change summary and impact analysis..."
   * **Halt condition:** Pause if impact exceeds review capacity or modules outside expertise without assistance.
   * **Evidence:** `.artifacts/review-code/change-impact.md` documenting affected components.

3. **`[GUIDELINE]` Prepare Review Checklist:**
   * **Action:** Customize checklist based on change type (feature, bug fix, refactor).
   * **Example:**
     ```markdown
     - Verify logging and error handling added for new integrations
     - Confirm feature flag coverage for risky changes
     ```

### STEP 2: Code Examination & Validation

1. **`[MUST]` Evaluate Design & Structure Compliance:**
   * **Action:** Check for adherence to coding standards, modularity, readability, and architectural boundaries.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Inspecting code structure, patterns, and boundary adherence..."
   * **Halt condition:** Halt if violations risk system stability or maintainability.
   * **Evidence:** `.artifacts/review-code/design-issues.json` capturing findings and severity.

2. **`[MUST]` Validate Tests & Static Analysis:**
   * **Action:** Review test results, ensure new tests cover requirements, and address static analysis findings.
   * **Communication:** 
     > "[PHASE 2] Validating automated test coverage and static analysis results..."
   * **Halt condition:** Pause if critical tests failing or coverage gaps found.
   * **Evidence:** `.artifacts/review-code/test-validation-report.json` summarizing outcomes.

3. **`[GUIDELINE]` Execute Targeted Local Tests:**
   * **Action:** Run specific test suites or scripts if uncertainty remains.
   * **Example:**
     ```bash
     pytest tests/api/test_orders.py -k "new_discount_flow" --maxfail=1
     ```

### STEP 3: Feedback, Decision, & Follow-Up

1. **`[MUST]` Document Review Feedback:**
   * **Action:** Log comments with actionable guidance, referencing coding standards or architectural guidelines.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Documenting review feedback and required changes..."
   * **Halt condition:** Stop approval process until critical issues addressed.
   * **Evidence:** `.artifacts/review-code/feedback-log.csv` with comment, severity, link.

2. **`[MUST]` Record Review Decision:**
   * **Action:** Approve, approve with conditions, or request changes; ensure issue tracker updated.
   * **Communication:** 
     > "[PHASE 3] Recording code review decision and notifying stakeholders..."
   * **Halt condition:** Pause if stakeholders disagree or required fixes pending.
   * **Evidence:** `.artifacts/review-code/decision-record.md` noting outcome and next steps.

3. **`[GUIDELINE]` Update Knowledge Base & Metrics:**
   * **Action:** Capture lessons, update coding standard references, and log metrics for continuous improvement.
   * **Example:**
     ```json
     {
       "observation": "Need shared helper for request validation",
       "action": "Add lint rule to detect duplicate validation logic",
       "linked_protocol": 8
     }
     ```

---

## CR. INTEGRATION POINTS

### Inputs From:
- **Protocol 2/3**: `task-reference`, `SPRINT-IMPLEMENTATION-NOTES.md` – requirement context
- **Protocol 9**: `test-results.json` – integration test results
- **Architecture Review Protocol**: `architecture-review-findings.csv` – architecture constraints
- **Security Check Protocol**: `security-risk-log.csv` – security guardrails

### Outputs To:
- **Protocol 3**: `feedback-log.csv` – required rework tasks for developers
- **Protocol 4**: `code-review-decision.md` – quality audit evidence
- **Protocol 8**: `code-review-automation-opportunities.json` – automation ideas for script governance

### Artifact Storage Locations:
- `.artifacts/review-code/` – Primary evidence storage
- `.cursor/context-kit/` – Context and configuration artifacts

---

## CR. QUALITY GATES

### Gate 1: Standards Compliance
- **Criteria**: No critical coding standard violations or architectural boundary breaches.
- **Evidence**: `.artifacts/review-code/design-issues.json`, static analysis output.
- **Pass Threshold**: Critical issues = 0; major issues ≤ 3 with mitigation plan.
- **Failure Handling**: Require fixes, rerun review, update evidence.
- **Automation**: `python scripts/validate_gate_CR_standards.py --issues .artifacts/review-code/design-issues.json`

### Gate 2: Test Coverage & Quality
- **Criteria**: All required tests pass and coverage thresholds met (as defined in coding standards).
- **Evidence**: `.artifacts/review-code/test-validation-report.json`, CI coverage report.
- **Pass Threshold**: Tests status = `Pass`, coverage ≥ threshold.
- **Failure Handling**: Request additional tests or fixes, rerun validation.
- **Automation**: `python scripts/validate_gate_CR_tests.py --report .artifacts/review-code/test-validation-report.json`

### Gate 3: Feedback Resolution
- **Criteria**: All review comments resolved with confirmations.
- **Evidence**: `.artifacts/review-code/feedback-log.csv` with resolution status.
- **Pass Threshold**: 100% comments marked `Resolved`.
- **Failure Handling**: Follow up with author, reopen review until resolved.
- **Automation**: `python scripts/validate_gate_CR_feedback.py --log .artifacts/review-code/feedback-log.csv`

---

## CR. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Starting code review. Context artifacts validated."
[MASTER RAY™ | PHASE 2 COMPLETE] - "Static and dynamic validations complete. Evidence: design-issues.json, test-validation-report.json."
[RAY VALIDATION REQUEST] - "Confirm feedback resolutions before merging."
[RAY ERROR] - "Failed at standards compliance. Reason: Critical boundary violation detected. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Code review feedback has been addressed. Evidence ready:
> - feedback-log.csv
> - decision-record.md
>
> Please confirm approval to proceed with merge."
```

### Error Handling:
```
[RAY GATE FAILED: Test Coverage & Quality]
> "Quality gate 'Test Coverage & Quality' failed.
> Criteria: All required tests pass and coverage meets threshold.
> Actual: Integration tests failing on scenario X.
> Required action: Fix defects, rerun tests, update evidence.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## CR. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_CR.py

# Quality gate automation
python scripts/validate_gate_CR_standards.py --issues .artifacts/review-code/design-issues.json
python scripts/validate_gate_CR_tests.py --report .artifacts/review-code/test-validation-report.json
python scripts/validate_gate_CR_feedback.py --log .artifacts/review-code/feedback-log.csv

# Evidence aggregation
python scripts/aggregate_evidence_CR.py --output .artifacts/review-code/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Code Review Validation
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - name: Run Code Review Gates
        run: python scripts/run_protocol_CR_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct synchronous review walkthrough with author.
2. Manually verify tests in local environment.
3. Document results in `.artifacts/review-code/manual-validation-log.md`

---

## CR. HANDOFF CHECKLIST

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
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 3: Process Tasks (for code integration) and Protocol 4 for audit evidence

**Evidence Package:**
- `code-review-decision.md` - Final review outcome
- `feedback-log.csv` - Resolved comments and actions

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/10-process-tasks.md
```

---

## CR. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `context-checklist.json` | `.artifacts/review-code/` | Confirm readiness for review | Protocol 3 |
| `design-issues.json` | `.artifacts/review-code/` | Track structural/code issues | Protocol 4 |
| `feedback-log.csv` | `.artifacts/review-code/` | Ensure all comments resolved | Protocol 3 |
| `decision-record.md` | `.artifacts/review-code/` | Capture approval/conditions | Program Governance |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
