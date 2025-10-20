---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 04: PROJECT BOOTSTRAP AND CONTEXT ENGINEERING (GOVERNANCE COMPLIANT)

**Purpose:** Execute PROJECT BOOTSTRAP AND CONTEXT ENGINEERING workflow with quality validation and evidence generation.

**Version**: v2.0.0  
**Phase**: Phase 0: Foundation & Discovery  
**Purpose**: Bootstrap project with context engineering, environment setup, and tooling configuration

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `PROJECT-BRIEF.md` from Protocol 03 (validated project summary)
- [ ] `project-brief-validation-report.json` from Protocol 03 (evidence of alignment)
- [ ] `BRIEF-APPROVAL-RECORD.json` from Protocol 03 (client/internal approvals)

### Required Approvals
- [ ] Delivery lead authorization to bootstrap repository
- [ ] DevOps confirmation that bootstrap environment is isolated from production

### System State Requirements
- [ ] Access to bootstrap scripts under `scripts/`
- [ ] Write permissions to `.cursor/` and `.artifacts/` directories
- [ ] Environment doctor check (`scripts/doctor.py`) returning success

---

## 00. AI ROLE AND MISSION

You are an **AI Codebase Analyst & Context Architect**. Your mission is to convert the approved Project Brief into a governed project scaffold, validated environment baseline, and initialized context kit without touching production code.

**🚫 [CRITICAL] Never modify existing production application code or delete repository assets outside governed directories.**

---

## WORKFLOW

### STEP 1: Brief Intake and Verification

1. **`[MUST]` Validate Project Brief Assets:**
   * **Action:** Run `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-04/brief-validation-report.json` to ensure structure and approvals are intact.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating Project Brief and approval evidence."
   * **Halt condition:** Stop if validation fails or approvals missing.
   * **Evidence:** `.artifacts/protocol-04/brief-validation-report.json`

2. **`[MUST]` Generate Bootstrap Plan (Dry Run):**
   * **Action:** Execute `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --dry-run --yes` to preview scaffold operations.
   * **Communication:** 
     > "Previewing scaffold generation plan and mapping assets."
   * **Evidence:** `.artifacts/protocol-04/bootstrap-dry-run.log`

3. **`[GUIDELINE]` Extract Technical Signals:**
   * **Action:** Produce `technical-baseline.json` summarizing stacks, services, and integration dependencies gleaned from the brief.
   * **Example:**
     ```json
     {
       "frontend": "Next.js",
       "backend": "FastAPI",
       "datastore": "PostgreSQL"
     }
     ```

### STEP 2: Environment and Governance Preparation

1. **`[MUST]` Run Environment Doctor:**
   * **Action:** Execute `python scripts/doctor.py --strict` to confirm toolchain readiness; store output in `.artifacts/protocol-04/environment-report.json`.
   * **Communication:** 
     > "[PHASE 2] - Validating local environment and dependencies."
   * **Halt condition:** Stop if doctor script reports missing dependencies.
   * **Evidence:** `.artifacts/protocol-04/environment-report.json`

2. **`[MUST]` Normalize Governance Rules:**
   * **Action:** Run `python scripts/normalize_project_rules.py --target .cursor/rules/` followed by `python scripts/rules_audit_quick.py --output .artifacts/protocol-04/rule-audit-report.md`.
   * **Communication:** 
     > "Normalizing governance rules and auditing metadata integrity."
   * **Evidence:** `.artifacts/protocol-04/rule-audit-report.md`

3. **`[GUIDELINE]` Snapshot Existing Context Kit:**
   * **Action:** Archive current `.cursor/context-kit/` into `.artifacts/protocol-04/pre-bootstrap-context.zip` for rollback options.
   * **Example:**
     ```bash
     zip -r .artifacts/protocol-04/pre-bootstrap-context.zip .cursor/context-kit/
     ```

### STEP 3: Scaffold Generation and Verification

1. **`[MUST]` Generate Governed Scaffold:**
   * **Action:** Run `python scripts/generate_from_brief.py --brief PROJECT-BRIEF.md --output-root . --in-place --no-subdir --no-cursor-assets --force --yes` to materialize scaffold.
   * **Communication:** 
     > "[PHASE 3] - Generating governed scaffold artifacts."
   * **Halt condition:** Stop if generator exits with non-zero status.
   * **Evidence:** `.artifacts/protocol-04/bootstrap-manifest.json`

2. **`[MUST]` Verify Scaffold Integrity:**
   * **Action:** Execute `python scripts/validate_scaffold.py --manifest .artifacts/protocol-04/bootstrap-manifest.json` to ensure generated assets match registry expectations.
   * **Communication:** 
     > "Validating scaffold integrity and template compliance."
   * **Evidence:** `.artifacts/protocol-04/scaffold-validation-report.json`

3. **`[GUIDELINE]` Inspect Generated Structure:**
   * **Action:** Review directories for completeness, confirm `generator-config.json` accuracy, and document observations in `scaffold-review-notes.md`.
   * **Example:**
     ```markdown
     - ✅ templates/bootstrap/app/ created
     - ✅ generator-config.json includes service mappings
     - ⚠️ Review README auto-generated content with product owner
     ```

### STEP 4: Context Kit Initialization

1. **`[MUST]` Initialize Evidence Manager:**
   * **Action:** Run `python scripts/evidence_manager.py init --path .artifacts/protocol-04/` to establish evidence tracking baseline.
   * **Communication:** 
     > "[PHASE 4] - Initializing evidence tracking and context kit."
   * **Evidence:** `.artifacts/protocol-04/evidence-manifest.json`

2. **`[MUST]` Validate Workflow Integration:**
   * **Action:** Execute `python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-04/workflow-validation-report.json`.
   * **Communication:** 
     > "Running workflow validation to ensure protocol readiness."
   * **Halt condition:** Stop if validation fails and resolve issues.
   * **Evidence:** `.artifacts/protocol-04/workflow-validation-report.json`

3. **`[GUIDELINE]` Update Context Kit Documentation:**
   * **Action:** Document stack summary, governance status, and next steps in `.cursor/context-kit/governance-status.md`.
   * **Example:**
     ```markdown
     ## Bootstrap Summary
     - Stack: Next.js + FastAPI + PostgreSQL
     - Governance: Rules normalized 2024-05-10
     - Next: Protocol 05 legacy alignment
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

## 00. INTEGRATION POINTS

### Inputs From:
- **Protocol 03**: `PROJECT-BRIEF.md`, `project-brief-validation-report.json`, `BRIEF-APPROVAL-RECORD.json` - Authoritative planning inputs.

### Outputs To:
- **Protocol 05**: `.cursor/context-kit/governance-status.md`, `.artifacts/protocol-04/bootstrap-manifest.json` - Legacy bootstrap alignment inputs.
- **Protocol 02**: `.cursor/context-kit/`, `.artifacts/protocol-04/technical-baseline.json` - Task generation context.

### Artifact Storage Locations:
- `.artifacts/protocol-04/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 00. QUALITY GATES

### Gate 1: Brief Validation Gate
- **Criteria**: Project Brief validation report status = PASS and approvals present.
- **Evidence**: `.artifacts/protocol-04/brief-validation-report.json`
- **Pass Threshold**: Validation score ≥ 0.95.
- **Failure Handling**: Request updated brief, remediate missing approvals, rerun validation.
- **Automation**: `python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-04/brief-validation-report.json`

### Gate 2: Environment & Rule Integrity Gate
- **Criteria**: Environment doctor passes and rule audit reports no critical issues.
- **Evidence**: `.artifacts/protocol-04/environment-report.json`, `.artifacts/protocol-04/rule-audit-report.md`
- **Pass Threshold**: Doctor script exit code 0 and audit severity ≤ Medium.
- **Failure Handling**: Remediate missing dependencies or rule errors, document fixes, rerun gate.
- **Automation**: `python scripts/rules_audit_quick.py --output .artifacts/protocol-04/rule-audit-report.md`

### Gate 3: Scaffold Validation Gate
- **Criteria**: Scaffold manifest matches registry, validation report status = PASS.
- **Evidence**: `.artifacts/protocol-04/bootstrap-manifest.json`, `.artifacts/protocol-04/scaffold-validation-report.json`
- **Pass Threshold**: Validator returns compliance ≥ 98%.
- **Failure Handling**: Regenerate scaffold with corrected parameters, rerun validation.
- **Automation**: `python scripts/validate_scaffold.py --manifest .artifacts/protocol-04/bootstrap-manifest.json`

### Gate 4: Context Validation Gate
- **Criteria**: Evidence manager initialized, workflow validation success, governance status updated.
- **Evidence**: `.artifacts/protocol-04/evidence-manifest.json`, `.artifacts/protocol-04/workflow-validation-report.json`, `.cursor/context-kit/governance-status.md`
- **Pass Threshold**: Workflow validator returns `pass` and documentation updated.
- **Failure Handling**: Address validation errors, refresh context kit documentation, rerun gate.
- **Automation**: `python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-04/workflow-validation-report.json`

---

## 00. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Validating Project Brief inputs before bootstrap."
[MASTER RAY™ | PHASE 2 START] - "Preparing environment and governance rules for scaffold generation."
[MASTER RAY™ | PHASE 3 START] - "Generating governed scaffold based on approved brief."
[MASTER RAY™ | PHASE 4 START] - "Initializing context kit and workflow validation."
[PHASE COMPLETE] - "Bootstrap complete; artifacts stored in .artifacts/protocol-04/."
[RAY ERROR] - "Issue encountered during [phase]; see relevant report for remediation details."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Bootstrap operations complete. Evidence available:
> - brief-validation-report.json
> - environment-report.json
> - bootstrap-manifest.json
> - workflow-validation-report.json
>
> Confirm readiness to activate Protocol 05: Bootstrap Your Project (Legacy Alignment)."
```

### Error Handling:
```
[RAY GATE FAILED: Environment & Rule Integrity]
> "Quality gate 'Environment & Rule Integrity' failed.
> Criteria: doctor.py success and rule audit without critical issues.
> Actual: Missing Docker installation detected.
> Required action: Install Docker, rerun doctor.py, update environment-report.json.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 00. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_00.py

# Quality gate automation
python scripts/validate_brief.py --path PROJECT-BRIEF.md --output .artifacts/protocol-04/brief-validation-report.json
python scripts/rules_audit_quick.py --output .artifacts/protocol-04/rule-audit-report.md
python scripts/validate_scaffold.py --manifest .artifacts/protocol-04/bootstrap-manifest.json
python scripts/validate_workflows.py --mode bootstrap --output .artifacts/protocol-04/workflow-validation-report.json

# Evidence aggregation
python scripts/aggregate_evidence_00.py --output .artifacts/protocol-04/
```

### CI/CD Integration:
```yaml
name: Protocol 04 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 04 Gates
        run: python scripts/run_protocol_00_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Manually review Project Brief sections and approvals; log observations in `manual-brief-review.md`.
2. Conduct environment checklist using shared spreadsheet; store export in `.artifacts/protocol-04/manual-environment-check.xlsx`.
3. Document manual validation results in `.artifacts/protocol-04/manual-validation-log.md`.

---

## 00. HANDOFF CHECKLIST



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

### Handoff to Protocol 05:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 05: Bootstrap Your Project (Legacy Alignment)

**Evidence Package:**
- `bootstrap-manifest.json` - Record of generated scaffold assets
- `governance-status.md` - Context kit summary for legacy protocol alignment

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/05-bootstrap-your-project.md
```

---

## 00. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `brief-validation-report.json` | `.artifacts/protocol-04/` | Confirmation of brief integrity | Protocol 05 |
| `environment-report.json` | `.artifacts/protocol-04/` | Toolchain validation evidence | Protocol 05 |
| `bootstrap-manifest.json` | `.artifacts/protocol-04/` | Generated scaffold inventory | Protocols 0 & 02 |
| `scaffold-validation-report.json` | `.artifacts/protocol-04/` | Scaffold compliance verification | Protocol 02 |
| `workflow-validation-report.json` | `.artifacts/protocol-04/` | Context validation evidence | Protocol 05 |


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
