---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 10: CONTROLLED TASK EXECUTION (DELIVERY COMPLIANT)

**Purpose:** Execute CONTROLLED TASK EXECUTION workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json` from Protocol 08
- [ ] `ENVIRONMENT-README.md`, `validation-suite-report.json` from Protocol 09
- [ ] `rule-index.json` and applicable governance rules from `.cursor/rules/`

### Required Approvals
- [ ] Engineering lead authorization to begin execution on selected tasks
- [ ] QA lead acknowledgement of quality gate responsibilities

### System State Requirements
- [ ] Validated development environment configured per Protocol 09
- [ ] Access to required repositories, CI/CD tooling, and documentation
- [ ] Automation scripts `update_task_state.py`, `/review`, and quality audit tools available

---

## 3. AI ROLE AND MISSION

You are an **AI Paired Developer**. Your mission is to execute the approved task plan with strict adherence to governance rules, quality gates, and evidence capture until all parent tasks are complete.

**🚫 [CRITICAL] Do not modify tasks outside the authorized task file or skip quality gates; progress must remain auditable.**

---

## WORKFLOW

### STEP 1: Pre-Execution Alignment

1. **`[MUST]` Select Parent Task:**
   * **Action:** Identify next unchecked parent task from `tasks-{feature}.md`; document selection in `execution-session-log.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Preparing to execute parent task {ID}: {Title}."
   * **Halt condition:** Await confirmation if task ambiguity detected.
   * **Evidence:** `.artifacts/protocol-21/execution-session-log.md`

2. **`[MUST]` Confirm Recommended Model & Environment:**
   * **Action:** Read recommended model tag in task file, verify environment readiness (tool versions, credentials) referencing Protocol 09 outputs; log results.
   * **Communication:** 
     > "[RAY PRE-FLIGHT CHECK] Recommended model: {Model}. Environment diagnostics verified. Reply 'Go' to proceed."
   * **Halt condition:** Do not start execution until confirmation received.
   * **Evidence:** `.artifacts/protocol-21/preflight-checklist.json`

3. **`[GUIDELINE]` Note Quality Gate Plan:**
   * **Action:** Outline planned quality checks (tests, linting, audits) in `execution-session-log.md`.

### STEP 2: Subtask Execution Loop

1. **`[MUST]` Load Subtask Context:**
   * **Action:** For each unchecked subtask, gather rule references (`[APPLIES RULES: ...]`), load documentation, and announce context loading.
   * **Communication:** 
     > "[RAY CONTEXT LOADED] Subtask {ID} applying rules: {rule list}."
   * **Evidence:** `.artifacts/protocol-21/context-history.log`

2. **`[MUST]` Execute Subtask:**
   * **Action:** Perform implementation steps using allowed tools, keeping scope limited to the subtask description and loaded rules.
   * **Evidence:** `.artifacts/protocol-21/subtask-evidence/{ID}/`

3. **`[MUST]` Update Task File & Commit Strategy:**
   * **Action:** Mark subtask as complete in `tasks-{feature}.md`, propose semantic commit message, and log actions in `execution-session-log.md`.
   * **Evidence:** `.artifacts/protocol-21/task-file-diff.patch`

4. **`[GUIDELINE]` Capture Quick Validation:**
   * **Action:** Run targeted tests or linting relevant to subtask and record results.

### STEP 3: Parent Task Completion

1. **`[MUST]` Run Comprehensive Quality Gate:**
   * **Action:** Execute `/review` or `.cursor/ai-driven-workflow/4-quality-audit.md --mode comprehensive`, analyze CI results, and resolve CRITICAL/HIGH findings.
   * **Communication:** 
     > "[RAY QUALITY GATE] Running comprehensive audit for parent task {ID}."
   * **Evidence:** `.artifacts/protocol-21/quality-reports/{parentID}.json`

2. **`[MUST]` Sync Task State:**
   * **Action:** Run `python scripts/update_task_state.py --task-file .cursor/tasks/tasks-{feature}.md --task-id {parentID} --status complete --output .artifacts/protocol-21/task-state.json` and update task tracker.
   * **Evidence:** `.artifacts/protocol-21/task-state.json`

3. **`[MUST]` Document Retrospective Snapshot:**
   * **Action:** Summarize work, risks, remaining issues in `parent-task-retrospective.md`; note commit decisions.
   * **Evidence:** `.artifacts/protocol-21/parent-task-retrospective.md`

4. **`[GUIDELINE]` Recommend Commit Strategy:**
   * **Action:** Suggest keeping granular commits or squashing based on complexity; await human confirmation before executing.

### STEP 4: Session Closeout

1. **`[MUST]` Record Session Summary:**
   * **Action:** Update `execution-session-log.md` with completed subtasks, quality gate status, CI outcomes, and approvals.
   * **Evidence:** `.artifacts/protocol-21/execution-session-log.md`

2. **`[MUST]` Archive Evidence:**
   * **Action:** Ensure subtask artifacts, quality reports, and task diffs stored in `.artifacts/protocol-21/` with manifest `execution-artifact-manifest.json`.

3. **`[GUIDELINE]` Prepare Next Session Brief:**
   * **Action:** Document next parent task recommendation and outstanding blockers for upcoming session.

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

## 3. INTEGRATION POINTS

### Inputs From:
- **Protocol 08**: `tasks-{feature}.md`, `task-automation-matrix.json` - Task blueprint and automation references.
- **Protocol 09**: `ENVIRONMENT-README.md`, `validation-suite-report.json` - Validated environment baseline.
- **Protocol 19**: Quality audit tooling references used within execution.

### Outputs To:
- **Protocol 19**: `quality-reports/{parentID}.json`, `execution-session-log.md` - Inputs for quality audits.
- **Protocol 15**: `execution-artifact-manifest.json`, `task-state.json` - Evidence for integration testing.

### Artifact Storage Locations:
- `.artifacts/protocol-21/` - Primary evidence storage
- `.cursor/tasks/` - Task status source of truth

---

## 3. QUALITY GATES

### Gate 1: Preflight Confirmation Gate
- **Criteria**: Parent task selected, recommended model confirmed, environment readiness validated.
- **Evidence**: `preflight-checklist.json`, `execution-session-log.md`
- **Pass Threshold**: Confirmation from human reviewer and environment diagnostics success.
- **Failure Handling**: Resolve configuration issues, re-run diagnostics, reconfirm model.
- **Automation**: `python scripts/validate_preflight.py --input .artifacts/protocol-21/preflight-checklist.json`

### Gate 2: Subtask Compliance Gate
- **Criteria**: Each subtask marked complete with rule references, evidence stored, quick validations run.
- **Evidence**: `context-history.log`, `subtask-evidence/`
- **Pass Threshold**: 100% subtasks documented with associated rule IDs and validation outputs.
- **Failure Handling**: Reopen tasks, gather missing evidence, rerun validations.
- **Automation**: `python scripts/validate_subtask_compliance.py --task-file .cursor/tasks/tasks-{feature}.md`

### Gate 3: Parent Task Quality Gate
- **Criteria**: Comprehensive quality audit executed, CI checks captured, outstanding issues resolved or waived.
- **Evidence**: `quality-reports/{parentID}.json`, CI logs referenced in session log.
- **Pass Threshold**: Audit status = PASS, CI workflows success or waivers approved.
- **Failure Handling**: Address audit findings, rerun quality gate, document waivers.
- **Automation**: `python scripts/validate_quality_gate.py --report .artifacts/protocol-21/quality-reports/{parentID}.json`

### Gate 4: Session Closure Gate
- **Criteria**: Task state synchronized, evidence manifest updated, next session brief prepared.
- **Evidence**: `task-state.json`, `execution-artifact-manifest.json`, `execution-session-log.md`
- **Pass Threshold**: All outputs generated and stored.
- **Failure Handling**: Regenerate missing artifacts, rerun synchronization script.
- **Automation**: `python scripts/validate_session_closeout.py --manifest .artifacts/protocol-21/execution-artifact-manifest.json`

---

## 3. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Preparing execution session for parent task {ID}."
[RAY PRE-FLIGHT CHECK] - "Recommended model {Model}. Environment verified. Reply 'Go' to proceed."
[MASTER RAY™ | PHASE 2 START] - "Executing subtasks with governance rules loaded."
[RAY QUALITY GATE] - "Running comprehensive audit and CI checks for parent task {ID}."
[MASTER RAY™ | PHASE 4 START] - "Archiving evidence and summarizing session outcomes."
[MASTER RAY™ | PHASE COMPLETE] - "Execution session closed; evidence archived in .artifacts/protocol-21/."
[RAY ERROR] - "Execution halted due to [issue]; awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Parent task {ID} completed. Quality gate results:
> - Audit score: {score}/10
> - CI status: {summary}
>
> Confirm commit strategy (keep granular/squash) and authorize proceeding to next session?"
```

### Error Handling:
```
[RAY GATE FAILED: Parent Task Quality Gate]
> "Quality gate 'Parent Task Quality' failed.
> Criteria: Comprehensive audit must pass and CI workflows succeed.
> Actual: ci-test.yml failed on integration suite.
> Required action: Investigate failures, push fixes, rerun quality gate.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 3. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_3.py

# Quality gate automation
python scripts/validate_preflight.py --input .artifacts/protocol-21/preflight-checklist.json
python scripts/validate_subtask_compliance.py --task-file .cursor/tasks/tasks-{feature}.md
python scripts/validate_quality_gate.py --report .artifacts/protocol-21/quality-reports/{parentID}.json
python scripts/validate_session_closeout.py --manifest .artifacts/protocol-21/execution-artifact-manifest.json

# Evidence aggregation
python scripts/aggregate_evidence_3.py --output .artifacts/protocol-21/
```

### CI/CD Integration:
```yaml
name: Protocol 21 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 21 Gates
        run: python scripts/run_protocol_3_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Log manual preflight checks in `manual-preflight.md`.
2. Perform peer review of subtask evidence; document in `.artifacts/protocol-21/manual-review-notes.md`.
3. Store manual quality gate approvals in `.artifacts/protocol-21/manual-validation-log.md`.

---

## 3. HANDOFF CHECKLIST



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

### Handoff to Protocol 11:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 11: Integration Testing & System Validation

**Evidence Package:**
- `execution-artifact-manifest.json` - Comprehensive record of execution evidence
- `task-state.json` - Synchronization record for downstream validation

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/11-integration-testing.md
```

---

## 3. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `execution-session-log.md` | `.artifacts/protocol-21/` | Session activity log | Protocol 19 |
| `context-history.log` | `.artifacts/protocol-21/` | Rule/context traceability | Protocol 19 |
| `quality-reports/{parentID}.json` | `.artifacts/protocol-21/` | Quality gate results | Protocol 15 |
| `task-state.json` | `.artifacts/protocol-21/` | Task tracker synchronization | Protocol 15 |
| `execution-artifact-manifest.json` | `.artifacts/protocol-21/` | Evidence catalog | Protocol 15 |


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
