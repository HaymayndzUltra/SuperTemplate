---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 08: TECHNICAL TASK GENERATION (PLANNING COMPLIANT)

**Purpose:** Execute TECHNICAL TASK GENERATION workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `TECHNICAL-DESIGN.md` and `task-generation-input.json` from Protocol 07
- [ ] `prd-{feature}.md`, `user-stories.md`, `functional-requirements.md` from Protocol 06
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

## WORKFLOW

### STEP 1: Context Preparation

1. **`[MUST]` Index Governance Rules:**
   * **Action:** Locate rule directories, parse metadata (description, tags, triggers, scope), and build an index stored in `rule-index.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Indexing governance rules for task alignment."
   * **Halt condition:** Stop if rule directories missing or metadata incomplete.
   * **Evidence:** `.artifacts/protocol-08/rule-index.json`

2. **`[MUST]` Analyze Inputs:**
   * **Action:** Review PRD, technical design, and task-generation input to identify feature scope, implementation layers, and constraints; log summary in `task-context.md`.
   * **Evidence:** `.artifacts/protocol-08/task-context.md`

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
   * **Evidence:** `.artifacts/protocol-08/high-level-tasks.json`

3. **`[MUST]` Present for Approval:**
   * **Action:** Share high-level task list summary and await explicit "Go" before decomposition.
   * **Halt condition:** Do not proceed until approval recorded in `task-approval-log.md`.
   * **Evidence:** `.artifacts/protocol-08/task-approval-log.md`

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
   * **Evidence:** `.artifacts/protocol-08/task-automation-matrix.json`

3. **`[GUIDELINE]` Map Personas:**
   * **Action:** Assign LLM personas or role ownership per high-level task in `task-personas.json`.

### STEP 4: Validation and Packaging

1. **`[MUST]` Validate Task Structure:**
   * **Action:** Execute `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-validation.json` to ensure completeness and compliance.
   * **Communication:** 
     > "Task validation status: {status} - {issues} issues detected."
   * **Evidence:** `.artifacts/protocol-08/task-validation.json`

2. **`[MUST]` Enrich Task Metadata:**
   * **Action:** Run `python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-enrichment.json` to add effort estimates, risk flags, and automation coverage.
   * **Evidence:** `.artifacts/protocol-08/task-enrichment.json`

3. **`[MUST]` Archive Supporting Data:**
   * **Action:** Save rule index, personas, automation matrix, and validation outputs in `.artifacts/protocol-08/` with manifest `task-artifact-manifest.json`.

4. **`[GUIDELINE]` Summarize Execution Plan:**
   * **Action:** Produce `task-execution-summary.md` highlighting dependencies, automation, and readiness for Protocol 21.

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

## 2. INTEGRATION POINTS

### Inputs From:
- **Protocol 07**: `task-generation-input.json`, `TECHNICAL-DESIGN.md` - Architecture decomposition and sequencing.
- **Protocol 06**: `prd-{feature}.md`, `functional-requirements.md`, `validation-plan.md` - Detailed requirements and acceptance criteria.
- **Protocol 05**: `rule-audit-final.md`, `template-inventory.md` - Governance references and available accelerators.

### Outputs To:
- **Protocol 09**: `task-automation-matrix.json` - Automation readiness for environment setup.
- **Protocol 21**: `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json`, `task-execution-summary.md` - Execution blueprint.

### Artifact Storage Locations:
- `.artifacts/protocol-08/` - Primary evidence storage
- `.cursor/tasks/` - Task documentation repository

---

## 2. QUALITY GATES

### Gate 1: Context Preparation Gate
- **Criteria**: Rule index generated, task context summarized, personas identified.
- **Evidence**: `rule-index.json`, `task-context.md`, `task-personas.json`
- **Pass Threshold**: Rule index coverage ≥ 95% of rule directories.
- **Failure Handling**: Rebuild index, verify metadata completeness, rerun gate.
- **Automation**: `python scripts/validate_rule_index.py --input .artifacts/protocol-08/rule-index.json`

### Gate 2: High-Level Task Approval Gate
- **Criteria**: High-level tasks documented with WHY, complexity, dependencies; stakeholder approval logged.
- **Evidence**: `high-level-tasks.json`, `task-approval-log.md`
- **Pass Threshold**: Approval status recorded and dependencies resolved.
- **Failure Handling**: Revise tasks per feedback, re-seek approval, rerun gate.
- **Automation**: `python scripts/validate_high_level_tasks.py --input .artifacts/protocol-08/high-level-tasks.json`

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
[MASTER RAY™ | PHASE 1 START] - "Indexing rules and aligning context for task generation."
[MASTER RAY™ | PHASE 2 START] - "Drafting high-level task structure with dependencies and WHY context."
[MASTER RAY™ | PHASE 3 START] - "Decomposing tasks into actionable subtasks with rule mapping."
[MASTER RAY™ | PHASE 4 START] - "Running validation and enrichment on task plan."
[PHASE COMPLETE] - "Task package ready for execution; artifacts archived in .artifacts/protocol-08/."
[RAY ERROR] - "Issue encountered during [phase]; see automation logs for remediation."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "High-level tasks prepared with WHY context and dependencies. Evidence ready:
> - high-level-tasks.json
> - task-context.md
>
> Please reply 'Go' to authorize detailed decomposition."
```

### Error Handling:
```
[RAY GATE FAILED: Decomposition Integrity Gate]
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


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_2.py

# Quality gate automation
python scripts/validate_rule_index.py --input .artifacts/protocol-08/rule-index.json
python scripts/validate_high_level_tasks.py --input .artifacts/protocol-08/high-level-tasks.json
python scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md
python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-validation.json
python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-enrichment.json

# Evidence aggregation
python scripts/aggregate_evidence_2.py --output .artifacts/protocol-08/
```

### CI/CD Integration:
```yaml
name: Protocol 08 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 08 Gates
        run: python scripts/run_protocol_2_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review high-level tasks with stakeholders; document feedback in `manual-task-review.md`.
2. Manually verify automation commands; note results in `.artifacts/protocol-08/manual-automation-checklist.md`.
3. Archive manual validations in `.artifacts/protocol-08/manual-validation-log.md`.

---

## 2. HANDOFF CHECKLIST



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

### Handoff to Protocol 09:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 09: Environment Setup & Validation

**Evidence Package:**
- `tasks-{feature}.md` - Execution-ready task list
- `task-automation-matrix.json` - Automation references for environment setup and execution

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/09-environment-setup-validation.md
```

---

## 2. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `rule-index.json` | `.artifacts/protocol-08/` | Governance mapping for tasks | Protocol 21 |
| `high-level-tasks.json` | `.artifacts/protocol-08/` | Approved high-level task list | Protocol 21 |
| `tasks-{feature}.md` | `.cursor/tasks/` | Detailed task documentation | Protocol 21 |
| `task-automation-matrix.json` | `.artifacts/protocol-08/` | Automation mapping | Protocol 09 |
| `task-validation.json` | `.artifacts/protocol-08/` | Validation results | Protocol 21 |
| `task-enrichment.json` | `.artifacts/protocol-08/` | Enriched metadata | Protocol 21 |


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
