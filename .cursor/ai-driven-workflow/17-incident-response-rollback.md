---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 17: INCIDENT RESPONSE & ROLLBACK (OPERATIONS RESILIENCE COMPLIANT)

**Purpose:** Execute INCIDENT RESPONSE & ROLLBACK workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `MONITORING-PACKAGE.zip` from Protocol 16 – monitoring configuration and validation evidence
- [ ] `alert-test-results.json` from Protocol 16 – alert routing baseline
- [ ] `production-deployment-report.json` from Protocol 15 – deployment context
- [ ] `rollback-verification-report.json` from Protocol 14 – rollback rehearsal evidence
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

## WORKFLOW

### STEP 1: Detection and Severity Assessment

1. **`[MUST]` Monitor Active Alerts:**
   * **Action:** Continuously ingest alerts and dashboards from Protocol 19 outputs to detect incidents.
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
   * **Action:** Summarize severity, timeline, actions, and next steps in `INCIDENT-REPORT.md` for Protocol 22.
   * **Example:**
     ```markdown
     ## Summary
     - Severity: SEV-1
     - Duration: 27 minutes
     - Resolution: Rollback to release v1.2.3
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

## 13. INTEGRATION POINTS

### Inputs From:
- **Protocol 19**: `MONITORING-PACKAGE.zip`, `alert-test-results.json`, `monitoring-approval-record.json`
- **Protocol 15**: `production-deployment-report.json`, `post-deployment-validation.json`
- **Protocol 21**: `rollback-verification-report.json`

### Outputs To:
- **Protocol 22**: `INCIDENT-REPORT.md`, `rca-manifest.json`, `recovery-validation.json`
- **Protocol 21**: `incident-intake-log.md`, performance degradation notes for tuning
- **Protocol 19**: `alert-tuning-feedback.json` (if alert improvements identified)

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


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


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
name: Protocol 20 Validation
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
      - name: Run Protocol 20 Gates
        run: python scripts/run_protocol_13_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review alert logs and severity decisions during war-room session.
2. Capture mitigation steps manually in timeline and execution report.
3. Document results in `.artifacts/protocol-20/manual-validation-log.md`

---

## 13. HANDOFF CHECKLIST



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

### Handoff to Protocol 18:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 18: Performance Optimization & Tuning

**Evidence Package:**
- `INCIDENT-REPORT.md` - Incident summary for retrospective
- `recovery-validation.json` - Verification of restored service health

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/18-performance-optimization.md
```

---

## 13. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `incident-intake-log.md` | `.artifacts/incidents/` | Captures alert signals and timestamps | Protocol 20 Gates |
| `mitigation-plan.md` | `.artifacts/incidents/` | Documents containment strategy | Protocol 20 Gates |
| `recovery-validation.json` | `.artifacts/incidents/` | Confirms system stabilization | Protocol 22 |
| `INCIDENT-REPORT.md` | `.artifacts/incidents/` | Incident summary and actions | Protocol 22 |
| `rca-manifest.json` | `.artifacts/incidents/` | Root cause evidence index | Protocol 22 |


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
| Gate 3 Pass Rate | ≥ 95% | [TBD] | ⏳ |
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
