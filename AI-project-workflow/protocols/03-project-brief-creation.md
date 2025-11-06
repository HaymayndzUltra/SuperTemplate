---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 03: PROJECT BRIEF CREATION (PROJECT-SCOPING COMPLIANT)

## IDENTITY & OWNERSHIP

### Protocol Identity
- **Protocol ID:** 03
- **Protocol Name:** PROJECT BRIEF CREATION (PROJECT-SCOPING COMPLIANT)
- **Protocol Owner:** Brief Creator
- **Owner Contact:** [Email/Slack]
- **Created:** 2025-01-01
- **Last Updated:** 2025-11-06
- **Version:** 2.0

### Protocol Classification
- **Category:** Documentation
- **Criticality:** High
- **Complexity:** High
- **Scope:** Module

### Protocol Lineage
- **Predecessor:** Protocol 02
- **Successor:** Protocol 04
- **Related Protocols:** [List related protocols]

### Protocol Metadata
- **Purpose:** Create comprehensive project brief from discovery insights
- **Success Criteria:** All quality gates pass, artifacts complete for next protocol
- **Failure Modes:** [List potential failure modes]
- **Recovery Procedure:** [Define recovery steps]

---
## ROLES & RESPONSIBILITIES

### Primary Roles

#### Protocol Executor
- **Role:** Brief Creator
- **Responsibilities:**
  - Execute protocol steps in sequence
  - Validate at each checkpoint
  - Escalate blockers immediately
  - Document decisions and rationale
- **Authority:** Can make decisions on protocol execution and quality gates
- **Escalation:** Technical Lead or Project Manager

#### Protocol Owner
- **Role:** Brief Creator
- **Responsibilities:**
  - Approve protocol execution
  - Review quality gates
  - Sign off on handoff
  - Address escalations
- **Authority:** Can make decisions on protocol execution and quality gates

#### Downstream Owner
- **Role:** Protocol 04 Owner
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

1. **`[MUST]` Seed Brief Frontmatter:**
   * **Action:** Prepend `PROJECT-BRIEF.md` with YAML frontmatter capturing stack metadata for downstream automation. Include keys: `name`, `industry`, `project_type`, `frontend`, `backend`, `database`, `auth`, `deploy`, `compliance` (array), `features` (array), and `separate_repos` (boolean). Populate values from validated discovery signals and protocol defaults (fallbacks: `industry=saas`, `project_type=fullstack`, `separate_repos=true`).
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
   * **Validation:** Frontmatter parses as valid YAML and matches stack selections recorded in `technical-baseline.json`.

   **Example (DO):**
   ```yaml
   ---
   name: acme-analytics
   industry: saas
   project_type: fullstack
   frontend: nextjs
   backend: fastapi
   database: postgres
   auth: auth0
   deploy: aws
   compliance:
     - soc2
     - gdpr
   features:
     - data-foundations
     - model-ops
   separate_repos: true
   ---
   ```

2. **`[MUST]` Compile Core Sections:**
   * **Action:** Generate `PROJECT-BRIEF.md` with sections: Executive Summary, Business Objectives, Functional Scope, Technical Architecture Baseline, Delivery Plan, Communication Plan, Risks & Assumptions.
   * **Evidence:** `.artifacts/protocol-03/PROJECT-BRIEF.md`
   * **Validation:** All required sections populated with content from validated sources.
   
   **Communication:** 
   > "[PHASE 2] - Assembling Project Brief from validated discovery inputs."
   
   **Halt condition:** Pause if any section cannot be populated from validated sources.

3. **`[MUST]` Embed Traceability Links:**
   * **Action:** Reference source artifacts using inline footnotes and appendices linking back to discovery evidence.
   * **Evidence:** `.artifacts/protocol-03/traceability-map.json`
   * **Validation:** Every brief section has at least one source reference in traceability map.
   
   **Communication:** 
   > "Embedding traceability to maintain auditability between discovery and brief."

4. **`[GUIDELINE]` Draft Risk Register:**
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
---

## 5. INTEGRATION POINTS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Defining standards for inputs/outputs and artifact storage -->

### Inputs From:
**[STRICT]** The following inputs must be validated before execution:
- **Protocol 01**: `PROPOSAL.md`, `proposal-summary.json` - Alignment baseline and commitments.
- **Protocol 02**: `client-discovery-form.md`, `scope-clarification.md`, `communication-plan.md`, `timeline-discussion.md`, `discovery-recap.md` - Validated discovery intelligence.

### Outputs To:
**[STRICT]** The following outputs must be generated for downstream protocols:
- **Protocol 04**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json` - Context kit enrichment for bootstrap activities.
- **Protocol 06**: `technical-baseline.json` (extracted from brief) - Inputs for technical design.

### Artifact Storage Locations:
**[STRICT]** All artifacts must be stored in standardized locations:
- `.artifacts/protocol-03/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## QUALITY GATES
<!-- [Category: GUIDELINES-FORMATS] -->

### Gate 1: Discovery Evidence Verification
**Type:** Prerequisite  
**Purpose:** Confirm discovery deliverables from Protocol 02 meet fidelity requirements before drafting the brief.  
**Pass Criteria:**
- **Threshold:** Validation score ≥0.95 in `project-brief-validation-report.json`; discrepancy metric ≤1 open item.  
- **Boolean Check:** `project-brief-validation-report.json` field `status` equals `PASS`.  
- **Metrics:** Report captures evidence completeness metric and discrepancy count metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-03/project-brief-validation-report.json`.  
**Automation:**
- Script: `python3 scripts/validate_discovery_inputs.py --input .artifacts/protocol-02/ --output .artifacts/protocol-03/project-brief-validation-report.json`.  
- Script: `python3 scripts/validate_prerequisites_03.py --log .artifacts/protocol-03/prerequisites-log.json`.  
- CI Integration: `real-validation-pipeline.yml` invokes discovery verification on push; failures gate pull requests.  
- Config: `config/protocol_gates/03.yaml` defines validation-score thresholds and discrepancy limits.  
**Failure Handling:**
- **Rollback:** Reopen discovery artifacts, resolve flagged discrepancies, and rerun validation script.  
- **Notification:** Alert Protocol 02 owner and solutions architect via governance channel when validation score drops below threshold.  
- **Waiver:** Waivers stored in `.artifacts/protocol-03/gate-waivers.json` with executive sponsor approval before proceeding.

### Gate 2: Structural Integrity
**Type:** Execution  
**Purpose:** Guarantee PROJECT-BRIEF structure, traceability, and glossary conform to template.  
**Pass Criteria:**
- **Threshold:** Structural coverage metric ≥100%; unresolved section metric = 0.  
- **Boolean Check:** `traceability-map.json` references all major brief sections.  
- **Metrics:** `brief-structure-report.json` captures section coverage metric, glossary completeness metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-03/PROJECT-BRIEF.md` and `.artifacts/protocol-03/traceability-map.json`.  
**Automation:**
- Script: `python3 scripts/validate_brief_structure.py --input .artifacts/protocol-03/PROJECT-BRIEF.md --report .artifacts/protocol-03/brief-structure-report.json`.  
- Script: `python3 scripts/traceability_mapper.py --brief .artifacts/protocol-03/PROJECT-BRIEF.md --output .artifacts/protocol-03/traceability-map.json`.  
- CI Integration: Structural validation stage runs on `ubuntu-latest` with artefact upload to validation dashboard.  
- Config: `config/protocol_gates/03.yaml` stores structural coverage minimums and glossary requirements.  
**Failure Handling:**
- **Rollback:** Update missing sections, regenerate traceability map, rerun structural validator before handoff.  
- **Notification:** Notify product owner when structure coverage metric falls below 100%.  
- **Waiver:** Exceptional waivers require architecture council sign-off and must document compensating controls.

### Gate 3: Approval Compliance
**Type:** Execution  
**Purpose:** Ensure client and internal approvals captured with timestamps for legal compliance.  
**Pass Criteria:**
- **Threshold:** Approval completion rate metric ≥90% within 48 hours; pending approvals metric ≤1.  
- **Boolean Check:** `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json` entries include both `client_status: approved` and `internal_status: approved`.  
- **Metrics:** `approval-tracker.json` logs approval latency metric and reminder count metric.  
- **Evidence Link:** Evidence validated against `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`.  
**Automation:**
- Script: `python3 scripts/verify_brief_approvals.py --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json --output .artifacts/protocol-03/approval-tracker.json`.  
- Script: `python3 scripts/send_approval_reminders.py --record .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`.  
- CI Integration: Nightly workflow posts approval status summary to `.artifacts/validation/protocol_quality_gates-summary.json`.  
- Config: `config/protocol_gates/03.yaml` codifies approval latency and reminder thresholds.  
**Failure Handling:**
- **Rollback:** Pause Protocol 04 activation, reconcile feedback with stakeholders, rerun approval verification.  
- **Notification:** Escalate to account lead and governance queue if approval pending beyond SLA.  
- **Waiver:** Not applicable – approvals mandatory unless executive override logged with legal review.

### Gate 4: Handoff Integrity
**Type:** Completion  
**Purpose:** Validate that packaged brief artifacts meet downstream readiness for Protocol 04 and Protocol 06.  
**Pass Criteria:**
- **Threshold:** Handoff readiness score ≥0.97 in evidence manifest; downstream dependency metric = pass.  
- **Boolean Check:** Handoff checklist confirms `status: ready_for_protocol_04`.  
- **Metrics:** `handoff-verification.json` documents readiness metric, dependency resolution metric, checksum metric.  
- **Evidence Link:** Validated against `.artifacts/protocol-03/handoff-verification.json` and `.artifacts/protocol-03/evidence-manifest.json`.  
**Automation:**
- Script: `python3 scripts/aggregate_evidence_03.py --output .artifacts/protocol-03/ --protocol-id 03`.  
- Script: `python3 scripts/run_protocol_03_gates.py --report .artifacts/protocol-03/handoff-verification.json`.  
- CI Integration: `script-registry-enforcement.yml` confirms aggregator registered and executed before merge.  
- Config: `config/protocol_gates/03.yaml` defines readiness score threshold and required artifacts list.  
**Failure Handling:**
- **Rollback:** Regenerate missing artifacts, resolve dependency gaps, rerun aggregator prior to downstream notification.  
- **Notification:** Inform Protocol 04 owner of handoff delay and share blocker summary.  
- **Waiver:** Emergency waiver documented in `gate-waivers.json` with CTO approval and mitigation steps.

### Compliance Integration
- **Industry Standards:** CommonMark Markdown, JSON Schema validation, YAML configuration standards applied to brief assets.  
- **Security Requirements:** SOC2-aligned access controls, GDPR-safe handling of client data, encryption at rest for approval logs.  
- **Regulatory Compliance:** FTC disclosure alignment for commitments, ISO 9001 documentation retention, audit readiness for governance reviews.  
- **Governance:** Gate thresholds governed via `config/protocol_gates/03.yaml`; automation telemetry captured in `.artifacts/validation/protocol_quality_gates-summary.json` and protocol governance dashboards.

---

## 7. COMMUNICATION PROTOCOLS
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting communication standards and templates -->

### Status Announcements:
**[STRICT]** Use standardized announcements for phase transitions:
```
[MASTER RAY™ | PHASE 1 START] - "Validating discovery evidence for Project Brief creation."
[MASTER RAY™ | PHASE 2 START] - "Compiling Project Brief sections with traceable sources."
[MASTER RAY™ | PHASE 3 START] - "Running structural validation and collecting approvals."
[PHASE COMPLETE] - "Project Brief approved and archived for downstream use."
[RAY ERROR] - "Issue encountered during [phase]; see validation-issues.md for details."
```

### Validation Prompts:
**[STRICT]** Use standardized prompts for validation requests:
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
**[STRICT]** Use standardized error messages for gate failures:
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

## 8. AUTOMATION HOOKS
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple execution of validation scripts with clear steps -->

**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### Validation Scripts:

1. **`[MUST]` Run prerequisite validation:**
   * **Action:** Execute script to validate prerequisites
   * **Evidence:** Validation output in execution log
   * **Validation:** Exit code 0
   
   ```bash
   # Prerequisite validation
   python scripts/validate_prerequisites_03.py
   ```

2. **`[MUST]` Run discovery input validation:**
   * **Action:** Execute script to validate discovery artifacts
   * **Evidence:** `.artifacts/protocol-03/project-brief-validation-report.json`
   * **Validation:** Validation score ≥ 0.95
   
   ```bash
   # Quality gate automation
   python scripts/validate_discovery_inputs.py \
     --input .artifacts/protocol-02/ \
     --output .artifacts/protocol-03/project-brief-validation-report.json
   ```

3. **`[MUST]` Run structural validation:**
   * **Action:** Execute script to validate brief structure
   * **Evidence:** `.artifacts/protocol-03/brief-structure-report.json`
   * **Validation:** Coverage ≥ 100%
   
   ```bash
   python scripts/validate_brief_structure.py \
     --input .artifacts/protocol-03/PROJECT-BRIEF.md \
     --report .artifacts/protocol-03/brief-structure-report.json
   ```

4. **`[MUST]` Run approval verification:**
   * **Action:** Execute script to verify approvals
   * **Evidence:** `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json`
   * **Validation:** Both client and internal approvals recorded
   
   ```bash
   python scripts/verify_brief_approvals.py \
     --input .artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json
   ```

5. **`[MUST]` Aggregate evidence:**
   * **Action:** Execute script to collect all evidence
   * **Evidence:** Evidence manifest in `.artifacts/protocol-03/`
   * **Validation:** All artifacts included in manifest
   
   ```bash
   # Evidence aggregation
   python scripts/aggregate_evidence_03.py \
     --output .artifacts/protocol-03/
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
        run: python scripts/run_protocol_03_gates.py
```

### Manual Fallbacks:

**When automation is unavailable:**

1. **Manual Discovery Validation:**
   - Perform manual peer review of discovery artifacts
   - Note findings in `manual-validation-checklist.md`
   - Document in `.artifacts/protocol-03/manual-validation-log.md`

2. **Manual Brief Review:**
   - Review PROJECT-BRIEF.md with stakeholders over call
   - Capture approval email or meeting minutes
   - Store evidence in `.artifacts/protocol-03/manual-validation-log.md`

3. **Manual Evidence Collection:**
   - Create manual checklist of all required artifacts
   - Verify each artifact exists and contains expected content
   - Document validation in manual evidence log
---

## 9. HANDOFF CHECKLIST
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple checklist execution for protocol completion -->

### Continuous Improvement Validation:

1. **`[GUIDELINE]` Validate improvement mechanisms:**
   * **Action:** Verify feedback collection and learning mechanisms are active
   * **Evidence:** Improvement tracking entries in execution log
   * **Validation:** All improvement checkpoints completed
   
   **Checklist:**
   - [ ] Execution feedback collected and logged
   - [ ] Lessons learned documented in protocol artifacts
   - [ ] Quality metrics captured for improvement tracking
   - [ ] Knowledge base updated with new patterns or insights
   - [ ] Protocol adaptation opportunities identified and logged
   - [ ] Retrospective scheduled (if required for this protocol phase)

### Pre-Handoff Validation:

1. **`[MUST]` Validate protocol completion:**
   * **Action:** Verify all prerequisites, steps, and quality gates completed
   * **Evidence:** Completed checklist in protocol execution log
   * **Validation:** All items checked
   
   **Checklist:**
   - [ ] All prerequisites were met
   - [ ] All workflow steps completed successfully
   - [ ] All quality gates passed (or waivers documented)
   - [ ] All evidence artifacts captured and stored
   - [ ] All integration outputs generated
   - [ ] All automation hooks executed successfully
   - [ ] Communication log complete

### Handoff to Protocol 04:

1. **`[MUST]` Execute protocol handoff:**
   * **Action:** Package evidence and trigger Protocol 04
   * **Evidence:** Handoff confirmation in execution log
   * **Validation:** Protocol 04 acknowledges receipt
   
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

## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `gate_utils.py` | Gate Utils | `scripts/` | ✅ Exists |
| `validate_gate_03_discovery.py` | Validate Gate 03 Discovery | `scripts/` | ✅ Exists |
| `aggregate_evidence_03.py` | Aggregate Evidence 03 | `scripts/` | ✅ Exists |
| `validate_gate_03_approvals.py` | Validate Gate 03 Approvals | `scripts/` | ✅ Exists |
| `run_protocol_gates.py` | Run Protocol Gates | `scripts/` | ✅ Exists |
| `validate_gate_03_structure.py` | Validate Gate 03 Structure | `scripts/` | ✅ Exists |

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
| `validate_gate_03_brief.py` | Validate Gate 03 Brief | `scripts/` | ✅ Exists |
| `generate_brief.py` | Generate Brief | `scripts/` | ✅ Exists |
| `aggregate_evidence_03.py` | Aggregate Evidence 03 | `scripts/` | ✅ Exists |

### Script Dependencies
- **Input:** [List input files/formats]
- **Output:** [List output files/formats]
- **External Dependencies:** Python 3.8+, [other dependencies]

### Automation Hooks
- **Pre-execution:** [Setup scripts if any]
- **During execution:** [Monitoring/logging scripts]
- **Post-execution:** [Cleanup/archival scripts]

### Script Maintenance
- Scripts reviewed and tested: 2025-11-06
- Last execution: 2025-11-06
- Known issues: None

---
## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Execute discovery analysis activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-03/workflow-logs/`

**Duration:** Varies based on complexity

---

### STEP 2

**Action:** Execute brief drafting activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-03/workflow-logs/`

**Duration:** Varies based on complexity

---

### STEP 3

**Action:** Execute stakeholder review activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-03/workflow-logs/`

**Duration:** Varies based on complexity

---

### STEP 4

**Action:** Execute finalization activities

**Description:** Execution phase

**Input:** Required artifacts from previous phase

**Output:** Validated artifacts for next phase

Communication: Document progress and blockers

Evidence: Track artifacts and validation results in `.artifacts/protocol-03/workflow-logs/`

**Duration:** Varies based on complexity

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 4 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to supervisor

### Workflow State Management

- State stored in: `.artifacts/protocol-03/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-03/workflow-status.json`
- Execution logs: `.artifacts/protocol-03/workflow-logs/`
- Performance metrics: `.artifacts/protocol-03/workflow-metrics.json`


---
## EVIDENCE SUMMARY
<!-- [Category: GUIDELINES-FORMATS] -->

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| project-brief-validation-report.json | Validation score ≥0.95, discrepancy metric ≤1 | `.artifacts/protocol-03/project-brief-validation-report.json` | Gate 1 discovery verification |
| PROJECT-BRIEF.md | Section coverage metric = 100%, glossary completeness metric = pass | `.artifacts/protocol-03/PROJECT-BRIEF.md` | Gate 2 structural integrity |
| traceability-map.json | Traceability link count metric ≥ all major sections, dependency metric = pass | `.artifacts/protocol-03/traceability-map.json` | Gate 2 structural integrity |
| BRIEF-APPROVAL-RECORD.json | Approval latency metric ≤48h, reminder metric ≤2 | `.artifacts/protocol-03/BRIEF-APPROVAL-RECORD.json` | Gate 3 approval compliance |
| technical-baseline.json | Architecture coverage metric ≥90%, risk flag metric documented | `.artifacts/protocol-03/technical-baseline.json` | Gate 4 handoff integrity |
| brief-structure-report.json | Structural score metric ≥100%, unresolved section metric = 0 | `.artifacts/protocol-03/brief-structure-report.json` | Gate 2 structural integrity |
| evidence-manifest.json | Artifact count metric = full list, checksum verification metric = pass | `.artifacts/protocol-03/evidence-manifest.json` | Gate 4 handoff integrity |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-03/`  
- **Subdirectories:** `patterns/`, `knowledge-base/`, and optional `approvals/` for signed evidence.  
- **Permissions:** Read/write for protocol executor and solutions architect, read-only for downstream protocols and governance.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `PROJECT-BRIEF.md`, `brief-structure-report.json`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-03/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash for every artifact and validator log.  
- Size: File size in bytes recorded in manifest `integrity` block.  
- Dependencies: Upstream sources listed with protocol references and downstream consumers.  

**Dependency Tracking:**
- Input: `.artifacts/protocol-02/` discovery assets, Protocol 01 proposal context, template registry metadata.  
- Output: All artifacts in Artifact Generation Table plus `approval-tracker.json`, `handoff-verification.json`.  
- Transformations: Discovery validation → Brief drafting → Structural validation → Approval capture → Handoff packaging.  

**Coverage:** Manifest documents 100% of required artifacts, validators, and approvals with checksum confirmation.

### Traceability

**Input Sources:**
- **Input From:** `.artifacts/protocol-02/client-discovery-form.md` – Client-approved requirements baseline.  
- **Input From:** `.artifacts/protocol-02/scope-clarification.md` – Technical constraints feeding architecture sections.  

**Output Artifacts:**
- **Output To:** `PROJECT-BRIEF.md` – Canonical brief for Protocols 04 and 06.  
- **Output To:** `technical-baseline.json` – Architecture summary consumed by Protocol 06.  
- **Output To:** `context-summary.md` – Quick reference digest for stakeholders.  
- **Output To:** `BRIEF-APPROVAL-RECORD.json` – Legal evidence of approvals.  
- **Output To:** `evidence-manifest.json` – Comprehensive audit ledger.  

**Transformation Steps:**
1. Discovery evidence → project-brief-validation-report.json: Validate completeness metrics.  
2. Validated inputs → PROJECT-BRIEF.md: Assemble structured narrative with traceability markers.  
3. Brief content → traceability-map.json: Generate linkage map from sections to sources.  
4. Brief + approvals → BRIEF-APPROVAL-RECORD.json: Capture sign-off metadata.  
5. Full bundle → evidence-manifest.json: Aggregate artifacts, metrics, and checksums.  

**Audit Trail:**
- Manifest logs timestamps, checksum hashes, and verification owners for every artifact.  
- Approval tracker retains notification history and escalation records.  
- Handoff verification records downstream requirements and validation outcomes.  
- Execution log captures script outputs and validation decisions.

### Archival Strategy

**Compression:**
- Artifacts compressed into `.artifacts/protocol-03/evidence-bundle.zip` after approval completion and Protocol 04 acknowledgment.  
- Compression uses ZIP with AES-256 option when enabled to protect client data.  

**Retention Policy:**
- Active artifacts retained for 180 days post-brief approval to support revisions.  
- Archived bundles retained for 5 years to satisfy ISO 9001 and client contract retention clauses.  
- Cleanup automation runs quarterly; retention exceptions logged for regulated industries.  

**Retrieval Procedures:**
- Active artifacts accessed directly with manifest cross-check before modification.  
- Archived bundles restored from `evidence-bundle.zip`; verify checksums before circulation.  
- Governance portal references manifest entries for audit-ready retrieval.  

**Cleanup Process:**
- Quarterly script appends deletion summary to `.artifacts/protocol-03/cleanup-log.json` with checksum snapshot.  
- Critical artifacts flagged `extended_retention: true` remain until legal clearance.  
- Governance officer reviews cleanup log and signs off in `.artifacts/protocol-03/retention-approvals.json`.

---

## 11. REASONING & COGNITIVE PROCESS
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level protocol analysis and reasoning patterns documentation -->

### Reasoning Patterns

#### Primary Reasoning Pattern: Systematic Execution
- Execute protocol steps sequentially with validation at each checkpoint
- Ensure each step builds on validated outputs from previous steps
- Pattern ensures completeness and traceability

#### Secondary Reasoning Pattern: Quality-Driven Validation
- Apply quality gates to ensure artifact completeness before downstream handoff
- Validate both content and structure of deliverables
- Pattern prevents propagation of errors to dependent protocols

#### Pattern Improvement Strategy:
- Track pattern effectiveness via quality gate pass rates and downstream protocol feedback
- Quarterly review identifies pattern weaknesses and optimization opportunities
- Iterate patterns based on empirical evidence from completed executions

### Decision Logic

#### Decision Point 1: Execution Readiness
**Context:** Determining if prerequisites are met to begin protocol execution

**Decision Criteria:**
- All prerequisite artifacts present → Proceed
- Required approvals obtained → Proceed
- System state validated → Proceed
- Any prerequisite missing → Halt

**Outcomes:**
- **Proceed:** Execute protocol workflow starting with Phase 1
- **Halt:** Document missing prerequisites, notify stakeholders, await resolution

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

**Feedback Loop 1: Execution Outcomes**
- **Collection:** Capture outcome data after each protocol execution
- **Analysis:** Identify patterns in successful vs. failed executions
- **Action:** Update protocol templates based on patterns
- **Closure:** Validate improvements in next executions

**Feedback Loop 2: Quality Gate Performance**
- **Collection:** Track gate pass/fail patterns in historical logs
- **Analysis:** Identify consistently failing gates or criteria
- **Action:** Adjust gate thresholds or improve upstream deliverables
- **Closure:** Monitor adjusted gates for improved pass rates

**Feedback Loop 3: Downstream Protocol Feedback**
- **Collection:** Capture issues reported by Protocol 04 and 06
- **Analysis:** Identify gaps in brief content or structure
- **Action:** Enhance brief template or validation criteria
- **Closure:** Verify downstream satisfaction improves

**Feedback Loop 4: Stakeholder Satisfaction**
- **Collection:** Gather feedback from client and internal teams
- **Analysis:** Identify pain points in approval process
- **Action:** Streamline approval workflow or communication
- **Closure:** Measure reduced approval collection time

#### Improvement Tracking
**Purpose:** Systematically track protocol effectiveness improvements over time.

**Metrics Dashboard:** `.artifacts/protocol-03/improvement-metrics.json`
- Brief assembly time trend (target: <4 hours)
- Approval collection time trend (target: <2 days)
- Gate pass rate trends (target: ≥95% each)
- Downstream rework requests (target: <5%)

**Template Evolution Log:** `.artifacts/protocol-03/template-changelog.md`
- Document all protocol template changes
- Include rationale and expected impact
- Track actual vs. expected outcomes

**Effectiveness Measurement:**
- Compare before/after metrics for each improvement
- Validate improvements with statistical significance
- Roll back changes that degrade performance

#### Knowledge Base Integration
**Purpose:** Build and leverage institutional knowledge to accelerate protocol quality.

**Pattern Library:** `.artifacts/protocol-03/patterns/`
- Successful brief structures by project type
- Effective traceability approaches
- Approval collection best practices

**Best Practices:** `.artifacts/protocol-03/best-practices.md`
- Proven approaches for common scenarios
- Tips for accelerating approval collection
- Techniques for comprehensive traceability

**Common Blockers:** `.artifacts/protocol-03/common-blockers.md`
- Typical issues with proven resolutions
- Missing discovery artifact patterns
- Approval delay mitigation strategies

**Industry Templates:** `.templates/briefs/industries/`
- Healthcare project brief template
- FinTech project brief template
- E-commerce project brief template

#### Adaptation Mechanisms
**Purpose:** Enable protocol to automatically adjust based on context and patterns.

**Adaptation 1: Context-Based Templates**
- **Trigger:** Project type identified from discovery artifacts
- **Action:** Select appropriate brief template variant
- **Example:** Healthcare project → Include HIPAA compliance section
- **Benefit:** Reduces manual customization effort

**Adaptation 2: Risk-Based Validation**
- **Trigger:** Project risk score from Protocol 02
- **Action:** Adjust quality gate thresholds
- **Example:** High-risk project → Require 100% coverage vs. 95%
- **Benefit:** Proportional quality assurance

**Adaptation 3: Approval Workflow Optimization**
- **Trigger:** Client communication preferences from Protocol 02
- **Action:** Adapt approval collection method
- **Example:** Async client → Email approval; Sync client → Call approval
- **Benefit:** Faster approval turnaround

**Adaptation 4: Automation Selection**
- **Trigger:** Available tooling and environment
- **Action:** Choose optimal validation approach
- **Example:** CI/CD available → Automated gates; Manual only → Checklists
- **Benefit:** Maximum efficiency with available resources

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

## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=03` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-03/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/03-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-03/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_03.py \
  --protocol 03 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 03` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-03/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 03 \
  --input .artifacts/protocol-03/input/ \
  --output .artifacts/protocol-03/output/ \
  --log-file .artifacts/protocol-03/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 03` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/protocol-03/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_03.py \
  --protocol 03 \
  --artifacts-dir .artifacts/protocol-03/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 03` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/protocol-03/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_03.py \
  --protocol 03 \
  --artifacts-dir .artifacts/protocol-03/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 03` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/protocol-03/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error

### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-03/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-03/execution.log`
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
- `.artifacts/protocol-03/execution.log` - Main execution log
- `.artifacts/protocol-03/validation.log` - Validation log
- `.artifacts/protocol-03/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-03/workflow-status.json` - Real-time status
- `.artifacts/protocol-03/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-03/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-03/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-03-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol 04

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
[PROTOCOL 03 | PHASE X START] - [Action description]
[PROTOCOL 03 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 03 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Brief Creator - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** Technical Lead, Client - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/protocol-03/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders

---