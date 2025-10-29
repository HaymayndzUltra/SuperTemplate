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
   * **Evidence:** `.artifacts/protocol-21/execution-session-log.md`
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
   * **Evidence:** `.artifacts/protocol-21/preflight-checklist.json`
   * **Validation:** Explicit "Go" confirmation documented

3. **`[GUIDELINE]` Note Quality Gate Plan:**
   * **Action:** Outline planned quality checks (tests, linting, audits) in `execution-session-log.md`.
   * **Evidence:** Updated `.artifacts/protocol-21/execution-session-log.md`
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
       * **Evidence:** `.artifacts/protocol-21/context-history.log`
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
       * **Evidence:** `.artifacts/protocol-21/subtask-evidence/{ID}/`
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
       * **Evidence:** `.artifacts/protocol-21/task-file-diff.patch`
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
       * **Evidence:** `.artifacts/protocol-21/quality-reports/{parentID}.json`
       * **Validation:** No unresolved critical issues

2. **`[MUST]` Sync Task State:**
   * **2.1. Run State Update Script:**
       * **Action:** Execute `python scripts/update_task_state.py --task-file .cursor/tasks/tasks-{feature}.md --task-id {parentID} --status complete --output .artifacts/protocol-21/task-state.json`
       * **Evidence:** Script execution log
       * **Validation:** State updated successfully
   
   * **2.2. Update Task Tracker:**
       * **Action:** Synchronize with external task tracking system
       * **Evidence:** `.artifacts/protocol-21/task-state.json`
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
       * **Evidence:** `.artifacts/protocol-21/parent-task-retrospective.md`
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
   * **Evidence:** `.artifacts/protocol-21/execution-session-log.md`
   * **Validation:** Summary comprehensive and accurate

2. **`[MUST]` Archive Evidence:**
   * **Action:** Ensure subtask artifacts, quality reports, and task diffs stored in `.artifacts/protocol-21/` with manifest `execution-artifact-manifest.json`.
   * **Evidence:** `.artifacts/protocol-21/execution-artifact-manifest.json`
   * **Validation:** All artifacts archived and indexed

3. **`[GUIDELINE]` Prepare Next Session Brief:**
   * **Action:** Document next parent task recommendation and outstanding blockers for upcoming session.
   * **Evidence:** Next session section in session log
   * **Validation:** Clear handoff for next session
