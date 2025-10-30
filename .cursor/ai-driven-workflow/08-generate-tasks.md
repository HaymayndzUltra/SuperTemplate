---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 08: TECHNICAL TASK GENERATION (PLANNING COMPLIANT)

**Purpose:** Execute TECHNICAL TASK GENERATION workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `TECHNICAL-DESIGN.md` and `task-generation-input.json` from Protocol 07
- **`[MUST]`** `prd-{feature}.md`, `user-stories.md`, `functional-requirements.md` from Protocol 06
- **`[MUST]`** Applicable rule index files and automation catalog from `.cursor/rules/` and `.cursor/context-kit/`

### 1.2 Required Approvals
- **`[MUST]`** Technical design approval recorded in `design-approval-record.json`
- **`[MUST]`** Product owner acknowledgement that PRD is final for decomposition

### 1.3 System State Requirements
- **`[MUST]`** Access to repository search tools compliant with Tool Usage Protocol
- **`[MUST]`** Ability to execute automation scripts `validate_tasks.py` and `enrich_tasks.py`
- **`[MUST]`** Permissions to write task files under `.cursor/tasks/` or `tasks/`

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

**`[STRICT]` Role Definition:**
You are a **Technical Lead**. Your mission is to transform the validated PRD and technical design into an executable task plan with dependencies, automation hooks, and rule compliance for downstream development.

**🚫 [CRITICAL] Directive:**
Do not author production code; produce structured task documentation only.

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Context Preparation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for indexing rules and analyzing inputs -->

1. **`[MUST]` Index Governance Rules:**
   * **Action:** Locate rule directories, parse metadata (description, tags, triggers, scope), and build an index stored in `rule-index.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Indexing governance rules for task alignment."
   * **Halt condition:** Stop if rule directories missing or metadata incomplete.
   * **Evidence:** `.artifacts/protocol-08/rule-index.json`
   * **Validation:** Rule index covers ≥ 95% of rule directories

2. **`[MUST]` Analyze Inputs:**
   * **Action:** Review PRD, technical design, and task-generation input to identify feature scope, implementation layers, and constraints; log summary in `task-context.md`.
   * **Evidence:** `.artifacts/protocol-08/task-context.md`
   * **Validation:** Context document complete with all inputs analyzed

3. **`[GUIDELINE]` Identify Personas & Automation Candidates:**
   * **Action:** Determine LLM personas and relevant automation hooks from previous protocols; note in `task-personas.json`.
   * **Evidence:** `.artifacts/protocol-08/task-personas.json`
   * **Validation:** Personas mapped to task categories

### STEP 2: High-Level Task Structuring
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical decision point requiring stakeholder approval and WHY context for tasks -->

1. **`[MUST]` Create Task File Skeleton:**
   * **Action:** Initialize `tasks-{feature}.md` under `.cursor/tasks/` with sections for high-level tasks, dependencies, and automation metadata.
   * **Communication:** 
     > "[PHASE 2] - Drafting high-level task structure with WHY context."
   
   **[REASONING]:**
   - **Premises:** Tasks must align with technical design and be executable by downstream protocols
   - **Constraints:** Resource availability, timeline requirements, rule compliance mandates
   - **Alternatives Considered:**
     * **A)** Single monolithic task file - Rejected: Lacks granularity for parallel execution
     * **B)** Task per component - Selected: Enables parallel work and clear ownership
     * **C)** Task per layer - Considered: May be used for cross-cutting concerns
   - **Decision:** Component-based task structuring with dependency mapping
   - **Evidence:** Technical design boundaries, PRD feature scope
   - **Risks & Mitigations:**
     * **Risk:** Task interdependencies create bottlenecks → **Mitigation:** Explicit dependency matrix
     * **Risk:** Over-decomposition creates overhead → **Mitigation:** Group related subtasks
   - **Acceptance Link:** Technical design component mapping
   
   * **Evidence:** `.cursor/tasks/tasks-{feature}.md`
   * **Validation:** Task file structure follows template

2. **`[MUST]` Generate High-Level Tasks:**
   * **Action:** Produce MVP-focused tasks with numbering, WHY statements, complexity tags, and dependency annotations referencing other tasks.
   
   **[REASONING]:**
   - **Premises:** Each task must have clear business value and technical rationale
   - **Constraints:** MVP scope limitations, available expertise, automation capabilities
   - **WHY Context Requirements:**
     * Business justification for the task
     * Technical necessity explanation
     * Impact if task is not completed
   - **Decision:** Include comprehensive WHY statements for every high-level task
   - **Evidence:** PRD business requirements, stakeholder priorities
   - **Acceptance Link:** PRD validation criteria
   
   * **Evidence:** `.artifacts/protocol-08/high-level-tasks.json`
   * **Validation:** All tasks have WHY statements and complexity ratings

3. **`[MUST]` Present for Approval:**
   * **Action:** Share high-level task list summary and await explicit "Go" before decomposition.
   * **Halt condition:** Do not proceed until approval recorded in `task-approval-log.md`.
   * **Evidence:** `.artifacts/protocol-08/task-approval-log.md`
   * **Validation:** Explicit "Go" approval documented

4. **`[GUIDELINE]` Recommend Branching Strategy:**
   * **Action:** Suggest Git branch naming and parallelization strategy in `task-context.md`.
   * **Evidence:** Updated `.artifacts/protocol-08/task-context.md`
   * **Validation:** Branching strategy aligns with task dependencies

### STEP 3: Detailed Decomposition
<!-- [Category: EXECUTION-SUBSTEPS] -->
<!-- Why: Multiple precise substeps for detailed task breakdown with rule mapping and automation -->

1. **`[MUST]` Break Down Tasks by Layer:**
   * **1.1. Frontend Layer Decomposition:**
       * **Action:** Generate UI component tasks with styling, state management, and interaction requirements
       * **Evidence:** Updated `.cursor/tasks/tasks-{feature}.md` with frontend subtasks
       * **Validation:** Each UI component has corresponding task
   
   * **1.2. Backend Layer Decomposition:**
       * **Action:** Create API endpoint tasks with request/response schemas and business logic
       * **Evidence:** Updated `.cursor/tasks/tasks-{feature}.md` with backend subtasks
       * **Validation:** All API endpoints documented
   
   * **1.3. Data Layer Decomposition:**
       * **Action:** Define database schema tasks, migration scripts, and data access patterns
       * **Evidence:** Updated `.cursor/tasks/tasks-{feature}.md` with data subtasks
       * **Validation:** Data models align with technical design
   
   * **1.4. Integration Layer Decomposition:**
       * **Action:** Specify integration tasks for external services and third-party APIs
       * **Evidence:** Updated `.cursor/tasks/tasks-{feature}.md` with integration subtasks
       * **Validation:** All external dependencies identified
   
   * **1.5. Testing Layer Decomposition:**
       * **Action:** Generate test tasks including unit, integration, and end-to-end test requirements
       * **Evidence:** Updated `.cursor/tasks/tasks-{feature}.md` with testing subtasks
       * **Validation:** Test coverage targets specified
   
   * **Communication:** 
     > "[PHASE 3] - Decomposing approved tasks into actionable subtasks with rule mapping."

2. **`[MUST]` Assign Automation Hooks:**
   * **2.1. Script Automation Mapping:**
       * **Action:** Link validation scripts to relevant tasks
       * **Evidence:** Automation annotations in task file
       * **Validation:** Critical tasks have automation hooks
   
   * **2.2. CI/CD Integration Points:**
       * **Action:** Identify tasks requiring pipeline integration
       * **Evidence:** CI/CD markers in task documentation
       * **Validation:** Deployment tasks have pipeline hooks
   
   * **2.3. Tool Command References:**
       * **Action:** Add specific tool commands for task execution
       * **Evidence:** `.artifacts/protocol-08/task-automation-matrix.json`
       * **Validation:** Commands are executable and tested

3. **`[GUIDELINE]` Map Personas:**
   * **3.1. Technical Persona Assignment:**
       * **Action:** Assign appropriate LLM personas for technical tasks
       * **Evidence:** Persona mapping in `task-personas.json`
       * **Validation:** Each task category has persona
   
   * **3.2. Role-Based Ownership:**
       * **Action:** Define human role ownership where LLM assistance ends
       * **Evidence:** Ownership matrix in task documentation
       * **Validation:** Clear handoff points identified

### STEP 4: Validation and Packaging
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward validation execution and artifact packaging -->

1. **`[MUST]` Validate Task Structure:**
   * **Action:** Execute `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-validation.json` to ensure completeness and compliance.
   * **Communication:** 
     > "Task validation status: {status} - {issues} issues detected."
   * **Evidence:** `.artifacts/protocol-08/task-validation.json`
   * **Validation:** All validation checks pass

2. **`[MUST]` Enrich Task Metadata:**
   * **Action:** Run `python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-enrichment.json` to add effort estimates, risk flags, and automation coverage.
   * **Evidence:** `.artifacts/protocol-08/task-enrichment.json`
   * **Validation:** ≥90% tasks have enriched metadata

3. **`[MUST]` Archive Supporting Data:**
   * **Action:** Save rule index, personas, automation matrix, and validation outputs in `.artifacts/protocol-08/` with manifest `task-artifact-manifest.json`.
   * **Evidence:** `.artifacts/protocol-08/task-artifact-manifest.json`
   * **Validation:** All artifacts listed in manifest

4. **`[GUIDELINE]` Summarize Execution Plan:**
   * **Action:** Produce `task-execution-summary.md` highlighting dependencies, automation, and readiness for Protocol 21.
   * **Evidence:** `.artifacts/protocol-08/task-execution-summary.md`
   * **Validation:** Summary covers all critical paths

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
- **Protocol 07:** `task-generation-input.json`, `TECHNICAL-DESIGN.md` - Architecture decomposition and sequencing.
- **Protocol 06:** `prd-{feature}.md`, `functional-requirements.md`, `validation-plan.md` - Detailed requirements and acceptance criteria.
- **Protocol 05:** `rule-audit-final.md`, `template-inventory.md` - Governance references and available accelerators.

### 5.2 Outputs To:
- **Protocol 09:** `task-automation-matrix.json` - Automation readiness for environment setup.
- **Protocol 21:** `tasks-{feature}.md`, `task-validation.json`, `task-enrichment.json`, `task-execution-summary.md` - Execution blueprint.

### 5.3 Artifact Storage Locations:
- **Primary Evidence:** `.artifacts/protocol-08/` - Primary evidence storage
- **Task Repository:** `.cursor/tasks/` - Task documentation repository

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Context Preparation Gate
- **`[STRICT]` Criteria:** Rule index generated, task context summarized, personas identified.
- **Evidence:** `rule-index.json`, `task-context.md`, `task-personas.json`
- **Pass Threshold:** Rule index coverage ≥ 95% of rule directories.
- **Failure Handling:** Rebuild index, verify metadata completeness, rerun gate.
- **Automation:** `python scripts/validate_rule_index.py --input .artifacts/protocol-08/rule-index.json`

### Gate 2: High-Level Task Approval Gate
- **`[STRICT]` Criteria:** High-level tasks documented with WHY, complexity, dependencies; stakeholder approval logged.
- **Evidence:** `high-level-tasks.json`, `task-approval-log.md`
- **Pass Threshold:** Approval status recorded and dependencies resolved.
- **Failure Handling:** Revise tasks per feedback, re-seek approval, rerun gate.
- **Automation:** `python scripts/validate_high_level_tasks.py --input .artifacts/protocol-08/high-level-tasks.json`

### Gate 3: Decomposition Integrity Gate
- **`[STRICT]` Criteria:** Subtasks include rule references, automation hooks mapped, personas assigned.
- **Evidence:** `tasks-{feature}.md`, `task-automation-matrix.json`, `task-personas.json`
- **Pass Threshold:** 100% subtasks linked to at least one rule and automation coverage ≥ 80% of high-level tasks.
- **Failure Handling:** Update subtasks, adjust automation assignments, rerun gate.
- **Automation:** `python scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md`

### Gate 4: Task Validation Gate
- **`[STRICT]` Criteria:** Task validation and enrichment scripts succeed, outputs archived.
- **Evidence:** `task-validation.json`, `task-enrichment.json`, `task-artifact-manifest.json`
- **Pass Threshold:** Validation status `pass` and enrichment completed with ≥90% tasks enhanced.
- **Failure Handling:** Address reported issues, rerun scripts, update manifest.
- **Automation:** `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md`

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### 7.1 Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Indexing rules and aligning context for task generation."
[MASTER RAY™ | PHASE 2 START] - "Drafting high-level task structure with dependencies and WHY context."
[MASTER RAY™ | PHASE 3 START] - "Decomposing tasks into actionable subtasks with rule mapping."
[MASTER RAY™ | PHASE 4 START] - "Running validation and enrichment on task plan."
[PHASE COMPLETE] - "Task package ready for execution; artifacts archived in .artifacts/protocol-08/."
[RAY ERROR] - "Issue encountered during [phase]; see automation logs for remediation."
```

### 7.2 Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "High-level tasks prepared with WHY context and dependencies. Evidence ready:
> - high-level-tasks.json
> - task-context.md
>
> Please reply 'Go' to authorize detailed decomposition."
```

### 7.3 Error Handling:
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

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### 8.1 Validation Scripts:

1. **`[MUST]` Prerequisite Validation:**
   * **Action:** Run prerequisite check script
   * **Command:** `python scripts/validate_prerequisites_2.py`
   * **Evidence:** Script execution log
   * **Validation:** All prerequisites met

2. **`[MUST]` Quality Gate Automation:**
   * **Action:** Execute quality gate validation scripts
   * **Commands:**
     - `python scripts/validate_rule_index.py --input .artifacts/protocol-08/rule-index.json`
     - `python scripts/validate_high_level_tasks.py --input .artifacts/protocol-08/high-level-tasks.json`
     - `python scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md`
     - `python scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-validation.json`
     - `python scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-enrichment.json`
   * **Evidence:** Validation reports
   * **Validation:** All gates pass or have waivers

3. **`[MUST]` Evidence Aggregation:**
   * **Action:** Aggregate all protocol evidence
   * **Command:** `python scripts/aggregate_evidence_2.py --output .artifacts/protocol-08/`
   * **Evidence:** Aggregated evidence report
   * **Validation:** All evidence artifacts present

### 8.2 CI/CD Integration:
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

### 8.3 Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review high-level tasks with stakeholders; document feedback in `manual-task-review.md`.
2. Manually verify automation commands; note results in `.artifacts/protocol-08/manual-automation-checklist.md`.
3. Archive manual validations in `.artifacts/protocol-08/manual-validation-log.md`.

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

### 9.3 Handoff to Protocol 09:

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

## 10. EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for evidence collection and quality metrics -->

### 10.1 Learning and Improvement Mechanisms

**`[STRICT]` Feedback Collection:** 
All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**`[STRICT]` Improvement Tracking:** 
Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**`[GUIDELINE]` Knowledge Integration:** 
Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**`[GUIDELINE]` Adaptation:** 
Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.

### 10.2 Generated Artifacts:

| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `rule-index.json` | `.artifacts/protocol-08/` | Governance mapping for tasks | Protocol 21 |
| `high-level-tasks.json` | `.artifacts/protocol-08/` | Approved high-level task list | Protocol 21 |
| `tasks-{feature}.md` | `.cursor/tasks/` | Detailed task documentation | Protocol 21 |
| `task-automation-matrix.json` | `.artifacts/protocol-08/` | Automation mapping | Protocol 09 |
| `task-validation.json` | `.artifacts/protocol-08/` | Validation results | Protocol 21 |
| `task-enrichment.json` | `.artifacts/protocol-08/` | Enriched metadata | Protocol 21 |

### 10.3 Traceability Matrix

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

### 10.4 Quality Metrics:

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 95% | [TBD] | ⏳ |
| Evidence Completeness | 100% | [TBD] | ⏳ |
| Integration Integrity | 100% | [TBD] | ⏳ |

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
