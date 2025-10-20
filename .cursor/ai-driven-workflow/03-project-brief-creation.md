---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 03: PROJECT BRIEF CREATION (PROJECT-SCOPING COMPLIANT)

**Purpose:** Execute PROJECT BRIEF CREATION workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `client-discovery-form.md` from Protocol 02 (validated functional requirements)
- [ ] `scope-clarification.md` from Protocol 02 (technical constraints)
- [ ] `communication-plan.md` and `timeline-discussion.md` from Protocol 02 (collaboration expectations)
- [ ] `PROPOSAL.md` and `proposal-summary.json` from Protocol 01 (accepted commitments)

### Required Approvals
- [ ] Client confirmation captured in `discovery-recap.md`
- [ ] Internal solutions architect sign-off that discovery evidence is complete

### System State Requirements
- [ ] Access to project brief templates under `.templates/briefs/`
- [ ] Automation scripts `assemble_project_brief.py` and `validate_brief_structure.py` available

---

## 01. AI ROLE AND MISSION

You are a **Freelance Solutions Architect**. Your mission is to convert validated discovery intelligence into a single source of truth—an implementation-ready Project Brief that downstream teams can trust.

**🚫 [CRITICAL] Do not finalize the brief without recorded client approval and reconciliation against discovery scope.**

---

## WORKFLOW

### STEP 1: Discovery Validation

1. **`[MUST]` Audit Required Artifacts:**
   * **Action:** Confirm discovery artifacts exist, contain approved content, and align with accepted proposal commitments; log results in `project-brief-validation-report.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Auditing discovery artifacts for completeness and alignment."
   * **Halt condition:** Stop if any artifact is missing, empty, or lacks approval evidence.
   * **Evidence:** `.artifacts/protocol-03/project-brief-validation-report.json`

2. **`[MUST]` Resolve Inconsistencies:**
   * **Action:** Cross-check feature lists, constraints, and expectations; record discrepancies in `validation-issues.md` and resolve with stakeholders before proceeding.
   * **Communication:** 
     > "Highlighting discovery inconsistencies for resolution before brief assembly."
   * **Evidence:** `.artifacts/protocol-03/validation-issues.md`

3. **`[GUIDELINE]` Capture Context Summary:**
   * **Action:** Summarize client goals, audience, and success metrics in `context-summary.md` for quick reference.
   * **Example:**
     ```markdown
     **Client Goals**
     - Reduce onboarding time from 7 days to 2 days
     - Support 10k MAU within first quarter
     ```

### STEP 2: Brief Assembly

1. **`[MUST]` Compile Core Sections:**
   * **Action:** Generate `PROJECT-BRIEF.md` with sections: Executive Summary, Business Objectives, Functional Scope, Technical Architecture Baseline, Delivery Plan, Communication Plan, Risks & Assumptions.
   * **Communication:** 
     > "[PHASE 2] - Assembling Project Brief from validated discovery inputs."
   * **Halt condition:** Pause if any section cannot be populated from validated sources.
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`

2. **`[MUST]` Embed Traceability Links:**
   * **Action:** Reference source artifacts using inline footnotes and appendices linking back to discovery evidence.
   * **Communication:** 
     > "Embedding traceability to maintain auditability between discovery and brief."
   * **Evidence:** `.artifacts/protocol-03/traceability-map.json`

3. **`[GUIDELINE]` Draft Risk Register:**
   * **Action:** Populate risk appendix with impact, likelihood, and mitigation strategies derived from discovery notes.
   * **Example:**
     ```markdown
     | Risk | Impact | Likelihood | Mitigation |
     |------|--------|------------|------------|
     | Third-party API delay | High | Medium | Add buffer sprint and mock services |
     ```

### STEP 3: Validation and Approval

1. **`[MUST]` Run Structural Validation:**
   * **Action:** Execute `validate_brief_structure.py` to confirm section coverage, glossary presence, and formatting standards.
   * **Communication:** 
     > "[PHASE 3] - Running automated validation on Project Brief structure and content."
   * **Halt condition:** Stop if validation fails; remediate and rerun.
   * **Evidence:** `.artifacts/protocol-03/brief-structure-report.json`

2. **`[MUST]` Capture Approval Evidence:**
   * **Action:** Send approval summary to client and internal lead; log confirmations in `BRIEF-APPROVAL-RECORD.json`.
   * **Communication:** 
     > "Awaiting explicit client approval for Project Brief finalization."
   * **Halt condition:** Do not proceed until approvals recorded.
   * **Evidence:** `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`

3. **`[GUIDELINE]` Prepare Downstream Briefing Deck:**
   * **Action:** Optional slide deck summarizing key sections for kickoff; save as `project-brief-slides.pptx` if requested.
   * **Example:**
     ```markdown
     Slide 1: Objectives & Success Metrics
     Slide 2: MVP Scope Overview
     Slide 3: Timeline & Governance
     ```

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

## 01. INTEGRATION POINTS

### Inputs From:
- **Protocol 01**: `PROPOSAL.md`, `proposal-summary.json` - Alignment baseline and commitments.
- **Protocol 02**: `client-discovery-form.md`, `scope-clarification.md`, `communication-plan.md`, `timeline-discussion.md`, `discovery-recap.md` - Validated discovery intelligence.

### Outputs To:
- **Protocol 04**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json` - Context kit enrichment for bootstrap activities.
- **Protocol 06**: `technical-baseline.json` (extracted from brief) - Inputs for technical design.

### Artifact Storage Locations:
- `.artifacts/protocol-03/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 01. QUALITY GATES

### Gate 1: Discovery Evidence Verification
- **Criteria**: All prerequisite artifacts validated, discrepancies resolved, validation report status = PASS.
- **Evidence**: `.artifacts/protocol-03/project-brief-validation-report.json`
- **Pass Threshold**: Validation score ≥ 0.95.
- **Failure Handling**: Re-open discovery with client, update artifacts, rerun validation.
- **Automation**: `python scripts/validate_discovery_inputs.py --input .artifacts/protocol-02/ --output .artifacts/protocol-03/project-brief-validation-report.json`

### Gate 2: Structural Integrity
- **Criteria**: Every brief section populated, traceability map references source artifacts, glossary present.
- **Evidence**: `.artifacts/protocol-03/PROJECT-BRIEF.md`, `.artifacts/protocol-03/traceability-map.json`
- **Pass Threshold**: Structural validator returns `pass` with coverage ≥ 100%.
- **Failure Handling**: Fill missing sections, update traceability, rerun validator.
- **Automation**: `python scripts/validate_brief_structure.py --input .artifacts/protocol-03/PROJECT-BRIEF.md --report .artifacts/protocol-03/brief-structure-report.json`

### Gate 3: Approval Compliance
- **Criteria**: Client and internal approvals recorded with timestamps and references.
- **Evidence**: `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`
- **Pass Threshold**: Approval record includes `client_status = approved` and `internal_status = approved`.
- **Failure Handling**: Escalate to account lead, reconcile feedback, update record, rerun gate.
- **Automation**: `python scripts/verify_brief_approvals.py --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`

---

## 01. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating discovery evidence for Project Brief creation."
[MASTER RAY™ | PHASE 2 START] - "Compiling Project Brief sections with traceable sources."
[MASTER RAY™ | PHASE 3 START] - "Running structural validation and collecting approvals."
[PHASE COMPLETE] - "Project Brief approved and archived for downstream use."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Project Brief assembled and validated. Evidence available:
> - project-brief-validation-report.json
> - PROJECT-BRIEF.md
> - brief-structure-report.json
> - BRIEF-APPROVAL-RECORD.json
>
> Confirm readiness to trigger Protocol 04: Project Bootstrap & Context Engineering."
```

### Error Handling:
```
[RAY GATE FAILED: Structural Integrity]
> "Quality gate 'Structural Integrity' failed.
> Criteria: All sections must be populated with traceable references.
> Actual: Technical Architecture Baseline missing source references.
> Required action: Update traceability-map.json, repopulate section, rerun validator.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 01. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_01.py

# Quality gate automation
python scripts/validate_discovery_inputs.py --input .artifacts/protocol-02/ --output .artifacts/protocol-03/project-brief-validation-report.json
python scripts/validate_brief_structure.py --input .artifacts/protocol-03/PROJECT-BRIEF.md --report .artifacts/protocol-03/brief-structure-report.json
python scripts/verify_brief_approvals.py --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json

# Evidence aggregation
python scripts/aggregate_evidence_01.py --output .artifacts/protocol-03/
```

### CI/CD Integration:
```yaml
name: Protocol 03 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 03 Gates
        run: python scripts/run_protocol_01_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual peer review of discovery artifacts; note findings in `manual-validation-checklist.md`.
2. Review PROJECT-BRIEF.md with stakeholders over call; capture approval email or meeting minutes.
3. Store manual evidence in `.artifacts/protocol-03/manual-validation-log.md`.

---

## 01. HANDOFF CHECKLIST



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

### Handoff to Protocol 04:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 04: Project Bootstrap & Context Engineering

**Evidence Package:**
- `PROJECT-BRIEF.md` - Canonical source of truth for planning
- `technical-baseline.json` - Extracted architecture signals for bootstrap and technical design

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md
```

---

## 01. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `project-brief-validation-report.json` | `.artifacts/protocol-03/` | Proof of discovery alignment | Protocol 04 |
| `PROJECT-BRIEF.md` | `.artifacts/protocol-03/` | Authoritative brief | Protocols 00 & 06 |
| `traceability-map.json` | `.artifacts/protocol-03/` | Source linkage for brief content | Protocol 06 |
| `BRIEF-APPROVAL-RECORD.json` | `.artifacts/protocol-03/` | Approval evidence | Protocol 04 |
| `technical-baseline.json` | `.artifacts/protocol-03/` | Technical summary for design | Protocol 06 |


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
