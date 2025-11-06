---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 10: CONTROLLED TASK EXECUTION (DELIVERY COMPLIANT)

**Purpose:** Execute CONTROLLED TASK EXECUTION workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json` from Protocol 08
- **`[MUST]`** `ENVIRONMENT-README.md`, `validation-suite-report.json` from Protocol 09
- **`[MUST]`** `rule-index.json` and applicable governance rules from `.cursor/rules/`

### 1.2 Required Approvals
- **`[MUST]`** Engineering lead authorization to begin execution on selected tasks
- **`[MUST]`** QA lead acknowledgement of quality gate responsibilities

### 1.3 System State Requirements
- **`[MUST]`** Validated development environment configured per Protocol 09
- **`[MUST]`** Access to required repositories, CI/CD tooling, and documentation
- **`[MUST]`** Automation scripts `update_task_state.py`, `/review`, and quality audit tools available

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

**`[STRICT]` Role Definition:**
You are an **AI Paired Developer**. Your mission is to execute the approved task plan with strict adherence to governance rules, quality gates, and evidence capture until all parent tasks are complete.

**🚫 [CRITICAL] Directive:**
Do not modify tasks outside the authorized task file or skip quality gates; progress must remain auditable.

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Pre-Execution Alignment
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical task selection and confirmation gate requiring human approval -->

1. **`[MUST]` Select Parent Task:**
   * **Action:** Identify next unchecked parent task from `tasks-{feature}.md`; document selection in `execution-session-log.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Preparing to execute parent task {ID}: {Title}."
   
   **[REASONING]:**
   - **Premises:** Tasks must be executed in priority order with clear scope boundaries
   - **Constraints:** Resource availability, dependency completion, governance compliance
   - **Alternatives Considered:**
     * **A)** Random task selection - Rejected: Breaks dependency chains
     * **B)** Sequential execution - Selected: Ensures proper order and traceability
     * **C)** Parallel execution - Considered: For independent tasks only
   - **Decision:** Sequential parent task execution with subtask parallelization where safe
   - **Evidence:** Task dependencies from Protocol 08, priority rankings
   - **Risks & Mitigations:**
     * **Risk:** Blocking dependencies → **Mitigation:** Verify prerequisites before starting
     * **Risk:** Scope creep → **Mitigation:** Strict task boundary enforcement
   - **Acceptance Link:** Task file approval from Protocol 08
   
   * **Halt condition:** Await confirmation if task ambiguity detected.
   * **Evidence:** `.artifacts/protocol-10/execution-session-log.md`
   * **Validation:** Task clearly identified and logged

2. **`[MUST]` Confirm Recommended Model & Environment:**
   * **Action:** Read recommended model tag in task file, verify environment readiness (tool versions, credentials) referencing Protocol 09 outputs; log results.
   * **Communication:** 
     > "[RAY PRE-FLIGHT CHECK] Recommended model: {Model}. Environment diagnostics verified. Reply 'Go' to proceed."
   
   **[REASONING]:**
   - **Premises:** Model capabilities must match task requirements
   - **Constraints:** Environment must be stable and validated
   - **Decision:** Require explicit "Go" confirmation before execution
   - **Evidence:** Environment validation from Protocol 09
   - **Acceptance Link:** Human confirmation required
   
   * **Halt condition:** Do not start execution until confirmation received.
   * **Evidence:** `.artifacts/protocol-10/preflight-checklist.json`
   * **Validation:** Explicit "Go" confirmation documented

3. **`[GUIDELINE]` Note Quality Gate Plan:**
   * **Action:** Outline planned quality checks (tests, linting, audits) in `execution-session-log.md`.
   * **Evidence:** Updated `.artifacts/protocol-10/execution-session-log.md`
   * **Validation:** Quality plan documented

### STEP 2: Subtask Execution Loop
<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Iterative execution loop with multiple precise substeps per subtask -->

1. **`[MUST]` Load Subtask Context:**
   * **1.1. Gather Rule References:**
       * **Action:** Extract rule IDs from `[APPLIES RULES: ...]` annotations
       * **Evidence:** Rule loading logged in context history
       * **Validation:** All referenced rules loaded
   
   * **1.2. Load Documentation:**
       * **Action:** Retrieve relevant documentation and examples
       * **Evidence:** Documentation paths logged
       * **Validation:** Required docs accessible
   
   * **1.3. Announce Context Loading:**
       * **Communication:** 
         > "[RAY CONTEXT LOADED] Subtask {ID} applying rules: {rule list}."
       * **Evidence:** `.artifacts/protocol-10/context-history.log`
       * **Validation:** Context announcement made

2. **`[MUST]` Execute Subtask:**
   * **2.1. Implementation Steps:**
       * **Action:** Perform code changes using allowed tools
       * **Evidence:** Code changes tracked in version control
       * **Validation:** Changes scoped to subtask
   
   * **2.2. Rule Compliance:**
       * **Action:** Ensure all rule requirements met
       * **Evidence:** Compliance checklist completed
       * **Validation:** No rule violations detected
   
   * **2.3. Evidence Capture:**
       * **Action:** Store implementation evidence
       * **Evidence:** `.artifacts/protocol-10/subtask-evidence/{ID}/`
       * **Validation:** Evidence complete and organized

3. **`[MUST]` Update Task File & Commit Strategy:**
   * **3.1. Mark Subtask Complete:**
       * **Action:** Check off subtask in `tasks-{feature}.md`
       * **Evidence:** Task file updated
       * **Validation:** Checkbox marked
   
   * **3.2. Propose Commit Message:**
       * **Action:** Generate semantic commit message
       * **Evidence:** Commit message logged
       * **Validation:** Follows conventional commits
   
   * **3.3. Log Actions:**
       * **Action:** Document all actions taken
       * **Evidence:** `.artifacts/protocol-10/task-file-diff.patch`
       * **Validation:** Actions traceable

4. **`[GUIDELINE]` Capture Quick Validation:**
   * **4.1. Run Targeted Tests:**
       * **Action:** Execute tests relevant to changes
       * **Evidence:** Test results captured
       * **Validation:** Tests pass or issues documented
   
   * **4.2. Linting Check:**
       * **Action:** Run linters on modified files
       * **Evidence:** Linting report generated
       * **Validation:** No critical lint errors

### STEP 3: Parent Task Completion
<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Multiple critical completion steps including quality gates and retrospectives -->

1. **`[MUST]` Run Comprehensive Quality Gate:**
   * **1.1. Execute Quality Audit:**
       * **Action:** Run `/review` or `.cursor/ai-driven-workflow/4-quality-audit.md --mode comprehensive`
       * **Communication:** 
         > "[RAY QUALITY GATE] Running comprehensive audit for parent task {ID}."
       * **Evidence:** Quality audit report generated
       * **Validation:** Audit completed successfully
   
   * **1.2. Analyze CI Results:**
       * **Action:** Review CI/CD pipeline outcomes
       * **Evidence:** CI logs analyzed and documented
       * **Validation:** CI checks pass or issues identified
   
   * **1.3. Resolve Critical Findings:**
       * **Action:** Address all CRITICAL and HIGH severity issues
       * **Evidence:** `.artifacts/protocol-10/quality-reports/{parentID}.json`
       * **Validation:** No unresolved critical issues

2. **`[MUST]` Sync Task State:**
   * **2.1. Run State Update Script:**
       * **Action:** Execute `python scripts/update_task_state.py --task-file .cursor/tasks/tasks-{feature}.md --task-id {parentID} --status complete --output .artifacts/protocol-10/task-state.json`
       * **Evidence:** Script execution log
       * **Validation:** State updated successfully
   
   * **2.2. Update Task Tracker:**
       * **Action:** Synchronize with external task tracking system
       * **Evidence:** `.artifacts/protocol-10/task-state.json`
       * **Validation:** Tracker reflects completion

3. **`[MUST]` Document Retrospective Snapshot:**
   * **3.1. Summarize Work:**
       * **Action:** Document work completed and outcomes
       * **Evidence:** Summary section in retrospective
       * **Validation:** All subtasks covered
   
   * **3.2. Note Risks & Issues:**
       * **Action:** Document remaining risks and open issues
       * **Evidence:** Risk section in retrospective
       * **Validation:** Known issues captured
   
   * **3.3. Record Commit Decisions:**
       * **Action:** Document commit strategy choices
       * **Evidence:** `.artifacts/protocol-10/parent-task-retrospective.md`
       * **Validation:** Decisions justified

4. **`[GUIDELINE]` Recommend Commit Strategy:**
   * **4.1. Evaluate Complexity:**
       * **Action:** Assess whether to keep granular commits or squash
       * **Evidence:** Complexity analysis documented
       * **Validation:** Recommendation provided
   
   * **4.2. Await Confirmation:**
       * **Action:** Get human approval before executing
       * **Evidence:** Confirmation logged
       * **Validation:** Human decision recorded

### STEP 4: Session Closeout
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple archival and documentation steps -->

1. **`[MUST]` Record Session Summary:**
   * **Action:** Update `execution-session-log.md` with completed subtasks, quality gate status, CI outcomes, and approvals.
   * **Evidence:** `.artifacts/protocol-10/execution-session-log.md`
   * **Validation:** Summary comprehensive and accurate

2. **`[MUST]` Archive Evidence:**
   * **Action:** Ensure subtask artifacts, quality reports, and task diffs stored in `.artifacts/protocol-10/` with manifest `execution-artifact-manifest.json`.
   * **Evidence:** `.artifacts/protocol-10/execution-artifact-manifest.json`
   * **Validation:** All artifacts archived and indexed

3. **`[GUIDELINE]` Prepare Next Session Brief:**
   * **Action:** Document next parent task recommendation and outstanding blockers for upcoming session.
   * **Evidence:** Next session section in session log
   * **Validation:** Clear handoff for next session
---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

### 4.1 Retrospective Guidance

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

### 4.2 Continuous Improvement Opportunities

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

### 4.3 System Evolution

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

### 4.4 Knowledge Capture and Organizational Learning

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

### 4.5 Future Planning

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

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### 5.1 Inputs From:
- **Protocol 08:** `tasks-{feature}.md`, `task-automation-matrix.json` - Task blueprint and automation references.
- **Protocol 09:** `ENVIRONMENT-README.md`, `validation-suite-report.json` - Validated environment baseline.
- **Protocol 19:** Quality audit tooling references used within execution.

### 5.2 Outputs To:
- **Protocol 19:** `quality-reports/{parentID}.json`, `execution-session-log.md` - Inputs for quality audits.
- **Protocol 15:** `execution-artifact-manifest.json`, `task-state.json` - Evidence for integration testing.

### 5.3 Artifact Storage Locations:
- **Primary Evidence:** `.artifacts/protocol-10/` - Primary evidence storage
- **Task Repository:** `.cursor/tasks/` - Task status source of truth

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Preflight Confirmation Gate
**Type:** Prerequisite  
**Purpose:** Verify parent task selection, environment readiness, and model alignment before execution kicks off.

**Pass Criteria:**
- **Threshold:** Preflight readiness metric ≥0.95 and environment verification score ≥0.9.  
- **Threshold:** Reviewer acknowledgment latency ≤12 hours across all preflight checkpoints.  
- **Boolean Check:** `preflight_check` flag equals `approved` and recommended model matches session scope.  
- **Boolean Check:** Session log verification flag reports `pass` with zero unresolved checklist items.  
- **Metrics:** Readiness metrics, environment diagnostics metrics, and reviewer confirmation metrics stored in preflight report.  
- **Evidence Link:** `.artifacts/protocol-10/preflight-checklist.json`, `.artifacts/protocol-10/execution-session-log.md`.

**Automation:**
- Script: `python3 scripts/validate_preflight.py --input .artifacts/protocol-10/preflight-checklist.json`
- Script: `python3 scripts/generate_preflight_report.py --session .artifacts/protocol-10/execution-session-log.md`
- Script: `python3 scripts/log_preflight_metrics.py --input .artifacts/protocol-10/preflight-checklist.json`
- CI/CD Integration: Workflow `protocol-10-preflight.yml` runs on pull requests to confirm readiness metrics and publish audit logs.

**Failure Handling:**
- **Rollback:** Re-run environment diagnostics, adjust model selection, and regenerate the checklist before resuming.  
- **Notification:** Notify protocol owner and environment steward via Slack when boolean checks fail.  
- **Waiver:** Waivers allowed only for model mismatch with architect sign-off; justification logged in `.artifacts/protocol-10/gate-waivers.json`.

### Gate 2: Subtask Compliance Gate
**Type:** Execution  
**Purpose:** Ensure every subtask includes rule references, evidence artifacts, and quick validation outputs.

**Pass Criteria:**
- **Threshold:** Automation coverage ≥80% of high-level tasks and rule linkage completeness ≥100%.  
- **Threshold:** Evidence capture completeness ≥95% across subtask outputs.  
- **Boolean Check:** Each subtask entry sets `compliance_status = pass` and evidence pointer recorded.  
- **Boolean Check:** Persona distribution check flag equals `pass` with zero unassigned personas.  
- **Metrics:** Rule linkage metrics, automation metrics, and persona coverage metrics documented in compliance report.  
- **Evidence Link:** `.artifacts/protocol-10/context-history.log`, `.artifacts/protocol-10/subtask-evidence/`.

**Automation:**
- Script: `python3 scripts/validate_subtask_compliance.py --task-file .cursor/tasks/tasks-{feature}.md`
- Script: `python3 scripts/audit_subtask_evidence.py --output .artifacts/protocol-10/subtask-audit-report.json`
- Script: `python3 scripts/summarize_subtask_personas.py --input .artifacts/protocol-10/subtask-evidence/`
- CI/CD Integration: Config `config/protocol_gates/10.yaml` powers workflow `protocol-10-compliance.yml` to enforce linkage thresholds on merge.

**Failure Handling:**
- **Rollback:** Reopen incomplete subtasks, capture missing evidence, and rerun automation scripts.  
- **Notification:** Alert automation lead when rule linkage metric drops below threshold.  
- **Waiver:** Waivers not permitted; compliance gate is mandatory.

### Gate 3: Parent Task Quality Gate
**Type:** Execution  
**Purpose:** Validate comprehensive audits, CI telemetry, and defect remediation before session closure.

**Pass Criteria:**
- **Threshold:** Quality audit score ≥0.93 and CI stability metric ≥0.9.  
- **Threshold:** Defect remediation rate ≥0.85 before session closure.  
- **Boolean Check:** Audit status recorded as `pass`.  
- **Boolean Check:** CI workflow result equals `success` or approved waiver with mitigation plan recorded.  
- **Metrics:** Audit metrics, defect density metrics, and CI telemetry metrics preserved in quality report.  
- **Evidence Link:** `.artifacts/protocol-10/quality-reports/{parentID}.json`, `.artifacts/protocol-10/ci-summary.json`.

**Automation:**
- Script: `python3 scripts/validate_quality_gate.py --report .artifacts/protocol-10/quality-reports/{parentID}.json`
- Script: `python3 scripts/collect_ci_telemetry.py --output .artifacts/protocol-10/ci-summary.json`
- Script: `python3 scripts/validate_ci_results.py --input .artifacts/protocol-10/ci-summary.json`
- CI/CD Integration: Nightly job `protocol-10-quality.yml` posts metrics to governance dashboard with automated alerts.

**Failure Handling:**
- **Rollback:** Address audit findings, rerun CI suites, and refresh quality report before advancing.  
- **Notification:** Notify quality orchestrator and project manager when CI telemetry boolean check fails.  
- **Waiver:** Waiver requires governance board approval with mitigation plan recorded in `gate-waivers.json`.

### Gate 4: Session Closure Gate
**Type:** Completion  
**Purpose:** Confirm task synchronization, manifest accuracy, and next-session brief readiness for downstream protocols.

**Pass Criteria:**
- **Threshold:** Handoff readiness metric ≥0.96 and manifest completeness metric =100%.  
- **Threshold:** Evidence bundle checksum confidence ≥0.98 before release.  
- **Boolean Check:** `task_state.synced = true`.  
- **Boolean Check:** Next session brief timestamp recorded and manifest verification flag equals `pass`.  
- **Metrics:** Synchronization metrics, artifact completeness metrics, and readiness metrics captured in manifest.  
- **Evidence Link:** `.artifacts/protocol-10/task-state.json`, `.artifacts/protocol-10/execution-artifact-manifest.json`, `.artifacts/protocol-10/next-session-brief.md`.

**Automation:**
- Script: `python3 scripts/validate_session_closeout.py --manifest .artifacts/protocol-10/execution-artifact-manifest.json`
- Script: `python3 scripts/generate_next_session_brief.py --output .artifacts/protocol-10/next-session-brief.md`
- Script: `python3 scripts/aggregate_evidence_3.py --output .artifacts/protocol-10/`
- Script: `python3 scripts/publish_execution_summary.py --output .artifacts/protocol-10/execution-summary.json`
- CI/CD Integration: Closure workflow posts manifest checksum to governance Slack channel with summary attachment.

**Failure Handling:**
- **Rollback:** Re-sync task state, regenerate manifest, and rerun automation until completeness achieved.  
- **Notification:** Notify Protocol 11 owner when boolean check fails to prevent premature handoff.  
- **Waiver:** No waiver permitted; session closure gate mandatory.

### Compliance Integration
- **Industry Standards:** Evidence artifacts comply with CommonMark Markdown, JSON Schema, and automated trace logging norms.  
- **Security Requirements:** Execution logs inherit SOC 2 logging controls, subtask evidence enforces GDPR redaction, and manifests respect least-privilege access.  
- **Regulatory Compliance:** Quality audits reference FTC transparency guidance and sector-specific assurance mandates.  
- **Governance:** Thresholds and metrics defined in `config/protocol_gates/10.yaml`, synchronized with protocol governance registry and CI dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### 7.1 Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Preparing execution session for parent task {ID}."
[RAY PRE-FLIGHT CHECK] - "Recommended model {Model}. Environment verified. Reply 'Go' to proceed."
[MASTER RAY™ | PHASE 2 START] - "Executing subtasks with governance rules loaded."
[RAY QUALITY GATE] - "Running comprehensive audit and CI checks for parent task {ID}."
[MASTER RAY™ | PHASE 4 START] - "Archiving evidence and summarizing session outcomes."
[MASTER RAY™ | PHASE COMPLETE] - "Execution session closed; evidence archived in .artifacts/protocol-10/."
[RAY ERROR] - "Execution halted due to [issue]; awaiting instructions."
```

### 7.2 Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Parent task {ID} completed. Quality gate results:
> - Audit score: {score}/10
> - CI status: {summary}
>
> Confirm commit strategy (keep granular/squash) and authorize proceeding to next session?"
```

### 7.3 Error Handling:
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

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### 8.1 Validation Scripts:

1. **`[MUST]` Prerequisite Validation:**
   * **Action:** Run prerequisite check script
   * **Command:** `python scripts/validate_prerequisites_3.py`
   * **Evidence:** Script execution log
   * **Validation:** All prerequisites met

2. **`[MUST]` Quality Gate Automation:**
   * **Action:** Execute quality gate validation scripts
   * **Commands:**
     - `python scripts/validate_preflight.py --input .artifacts/protocol-10/preflight-checklist.json`
     - `python scripts/validate_subtask_compliance.py --task-file .cursor/tasks/tasks-{feature}.md`
     - `python scripts/validate_quality_gate.py --report .artifacts/protocol-10/quality-reports/{parentID}.json`
     - `python scripts/validate_session_closeout.py --manifest .artifacts/protocol-10/execution-artifact-manifest.json`
   * **Evidence:** Validation reports
   * **Validation:** All gates pass or have waivers

3. **`[MUST]` Evidence Aggregation:**
   * **Action:** Aggregate all protocol evidence
   * **Command:** `python scripts/aggregate_evidence_3.py --output .artifacts/protocol-10/`
   * **Evidence:** Aggregated evidence report
   * **Validation:** All evidence artifacts present

### 8.2 CI/CD Integration:
```yaml
name: Protocol 10 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 10 Gates
        run: python scripts/run_protocol_3_gates.py
```

### 8.3 Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Log manual preflight checks in `manual-preflight.md`.
2. Perform peer review of subtask evidence; document in `.artifacts/protocol-10/manual-review-notes.md`.
3. Store manual quality gate approvals in `.artifacts/protocol-10/manual-validation-log.md`.

---

## 9. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### 9.1 Continuous Improvement Validation:

1. **`[MUST]` Execution Feedback:**
   * **Action:** Collect and log execution feedback
   * **Evidence:** Feedback logged in protocol artifacts
   * **Validation:** Feedback captured for all phases

2. **`[MUST]` Lessons Learned:**
   * **Action:** Document lessons learned in protocol artifacts
   * **Evidence:** Lessons documented in knowledge base
   * **Validation:** At least one lesson per execution

3. **`[MUST]` Quality Metrics:**
   * **Action:** Capture quality metrics for improvement tracking
   * **Evidence:** Metrics recorded in dashboard
   * **Validation:** All required metrics captured

4. **`[GUIDELINE]` Knowledge Base Update:**
   * **Action:** Update knowledge base with new patterns or insights
   * **Evidence:** Knowledge base entries created/updated
   * **Validation:** Relevant patterns documented

5. **`[GUIDELINE]` Protocol Adaptation:**
   * **Action:** Identify and log protocol adaptation opportunities
   * **Evidence:** Adaptation opportunities logged
   * **Validation:** Opportunities reviewed quarterly

6. **`[GUIDELINE]` Retrospective Scheduling:**
   * **Action:** Schedule retrospective if required for this protocol phase
   * **Evidence:** Calendar invitation sent
   * **Validation:** Stakeholders confirmed attendance

### 9.2 Pre-Handoff Validation:

Before declaring protocol complete, validate:

1. **`[MUST]` Prerequisites Met:**
   * **Action:** Verify all prerequisites were satisfied
   * **Evidence:** Prerequisite checklist complete
   * **Validation:** 100% prerequisites met

2. **`[MUST]` Workflow Completion:**
   * **Action:** Confirm all workflow steps executed successfully
   * **Evidence:** Workflow execution log
   * **Validation:** All steps marked complete

3. **`[MUST]` Quality Gates Passed:**
   * **Action:** Verify all quality gates passed or have waivers
   * **Evidence:** Gate validation reports
   * **Validation:** 100% gates resolved

4. **`[MUST]` Evidence Captured:**
   * **Action:** Confirm all evidence artifacts captured and stored
   * **Evidence:** Evidence inventory complete
   * **Validation:** All required artifacts present

5. **`[MUST]` Integration Outputs:**
   * **Action:** Verify all integration outputs generated
   * **Evidence:** Output manifest
   * **Validation:** All outputs available

6. **`[MUST]` Automation Execution:**
   * **Action:** Confirm all automation hooks executed successfully
   * **Evidence:** Automation execution logs
   * **Validation:** All scripts ran successfully

7. **`[MUST]` Communication Complete:**
   * **Action:** Verify communication log is complete
   * **Evidence:** Communication log
   * **Validation:** All phases communicated

### 9.3 Handoff to Protocol 11:

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

## 10. EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for evidence collection and quality metrics -->

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| preflight artifact (`preflight-checklist.json`) | Readiness metric ≥0.95, reviewer confirmation metric captured | `.artifacts/protocol-10/preflight-checklist.json` | Gate 1 evidence bundle |
| session-log artifact (`execution-session-log.md`) | Environment verification metric ≥0.9, decision metric logged | `.artifacts/protocol-10/execution-session-log.md` | Gate 1 evidence log |
| compliance-history artifact (`context-history.log`) | Rule linkage metric =100%, automation metric ≥85% | `.artifacts/protocol-10/context-history.log` | Gate 2 evidence reference |
| subtask-evidence artifact (`subtask-evidence/`) | Evidence completeness metric 100%, validation metric recorded | `.artifacts/protocol-10/subtask-evidence/` | Gate 2 evidence archive |
| quality-report artifact (`quality-reports/{parentID}.json`) | Audit score metric ≥0.93, defect density metric documented | `.artifacts/protocol-10/quality-reports/{parentID}.json` | Gate 3 evidence report |
| ci-summary artifact (`ci-summary.json`) | CI stability metric ≥0.9, workflow status metric captured | `.artifacts/protocol-10/ci-summary.json` | Gate 3 evidence telemetry |
| task-state artifact (`task-state.json`) | Synchronization metric =100%, state consistency metric logged | `.artifacts/protocol-10/task-state.json` | Gate 4 evidence record |
| manifest artifact (`execution-artifact-manifest.json`) | Manifest completeness metric 100%, checksum metric verified | `.artifacts/protocol-10/execution-artifact-manifest.json` | Gate 4 evidence manifest |
| next-session artifact (`next-session-brief.md`) | Handoff readiness metric ≥0.96, briefing metric documented | `.artifacts/protocol-10/next-session-brief.md` | Gate 4 evidence brief |
| retrospective artifact (`execution-retrospective.json`) | Continuous improvement metric logged, action metric captured | `.artifacts/protocol-10/execution-retrospective.json` | Continuous improvement evidence |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-10/`  
- **Subdirectories:** `subtasks/` for decomposed evidence, `quality/` for audits, `closure/` for manifests and briefs.  
- **Permissions:** Read/write for protocol executor, read-only for downstream protocols and governance auditors.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `quality-reports/{parentID}.json`, `execution-retrospective.json`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-10/execution-artifact-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash logged for every artifact in the table.  
- Size: File size in bytes recorded for audit.  
- Dependencies: Upstream dependencies (Protocol 08 tasks, Protocol 09 environment package) and downstream consumers (Protocol 11 integration testing).

**Dependency Tracking:**
- Input: Protocol 08 `tasks-{feature}.md`, Protocol 09 `ENVIRONMENT-README.md`, governance rule inventory.  
- Output: All artifacts listed above plus manifest and retrospective.  
- Transformations: Preflight alignment → Subtask execution → Quality audits → Session closure and retrospectives.

**Coverage:** 100% of required artifacts documented with checksum and dependency references.

### Traceability

**Input Sources:**
- **Input From:** Protocol 08 `task-automation-matrix.json` – Automation references for execution.  
- **Input From:** Protocol 09 `validation-suite-report.json` – Environment validation baseline.  
- **Input From:** Stakeholder guidance logs – Acceptance criteria and risk notes.

**Output Artifacts:**
- **Output To:** `quality-reports/{parentID}.json` – Consumed by Protocol 11 audit workflows.  
- **Output To:** `execution-artifact-manifest.json` – Referenced by downstream protocol evidence validators.  
- **Output To:** `next-session-brief.md` – Kick-off input for subsequent execution sessions.  
- **Output To:** `execution-retrospective.json` – Continuous improvement input for governance reviews.

**Transformation Steps:**
1. Preflight verification → Checklist completion → Session log updates.  
2. Task execution → Evidence capture → Compliance reports.  
3. Quality audits → CI telemetry aggregation → Quality report updates.  
4. Session closure → Manifest generation → Next session briefing and retrospective capture.

**Audit Trail:**
- Manifest logs timestamps, checksums, and verified_by fields for every artifact.  
- Automation scripts emit execution logs stored in `.artifacts/protocol-10/quality/`.  
- Session log cross-references decision prompts and approvals for compliance audits.  
- Retrospective artifact catalogs improvement actions linked to specific gate outcomes.

### Archival Strategy

**Compression:**
- Compress artifacts into `.artifacts/protocol-10/evidence-bundle.zip` post-session using ZIP standard compression.

**Retention Policy:**
- Active artifacts retained for 150 days after session closure.  
- Archived bundles retained for 3 years after project completion.  
- Cleanup automation `scripts/cleanup_artifacts.py` enforces retention quarterly.

**Retrieval Procedures:**
- Active artifacts accessed directly from `.artifacts/protocol-10/` via read-only mounts.  
- Archived bundles retrieved with `unzip .artifacts/protocol-10/evidence-bundle.zip` and verified against manifest checksums.  
- Recovery instructions documented in `closure/recovery-playbook.md`.

**Cleanup Process:**
- Quarterly cleanup logs stored in `.artifacts/protocol-10/cleanup-log.json`.  
- Critical artifacts flagged for extended retention require governance board approval.  
- Manual overrides captured with timestamp, reviewer, and justification entries.

---

## 11. REASONING & COGNITIVE PROCESS
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level protocol analysis and reasoning patterns documentation -->

### 11.1 Reasoning Patterns

**Primary Reasoning Pattern: Systematic Execution**
- Execute protocol steps sequentially with validation at each checkpoint

**Secondary Reasoning Pattern: Quality-Driven Validation**
- Apply quality gates to ensure artifact completeness before downstream handoff

**Pattern Improvement Strategy:**
- Track pattern effectiveness via quality gate pass rates and downstream protocol feedback
- Quarterly review identifies pattern weaknesses and optimization opportunities
- Iterate patterns based on empirical evidence from completed executions

### 11.2 Decision Logic

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

### 11.3 Root Cause Analysis Framework

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

### 11.4 Learning Mechanisms

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

### 11.5 Meta-Cognition

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

---
