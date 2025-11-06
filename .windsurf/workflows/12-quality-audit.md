---
description: Apply instructions from @12-quality-audit.md
auto_execution_mode: 1
---

# PROTOCOL 12 : QUALITY AUDIT ORCHESTRATOR (QUALITY ASSURANCE COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

<!-- [Category: GUIDELINES-FORMATS - Requirements & Standards] -->
## 1. PREREQUISITES

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
**[MUST]** Validate presence of upstream artifacts before protocol initiation:

- **`[REQUIRED]`** `INTEGRATION-EVIDENCE.zip` from Protocol 11 – consolidated integration and regression results
- **`[REQUIRED]`** `integration-signoff.json` from Protocol 11 – upstream readiness snapshot
- **`[REQUIRED]`** Latest Git diff summary produced by `scripts/collect_change_context.py`
- **`[REQUIRED]`** `TECHNICAL-DESIGN.md` from Protocol 07 – architecture baseline for compliance checks

### 1.2 Required Approvals
**[MUST]** Obtain necessary authorizations:

- **`[REQUIRED]`** Integration validation sign-off from Protocol 11 Integration Lead
- **`[REQUIRED]`** Security waiver or approval (if applicable)
- **`[REQUIRED]`** Product Owner acknowledgement that scope matches PRD acceptance criteria (Protocol 06)

### 1.3 System State Requirements
**[MUST]** Verify system readiness:

- **`[REQUIRED]`** CI workflows `ci-test.yml` and `ci-lint.yml` configured in repository
- **`[REQUIRED]`** Access to `.cursor/ai-driven-workflow/review-protocols/` directory and router utility
- **`[REQUIRED]`** Write permissions to `.artifacts/quality-audit/` for evidence capture

<!-- [Category: GUIDELINES-FORMATS - Role Definition] -->
## 2. AI ROLE AND MISSION

You are a **Senior Quality Engineer**. Your mission is to orchestrate the correct review protocol, execute pre-audit automation, and consolidate the unified audit record that underpins downstream release decisions.

**🚫 [CRITICAL]** DO NOT bypass pre-audit automation or deliver reports without executing the selected specialized protocol end-to-end.

<!-- [Category: EXECUTION-FORMATS - Mixed variants by phase] -->
## 3. WORKFLOW

<!-- [Category: EXECUTION-SUBSTEPS - Multiple validation tasks] -->
### PHASE 1: Pre-Audit Automation Enablement

1. **`[MUST]` Execute Baseline CI Validation:**
   
   * **1.1. Run CI Workflows:**
     * **Action:** Run required CI workflows (`ci-test.yml`, `ci-lint.yml`)
     * **Evidence:** Store outputs at `.artifacts/quality-audit/ci-<workflow>-results.json`
     * **Communication:** 
       > "[MASTER RAY™ | PHASE 1 START] - Executing baseline CI workflows for quality audit enablement..."
     * **Halt Condition:** Stop if any workflow fails or artifacts cannot be generated
   
   * **1.2. Aggregate Coverage Metrics:**
     * **Action:** Invoke coverage aggregation to produce `.artifacts/quality-audit/coverage-report.json` with line/function coverage stats
     * **Evidence:** Coverage report and timestamped metadata file `coverage-metadata.yaml`
     * **Communication:** 
       > "[RAY AUTOMATION] Coverage aggregation complete. Overall coverage: {percentage}%"
     * **Halt Condition:** Pause if coverage report lacks required sections or falls below mandated baseline (<80%)
   
   * **1.3. Snapshot Change Context:**
     * **Action:** Generate Git diff summary focusing on touched modules to guide audit scope
     * **Evidence:** `.artifacts/quality-audit/change-context.json`
     * **Example:**
       ```bash
       python scripts/collect_change_context.py --since main --output .artifacts/quality-audit/change-context.json
       ```

<!-- [Category: EXECUTION-REASONING - Mode determination decisions] -->
### PHASE 2: Mode Determination and Routing

1. **`[MUST]` Determine Review Mode and Protocol:**
   
   **[REASONING]:**
   - **Premises:** Review mode selection drives specialized protocol execution path
   - **Constraints:** Must use centralized router for consistency and fallback handling
   - **Alternatives Considered:**
     * **A)** Direct protocol selection - Rejected: Bypasses validation and fallback logic
     * **B)** Centralized router - Selected: Ensures consistency and proper fallback
     * **C)** Manual selection - Rejected: Error-prone and lacks audit trail
   - **Decision:** Use centralized router with fallback validation
   - **Evidence:** Router configuration and available protocols list
   
   * **2.1. Resolve Review Mode:**
     * **Action:** Parse `/review --mode {target}` input or fallback rules to determine specialized protocol
     * **Communication:** 
       > "[MASTER RAY™ | PHASE 2 START] - Determining review mode '{mode}' via centralized router..."
     * **Halt Condition:** Suspend execution if router cannot map mode to protocol
     * **Evidence:** `.artifacts/quality-audit/mode-resolution.json` capturing requested mode, router decision, and fallback chain
   
   * **2.2. Load Specialized Protocol Instructions:**
     * **Action:** Fetch markdown from `.cursor/ai-driven-workflow/review-protocols/{protocol}.md` and register execution scope
     * **Communication:** 
       > "[ROUTER] Specialized protocol '{protocol}' loaded for execution."
     * **Halt Condition:** Stop if file retrieval fails or integrity check mismatches expected hash
     * **Evidence:** `.artifacts/quality-audit/protocol-manifest.json` with hash, version, and dependencies
   
   * **2.3. Validate Router Fallback Logic:**
     * **Action:** Confirm router escalates from custom to generic protocol when custom file missing
     * **Example:**
       ```python
       selected = router.resolve(mode)
       assert selected in router.available_protocols
       ```

<!-- [Category: EXECUTION-SUBSTEPS - Complex protocol execution] -->
### PHASE 3: Specialized Protocol Execution Oversight

1. **`[MUST]` Execute and Monitor Specialized Protocol:**
   
   * **3.1. Execute Selected Review Protocol:**
     * **Action:** Follow instructions inside loaded protocol, delegating steps while capturing evidence references in orchestrator log
     * **Communication:** 
       > "[MASTER RAY™ | PHASE 3 START] - Executing specialized review protocol '{protocol}'..."
     * **Halt Condition:** Halt if specialized protocol reports blocking findings without mitigation
     * **Evidence:** `.artifacts/quality-audit/execution-log.md` enumerating steps, checks, and outcomes
   
   * **3.2. Consolidate Findings Across Checks:**
     * **Action:** Merge lint/test/security outputs into unified dataset `audit-findings.json` categorized by severity
     * **Communication:** 
       > "[PHASE 3] Consolidating findings from specialized review outputs..."
     * **Halt Condition:** Pause if any required artifact missing from specialized run
     * **Evidence:** `.artifacts/quality-audit/audit-findings.json` plus severity summary chart `finding-summary.csv`
   
   * **3.3. Trigger Extended Checks for Comprehensive Mode:**
     * **Action:** When mode == `comprehensive`, sequence quick → security → architecture → design → ui reviews
     * **Example:**
       ```bash
       python scripts/run_comprehensive_review.py --output .artifacts/quality-audit/comprehensive-trace.json
       ```

<!-- [Category: EXECUTION-BASIC - Sequential reporting] -->
### PHASE 4: Unified Reporting and Handoff Preparation

1. **`[MUST]` Generate Audit Report Package:**
   * **Action:** Compile CI, coverage, specialized findings, and router manifests into `QUALITY-AUDIT-PACKAGE.zip`
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Packaging unified quality audit deliverables..."
   * **Halt Condition:** Stop if package checksum verification fails
   * **Evidence:** `.artifacts/quality-audit/quality-audit-manifest.json` plus zipped artifact

2. **`[MUST]` Issue Readiness Recommendation:**
   * **Action:** Produce decision record (`go`, `go-with-risks`, `no-go`) referencing gate scores and mitigations
   * **Communication:** 
     > "[RAY VALIDATION REQUEST] - Audit decision: {decision}. Confirm acceptance to proceed to UAT coordination?"
   * **Halt Condition:** Await stakeholder confirmation for `go-with-risks` or `no-go` outcomes
   * **Evidence:** `.artifacts/quality-audit/readiness-recommendation.md` detailing rationale and signatories

3. **`[GUIDELINE]` Publish Audit Summary to Context Kit:**
   * **Action:** Update `.cursor/context-kit/quality-audit-summary.json` for rapid reuse in subsequent phases
   * **Example:**
     ```python
     save_summary(findings, path=".cursor/context-kit/quality-audit-summary.json")
     ```

<!-- [Category: META-FORMATS - Retrospective and Learning] -->
## 4. REFLECTION & LEARNING

### 4.1 Retrospective Guidance

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

### 4.2 Continuous Improvement Opportunities

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

### 4.3 System Evolution

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

### 4.4 Knowledge Capture and Organizational Learning

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

### 4.5 Future Planning

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

<!-- [Category: GUIDELINES-FORMATS - Integration Standards] -->
## 5. INTEGRATION POINTS

### 5.1 Inputs From
- **Protocol 11:** `INTEGRATION-EVIDENCE.zip` – regression and integration proof set
- **Protocol 11:** `integration-signoff.json` – upstream readiness confirmation
- **Protocol 07:** `TECHNICAL-DESIGN.md` – architecture baseline for compliance checks

### 5.2 Outputs To
- **Protocol 20:** `QUALITY-AUDIT-PACKAGE.zip` – formal audit deliverables for UAT entry gate
- **Protocol 21:** `readiness-recommendation.md` – informs pre-deployment intake validation
- **Protocol 22:** `quality-audit-summary.json` – lessons learned for retrospective analysis
- **Protocol 23:** `finding-summary.csv` – feedback loop for automation improvements

### 5.3 Artifact Storage Locations
- `.artifacts/quality-audit/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

<!-- [Category: GUIDELINES-FORMATS - Quality Gate Definitions] -->
## 6. QUALITY GATES

### Gate 1: Baseline Automation Integrity
**Type:** Prerequisite  
**Purpose:** Confirm CI evidence, coverage metrics, and router bootstrap before audit execution.

**Pass Criteria:**
- **Threshold:** Coverage score ≥ 0.80 with ≥ 1 coverage metric recorded. 
- **Boolean Check:** CI status = pass for `ci-test.yml` and `ci-lint.yml` runs. 
- **Metrics:** Coverage percentage, automation run duration, checksum validation rate. 
- **Evidence Link:** Validated against `.artifacts/protocol-12/ci-results.json` and `.artifacts/protocol-12/coverage-report.json`.

**Automation:**
- Script: `python3 scripts/run_protocol_12_gates.py --stage baseline`
- Script: `python3 scripts/collect_change_context.py --since main --output .artifacts/protocol-12/change-context.json`
- CI/CD Integration: Executes inside release workflow (`runs-on: ubuntu-latest`) prior to manual review, referencing `config/protocol_gates/12.yaml` thresholds.

**Failure Handling:**
- **Rollback:** Re-run CI workflows and regenerate coverage bundle before escalating. 
- **Notification:** Notify DevOps lead via Slack when automation metric dips below 0.80 threshold. 
- **Waiver:** Waiver recorded in `.artifacts/protocol-12/gate-waivers.json` with justification; only valid if change scope low risk.

### Gate 2: Routing and Mode Verification
**Type:** Execution  
**Purpose:** Ensure router maps requested review mode to correct specialized protocol with fallback safety.

**Pass Criteria:**
- **Threshold:** Router checksum validation ≥ 0.98 accuracy score.
- **Boolean Check:** Mode resolution flag = true before protocol execution. 
- **Metrics:** Manifest hash comparison, fallback invocation rate, routing latency metric. 
- **Evidence Link:** Validated against `.artifacts/protocol-12/mode-resolution.json` and `.artifacts/protocol-12/protocol-manifest.json`.

**Automation:**
- Script: `python3 scripts/validate_router_mapping.py --mode comprehensive`
- Script: `python3 scripts/run_protocol_12_gates.py --stage routing`
- CI/CD Integration: Router smoke test runs in quality-assurance workflow and publishes metrics to `.artifacts/validation/` dashboard configured via `config/protocol_gates/12.yaml`.

**Failure Handling:**
- **Rollback:** Reset router cache and reload manifests from main branch.
- **Notification:** Email workflow maintainer and protocol steward when boolean routing check fails. 
- **Waiver:** Waiver not permitted—routing integrity is mandatory.

### Gate 3: Findings Resolution Readiness
**Type:** Execution  
**Purpose:** Validate that specialized protocol outputs are consolidated and blockers triaged before packaging.

**Pass Criteria:**
- **Threshold:** Blocker severity rate ≤ 5% across consolidated findings.
- **Boolean Check:** All blocker findings set to `triaged=true` in audit log. 
- **Metrics:** Severity distribution score, remediation elapsed time metric, triage completion percentage. 
- **Evidence Link:** Validated against `.artifacts/protocol-12/audit-findings.json` and `.artifacts/protocol-12/execution-log.md`.

**Automation:**
- Script: `python3 scripts/aggregate_evidence_01.py --output .artifacts/protocol-12/audit-findings.json`
- Script: `python3 scripts/validate_gate_12_assurance.py --manifest .artifacts/protocol-12/triage-matrix.json`
- CI/CD Integration: Gated check inside `quality-audit` workflow ensures triage metrics published to governance dashboard.

**Failure Handling:**
- **Rollback:** Reopen specialized protocol session to resolve outstanding findings. 
- **Notification:** Post alert in quality-audit channel with unresolved blockers summary. 
- **Waiver:** Documented as “Not applicable – mandatory gate” when severity rate cannot be reduced; escalation required.

### Gate 4: Package & Recommendation Approval
**Type:** Completion  
**Purpose:** Certify that the unified package, manifest metrics, and readiness recommendation meet governance thresholds.

**Pass Criteria:**
- **Threshold:** Manifest completeness score ≥ 0.95 with checksum validation metric = 100%.
- **Boolean Check:** Readiness decision signed and checksum verification flag true. 
- **Metrics:** Manifest coverage score, checksum verification rate, approval latency metric. 
- **Evidence Link:** Validated against `.artifacts/protocol-12/quality-audit-manifest.json`, `.artifacts/protocol-12/readiness-recommendation.md`, and `.artifacts/protocol-12/evidence-manifest.json`.

**Automation:**
- Script: `python3 scripts/validate_gate_12_handoff.py --threshold 0.95`
- Script: `python3 scripts/run_protocol_12_gates.py --stage completion`
- CI/CD Integration: Completion stage in governance pipeline verifies approvals declared in `config/protocol_gates/12.yaml`.

**Failure Handling:**
- **Rollback:** Rebuild `QUALITY-AUDIT-PACKAGE.zip`, rerun checksum routine, and request new signatures.
- **Notification:** Notify Senior Quality Engineer and Release Manager when manifest completeness drops below threshold. 
- **Waiver:** Waiver allowed only under emergency release; justification logged with risk statement in `.artifacts/protocol-12/waiver-log.md`.

### Compliance Integration
- **Industry Standards:** CommonMark Markdown, JSON Schema 2020-12, YAML 1.2 formatting enforced during artifact generation.
- **Security Requirements:** SOC2-labeled evidence, security waiver tracking, access governed by least-privilege ACLs.
- **Regulatory Compliance:** FTC disclosure readiness, GDPR data handling for logs, audit retention consistent with quality governance charter.
- **Governance:** Gate thresholds centralized in `config/protocol_gates/12.yaml` and mirrored in validation registry for downstream audits.

<!-- [Category: GUIDELINES-FORMATS - Communication Standards] -->
## 7. COMMUNICATION PROTOCOLS

### 7.1 Status Announcements
**[GUIDELINE]** Standard status messages for protocol execution:

```
[MASTER RAY™ | PHASE 1 START] - Executing baseline CI workflows for quality audit enablement...
[MASTER RAY™ | PHASE 1 COMPLETE] - Pre-audit automation complete. Evidence: ci-workflow-log.txt, coverage-report.json.
[MASTER RAY™ | PHASE 2 START] - Determining review mode '{mode}' via centralized router...
[MASTER RAY™ | PHASE 3 START] - Executing specialized review protocol '{protocol}'...
[MASTER RAY™ | PHASE 4 START] - Packaging unified quality audit deliverables...
[MASTER RAY™ | PHASE 4 COMPLETE] - Quality audit package ready. Evidence: QUALITY-AUDIT-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### 7.2 User Interaction Prompts

**Confirmation Prompt:**
```
[RAY CONFIRMATION REQUIRED]
"Quality audit complete and package ready:
- QUALITY-AUDIT-PACKAGE.zip
- readiness-recommendation.md
- audit-findings.json

Please review and confirm readiness to proceed to Protocol 13."
```

**Clarification Prompt:**
```
[RAY CLARIFICATION NEEDED]
"I detected ambiguity in the requirements regarding '{specific audit scope or review mode}'. Please clarify:
1. Which review mode should be used for this audit cycle?
2. What are the acceptable thresholds for blocking findings?
3. Are there specific compliance requirements that must be validated?

This will help me proceed more accurately."
```

**Decision Point Prompt:**
```
[RAY DECISION REQUIRED]
"Multiple approaches identified for '{review mode selection or audit strategy}'. Please choose:
- Option A: [Description] - Pros: [list], Cons: [list]
- Option B: [Description] - Pros: [list], Cons: [list]
- Option C: [Description] - Pros: [list], Cons: [list]

Which approach should I proceed with?"
```

**Feedback Prompt:**
```
[RAY FEEDBACK REQUESTED]
"Quality audit report draft complete. Please review and provide feedback on:
1. Completeness and accuracy of findings
2. Quality and alignment with acceptance criteria
3. Any adjustments needed before finalization

Your feedback will be incorporated into the final deliverables."
```

### 7.3 Error Messaging

**Error Severity Levels:**
- **CRITICAL:** Blocks protocol execution; requires immediate user intervention
- **WARNING:** May affect quality but allows continuation; user should review
- **INFO:** Informational only; no action required

**Error Template with Severity:**
```
[RAY GATE FAILED: {Gate Name}] [CRITICAL]
"Quality gate '{Gate Name}' failed for quality audit.
Context: {Context description}
Resolution: {Resolution steps}
Impact: Blocks handoff until resolved"
```

**Error Template with Context:**
```
[RAY VALIDATION ERROR: {Validation Type}] [WARNING]
"Quality audit validation warning detected: {warning message}
Context: {Context details}
Resolution: {Resolution steps}
Impact: May affect quality; review recommended before handoff"
```

**Error Template with Resolution:**
```
[RAY SCRIPT ERROR: {Script Name}] [INFO]
"Quality audit script execution completed with minor issues: {info message}
Context: {Context info}
Resolution: {Resolution action}
Impact: Minor; {automatic fix description}"
```

<!-- [Category: GUIDELINES-FORMATS - Automation Standards] -->
## 8. AUTOMATION HOOKS

### 8.1 Registry Reference
**[GUIDELINE]** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.

### 8.2 Validation Scripts
**[MUST]** Execute automation scripts in sequence:

```bash
# Prerequisite validation
python scripts/validate_prerequisites_4.py

# Quality gate automation
python scripts/validate_gate_4_pre_audit.py --threshold 0.80
python scripts/validate_gate_4_reporting.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_4.py --output .artifacts/quality-audit/
```

### 8.3 CI/CD Integration
**[GUIDELINE]** Pipeline configuration template:

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

### 8.4 Manual Fallbacks
**[GUIDELINE]** When automation is unavailable, execute manual validation:

1. Review CI results directly in pipeline dashboard and export JSON summaries
2. Manually verify router mapping by cross-checking available protocols list
3. Document results in `.artifacts/protocol-19/manual-validation-log.md`

<!-- [Category: EXECUTION-BASIC - Validation Checklist] -->
## 9. HANDOFF CHECKLIST

### 9.1 Continuous Improvement Validation
**[MUST]** Verify improvement tracking:

- [x] Execution feedback collected and logged
- [x] Lessons learned documented in protocol artifacts
- [x] Quality metrics captured for improvement tracking
- [x] Knowledge base updated with new patterns or insights
- [x] Protocol adaptation opportunities identified and logged
- [x] Retrospective scheduled (if required for this protocol phase)

### 9.2 Pre-Handoff Validation
**[MUST]** Before declaring protocol complete, validate:

- [x] All prerequisites were met
- [x] All workflow steps completed successfully
- [x] All quality gates passed (or waivers documented)
- [x] All evidence artifacts captured and stored
- [x] All integration outputs generated
- [x] All automation hooks executed successfully
- [x] Communication log complete

**Stakeholder Sign-Off:**
- **Approvals Required:** Quality audit readiness recommendation signed by Senior Quality Engineer before proceeding to Protocol 13
- **Reviewers:** Senior Quality Engineer reviews audit completeness and recommendation alignment
- **Sign-Off Evidence:** Readiness recommendation documented in `.artifacts/protocol-12/readiness-recommendation.md`, reviewer sign-off in `.artifacts/protocol-12/reviewer-signoff.json`
- **Confirmation Required:** Explicit confirmation that quality audit is complete and Protocol 13 prerequisites satisfied

**Documentation Requirements:**
- **Document Format:** All artifacts in Markdown (`.md`) or JSON (`.json`) format
- **Storage Location:** All documentation stored in `.artifacts/protocol-12/` directory
- **Reviewer Documentation:** Reviewers document approval/rejection rationale in `.artifacts/protocol-12/reviewer-signoff.json`
- **Evidence Manifest:** Complete manifest file at `.artifacts/protocol-12/evidence-manifest.json` with all artifact checksums
- **Documentation Types:** All documentation includes logs, briefs, notes, transcripts, manifests, and reports as required

**Ready-for-Next-Protocol Statement:**
✅ **Protocol 12 COMPLETE - Ready for Protocol 13**

All quality audit artifacts validated, approvals obtained, and Protocol 13 prerequisites satisfied. Protocol 13 (UAT Coordination) can now proceed.

**Next Protocol Command:**
```bash
# Run Protocol 13: UAT Coordination
@apply .cursor/ai-driven-workflow/13-uat-coordination.md
# Or trigger validation: python3 validators-system/scripts/validate_all_protocols.py --protocol 13 --workspace .
```

**Continuation Instructions:**
After Protocol 12 completion, run Protocol 13 continuation script to proceed. Generate session continuation for Protocol 13 workflow execution. Ensure all handoff checklist items verified and approvals obtained before proceeding.

**Dependencies Satisfied:**
- ✅ Quality audit complete and validated
- ✅ Evidence bundle complete
- ✅ Quality gates passed
- ✅ Stakeholder sign-off obtained

### 9.3 Handoff to Protocol 13
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 13: User Acceptance Testing Coordination

**Evidence Package:**
- `QUALITY-AUDIT-PACKAGE.zip` - Consolidated audit artifacts
- `readiness-recommendation.md` - Decision record with approvals

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/13-uat-coordination.md
```

<!-- [Category: GUIDELINES-FORMATS - Documentation Standards] -->
## 10. EVIDENCE SUMMARY

### Artifact Generation Table

| Artifact Name | Metrics | Location | Evidence Link |
|---------------|---------|----------|---------------|
| audit-findings.json | Severity distribution metric ≤5% blockers, remediation latency score | `.artifacts/protocol-12/audit-findings.json` | Gate 3 validation |
| quality-audit-manifest.json | Manifest completeness metric ≥95%, checksum verification result = 100% | `.artifacts/protocol-12/quality-audit-manifest.json` | Gate 4 validation |
| readiness-recommendation.md | Decision confidence score ≥0.9, Boolean approval status captured | `.artifacts/protocol-12/readiness-recommendation.md` | Gate 4 validation |
| QUALITY-AUDIT-PACKAGE.zip | Package integrity metric passes SHA-256, evidence bundle size reported | `.artifacts/protocol-12/QUALITY-AUDIT-PACKAGE.zip` | Gate 4 validation |
| coverage-report.json | Coverage metric ≥80%, automation result summary | `.artifacts/protocol-12/coverage-report.json` | Gate 1 validation |

### Storage Structure

**Protocol Directory:** `.artifacts/protocol-12/`
- **Subdirectories:** `logs/` for execution transcripts, `packages/` for zipped bundles, `metrics/` for automation summaries
- **Permissions:** Read/write for protocol executor, read-only for downstream protocols 13-15
- **Naming Convention:** `{artifact-name}.{extension}` (e.g., `audit-findings.json`, `readiness-recommendation.md`)

### Manifest Completeness

**Manifest File:** `.artifacts/protocol-12/evidence-manifest.json`

**Metadata Requirements:**
- Timestamp: ISO 8601 format (e.g., `2025-11-06T05:34:29Z`)
- Artifact checksums: SHA-256 hash for each artifact
- Size: File size in bytes for every entry
- Dependencies: List upstream artifacts or contextual inputs

**Dependency Tracking:**
- Input: `INTEGRATION-EVIDENCE.zip`, `integration-signoff.json`, `TECHNICAL-DESIGN.md`
- Output: `audit-findings.json`, `quality-audit-manifest.json`, `readiness-recommendation.md`, `QUALITY-AUDIT-PACKAGE.zip`
- Transformations: CI validation → router resolution → specialized execution → unified packaging

**Coverage:** 100% of required artifacts documented in manifest

### Traceability

**Input Sources:**
- **Input From:** `.artifacts/protocol-11/INTEGRATION-EVIDENCE.zip` – Regression and integration evidence bundle
- **Input From:** `.artifacts/protocol-07/TECHNICAL-DESIGN.md` – Architecture baseline for compliance checks

**Output Artifacts:**
- **Output To:** `.artifacts/protocol-12/audit-findings.json` – Consolidated findings for downstream consumers
- **Output To:** `.artifacts/protocol-12/readiness-recommendation.md` – Go/no-go decision log
- **Output To:** `.artifacts/protocol-12/QUALITY-AUDIT-PACKAGE.zip` – Packaging for Protocols 13 and 20
- **Output To:** `.cursor/context-kit/quality-audit-summary.json` – Snapshot for rapid reuse

**Transformation Steps:**
1. CI outputs + change context → Coverage baseline ingestion
2. Router manifests → Specialized protocol execution oversight
3. Specialized outputs → Severity consolidation in findings dataset
4. Findings + approvals → Final package creation and manifest updates

**Audit Trail:**
- Each transformation logged in `.artifacts/protocol-12/execution-log.md`
- Timestamps record generation events within manifest entry metadata
- Checksums enable integrity verification during handoff
- Dependencies mapped through manifest `dependencies` node

### Archival Strategy

**Compression:**
- Artifacts compressed into `.artifacts/protocol-12/QUALITY-AUDIT-PACKAGE.zip` after stakeholder confirmation
- Compression format: ZIP (deflated) with manifest cross-reference stored in `packages/`

**Retention Policy:**
- Active artifacts: Retained for 120 days after protocol completion
- Archived bundles: Retained for 3 years post project closure per governance charter
- Cleanup: Automated cleanup script runs quarterly to remove items beyond retention window

**Retrieval Procedures:**
- Active artifacts: Access directly in `.artifacts/protocol-12/`
- Archived bundles: Retrieve from `packages/` directory and verify via manifest checksums
- Integrity verification: SHA values in `evidence-manifest.json` rechecked during restore

**Cleanup Process:**
- Quarterly cleanup script logs actions to `.artifacts/protocol-12/cleanup-log.json`
- Critical artifacts flagged `retention_override=true` in manifest remain stored longer
- Manual review required before deleting any artifact linked to open incidents

<!-- [Category: META-FORMATS - Protocol Analysis] -->
## 11. REASONING & COGNITIVE PROCESS

### 11.1 Reasoning Patterns

**Primary Reasoning Pattern: Systematic Execution**
- Execute protocol steps sequentially with validation at each checkpoint

**Secondary Reasoning Pattern: Quality-Driven Validation**
- Apply quality gates to ensure artifact completeness before downstream handoff

**Pattern Improvement Strategy:**
- Track pattern effectiveness via quality gate pass rates and downstream protocol feedback
- Quarterly review identifies pattern weaknesses and optimization opportunities
- Iterate patterns based on empirical evidence from completed executions

### 11.2 Decision Logic

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

### 11.3 Root Cause Analysis Framework

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

### 11.4 Learning Mechanisms

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

### 11.5 Meta-Cognition

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