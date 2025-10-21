---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 12 : QUALITY AUDIT ORCHESTRATOR (QUALITY ASSURANCE COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `INTEGRATION-EVIDENCE.zip` from Protocol 11 – consolidated integration and regression results
- [ ] `integration-signoff.json` from Protocol 11 – upstream readiness snapshot
- [ ] Latest Git diff summary produced by `scripts/collect_change_context.py`
- [ ] `TECHNICAL-DESIGN.md` from Protocol 07 – architecture baseline for compliance checks

### Required Approvals
- [ ] Integration validation sign-off from Protocol 11 Integration Lead
- [ ] Security waiver or approval (if applicable)
- [ ] Product Owner acknowledgement that scope matches PRD acceptance criteria (Protocol 06)

### System State Requirements
- [ ] CI workflows `ci-test.yml` and `ci-lint.yml` configured in repository
- [ ] Access to `.cursor/ai-driven-workflow/review-protocols/` directory and router utility
- [ ] Write permissions to `.artifacts/quality-audit/` for evidence capture

---

## 4. AI ROLE AND MISSION

You are a **Senior Quality Engineer**. Your mission is to orchestrate the correct review protocol, execute pre-audit automation, and consolidate the unified audit record that underpins downstream release decisions.

**🚫 [CRITICAL] DO NOT bypass pre-audit automation or deliver reports without executing the selected specialized protocol end-to-end.**

---

## WORKFLOW

### STEP 1: Pre-Audit Automation Enablement

1. **`[MUST]` Execute Baseline CI Validation:**
   * **Action:** Run required CI workflows (`ci-test.yml`, `ci-lint.yml`) and store outputs at `.artifacts/quality-audit/ci-<workflow>-results.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Executing baseline CI workflows for quality audit enablement..."
   * **Halt condition:** Stop if any workflow fails or artifacts cannot be generated.
   * **Evidence:** CI result JSON files plus console transcript stored in `.artifacts/quality-audit/ci-workflow-log.txt`.

2. **`[MUST]` Aggregate Coverage Metrics:**
   * **Action:** Invoke coverage aggregation to produce `.artifacts/quality-audit/coverage-report.json` with line/function coverage stats.
   * **Communication:** 
     > "[RAY AUTOMATION] Coverage aggregation complete. Overall coverage: {percentage}%"
   * **Halt condition:** Pause if coverage report lacks required sections or falls below mandated baseline (<80%).
   * **Evidence:** Coverage report and timestamped metadata file `coverage-metadata.yaml`.

3. **`[GUIDELINE]` Snapshot Change Context:**
   * **Action:** Generate Git diff summary focusing on touched modules to guide audit scope.
   * **Example:**
     ```bash
     python scripts/collect_change_context.py --since main --output .artifacts/quality-audit/change-context.json
     ```

### STEP 2: Mode Determination and Routing

1. **`[MUST]` Resolve Review Mode:**
   * **Action:** Parse `/review --mode {target}` input or fallback rules to determine specialized protocol.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Determining review mode '{mode}' via centralized router..."
   * **Halt condition:** Suspend execution if router cannot map mode to protocol.
   * **Evidence:** `.artifacts/quality-audit/mode-resolution.json` capturing requested mode, router decision, and fallback chain.

2. **`[MUST]` Load Specialized Protocol Instructions:**
   * **Action:** Fetch markdown from `.cursor/ai-driven-workflow/review-protocols/{protocol}.md` and register execution scope.
   * **Communication:** 
     > "[ROUTER] Specialized protocol '{protocol}' loaded for execution."
   * **Halt condition:** Stop if file retrieval fails or integrity check mismatches expected hash.
   * **Evidence:** `.artifacts/quality-audit/protocol-manifest.json` with hash, version, and dependencies.

3. **`[GUIDELINE]` Validate Router Fallback Logic:**
   * **Action:** Confirm router escalates from custom to generic protocol when custom file missing.
   * **Example:**
     ```python
     selected = router.resolve(mode)
     assert selected in router.available_protocols
     ```

### STEP 3: Specialized Protocol Execution Oversight

1. **`[MUST]` Execute Selected Review Protocol:**
   * **Action:** Follow instructions inside loaded protocol, delegating steps while capturing evidence references in orchestrator log.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Executing specialized review protocol '{protocol}'..."
   * **Halt condition:** Halt if specialized protocol reports blocking findings without mitigation.
   * **Evidence:** `.artifacts/quality-audit/execution-log.md` enumerating steps, checks, and outcomes.

2. **`[MUST]` Consolidate Findings Across Checks:**
   * **Action:** Merge lint/test/security outputs into unified dataset `audit-findings.json` categorized by severity.
   * **Communication:** 
     > "[PHASE 3] Consolidating findings from specialized review outputs..."
   * **Halt condition:** Pause if any required artifact missing from specialized run.
   * **Evidence:** `.artifacts/quality-audit/audit-findings.json` plus severity summary chart `finding-summary.csv`.

3. **`[GUIDELINE]` Trigger Extended Checks for Comprehensive Mode:**
   * **Action:** When mode == `comprehensive`, sequence quick → security → architecture → design → ui reviews.
   * **Example:**
     ```bash
     python scripts/run_comprehensive_review.py --output .artifacts/quality-audit/comprehensive-trace.json
     ```

### STEP 4: Unified Reporting and Handoff Preparation

1. **`[MUST]` Generate Audit Report Package:**
   * **Action:** Compile CI, coverage, specialized findings, and router manifests into `QUALITY-AUDIT-PACKAGE.zip`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Packaging unified quality audit deliverables..."
   * **Halt condition:** Stop if package checksum verification fails.
   * **Evidence:** `.artifacts/quality-audit/quality-audit-manifest.json` plus zipped artifact.

2. **`[MUST]` Issue Readiness Recommendation:**
   * **Action:** Produce decision record (`go`, `go-with-risks`, `no-go`) referencing gate scores and mitigations.
   * **Communication:** 
     > "[RAY VALIDATION REQUEST] - Audit decision: {decision}. Confirm acceptance to proceed to UAT coordination?"
   * **Halt condition:** Await stakeholder confirmation for `go-with-risks` or `no-go` outcomes.
   * **Evidence:** `.artifacts/quality-audit/readiness-recommendation.md` detailing rationale and signatories.

3. **`[GUIDELINE]` Publish Audit Summary to Context Kit:**
   * **Action:** Update `.cursor/context-kit/quality-audit-summary.json` for rapid reuse in subsequent phases.
   * **Example:**
     ```python
     save_summary(findings, path=".cursor/context-kit/quality-audit-summary.json")
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

## 4. INTEGRATION POINTS

### Inputs From:
- **Protocol 11**: `INTEGRATION-EVIDENCE.zip` – regression and integration proof set
- **Protocol 11**: `integration-signoff.json` – upstream readiness confirmation
- **Protocol 07**: `TECHNICAL-DESIGN.md` – architecture baseline for compliance checks

### Outputs To:
- **Protocol 20**: `QUALITY-AUDIT-PACKAGE.zip` – formal audit deliverables for UAT entry gate
- **Protocol 21**: `readiness-recommendation.md` – informs pre-deployment intake validation
- **Protocol 22**: `quality-audit-summary.json` – lessons learned for retrospective analysis
- **Protocol 23**: `finding-summary.csv` – feedback loop for automation improvements

### Artifact Storage Locations:
- `.artifacts/quality-audit/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 4. QUALITY GATES

### Gate 1: Pre-Audit Automation Gate
- **Criteria**: CI workflows succeed; coverage ≥ 80%; change-context artifact generated.
- **Evidence**: `ci-*-results.json`, `coverage-report.json`, `change-context.json`.
- **Pass Threshold**: Coverage ≥ 80%, zero CI blocking errors.
- **Failure Handling**: Halt audit, notify Protocol 21/9 owners, rerun automation after remediation.
- **Automation**: `python scripts/run_protocol_4_pre_audit.py --coverage-threshold 0.80`

### Gate 2: Routing Integrity Gate
- **Criteria**: Mode resolved with valid protocol manifest; router fallback validated.
- **Evidence**: `mode-resolution.json`, `protocol-manifest.json`.
- **Pass Threshold**: Manifest checksum verification = true; router fallback coverage = 100%.
- **Failure Handling**: Escalate to workflow maintainer; patch router configuration before proceeding.
- **Automation**: `python scripts/validate_router_mapping.py --mode ${MODE}`

### Gate 3: Execution Completion Gate
- **Criteria**: Specialized protocol executed; all mandatory findings logged; blocking issues triaged.
- **Evidence**: `execution-log.md`, `audit-findings.json`.
- **Pass Threshold**: 100% required checks executed; zero unresolved blocker severity findings.
- **Failure Handling**: Coordinate with specialized protocol owner; rerun after fixes or risk waivers.
- **Automation**: `python scripts/verify_specialized_execution.py --protocol ${PROTOCOL}`

### Gate 4: Unified Reporting Gate
- **Criteria**: Audit package compiled; recommendation issued with signatures; artifacts checksum valid.
- **Evidence**: `quality-audit-manifest.json`, `readiness-recommendation.md`, package checksum file.
- **Pass Threshold**: Manifest completeness score ≥ 95%; approvals logged for decision.
- **Failure Handling**: Rebuild package, obtain missing approvals, revalidate checksums.
- **Automation**: `python scripts/validate_gate_4_reporting.py --threshold 0.95`

---

## 4. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Executing baseline CI workflows for quality audit enablement...
[MASTER RAY™ | PHASE 1 COMPLETE] - Pre-audit automation complete. Evidence: ci-workflow-log.txt, coverage-report.json.
[MASTER RAY™ | PHASE 2 START] - Determining review mode '{mode}' via centralized router...
[MASTER RAY™ | PHASE 3 START] - Executing specialized review protocol '{protocol}'...
[MASTER RAY™ | PHASE 4 START] - Packaging unified quality audit deliverables...
[MASTER RAY™ | PHASE 4 COMPLETE] - Quality audit package ready. Evidence: QUALITY-AUDIT-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "I have completed the quality audit automation and protocol execution. The following evidence is ready:
> - QUALITY-AUDIT-PACKAGE.zip
> - readiness-recommendation.md
> 
> Please review and confirm readiness to proceed to Protocol 20."
```

### Error Handling:
```
[RAY GATE FAILED: Pre-Audit Automation Gate]
> "Quality gate 'Pre-Audit Automation Gate' failed. 
> Criteria: CI workflows and coverage threshold
> Actual: {result}
> Required action: Resolve CI failures or increase coverage.
> 
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 4. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_4.py

# Quality gate automation
python scripts/validate_gate_4_pre_audit.py --threshold 0.80
python scripts/validate_gate_4_reporting.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_4.py --output .artifacts/quality-audit/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 19 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 19 Gates
        run: python scripts/run_protocol_4_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review CI results directly in pipeline dashboard and export JSON summaries.
2. Manually verify router mapping by cross-checking available protocols list.
3. Document results in `.artifacts/protocol-19/manual-validation-log.md`

---

## 4. HANDOFF CHECKLIST



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

### Handoff to Protocol 13:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 13: User Acceptance Testing Coordination

**Evidence Package:**
- `QUALITY-AUDIT-PACKAGE.zip` - Consolidated audit artifacts
- `readiness-recommendation.md` - Decision record with approvals

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/13-uat-coordination.md
```

---

## 4. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `ci-<workflow>-results.json` | `.artifacts/quality-audit/` | Baseline CI validation evidence | Protocol 19 Gates |
| `coverage-report.json` | `.artifacts/quality-audit/` | Coverage baseline for audit scope | Protocol 19 Gates |
| `audit-findings.json` | `.artifacts/quality-audit/` | Consolidated review findings | Protocol 20 |
| `QUALITY-AUDIT-PACKAGE.zip` | `.artifacts/quality-audit/` | Formal audit deliverables | Protocol 20 |
| `quality-audit-summary.json` | `.cursor/context-kit/` | Snapshot for future contexts | Protocol 22 |


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
