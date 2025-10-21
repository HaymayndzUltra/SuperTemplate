---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 23 : SCRIPT GOVERNANCE (AUTOMATION QUALITY COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `.artifacts/quality-audit/QUALITY-AUDIT-PACKAGE.zip` from Protocol 19 – baseline quality expectations
- [ ] `.cursor/context-kit/quality-audit-summary.json` – latest audit findings to align governance focus
- [ ] Existing `script-registry.json` (if present) in `.cursor/context-kit/` – prior inventory snapshot

### Required Approvals
- [ ] Automation owner approval to perform read-only validation on `/scripts/`
- [ ] Security lead acknowledgement for accessing script metadata

### System State Requirements
- [ ] Repository `/scripts/` directory accessible with read permissions
- [ ] Static analysis tools (`pylint`, `shellcheck`, `yamllint`) installed or containerized equivalents configured
- [ ] Write permissions to `.artifacts/scripts/` and `.cursor/context-kit/`

---

## AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Governance Toolkit (Recommended):
```bash
# Validate coverage and generate report
python3 scripts/validate_script_registry.py \
  --output .artifacts/validation/script-registry-report.json \
  --min-coverage 95.0

# Auto-register orphaned scripts (review before applying)
python3 scripts/auto_register_scripts.py --dry-run
python3 scripts/auto_register_scripts.py

# Generate Protocol 23 evidence package
python3 scripts/generate_protocol_23_artifacts.py \
  --registry-report .artifacts/validation/script-registry-report.json
```

### Manual Spot Checks (Fallback):
1. Manually list `/scripts/` directory and compare with `scripts/script-registry.json`.
2. Review documentation and static analysis outputs; record findings in `manual-governance-checklist.md`.
3. Capture remediation items in `.artifacts/scripts/manual-remediation-log.md`.

### Quick Reference:
- **Registry**: `scripts/script-registry.json`
- **Evidence output**: `.artifacts/protocol-23/`
- **Validation report**: `.artifacts/validation/script-registry-report.json`
- **Cursor-independent guide**: `documentation/cursor-independent-guide.md`

---

## 8. AI ROLE AND MISSION

You are an **Automation Compliance Auditor**. Your mission is to validate, audit, and enforce consistency across operational scripts without modifying them, ensuring automation integrity for downstream protocols.

**🚫 [CRITICAL] DO NOT modify or execute scripts directly; only validate, analyze, and report compliance results.**

---

## WORKFLOW

### STEP 1: Script Discovery and Inventory Baseline

1. **`[MUST]` Index Scripts Across Repository:**
   * **Action:** Enumerate `.py`, `.sh`, `.ps1`, and `.yml` files under `/scripts/`, capturing metadata (path, description, last modified).
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Beginning script discovery and indexing..."
   * **Halt condition:** Stop if `/scripts/` directory missing or inaccessible.
   * **Evidence:** `.artifacts/scripts/script-index.json` with completeness score.

2. **`[MUST]` Validate Inventory Completeness:**
   * **Action:** Compare discovered files against existing registry (if available) ensuring ≥95% alignment.
   * **Communication:** 
     > "[PHASE 1] Inventory completeness evaluated. Deviations recorded."
   * **Halt condition:** Pause if completeness <95% without documented rationale.
   * **Evidence:** `.artifacts/scripts/inventory-validation-report.json` summarizing matches and gaps.
   * **Automation:** `python3 scripts/validate_script_registry.py --min-coverage 95.0 --fail-on-orphans`

3. **`[GUIDELINE]` Categorize Scripts by Function:**
   * **Action:** Group scripts into categories (deployment, validation, reporting) for governance insights.
   * **Example:**
     ```python
     categories = classify_scripts(script_index)
     save(categories, ".artifacts/scripts/script-categories.json")
     ```

### STEP 2: Documentation and Static Compliance Checks

1. **`[MUST]` Assess Documentation Quality:**
   * **Action:** Ensure each script includes purpose statement, usage instructions, and artifact output description.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Auditing script documentation completeness..."
   * **Halt condition:** Halt if any critical script lacks documentation.
   * **Evidence:** `.artifacts/scripts/documentation-audit.csv` capturing compliance per script.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

2. **`[MUST]` Run Static Analysis Toolchain:**
   * **Action:** Execute read-only static analysis (`pylint`, `shellcheck`, `yamllint`) capturing warnings and severity levels.
   * **Communication:** 
     > "[RAY AUTOMATION] Executing static analysis suite across script inventory..."
   * **Halt condition:** Pause if tool execution fails or generates blocking severity findings.
   * **Evidence:** `.artifacts/scripts/static-analysis-report.json` aggregated by tool and script.

3. **`[MUST]` Confirm Artifact Output Compliance:**
   * **Action:** Validate each script’s expected outputs align with `.artifacts/` storage conventions and JSON schema rules.
   * **Communication:** 
     > "[PHASE 2] Verifying artifact output compliance and schema adherence..."
   * **Halt condition:** Stop if artifact paths or schemas deviate without mitigation plan.
   * **Evidence:** `.artifacts/scripts/artifact-compliance-report.json` including schema validation results.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

4. **`[GUIDELINE]` Extend Protocol 19 Gates:**
   * **Action:** Map relevant Protocol 19 quality gate expectations to scripts to ensure consistency.
   * **Example:**
     ```markdown
     - Gate Alignment: Pre-Audit Automation → Scripts: run_protocol_4_pre_audit.py
     - Evidence: static-analysis-report.json (severity <= medium)
     ```

### STEP 3: Governance Reporting and Feedback Loop

1. **`[MUST]` Generate Compliance Scorecard:**
   * **Action:** Consolidate inventory, documentation, static analysis, and artifact compliance into `script-compliance.json`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Compiling script governance scorecard for downstream consumers..."
   * **Halt condition:** Pause if data model validation fails.
   * **Evidence:** `.cursor/context-kit/script-compliance.json` with compliance index.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

2. **`[MUST]` Publish Remediation Backlog:**
   * **Action:** Create backlog entries for non-compliant scripts and notify owners.
   * **Communication:** 
     > "[PHASE 3] Script remediation backlog prepared. Owners notified."
   * **Halt condition:** Stop if backlog cannot be linked to issue tracker.
   * **Evidence:** `.artifacts/scripts/remediation-backlog.csv` containing action items.

3. **`[GUIDELINE]` Share Insights with Quality Audit:**
   * **Action:** Provide summary to Protocol 19 to influence upcoming audits.
   * **Example:**
     ```markdown
     ### Script Governance Highlights
     - Coverage: 98% scripts documented
     - Blocking Issues: None
     - Recommendations: Automate schema validation nightly
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

## 8. INTEGRATION POINTS

### Inputs From:
- **Protocol 19**: `quality-audit-summary.json` – establishes baseline quality expectations
- **Protocol 21**: `automation-task-tracker.csv` – links script ownership to tasks

### Outputs To:
- **Protocol 19**: `artifact-compliance-report.json`, `script-compliance.json` – informs future audits
- **Protocol 22**: `remediation-backlog.csv` – retrospective review of automation improvements
- **Protocol 19**: `script-categories.json` – supports monitoring automation classification

### Artifact Storage Locations:
- `.artifacts/scripts/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 8. QUALITY GATES

### Gate 1: Inventory Accuracy Gate
- **Criteria**: All scripts indexed; completeness ≥ 95%; metadata populated.
- **Evidence**: `script-index.json`, `inventory-validation-report.json`.
- **Pass Threshold**: Completeness ≥ 0.95.
- **Failure Handling**: Re-run discovery; resolve permissions; document exceptions.
- **Automation**: `python scripts/validate_gate_8_inventory.py --threshold 0.95`

### Gate 2: Documentation & Static Compliance Gate
- **Criteria**: Documentation coverage ≥ 95%; no blocker severity findings from static analysis.
- **Evidence**: `documentation-audit.csv`, `static-analysis-report.json`.
- **Pass Threshold**: Documentation coverage ≥ 0.95; blocker count = 0.
- **Failure Handling**: Notify script owners; remediate documentation or code issues before proceeding.
- **Automation**: `python scripts/validate_gate_8_static.py --report .artifacts/scripts/static-analysis-report.json`

### Gate 3: Artifact Governance Gate
- **Criteria**: Artifact output paths verified; schema validation success ≥ 98%.
- **Evidence**: `artifact-compliance-report.json`, schema validation logs.
- **Pass Threshold**: Compliance score ≥ 0.98.
- **Failure Handling**: Flag non-compliant scripts; update schemas or script instructions; rerun validation.
- **Automation**: `python scripts/validate_gate_8_artifacts.py --threshold 0.98`

### Gate 4: Governance Reporting Gate
- **Criteria**: Scorecard generated; remediation backlog created; insights shared with Protocol 19.
- **Evidence**: `script-compliance.json`, `remediation-backlog.csv`, governance summary note.
- **Pass Threshold**: Scorecard validation = true; backlog coverage 100% of non-compliant scripts.
- **Failure Handling**: Rebuild scorecard; ensure backlog entries mapped to owners; resend summary.
- **Automation**: `python scripts/validate_gate_8_reporting.py`

---

## 8. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Beginning script discovery and indexing...
[MASTER RAY™ | PHASE 1 COMPLETE] - Inventory baseline captured. Evidence: script-index.json.
[MASTER RAY™ | PHASE 2 START] - Auditing script documentation completeness...
[MASTER RAY™ | PHASE 2 COMPLETE] - Documentation and static analysis results available.
[MASTER RAY™ | PHASE 3 START] - Compiling script governance scorecard for downstream consumers...
[MASTER RAY™ | PHASE 3 COMPLETE] - Governance scorecard delivered. Evidence: script-compliance.json.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Script governance validation is complete.
> - script-compliance.json
> - remediation-backlog.csv
>
> Please review and confirm readiness to inform Protocol 19 and 5."
```

### Error Handling:
```
[RAY GATE FAILED: Documentation & Static Compliance Gate]
> "Quality gate 'Documentation & Static Compliance Gate' failed.
> Criteria: Documentation coverage ≥ 95%, blocker findings = 0
> Actual: {result}
> Required action: Engage script owners to remediate documentation or fix static analysis issues.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 8. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_8.py

# Quality gate automation
python scripts/validate_gate_8_inventory.py --threshold 0.95
python scripts/validate_gate_8_artifacts.py --threshold 0.98

# Evidence aggregation
python scripts/aggregate_evidence_8.py --output .artifacts/scripts/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 23 Validation
on:
  schedule:
    - cron: '0 3 * * 1'
  workflow_dispatch:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 23 Gates
        run: python scripts/run_protocol_8_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual script inventory using `find` command and update spreadsheet.
2. Inspect documentation within scripts and annotate compliance results manually.
3. Document results in `.artifacts/protocol-23/manual-validation-log.md`

---

## 8. HANDOFF CHECKLIST



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

### Handoff to Protocol 12 & 22:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 12: Quality Audit and Protocol 22: Implementation Retrospective

**Evidence Package:**
- `script-compliance.json` - Governance summary for audit alignment
- `remediation-backlog.csv` - Actions for retrospective review

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/12-quality-audit.md
```

---

## 8. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `script-index.json` | `.artifacts/scripts/` | Inventory of automation assets | Protocol 23 Gates |
| `documentation-audit.csv` | `.artifacts/scripts/` | Documentation compliance snapshot | Protocol 23 Gates |
| `static-analysis-report.json` | `.artifacts/scripts/` | Static analysis findings | Protocol 19 |
| `remediation-backlog.csv` | `.artifacts/scripts/` | Follow-up actions | Protocol 22 |
| `script-compliance.json` | `.cursor/context-kit/` | Governance scorecard | Protocol 19 |


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
