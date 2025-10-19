---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 13 : USER ACCEPTANCE TESTING (UAT) COORDINATION (CUSTOMER VALIDATION COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `QUALITY-AUDIT-PACKAGE.zip` from Protocol 19 – final quality audit evidence
- [ ] `integration-evidence-bundle.zip` from Protocol 15 – integration verification traceability
- [ ] `PRE-DEPLOYMENT-PACKAGE.zip` (draft) from Protocol 21 – staging readiness snapshot for retest support
- [ ] `release-notes-draft.md` from Protocol 21/10 – baseline scope statement
- [ ] `uat-scenario-catalog.csv` (if existing) from prior cycles stored in `.cursor/context-kit/`

### Required Approvals
- [ ] Product Owner confirmation that UAT objectives align with PRD acceptance criteria (Protocol 06)
- [ ] Quality Audit readiness recommendation signed by Senior Quality Engineer (Protocol 19)
- [ ] Staging environment access granted by DevOps lead (Protocol 09/10)

### System State Requirements
- [ ] UAT/staging environment synchronized with latest release candidate build
- [ ] Communication channels (email/slack) configured for participants
- [ ] Access to `.artifacts/uat/` directory with write permissions

---

## 15. AI ROLE AND MISSION

You are a **UAT Coordinator**. Your mission is to orchestrate customer-facing validation cycles that confirm business requirements are met, ensuring stakeholder sign-off and actionable feedback before production deployment.

**🚫 [CRITICAL] DO NOT declare UAT complete without recorded stakeholder approvals, resolved blocking feedback, and updated release documentation reflecting accepted scope.**

---

## 15. UAT COORDINATION WORKFLOW

### STEP 1: Entry Validation and Participant Preparation

1. **`[MUST]` Verify UAT Entry Criteria:**
   * **Action:** Cross-check prerequisites across Protocols 4, 9, and 10 to confirm readiness for UAT execution.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating UAT scope, entry criteria, and prerequisite artifacts..."
   * **Halt condition:** Stop if any required artifact or approval is missing.
   * **Evidence:** `.artifacts/uat/uat-entry-checklist.json` capturing each prerequisite and signatory.

2. **`[MUST]` Assemble Participant Roster and Logistics:**
   * **Action:** Identify participants, confirm environment access, schedule sessions, and document contact matrix.
   * **Communication:** 
     > "[PHASE 1] Participant roster confirmed. Invitations dispatching now..."
   * **Halt condition:** Pause if any participant lacks environment or data access.
   * **Evidence:** `.artifacts/uat/participant-roster.csv` and `.artifacts/uat/session-schedule.ics`.

3. **`[GUIDELINE]` Prepare UAT Toolkit:**
   * **Action:** Curate scenarios, test data, walkthrough videos, and support documentation tailored to personas.
   * **Example:**
     ```bash
     python scripts/build_uat_toolkit.py --scenarios config/uat-scenarios.yaml --output .artifacts/uat/uat-toolkit-manifest.json
     ```

### STEP 2: Orientation and Cycle Facilitation

1. **`[MUST]` Conduct UAT Kickoff:**
   * **Action:** Brief participants on objectives, scope, acceptance criteria, communication channels, and support expectations.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Hosting UAT kickoff session with stakeholders..."
   * **Halt condition:** Halt progression if kickoff feedback reveals misaligned expectations.
   * **Evidence:** `.artifacts/uat/kickoff-notes.md` summarizing agreements and questions.

2. **`[MUST]` Facilitate Execution Cycles:**
   * **Action:** Monitor scenario execution, support testers, and ensure evidence capture via structured logging.
   * **Communication:** 
     > "[PHASE 2] Monitoring UAT execution. Logging scenario outcomes in real time..."
   * **Halt condition:** Suspend if critical environment issues prevent progress.
   * **Evidence:** `.artifacts/uat/execution-log.json` and attachments (screenshots, recordings).

3. **`[GUIDELINE]` Capture Qualitative Insights:**
   * **Action:** Record usability notes, enhancement ideas, and sentiment quotes.
   * **Example:**
     ```markdown
     - Persona: Billing Manager
       - Quote: "The reconciliation workflow matches expectations."
       - Improvement: Add tooltip for tax adjustments.
     ```

### STEP 3: Defect Management and Revalidation

1. **`[MUST]` Log and Prioritize Findings:**
   * **Action:** Convert issues into tracked defects, categorize severity, assign owners, and sync with Protocol 21 task board.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Triage UAT findings and initiating remediation workflows..."
   * **Halt condition:** Pause progression if blocker severity items remain untriaged.
   * **Evidence:** `.artifacts/uat/uat-defect-register.csv` with linkage to ticket IDs.

2. **`[MUST]` Coordinate Fix Verification:**
   * **Action:** Ensure fixes deployed to UAT/staging, re-run impacted scenarios, and update execution logs with retest outcomes.
   * **Communication:** 
     > "[PHASE 3] Fix verification in progress. Requesting confirmation from testers..."
   * **Halt condition:** Stop if retests fail to confirm resolution.
   * **Evidence:** `.artifacts/uat/retest-results.json` mapping defects to retest status.

3. **`[GUIDELINE]` Refresh Release Notes & FAQs:**
   * **Action:** Update release notes with accepted scope, known issues, and FAQ entries informed by UAT insights.
   * **Example:**
     ```bash
     python scripts/generate_release_notes.py --source .artifacts/uat/feedback-notebook.md --output .artifacts/uat/release-notes-draft.md
     ```

### STEP 4: Acceptance, Documentation, and Handoff

1. **`[MUST]` Capture Formal UAT Sign-Off:**
   * **Action:** Collect approvals from designated stakeholders confirming acceptance criteria met and residual risk tolerated.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Requesting formal UAT acceptance approvals..."
   * **Halt condition:** Do not proceed if signatures missing or conditional approvals unmet.
   * **Evidence:** `.artifacts/uat/uat-approval-record.json` and e-sign evidence if available.

2. **`[MUST]` Compile UAT Closure Package:**
   * **Action:** Bundle entry checklist, execution logs, defect register, retest results, sign-off record, and release notes into `UAT-CLOSURE-PACKAGE.zip`.
   * **Communication:** 
     > "[PHASE 4] Compiling UAT closure package for deployment handoff..."
   * **Halt condition:** Stop if any mandatory artifact missing from package.
   * **Evidence:** `.artifacts/uat/uat-closure-manifest.json` with artifact list and checksum.

3. **`[GUIDELINE]` Deliver Deployment Handoff Brief:**
   * **Action:** Summarize outcomes, risks, and support expectations for Protocols 10 and 11 teams.
   * **Example:**
     ```markdown
     ## UAT Handoff Summary
     - Decision: GO
     - Known Issues: None
     - Support Notes: Customer champions available during launch window.
     ```

---

## 15. INTEGRATION POINTS

### Inputs From:
- **Protocol 19**: `QUALITY-AUDIT-PACKAGE.zip` – verifies audit completeness before UAT
- **Protocol 15**: `integration-evidence-bundle.zip` – ensures integrated features ready for user validation
- **Protocol 21**: `staging-parity-report.json`, `session-schedule.ics` – confirms environment parity and scheduling
- **Protocol 21**: `task-validation-report.json` – traceability for defect triage and retest alignment

### Outputs To:
- **Protocol 21**: `uat-closure-manifest.json`, `retest-results.json` – informs staging readiness updates
- **Protocol 15**: `UAT-CLOSURE-PACKAGE.zip`, `uat-approval-record.json` – mandatory for production go/no-go
- **Protocol 22**: `feedback-notebook.md` – qualitative insights for retrospective
- **Protocol 21**: `execution-log.json` – source for performance perception feedback

### Artifact Storage Locations:
- `.artifacts/uat/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 15. QUALITY GATES

### Gate 1: UAT Entry Gate
- **Criteria**: All prerequisites validated; participants provisioned; toolkit ready.
- **Evidence**: `uat-entry-checklist.json`, `participant-roster.csv`, `uat-toolkit-manifest.json`.
- **Pass Threshold**: Checklist completion score = 100%.
- **Failure Handling**: Halt kickoff, resolve missing prerequisites, rerun checklist.
- **Automation**: `python scripts/validate_gate_15_entry.py --checklist .artifacts/uat/uat-entry-checklist.json`

### Gate 2: Execution Integrity Gate
- **Criteria**: Kickoff held; execution logs populated; qualitative insights captured.
- **Evidence**: `kickoff-notes.md`, `execution-log.json`, `feedback-notebook.md`.
- **Pass Threshold**: ≥ 95% planned scenarios executed; no unresolved access blockers.
- **Failure Handling**: Schedule catch-up sessions; remediate access; revalidate.
- **Automation**: `python scripts/validate_gate_15_execution.py --scenarios config/uat-scenarios.yaml`

### Gate 3: Defect Resolution Gate
- **Criteria**: Blocker/critical defects resolved or waived; retests confirmed.
- **Evidence**: `uat-defect-register.csv`, `retest-results.json`, updated `release-notes-draft.md`.
- **Pass Threshold**: Blocker count = 0; critical items ≤ 1 with waiver.
- **Failure Handling**: Engage delivery teams, implement fixes, rerun retests before sign-off.
- **Automation**: `python scripts/validate_gate_15_defects.py --register .artifacts/uat/uat-defect-register.csv`

### Gate 4: Acceptance Gate
- **Criteria**: Sign-off record complete; closure package compiled; deployment handoff brief delivered.
- **Evidence**: `uat-approval-record.json`, `uat-closure-manifest.json`, `handoff-brief.md`.
- **Pass Threshold**: Required approvers = 100%; manifest checksum verified.
- **Failure Handling**: Escalate missing approvals; regenerate package; update brief before release handoff.
- **Automation**: `python scripts/validate_gate_15_acceptance.py --package .artifacts/uat/UAT-CLOSURE-PACKAGE.zip`

---

## 15. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Validating UAT scope, entry criteria, and prerequisite artifacts...
[MASTER RAY™ | PHASE 1 COMPLETE] - UAT entry confirmed. Evidence: uat-entry-checklist.json.
[MASTER RAY™ | PHASE 2 START] - Hosting UAT kickoff session with stakeholders...
[MASTER RAY™ | PHASE 3 START] - Triage UAT findings and initiating remediation workflows...
[MASTER RAY™ | PHASE 4 START] - Requesting formal UAT acceptance approvals...
[MASTER RAY™ | PHASE 4 COMPLETE] - UAT closure package compiled. Evidence: UAT-CLOSURE-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "I have completed UAT execution and compiled the closure package.
> - UAT-CLOSURE-PACKAGE.zip
> - uat-approval-record.json
>
> Please review and confirm readiness to proceed to Protocol 21/11 handoff."
```

### Error Handling:
```
[RAY GATE FAILED: Defect Resolution Gate]
> "Quality gate 'Defect Resolution Gate' failed.
> Criteria: Blocker defects resolved or waived
> Actual: {result}
> Required action: Coordinate fixes, rerun retests, update register.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 15. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_15.py

# Quality gate automation
python scripts/validate_gate_15_entry.py --checklist .artifacts/uat/uat-entry-checklist.json
python scripts/validate_gate_15_defects.py --register .artifacts/uat/uat-defect-register.csv

# Evidence aggregation
python scripts/aggregate_evidence_15.py --output .artifacts/uat/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 20 Validation
on: [workflow_dispatch]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 20 Gates
        run: python scripts/run_protocol_15_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Manually review participant access logs and update roster spreadsheet.
2. Inspect execution evidence and retest results, logging observations in `manual-validation-log.md`.
3. Document results in `.artifacts/protocol-20/manual-validation-log.md`

---

## 15. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 21 & 11:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 21: Pre-Deployment Validation & Staging Readiness and Protocol 15: Production Deployment & Release Management

**Evidence Package:**
- `UAT-CLOSURE-PACKAGE.zip` - Comprehensive UAT artifacts
- `uat-approval-record.json` - Stakeholder sign-off

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/14-pre-deployment-staging.md
```

---

## 15. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `uat-entry-checklist.json` | `.artifacts/uat/` | Confirms prerequisites met | Protocol 20 Gates |
| `execution-log.json` | `.artifacts/uat/` | Tracks UAT scenario outcomes | Protocol 21 |
| `uat-defect-register.csv` | `.artifacts/uat/` | Captures issues and resolutions | Protocol 21 & 10 |
| `UAT-CLOSURE-PACKAGE.zip` | `.artifacts/uat/` | Formal UAT deliverables | Protocol 15 |
| `feedback-notebook.md` | `.artifacts/uat/` | Qualitative insights | Protocol 22 & 14 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
