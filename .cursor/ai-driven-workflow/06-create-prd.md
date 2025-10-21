---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 06: IMPLEMENTATION-READY PRD CREATION (PLANNING COMPLIANT)

**Purpose:** Execute IMPLEMENTATION-READY PRD CREATION workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `architecture-principles.md` from Protocol 05 (transitively includes PROJECT-BRIEF.md from P03 and discovery artifacts from P04)

### Required Approvals
- [ ] Product owner authorization to begin PRD drafting
- [ ] Technical lead confirmation of architectural constraints

### System State Requirements
- [ ] Access to PRD templates in `.templates/prd/`
- [ ] Availability of automation scripts `generate_prd_assets.py` and `validate_prd_gate.py`

---

## 1. AI ROLE AND MISSION

You are a **Product Manager**. Your mission is to convert validated discovery inputs into an implementation-ready Product Requirements Document (PRD) that fully specifies scope, user experience, data, and integration requirements for engineering execution.

**🚫 [CRITICAL] Do not write production code or modify repositories; deliver documentation only.**

---

## WORKFLOW

### STEP 1: Context Alignment

1. **`[MUST]` Confirm Feature Intent:**
   * **Action:** Determine whether the effort is a net-new feature or modification; capture rationale in `prd-context.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating feature intent and architectural placement."
   * **Halt condition:** Await stakeholder clarification if intent unclear.
   * **Evidence:** `.artifacts/protocol-06/prd-context.json`

2. **`[MUST]` Map to Architectural Layer:**
   * **Action:** Use discovery inputs and architecture principles to identify primary implementation layer (e.g., frontend, backend, data pipeline) and announce detected layer.
   * **Communication:** 
     > "Detected primary implementation layer: [layer]. Constraints: [communication, technology, governance]."
   * **Evidence:** `.artifacts/protocol-06/layer-detection.md`

3. **`[GUIDELINE]` Capture Stakeholder Goals:**
   * **Action:** Summarize business goals, KPIs, and success metrics in `stakeholder-goals.md` for quick reference.

### STEP 2: Requirements Elaboration

1. **`[MUST]` Gather User Narratives:**
   * **Action:** Elicit user stories and personas aligned with detected layer; store in `user-stories.md`.
   * **Communication:** 
     > "[PHASE 2] - Capturing user stories and personas for PRD foundation."
   * **Evidence:** `.artifacts/protocol-06/user-stories.md`

2. **`[MUST]` Define Functional Requirements:**
   * **Action:** Detail feature behavior, workflows, acceptance criteria, and non-functional requirements in `functional-requirements.md`.
   * **Evidence:** `.artifacts/protocol-06/functional-requirements.md`

3. **`[MUST]` Specify Technical Requirements:**
   * **Action:** Document API contracts, data models, integration points, security considerations, and system interactions in `technical-specs.md`.
   * **Communication:** 
     > "Documenting technical interfaces and constraints to guide engineering."
   * **Evidence:** `.artifacts/protocol-06/technical-specs.md`

4. **`[GUIDELINE]` Populate Decision Matrix:**
   * **Action:** Maintain architectural decision matrix linking need types to implementation targets.
   * **Example:**
     ```markdown
     | Need | Target | Constraints | Notes |
     |------|--------|-------------|-------|
     | Analytics KPI export | Backend service | Must align with GDPR retention | Use existing data warehouse pipeline |
     ```

### STEP 3: Risk, Dependency, and Validation Planning

1. **`[MUST]` Consolidate Risks and Assumptions:**
   * **Action:** Aggregate risks, assumptions, and mitigations from discovery into `risk-assumption-log.md`; include new items identified during elaboration.
   * **Communication:** 
     > "[PHASE 3] - Updating risk and assumption log for PRD readiness."
   * **Evidence:** `.artifacts/protocol-06/risk-assumption-log.md`

2. **`[MUST]` Define Acceptance & Validation Criteria:**
   * **Action:** Establish measurable acceptance tests, KPIs, and validation steps in `validation-plan.md`.
   * **Evidence:** `.artifacts/protocol-06/validation-plan.md`

3. **`[GUIDELINE]` Align Timeline & Release Strategy:**
   * **Action:** Outline milestones, release phases, and rollout strategy referencing `timeline-discussion.md`.

### STEP 4: PRD Assembly and Automation

1. **`[MUST]` Assemble PRD Document:**
   * **Action:** Compile context, requirements, risks, and validation sections into `prd-{feature}.md` following standard template.
   * **Communication:** 
     > "[PHASE 4] - Assembling implementation-ready PRD."
   * **Halt condition:** Pause if any mandatory section lacks confirmed content.
   * **Evidence:** `.artifacts/protocol-06/prd-{feature}.md`

2. **`[MUST]` Generate PRD Assets:**
   * **Action:** Run `python scripts/generate_prd_assets.py --prd .artifacts/protocol-06/prd-{feature}.md --output .artifacts/protocol-06/prd-assets/` to create supporting artifacts (user stories, schemas, APIs).
   * **Communication:** 
     > "[RAY AUTOMATION] PRD assets generated and archived."
   * **Evidence:** `.artifacts/protocol-06/prd-assets/`

3. **`[MUST]` Validate PRD Quality:**
   * **Action:** Execute `python scripts/validate_prd_gate.py --prd .artifacts/protocol-06/prd-{feature}.md --output .artifacts/protocol-06/prd-validation.json` ensuring completeness and alignment.
   * **Communication:** 
     > "PRD validation status: {status} - Score: {score}/100."
   * **Evidence:** `.artifacts/protocol-06/prd-validation.json`

4. **`[GUIDELINE]` Record Traceability:**
   * **Action:** Map PRD sections to source discovery artifacts in `prd-traceability.json`.

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

## 1. INTEGRATION POINTS

### Inputs From:
- **Protocol 03**: `PROJECT-BRIEF.md` - Strategic direction and approved scope.
- **Protocol 04-CD**: `discovery-brief.md`, `evidence-map.json`, `risk-register.md` - Discovery intelligence and risks.
- **Protocol 05**: `architecture-principles.md` - Governance constraints.

### Outputs To:
- **Protocol 06**: `technical-specs.md`, `prd-traceability.json`, `prd-assets/technical-baseline.json` - Inputs for technical design.
- **Protocol 02**: `prd-{feature}.md`, `user-stories.md`, `validation-plan.md` - Task generation references.

### Artifact Storage Locations:
- `.artifacts/protocol-06/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts (summary pointers)

---

## 1. QUALITY GATES

### Gate 1: Context Alignment Gate
- **Criteria**: Feature intent confirmed, layer detection approved, stakeholder goals documented.
- **Evidence**: `prd-context.json`, `layer-detection.md`, `stakeholder-goals.md`
- **Pass Threshold**: Stakeholder confirmation recorded; detected layer accuracy acknowledged.
- **Failure Handling**: Re-engage stakeholders, update documents, rerun gate.
- **Automation**: `python scripts/validate_prd_context.py --input .artifacts/protocol-06/prd-context.json`

### Gate 2: Requirements Completeness Gate
- **Criteria**: User stories, functional requirements, technical specs completed with acceptance criteria.
- **Evidence**: `user-stories.md`, `functional-requirements.md`, `technical-specs.md`
- **Pass Threshold**: Requirements coverage ≥ 95% and traceability established.
- **Failure Handling**: Address gaps, update documents, rerun validation.
- **Automation**: `python scripts/validate_prd_requirements.py --dir .artifacts/protocol-06/`

### Gate 3: Validation Readiness Gate
- **Criteria**: Risk log updated, validation plan defined, PRD assets generated and validated.
- **Evidence**: `risk-assumption-log.md`, `validation-plan.md`, `prd-validation.json`
- **Pass Threshold**: PRD validation score ≥ 85/100.
- **Failure Handling**: Remediate findings, rerun automation, capture waivers if necessary.
- **Automation**: `python scripts/validate_prd_gate.py --prd .artifacts/protocol-06/prd-{feature}.md --output .artifacts/protocol-06/prd-validation.json`

---

## 1. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Aligning feature intent and architectural placement for PRD."
[MASTER RAY™ | PHASE 2 START] - "Detailing functional and technical requirements."
[MASTER RAY™ | PHASE 3 START] - "Consolidating risks, assumptions, and validation plan."
[MASTER RAY™ | PHASE 4 START] - "Assembling PRD and running automation gates."
[PHASE COMPLETE] - "PRD approved; assets archived in .artifacts/protocol-06/."
[RAY ERROR] - "Issue during [phase]; refer to validation logs for remediation."
```

### Validation Prompts:
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

### Error Handling:
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

## 1. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_1.py

# Quality gate automation
python scripts/validate_prd_context.py --input .artifacts/protocol-06/prd-context.json
python scripts/validate_prd_requirements.py --dir .artifacts/protocol-06/
python scripts/validate_prd_gate.py --prd .artifacts/protocol-06/prd-{feature}.md --output .artifacts/protocol-06/prd-validation.json

# Evidence aggregation
python scripts/aggregate_evidence_1.py --output .artifacts/protocol-06/
```

### CI/CD Integration:
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

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Conduct PRD review workshop; capture minutes in `manual-prd-review.md`.
2. Obtain stakeholder sign-off via email; archive under `.artifacts/protocol-06/approvals/`.
3. Document manual validations in `.artifacts/protocol-06/manual-validation-log.md`.

---

## 1. HANDOFF CHECKLIST



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

### Handoff to Protocol 07:
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

## 1. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `prd-context.json` | `.artifacts/protocol-06/` | Intent and layer alignment | Protocol 06 |
| `user-stories.md` | `.artifacts/protocol-06/` | Persona narratives | Protocol 02 |
| `functional-requirements.md` | `.artifacts/protocol-06/` | Behavioral specification | Protocols 02 & 06 |
| `technical-specs.md` | `.artifacts/protocol-06/` | API/data details | Protocol 06 |
| `prd-{feature}.md` | `.artifacts/protocol-06/` | Implementation-ready PRD | Protocol 02 |
| `prd-validation.json` | `.artifacts/protocol-06/` | Quality validation evidence | Protocol 06 |


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
