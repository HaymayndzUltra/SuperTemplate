---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 07: TECHNICAL DESIGN & ARCHITECTURE (ARCHITECTURE COMPLIANT)

**Purpose:** Execute TECHNICAL DESIGN & ARCHITECTURE workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `prd-{feature}.md`, `technical-specs.md`, and `prd-validation.json` from Protocol 06 (transitively includes PROJECT-BRIEF.md from P03 and risk artifacts from P04)

### 1.2 Required Approvals
- **`[MUST]`** Product and engineering leadership approval to begin architecture design
- **`[MUST]`** Security/compliance stakeholder availability for design review

### 1.3 System State Requirements
- **`[MUST]`** Access to architecture templates (`.templates/architecture/`)
- **`[MUST]`** Diagram tooling (draw.io, Mermaid) or ASCII diagram capability
- **`[MUST]`** Automation scripts `plan_from_brief.py`, `validate_workflow_integration.py` available

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

**`[STRICT]` Role Definition:**
You are a **Solutions Architect**. Your mission is to transform the approved PRD and discovery evidence into a validated technical architecture package with explicit decisions, diagrams, and task-generation inputs.

**🚫 [CRITICAL] Directive:**
Do not introduce components or integrations that lack grounding in the brief or PRD; every element must trace to validated requirements.

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Source Validation & Context Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for input validation and context alignment -->

1. **`[MUST]` Verify Inputs and Versions:**
   * **Action:** Confirm that Project Brief, PRD, and discovery artifacts exist, match approved versions, and reflect latest sign-offs; record results in `source-alignment-report.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating brief and PRD alignment for architecture planning."
   * **Halt condition:** Stop if any artifact missing or outdated.
   * **Evidence:** `.artifacts/protocol-07/source-alignment-report.json`
   * **Validation:** All inputs verified and current

2. **`[MUST]` Consolidate Design Inputs:**
   * **Action:** Extract functional scope, non-functional requirements, constraints, and risks into `design-input-matrix.md`.
   * **Communication:** 
     > "Consolidating functional and non-functional requirements into design input matrix."
   * **Evidence:** `.artifacts/protocol-07/design-input-matrix.md`
   * **Validation:** Matrix complete with all requirements mapped

3. **`[GUIDELINE]` Map Key Assumptions:**
   * **Action:** Translate outstanding assumptions into design checkpoints for later validation; store in `design-assumptions.md`.
   * **Evidence:** `.artifacts/protocol-07/design-assumptions.md`
   * **Validation:** Assumptions documented with validation criteria

### STEP 2: Architecture Decomposition
<!-- [Category: EXECUTION-REASONING] -->
<!-- Why: Critical architectural decisions requiring documented rationale and alternatives -->

1. **`[MUST]` Identify System Boundaries:**
   * **Action:** Use `plan_from_brief.py` to derive domains, services, and integration surfaces; output to `architecture-boundaries.json`.
   * **Communication:** 
     > "[PHASE 2] - Mapping system boundaries and core components."
   
   **[REASONING]:**
   - **Premises:** System must align with PRD requirements and existing architecture principles
   - **Constraints:** Technology stack limitations, security boundaries, compliance requirements
   - **Alternatives Considered:**
     * **A)** Monolithic architecture - Rejected: Does not scale with PRD requirements
     * **B)** Microservices architecture - Selected: Aligns with scalability needs
     * **C)** Serverless architecture - Considered: May be used for specific components
   - **Decision:** Domain-driven design with clear bounded contexts
   - **Evidence:** Architecture principles from Protocol 05, PRD technical requirements
   - **Risks & Mitigations:**
     * **Risk:** Service boundary complexity → **Mitigation:** Clear interface contracts
     * **Risk:** Integration overhead → **Mitigation:** API gateway pattern
   - **Acceptance Link:** PRD technical specifications section
   
   * **Evidence:** `.artifacts/protocol-07/architecture-boundaries.json`
   * **Validation:** All system boundaries identified and documented

2. **`[MUST]` Capture Architecture Decisions:**
   * **Action:** Create Architecture Decision Records (ADRs) for key choices, including rationale, constraints, and alternatives; compile in `architecture-decisions.md`.
   * **Communication:** 
     > "Documenting architecture decisions with traceable rationale."
   
   **[REASONING]:**
   - **Premises:** Every architectural choice must be justified and reversible
   - **Constraints:** Time constraints, team expertise, existing infrastructure
   - **Decision Documentation:** Each ADR includes context, decision, consequences, and alternatives
   - **Evidence:** Industry best practices, team retrospectives
   - **Acceptance Link:** Architecture governance standards
   
   * **Evidence:** `.artifacts/protocol-07/architecture-decisions.md`
   * **Validation:** All major decisions have complete ADRs

3. **`[GUIDELINE]` Produce Interaction Diagrams:**
   * **Action:** Generate sequence/data flow diagram showing critical interactions; save as `interaction-diagram.drawio` or `interaction-diagram.md`.
   * **Evidence:** `.artifacts/protocol-07/interaction-diagram.drawio` or `.artifacts/protocol-07/interaction-diagram.md`
   * **Validation:** Diagrams cover all critical workflows

### STEP 3: Specification Packaging & Validation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward document assembly and validation execution -->

1. **`[MUST]` Assemble Technical Design Document:**
   * **Action:** Compile inputs, boundaries, ADRs, data contracts, security notes, and operational considerations into `TECHNICAL-DESIGN.md`.
   * **Communication:** 
     > "[PHASE 3] - Assembling comprehensive technical design specification."
   * **Evidence:** `.artifacts/protocol-07/TECHNICAL-DESIGN.md`
   * **Validation:** Document contains all required sections

2. **`[MUST]` Validate Compliance and Feasibility:**
   * **Action:** Run `python scripts/validate_workflow_integration.py --design .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-validation-report.json` covering security, integration, and performance constraints.
   * **Communication:** 
     > "Design validation status: {status}; review report for details."
   * **Evidence:** `.artifacts/protocol-07/design-validation-report.json`
   * **Validation:** All validation checks pass

3. **`[GUIDELINE]` Draft Implementation Roadmap:**
   * **Action:** Outline epics/modules, sequencing, and readiness criteria in `implementation-roadmap.md`.
   * **Evidence:** `.artifacts/protocol-07/implementation-roadmap.md`
   * **Validation:** Roadmap aligns with project timeline

### STEP 4: Approval & Handoff Preparation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple approval workflow and handoff preparation steps -->

1. **`[MUST]` Conduct Stakeholder Review:**
   * **Action:** Present design summary, diagram, and decisions; log approvals in `design-approval-record.json` with timestamps and approvers.
   * **Communication:** 
     > "[PHASE 4] - Requesting stakeholder approval for technical design."
   * **Halt condition:** Do not continue without recorded approval or documented waiver.
   * **Evidence:** `.artifacts/protocol-07/design-approval-record.json`
   * **Validation:** All required approvals obtained

2. **`[MUST]` Generate Task Inputs:**
   * **Action:** Export component responsibilities, interfaces, and dependencies into `task-generation-input.json` for Protocol 08.
   * **Evidence:** `.artifacts/protocol-07/task-generation-input.json`
   * **Validation:** Task inputs complete and structured

3. **`[GUIDELINE]` Archive Artifacts:**
   * **Action:** Produce `design-artifact-manifest.json` listing all diagrams, ADRs, validation reports, and locations.
   * **Evidence:** `.artifacts/protocol-07/design-artifact-manifest.json`
   * **Validation:** Manifest includes all generated artifacts

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
- **Protocol 03:** `PROJECT-BRIEF.md`, `project-brief-validation-report.json`, `BRIEF-APPROVAL-RECORD.json` - Strategic alignment.
- **Protocol 06:** `prd-{feature}.md`, `technical-specs.md`, `prd-validation.json` - Detailed functional/technical requirements.
- **Protocol 04-CD:** `risk-register.md`, `assumptions-v1.md` - Risk and assumption context.

### 5.2 Outputs To:
- **Protocol 08:** `task-generation-input.json`, `TECHNICAL-DESIGN.md`, `implementation-roadmap.md` - Task planning data.
- **Protocol 09:** `design-validation-report.json`, `architecture-boundaries.json` - Environment setup dependencies.

### 5.3 Artifact Storage Locations:
- **Primary Evidence:** `.artifacts/protocol-07/` - Primary evidence storage
- **Context Repository:** `.cursor/context-kit/` - Context and configuration artifacts

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting validation standards and criteria -->

### Gate 1: Source Alignment Gate
- **`[STRICT]` Criteria:** Project Brief and PRD validated, discovery risks acknowledged, design input matrix complete.
- **Evidence:** `source-alignment-report.json`, `design-input-matrix.md`
- **Pass Threshold:** Validation status `pass`, no missing artifacts.
- **Failure Handling:** Obtain updated inputs, refresh reports, rerun validation.
- **Automation:** `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-07/source-alignment-report.json`

### Gate 2: Architecture Integrity Gate
- **`[STRICT]` Criteria:** Boundaries defined, ADRs documented, interaction diagrams generated.
- **Evidence:** `architecture-boundaries.json`, `architecture-decisions.md`, `interaction-diagram.*`
- **Pass Threshold:** All core components mapped with traceable decisions.
- **Failure Handling:** Reassess decomposition, update ADRs, rerun gate.
- **Automation:** `python scripts/plan_from_brief.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-07/architecture-boundaries.json`

### Gate 3: Design Validation Gate
- **`[STRICT]` Criteria:** Compliance validation passes with no critical issues, risks mitigated, assumptions addressed.
- **Evidence:** `design-validation-report.json`, `design-assumptions.md`
- **Pass Threshold:** Validation script returns `pass` and all critical risks mitigated.
- **Failure Handling:** Update design, adjust ADRs, rerun validation script.
- **Automation:** `python scripts/validate_workflow_integration.py --design .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-validation-report.json`

### Gate 4: Approval & Handoff Gate
- **`[STRICT]` Criteria:** Stakeholder approvals logged, task-generation input produced, artifact manifest created.
- **Evidence:** `design-approval-record.json`, `task-generation-input.json`, `design-artifact-manifest.json`
- **Pass Threshold:** Approval status `approved`, outputs delivered to downstream protocols.
- **Failure Handling:** Follow up for approval, document waivers, ensure outputs regenerated.
- **Automation:** `python scripts/validate_design_handoff.py --input .artifacts/protocol-07/task-generation-input.json`

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### 7.1 Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating PRD and discovery inputs for architecture design."
[MASTER RAY™ | PHASE 2 START] - "Decomposing system boundaries and documenting decisions."
[MASTER RAY™ | PHASE 3 START] - "Compiling technical design and running validation checks."
[MASTER RAY™ | PHASE 4 START] - "Seeking stakeholder approval and packaging task inputs."
[PHASE COMPLETE] - "Technical design approved; artifacts archived in .artifacts/protocol-07/."
[RAY ERROR] - "Issue encountered during [phase]; see corresponding report for details."
```

### 7.2 Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Technical design package ready. Evidence includes:
> - source-alignment-report.json
> - architecture-decisions.md
> - design-validation-report.json
> - task-generation-input.json
>
> Confirm readiness to initiate Protocol 08: Generate Tasks."
```

### 7.3 Error Handling:
```
[RAY GATE FAILED: Design Validation Gate]
> "Quality gate 'Design Validation' failed.
> Criteria: Compliance validation must pass with no critical issues.
> Actual: Security review flagged unauthenticated webhook integration.
> Required action: Update TECHNICAL-DESIGN.md with auth flow, rerun validation.
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
   * **Command:** `python scripts/validate_prerequisites_6.py`
   * **Evidence:** Script execution log
   * **Validation:** All prerequisites met

2. **`[MUST]` Quality Gate Automation:**
   * **Action:** Execute quality gate validation scripts
   * **Commands:**
     - `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-07/source-alignment-report.json`
     - `python scripts/plan_from_brief.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-07/architecture-boundaries.json`
     - `python scripts/validate_workflow_integration.py --design .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-validation-report.json`
     - `python scripts/validate_design_handoff.py --input .artifacts/protocol-07/task-generation-input.json`
   * **Evidence:** Validation reports
   * **Validation:** All gates pass or have waivers

3. **`[MUST]` Evidence Aggregation:**
   * **Action:** Aggregate all protocol evidence
   * **Command:** `python scripts/aggregate_evidence_6.py --output .artifacts/protocol-07/`
   * **Evidence:** Aggregated evidence report
   * **Validation:** All evidence artifacts present

### 8.2 CI/CD Integration:
```yaml
name: Protocol 07 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 07 Gates
        run: python scripts/run_protocol_6_gates.py
```

### 8.3 Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct architecture review meeting; record minutes in `manual-design-review.md`.
2. Perform manual compliance checklist; store results in `.artifacts/protocol-07/manual-compliance-checklist.md`.
3. Document manual validation evidence in `.artifacts/protocol-07/manual-validation-log.md`.

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

### 9.3 Handoff to Protocol 08:

**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 08: Technical Task Generation

**Evidence Package:**
- `TECHNICAL-DESIGN.md` - Comprehensive architecture guide
- `task-generation-input.json` - Structured input for task generation automation

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/08-generate-tasks.md
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
| `source-alignment-report.json` | `.artifacts/protocol-07/` | Input verification evidence | Protocol 08 |
| `architecture-boundaries.json` | `.artifacts/protocol-07/` | Component & boundary mapping | Protocols 2 & 7 |
| `architecture-decisions.md` | `.artifacts/protocol-07/` | Decision rationale log | Protocol 08 |
| `TECHNICAL-DESIGN.md` | `.artifacts/protocol-07/` | Master technical spec | Protocols 2 & 7 |
| `design-validation-report.json` | `.artifacts/protocol-07/` | Compliance validation proof | Protocol 09 |
| `task-generation-input.json` | `.artifacts/protocol-07/` | Task generation dataset | Protocol 08 |

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
