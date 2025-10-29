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
