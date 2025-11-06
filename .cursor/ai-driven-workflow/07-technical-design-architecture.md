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
**Type:** Prerequisite  
**Purpose:** Verify upstream discovery assets align with design scope before architecture work begins.

**Pass Criteria:**
- **Threshold:** Validation coverage score ≥95% and discovery risk acknowledgment ratio ≥90% complete.  
- **Threshold:** Alignment evidence freshness metric ≥0.9 across all inputs.  
- **Boolean Check:** Project brief status equals `approved` and design input matrix flag set to `ready`.  
- **Boolean Check:** Source alignment status reports `pass` for every discovery artifact with no `fail` entries.  
- **Metrics:** Coverage metrics, dependency completeness metrics, and risk mitigation metrics captured in alignment report.  
- **Evidence Link:** Evidence recorded in `.artifacts/protocol-07/source-alignment-report.json` and `.artifacts/protocol-07/design-input-matrix.md`.

**Automation:**
- Script: `python3 scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-07/source-alignment-report.json`
- Script: `python3 scripts/generate_design_inputs.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-07/design-input-matrix.md`
- Script: `python3 scripts/aggregate_evidence_6.py --output .artifacts/protocol-07/source-alignment-evidence.json`
- CI/CD Integration: Runs in workflow `protocol-07-alignment.yml` on push events with automated evidence upload.

**Failure Handling:**
- **Rollback:** Reopen discovery session and regenerate validated inputs before resuming design.
- **Notification:** Notify solution architect and protocol owner via Slack when coverage drops below threshold.
- **Waiver:** Document waiver in `.artifacts/protocol-07/gate-waivers.json` with executive sponsor approval if upstream artifacts delayed.

### Gate 2: Architecture Integrity Gate
**Type:** Execution  
**Purpose:** Ensure architecture decisions, boundaries, and diagrams remain internally consistent.

**Pass Criteria:**
- **Threshold:** Component boundary completeness ≥92% and ADR decision confidence ≥0.9.  
- **Threshold:** Interface coverage metric ≥90% for cross-domain interactions.  
- **Boolean Check:** Architecture decision records include `signed_off = true` and interaction diagrams present.  
- **Boolean Check:** Trace validation flags `pass` for boundaries with zero `fail` interactions.  
- **Metrics:** Boundary coverage metrics, decision trace metrics, and integration complexity metrics tracked per component.  
- **Evidence Link:** Evidence stored in `.artifacts/protocol-07/architecture-boundaries.json`, `.artifacts/protocol-07/architecture-decisions.md`, and `.artifacts/protocol-07/interaction-diagram.drawio`.

**Automation:**
- Script: `python3 scripts/plan_from_brief.py --brief PROJECT-BRIEF.md --output .artifacts/protocol-07/architecture-boundaries.json`
- Script: `python3 scripts/render_architecture_diagrams.py --input .artifacts/protocol-07/architecture-boundaries.json --output .artifacts/protocol-07/interaction-diagram.drawio`
- Script: `python3 scripts/verify_architecture_trace.py --input .artifacts/protocol-07/architecture-decisions.md`
- Config: `config/protocol_gates/07.yaml` defines structural thresholds applied in CI/CD workflow.

**Failure Handling:**
- **Rollback:** Re-run decomposition workshop, update ADRs, and regenerate diagrams before retrying gate.  
- **Notification:** Alert technical design lead via email and incident channel when boolean checks fail.  
- **Waiver:** Waivers permitted only with CTO sign-off; log justification in `gate-waivers.json`.

### Gate 3: Design Validation Gate
**Type:** Execution  
**Purpose:** Validate technical design against compliance, risk, and integration readiness requirements.

**Pass Criteria:**
- **Threshold:** Validation engine score ≥0.93 and critical risk count ≤0.  
- **Threshold:** Control coverage metric ≥0.9 across compliance categories.  
- **Boolean Check:** Risk register marked `cleared` and mitigation summary appended.  
- **Boolean Check:** Control validation flag equals `pass` with no `fail` exceptions logged.  
- **Metrics:** Compliance metrics, validation coverage metrics, and residual risk metrics summarized in validation report.  
- **Evidence Link:** Evidence captured in `.artifacts/protocol-07/design-validation-report.json` and `.artifacts/protocol-07/design-assumptions.md`.

**Automation:**
- Script: `python3 scripts/validate_workflow_integration.py --design .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-validation-report.json`
- Script: `python3 scripts/assess_design_risk.py --input .artifacts/protocol-07/TECHNICAL-DESIGN.md --output .artifacts/protocol-07/design-assumptions.md`
- Script: `python3 scripts/validate_design_controls.py --input .artifacts/protocol-07/design-validation-report.json`
- CI/CD Integration: Validation job `protocol-07-validate` runs nightly with metrics export to governance dashboard.

**Failure Handling:**
- **Rollback:** Reopen design review, adjust architecture components, and re-run validation scripts.  
- **Notification:** Notify compliance reviewer and risk owner when residual risk metric exceeds tolerance.  
- **Waiver:** Document not-applicable mitigations with root-cause analysis; approval required from governance board.

### Gate 4: Approval & Handoff Gate
**Type:** Completion  
**Purpose:** Confirm stakeholder approvals and ensure downstream assets are packaged for Protocol 08.

**Pass Criteria:**
- **Threshold:** Handoff readiness score ≥0.96 and artifact manifest completeness ≥100%.  
- **Threshold:** Evidence bundle checksum confidence ≥0.98 prior to release.  
- **Boolean Check:** Approval records marked `approved` and downstream payload published.  
- **Boolean Check:** Manifest verification flag reports `pass` with zero `fail` entries before release.  
- **Metrics:** Readiness metrics, approval latency metrics, and artifact accuracy metrics tracked in handoff manifest.  
- **Evidence Link:** Evidence maintained in `.artifacts/protocol-07/design-approval-record.json`, `.artifacts/protocol-07/task-generation-input.json`, and `.artifacts/protocol-07/design-artifact-manifest.json`.

**Automation:**
- Script: `python3 scripts/validate_design_handoff.py --input .artifacts/protocol-07/task-generation-input.json`
- Script: `python3 scripts/aggregate_evidence_6.py --output .artifacts/protocol-07/design-artifact-manifest.json`
- Script: `python3 scripts/package_design_bundle.py --output .artifacts/protocol-07/handoff/design-evidence-bundle.zip`
- CI/CD Integration: Handoff workflow posts to governance channel with evidence summary attachment and checksum check.

**Failure Handling:**
- **Rollback:** Revert to remediation checklist, regenerate missing artifacts, and obtain new approvals.  
- **Notification:** Notify Protocol 08 owner and project manager if approval boolean check fails.  
- **Waiver:** No waiver allowed; approval gate mandatory for downstream execution.

### Compliance Integration
- **Industry Standards:** Documentation adheres to CommonMark Markdown, JSON Schema Draft 2020-12, and BPMN diagram guidelines.  
- **Security Requirements:** Architecture decisions reference SOC 2 controls, design validation enforces GDPR data boundaries, and evidence storage inherits least-privilege permissions.  
- **Regulatory Compliance:** Risk assessments align with FTC software transparency guidance and HIPAA safeguards where applicable.  
- **Governance:** Thresholds and metrics sourced from `config/protocol_gates/07.yaml`, synchronized with the protocol governance registry.

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

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| source-alignment artifact (`source-alignment-report.json`) | Coverage metric ≥95%, validation metric `pass` | `.artifacts/protocol-07/source-alignment-report.json` | Gate 1 evidence summary |
| design-input artifact (`design-input-matrix.md`) | Readiness metric 100%, dependency metric complete | `.artifacts/protocol-07/design-input-matrix.md` | Gate 1 evidence log |
| architecture-boundaries artifact (`architecture-boundaries.json`) | Boundary coverage metric ≥92%, complexity metric tracked | `.artifacts/protocol-07/architecture-boundaries.json` | Gate 2 evidence bundle |
| architecture-decisions artifact (`architecture-decisions.md`) | Decision confidence metric ≥0.9, audit metric recorded | `.artifacts/protocol-07/architecture-decisions.md` | Gate 2 evidence narrative |
| design-validation artifact (`design-validation-report.json`) | Validation score metric ≥0.93, risk metric ≤0 | `.artifacts/protocol-07/design-validation-report.json` | Gate 3 evidence package |
| design-assumptions artifact (`design-assumptions.md`) | Mitigation metric complete, residual risk metric documented | `.artifacts/protocol-07/design-assumptions.md` | Gate 3 evidence log |
| design-approval artifact (`design-approval-record.json`) | Approval metric 100%, latency metric <24h | `.artifacts/protocol-07/design-approval-record.json` | Gate 4 evidence record |
| task-generation artifact (`task-generation-input.json`) | Handoff readiness metric ≥0.96, artifact completeness metric 100% | `.artifacts/protocol-07/task-generation-input.json` | Gate 4 evidence payload |
| design-manifest artifact (`design-artifact-manifest.json`) | Manifest coverage metric 100%, checksum metric verified | `.artifacts/protocol-07/design-artifact-manifest.json` | Gate 4 evidence manifest |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-07/`  
- **Subdirectories:** `diagrams/` for rendered visuals, `handoff/` for downstream packages, `logs/` for validation exports.  
- **Permissions:** Read/write access for protocol executor, read-only access for downstream protocols and governance auditors.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `design-approval-record.json`, `interaction-diagram.drawio`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-07/design-artifact-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).
- Artifact checksums: SHA-256 hash recorded for every artifact in the table.  
- Size: File size in bytes captured for audit.  
- Dependencies: List upstream sources (`PROJECT-BRIEF.md`, `TECHNICAL-DESIGN.md`) and downstream consumers (`task-generation-input.json`).

**Dependency Tracking:**
- Input: Project brief package, validated PRD set, discovery risk log.  
- Output: All artifacts listed in Artifact Generation Table, including handoff manifest.  
- Transformations: Discovery inputs → Alignment reports → Architecture decomposition → Validation outputs → Downstream handoff package.

**Coverage:** 100% of required artifacts documented in manifest with checksum and dependency references.

### Traceability

**Input Sources:**
- **Input From:** Protocol 06 `prd-core.md` – Baseline requirements and acceptance criteria.  
- **Input From:** Protocol 05 `rule-audit-final.md` – Governance constraints and reusable rule inventory.  
- **Input From:** Stakeholder interviews log – Architectural boundary clarifications and risk discussions.

**Output Artifacts:**
- **Output To:** `architecture-boundaries.json` – Boundary map consumed by downstream task generation.  
- **Output To:** `design-validation-report.json` – Evidence for compliance and environment readiness review.  
- **Output To:** `task-generation-input.json` – Structured payload for Protocol 08 automation.  
- **Output To:** `design-approval-record.json` – Approval ledger for governance board.  
- **Output To:** `design-artifact-manifest.json` – Complete inventory for archival and validation.

**Transformation Steps:**
1. Discovery artifacts → Source alignment → Alignment report and design input matrix.  
2. Alignment output → Architecture decomposition → Boundaries, ADRs, and diagrams.  
3. Architecture assets → Validation pipeline → Validation report and assumptions log.  
4. Validated design → Approval workflow → Approval record and downstream handoff package.  
5. Handoff assets → Manifest generator → Final manifest and archival bundle.

**Audit Trail:**
- Every transformation logged in manifest with timestamp and checksum.  
- Validation pipeline exports residual risk metrics for governance review.  
- Dependencies stored in manifest to support forward and backward traceability.  
- Evidence references cross-linked in gate reports for rapid audits.

### Archival Strategy

**Compression:**
- Artifacts compressed into `.artifacts/protocol-07/evidence-bundle.zip` after approval, using ZIP standard compression.

**Retention Policy:**
- Active artifacts retained for 120 days post-protocol completion.  
- Archived bundles retained for 3 years after project closure.  
- Cleanup job `scripts/cleanup_artifacts.py` runs quarterly to enforce retention policy.

**Retrieval Procedures:**
- Active artifacts accessed directly from `.artifacts/protocol-07/` with read-only mounts.  
- Archived bundles retrieved via `unzip .artifacts/protocol-07/evidence-bundle.zip` with checksum verification.  
- Integrity verified against SHA-256 values stored in manifest and validation report.

**Cleanup Process:**
- Quarterly automation logs actions to `.artifacts/protocol-07/cleanup-log.json`.  
- Critical artifacts flagged for extended retention require architect approval before deletion.  
- Manual recovery instructions stored in `handoff/recovery-playbook.md` for incident response.

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
