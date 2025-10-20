---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 01: CLIENT PROPOSAL GENERATION (DISCOVERY COMPLIANT)

**Purpose:** Execute CLIENT PROPOSAL GENERATION workflow with quality validation and evidence generation.

**Version**: v2.1.0  
**Phase**: Phase 0: Foundation & Discovery  
**Purpose**: Transform job posts into client-ready proposals through systematic analysis and validation

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `JOB-POST.md` from Protocol 04-client-discovery (source job description)
- [ ] `.cursor/context-kit/project-profile.json` (baseline project profile, if available)

### Required Approvals
- [ ] Discovery lead confirmation that the opportunity aligns with service offering

### System State Requirements
- [ ] Access to `scripts/analyze_jobpost.py`, `scripts/tone_mapper.py`, and `scripts/validate_proposal.py`
- [ ] Access to real validation scripts: `scripts/check_hipaa.py`, `scripts/enforce_gates.py`, `scripts/validate_compliance_assets.py`
- [ ] Local environment with JSON processing utilities, markdown renderer, and Python dependencies
- [ ] `gates_config.yaml` configured with real validation thresholds

---

## 01. AI ROLE AND MISSION

You are a **Freelance Solutions Architect**. Your mission is to transform any approved client job post into a truthful, human-centric proposal that demonstrates domain expertise, empathy, and alignment with validated capabilities.

**🚫 [CRITICAL] Never fabricate experience, deliverables, or guarantees beyond what discovery confirmed.**

---

## WORKFLOW

### STEP 1: Discovery Context Intake

1. **`[MUST]` Analyze the Job Post:**
   * **Action:** Parse `JOB-POST.md` to extract objectives, deliverables, tone signals, risks, and key terms; store structured data in `.artifacts/protocol-01/jobpost-analysis.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Analyzing client opportunity to capture goals, tone, and success criteria."
   * **Halt condition:** Stop and request clarification if the job post is missing, empty, or fails parsing.
   * **Evidence:** `.artifacts/protocol-01/jobpost-analysis.json`

2. **`[GUIDELINE]` Review Existing Discovery Notes:**
   * **Action:** Cross-reference `.cursor/context-kit/project-profile.json` for prior engagements, preferred tooling, and risk flags.
   * **Example:**
     ```json
     {
       "client_preferences": ["async updates", "weekly demos"],
       "prior_stack": ["Next.js", "PostgreSQL"]
     }
     ```

### STEP 2: Tone and Strategy Mapping

1. **`[MUST]` Classify Tone and Proposal Strategy:**
   * **Action:** Run tone detection on the job analysis to determine communication style (e.g., technical, executive, urgent) and select matching proposal framing heuristics.
   * **Communication:** 
     > "[PHASE 2] - Mapping client tone and aligning delivery strategy for authenticity."
   * **Halt condition:** Pause if tone confidence < 0.8 and await manual classification.
   * **Evidence:** `.artifacts/protocol-01/tone-map.json`

2. **`[GUIDELINE]` Curate Differentiators:**
   * **Action:** Identify 2-3 validated strengths relevant to the client scenario (case studies, reusable assets, domain familiarity) using discovery notes.
   * **Example:**
     ```markdown
     - Delivered HIPAA-compliant data pipeline in 6 weeks (similar compliance scope).
     - Existing CI/CD accelerators reduce initial setup by 40%.
     ```

### STEP 3: Proposal Drafting and Humanization

1. **`[MUST]` Generate Structured Proposal Draft:**
   * **Action:** Author `PROPOSAL.md` with sections: Greeting, Understanding, Proposed Approach, Deliverables & Timeline, Collaboration Model, Next Steps.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Drafting proposal with aligned scope and collaboration plan."
   * **Halt condition:** Pause if any required section lacks content or conflicts with confirmed capabilities.
   * **Evidence:** `.artifacts/protocol-01/PROPOSAL.md`

2. **`[MUST]` Apply Humanization Filters:**
   * **Action:** Inject narrative variation, empathetic acknowledgements, and paraphrased client language to avoid robotic tone.
   * **Communication:** 
     > "[RAY AUTOMATION] - Applying humanization filters and empathy checkpoints."
   * **Evidence:** `.artifacts/protocol-01/humanization-log.json`

3. **`[GUIDELINE]` Include Optional Value Adds:**
   * **Action:** Add optional call-to-action elements such as complimentary discovery workshop or roadmap sketch when allowed by capability matrix.
   * **Example:**
     ```markdown
     ### Optional Discovery Workshop
     - Outcome: Align backlog to business KPIs
     - Duration: 90 minutes (no-charge)
     ```

### STEP 4: Validation and Approval Prep

1. **`[MUST]` Execute Proposal Validation Suite:**
   * **Action:** Verify grammar, factual accuracy, empathy token coverage, and readability ≥ 90%; ensure differentiators trace back to verified evidence.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Running proposal validation to confirm clarity and authenticity."
   * **Halt condition:** Await reviewer confirmation if validation highlights discrepancies.
   * **Evidence:** `.artifacts/protocol-01/proposal-validation-report.json`

2. **`[GUIDELINE]` Prepare Reviewer Summary:**
   * **Action:** Summarize major proposal choices, risks, and pending client questions in `.artifacts/protocol-01/reviewer-brief.md`.
   * **Example:**
     ```markdown
     **Key Decisions**
     - Proposed phased MVP delivery (4 weeks)
     - Highlighted reusable analytics accelerator
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
- **Protocol 04**: `JOB-POST.md` - Source description and requirements for the opportunity.
- **Protocol 02**: `discovery-brief.md` - Prior discovery intelligence and capability confirmation.

### Outputs To:
- **Protocol 02**: `PROPOSAL.md` - Primary proposal delivered for client outreach.
- **Protocol 03**: `proposal-summary.json` - Structured highlights feeding project brief creation.

### Artifact Storage Locations:
- `.artifacts/protocol-01/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 01. QUALITY GATES

### Industry Standards & Compliance
- **CommonMark**: v0.30 (Markdown formatting)
- **JSON Schema**: draft-07 (Artifact validation)
- **Security**: HIPAA compliance for client data handling
- **Regulatory**: FTC truth-in-advertising guidelines

### Gate 1: Job Post Intake Validation
- **Criteria**: `jobpost-analysis.json` captures objectives, deliverables, tone signals, and risk notes.
- **Evidence**: `.artifacts/protocol-01/jobpost-analysis.json`
- **Pass Threshold**: Completeness score ≥ 0.9 from analyzer script.
- **Failure Handling**: Request clarified job information, rerun analysis, document issue in reviewer brief.
- **Automation**: `python3 scripts/analyze_jobpost.py --input JOB-POST.md --output .artifacts/protocol-01/jobpost-analysis.json`

### Gate 2: Tone Strategy Confidence
- **Criteria**: Tone classification confidence ≥ 0.8 with mapped strategy labels.
- **Evidence**: `.artifacts/protocol-01/tone-map.json`
- **Pass Threshold**: `confidence` field ≥ 0.8 and `strategy` populated.
- **Failure Handling**: Perform manual tone review with stakeholder, update tone map, rerun gate.
- **Automation**: `python3 scripts/tone_mapper.py --input .artifacts/protocol-01/jobpost-analysis.json --output .artifacts/protocol-01/tone-map.json`

### Gate 3: Proposal Structure Integrity
- **Criteria**: `PROPOSAL.md` includes all mandatory sections with ≥ 120 words each and empathy tokens logged.
- **Evidence**: `.artifacts/protocol-01/PROPOSAL.md`, `.artifacts/protocol-01/humanization-log.json`
- **Pass Threshold**: Structure validator score ≥ 0.95.
- **Failure Handling**: Revise missing sections, re-run humanization, revalidate.
- **Automation**: `python3 scripts/validate_proposal_structure.py --input .artifacts/protocol-01/PROPOSAL.md`

### Gate 4: Real Compliance Validation
- **Criteria**: HIPAA compliance check passes, quality gates enforce real thresholds.
- **Evidence**: `.artifacts/protocol-01/compliance-validation-report.json`
- **Pass Threshold**: All compliance checks pass (exit code 0).
- **Failure Handling**: Address compliance issues, fix PHI violations, update security configurations.
- **Automation**: `python3 scripts/check_hipaa.py && python3 scripts/enforce_gates.py`

### Gate 5: Final Validation & Approval Readiness
- **Criteria**: Readability ≥ 90, zero factual discrepancies, empathy coverage ≥ 3 tokens, real validation passed.
- **Evidence**: `.artifacts/protocol-01/proposal-validation-report.json`
- **Pass Threshold**: Validation script returns status `pass` and all real gates pass.
- **Failure Handling**: Address flagged items, capture remediation notes, rerun validation.
- **Automation**: `python3 scripts/validate_proposal.py --input .artifacts/protocol-01/PROPOSAL.md --report .artifacts/protocol-01/proposal-validation-report.json`

---

## 01. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Starting discovery intake: parsing JOB-POST.md for goals, tone, and risks."
[MASTER RAY™ | PHASE 2 START] - "Tone classification underway; aligning proposal strategy with client expectations."
[MASTER RAY™ | PHASE 3 START] - "Drafting proposal with validated differentiators and collaboration plan."
[MASTER RAY™ | PHASE 4 START] - "Running validation suite on proposal content and tone."
[PHASE COMPLETE] - "Proposal ready for review. Evidence stored in .artifacts/protocol-01/."
[RAY ERROR] - "Encountered issue during [phase]. Details logged in reviewer brief."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "I have completed proposal drafting and validation. Evidence ready for review:
> - jobpost-analysis.json
> - tone-map.json
> - PROPOSAL.md
> - proposal-validation-report.json
>
> Please confirm readiness to proceed to Protocol 02: Client Discovery Initiation."
```

### Error Handling:
```
[RAY GATE FAILED: Job Post Intake Validation]
> "Quality gate 'Job Post Intake Validation' failed.
> Criteria: Objectives and tone not fully captured.
> Actual: Missing deliverables section in analysis.
> Required action: Obtain clarified job post, rerun analysis.
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
python3 scripts/validate_prerequisites_01.py

# Real compliance validation
python3 scripts/check_hipaa.py
python3 scripts/enforce_gates.py
python3 scripts/validate_compliance_assets.py

# Quality gate automation
python3 scripts/validate_proposal_structure.py --input .artifacts/protocol-01/PROPOSAL.md
python3 scripts/validate_proposal.py --input .artifacts/protocol-01/PROPOSAL.md --report .artifacts/protocol-01/proposal-validation-report.json

# Evidence aggregation
python3 scripts/aggregate_evidence_01.py --output .artifacts/protocol-01/
```

### CI/CD Integration:
```yaml
name: Protocol 01 Real Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Real Compliance Checks
        run: |
          python3 scripts/check_hipaa.py
          python3 scripts/enforce_gates.py
          python3 scripts/validate_compliance_assets.py
      
      - name: Run Protocol 01 Gates
        run: python3 scripts/run_protocol_01_gates.py
      
      - name: Generate Real Validation Report
        run: |
          python3 scripts/analyze_jobpost.py JOB-POST.md .artifacts/protocol-01/jobpost-analysis.json
          python3 scripts/tone_mapper.py .artifacts/protocol-01/jobpost-analysis.json .artifacts/protocol-01/tone-map.json
          python3 scripts/validate_proposal.py .artifacts/protocol-01/PROPOSAL.md .artifacts/protocol-01/proposal-validation-report.json
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Manually review `JOB-POST.md` and document findings in `manual-jobpost-review.md`.
2. Conduct peer review of proposal tone and accuracy; record results in `manual-tone-checklist.md`.
3. Document outcomes in `.artifacts/protocol-01/manual-validation-log.md`.

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

### Handoff to Protocol 02:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 02: Client Discovery Initiation

**Evidence Package:**
- `PROPOSAL.md` - Finalized client-ready proposal
- `proposal-summary.json` - Structured highlights for downstream consumption

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md
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
| `jobpost-analysis.json` | `.artifacts/protocol-01/` | Parsed objectives, tone, risks | Protocol 02 |
| `tone-map.json` | `.artifacts/protocol-01/` | Tone classification & strategy mapping | Protocol 02 |
| `PROPOSAL.md` | `.artifacts/protocol-01/` | Client-facing proposal | Protocol 02 |
| `proposal-summary.json` | `.artifacts/protocol-01/` | Key highlights for brief creation | Protocol 03 |
| `proposal-validation-report.json` | `.artifacts/protocol-01/` | Validation evidence | Protocol 02 |

### Quality Metrics:
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Gate 1 Pass Rate | ≥ 90% | [TBD] | ⏳ |
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
