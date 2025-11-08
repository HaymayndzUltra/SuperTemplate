---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 21 : CONTINUOUS MAINTENANCE & SUPPORT PLANNING (SERVICE RELIABILITY COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `CLOSURE-PACKAGE.zip` from Protocol 20 – curated operational handover assets
- [ ] `operational-handover-record.json` from Protocol 20 – ownership assignments and SLAs
- [ ] `knowledge-transfer-feedback.json` from Protocol 19 – open knowledge gaps and follow-ups
- [ ] `OBSERVABILITY-BASELINE.md` from Protocol 19 – monitoring dashboards and alert thresholds
- [ ] `INCIDENT-POSTMORTEMS/` from Protocol 17 – outstanding corrective actions (if available)
- [ ] `PERFORMANCE-IMPROVEMENT-BACKLOG.json` (initialize as empty template) – optimization work queue to be populated
- [ ] `TECH-DEBT-REGISTER.md` from Protocol 10 – backlog of technical debt items identified during development
- [ ] `SECURITY-RISK-LOG.csv` from Security Review – active security obligations
- [ ] `SERVICE-CATALOG.xlsx` from Operations – service inventory and dependencies

### Required Approvals
- [ ] Operations Director endorsement of maintenance planning scope
- [ ] Support Lead confirmation of staffing and coverage model
- [ ] Product Owner acknowledgement of ongoing enhancement priorities
- [ ] Security Lead approval of remediation commitments

### System State Requirements
- [ ] Access to monitoring, ticketing, and knowledge base platforms
- [ ] Support tooling configured for escalation paths and runbook references
- [ ] Service level objective dashboards accessible for ongoing measurement

---

## 18. AI ROLE AND MISSION

You are a **Maintenance & Support Planner**. Your mission is to translate project closure outputs into a living maintenance program that safeguards reliability, responsiveness, and continuous improvement across the product lifecycle.

**🚫 [CRITICAL] DO NOT finalize the maintenance plan without explicit commitments for every critical incident follow-up, SLA target, and optimization backlog item.**

---

## WORKFLOW

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase one evaluates operational readiness with direct evidence capture and linear halt checks. -->
### PHASE 1: Intake & Operational Readiness Assessment

1. **`[MUST]` Validate Handover Completeness:**
   * **Action:** Inspect handover package, ownership records, and knowledge gaps to confirm operational readiness.
   * **Communication:**
     > "[MASTER RAY™ | PHASE 1 START] - Reviewing handover package and operational assignments for maintenance planning..."
   * **Halt Condition:** Stop if any critical artifact missing or ownership assignment unclear.
   * **Evidence:** `.artifacts/protocol-21/handover-validation-report.json` summarizing completeness checks.

2. **`[MUST]` Assess Operational Baselines:**
   * **Action:** Review observability baselines, SLA metrics, and incident history to identify risk areas.
   * **Communication:**
     > "[PHASE 1] Assessing operational baselines and historic incidents..."
   * **Halt Condition:** Pause if baseline metrics unavailable or outdated.
   * **Evidence:** `.artifacts/protocol-21/operational-baseline-analysis.md` with findings.

3. **`[GUIDELINE]` Align Support Model with Demand Forecast:**
   * **Action:** Estimate ticket volume, coverage requirements, and staffing rotation using historic data.
   * **Reference Example:**
     ```python
     from maintenance.forecast import forecast_ticket_volume
     forecast_ticket_volume(input_path=".artifacts/protocol-21/ticket-history.csv",
                            output_path=".artifacts/protocol-21/support-coverage-plan.json")
     ```

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase two consolidates and prioritizes backlog workstreams through sequential execution steps. -->
### PHASE 2: Maintenance Backlog Formation & Prioritization

1. **`[MUST]` Consolidate Maintenance Backlog:**
   * **Action:** Merge technical debt, incident remediation, security risks, and performance backlog into a unified tracker.
   * **Communication:**
     > "[MASTER RAY™ | PHASE 2 START] - Consolidating maintenance backlog from cross-protocol sources..."
   * **Halt Condition:** Halt if backlog items lack ownership or severity ratings.
   * **Evidence:** `.artifacts/protocol-21/maintenance-backlog.csv` with priority, owner, due date.

2. **`[MUST]` Prioritize Remediation & Enhancement Streams:**
   * **Action:** Apply risk, impact, and effort scoring to backlog items; align with SLA and compliance requirements.
   * **Communication:**
     > "[PHASE 2] Prioritizing maintenance items based on risk and business impact..."
   * **Halt Condition:** Pause if prioritization conflicts unresolved with stakeholders.
   * **Evidence:** `.artifacts/protocol-21/backlog-prioritization-matrix.json` with scoring rationale.

3. **`[GUIDELINE]` Establish Automation Opportunities:**
   * **Action:** Identify tasks suitable for runbook automation or self-healing workflows.
   * **Reference Example:**
     ```bash
     python scripts/discover_automation_candidates.py --input .artifacts/protocol-21/maintenance-backlog.csv \
       --output .artifacts/protocol-21/automation-candidates.json
     ```

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase three finalizes governance deliverables with straightforward approval checkpoints. -->
### PHASE 3: Maintenance Plan Finalization & Governance Setup

1. **`[MUST]` Draft Maintenance & Support Plan:**
   * **Action:** Document maintenance cadence, release windows, escalation matrix, and KPI reporting structure.
   * **Communication:**
     > "[MASTER RAY™ | PHASE 3 START] - Drafting maintenance plan and aligning governance cadence..."
   * **Halt Condition:** Stop if plan lacks coverage for critical services or SLAs.
   * **Evidence:** `.artifacts/protocol-21/maintenance-plan.md` with sections for cadence, responsibilities, governance.

2. **`[MUST]` Secure Stakeholder Approvals:**
   * **Action:** Review plan with operations, support, product, and security leads; capture approvals and adjustments.
   * **Communication:**
     > "[PHASE 3] Presenting maintenance plan for stakeholder approval..."
   * **Halt Condition:** Pause if any stakeholder rejects or defers approval.
   * **Evidence:** `.artifacts/protocol-21/approval-log.csv` documenting approvals, conditions, and dates.

3. **`[GUIDELINE]` Configure Monitoring & Reporting Cadence:**
   * **Action:** Schedule KPI reviews, set up dashboards, and document reporting templates.
   * **Reference Example:**
     ```yaml
     kpi_reviews:
       - metric: "Mean Time to Resolution"
         cadence: "Weekly"
         owner: "Support Lead"
       - metric: "Error Budget Consumption"
         cadence: "Monthly"
         owner: "SRE Manager"
     ```

---


<!-- [Category: META-FORMATS - RETROSPECTIVE SYNTHESIS] -->
<!-- Why: Provides structured learning capture guidance following maintenance planning execution. -->
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

<!-- [Category: GUIDELINES-FORMATS - INTEGRATION MAPPING] -->
<!-- Why: Outlines cross-protocol dependencies and deliverable routing for maintenance planning. -->
## 18. INTEGRATION POINTS

### Inputs From:
- **Protocol 20**: `CLOSURE-PACKAGE.zip`, `operational-handover-record.json` – transition evidence and ownership
- **Protocol 19**: `knowledge-transfer-feedback.json` – outstanding knowledge gaps
- **Protocol 19**: `OBSERVABILITY-BASELINE.md` – monitoring metrics baseline
- **Protocol 20**: `INCIDENT-POSTMORTEMS/` – remediation commitments
- **Protocol 21**: `PERFORMANCE-IMPROVEMENT-BACKLOG.json` – performance tasks
- **Protocol 21**: `TECH-DEBT-REGISTER.md` – technical debt items
- **Security Review Protocol**: `SECURITY-RISK-LOG.csv` – security tasks and deadlines

### Outputs To:
- **Protocol 22**: `maintenance-lessons-input.md` – maintenance insights for retrospective
- **Operational Teams**: `maintenance-plan.md` – ongoing support playbook
- **Protocol 23**: `automation-candidates.json` – inputs for script governance updates

### Artifact Storage Locations:
- `.artifacts/protocol-21/` – Primary evidence storage
- `.cursor/context-kit/` – Context and configuration artifacts

---

<!-- [Category: GUIDELINES-FORMATS - QUALITY CONTROL] -->
<!-- Why: Establishes validation criteria, automation hooks, and remediation steps. -->
## 18. QUALITY GATES

### Gate 1: Maintenance Backlog Integrity
**Type:** Prerequisite  
**Purpose:** Verify 100% of critical backlog items captured with owner, priority, and due date.

**Pass Criteria:**
- **Threshold:** Critical item coverage metric =100% and assignment completeness metric =100%.  
- **Boolean Check:** `backlog_audit.all_critical_assigned = true` and `due_dates.status = complete`.  
- **Metrics:** Critical item count metric, assignment rate metric, due date coverage metric documented in backlog.  
- **Evidence Link:** `.artifacts/protocol-21/maintenance-backlog.csv`, `.artifacts/protocol-21/backlog-audit-report.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_21_backlog.py --input .artifacts/protocol-21/maintenance-backlog.csv --output .artifacts/protocol-21/backlog-validation.json`
- Script: `python3 scripts/verify_backlog_assignments.py --output .artifacts/protocol-21/assignment-verification.json`
- CI Integration: `protocol-21-backlog.yml` workflow validates backlog integrity on maintenance planning; runs-on ubuntu-latest.
- Config: `config/protocol_gates/21.yaml` defines critical item thresholds and assignment requirements.

**Failure Handling:**
- **Rollback:** Escalate missing assignments, update backlog, rerun gate before approval.  
- **Notification:** Alert support leadership and maintenance team via Slack when boolean check fails.  
- **Waiver:** Waiver requires support director approval with documented assignment plan in `.artifacts/protocol-21/gate-waivers.json`.

### Gate 2: Stakeholder Approval Confirmation
**Type:** Execution  
**Purpose:** Confirm Operations, Support, Product, and Security leads approve the maintenance plan.

**Pass Criteria:**
- **Threshold:** Stakeholder approval coverage metric =100% and approval latency metric <48h.  
- **Boolean Check:** `approval_log.all_stakeholders_approved = true` and `approval_status = complete`.  
- **Metrics:** Approval count metric, stakeholder coverage metric, approval latency metric captured in log.  
- **Evidence Link:** `.artifacts/protocol-21/approval-log.csv`, `.artifacts/protocol-21/stakeholder-approvals.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_21_approvals.py --log .artifacts/protocol-21/approval-log.csv --output .artifacts/protocol-21/approval-validation.json`
- Script: `python3 scripts/collect_stakeholder_approvals.py --output .artifacts/protocol-21/stakeholder-approvals.json`
- CI Integration: `protocol-21-approvals.yml` workflow collects and validates approvals; runs-on ubuntu-latest.
- Config: `config/protocol_gates/21.yaml` defines required stakeholders and approval thresholds.

**Failure Handling:**
- **Rollback:** Address feedback, revise maintenance plan, reacquire approvals before proceeding.  
- **Notification:** Alert stakeholders and support leadership when boolean check fails.  
- **Waiver:** Not applicable - stakeholder approval mandatory for maintenance plan activation.

### Gate 3: Governance Cadence Activation
**Type:** Completion  
**Purpose:** Ensure reporting cadence scheduled, dashboards configured, and monitoring alerts active.

**Pass Criteria:**
- **Threshold:** Cadence configuration metric =100% and dashboard activation metric =100%.  
- **Boolean Check:** `governance_cadence.status = activated` and `dashboards.status = configured`.  
- **Metrics:** Schedule count metric, dashboard count metric, alert count metric logged in checklist.  
- **Evidence Link:** `.artifacts/protocol-21/governance-cadence-checklist.json`, `.artifacts/protocol-21/dashboard-configuration.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_21_governance.py --checklist .artifacts/protocol-21/governance-cadence-checklist.json --output .artifacts/protocol-21/governance-validation.json`
- Script: `python3 scripts/activate_monitoring_dashboards.py --output .artifacts/protocol-21/dashboard-activation.json`
- CI Integration: `protocol-21-governance.yml` workflow activates governance cadence; runs-on ubuntu-latest.
- Config: `config/protocol_gates/21.yaml` defines cadence schedule and dashboard requirements.

**Failure Handling:**
- **Rollback:** Configure missing dashboards or schedules, activate monitoring alerts, rerun validation.  
- **Notification:** Alert governance team and support leadership when boolean check fails.  
- **Waiver:** Waiver requires support director approval with documented activation plan.

### Compliance Integration
- **Industry Standards:** Maintenance planning aligns with CommonMark documentation, JSON Schema validation, IT service management standards.  
- **Security Requirements:** Maintenance artifacts enforce SOC 2 audit logging, GDPR compliance for maintenance records, secure storage of operational procedures.  
- **Regulatory Compliance:** Maintenance procedures reference FTC transparency requirements, ISO 27001 change management, SLA compliance obligations.  
- **Governance:** Gate thresholds governed via `config/protocol_gates/21.yaml`, synchronized with protocol governance registry and maintenance dashboards.

---

<!-- [Category: GUIDELINES-FORMATS - COMMUNICATION PLAYBOOK] -->
<!-- Why: Defines announcement, validation, and error messaging standards. -->
## COMMUNICATION PROTOCOLS

### Status Announcements
```
[MASTER RAY™ | PHASE 1 START] Beginning maintenance planning intake using closure outputs and operational baselines.
[MASTER RAY™ | PHASE 2 START] Consolidating maintenance backlog from cross-protocol sources.
[MASTER RAY™ | PHASE 3 START] Drafting maintenance plan and aligning governance cadence.
[PHASE COMPLETE] Maintenance plan ready. Artifacts stored in .artifacts/protocol-21/.
```

### User Interaction Prompts

**Confirmation Prompt:**
```
[RAY CONFIRMATION REQUIRED]
"Maintenance & support plan finalized and stakeholder approvals secured. Evidence bundle:
- maintenance-plan.md
- maintenance-lessons-input.md
- approval-log.csv
- maintenance-backlog.csv
Confirm handoff to Protocol 22?"
```

**Clarification Prompt:**
```
[RAY CLARIFICATION NEEDED]
"I detected ambiguity in the requirements regarding '{specific_point}'. Please clarify:
1. [Specific question about maintenance backlog scope]
2. [Specific question about support coverage expectations]
3. [Specific question about approval requirements]

This will help me proceed more accurately."
```

**Decision Point Prompt:**
```
[RAY DECISION REQUIRED]
"Multiple approaches identified for '{topic}'. Please choose:
- Option A: [Description] - Pros: [list], Cons: [list]
- Option B: [Description] - Pros: [list], Cons: [list]
- Option C: [Description] - Pros: [list], Cons: [list]

Which approach should I proceed with?"
```

**Feedback Prompt:**
```
[RAY FEEDBACK REQUESTED]
"Maintenance plan draft complete. Please review and provide feedback on:
1. Completeness and accuracy
2. Quality and alignment with support needs
3. Any adjustments needed before finalization

Your feedback will be incorporated into the final deliverables."
```

### Error Messaging

**Error Severity Levels:**
- **CRITICAL:** Blocks protocol execution; requires immediate user intervention
- **WARNING:** May affect quality but allows continuation; user should review
- **INFO:** Informational only; no action required

**Error Template with Severity:**
```
[RAY GATE FAILED: Maintenance Backlog Integrity] [CRITICAL]
"Quality gate 'Maintenance Backlog Integrity' failed. All critical items must be assigned with due dates before proceeding."
Context: 4 critical items missing owners
Resolution: Assign owners, update backlog, rerun validation
Impact: Blocks handoff until resolved
```

**Error Template with Context:**
```
[RAY VALIDATION ERROR: Stakeholder Approval Confirmation] [WARNING]
"Stakeholder approval missing. Support Lead approval pending."
Context: approval-log.csv shows Support Lead status = Pending
Resolution: Address feedback, revise plan, reacquire approvals
Impact: May affect quality; review recommended before handoff
```

**Error Template with Resolution:**
```
[RAY SCRIPT ERROR: Backlog Consolidation] [INFO]
"Backlog consolidation script incomplete."
Context: Missing artifact checksum for maintenance-backlog.csv
Resolution: Re-run backlog consolidation script
Impact: Minor; backlog will be updated automatically
```

---

## 18. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_21.py

# Quality gate automation
python scripts/validate_gate_21_backlog.py --input .artifacts/protocol-21/maintenance-backlog.csv
python scripts/validate_gate_21_approvals.py --log .artifacts/protocol-21/approval-log.csv
python scripts/validate_gate_21_governance.py --checklist .artifacts/protocol-21/governance-cadence-checklist.json

# Evidence aggregation
python scripts/aggregate_evidence_21.py --output .artifacts/protocol-21/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 21 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 21 Gates
        run: python scripts/run_protocol_18_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review backlog entries with owners during maintenance planning workshop.
2. Confirm approval sign-offs via recorded meeting or email acknowledgement.
3. Document results in `.artifacts/protocol-21/manual-validation-log.md`

---

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Checklist ensures readiness for Protocol 22 with explicit evidence requirements. -->
## 18. HANDOFF CHECKLIST

### Continuous Improvement Validation:
- [x] Execution feedback collected and logged
- [x] Lessons learned documented in protocol artifacts
- [x] Quality metrics captured for improvement tracking
- [x] Knowledge base updated with new patterns or insights
- [x] Protocol adaptation opportunities identified and logged
- [x] Retrospective scheduled (if required for this protocol phase)

### Pre-Handoff Validation:
Before declaring protocol complete, validate:

- [x] All prerequisites were met
- [x] All workflow steps completed successfully
- [x] All quality gates passed (or waivers documented)
- [x] All evidence artifacts captured and stored
- [x] All integration outputs generated
- [x] All automation hooks executed successfully
- [x] Communication log complete

**Stakeholder Sign-Off:**
- **Approvals Required:** Operations Director endorsement of maintenance planning scope, Support Lead confirmation of staffing and coverage model, Product Owner acknowledgement of ongoing enhancement priorities, and Security Lead approval of remediation commitments before proceeding to Protocol 22
- **Reviewers:** Operations Director reviews maintenance planning scope, Support Lead reviews staffing and coverage model, Product Owner reviews enhancement priorities, Security Lead reviews remediation commitments
- **Sign-Off Evidence:** Approvals documented in `.artifacts/protocol-21/reviewer-signoff.json`, reviewer sign-off in `.artifacts/protocol-21/reviewer-signoff.json`
- **Confirmation Required:** Explicit confirmation that maintenance plan is approved, backlog items are prioritized, and Protocol 22 prerequisites satisfied

**Documentation Requirements:**
- **Document Format:** All artifacts in Markdown (`.md`) or JSON (`.json`) format
- **Storage Location:** All documentation stored in `.artifacts/protocol-21/` directory
- **Reviewer Documentation:** Reviewers document approval/rejection rationale in `.artifacts/protocol-21/reviewer-signoff.json`
- **Evidence Manifest:** Complete manifest file at `.artifacts/protocol-21/evidence-manifest.json` with all artifact checksums
- **Documentation Types:** All documentation includes logs, briefs, notes, transcripts, manifests, and reports as required

**Ready-for-Next-Protocol Statement:**
✅ **Protocol 21 COMPLETE - Ready for Protocol 22**

All maintenance backlog consolidated, stakeholder approvals obtained, maintenance plan finalized, and Protocol 22 prerequisites satisfied. Protocol 22 (Implementation Retrospective) can now proceed.

**Next Protocol Command:**
```bash
# Run Protocol 22: Implementation Retrospective
@apply .cursor/ai-driven-workflow/22-implementation-retrospective.md
# Or trigger validation: python3 validators-system/scripts/validate_all_protocols.py --protocol 22 --workspace .
```

**Continuation Instructions:**
After Protocol 21 completion, run Protocol 22 continuation script to proceed. Generate session continuation for Protocol 22 workflow execution. Ensure all handoff checklist items verified and approvals obtained before proceeding.

**Dependencies Satisfied:**
- ✅ Maintenance backlog consolidated and prioritized
- ✅ Maintenance plan approved
- ✅ Evidence bundle complete
- ✅ Quality gates passed
- ✅ Stakeholder sign-off obtained

---

<!-- [Category: META-FORMATS - EVIDENCE INVENTORY] -->
<!-- Why: Aggregates artifacts, traceability, and metrics for audit and governance. -->
## 18. EVIDENCE SUMMARY

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| backlog artifact (`maintenance-backlog.csv`) | Critical item count metric, assignment rate metric =100% | `.artifacts/protocol-21/maintenance-backlog.csv` | Gate 1 backlog integrity |
| backlog-audit artifact (`backlog-audit-report.json`) | Audit completeness metric =100%, priority distribution metric documented | `.artifacts/protocol-21/backlog-audit-report.json` | Gate 1 audit evidence |
| approval-log artifact (`approval-log.csv`) | Approval count metric, stakeholder coverage metric =100% | `.artifacts/protocol-21/approval-log.csv` | Gate 2 approval confirmation |
| stakeholder-approvals artifact (`stakeholder-approvals.json`) | Approval latency metric <48h, approval status metric =complete | `.artifacts/protocol-21/stakeholder-approvals.json` | Gate 2 approval evidence |
| cadence-checklist artifact (`governance-cadence-checklist.json`) | Checklist completion metric =100%, schedule count metric documented | `.artifacts/protocol-21/governance-cadence-checklist.json` | Gate 3 cadence activation |
| dashboard-config artifact (`dashboard-configuration.json`) | Dashboard count metric, alert count metric, configuration status metric logged | `.artifacts/protocol-21/dashboard-configuration.json` | Gate 3 dashboard evidence |
| maintenance-plan artifact (`maintenance-plan.md`) | Plan completeness metric >=95%, strategy coverage metric documented | `.artifacts/protocol-21/maintenance-plan.md` | Gate 3 operational strategy |
| automation-candidates artifact (`automation-candidates.json`) | Candidate count metric, automation potential metric recorded | `.artifacts/protocol-21/automation-candidates.json` | Gate 3 automation opportunities |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-21/`  
- **Subdirectories:** `backlog/` for maintenance items, `approvals/` for stakeholder records, `governance/` for cadence configuration.  
- **Permissions:** Read/write for support leadership and maintenance team, read-only for retrospective and governance teams.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `maintenance-backlog.csv`, `maintenance-plan.md`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-21/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash recorded for every artifact and maintenance record.  
- Size: File size in bytes captured in manifest integrity block.  
- Dependencies: Upstream protocols (20, 19) and downstream consumers (22, 23) documented.

**Dependency Tracking:**
- Input: Protocol 20 `CLOSURE-PACKAGE.zip`, Protocol 19 documentation, operational baseline.  
- Output: All artifacts listed above plus gate validation reports and maintenance evidence bundle.  
- Transformations: Backlog integrity -> Stakeholder approval -> Governance cadence activation.

**Coverage:** Manifest documents 100% of required artifacts, maintenance items, approval records, and governance configuration with checksum verification.

### Traceability

**Input Sources:**
- **Input From:** Protocol 20 `.artifacts/protocol-20/CLOSURE-PACKAGE.zip` – Handover materials and operational baseline.  
- **Input From:** Protocol 19 documentation – Knowledge transfer and operational procedures.  
- **Input From:** Operational baseline `config/operational-baseline.yaml` – Current system state and SLAs.

**Output Artifacts:**
- **Output To:** `maintenance-plan.md` – Operational strategy consumed by Protocol 22 (Retrospective).  
- **Output To:** `automation-candidates.json` – Automation opportunities for Protocol 23 (Governance).  
- **Output To:** `maintenance-lessons-input.md` – Lessons for retrospective analysis and learning.  
- **Output To:** `evidence-manifest.json` – Audit ledger for governance and compliance reviews.

**Transformation Steps:**
1. Backlog audit -> maintenance-backlog.csv and backlog-audit-report.json: Verify critical items and assignments.  
2. Approval collection -> approval-log.csv and stakeholder-approvals.json: Collect and validate stakeholder approvals.  
3. Governance activation -> governance-cadence-checklist.json and dashboard-configuration.json: Activate cadence and dashboards.  
4. Evidence bundling -> maintenance-plan.md and automation-candidates.json: Compile maintenance strategy and identify opportunities.

**Audit Trail:**
- Manifest stores timestamps, checksums, and support leader identity for each artifact.  
- Approval records retain stakeholder signatures and approval timestamps.  
- Backlog items maintain priority assignments and due date confirmations.  
- Governance records document cadence activation and dashboard configuration.

### Archival Strategy

**Compression:**
- Maintenance artifacts compressed into `.artifacts/protocol-21/MAINTENANCE-PLAN-BUNDLE.zip` after Gate 3 completion using ZIP standard compression.

**Retention Policy:**
- Active artifacts retained for 2 years post-activation to support ongoing maintenance operations.  
- Archived bundles retained for 5 years per operational and compliance requirements.  
- Cleanup automation `scripts/cleanup_artifacts.py` enforces retention quarterly.

**Retrieval Procedures:**
- Active artifacts accessed directly from `.artifacts/protocol-21/` with read-only permissions.  
- Archived bundles retrieved via `unzip .artifacts/protocol-21/MAINTENANCE-PLAN-BUNDLE.zip` with manifest checksum verification.  
- Maintenance runbook stored in `governance/maintenance-runbook.md` for operational reference.

**Cleanup Process:**
- Quarterly cleanup logs actions to `.artifacts/protocol-21/cleanup-log.json` with maintenance artifact inventory snapshot.  
- Critical maintenance artifacts flagged for extended retention require support director approval.  
- Manual retention overrides documented with timestamp, approver identity, and business justification.


---

<!-- [Category: META-FORMATS - COGNITIVE EXPLAINABILITY] -->
<!-- Why: Documents reasoning patterns, decision logic, and adaptation strategies. -->
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

## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `validate_gate_21_backlog.py` | Validate Gate 21 Backlog | `scripts/` | ✅ Exists |
| `gate_utils.py` | Gate Utils | `scripts/` | ✅ Exists |
| `validate_gate_21_governance.py` | Validate Gate 21 Governance | `scripts/` | ✅ Exists |
| `validate_gate_21_approvals.py` | Validate Gate 21 Approvals | `scripts/` | ✅ Exists |
| `aggregate_evidence_21.py` | Aggregate Evidence 21 | `scripts/` | ✅ Exists |
| `run_protocol_gates.py` | Run Protocol Gates | `scripts/` | ✅ Exists |

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
| `validate_gate_21_*.py` | Gate validation | `scripts/` | ✅ Exists |
| `verify_protocol_21.py` | Protocol verification | `scripts/` | ✅ Exists |
| `generate_artifacts_21.py` | Artifact generation | `scripts/` | ✅ Exists |
| `aggregate_evidence_21.py` | Evidence aggregation | `scripts/` | ✅ Exists |

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

---

## WORKFLOW ORCHESTRATION

### STEP 1

**Action:** Initialize protocol execution

**Description:** Setup environment and load prerequisites

Communication: Notify stakeholders of protocol start

Evidence: Track initialization in `.artifacts/protocol-21/workflow-logs/`

**Duration:** 15 minutes

---

### STEP 2

**Action:** Execute main protocol activities

**Description:** Perform core protocol tasks and validations

Communication: Document progress and any blockers

Evidence: Store artifacts in `.artifacts/protocol-21/`

**Duration:** Varies based on complexity

---

### STEP 3

**Action:** Validate and package results

**Description:** Run validation scripts and prepare handoff

Communication: Report completion status to stakeholders

Evidence: Generate validation report and evidence manifest

**Duration:** 20 minutes

---

### Workflow Dependencies

- **Sequential:** STEP 1 → STEP 2 → STEP 3 (must complete in order)
- **Parallel:** None (all steps sequential)
- **Conditional:** Halt if validation fails, escalate to supervisor

### Workflow State Management

- State stored in: `.artifacts/protocol-21/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-21/workflow-status.json`
- Execution logs: `.artifacts/protocol-21/workflow-logs/`
- Performance metrics: `.artifacts/protocol-21/workflow-metrics.json`

---

## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=21` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-21/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/21-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-21/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_21.py \
  --protocol 21 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 21` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-21/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 21 \
  --input .artifacts/protocol-21/input/ \
  --output .artifacts/protocol-21/output/ \
  --log-file .artifacts/protocol-21/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 21` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/protocol-21/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_21.py \
  --protocol 21 \
  --artifacts-dir .artifacts/protocol-21/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 21` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/protocol-21/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_21.py \
  --protocol 21 \
  --artifacts-dir .artifacts/protocol-21/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 21` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/protocol-21/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error

### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-21/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-21/execution.log`
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
- `.artifacts/protocol-21/execution.log` - Main execution log
- `.artifacts/protocol-21/validation.log` - Validation log
- `.artifacts/protocol-21/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-21/workflow-status.json` - Real-time status
- `.artifacts/protocol-21/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-21/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-21/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-21-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Clear handoff to Protocol 22

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
[PROTOCOL 21 | PHASE X START] - [Action description]
[PROTOCOL 21 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 21 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Support Lead - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** Support Team, Technical Lead, Client - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/protocol-21/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders

---