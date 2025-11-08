---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 08: TECHNICAL TASK GENERATION (PLANNING COMPLIANT)

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 09
- **Protocol Name:** TECHNICAL TASK GENERATION (PLANNING COMPLIANT)
- **Protocol Owner:** Technical Lead
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-01
- **Last Updated:** 2025-11-06
- **Version:** 2.0

### Protocol Classification
- **Category:** Planning
- **Criticality:** High
- **Complexity:** Medium
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 07
- **Successor:** Protocol 09
- **Related Protocols:** [List related protocols]

### Protocol Metadata
- **Purpose:** Generate and organize development tasks from requirements
- **Success Criteria:** All quality gates pass, artifacts complete for next protocol
- **Failure Modes:** [List potential failure modes]
- **Recovery Procedure:** [Define recovery steps]

---
## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** Technical Lead
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** Can make decisions on protocol execution and quality gates
- **Escalation:** Technical Lead or Project Manager

#### Protocol Owner
- **Role:** Technical Lead
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** Can make decisions on protocol execution and quality gates

#### Downstream Owner
- **Role:** Protocol 09 Owner
- **Responsibilities:**
  - Receive handoff package
  - Validate inputs from this protocol
  - Provide feedback on quality
  - Confirm readiness for next phase
- **Authority:** [What decisions can they make]

### Role Interactions
- **Executor → Owner:** [Communication frequency and method]
- **Owner → Downstream:** [Handoff process]
- **Downstream → Executor:** [Feedback loop]

### Decision Authority Matrix
| Decision Type | Executor | Owner | Downstream | Executive |
|---------------|----------|-------|------------|-----------|
| [Decision 1] | ❌ | ✅ | ❌ | ❌ |
| [Decision 2] | ✅ | ✅ | ❌ | ❌ |
| [Decision 3] | ❌ | ❌ | ✅ | ❌ |
| [Decision 4] | ❌ | ❌ | ❌ | ✅ |

---
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
**Type:** Prerequisite  
**Purpose:** Confirm discovery context, rule coverage, and persona inventory before generating detailed tasks.

**Pass Criteria:**
- **Threshold:** Rule index coverage ≥95% and persona readiness score ≥0.9.  
- **Threshold:** Context freshness metric ≥0.9 across rule and persona data.  
- **Boolean Check:** Task context summary flag set to `complete` and stakeholder persona list verified.  
- **Boolean Check:** Rule index audit flag equals `pass` with zero stale entries detected.  
- **Metrics:** Coverage metrics, persona completeness metrics, and context freshness metrics captured in preparation report.  
- **Evidence Link:** `.artifacts/protocol-08/rule-index.json`, `.artifacts/protocol-08/task-context.md`, `.artifacts/protocol-08/task-personas.json`.

**Automation:**
- Script: `python3 scripts/validate_rule_index.py --input .artifacts/protocol-08/rule-index.json`
- Script: `python3 scripts/summarize_task_context.py --output .artifacts/protocol-08/task-context.md`
- Script: `python3 scripts/update_task_personas.py --input .artifacts/protocol-08/task-personas.json`
- CI/CD Integration: Workflow `protocol-08-context.yml` runs nightly to confirm coverage metrics and publish persona status.

**Failure Handling:**
- **Rollback:** Re-run discovery alignment, regenerate missing rule references, and capture updated personas.  
- **Notification:** Alert protocol owner and governance steward via Slack when coverage threshold breaches.  
- **Waiver:** Document waiver in `.artifacts/protocol-08/gate-waivers.json` with program lead approval if persona data pending.

### Gate 2: High-Level Task Approval Gate
**Type:** Execution  
**Purpose:** Validate that high-level tasks, dependencies, and WHY context earned stakeholder approval.

**Pass Criteria:**
- **Threshold:** Approval confidence score ≥0.92 and dependency resolution rate ≥95%.  
- **Threshold:** Stakeholder response rate ≥90% within SLA.  
- **Boolean Check:** Approval status recorded as `approved` and all blocking dependencies cleared.  
- **Boolean Check:** Approval log validation flag reports `pass` with zero pending signatures.  
- **Metrics:** Approval metrics, dependency metrics, and WHY coverage metrics logged in approval report.  
- **Evidence Link:** `.artifacts/protocol-08/high-level-tasks.json`, `.artifacts/protocol-08/task-approval-log.md`.

**Automation:**
- Script: `python3 scripts/validate_high_level_tasks.py --input .artifacts/protocol-08/high-level-tasks.json`
- Script: `python3 scripts/check_task_dependencies.py --input .artifacts/protocol-08/high-level-tasks.json --output .artifacts/protocol-08/task-dependency-report.json`
- Script: `python3 scripts/log_task_approvals.py --input .artifacts/protocol-08/task-approval-log.md`
- CI/CD Integration: Config `config/protocol_gates/08.yaml` drives workflow `protocol-08-approvals.yml` that enforces approval thresholds on pull requests.

**Failure Handling:**
- **Rollback:** Return to stakeholder review, refine task WHY statements, and rerun approval automation.  
- **Notification:** Notify product owner and PM when boolean check fails or threshold dips.  
- **Waiver:** Log waiver rationale in `gate-waivers.json` only with steering committee sign-off.

### Gate 3: Decomposition Integrity Gate
**Type:** Execution  
**Purpose:** Ensure detailed tasks include rule references, automation hooks, and persona mapping.

**Pass Criteria:**
- **Threshold:** Automation coverage ≥80% of high-level tasks and rule linkage completeness ≥100%.  
- **Threshold:** Persona assignment consistency ≥95% across subtasks.  
- **Boolean Check:** Each subtask contains at least one rule reference and assigned persona.  
- **Boolean Check:** Decomposition validation flag equals `pass` with no missing automation references.  
- **Metrics:** Linkage metrics, automation metrics, and persona coverage metrics summarized in decomposition matrix.  
- **Evidence Link:** `.cursor/tasks/tasks-{feature}.md`, `.artifacts/protocol-08/task-automation-matrix.json`, `.artifacts/protocol-08/task-personas.json`.

**Automation:**
- Script: `python3 scripts/validate_task_decomposition.py --task-file .cursor/tasks/tasks-{feature}.md`
- Script: `python3 scripts/audit_task_automation.py --matrix .artifacts/protocol-08/task-automation-matrix.json`
- Script: `python3 scripts/verify_task_personas.py --input .artifacts/protocol-08/task-personas.json`
- CI/CD Integration: Decomposition workflow posts metrics to governance dashboard on merge via `protocol-08-decomposition.yml`.

**Failure Handling:**
- **Rollback:** Rebuild subtask mapping, update automation assignments, and rerun validation scripts.  
- **Notification:** Alert automation lead when automation metric falls below target.  
- **Waiver:** Not permitted; decomposition integrity is mandatory.

### Gate 4: Task Validation Gate
**Type:** Completion  
**Purpose:** Confirm enriched tasks, validation outputs, and manifests prepared for downstream execution.

**Pass Criteria:**
- **Threshold:** Validation success rate ≥0.9 and enrichment coverage ≥90% of tasks.  
- **Threshold:** Manifest checksum confidence ≥0.98 before handoff.  
- **Boolean Check:** Task artifact manifest equals `complete` and QA sign-off recorded.  
- **Boolean Check:** Validation summary flag reports `pass` with zero open failures.  
- **Metrics:** Validation metrics, enrichment metrics, and manifest completeness metrics compiled in final report.  
- **Evidence Link:** `.artifacts/protocol-08/task-validation.json`, `.artifacts/protocol-08/task-enrichment.json`, `.artifacts/protocol-08/task-artifact-manifest.json`.

**Automation:**
- Script: `python3 scripts/validate_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-validation.json`
- Script: `python3 scripts/enrich_tasks.py --task-file .cursor/tasks/tasks-{feature}.md --output .artifacts/protocol-08/task-enrichment.json`
- Script: `python3 scripts/aggregate_evidence_2.py --output .artifacts/protocol-08/task-artifact-manifest.json`
- CI/CD Integration: Final validation workflow `protocol-08-final.yml` publishes summary to project channel with manifest checksum check.

**Failure Handling:**
- **Rollback:** Reopen decomposition, remediate failing tasks, and regenerate manifests.  
- **Notification:** Notify QA reviewer and Protocol 09 owner when boolean check fails.  
- **Waiver:** Waiver only allowed for enrichment coverage with CTO approval; document justification in `gate-waivers.json`.

### Compliance Integration
- **Industry Standards:** Tasks documented in CommonMark, JSON artifacts aligned with JSON Schema, and automation commands follow YAML CI/CD syntax.  
- **Security Requirements:** Task metadata respects SOC 2 audit logging, GDPR data minimization, and least-privilege access for automation outputs.  
- **Regulatory Compliance:** QA validation honors FTC transparency requirements and regulatory trace logs for industry-specific mandates.  
- **Governance:** Gate thresholds sourced from `config/protocol_gates/08.yaml`, synchronized with governance registry and automation dashboards.

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

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| rule-index artifact (rule-index.json) | Coverage metric ≥95%, freshness metric recorded | `.artifacts/protocol-08/rule-index.json` | Gate 1 evidence bundle |
| task-context artifact (task-context.md) | Context completeness metric ≥0.9, narrative metric documented | `.artifacts/protocol-08/task-context.md` | Gate 1 evidence narrative |
| task-personas artifact (task-personas.json) | Persona readiness metric ≥0.9, assignment metric tracked | `.artifacts/protocol-08/task-personas.json` | Gate 1 evidence log |
| high-level-tasks artifact (high-level-tasks.json) | Approval metric ≥0.92, dependency metric ≥95% | `.artifacts/protocol-08/high-level-tasks.json` | Gate 2 evidence package |
| task-approval-log artifact (task-approval-log.md) | Approval latency metric <24h, sign-off metric complete | `.artifacts/protocol-08/task-approval-log.md` | Gate 2 evidence ledger |
| tasks artifact (tasks-{feature}.md) | Rule linkage metric 100%, persona coverage metric recorded | `.cursor/tasks/tasks-{feature}.md` | Gate 3 evidence reference |
| task-automation-matrix artifact (task-automation-matrix.json) | Automation coverage metric ≥80%, script count metric documented | `.artifacts/protocol-08/task-automation-matrix.json` | Gate 3 evidence matrix |
| task-validation artifact (task-validation.json) | Validation success metric ≥0.9, failure metric logged | `.artifacts/protocol-08/task-validation.json` | Gate 4 evidence report |
| task-enrichment artifact (task-enrichment.json) | Enrichment coverage metric ≥90%, quality metric tracked | `.artifacts/protocol-08/task-enrichment.json` | Gate 4 evidence enhancement |
| task-artifact-manifest artifact (task-artifact-manifest.json) | Manifest completeness metric 100%, checksum metric verified | `.artifacts/protocol-08/task-artifact-manifest.json` | Gate 4 evidence manifest |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-08/`  
- **Subdirectories:** `approvals/` for stakeholder sign-offs, `decomposition/` for detailed task outputs, `logs/` for automation exports.  
- **Permissions:** Read/write for protocol executor, read-only for downstream protocols and governance auditors.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `task-approval-log.md`, `task-enrichment.json`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-08/task-artifact-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash stored for every artifact listed above.  
- Size: File size in bytes recorded for audit.  
- Dependencies: Upstream dependencies (Protocols 05-07 artifacts) and downstream consumers (Protocols 09, 21).

**Dependency Tracking:**
- Input: Protocol 07 handoff (`task-generation-input.json`), governance rule inventory, stakeholder persona catalog.  
- Output: All artifacts listed in table plus manifest.  
- Transformations: Context preparation → High-level approval → Decomposition → Validation and enrichment → Manifest aggregation.

**Coverage:** 100% of required artifacts documented with checksums and dependency references.

### Traceability

**Input Sources:**
- **Input From:** Protocol 07 `task-generation-input.json` – Architecture-aligned task seed data.  
- **Input From:** Protocol 06 `functional-requirements.md` – Requirement reference for task WHY mapping.  
- **Input From:** Governance rule index – Compliance constraints and automation rules.

**Output Artifacts:**
- **Output To:** `tasks-{feature}.md` – Execution package for Protocols 09 and 21.  
- **Output To:** `task-automation-matrix.json` – Automation blueprint for environment setup and execution.  
- **Output To:** `task-artifact-manifest.json` – Comprehensive inventory for audit and archival.  
- **Output To:** `task-validation.json` – Validation results consumed by QA and compliance reviewers.

**Transformation Steps:**
1. Rule index ingestion → Context summary creation → Persona alignment.  
2. Context outputs → High-level task drafting → Stakeholder approval capture.  
3. Approved tasks → Decomposition workflow → Detailed task files and automation matrix.  
4. Detailed tasks → Validation suite → Validation and enrichment reports.  
5. Validated outputs → Manifest generator → Final manifest and archival bundle.

**Audit Trail:**
- Manifest logs timestamps, checksums, and verified_by fields for every artifact.  
- Automation scripts emit execution logs stored in `.artifacts/protocol-08/logs/`.  
- Approval log references stakeholder signatures for governance traceability.  
- All evidence references cross-linked inside gate reports.

### Archival Strategy

**Compression:**
- Compress artifacts into `.artifacts/protocol-08/evidence-bundle.zip` after completion using ZIP standard compression level.

**Retention Policy:**
- Active artifacts retained for 120 days post-completion.  
- Archived bundles retained for 3 years after project closure.  
- Cleanup automation `scripts/cleanup_artifacts.py` enforces retention quarterly.

**Retrieval Procedures:**
- Active artifacts accessed directly from `.artifacts/protocol-08/` with read-only enforcement.  
- Archived bundles retrieved with `unzip .artifacts/protocol-08/evidence-bundle.zip` and verified against manifest checksums.  
- Recovery instructions stored in `decomposition/recovery-playbook.md`.

**Cleanup Process:**
- Quarterly cleanup logs actions to `.artifacts/protocol-08/cleanup-log.json`.  
- Critical artifacts flagged for extended retention require governance lead approval.  
- Manual overrides documented with timestamp and reviewer signature.

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

## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `run_protocol_gates.py` | Run Protocol Gates | `scripts/` | ✅ Exists |
| `gate_utils.py` | Gate Utils | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** Required artifacts from previous protocol
- **Output:** Protocol artifacts and validation reports
- **External Dependencies:** Python 3.8+, standard libraries

### Automation Hooks
- **Pre-execution:** Load context from previous protocol
- **During execution:** Validate protocol execution
- **Post-execution:** Generate evidence bundle

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

----------------|---------|----------|--------|
| `validate_gate_08_*.py` | Gate validation | `scripts/` | ✅ Exists |
| `verify_protocol_08.py` | Protocol verification | `scripts/` | ✅ Exists |
| `generate_artifacts_08.py` | Artifact generation | `scripts/` | ✅ Exists |
| `aggregate_evidence_08.py` | Evidence aggregation | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** Required artifacts from previous protocol
- **Output:** Protocol artifacts and validation reports
- **External Dependencies:** Python 3.8+, standard libraries

### Automation Hooks
- **Pre-execution:** Load context from previous protocol
- **During execution:** Validate protocol execution
- **Post-execution:** Generate evidence bundle

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---

## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Initialize protocol execution

**Description:** Setup environment and load prerequisites

Communication: Notify stakeholders of protocol start

Evidence: Track initialization in `.artifacts/protocol-08/workflow-logs/`

**Duration:** 15 minutes

---

### STEP 2

**Action:** Execute main protocol activities

**Description:** Perform core protocol tasks and validations

Communication: Document progress and any blockers

Evidence: Store artifacts in `.artifacts/protocol-08/`

**Duration:** Varies based on complexity

---

### STEP 3

**Action:** Validate and package results

**Description:** Run validation scripts and prepare handoff

Communication: Report completion status to stakeholders

Evidence: Generate validation report and evidence manifest

**Duration:** 20 minutes

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 3 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to supervisor

### Workflow State Management

- State stored in: `.artifacts/protocol-08/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-08/workflow-status.json`
- Execution logs: `.artifacts/protocol-08/workflow-logs/`
- Performance metrics: `.artifacts/protocol-08/workflow-metrics.json`

---

## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=08` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-08/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/08-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-08/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_08.py \
  --protocol 08 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 08` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-08/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 08 \
  --input .artifacts/protocol-08/input/ \
  --output .artifacts/protocol-08/output/ \
  --log-file .artifacts/protocol-08/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 08` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/protocol-08/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_08.py \
  --protocol 08 \
  --artifacts-dir .artifacts/protocol-08/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 08` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/protocol-08/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_08.py \
  --protocol 08 \
  --artifacts-dir .artifacts/protocol-08/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 08` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/protocol-08/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error

### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-08/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-08/execution.log`
2. Review error code and message
3. **Retry:** Re-run with `--error-handling retry` (up to 3 times)
4. **Fallback:** Run with `--error-handling escalate`
5. **Escalate:** Notify supervisor with logs

**If Command 3 (Aggregation) Fails:**
1. Verify all artifacts present in output directory
2. Check artifact file formats and integrity
3. **Fallback:** Run without `--output-manifest`
4. **Escalate:** If artifacts corrupted, restart from Command 2

**If Command 4 (Validation) Fails:**
1. Review validation report
2. Identify which quality gates failed
3. **Fallback:** Run with `--quality-gates relaxed`
4. **Escalate:** Return to Command 2 and remediate

### Scheduling & Execution Context

**Execution Timing:**
- Pre-execution: 5 minutes (setup + prerequisites validation)
- Main execution: 15-45 minutes (depends on protocol complexity)
- Post-execution: 10 minutes (aggregation + validation)
- Total: 30-60 minutes per protocol

**Parallel Execution:** Can run up to 4 protocols in parallel (if resources allow)

**CI/CD Integration:**
- Trigger on: Protocol file changes, manual trigger
- Timeout: 90 minutes per protocol
- Retry policy: 2 retries on transient failures
- Notification: Slack/Email on success/failure

### Monitoring & Logging

**Log Files:**
- `.artifacts/protocol-08/execution.log` - Main execution log
- `.artifacts/protocol-08/validation.log` - Validation log
- `.artifacts/protocol-08/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-08/workflow-status.json` - Real-time status
- `.artifacts/protocol-08/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-08/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-08/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-08-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol 09

### Handoff Verification
- [ ] Checksum verification passed
- [ ] Downstream protocol has received package
- [ ] Downstream protocol confirms receipt and readiness
- [ ] No outstanding questions or clarifications needed

### Sign-Off
- Protocol Owner: _________________ Date: _________
- Downstream Owner: _________________ Date: _________

---
## COMMUNICATION & STAKEHOLDER ALIGNMENT

### Status Announcements (Template)
```
[PROTOCOL 08 | PHASE X START] - [Action description]
[PROTOCOL 08 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 08 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Technical Lead - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** Development Team, Project Manager - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/protocol-08/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders

---