---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 06: IMPLEMENTATION-READY PRD CREATION v1.0.0 (PLANNING COMPLIANT) - Product Management & Documentation

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 06
- **Protocol Name:** IMPLEMENTATION-READY PRD CREATION (PLANNING COMPLIANT)
- **Protocol Owner:** Product Manager
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-01
- **Last Updated:** 2025-11-06
- **Version:** v1.0.0

### Protocol Classification
- **Category:** Documentation
- **Criticality:** High
- **Complexity:** High
- **Scope:** Module - Creates comprehensive PRD for development teams
- **Phase:** Phase 1-2 (Planning & Design)

### Protocol Lineage
- **Predecessor:** Protocol 05
- **Successor:** Protocol 07
- **Related Protocols:** [List related protocols]

### Protocol Metadata
- **Purpose:** Create detailed Product Requirements Document with implementation-ready specifications
- **Success Criteria:** All quality gates pass, artifacts complete for next protocol
- **Failure Modes:** [List potential failure modes]
- **Recovery Procedure:** [Define recovery steps]
- **Domain Expertise:** Product Management, Technical Documentation, Stakeholder Communication

---
## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** Product Manager
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** Can make decisions on protocol execution and quality gates
- **Escalation:** Technical Lead or Project Manager

#### Protocol Owner
- **Role:** Product Manager
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** Can make decisions on protocol execution and quality gates

#### Downstream Owner
- **Role:** Protocol 07 Owner
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
**Purpose:** Execute IMPLEMENTATION-READY PRD CREATION workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `architecture-principles.md` from Protocol 05 (transitively includes PROJECT-BRIEF.md from P03 and discovery artifacts from P04)

### 1.2 Required Approvals
- **`[MUST]`** Product owner authorization to begin PRD drafting
- **`[MUST]`** Technical lead confirmation of architectural constraints

### 1.3 System State Requirements
- **`[MUST]`** Access to PRD templates in `.templates/prd/`
- **`[MUST]`** Availability of automation scripts `generate_prd_assets.py` and `validate_prd_gate.py`

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

### Role Activation
When this protocol is triggered, **you are a Product Manager** with deep domain expertise in product management and technical documentation. **You are a** strategic product leader who transforms business requirements into implementation-ready specifications.

### Mission Statement
Your mission is to convert validated discovery inputs into an implementation-ready Product Requirements Document (PRD) that fully specifies scope, user experience, data, and integration requirements for engineering execution, providing measurable value and impact to clients through evidence-based product planning.

### Success Criteria for Mission
- **PRD completeness validated** with all sections documented
- **Stakeholder approval recorded** with formal sign-off documentation  
- **Implementation requirements specified** with technical clarity
- **Quality gates passed** for documentation standards

### Value Proposition
Deliver comprehensive PRD that bridges business requirements with technical implementation, ensuring engineering teams have clear specifications for successful product development and client value delivery.

### Critical Constraints
- **[STRICT]** Do not write production code or modify repositories; deliver documentation only
- **[GUIDELINE]** Ensure all requirements are implementation-ready
- **[STRICT]** Obtain stakeholder approval before completion

### Behavioral Traits
- **Strategic Thinking**: Break down complex business requirements into structured specifications
- **Evidence-Based Approach**: Base all requirements on validated discovery inputs and governance standards
- **Stakeholder Empathy**: Translate business needs into clear technical specifications
- **Systematic Rigor**: Apply structured methodology to requirement documentation

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Context Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for feature intent and architectural mapping -->

**Reasoning Pattern:** Align-before-elaborate heuristic — systematically validate feature intent and architectural placement before elaborating requirements. This prevents wasted effort on requirements that don't align with architectural constraints.

**Pattern Improvement:** Track alignment failures to identify common gaps between feature intent and architectural constraints. Refine layer detection logic based on execution feedback. Iteratively improve architectural mapping templates.

**Example Scenario:** When confirming feature intent, determine if effort is net-new feature or modification. If intent unclear, halt and request stakeholder clarification. Then map feature to architectural layer (frontend, backend, data pipeline) using discovery inputs and architecture principles. Therefore, requirements elaboration proceeds with validated architectural context, preventing downstream rework.

**Strategy Rationale:** Because PRD serves as implementation contract between product and engineering, ensuring alignment with architectural constraints before requirements elaboration prevents engineering conflicts. This systematic alignment reduces PRD rework and accelerates implementation.

**User Interaction**: "Please confirm the feature intent and architectural placement. Does this align with your technical vision?"

**Meta-Cognitive Check:** Before confirming feature intent, assess your own limitations:
- **Awareness:** Recognize that feature intent may be ambiguous or conflicting, requiring stakeholder clarification
- **Limitations:** Understand that architectural layer detection may require technical lead validation if constraints are unclear
- **Capacity:** Acknowledge that context alignment may require multiple stakeholder consultations, delaying requirements elaboration
- **Correction:** Be prepared to escalate unclear intent to product owner or technical lead for resolution

**Decision Tree:** When aligning context:
- **IF** feature intent is clear (net-new or modification) → Proceed to architectural mapping
- **ELSE IF** feature intent is ambiguous → Halt and request stakeholder clarification, document in `prd-context.json`
- **IF** architectural layer detected and technical lead approved → Proceed to requirements elaboration
- **IF** layer detection unclear → Document constraints and request technical lead validation
- **THEN** Capture stakeholder goals aligned with project brief

1. **`[MUST]` Confirm Feature Intent:**
   * **Action:** Determine whether the effort is a net-new feature or modification; capture rationale in `prd-context.json`.
   * **Reasoning:** Apply align-before-elaborate pattern — validate feature intent before proceeding to requirements elaboration. Use decision tree above to determine next steps based on intent clarity.
   * **Problem-Solving:** If intent is unclear:
  1. **Root Cause:** Identify why intent is ambiguous (stakeholder communication gap, incomplete discovery, or scope change)
  2. **Solution:** Document ambiguity in `prd-context.json` and request clarification from product owner. If clarification delayed, mark as `REQUIRES_INPUT` and proceed with architecture mapping tentatively
  3. **Validation:** Verify stakeholder confirmation recorded in JSON file before proceeding
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating feature intent and architectural placement."
   * **Halt condition:** Await stakeholder clarification if intent unclear.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-context.json`
   * **Validation:** Stakeholder confirmation recorded in JSON file

2. **`[MUST]` Map to Architectural Layer:**
   * **Action:** Use discovery inputs and architecture principles to identify primary implementation layer (e.g., frontend, backend, data pipeline) and announce detected layer.
   * **Reasoning:** Use architectural layer detection pattern — systematically map feature to implementation layer using discovery inputs and architecture principles. This ensures requirements elaboration aligns with architectural constraints.
   * **Decision Criteria:** When mapping to layer:
  - **IF** feature primarily affects user interface → Map to frontend layer
  - **ELSE IF** feature primarily affects business logic/APIs → Map to backend layer
  - **IF** feature primarily affects data processing → Map to data pipeline layer
  - **IF** feature spans multiple layers → Document primary layer and secondary dependencies
   * **Communication:** 
     > "Detected primary implementation layer: [layer]. Constraints: [communication, technology, governance]."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/layer-detection.md`
   * **Validation:** Layer detection approved by technical lead

3. **`[GUIDELINE]` Capture Stakeholder Goals:**
   * **Action:** Summarize business goals, KPIs, and success metrics in `stakeholder-goals.md` for quick reference.
   * **Reasoning:** Apply goals distillation pattern — extract key stakeholder goals from discovery inputs into concise reference document. This enables quick context retrieval during requirements elaboration.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/stakeholder-goals.md`
   * **Validation:** Goals aligned with project brief

### STEP 2: Requirements Elaboration
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward requirements gathering and documentation -->

**Reasoning Pattern:** Elaborate-with-validation strategy — systematically gather user narratives, functional requirements, and technical specs while validating completeness and alignment with architectural constraints. This ensures implementation-ready PRD that engineering can execute without ambiguity.

**Example Scenario:** When gathering user narratives, elicit user stories aligned with detected architectural layer. If frontend layer detected, focus on UI/UX stories; if backend layer, focus on API and business logic stories. Then define functional requirements with acceptance criteria and specify technical requirements with API contracts. Therefore, PRD contains complete, actionable requirements aligned with architecture.

**Strategy Rationale:** Because PRD serves as implementation contract, ensuring requirements are complete and aligned with architecture prevents engineering rework. This systematic elaboration ensures all requirements are actionable and traceable to user needs.

**Decision Tree:** When elaborating requirements:
- **IF** user stories gathered and personas covered → Proceed to functional requirements
- **ELSE IF** user stories incomplete → Request additional user input or document assumptions
- **IF** functional requirements defined with acceptance criteria → Proceed to technical requirements
- **IF** technical requirements specified with API contracts → Proceed to risk planning
- **THEN** Validate all requirements align with architectural layer and stakeholder goals

1. **`[MUST]` Gather User Narratives:**
   * **Action:** Elicit user stories and personas aligned with detected layer; store in `user-stories.md`.
   * **Reasoning:** Apply user-centric elaboration pattern — gather user stories aligned with architectural layer. This ensures requirements reflect user needs while respecting architectural constraints.
   * **Problem-Solving:** If user stories incomplete:
  1. **Root Cause:** Identify why stories are incomplete (user unavailability, persona gaps, or layer misalignment)
  2. **Solution:** Document incomplete stories with assumptions, request user interviews, or refine personas based on discovery inputs
  3. **Validation:** Verify user stories cover all identified personas before proceeding
   * **Communication:** 
     > "[PHASE 2] - Capturing user stories and personas for PRD foundation."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/user-stories.md`
   * **Validation:** User stories cover all identified personas

2. **`[MUST]` Define Functional Requirements:**
   * **Action:** Detail feature behavior, workflows, acceptance criteria, and non-functional requirements in `functional-requirements.md`.
   * **Reasoning:** Use systematic functional specification pattern — detail feature behavior with acceptance criteria to ensure requirements are testable and complete. This enables validation that implementation meets requirements.
   * **Problem-Solving:** If functional requirements ambiguous:
  1. **Root Cause:** Identify why requirements are ambiguous (behavior undefined, acceptance criteria missing, or workflow incomplete)
  2. **Solution:** Elaborate ambiguous requirements with examples, refine acceptance criteria with measurable outcomes, or request stakeholder clarification
  3. **Validation:** Verify all features have acceptance criteria defined before proceeding
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/functional-requirements.md`
   * **Validation:** All features have acceptance criteria defined

3. **`[MUST]` Specify Technical Requirements:**
   * **Action:** Document API contracts, data models, integration points, security considerations, and system interactions in `technical-specs.md`.
   * **Reasoning:** Apply technical specification pattern — document technical interfaces and constraints to guide engineering implementation. Use root cause analysis to ensure technical requirements address underlying architectural constraints.
   * **Problem-Solving:** When specifying technical requirements:
  1. **Root Cause:** Identify underlying technical constraints (API limitations, data model constraints, or integration dependencies)
  2. **Solution:** Document technical requirements that address root constraints (e.g., "API must support pagination due to high data volume" addresses performance constraint)
  3. **Validation:** Verify technical requirements reviewed by architecture team before proceeding
   * **Communication:** 
     > "Documenting technical interfaces and constraints to guide engineering."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/technical-specs.md`
   * **Validation:** Technical requirements reviewed by architecture team

4. **`[GUIDELINE]` Populate Decision Matrix:**
   * **Action:** Maintain architectural decision matrix linking need types to implementation targets.
   * **Reasoning:** Use decision matrix pattern — systematically link user needs to implementation targets with constraints and notes. This enables traceability between requirements and implementation decisions.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/decision-matrix.md`
   
   **Example (DO):**
   ```markdown
   | Need | Target | Constraints | Notes |
   |------|--------|-------------|-------|
   | Analytics KPI export | Backend service | Must align with GDPR retention | Use existing data warehouse pipeline |
   ```

### STEP 3: Risk, Dependency, and Validation Planning
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple risk assessment and validation planning steps -->

**Reasoning Pattern:** Plan-before-assemble heuristic — systematically consolidate risks, define validation criteria, and align timeline before assembling PRD. This ensures PRD includes complete risk mitigation and validation planning.

**Example Scenario:** When consolidating risks, aggregate risks from discovery into risk log and include new risks identified during requirements elaboration. Then define acceptance tests and validation criteria that are measurable and achievable. Finally, align timeline with business objectives. Therefore, PRD assembly includes complete risk and validation planning, enabling smooth implementation.

**Strategy Rationale:** Because PRD serves as implementation contract, including risk mitigation and validation planning ensures implementation addresses risks and validates success. This systematic planning prevents implementation surprises and ensures validation success.

**Decision Tree:** When planning risks and validation:
- **IF** risks consolidated with mitigation plans → Proceed to validation criteria definition
- **ELSE IF** high-severity risks lack mitigation → Document mitigation gaps and request stakeholder input
- **IF** validation criteria defined and measurable → Proceed to timeline alignment
- **IF** timeline aligns with business objectives → Proceed to PRD assembly
- **THEN** Verify all high-severity risks have mitigation plans

1. **`[MUST]` Consolidate Risks and Assumptions:**
   * **Action:** Aggregate risks, assumptions, and mitigations from discovery into `risk-assumption-log.md`; include new items identified during elaboration.
   * **Reasoning:** Apply risk consolidation pattern — systematically aggregate risks from discovery and requirements elaboration into unified risk log. Use root cause analysis to ensure mitigation strategies address underlying causes.
   * **Problem-Solving:** When consolidating risks:
  1. **Root Cause:** Identify underlying cause of each risk (e.g., "API rate limiting risk" → Root cause: "Third-party API has strict rate limits")
  2. **Solution:** Develop mitigation that addresses root cause (e.g., "Implement caching layer to reduce API calls")
  3. **Validation:** Verify all high-severity risks have mitigation plans before proceeding
   * **Communication:** 
     > "[PHASE 3] - Updating risk and assumption log for PRD readiness."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/risk-assumption-log.md`
   * **Validation:** All high-severity risks have mitigation plans

2. **`[MUST]` Define Acceptance & Validation Criteria:**
   * **Action:** Establish measurable acceptance tests, KPIs, and validation steps in `validation-plan.md`.
   * **Reasoning:** Use measurable validation pattern — establish acceptance tests and KPIs that are measurable and achievable. This enables validation that implementation meets requirements.
   * **Problem-Solving:** If validation criteria ambiguous:
  1. **Root Cause:** Identify why criteria are ambiguous (KPIs undefined, acceptance tests not measurable, or validation steps unclear)
  2. **Solution:** Define measurable KPIs (e.g., "API response time < 200ms"), create testable acceptance criteria (e.g., "User can complete checkout in < 2 minutes"), and specify validation steps
  3. **Validation:** Verify validation criteria are measurable and achievable before proceeding
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/validation-plan.md`
   * **Validation:** Validation criteria are measurable and achievable

3. **`[GUIDELINE]` Align Timeline & Release Strategy:**
   * **Action:** Outline milestones, release phases, and rollout strategy referencing `timeline-discussion.md`.
   * **Reasoning:** Apply timeline alignment pattern — align PRD timeline with business objectives and release strategy. This ensures PRD supports business goals and enables smooth rollout.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/timeline-discussion.md`
   * **Validation:** Timeline aligns with business objectives

### STEP 4: PRD Assembly and Automation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward document assembly and automation execution -->

**Reasoning Pattern:** Assemble-with-validation strategy — systematically compile PRD sections, generate assets, and validate quality before finalization. This ensures PRD is complete, traceable, and implementation-ready.

**Example Scenario:** When assembling PRD, compile context, requirements, risks, and validation sections into PRD document. Then run automation scripts to generate supporting artifacts (user stories, schemas, APIs). Finally, validate PRD quality with automation script. If validation fails, remediate and rerun. Therefore, PRD is complete, validated, and ready for engineering execution.

**Strategy Rationale:** Because PRD serves as implementation contract, ensuring PRD is complete and validated before handoff prevents engineering rework. This systematic assembly and validation ensures PRD quality and implementation readiness.

**Decision Tree:** When assembling PRD:
- **IF** all mandatory sections populated → Proceed to asset generation
- **ELSE IF** mandatory sections incomplete → Halt and request completion or document gaps
- **IF** assets generated successfully → Proceed to PRD validation
- **IF** PRD validation passes (score ≥ 85/100) → Proceed to traceability mapping
- **ELSE IF** validation fails → Remediate issues and rerun validation
- **THEN** Verify PRD contains all required sections and passes validation

1. **`[MUST]` Assemble PRD Document:**
   * **Action:** Compile context, requirements, risks, and validation sections into `prd-{feature}.md` following standard template.
   * **Reasoning:** Apply systematic assembly pattern — compile all PRD sections from validated inputs into unified document. Use decision tree above to determine when to proceed based on section completeness.
   * **Problem-Solving:** If mandatory sections incomplete:
  1. **Root Cause:** Identify why sections are incomplete (content missing, stakeholder input delayed, or template gaps)
  2. **Solution:** Document incomplete sections with placeholder text and follow-up plan, or request stakeholder completion before proceeding
  3. **Validation:** Verify PRD contains all required sections before proceeding
   * **Communication:** 
     > "[PHASE 4] - Assembling implementation-ready PRD."
   * **Halt condition:** Pause if any mandatory section lacks confirmed content.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-{feature}.md`
   * **Validation:** PRD contains all required sections

2. **`[MUST]` Generate PRD Assets:**
   * **Action:** Run `python scripts/generate_prd_assets.py --prd .artifacts/artisans-corner-dashboard/protocol-06/prd-{feature}.md --output .artifacts/artisans-corner-dashboard/protocol-06/prd-assets/` to create supporting artifacts (user stories, schemas, APIs).
   * **Reasoning:** Use automation pattern — generate supporting artifacts from PRD to enable engineering implementation. This automation reduces manual effort and ensures consistency.
   * **Problem-Solving:** If asset generation fails:
  1. **Root Cause:** Identify why generation failed (script error, PRD format issue, or missing dependencies)
  2. **Solution:** Fix script errors, correct PRD format, or install missing dependencies, then rerun generation
  3. **Validation:** Verify all asset files generated successfully before proceeding
   * **Communication:** 
     > "[RAY AUTOMATION] PRD assets generated and archived."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-assets/`
   * **Validation:** All asset files generated successfully

3. **`[MUST]` Validate PRD Quality:**
   * **Action:** Execute `python scripts/validate_prd_gate.py --prd .artifacts/artisans-corner-dashboard/protocol-06/prd-{feature}.md --output .artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json` ensuring completeness and alignment.
   * **Reasoning:** Apply validation-before-handoff pattern — validate PRD quality before proceeding to handoff. Use decision tree above to determine when to proceed based on validation results.
   * **Problem-Solving:** If validation fails:
  1. **Root Cause:** Identify why validation failed (completeness gaps, alignment issues, or quality threshold not met)
  2. **Solution:** Remediate validation failures (complete missing sections, fix alignment issues, or improve quality), then rerun validation
  3. **Validation:** Verify PRD validation score ≥ 85/100 before proceeding
   * **Communication:** 
     > "PRD validation status: {status} - Score: {score}/100."
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json`
   * **Validation:** PRD validation score ≥ 85/100

4. **`[GUIDELINE]` Record Traceability:**
   * **Action:** Map PRD sections to source discovery artifacts in `prd-traceability.json`.
   * **Reasoning:** Use traceability pattern — document source references for all PRD content to enable auditability and future updates. This ensures PRD remains synchronized with discovery evidence.
   * **Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-traceability.json`
   * **Validation:** All PRD content traceable to source artifacts

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
- **Protocol 03:** `PROJECT-BRIEF.md` - Strategic direction and approved scope.
- **Protocol 04-CD:** `discovery-brief.md`, `evidence-map.json`, `risk-register.md` - Discovery intelligence and risks.
- **Protocol 05:** `architecture-principles.md` - Governance constraints.

### 5.2 Outputs To:
- **Protocol 06:** `technical-specs.md`, `prd-traceability.json`, `prd-assets/technical-baseline.json` - Inputs for technical design.
- **Protocol 02:** `prd-{feature}.md`, `user-stories.md`, `validation-plan.md` - Task generation references.

### 5.3 Artifact Storage Locations:
- **Primary Evidence:** `.artifacts/artisans-corner-dashboard/protocol-06/` - Primary evidence storage
- **Context Repository:** `.cursor/context-kit/` - Context and configuration artifacts (summary pointers)

---

## 6. QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Context Alignment
**Type:** Prerequisite  
**Purpose:** Verify feature intent, architectural layer detection, and stakeholder goals before drafting detailed requirements.  
**Pass Criteria:**
- **Threshold:** Context alignment score ≥0.94; stakeholder alignment metric ≥90%.  
- **Boolean Check:** `stakeholder-goals.md` front matter `confirmation: true`.  
- **Metrics:** `prd-context.json` logs intent coverage metric, `layer-detection.md` records detection accuracy metric.  
- **Evidence Link:** `.artifacts/artisans-corner-dashboard/protocol-06/prd-context.json`, `.artifacts/artisans-corner-dashboard/protocol-06/layer-detection.md`, `.artifacts/artisans-corner-dashboard/protocol-06/stakeholder-goals.md`.  
**Automation:**
- Script: `python3 scripts/validate_prd_context.py --input .artifacts/artisans-corner-dashboard/protocol-06/prd-context.json --output .artifacts/artisans-corner-dashboard/protocol-06/context-validation.json`.  
- Script: `python3 scripts/validate_prerequisites_1.py --log .artifacts/artisans-corner-dashboard/protocol-06/prerequisites-log.json`.  
- CI Integration: Context validation stage runs via `real-validation-pipeline.yml` and posts metrics to validation summary.  
- Config: `config/protocol_gates/06.yaml` defines context score thresholds and stakeholder confirmation requirements.  
**Failure Handling:**
- **Rollback:** Re-engage stakeholders, update context artifacts, rerun validation scripts.  
- **Notification:** Alert product owner if context alignment score <0.94.  
- **Waiver:** Documented in `.artifacts/artisans-corner-dashboard/protocol-06/gate-waivers.json` with head of product approval when timeline-critical.

### Gate 2: Requirements Completeness
**Type:** Execution  
**Purpose:** Ensure requirements artifacts are comprehensive, traceable, and acceptance-ready.  
**Pass Criteria:**
- **Threshold:** Requirements coverage metric ≥95%; traceability completeness metric ≥0.92.  
- **Boolean Check:** `functional-requirements.md` metadata `status: complete`.  
- **Metrics:** `requirements-validation.json` records story coverage metric, acceptance criteria metric, dependency trace metric.  
- **Evidence Link:** `.artifacts/artisans-corner-dashboard/protocol-06/user-stories.md`, `.artifacts/artisans-corner-dashboard/protocol-06/functional-requirements.md`, `.artifacts/artisans-corner-dashboard/protocol-06/technical-specs.md`.  
**Automation:**
- Script: `python3 scripts/validate_prd_requirements.py --dir .artifacts/artisans-corner-dashboard/protocol-06/ --output .artifacts/artisans-corner-dashboard/protocol-06/requirements-validation.json`.  
- Script: `python3 scripts/traceability_matrix.py --input .artifacts/artisans-corner-dashboard/protocol-06/functional-requirements.md --output .artifacts/artisans-corner-dashboard/protocol-06/prd-traceability.json`.  
- CI Integration: Requirements validation job runs on `ubuntu-latest`, reporting metrics to `.artifacts/validation/protocol_quality_gates-summary.json`.  
- Config: `config/protocol_gates/06.yaml` captures coverage and traceability thresholds.  
**Failure Handling:**
- **Rollback:** Address requirement gaps, expand acceptance criteria, regenerate validation report before proceeding.  
- **Notification:** Notify engineering lead when coverage metric below threshold or traceability gaps detected.  
- **Waiver:** Not permitted; completeness mandatory.

### Gate 3: Validation Readiness
**Type:** Completion  
**Purpose:** Confirm risks, validation plan, and PRD assets meet readiness standards for downstream design and execution.  
**Pass Criteria:**
- **Threshold:** PRD validation score ≥0.88; risk mitigation coverage metric ≥90%; validation plan completeness metric ≥95%.  
- **Boolean Check:** `prd-validation.json` field `status: pass`.  
- **Metrics:** `prd-validation.json` captures scenario pass rate metric, risk closure metric; `validation-plan.md` includes test coverage metric.  
- **Evidence Link:** `.artifacts/artisans-corner-dashboard/protocol-06/risk-assumption-log.md`, `.artifacts/artisans-corner-dashboard/protocol-06/validation-plan.md`, `.artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json`.  
**Automation:**
- Script: `python3 scripts/validate_prd_gate.py --prd .artifacts/artisans-corner-dashboard/protocol-06/prd-{feature}.md --output .artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json`.  
- Script: `python3 scripts/aggregate_evidence_1.py --output .artifacts/artisans-corner-dashboard/protocol-06/ --protocol-id 06`.  
- CI Integration: Validation readiness stage integrated with pipeline to publish scores to governance dashboard.  
- Config: `config/protocol_gates/06.yaml` defines validation score thresholds and mitigation expectations.  
**Failure Handling:**
- **Rollback:** Update risk mitigations, expand validation scenarios, rerun automation until thresholds met.  
- **Notification:** Escalate to product and QA leads if validation score <0.88.  
- **Waiver:** Only allowed for pilot releases with CTO and QA signatures; log in `gate-waivers.json` with mitigation plan.

### Compliance Integration
- **Industry Standards:** CommonMark Markdown and JSON Schema for PRD artifacts, YAML for configuration descriptors.  
- **Security Requirements:** SOC2-aligned storage of PRD assets, GDPR-compliant handling of user data references, encrypted archives for validation logs.  
- **Regulatory Compliance:** FTC-aligned feature claims, ISO 9001 retention for validation evidence, accessibility compliance tracking via validation-plan.md.  
- **Governance:** Gate criteria driven by `config/protocol_gates/06.yaml`; automation telemetry stored in `.artifacts/validation/protocol_quality_gates-summary.json` and protocol governance dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### 7.1 Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Aligning feature intent and architectural placement for PRD."
[MASTER RAY™ | PHASE 2 START] - "Detailing functional and technical requirements."
[MASTER RAY™ | PHASE 3 START] - "Consolidating risks, assumptions, and validation plan."
[MASTER RAY™ | PHASE 4 START] - "Assembling PRD and running automation gates."
[PHASE COMPLETE] - "PRD approved; assets archived in .artifacts/artisans-corner-dashboard/protocol-06/."
[RAY ERROR] - "Issue during [phase]; refer to validation logs for remediation."
```

### 7.2 Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "PRD draft ready with validation evidence:
> - prd-context.json
> - functional-requirements.md
> - technical-specs.md
> - prd-validation.json
>
> Confirm readiness to proceed to Protocol 06: Technical Design & Architecture."
```

### 7.3 Error Handling:
```
[RAY GATE FAILED: Requirements Completeness Gate]
> "Quality gate 'Requirements Completeness' failed.
> Criteria: Functional and technical requirements must reach 95% coverage.
> Actual: Acceptance criteria missing for checkout workflow.
> Required action: Update functional-requirements.md, rerun validator.
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
   * **Command:** `python scripts/validate_prerequisites_1.py`
   * **Evidence:** Script execution log
   * **Validation:** All prerequisites met
   * **Exit Code Handling:** 
     - 0 = Success, continue to PRD creation
     - 1 = Error occurred, review logs and retry
     - 2 = Prerequisites missing, resolve before proceeding

2. **`[MUST]` Quality Gate Automation:**
   * **Action:** Execute quality gate validation scripts
   * **Commands:**
     - `python scripts/validate_prd_context.py --input .artifacts/artisans-corner-dashboard/protocol-06/prd-context.json --output .artifacts/artisans-corner-dashboard/protocol-06/context-validation.json`
     - `python scripts/validate_prd_requirements.py --dir .artifacts/artisans-corner-dashboard/protocol-06/ --output .artifacts/artisans-corner-dashboard/protocol-06/requirements-validation.json`
     - `python scripts/validate_prd_gate.py --prd .artifacts/artisans-corner-dashboard/protocol-06/prd-{feature}.md --output .artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json`
   * **Evidence:** Validation reports
   * **Exit Code Handling:** 
     - 0 = Success, continue to next step
     - 1 = Error occurred, review logs and retry
     - 2 = Validation failed, address issues and re-run
   * **Validation:** All gates pass or have waivers

3. **`[MUST]` Evidence Aggregation:**
   * **Action:** Aggregate all protocol evidence
   * **Command:** `python scripts/aggregate_evidence_1.py --output .artifacts/artisans-corner-dashboard/protocol-06/ --protocol-id 06`
   * **Evidence:** Aggregated evidence report
   * **Validation:** All evidence artifacts present
   * **Exit Code Handling:** 
     - 0 = Success, continue to handoff
     - 1 = Error occurred, review logs and retry
     - 2 = Missing evidence, address gaps and re-run

### User Interaction Prompts
- **Clarification needed**: "Please provide more details about the feature requirements"
- **Feedback requested**: "Do these user stories align with your expectations?"
- **Approval needed**: "Please confirm PRD completeness and approve for technical design"

### 8.2 CI/CD Integration:
```yaml
name: Protocol 06 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 06 Gates
        run: python scripts/run_protocol_1_gates.py
```

### 8.3 Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct PRD review workshop; capture minutes in `manual-prd-review.md`.
2. Obtain stakeholder sign-off via email; archive under `.artifacts/artisans-corner-dashboard/protocol-06/approvals/`.
3. Document manual validations in `.artifacts/artisans-corner-dashboard/protocol-06/manual-validation-log.md`.

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

### 9.3 Handoff to Protocol 07:

**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 07: Technical Design & Architecture

**Evidence Package:**
- `prd-{feature}.md` - Comprehensive PRD for design translation
- `technical-specs.md` - Detailed interfaces for architecture planning

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/07-technical-design-architecture.md
```

---

## 10. EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->

### 10.1 Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| prd-context.json | Context alignment metric ≥0.94, stakeholder alignment ≥90% | `.artifacts/artisans-corner-dashboard/protocol-06/prd-context.json` | Gate 1 context alignment |
| layer-detection.md | Detection accuracy metric ≥0.9, coverage metric documented | `.artifacts/artisans-corner-dashboard/protocol-06/layer-detection.md` | Gate 1 context alignment |
| stakeholder-goals.md | Stakeholder confirmation metric = true, goal coverage metric ≥95% | `.artifacts/artisans-corner-dashboard/protocol-06/stakeholder-goals.md` | Gate 1 context alignment |
| user-stories.md | Story coverage metric ≥95%, persona coverage metric recorded | `.artifacts/artisans-corner-dashboard/protocol-06/user-stories.md` | Gate 2 requirements completeness |
| functional-requirements.md | Acceptance criteria metric ≥95%, traceability metric ≥0.92 | `.artifacts/artisans-corner-dashboard/protocol-06/functional-requirements.md` | Gate 2 requirements completeness |
| technical-specs.md | Interface completeness metric ≥0.9, dependency metric documented | `.artifacts/artisans-corner-dashboard/protocol-06/technical-specs.md` | Gate 2 requirements completeness |
| prd-validation.json | Validation score ≥0.88, risk mitigation metric ≥90% | `.artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json` | Gate 3 validation readiness |
| validation-plan.md | Test coverage metric ≥95%, regression readiness metric recorded | `.artifacts/artisans-corner-dashboard/protocol-06/validation-plan.md` | Gate 3 validation readiness |
| evidence-manifest.json | Artifact count metric = 100%, checksum verification metric = pass | `.artifacts/artisans-corner-dashboard/protocol-06/evidence-manifest.json` | Aggregated evidence validator |

### 10.2 Storage Structure

**Protocol Directory:** `.artifacts/artisans-corner-dashboard/protocol-06/`  
- **Subdirectories:** `prd-assets/`, `logs/`, `approvals/`, optional `knowledge-base/`.  
- **Permissions:** Read/write for product owner and protocol executor; read-only for downstream protocols (07, 08) and governance reviewers.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `risk-assumption-log.md`, `requirements-validation.json`).

### 10.3 Manifest Completeness

**Manifest File:** `.artifacts/artisans-corner-dashboard/protocol-06/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash recorded for every artifact, report, and archive.  
- Size: File size in bytes listed for each artifact in manifest integrity block.  
- Dependencies: Upstream protocol references (03, 04, 05) and downstream consumers (07, 08) explicitly mapped.  

**Dependency Tracking:**
- Input: `PROJECT-BRIEF.md`, `bootstrap-manifest.json`, `architecture-principles.md`, market research briefs.  
- Output: All artifacts in table plus `requirements-validation.json`, `context-validation.json`, `prd-traceability.json`, and `prd-assets/technical-baseline.json`.  
- Transformations: Context alignment → requirements elaboration → validation readiness → evidence aggregation.  

**Coverage:** Manifest captures 100% of artifacts, automation outputs, and approvals with checksum verification and dependency linkage.

### 10.4 Traceability

**Input Sources:**
- **Input From:** `.cursor/context-kit/governance-status.md` – Governance constraints applied during PRD definition.  
- **Input From:** `.artifacts/artisans-corner-dashboard/protocol-05/architecture-principles.md` – Architectural guardrails shaping requirements.  

**Output Artifacts:**
- **Output To:** `technical-specs.md` – Consumed by Protocol 07 for design activities.  
- **Output To:** `prd-{feature}.md` – Reference for Protocol 02 task generation.  
- **Output To:** `prd-traceability.json` – Supports QA planning and audit reviews.  
- **Output To:** `risk-assumption-log.md` – Feeds risk management process in downstream protocols.  
- **Output To:** `evidence-manifest.json` – Audit ledger for governance.  

**Transformation Steps:**
1. Inputs → prd-context.json: Map strategy, stakeholders, and constraints.  
2. Context → user-stories.md / functional-requirements.md: Elaborate user journeys and system behaviors.  
3. Requirements → technical-specs.md: Translate behaviors into technical interfaces.  
4. Specs + risks → validation-plan.md / prd-validation.json: Define tests and validate readiness.  
5. Outputs → evidence-manifest.json: Aggregate artifacts, checksums, dependencies.  

**Audit Trail:**
- Manifest logs timestamps, checksum hashes, verification owners.  
- Automation logs appended to `.artifacts/artisans-corner-dashboard/protocol-06/logs/automation.log`.  
- Approvals stored in `.artifacts/artisans-corner-dashboard/protocol-06/approvals/` with signatures.  
- Cleanup actions recorded in `.artifacts/artisans-corner-dashboard/protocol-06/cleanup-log.json` for retention audits.

### 10.5 Archival Strategy

**Compression:**
- Artifacts archived into `.artifacts/artisans-corner-dashboard/protocol-06/archives/prd-bundle.zip` after Gate 3 passes.  
- Compression format: ZIP with AES-256 encryption for sensitive product data.  

**Retention Policy:**
- Active artifacts retained for 210 days post-launch or until superseded.  
- Archived bundles retained for 5 years in compliance with product governance policy.  
- Cleanup automation runs bi-annually; exceptions flagged for extended retention.  

**Retrieval Procedures:**
- Active artifacts accessed directly with manifest cross-check.  
- Archived bundles restored from `archives/` directory, integrity verified against manifest hashes.  
- Retrieval logged in `.artifacts/artisans-corner-dashboard/protocol-06/retention-approvals.json`.  

**Cleanup Process:**
- Bi-annual cleanup script updates `.artifacts/artisans-corner-dashboard/protocol-06/cleanup-log.json` with removed artifact list, sizes, and hashes.  
- Artifacts marked `extended_retention: true` persist until compliance officer approval.  
- Governance sign-off captured in retention approvals file.

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
| `generate_prd_assets.py` | PRD asset generation | `scripts/` | ✅ Exists |
| `validate_prd_gate.py` | PRD validation | `scripts/` | ✅ Exists |
| `aggregate_evidence_06.py` | Evidence aggregation | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** Architecture principles, discovery artifacts, project brief
- **Output:** PRD document, requirements matrix, validation reports
- **External Dependencies:** Python 3.8+, markdown processors

### Automation Hooks
- **Pre-execution:** Load architecture and discovery context
- **During execution:** Validate PRD structure and completeness
- **Post-execution:** Generate evidence bundle and handoff package

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---

## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Gather requirements from discovery and architecture

**Description:** Consolidate all requirements from previous protocols

Communication: Document any clarifications needed from client

Evidence: Track requirement sources in `.artifacts/artisans-corner-dashboard/protocol-06/workflow-logs/`

**Duration:** 30 minutes

---

### STEP 2

**Action:** Draft PRD document structure

**Description:** Create PRD outline with all required sections

Communication: Share draft outline with stakeholders for feedback

Evidence: Store draft in `.artifacts/artisans-corner-dashboard/protocol-06/prd-draft.md`

**Duration:** 45 minutes

---

### STEP 3

**Action:** Validate PRD completeness

**Description:** Run validation scripts and resolve gaps

Communication: Report validation results to product manager

Evidence: Generate validation report in `.artifacts/artisans-corner-dashboard/protocol-06/prd-validation.json`

**Duration:** 30 minutes

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 3 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to product manager

### Workflow State Management

- State stored in: `.artifacts/artisans-corner-dashboard/protocol-06/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/artisans-corner-dashboard/protocol-06/workflow-status.json`
- Execution logs: `.artifacts/artisans-corner-dashboard/protocol-06/workflow-logs/`
- Performance metrics: `.artifacts/artisans-corner-dashboard/protocol-06/workflow-metrics.json`

---

## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=06` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/artisans-corner-dashboard/protocol-06/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/06-*.md`, `.artifacts/`
- Write access to: `.artifacts/artisans-corner-dashboard/protocol-06/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_06.py \
  --protocol 06 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 06` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/artisans-corner-dashboard/protocol-06/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 06 \
  --input .artifacts/artisans-corner-dashboard/protocol-06/input/ \
  --output .artifacts/artisans-corner-dashboard/protocol-06/output/ \
  --log-file .artifacts/artisans-corner-dashboard/protocol-06/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 06` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/artisans-corner-dashboard/protocol-06/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_06.py \
  --protocol 06 \
  --artifacts-dir .artifacts/artisans-corner-dashboard/protocol-06/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 06` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/artisans-corner-dashboard/protocol-06/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_06.py \
  --protocol 06 \
  --artifacts-dir .artifacts/artisans-corner-dashboard/protocol-06/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 06` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/artisans-corner-dashboard/protocol-06/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error

### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/artisans-corner-dashboard/protocol-06/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/artisans-corner-dashboard/protocol-06/execution.log`
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
- `.artifacts/artisans-corner-dashboard/protocol-06/execution.log` - Main execution log
- `.artifacts/artisans-corner-dashboard/protocol-06/validation.log` - Validation log
- `.artifacts/artisans-corner-dashboard/protocol-06/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/artisans-corner-dashboard/protocol-06/workflow-status.json` - Real-time status
- `.artifacts/artisans-corner-dashboard/protocol-06/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/artisans-corner-dashboard/protocol-06/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/artisans-corner-dashboard/protocol-06/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] PRD document reviewed for completeness and accuracy
- [ ] Functional requirements validated against business objectives
- [ ] User stories documented with acceptance criteria
- [ ] Technical specifications provided for implementation
- [ ] Stakeholder approval obtained and documented
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-06-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol 07
- **PRD Documentation:** Complete PRD with all sections
- **Validation Reports:** All quality gate and script validation results
- **Stakeholder Approvals:** Formal sign-off records

### Sign-off Guidance
- **Protocol Owner Approval**: Required before handoff to Protocol 07
- **Stakeholder Confirmation**: Business stakeholder must approve PRD content
- **Technical Review**: Engineering lead must confirm implementation readiness
- **Quality Assurance**: QA team must validate documentation completeness

### Handoff Verification
- [ ] Checksum verification passed
- [ ] Downstream protocol has received package
- [ ] Protocol owner sign-off completed
- [ ] Stakeholder approvals documented
- [ ] Technical readiness confirmed
- [ ] Downstream protocol confirms receipt and readiness
- [ ] No outstanding questions or clarifications needed

### Sign-Off
- Protocol Owner: _________________ Date: _________
- Downstream Owner: _________________ Date: _________

---
## COMMUNICATION & STAKEHOLDER ALIGNMENT

### Status Announcements (Template)
```
[PROTOCOL 06 | PHASE X START] - [Action description]
[PROTOCOL 06 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 06 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Product Manager - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** Technical Lead, Client, QA Lead - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/artisans-corner-dashboard/protocol-06/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders


---

## INTEGRATION POINTS

### Inputs From
- **Protocol XX**: [Specify inputs]

### Outputs To
- **Protocol YY**: [Specify outputs]

### Artifact Storage
- **Primary Evidence**: `.artifacts/[project-name]/protocol-[ID]/`

---