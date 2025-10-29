---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 13 : USER ACCEPTANCE TESTING (UAT) COORDINATION (CUSTOMER VALIDATION COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `QUALITY-AUDIT-PACKAGE.zip` from Protocol 12 – final quality audit evidence
- [ ] `INTEGRATION-EVIDENCE.zip` from Protocol 11 – integration verification traceability
- [ ] `readiness-recommendation.md` from Protocol 12 – quality audit recommendation
- [ ] `release-notes-draft.md` from Protocol 10 – baseline scope statement
- [ ] `uat-scenario-catalog.csv` (if existing) from prior cycles stored in `.cursor/context-kit/`

### Required Approvals
- [ ] Product Owner confirmation that UAT objectives align with PRD acceptance criteria (Protocol 06)
- [ ] Quality Audit readiness recommendation signed by Senior Quality Engineer (Protocol 12)
- [ ] Staging environment access granted by DevOps lead (Protocol 09)

### System State Requirements
- [ ] UAT/staging environment synchronized with latest release candidate build
- [ ] Communication channels (email/slack) configured for participants
- [ ] Access to `.artifacts/uat/` directory with write permissions

---

## 15. AI ROLE AND MISSION

You are a **UAT Coordinator**. Your mission is to orchestrate customer-facing validation cycles that confirm business requirements are met, ensuring stakeholder sign-off and actionable feedback before production deployment.

**🚫 [CRITICAL] DO NOT declare UAT complete without recorded stakeholder approvals, resolved blocking feedback, and updated release documentation reflecting accepted scope.**

---

## WORKFLOW

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


## REFLECTION & LEARNING

### Retrospective Guidance

After completing protocol execution (successful or halted), conduct retrospective:

**Timing:** Within 24-48 hours of completion

**Participants:** Protocol executor, downstream consumers, stakeholders

**Agenda:**
1. **What went well:**
   - Which steps executed smoothly and efficiently?
   - Which quality gates were well-calibrated?
   - Which artifacts provided high value to downstream protocols?

2. **What went poorly:**
   - Which steps encountered blockers or delays?
   - Which quality gates were too strict or too lenient?
   - Which artifacts required rework or clarification?

3. **Action items:**
   - Protocol template updates needed?
   - Quality gate threshold adjustments?
   - New automation opportunities?

**Output:** Retrospective report stored in protocol execution artifacts

### Continuous Improvement Opportunities

#### Identified Improvement Opportunities
- Identify based on protocol-specific execution patterns

#### Process Optimization Tracking
- Track key performance metrics over time
- Monitor quality gate pass rates and execution velocity
- Measure downstream satisfaction and rework requests
- Identify automation opportunities

#### Tracking Mechanisms and Metrics
- Quarterly metrics dashboard with trends
- Improvement tracking log with before/after comparisons
- Evidence of improvement validation

#### Evidence of Improvement and Validation
- Metric trends showing improvement trajectories
- A/B testing results for protocol changes
- Stakeholder feedback scores
- Downstream protocol satisfaction ratings

### System Evolution

#### Version History
- Current version with implementation date
- Previous versions with change descriptions
- Deprecation notices for obsolete approaches

#### Rationale for Changes
- Documented reasons for each protocol evolution
- Evidence supporting the change decision
- Expected impact assessment

#### Impact Assessment
- Measured outcomes of protocol changes
- Comparison against baseline metrics
- Validation of improvement hypotheses

#### Rollback Procedures
- Process for reverting to previous protocol version
- Triggers for initiating rollback
- Communication plan for rollback events

### Knowledge Capture and Organizational Learning

#### Lessons Learned Repository
Maintain lessons learned with structure:
- Project/execution context
- Insight or discovery
- Action taken based on insight
- Outcome and applicability

#### Knowledge Base Growth
- Systematic extraction of patterns from executions
- Scheduled knowledge base updates
- Quality metrics for knowledge base content

#### Knowledge Sharing Mechanisms
- Internal distribution channels
- Onboarding integration
- Cross-team learning sessions
- Access controls and search tools

### Future Planning

#### Roadmap
- Planned enhancements with timelines
- Integration with other protocols
- Automation expansion plans

#### Priorities
- Ranked list of improvement initiatives
- Resource requirements
- Expected benefits

#### Resource Requirements
- Development effort estimates
- Tool or infrastructure needs
- Team capacity planning

#### Timeline
- Milestone dates for major enhancements
- Dependencies on other work
- Risk buffers and contingencies


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


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


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



### Continuous Improvement Validation:
- [ ] Execution feedback collected and logged
- [ ] Lessons learned documented in protocol artifacts
- [ ] Quality metrics captured for improvement tracking
- [ ] Knowledge base updated with new patterns or insights
- [ ] Protocol adaptation opportunities identified and logged
- [ ] Retrospective scheduled (if required for this protocol phase)


### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 14:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 14: Pre-Deployment Validation & Staging Readiness

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



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `uat-entry-checklist.json` | `.artifacts/uat/` | Confirms prerequisites met | Protocol 20 Gates |
| `execution-log.json` | `.artifacts/uat/` | Tracks UAT scenario outcomes | Protocol 21 |
| `uat-defect-register.csv` | `.artifacts/uat/` | Captures issues and resolutions | Protocol 21 & 10 |
| `UAT-CLOSURE-PACKAGE.zip` | `.artifacts/uat/` | Formal UAT deliverables | Protocol 15 |
| `feedback-notebook.md` | `.artifacts/uat/` | Qualitative insights | Protocol 22 & 14 |


### Traceability Matrix

**Upstream Dependencies:**
- Input artifacts inherit from: [list predecessor protocols]
- Configuration dependencies: [list config files or environment requirements]
- External dependencies: [list third-party systems or APIs]

**Downstream Consumers:**
- Output artifacts consumed by: [list successor protocols]
- Shared artifacts: [list artifacts used by multiple protocols]
- Archive requirements: [list retention policies]

**Verification Chain:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- Verification procedure: [describe validation process]
- Audit trail: All artifact modifications logged in protocol execution log

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |


---


## REASONING & COGNITIVE PROCESS

### Reasoning Patterns

**Primary Reasoning Pattern: Systematic Execution**
- Execute protocol steps sequentially with validation at each checkpoint

**Secondary Reasoning Pattern: Quality-Driven Validation**
- Apply quality gates to ensure artifact completeness before downstream handoff

**Pattern Improvement Strategy:**
- Track pattern effectiveness via quality gate pass rates and downstream protocol feedback
- Quarterly review identifies pattern weaknesses and optimization opportunities
- Iterate patterns based on empirical evidence from completed executions

### Decision Logic

#### Decision Point 1: Execution Readiness
**Context:** Determining if prerequisites are met to begin protocol execution

**Decision Criteria:**
- All prerequisite artifacts present
- Required approvals obtained
- System state validated

**Outcomes:**
- Proceed: Execute protocol workflow
- Halt: Document missing prerequisites, notify stakeholders

**Logging:** Record decision and prerequisites status in execution log

### Root Cause Analysis Framework

When protocol execution encounters blockers or quality gate failures:

1. **Identify Symptom:** What immediate issue prevented progress?
2. **Trace to Root Cause:**
   - Was prerequisite artifact missing or incomplete?
   - Did upstream protocol deliver inadequate inputs?
   - Were instructions ambiguous or insufficient?
   - Did environmental conditions fail?
3. **Document in Protocol Execution Log:**
   ```markdown
   **Blocker:** [Description]
   **Root Cause:** [Analysis]
   **Resolution:** [Action taken]
   **Prevention:** [Process/template update to prevent recurrence]
   ```
4. **Implement Fix:** Update protocol, re-engage stakeholders, adjust execution
5. **Validate Fix:** Re-run quality gates, confirm resolution

### Learning Mechanisms

#### Feedback Loops
**Purpose:** Establish continuous feedback collection to inform protocol improvements.

- **Execution feedback:** Collect outcome data after each protocol execution
- **Quality gate outcomes:** Track gate pass/fail patterns in historical logs
- **Downstream protocol feedback:** Capture issues reported by dependent protocols
- **Continuous monitoring:** Automated alerts for anomalies and degradation

#### Improvement Tracking
**Purpose:** Systematically track protocol effectiveness improvements over time.

- **Metrics tracking:** Monitor key performance indicators in quarterly dashboards
- **Template evolution:** Log all protocol template changes with rationale and impact
- **Effectiveness measurement:** Compare before/after metrics for each improvement
- **Continuous monitoring:** Automated alerts when metrics degrade

#### Knowledge Base Integration
**Purpose:** Build and leverage institutional knowledge to accelerate protocol quality.

- **Pattern library:** Maintain repository of successful execution patterns
- **Best practices:** Document proven approaches for common scenarios
- **Common blockers:** Catalog typical issues with proven resolutions
- **Industry templates:** Specialized variations for specific domains

#### Adaptation Mechanisms
**Purpose:** Enable protocol to automatically adjust based on context and patterns.

- **Context adaptation:** Adjust execution based on project type, complexity, constraints
- **Threshold tuning:** Modify quality gate thresholds based on risk tolerance
- **Workflow optimization:** Streamline steps based on historical efficiency data
- **Tool selection:** Choose optimal automation based on available resources

### Meta-Cognition

#### Self-Awareness and Process Awareness
**Purpose:** Enable AI to maintain explicit awareness of execution state and limitations.

**Awareness Statement Protocol:**
At each major execution checkpoint, generate awareness statement:
- Current phase and step status
- Artifacts completed vs. pending
- Identified blockers and their severity
- Confidence level in current outputs
- Known limitations and assumptions
- Required inputs for next steps

#### Process Monitoring and Progress Tracking
**Purpose:** Continuously track execution status and detect anomalies.

- **Progress tracking:** Update execution status after each step
- **Velocity monitoring:** Flag execution delays beyond expected duration
- **Quality monitoring:** Track gate pass rates and artifact completeness
- **Anomaly detection:** Alert on unexpected patterns or deviations

#### Self-Correction Protocols
**Purpose:** Enable autonomous detection and correction of execution issues.

- **Halt condition detection:** Recognize blockers and escalate appropriately
- **Quality gate failure handling:** Generate corrective action plans
- **Anomaly response:** Diagnose and propose fixes for unexpected conditions
- **Recovery procedures:** Maintain execution state for graceful resume

#### Continuous Improvement Integration
**Purpose:** Systematically capture lessons and evolve protocol effectiveness.

- **Retrospective execution:** Conduct after-action reviews post-completion
- **Template review cadence:** Scheduled protocol enhancement cycles
- **Gate calibration:** Periodic adjustment of pass criteria
- **Tool evaluation:** Assessment of automation effectiveness
