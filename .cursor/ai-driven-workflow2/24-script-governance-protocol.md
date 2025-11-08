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

## SCRIPTS & AUTOMATION

### Automation Scripts Referenced
| Script Name | Purpose | Location | Status |
|-------------|---------|----------|--------|
| `validate_gate_23_static.py` | Validate Gate 23 Static | `scripts/` | ✅ Exists |
| `gate_utils.py` | Gate Utils | `scripts/` | ✅ Exists |
| `validate_gate_23_artifacts.py` | Validate Gate 23 Artifacts | `scripts/` | ✅ Exists |
| `aggregate_evidence_23.py` | Aggregate Evidence 23 | `scripts/` | ✅ Exists |
| `run_protocol_gates.py` | Run Protocol Gates | `scripts/` | ✅ Exists |
| `validate_gate_23_inventory.py` | Validate Gate 23 Inventory | `scripts/` | ✅ Exists |
| `validate_gate_23_reporting.py` | Validate Gate 23 Reporting | `scripts/` | ✅ Exists |

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
| `validate_gate_23_*.py` | Gate validation | `scripts/` | ✅ Exists |
| `verify_protocol_23.py` | Protocol verification | `scripts/` | ✅ Exists |
| `generate_artifacts_23.py` | Artifact generation | `scripts/` | ✅ Exists |
| `aggregate_evidence_23.py` | Evidence aggregation | `scripts/` | ✅ Exists |

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

Evidence: Track initialization in `.artifacts/protocol-23/workflow-logs/`

**Duration:** 15 minutes

---

### STEP 2

**Action:** Execute main protocol activities

**Description:** Perform core protocol tasks and validations

Communication: Document progress and any blockers

Evidence: Store artifacts in `.artifacts/protocol-23/`

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

- State stored in: `.artifacts/protocol-23/workflow-state.json`
- Checkpoint validation at each step boundary
- Rollback procedure if step fails: Return to previous step and remediate

### Workflow Monitoring

- Real-time status: `.artifacts/protocol-23/workflow-status.json`
- Execution logs: `.artifacts/protocol-23/workflow-logs/`
- Performance metrics: `.artifacts/protocol-23/workflow-metrics.json`

---

## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All artifacts generated and stored in `.artifacts/protocol-23/`
- [ ] Evidence manifest complete with checksums
- [ ] Quality gates passed (all gates show PASS status)
- [ ] Downstream protocol owner notified and ready
- [ ] No blocking issues or waivers pending

### Handoff Package Contents
- **Evidence Bundle:** `PROTOCOL-23-EVIDENCE.zip` containing:
  - All gate validation reports
  - Artifact inventory and manifest
  - Traceability matrix
  - Archival strategy documentation
- **Readiness Attestation:** Signed-off by protocol owner
- **Next Protocol Brief:** Project completion and closure

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
[PROTOCOL 23 | PHASE X START] - [Action description]
[PROTOCOL 23 | PHASE X COMPLETE] - [Outcome with evidence reference]
[PROTOCOL 23 ERROR] - [Error type and resolution]
```

### Stakeholder Notifications
- **Primary Stakeholder:** Governance Lead - Notification method: [Email/Slack/Meeting]
- **Secondary Stakeholders:** Technical Lead, Security Team, Compliance - Notification method
- **Escalation Path:** [Define who to notify if issues arise]

### Feedback Collection
- Collect feedback from downstream protocol owners
- Document any concerns or improvement suggestions
- Log feedback in `.artifacts/protocol-23/feedback-log.json`

### Communication Cadence
- Daily status updates during execution
- Weekly summary reports to leadership
- Post-completion retrospective with stakeholders

---
## AUTOMATION HOOKS

### Pre-Execution Setup

**Environment Variables:**
- `PROTOCOL_ID=23` - Protocol identifier
- `WORKSPACE_ROOT=.` - Root workspace directory
- `ARTIFACTS_DIR=.artifacts/protocol-23/` - Artifacts storage location
- `LOG_LEVEL=INFO` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)

**Required Permissions:**
- Read access to: `.cursor/ai-driven-workflow/23-*.md`, `.artifacts/`
- Write access to: `.artifacts/protocol-23/`, `scripts/logs/`
- Execute access to: `scripts/validate_*.py`, `scripts/aggregate_*.py`

**System Dependencies:**
- Python 3.8+
- bash/sh shell
- Standard Unix utilities (grep, sed, awk)

### Automation Commands

#### Command 1: Pre-Execution Validation
```bash
python3 scripts/validate_prerequisites_23.py \
  --protocol 23 \
  --workspace . \
  --strict
```
**Flags:**
- `--protocol 23` - Protocol ID to validate
- `--workspace .` - Workspace root directory
- `--strict` - Enforce strict validation

**Output:** `.artifacts/protocol-23/prerequisites-validation.json`
**Exit Codes:** 0=success, 1=validation failed, 2=prerequisites missing

#### Command 2: Protocol Execution
```bash
python3 scripts/run_protocol_gates.py \
  --protocol 23 \
  --input .artifacts/protocol-23/input/ \
  --output .artifacts/protocol-23/output/ \
  --log-file .artifacts/protocol-23/execution.log \
  --error-handling retry
```
**Flags:**
- `--protocol 23` - Protocol ID
- `--input DIR` - Input artifacts directory
- `--output DIR` - Output artifacts directory
- `--log-file FILE` - Execution log file path
- `--error-handling {retry|escalate|halt}` - Error handling strategy

**Output:** `.artifacts/protocol-23/output/`
**Exit Codes:** 0=success, 1=execution error, 2=validation gate failed

#### Command 3: Evidence Aggregation
```bash
python3 scripts/aggregate_evidence_23.py \
  --protocol 23 \
  --artifacts-dir .artifacts/protocol-23/ \
  --output-manifest \
  --checksum sha256
```
**Flags:**
- `--protocol 23` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--output-manifest` - Generate manifest file
- `--checksum {md5|sha256}` - Checksum algorithm

**Output:** `.artifacts/protocol-23/EVIDENCE-MANIFEST.json`
**Exit Codes:** 0=success, 1=aggregation failed

#### Command 4: Post-Execution Validation
```bash
python3 scripts/validate_protocol_23.py \
  --protocol 23 \
  --artifacts-dir .artifacts/protocol-23/ \
  --quality-gates strict \
  --report json
```
**Flags:**
- `--protocol 23` - Protocol ID
- `--artifacts-dir DIR` - Artifacts directory
- `--quality-gates {strict|standard|relaxed}` - Gate strictness
- `--report {json|html|text}` - Report format

**Output:** `.artifacts/protocol-23/validation-report.json`
**Exit Codes:** 0=all gates pass, 1=gate failure, 2=critical error


### Error Handling & Fallback Procedures

**If Command 1 (Prerequisites) Fails:**
1. Check log: `.artifacts/protocol-XX/prerequisites-validation.json`
2. Verify all input artifacts exist
3. Ensure all environment variables are set
4. **Fallback:** Run with `--strict=false`
5. **Escalate:** Notify Protocol Owner if still failing

**If Command 2 (Execution) Fails:**
1. Check log: `.artifacts/protocol-XX/execution.log`
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
- `.artifacts/protocol-23/execution.log` - Main execution log
- `.artifacts/protocol-23/validation.log` - Validation log
- `.artifacts/protocol-23/error.log` - Error log (if any)

**Status Files:**
- `.artifacts/protocol-23/workflow-status.json` - Real-time status
- `.artifacts/protocol-23/workflow-metrics.json` - Performance metrics

**Checkpoints:**
- After prerequisites validation
- After each command execution
- Before handoff to next protocol

### Success Criteria

✅ All commands execute successfully (exit code 0)
✅ All quality gates pass (validation report shows PASS)
✅ Evidence manifest generated and checksums verified
✅ All artifacts stored in `.artifacts/protocol-23/`
✅ No errors in execution, validation, or aggregation logs
✅ Protocol ready for handoff to next protocol

---
## 8. AI ROLE AND MISSION

You are an **Automation Compliance Auditor**. Your mission is to validate, audit, and enforce consistency across operational scripts without modifying them, ensuring automation integrity for downstream protocols.

**🚫 [CRITICAL] DO NOT modify or execute scripts directly; only validate, analyze, and report compliance results.**

---

## WORKFLOW

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase one performs linear discovery and validation steps with explicit halt checks and evidence capture. -->
### PHASE 1: Script Discovery and Inventory Baseline

1. **`[MUST]` Index Scripts Across Repository:**
   * **Action:** Enumerate `.py`, `.sh`, `.ps1`, and `.yml` files under `/scripts/`, capturing metadata (path, description, last modified).
   * **Communication:**
     > "[MASTER RAY™ | PHASE 1 START] - Beginning script discovery and indexing..."
   * **Halt Condition:** Stop if `/scripts/` directory missing or inaccessible.
   * **Evidence:** `.artifacts/scripts/script-index.json` with completeness score.

2. **`[MUST]` Validate Inventory Completeness:**
   * **Action:** Compare discovered files against existing registry (if available) ensuring ≥95% alignment.
   * **Communication:**
     > "[PHASE 1] Inventory completeness evaluated. Deviations recorded."
   * **Halt Condition:** Pause if completeness <95% without documented rationale.
   * **Evidence:** `.artifacts/scripts/inventory-validation-report.json` summarizing matches and gaps.
   * **Automation:** `python3 scripts/validate_script_registry.py --min-coverage 95.0 --fail-on-orphans`

3. **`[GUIDELINE]` Categorize Scripts by Function:**
   * **Action:** Group scripts into categories (deployment, validation, reporting) for governance insights.
   * **Reference Example:**
     ```python
     categories = classify_scripts(script_index)
     save(categories, ".artifacts/scripts/script-categories.json")
     ```

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase two executes sequential compliance checks with straightforward halt conditions. -->
### PHASE 2: Documentation and Static Compliance Checks

1. **`[MUST]` Assess Documentation Quality:**
   * **Action:** Ensure each script includes purpose statement, usage instructions, and artifact output description.
   * **Communication:**
     > "[MASTER RAY™ | PHASE 2 START] - Auditing script documentation completeness..."
   * **Halt Condition:** Halt if any critical script lacks documentation.
   * **Evidence:** `.artifacts/scripts/documentation-audit.csv` capturing compliance per script.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

2. **`[MUST]` Run Static Analysis Toolchain:**
   * **Action:** Execute read-only static analysis (`pylint`, `shellcheck`, `yamllint`) capturing warnings and severity levels.
   * **Communication:**
     > "[RAY AUTOMATION] Executing static analysis suite across script inventory..."
   * **Halt Condition:** Pause if tool execution fails or generates blocking severity findings.
   * **Evidence:** `.artifacts/scripts/static-analysis-report.json` aggregated by tool and script.

3. **`[MUST]` Confirm Artifact Output Compliance:**
   * **Action:** Validate each script’s expected outputs align with `.artifacts/` storage conventions and JSON schema rules.
   * **Communication:**
     > "[PHASE 2] Verifying artifact output compliance and schema adherence..."
   * **Halt Condition:** Stop if artifact paths or schemas deviate without mitigation plan.
   * **Evidence:** `.artifacts/scripts/artifact-compliance-report.json` including schema validation results.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

4. **`[GUIDELINE]` Extend Protocol 19 Gates:**
   * **Action:** Map relevant Protocol 19 quality gate expectations to scripts to ensure consistency.
   * **Reference Example:**
     ```markdown
     - Gate Alignment: Pre-Audit Automation → Scripts: run_protocol_4_pre_audit.py
     - Evidence: static-analysis-report.json (severity <= medium)
     ```

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Phase three consolidates governance reporting with linear tasks and evidence capture. -->
### PHASE 3: Governance Reporting and Feedback Loop

1. **`[MUST]` Generate Compliance Scorecard:**
   * **Action:** Consolidate inventory, documentation, static analysis, and artifact compliance into `script-compliance.json`.
   * **Communication:**
     > "[MASTER RAY™ | PHASE 3 START] - Compiling script governance scorecard for downstream consumers..."
   * **Halt Condition:** Pause if data model validation fails.
   * **Evidence:** `.cursor/context-kit/script-compliance.json` with compliance index.
   * **Automation:** `python3 scripts/generate_protocol_23_artifacts.py --output-dir .artifacts/protocol-23`

2. **`[MUST]` Publish Remediation Backlog:**
   * **Action:** Create backlog entries for non-compliant scripts and notify owners.
   * **Communication:**
     > "[PHASE 3] Script remediation backlog prepared. Owners notified."
   * **Halt Condition:** Stop if backlog cannot be linked to issue tracker.
   * **Evidence:** `.artifacts/scripts/remediation-backlog.csv` containing action items.

3. **`[GUIDELINE]` Share Insights with Quality Audit:**
   * **Action:** Provide summary to Protocol 19 to influence upcoming audits.
   * **Reference Example:**
     ```markdown
     ### Script Governance Highlights
     - Coverage: 98% scripts documented
     - Blocking Issues: None
     - Recommendations: Automate schema validation nightly
     ```

---


<!-- [Category: META-FORMATS - RETROSPECTIVE SYNTHESIS] -->
<!-- Why: Guides post-governance learning capture and improvement tracking. -->
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
<!-- Why: Maps upstream audit inputs and downstream governance outputs. -->
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

<!-- [Category: GUIDELINES-FORMATS - QUALITY CONTROL] -->
<!-- Why: Establishes inventory, compliance, artifact, and reporting gate standards. -->
## 8. QUALITY GATES

### Gate 1: Inventory Accuracy Gate
**Type:** Prerequisite  
**Purpose:** Verify all scripts indexed with completeness ≥0.95 and metadata populated.

**Pass Criteria:**
- **Threshold:** Inventory completeness metric ≥0.95 and metadata coverage metric =100%.  
- **Boolean Check:** `script_index.status = complete` and `metadata.all_populated = true`.  
- **Metrics:** Script count metric, completeness rate metric, metadata coverage metric documented in index.  
- **Evidence Link:** `.artifacts/protocol-23/script-index.json`, `.artifacts/protocol-23/inventory-validation-report.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_23_inventory.py --threshold 0.95 --output .artifacts/protocol-23/inventory-validation.json`
- Script: `python3 scripts/verify_script_metadata.py --output .artifacts/protocol-23/metadata-verification.json`
- CI Integration: `protocol-23-inventory.yml` workflow validates script discovery; runs-on ubuntu-latest.
- Config: `config/protocol_gates/23.yaml` defines inventory completeness and metadata requirements.

**Failure Handling:**
- **Rollback:** Re-run discovery, resolve permissions issues, document exceptions, rerun gate.  
- **Notification:** Alert governance team and script owners via Slack when boolean check fails.  
- **Waiver:** Waiver requires governance lead approval with documented discovery plan in `.artifacts/protocol-23/gate-waivers.json`.

### Gate 2: Documentation & Static Compliance Gate
**Type:** Execution  
**Purpose:** Confirm documentation coverage ≥0.95 and zero blocker-severity findings from static analysis.

**Pass Criteria:**
- **Threshold:** Documentation coverage metric ≥0.95 and blocker finding count =0.  
- **Boolean Check:** `documentation_audit.status = pass` and `static_analysis.blocker_count = 0`.  
- **Metrics:** Documentation rate metric, blocker count metric, warning count metric captured in audit.  
- **Evidence Link:** `.artifacts/protocol-23/documentation-audit.csv`, `.artifacts/protocol-23/static-analysis-report.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_23_static.py --report .artifacts/protocol-23/static-analysis-report.json --output .artifacts/protocol-23/static-validation.json`
- Script: `python3 scripts/audit_script_documentation.py --output .artifacts/protocol-23/documentation-validation.json`
- CI Integration: `protocol-23-compliance.yml` workflow runs static analysis on all scripts; runs-on ubuntu-latest.
- Config: `config/protocol_gates/23.yaml` defines documentation thresholds and blocker severity levels.

**Failure Handling:**
- **Rollback:** Notify script owners, remediate documentation or code issues, rerun validation.  
- **Notification:** Alert development team and governance lead when boolean check fails.  
- **Waiver:** Not applicable - documentation and compliance mandatory for governance.

### Gate 3: Artifact Governance Gate
**Type:** Execution  
**Purpose:** Validate artifact output paths verified and schema validation success ≥0.98.

**Pass Criteria:**
- **Threshold:** Artifact compliance metric ≥0.98 and schema validation success metric ≥0.98.  
- **Boolean Check:** `artifact_compliance.status = pass` and `schema_validation.status = success`.  
- **Metrics:** Compliance score metric, validation pass rate metric, schema adherence metric logged in report.  
- **Evidence Link:** `.artifacts/protocol-23/artifact-compliance-report.json`, `.artifacts/protocol-23/schema-validation-logs.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_23_artifacts.py --threshold 0.98 --output .artifacts/protocol-23/artifact-validation.json`
- Script: `python3 scripts/verify_schema_compliance.py --output .artifacts/protocol-23/schema-validation-logs.json`
- CI Integration: `protocol-23-artifacts.yml` workflow validates artifact compliance; runs-on ubuntu-latest.
- Config: `config/protocol_gates/23.yaml` defines artifact path requirements and schema standards.

**Failure Handling:**
- **Rollback:** Flag non-compliant scripts, update schemas or instructions, rerun validation.  
- **Notification:** Alert script owners and governance lead when boolean check fails.  
- **Waiver:** Waiver requires governance lead approval with documented remediation plan.

### Gate 4: Governance Reporting Gate
**Type:** Completion  
**Purpose:** Ensure scorecard generated, remediation backlog created, and insights shared.

**Pass Criteria:**
- **Threshold:** Scorecard completeness metric =100% and backlog coverage metric =100%.  
- **Boolean Check:** `scorecard.status = generated` and `remediation_backlog.coverage = complete`.  
- **Metrics:** Scorecard item count metric, backlog entry count metric, reporting latency metric documented in report.  
- **Evidence Link:** `.artifacts/protocol-23/script-compliance.json`, `.artifacts/protocol-23/remediation-backlog.csv`.

**Automation:**
- Script: `python3 scripts/validate_gate_23_reporting.py --output .artifacts/protocol-23/reporting-validation.json`
- Script: `python3 scripts/generate_governance_scorecard.py --output .artifacts/protocol-23/script-compliance.json`
- CI Integration: `protocol-23-reporting.yml` workflow generates governance report; runs-on ubuntu-latest.
- Config: `config/protocol_gates/23.yaml` defines scorecard requirements and backlog standards.

**Failure Handling:**
- **Rollback:** Rebuild scorecard, ensure backlog entries mapped to owners, resend summary.  
- **Notification:** Alert governance lead and Protocol 19 owner when boolean check fails.  
- **Waiver:** Not applicable - governance reporting mandatory for compliance.

### Compliance Integration
- **Industry Standards:** Script governance aligns with CommonMark documentation, JSON Schema validation, code governance standards.  
- **Security Requirements:** Governance artifacts enforce SOC 2 audit logging, GDPR compliance for script metadata, secure storage of compliance reports.  
- **Regulatory Compliance:** Script procedures reference FTC transparency requirements, ISO 27001 change management, organizational governance mandates.  
- **Governance:** Gate thresholds governed via `config/protocol_gates/23.yaml`, synchronized with protocol governance registry and compliance dashboards.

---

<!-- [Category: GUIDELINES-FORMATS - COMMUNICATION PLAYBOOK] -->
<!-- Why: Provides messaging templates for governance status, validation, and errors. -->
## COMMUNICATION PROTOCOLS

### Status Announcements
```
[MASTER RAY™ | PHASE 1 START] Beginning script discovery and indexing.
[MASTER RAY™ | PHASE 2 START] Auditing script documentation completeness.
[MASTER RAY™ | PHASE 3 START] Compiling script governance scorecard for downstream consumers.
[PHASE COMPLETE] Script governance complete. Artifacts stored in .artifacts/protocol-23/.
```

### User Interaction Prompts

**Confirmation Prompt:**
```
[RAY CONFIRMATION REQUIRED]
"Script governance validation complete. Evidence bundle:
- script-compliance.json
- remediation-backlog.csv
- script-index.json
- documentation-audit.csv
Confirm protocol completion?"
```

**Clarification Prompt:**
```
[RAY CLARIFICATION NEEDED]
"I detected ambiguity in the requirements regarding '{specific_point}'. Please clarify:
1. [Specific question about script inventory scope]
2. [Specific question about compliance requirements]
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
"Script governance scorecard draft complete. Please review and provide feedback on:
1. Completeness and accuracy
2. Quality and alignment with governance needs
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
[RAY GATE FAILED: Documentation & Static Compliance Gate] [CRITICAL]
"Quality gate 'Documentation & Static Compliance Gate' failed. Documentation coverage must be ≥95% and blocker findings must be 0 before proceeding."
Context: Documentation coverage = 92%, blocker findings = 2
Resolution: Engage script owners to remediate documentation or fix static analysis issues
Impact: Blocks completion until resolved
```

**Error Template with Context:**
```
[RAY VALIDATION ERROR: Inventory Accuracy Gate] [WARNING]
"Inventory completeness below threshold (93% vs required 95%)."
Context: inventory-validation-report.json shows 93% completeness
Resolution: Re-run discovery, resolve permissions, document exceptions
Impact: May affect quality; review recommended before completion
```

**Error Template with Resolution:**
```
[RAY SCRIPT ERROR: Compliance Scorecard Generation] [INFO]
"Compliance scorecard generation incomplete."
Context: Missing artifact checksum for script-compliance.json
Resolution: Re-run compliance scorecard generation script
Impact: Minor; scorecard will be updated automatically
```

---

<!-- [Category: GUIDELINES-FORMATS - AUTOMATION PLAYBOOK] -->
<!-- Why: Documents validation scripts, CI/CD integration, and manual fallback steps. -->
## 8. AUTOMATION HOOKS

### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_23.py

# Quality gate automation
python scripts/validate_gate_23_inventory.py --threshold 0.95
python scripts/validate_gate_23_artifacts.py --threshold 0.98

# Evidence aggregation
python scripts/aggregate_evidence_23.py --output .artifacts/scripts/
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

<!-- [Category: EXECUTION-FORMATS - BASIC variant] -->
<!-- Why: Checklist confirms readiness before handing evidence to audit and retrospective protocols. -->
## 8. HANDOFF CHECKLIST

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
- **Approvals Required:** Automation owner approval for read-only validation, Security lead acknowledgement for accessing script metadata, and quality team approval for governance compliance before protocol completion
- **Reviewers:** Automation owner reviews validation results, Security lead reviews script metadata access, Quality team reviews governance compliance
- **Sign-Off Evidence:** Approvals documented in `.artifacts/protocol-23/reviewer-signoff.json`, reviewer sign-off in `.artifacts/protocol-23/reviewer-signoff.json`
- **Confirmation Required:** Explicit confirmation that script governance validation is complete, compliance scorecard is generated, and remediation backlog is documented

**Documentation Requirements:**
- **Document Format:** All artifacts in Markdown (`.md`) or JSON (`.json`) format
- **Storage Location:** All documentation stored in `.artifacts/protocol-23/` directory
- **Reviewer Documentation:** Reviewers document approval/rejection rationale in `.artifacts/protocol-23/reviewer-signoff.json`
- **Evidence Manifest:** Complete manifest file at `.artifacts/protocol-23/evidence-manifest.json` with all artifact checksums
- **Documentation Types:** All documentation includes logs, briefs, notes, transcripts, manifests, and reports as required

**Ready-for-Next-Protocol Statement:**
✅ **Protocol 23 COMPLETE - Final Protocol**

All script governance validation completed, compliance scorecard generated, remediation backlog documented, and stakeholder approvals obtained. Protocol 23 represents the final protocol in the workflow sequence.

**Protocol Completion:**
```bash
# Validate final protocol completion
python3 validators-system/scripts/validate_all_protocols.py --protocol 23 --workspace .
# Review script governance compliance and remediation backlog
```

**Continuation Instructions:**
Protocol 23 is the final protocol in the workflow sequence. All governance artifacts have been generated and documented. Script compliance scorecard and remediation backlog are available for ongoing governance activities.

**Dependencies Satisfied:**
- ✅ Script inventory validated and indexed
- ✅ Documentation and static compliance verified
- ✅ Governance scorecard generated
- ✅ Evidence bundle complete
- ✅ Quality gates passed
- ✅ Stakeholder sign-off obtained

---

<!-- [Category: META-FORMATS - EVIDENCE INVENTORY] -->
<!-- Why: Aggregates artifacts, traceability, and metrics for governance oversight. -->
## 8. EVIDENCE SUMMARY

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| script-index artifact (`script-index.json`) | Script count metric, completeness metric ≥0.95, metadata coverage metric =100% | `.artifacts/protocol-23/script-index.json` | Gate 1 inventory accuracy |
| inventory-validation artifact (`inventory-validation-report.json`) | Validation completeness metric =100%, discovery coverage metric documented | `.artifacts/protocol-23/inventory-validation-report.json` | Gate 1 validation evidence |
| documentation-audit artifact (`documentation-audit.csv`) | Documentation rate metric ≥0.95, coverage metric documented | `.artifacts/protocol-23/documentation-audit.csv` | Gate 2 documentation evidence |
| static-analysis artifact (`static-analysis-report.json`) | Blocker count metric =0, warning count metric, finding severity metric logged | `.artifacts/protocol-23/static-analysis-report.json` | Gate 2 compliance evidence |
| artifact-compliance artifact (`artifact-compliance-report.json`) | Compliance score metric ≥0.98, path verification metric =100% | `.artifacts/protocol-23/artifact-compliance-report.json` | Gate 3 artifact governance |
| schema-validation artifact (`schema-validation-logs.json`) | Validation success metric ≥0.98, schema adherence metric documented | `.artifacts/protocol-23/schema-validation-logs.json` | Gate 3 schema evidence |
| compliance-scorecard artifact (`script-compliance.json`) | Scorecard completeness metric =100%, item count metric documented | `.artifacts/protocol-23/script-compliance.json` | Gate 4 governance scorecard |
| remediation-backlog artifact (`remediation-backlog.csv`) | Backlog entry count metric, coverage metric =100%, owner assignment metric recorded | `.artifacts/protocol-23/remediation-backlog.csv` | Gate 4 remediation evidence |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-23/`  
- **Subdirectories:** `scripts/` for script inventory, `compliance/` for audit reports, `governance/` for scorecard and backlog.  
- **Permissions:** Read/write for governance team and script owners, read-only for retrospective and documentation teams.  
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `script-index.json`, `remediation-backlog.csv`).

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-23/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`).  
- Artifact checksums: SHA-256 hash recorded for every artifact and governance record.  
- Size: File size in bytes captured in manifest integrity block.  
- Dependencies: Upstream protocols (22, 21) and downstream consumers (19) documented.

**Dependency Tracking:**
- Input: Protocol 22 `retrospective-automation-candidates.json`, Protocol 21 `automation-candidates.json`, script repository.  
- Output: All artifacts listed above plus gate validation reports and governance evidence bundle.  
- Transformations: Script discovery -> Documentation audit -> Compliance validation -> Governance reporting.

**Coverage:** Manifest documents 100% of required artifacts, script records, compliance reports, and governance scorecards with checksum verification.

### Traceability

**Input Sources:**
- **Input From:** Protocol 22 `.artifacts/protocol-22/retrospective-automation-candidates.json` – Automation opportunities for script governance.  
- **Input From:** Protocol 21 `.artifacts/protocol-21/automation-candidates.json` – Maintenance automation candidates.  
- **Input From:** Script repository `scripts/` – All automation scripts and procedures.

**Output Artifacts:**
- **Output To:** `script-compliance.json` – Governance scorecard consumed by Protocol 19 (Documentation).  
- **Output To:** `remediation-backlog.csv` – Remediation actions for continuous improvement.  
- **Output To:** `static-analysis-report.json` – Code quality findings for development teams.  
- **Output To:** `evidence-manifest.json` – Audit ledger for governance and compliance reviews.

**Transformation Steps:**
1. Script discovery -> script-index.json and inventory-validation-report.json: Index all scripts and verify completeness.  
2. Documentation audit -> documentation-audit.csv and static-analysis-report.json: Audit documentation and code quality.  
3. Compliance validation -> artifact-compliance-report.json and schema-validation-logs.json: Verify artifact compliance and schema adherence.  
4. Governance reporting -> script-compliance.json and remediation-backlog.csv: Generate scorecard and backlog.

**Audit Trail:**
- Manifest stores timestamps, checksums, and governance lead identity for each artifact.  
- Script records maintain discovery timestamps and metadata completeness status.  
- Compliance reports document validation results and remediation recommendations.  
- Governance scorecards track compliance trends and improvement actions.

### Archival Strategy

**Compression:**
- Governance artifacts compressed into `.artifacts/protocol-23/GOVERNANCE-BUNDLE.zip` after Gate 4 completion using ZIP standard compression.

**Retention Policy:**
- Active artifacts retained for 2 years post-governance review to support compliance tracking and learning.  
- Archived bundles retained for 5 years per regulatory and organizational governance requirements.  
- Cleanup automation `scripts/cleanup_artifacts.py` enforces retention quarterly.

**Retrieval Procedures:**
- Active artifacts accessed directly from `.artifacts/protocol-23/` with read-only permissions.  
- Archived bundles retrieved via `unzip .artifacts/protocol-23/GOVERNANCE-BUNDLE.zip` with manifest checksum verification.  
- Governance standards stored in `governance/governance-standards.md` for organizational reference.

**Cleanup Process:**
- Quarterly cleanup logs actions to `.artifacts/protocol-23/cleanup-log.json` with governance artifact inventory snapshot.  
- Critical governance artifacts flagged for extended retention require governance lead approval.  
- Manual retention overrides documented with timestamp, approver identity, and business justification.


---

<!-- [Category: META-FORMATS - COGNITIVE EXPLAINABILITY] -->
<!-- Why: Captures reasoning patterns, decision logic, and adaptive learning mechanisms. -->
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
