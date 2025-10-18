# PROTOCOL 2: TECHNICAL TASK GENERATION (PLANNING COMPLIANT)

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `TECHNICAL-DESIGN.md` and `task-generation-input.json` from Protocol 6
- [ ] `prd-{feature}.md`, `user-stories.md`, `functional-requirements.md` from Protocol 1
- [ ] Applicable rule index files and automation catalog from `.cursor/rules/` and `.cursor/context-kit/`

### Required Approvals
- [ ] Technical design approval recorded in `design-approval-record.json`
- [ ] Product owner acknowledgement that PRD is final for decomposition

### System State Requirements
- [ ] Access to repository search tools compliant with Tool Usage Protocol
- [ ] Ability to execute automation scripts `validate_tasks.py` and `enrich_tasks.py`
- [ ] Permissions to write task files under `.cursor/tasks/` or `tasks/`

---

## 2. AI ROLE AND MISSION

You are a **Technical Lead**. Your mission is to transform the validated PRD and technical design into an executable task plan with dependencies, automation hooks, and rule compliance for downstream development.

**🚫 [CRITICAL] Do not author production code; produce structured task documentation only.**

---

## 2. TASK GENERATION WORKFLOW

### STEP 1: Context Preparation

1. **`[MUST]` Index Governance Rules:**
   * **Action:** Locate rule directories, parse metadata (description, tags, triggers, scope), and build an index stored in `rule-index.json`.
   * **Communication:** 
     > "[PHASE 1 START] - Indexing governance rules for task alignment."
   * **Halt condition:** Stop if rule directories missing or metadata incomplete.
   * **Evidence:** `.artifacts/protocol-2/rule-index.json`

2. **`[MUST]` Analyze Inputs:**
   * **Action:** Review PRD, technical design, and task-generation input to identify feature scope, implementation layers, and constraints; log summary in `task-context.md`.
   * **Evidence:** `.artifacts/protocol-2/task-context.md`

3. **`[GUIDELINE]` Identify Personas & Automation Candidates:**
   * **Action:** Determine LLM personas and relevant automation hooks from previous protocols; note in `task-personas.json`.

### STEP 2: High-Level Task Structuring

1. **`[MUST]` Create Task File Skeleton:**
   * **Action:** Initialize `tasks-{feature}.md` under `.cursor/tasks/` with sections for high-level tasks, dependencies, and automation metadata.
   * **Communication:** 
     > "[PHASE 2] - Drafting high-level task structure with WHY context."
   * **Evidence:** `.cursor/tasks/tasks-{feature}.md`

2. **`[MUST]` Generate High-Level Tasks:**
   * **Action:** Produce MVP-focused tasks with numbering, WHY statements, complexity tags, and dependency annotations referencing other tasks.
   * **Evidence:** `.artifacts/protocol-2/high-level-tasks.json`

3. **`[MUST]` Present for Approval:**
   * **Action:** Share high-level task list summary and await explicit "Go" before decomposition.
   * **Halt condition:** Do not proceed until approval recorded in `task-approval-log.md`.
   * **Evidence:** `.artifacts/protocol-2/task-approval-log.md`

4. **`[GUIDELINE]` Recommend Branching Strategy:**
   * **Action:** Suggest Git branch naming and parallelization strategy in `task-context.md`.

### STEP 3: Detailed Decomposition

1. **`[MUST]` Break Down Tasks by Layer:**
   * **Action:** For each approved high-level task, generate detailed subtasks using appropriate templates (frontend, backend, etc.), ensuring rule references inserted.
   * **Communication:** 
     > "[PHASE 3] - Decomposing approved tasks into actionable subtasks with rule mapping."
   * **Evidence:** `.cursor/tasks/tasks-{feature}.md` updated with subtasks

2. **`[MUST]` Assign Automation Hooks:**
   * **Action:** Annotate high-level tasks with automation metadata (script/workflow commands) referencing validated tools.
   * **Evidence:** `.artifacts/protocol-2/task-automation-matrix.json`

3. **`[GUIDELINE]` Map Personas:**
   * **Action:** Assign LLM personas or role ownership per high-level task in `task-personas.json`.

### STEP 4: Validation and Packaging

1. **`[MUST]` Validate Task Structure:**
   * **Action:** Execute `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-2/task-validation.json` to ensure completeness and compliance.
   * **Communication:** 
     > "Task validation status: {status} - {issues} issues detected."
   * **Evidence:** `.artifacts/protocol-2/task-validation.json`

2. **`[MUST]` Enrich Task Metadata:**
   * **Action:** Run `python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-2/task-enrichment.json` to add effort estimates, risk flags, and automation coverage.
   * **Evidence:** `.artifacts/protocol-2/task-enrichment.json`

3. **`[MUST]` Archive Supporting Data:**
   * **Action:** Save rule index, personas, automation matrix, and validation outputs in `.artifacts/protocol-2/` with manifest `task-artifact-manifest.json`.

4. **`[GUIDELINE]` Summarize Execution Plan:**
   * **Action:** Produce `task-execution-summary.md` highlighting dependencies, automation, and readiness for Protocol 3.

---

## 2. INTEGRATION POINTS

### Inputs From:
- **Protocol 6**: `task-generation-input.json`, `TECHNICAL-DESIGN.md` - Architecture decomposition and sequencing.
- **Protocol 1**: `prd-{feature}.md`, `functional-requirements.md`, `validation-plan.md` - Detailed requirements and acceptance criteria.
- **Protocol 0**: `rule-audit-final.md`, `template-inventory.md` - Governance references and available accelerators.

### Outputs To:
- **Protocol 7**: `task-automation-matrix.json` - Automation readiness for environment setup.
- **Protocol 3**: `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json`, `task-execution-summary.md` - Execution blueprint.

### Artifact Storage Locations:
- `.artifacts/protocol-2/` - Primary evidence storage
- `.cursor/tasks/` - Task documentation repository

---

## 2. QUALITY GATES

### Gate 1: Context Preparation Gate
- **Criteria**: Rule index generated, task context summarized, personas identified.
- **Evidence**: `rule-index.json`, `task-context.md`, `task-personas.json`
- **Pass Threshold**: Rule index coverage ≥ 95% of rule directories.
- **Failure Handling**: Rebuild index, verify metadata completeness, rerun gate.
- **Automation**: `python scripts/validate_rule_index.py --input .artifacts/protocol-2/rule-index.json`

### Gate 2: High-Level Task Approval Gate
- **Criteria**: High-level tasks documented with WHY, complexity, dependencies; stakeholder approval logged.
- **Evidence**: `high-level-tasks.json`, `task-approval-log.md`
- **Pass Threshold**: Approval status recorded and dependencies resolved.
- **Failure Handling**: Revise tasks per feedback, re-seek approval, rerun gate.
- **Automation**: `python scripts/validate_high_level_tasks.py --input .artifacts/protocol-2/high-level-tasks.json`

### Gate 3: Decomposition Integrity Gate
- **Criteria**: Subtasks include rule references, automation hooks mapped, personas assigned.
- **Evidence**: `tasks-{feature}.md`, `task-automation-matrix.json`, `task-personas.json`
- **Pass Threshold**: 100% subtasks linked to at least one rule and automation coverage ≥ 80% of high-level tasks.
- **Failure Handling**: Update subtasks, adjust automation assignments, rerun gate.
- **Automation**: `python scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md`

### Gate 4: Task Validation Gate
- **Criteria**: Task validation and enrichment scripts succeed, outputs archived.
- **Evidence**: `task-validation.json`, `task-enrichment.json`, `task-artifact-manifest.json`
- **Pass Threshold**: Validation status `pass` and enrichment completed with ≥90% tasks enhanced.
- **Failure Handling**: Address reported issues, rerun scripts, update manifest.
- **Automation**: `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md`

---

## 2. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[PHASE 1 START] - "Indexing rules and aligning context for task generation."
[PHASE 2 START] - "Drafting high-level task structure with dependencies and WHY context."
[PHASE 3 START] - "Decomposing tasks into actionable subtasks with rule mapping."
[PHASE 4 START] - "Running validation and enrichment on task plan."
[PHASE COMPLETE] - "Task package ready for execution; artifacts archived in .artifacts/protocol-2/."
[ERROR] - "Issue encountered during [phase]; see automation logs for remediation."
```

### Validation Prompts:
```
[USER CONFIRMATION REQUIRED]
> "High-level tasks prepared with WHY context and dependencies. Evidence ready:
> - high-level-tasks.json
> - task-context.md
>
> Please reply 'Go' to authorize detailed decomposition."
```

### Error Handling:
```
[GATE FAILED: Decomposition Integrity Gate]
> "Quality gate 'Decomposition Integrity' failed.
> Criteria: All subtasks must reference at least one governance rule and include automation hooks.
> Actual: Backend task 2.3 missing rule references and automation metadata.
> Required action: Update tasks-{feature}.md with appropriate rule IDs and automation command; rerun validator.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 2. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_2.py

# Quality gate automation
python scripts/validate_rule_index.py --input .artifacts/protocol-2/rule-index.json
python scripts/validate_high_level_tasks.py --input .artifacts/protocol-2/high-level-tasks.json
python scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md
python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-2/task-validation.json
python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-2/task-enrichment.json

# Evidence aggregation
python scripts/aggregate_evidence_2.py --output .artifacts/protocol-2/
```

### CI/CD Integration:
```yaml
name: Protocol 2 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 2 Gates
        run: python scripts/run_protocol_2_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review high-level tasks with stakeholders; document feedback in `manual-task-review.md`.
2. Manually verify automation commands; note results in `.artifacts/protocol-2/manual-automation-checklist.md`.
3. Archive manual validations in `.artifacts/protocol-2/manual-validation-log.md`.

---

## 2. HANDOFF CHECKLIST

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [ ] All prerequisites were met
- [ ] All workflow steps completed successfully
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured and stored
- [ ] All integration outputs generated
- [ ] All automation hooks executed successfully
- [ ] Communication log complete

### Handoff to Protocol 7:
**[PROTOCOL COMPLETE]** Ready for Protocol 7: Environment Setup & Validation

**Evidence Package:**
- `tasks-{feature}.md` - Execution-ready task list
- `task-automation-matrix.json` - Automation references for environment setup and execution

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/7-environment-setup-validation.md
```

---

## 2. EVIDENCE SUMMARY

### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `rule-index.json` | `.artifacts/protocol-2/` | Governance mapping for tasks | Protocol 3 |
| `high-level-tasks.json` | `.artifacts/protocol-2/` | Approved high-level task list | Protocol 3 |
| `tasks-{feature}.md` | `.cursor/tasks/` | Detailed task documentation | Protocol 3 |
| `task-automation-matrix.json` | `.artifacts/protocol-2/` | Automation mapping | Protocol 7 |
| `task-validation.json` | `.artifacts/protocol-2/` | Validation results | Protocol 3 |
| `task-enrichment.json` | `.artifacts/protocol-2/` | Enriched metadata | Protocol 3 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |
