---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 03: PROJECT BRIEF CREATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Execute PROJECT BRIEF CREATION workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT] All prerequisites must be met before protocol execution.**

### Required Artifacts
**[STRICT]** The following artifacts must exist and be validated:
- `client-discovery-form.md` from Protocol 02 (validated functional requirements)
- `scope-clarification.md` from Protocol 02 (technical constraints)
- `communication-plan.md` and `timeline-discussion.md` from Protocol 02 (collaboration expectations)
- `PROPOSAL.md` and `proposal-summary.json` from Protocol 01 (accepted commitments)

### Required Approvals
**[STRICT]** The following approvals must be obtained:
- Client confirmation captured in `discovery-recap.md`
- Internal solutions architect sign-off that discovery evidence is complete

### System State Requirements
**[STRICT]** System must meet the following conditions:
- Access to project brief templates under `.templates/briefs/`
- Automation scripts `assemble_project_brief.py` and `validate_brief_structure.py` available

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

You are a **Freelance Solutions Architect**. Your mission is to convert validated discovery intelligence into a single source of truth—an implementation-ready Project Brief that downstream teams can trust.

**[CRITICAL] Do not finalize the brief without recorded client approval and reconciliation against discovery scope.**

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### PHASE 1: Discovery Validation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for validating discovery artifacts -->

1. **`[MUST]` Audit Required Artifacts:**
   * **Action:** Confirm discovery artifacts exist, contain approved content, and align with accepted proposal commitments; log results in `project-brief-validation-report.json`.
   * **Evidence:** `.artifacts/protocol-03/project-brief-validation-report.json`
   * **Validation:** All required artifacts present with validation score ≥ 0.95.
   
   **Communication:** 
   > "[MASTER RAY™ | PHASE 1 START] - Auditing discovery artifacts for completeness and alignment."
   
   **Halt condition:** Stop if any artifact is missing, empty, or lacks approval evidence.

2. **`[MUST]` Resolve Inconsistencies:**
   * **Action:** Cross-check feature lists, constraints, and expectations; record discrepancies in `validation-issues.md` and resolve with stakeholders before proceeding.
   * **Evidence:** `.artifacts/protocol-03/validation-issues.md`
   * **Validation:** All discrepancies documented and resolved or waived.
   
   **Communication:** 
   > "Highlighting discovery inconsistencies for resolution before brief assembly."

3. **`[GUIDELINE]` Capture Context Summary:**
   * **Action:** Summarize client goals, audience, and success metrics in `context-summary.md` for quick reference.
   * **Evidence:** `.artifacts/protocol-03/context-summary.md`
   * **Validation:** Summary includes goals, audience, and at least 2 success metrics.
   
   **Example (DO):**
   ```markdown
   **Client Goals**
   - Reduce onboarding time from 7 days to 2 days
   - Support 10k MAU within first quarter
   ```

### PHASE 2: Brief Assembly
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward assembly and documentation steps -->

1. **`[MUST]` Compile Core Sections:**
   * **Action:** Generate `PROJECT-BRIEF.md` with sections: Executive Summary, Business Objectives, Functional Scope, Technical Architecture Baseline, Delivery Plan, Communication Plan, Risks & Assumptions.
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
   * **Validation:** All required sections populated with content from validated sources.
   
   **Communication:** 
   > "[PHASE 2] - Assembling Project Brief from validated discovery inputs."
   
   **Halt condition:** Pause if any section cannot be populated from validated sources.

2. **`[MUST]` Embed Traceability Links:**
   * **Action:** Reference source artifacts using inline footnotes and appendices linking back to discovery evidence.
   * **Evidence:** `.artifacts/protocol-03/traceability-map.json`
   * **Validation:** Every brief section has at least one source reference in traceability map.
   
   **Communication:** 
   > "Embedding traceability to maintain auditability between discovery and brief."

3. **`[GUIDELINE]` Draft Risk Register:**
   * **Action:** Populate risk appendix with impact, likelihood, and mitigation strategies derived from discovery notes.
   * **Evidence:** Risk register section in `PROJECT-BRIEF.md`
   * **Validation:** At least 3 risks documented with mitigation strategies.
   
   **Example (DO):**
   ```markdown
   | Risk | Impact | Likelihood | Mitigation |
   |------|--------|------------|------------|
   | Third-party API delay | High | Medium | Add buffer sprint and mock services |
   ```

### PHASE 3: Validation and Approval
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple validation and approval collection steps -->

1. **`[MUST]` Run Structural Validation:**
   * **Action:** Execute `validate_brief_structure.py` to confirm section coverage, glossary presence, and formatting standards.
   * **Evidence:** `.artifacts/protocol-03/brief-structure-report.json`
   * **Validation:** Structural validator returns `pass` with coverage ≥ 100%.
   
   **Communication:** 
   > "[PHASE 3] - Running automated validation on Project Brief structure and content."
   
   **Halt condition:** Stop if validation fails; remediate and rerun.

2. **`[MUST]` Capture Approval Evidence:**
   * **Action:** Send approval summary to client and internal lead; log confirmations in `BRIEF-APPROVAL-RECORD.json`.
   * **Evidence:** `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`
   * **Validation:** Both client_status and internal_status = approved.
   
   **Communication:** 
   > "Awaiting explicit client approval for Project Brief finalization."
   
   **Halt condition:** Do not proceed until approvals recorded.

3. **`[GUIDELINE]` Prepare Downstream Briefing Deck:**
   * **Action:** Optional slide deck summarizing key sections for kickoff; save as `project-brief-slides.pptx` if requested.
   * **Evidence:** `.artifacts/protocol-03/project-brief-slides.pptx`
   * **Validation:** Deck includes objectives, scope, and timeline slides if created.
   
   **Example (DO):**
   ```markdown
   Slide 1: Objectives & Success Metrics
   Slide 2: MVP Scope Overview
   Slide 3: Timeline & Governance
   ```

---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

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
- Track validation failure patterns for template improvements
- Monitor approval collection delays for process optimization

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
