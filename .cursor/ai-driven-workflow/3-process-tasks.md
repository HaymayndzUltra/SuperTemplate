# PROTOCOL 3: CONTROLLED TASK EXECUTION (DELIVERY COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json` from Protocol 2
- [ ] `ENVIRONMENT-README.md`, `validation-suite-report.json` from Protocol 7
- [ ] `rule-index.json` and applicable governance rules from `.cursor/rules/`

### Required Approvals
- [ ] Engineering lead authorization to begin execution on selected tasks
- [ ] QA lead acknowledgement of quality gate responsibilities

### System State Requirements
- [ ] Validated development environment configured per Protocol 7
- [ ] Access to required repositories, CI/CD tooling, and documentation
- [ ] Automation scripts `update_task_state.py`, `/review`, and quality audit tools available

---

## 3. AI ROLE AND MISSION

You are an **AI Paired Developer**. Your mission is to execute the approved task plan with strict adherence to governance rules, quality gates, and evidence capture until all parent tasks are complete.

**🚫 [CRITICAL] Do not modify tasks outside the authorized task file or skip quality gates; progress must remain auditable.**

---

## 3. EXECUTION WORKFLOW

### STEP 1: Pre-Execution Alignment

1. **`[MUST]` Select Parent Task:**
   * **Action:** Identify next unchecked parent task from `tasks-{feature}.md`; document selection in `execution-session-log.md`.
   * **Communication:** 
     > "[PHASE 1 START] - Preparing to execute parent task {ID}: {Title}."
   * **Halt condition:** Await confirmation if task ambiguity detected.
   * **Evidence:** `.artifacts/protocol-3/execution-session-log.md`

2. **`[MUST]` Confirm Recommended Model & Environment:**
   * **Action:** Read recommended model tag in task file, verify environment readiness (tool versions, credentials) referencing Protocol 7 outputs; log results.
   * **Communication:** 
     > "[PRE-FLIGHT] Recommended model: {Model}. Environment diagnostics verified. Reply 'Go' to proceed."
   * **Halt condition:** Do not start execution until confirmation received.
   * **Evidence:** `.artifacts/protocol-3/preflight-checklist.json`

3. **`[GUIDELINE]` Note Quality Gate Plan:**
   * **Action:** Outline planned quality checks (tests, linting, audits) in `execution-session-log.md`.

### STEP 2: Subtask Execution Loop

1. **`[MUST]` Load Subtask Context:**
   * **Action:** For each unchecked subtask, gather rule references (`[APPLIES RULES: ...]`), load documentation, and announce context loading.
   * **Communication:** 
     > "[CONTEXT LOADED] Subtask {ID} applying rules: {rule list}."
   * **Evidence:** `.artifacts/protocol-3/context-history.log`

2. **`[MUST]` Execute Subtask:**
   * **Action:** Perform implementation steps using allowed tools, keeping scope limited to the subtask description and loaded rules.
   * **Evidence:** `.artifacts/protocol-3/subtask-evidence/{ID}/`

3. **`[MUST]` Update Task File & Commit Strategy:**
   * **Action:** Mark subtask as complete in `tasks-{feature}.md`, propose semantic commit message, and log actions in `execution-session-log.md`.
   * **Evidence:** `.artifacts/protocol-3/task-file-diff.patch`

4. **`[GUIDELINE]` Capture Quick Validation:**
   * **Action:** Run targeted tests or linting relevant to subtask and record results.

### STEP 3: Parent Task Completion

1. **`[MUST]` Run Comprehensive Quality Gate:**
   * **Action:** Execute `/review` or `.cursor/ai-driven-workflow/4-quality-audit.md --mode comprehensive`, analyze CI results, and resolve CRITICAL/HIGH findings.
   * **Communication:** 
     > "[QUALITY GATE] Running comprehensive audit for parent task {ID}."
   * **Evidence:** `.artifacts/protocol-3/quality-reports/{parentID}.json`

2. **`[MUST]` Sync Task State:**
   * **Action:** Run `python scripts/update_task_state.py --task-file .cursor/tasks/tasks-{feature}.md --task-id {parentID} --status complete --output .artifacts/protocol-3/task-state.json` and update task tracker.
   * **Evidence:** `.artifacts/protocol-3/task-state.json`

3. **`[MUST]` Document Retrospective Snapshot:**
   * **Action:** Summarize work, risks, remaining issues in `parent-task-retrospective.md`; note commit decisions.
   * **Evidence:** `.artifacts/protocol-3/parent-task-retrospective.md`

4. **`[GUIDELINE]` Recommend Commit Strategy:**
   * **Action:** Suggest keeping granular commits or squashing based on complexity; await human confirmation before executing.

### STEP 4: Session Closeout

1. **`[MUST]` Record Session Summary:**
   * **Action:** Update `execution-session-log.md` with completed subtasks, quality gate status, CI outcomes, and approvals.
   * **Evidence:** `.artifacts/protocol-3/execution-session-log.md`

2. **`[MUST]` Archive Evidence:**
   * **Action:** Ensure subtask artifacts, quality reports, and task diffs stored in `.artifacts/protocol-3/` with manifest `execution-artifact-manifest.json`.

3. **`[GUIDELINE]` Prepare Next Session Brief:**
   * **Action:** Document next parent task recommendation and outstanding blockers for upcoming session.

---

## 3. INTEGRATION POINTS

### Inputs From:
- **Protocol 2**: `tasks-{feature}.md`, `task-automation-matrix.json` - Task blueprint and automation references.
- **Protocol 7**: `ENVIRONMENT-README.md`, `validation-suite-report.json` - Validated environment baseline.
- **Protocol 4**: Quality audit tooling references used within execution.

### Outputs To:
- **Protocol 4**: `quality-reports/{parentID}.json`, `execution-session-log.md` - Inputs for quality audits.
- **Protocol 9**: `execution-artifact-manifest.json`, `task-state.json` - Evidence for integration testing.

### Artifact Storage Locations:
- `.artifacts/protocol-3/` - Primary evidence storage
- `.cursor/tasks/` - Task status source of truth

---

## 3. QUALITY GATES

### Gate 1: Preflight Confirmation Gate
- **Criteria**: Parent task selected, recommended model confirmed, environment readiness validated.
- **Evidence**: `preflight-checklist.json`, `execution-session-log.md`
- **Pass Threshold**: Confirmation from human reviewer and environment diagnostics success.
- **Failure Handling**: Resolve configuration issues, re-run diagnostics, reconfirm model.
- **Automation**: `python scripts/validate_preflight.py --input .artifacts/protocol-3/preflight-checklist.json`

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
- **Automation**: `python scripts/validate_quality_gate.py --report .artifacts/protocol-3/quality-reports/{parentID}.json`

### Gate 4: Session Closure Gate
- **Criteria**: Task state synchronized, evidence manifest updated, next session brief prepared.
- **Evidence**: `task-state.json`, `execution-artifact-manifest.json`, `execution-session-log.md`
- **Pass Threshold**: All outputs generated and stored.
- **Failure Handling**: Regenerate missing artifacts, rerun synchronization script.
- **Automation**: `python scripts/validate_session_closeout.py --manifest .artifacts/protocol-3/execution-artifact-manifest.json`

---

## 3. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[PHASE 1 START] - "Preparing execution session for parent task {ID}."
[PRE-FLIGHT] - "Recommended model {Model}. Environment verified. Reply 'Go' to proceed."
[PHASE 2 START] - "Executing subtasks with governance rules loaded."
[QUALITY GATE] - "Running comprehensive audit and CI checks for parent task {ID}."
[PHASE 4 START] - "Archiving evidence and summarizing session outcomes."
[PHASE COMPLETE] - "Execution session closed; evidence archived in .artifacts/protocol-3/."
[ERROR] - "Execution halted due to [issue]; awaiting instructions."
```

### Validation Prompts:
```
[USER CONFIRMATION REQUIRED]
> "Parent task {ID} completed. Quality gate results:
> - Audit score: {score}/10
> - CI status: {summary}
>
> Confirm commit strategy (keep granular/squash) and authorize proceeding to next session?"
```

### Error Handling:
```
[GATE FAILED: Parent Task Quality Gate]
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

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_3.py

# Quality gate automation
python scripts/validate_preflight.py --input .artifacts/protocol-3/preflight-checklist.json
python scripts/validate_subtask_compliance.py --task-file .cursor/tasks/tasks-{feature}.md
python scripts/validate_quality_gate.py --report .artifacts/protocol-3/quality-reports/{parentID}.json
python scripts/validate_session_closeout.py --manifest .artifacts/protocol-3/execution-artifact-manifest.json

# Evidence aggregation
python scripts/aggregate_evidence_3.py --output .artifacts/protocol-3/
```

### CI/CD Integration:
```yaml
name: Protocol 3 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 3 Gates
        run: python scripts/run_protocol_3_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Log manual preflight checks in `manual-preflight.md`.
2. Perform peer review of subtask evidence; document in `.artifacts/protocol-3/manual-review-notes.md`.
3. Store manual quality gate approvals in `.artifacts/protocol-3/manual-validation-log.md`.

---

## 3. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 9:
**[PROTOCOL COMPLETE]** Ready for Protocol 9: Integration Testing & System Validation

**Evidence Package:**
- `execution-artifact-manifest.json` - Comprehensive record of execution evidence
- `task-state.json` - Synchronization record for downstream validation

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/9-integration-testing.md
```

---

## 3. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `execution-session-log.md` | `.artifacts/protocol-3/` | Session activity log | Protocol 4 |
| `context-history.log` | `.artifacts/protocol-3/` | Rule/context traceability | Protocol 4 |
| `quality-reports/{parentID}.json` | `.artifacts/protocol-3/` | Quality gate results | Protocol 9 |
| `task-state.json` | `.artifacts/protocol-3/` | Task tracker synchronization | Protocol 9 |
| `execution-artifact-manifest.json` | `.artifacts/protocol-3/` | Evidence catalog | Protocol 9 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
