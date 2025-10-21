---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 14 : PRE-DEPLOYMENT VALIDATION & STAGING READINESS (RELEASE COMPLIANT)

**Purpose:** Execute Unknown Protocol workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `QUALITY-AUDIT-PACKAGE.zip` from Protocol 12 – audit readiness evidence
- [ ] `integration-evidence-bundle.zip` from Protocol 11 – integration validation summary
- [ ] `UAT-CLOSURE-PACKAGE.zip` from Protocol 13 – stakeholder acceptance proof
- [ ] `.artifacts/pre-deployment/release-manifest.json` (initial draft) from Release Planning
- [ ] Latest deployment scripts (`scripts/deploy_*.sh`, `scripts/rollback_*.sh`) from repository

### Required Approvals
- [ ] Quality Audit readiness recommendation signed by Senior Quality Engineer (Protocol 12)
- [ ] Product Owner confirmation that release scope is fixed (Protocol 06)
- [ ] Security and compliance lead clearance for staging deployment rehearsals

### System State Requirements
- [ ] Staging environment mirrors production configuration (infrastructure, secrets, feature flags)
- [ ] Access to deployment automation credentials and secret stores for staging
- [ ] Monitoring dashboards accessible for baseline capture

---

## 10. AI ROLE AND MISSION

You are a **Release Engineer**. Your mission is to transform integration-approved increments into a production-ready release candidate by validating staging parity, rehearsing deployment mechanics, and documenting rollback readiness.

**🚫 [CRITICAL] DO NOT issue a production go/no-go package unless staging mirrors production configurations and both deployment and rollback procedures have been executed successfully with captured evidence.**

---

## WORKFLOW

### STEP 1: Intake Validation and Staging Alignment

1. **`[MUST]` Confirm Upstream Approvals:**
   * **Action:** Validate required artifacts and approvals from Protocols 11, 12, and 13 before staging rehearsal begins.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Validating upstream approvals and artifact completeness..."
   * **Halt condition:** Stop if any prerequisite artifact missing or expired.
   * **Evidence:** `.artifacts/pre-deployment/intake-validation-report.json` summarizing status.

2. **`[MUST]` Validate Staging Parity:**
   * **Action:** Compare staging vs production configurations, secrets, and infrastructure components for drift detection.
   * **Communication:** 
     > "[PHASE 1] Staging parity check underway. Reporting drift if detected..."
   * **Halt condition:** Pause if drift exists without remediation plan.
   * **Evidence:** `.artifacts/pre-deployment/staging-parity-report.json` including diff details.

3. **`[GUIDELINE]` Refresh Test Data & Feature Flags:**
   * **Action:** Sync staging datasets, feature flags, and service stubs to align with release candidate requirements.
   * **Example:**
     ```bash
     python scripts/refresh_staging_data.py --env staging --output .artifacts/pre-deployment/staging-data-refresh.md
     ```

### STEP 2: Deployment Rehearsal and Verification

1. **`[MUST]` Execute Staging Deployment Rehearsal:**
   * **Action:** Run deployment scripts in staging replicating production sequencing with logging enabled.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 2 START] - Rehearsing deployment on staging environment..."
   * **Halt condition:** Stop if automation fails or unexpected errors occur.
   * **Evidence:** `.artifacts/pre-deployment/staging-deployment-run.log` capturing commands and results.

2. **`[MUST]` Validate Smoke & Acceptance Tests:**
   * **Action:** Execute smoke, end-to-end, and targeted regression suites against staging release candidate.
   * **Communication:** 
     > "[PHASE 2] Staging test suites executing. Monitoring pass/fail status..."
   * **Halt condition:** Pause if critical tests fail without mitigation.
   * **Evidence:** `.artifacts/pre-deployment/staging-test-results.json` with coverage metrics.

3. **`[GUIDELINE]` Capture Observability Baseline:**
   * **Action:** Record monitoring dashboards and metrics post-rehearsal for Protocol 19 reference.
   * **Example:**
     ```markdown
     - Metric: API latency (p95) – 320ms
     - Metric: Error rate – 0.2%
     ```

### STEP 3: Rollback, Security, and Operational Readiness

1. **`[MUST]` Rehearse Rollback Procedure:**
   * **Action:** Execute rollback automation or blue/green switchback to validate recovery path.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 3 START] - Verifying rollback and recovery procedures..."
   * **Halt condition:** Stop if rollback fails or exceeds recovery time objective.
   * **Evidence:** `.artifacts/pre-deployment/rollback-verification-report.json` detailing steps and timings.

2. **`[MUST]` Complete Security & Compliance Checks:**
   * **Action:** Run required security scans, license audits, and compliance validations pre-production.
   * **Communication:** 
     > "[PHASE 3] Executing security and compliance scans for release candidate..."
   * **Halt condition:** Pause if blocking findings identified.
   * **Evidence:** `.artifacts/pre-deployment/security-compliance-report.json` with findings and approvals.

3. **`[GUIDELINE]` Validate Runbooks & Support Coverage:**
   * **Action:** Confirm operational runbooks, on-call rotations, and escalation matrices updated for release.
   * **Example:**
     ```markdown
     - Runbook: api-service.md – updated 2024-05-30
     - On-call: Primary SRE (Alex), Backup (Jordan)
     ```

### STEP 4: Final Readiness Review and Handoff

1. **`[MUST]` Assemble Go/No-Go Package:**
   * **Action:** Bundle parity report, deployment and rollback evidence, test results, and security findings into `PRE-DEPLOYMENT-PACKAGE.zip`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 4 START] - Compiling pre-deployment readiness package for release approval..."
   * **Halt condition:** Stop if package contents incomplete or checksum invalid.
   * **Evidence:** `.artifacts/pre-deployment/pre-deployment-manifest.json` indexing artifacts.

2. **`[MUST]` Conduct Readiness Review:**
   * **Action:** Present findings to Release Manager and stakeholders; capture approvals, risks, and action items.
   * **Communication:** 
     > "[PHASE 4] Readiness review in progress. Recording decisions and risk mitigations..."
   * **Halt condition:** Pause if approvals withheld or risks unresolved.
   * **Evidence:** `.artifacts/pre-deployment/readiness-approval.json` with signatures.

3. **`[GUIDELINE]` Publish Deployment Checklist Updates:**
   * **Action:** Update production deployment checklist and communication plan based on rehearsal learnings.
   * **Example:**
     ```bash
     python scripts/update_deployment_checklist.py --source .artifacts/pre-deployment/staging-deployment-run.log --output .artifacts/pre-deployment/deployment-checklist.md
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

## 10. INTEGRATION POINTS

### Inputs From:
- **Protocol 19**: `QUALITY-AUDIT-PACKAGE.zip`, readiness recommendation – informs release gate
- **Protocol 23**: `script-compliance.json` – assures automation readiness
- **Protocol 15**: `integration-evidence-bundle.zip` – verifies integrated functionality
- **Protocol 20**: `UAT-CLOSURE-PACKAGE.zip`, `uat-approval-record.json` – confirms user acceptance

### Outputs To:
- **Protocol 15**: `PRE-DEPLOYMENT-PACKAGE.zip`, `readiness-approval.json`, `deployment-checklist.md`
- **Protocol 19**: `observability-baseline.md`, `staging-test-results.json`
- **Protocol 20**: `rollback-verification-report.json` for incident response readiness
- **Protocol 21**: `staging-parity-report.json` supporting performance baseline alignment

### Artifact Storage Locations:
- `.artifacts/pre-deployment/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration artifacts

---

## 10. QUALITY GATES

### Gate 1: Intake Confirmation Gate
- **Criteria**: All upstream approvals verified; staging parity report free of critical drift.
- **Evidence**: `intake-validation-report.json`, `staging-parity-report.json`.
- **Pass Threshold**: Completeness score = 100%; drift severity ≤ low.
- **Failure Handling**: Halt; remediate configuration drift or obtain missing approvals.
- **Automation**: `python scripts/validate_gate_10_intake.py --drift-threshold low`

### Gate 2: Deployment Rehearsal Gate
- **Criteria**: Deployment rehearsal successful; smoke/regression tests pass with acceptable coverage.
- **Evidence**: `staging-deployment-run.log`, `staging-test-results.json`.
- **Pass Threshold**: 0 blocking errors; coverage ≥ 90% of targeted suites.
- **Failure Handling**: Rollback staging, fix issues, rerun rehearsal before proceeding.
- **Automation**: `python scripts/validate_gate_10_rehearsal.py --coverage 0.90`

### Gate 3: Rollback & Security Gate
- **Criteria**: Rollback rehearsal completes within RTO; security/compliance scans cleared.
- **Evidence**: `rollback-verification-report.json`, `security-compliance-report.json`.
- **Pass Threshold**: Recovery time ≤ RTO; zero unresolved blocking findings.
- **Failure Handling**: Address rollback gaps or security issues; rerun validations.
- **Automation**: `python scripts/validate_gate_10_security.py --rto 10`

### Gate 4: Readiness Approval Gate
- **Criteria**: Go/no-go package complete; readiness approvals signed; deployment checklist updated.
- **Evidence**: `pre-deployment-manifest.json`, `readiness-approval.json`, `deployment-checklist.md`.
- **Pass Threshold**: Manifest completeness ≥ 95%; approvals 100% recorded.
- **Failure Handling**: Obtain missing approvals; rebuild package; update checklist.
- **Automation**: `python scripts/validate_gate_10_readiness.py --threshold 0.95`

---

## 10. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - Validating upstream approvals and artifact completeness...
[MASTER RAY™ | PHASE 1 COMPLETE] - Intake validation succeeded. Evidence: intake-validation-report.json.
[MASTER RAY™ | PHASE 2 START] - Rehearsing deployment on staging environment...
[MASTER RAY™ | PHASE 3 START] - Verifying rollback and recovery procedures...
[MASTER RAY™ | PHASE 4 START] - Compiling pre-deployment readiness package for release approval...
[MASTER RAY™ | PHASE 4 COMPLETE] - Pre-deployment package ready. Evidence: PRE-DEPLOYMENT-PACKAGE.zip.
[RAY ERROR] - "Failed at {step}. Reason: {explanation}. Awaiting instructions."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Pre-deployment validation complete. Evidence prepared:
> - PRE-DEPLOYMENT-PACKAGE.zip
> - readiness-approval.json
>
> Confirm readiness to transition to Protocol 15?"
```

### Error Handling:
```
[RAY GATE FAILED: Deployment Rehearsal Gate]
> "Quality gate 'Deployment Rehearsal Gate' failed.
> Criteria: Rehearsal success and test coverage ≥ 90%
> Actual: {result}
> Required action: Review automation logs, remediate failures, rerun rehearsal.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 10. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_10.py

# Quality gate automation
python scripts/validate_gate_10_intake.py --drift-threshold low
python scripts/validate_gate_10_readiness.py --threshold 0.95

# Evidence aggregation
python scripts/aggregate_evidence_10.py --output .artifacts/pre-deployment/
```

### CI/CD Integration:
```yaml
# GitHub Actions workflow integration
name: Protocol 21 Validation
on: [push]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Run Protocol 21 Gates
        run: python scripts/run_protocol_10_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Review staging parity via infrastructure dashboards and log results.
2. Manually confirm deployment rehearsal steps using runbooks.
3. Document results in `.artifacts/protocol-21/manual-validation-log.md`

---

## 10. HANDOFF CHECKLIST



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

### Handoff to Protocol 15:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 15: Production Deployment & Release Management

**Evidence Package:**
- `PRE-DEPLOYMENT-PACKAGE.zip` - Comprehensive readiness evidence
- `readiness-approval.json` - Stakeholder go/no-go decision record

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/15-production-deployment.md
```

---

## 10. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `intake-validation-report.json` | `.artifacts/pre-deployment/` | Confirms prerequisite readiness | Protocol 21 Gates |
| `staging-parity-report.json` | `.artifacts/pre-deployment/` | Documents config parity | Protocol 21 |
| `staging-test-results.json` | `.artifacts/pre-deployment/` | Captures rehearsal test outcomes | Protocol 15/12 |
| `rollback-verification-report.json` | `.artifacts/pre-deployment/` | Validates rollback readiness | Protocol 20 |
| `PRE-DEPLOYMENT-PACKAGE.zip` | `.artifacts/pre-deployment/` | Final readiness package | Protocol 15 |


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
| Gate 2 Pass Rate | ≥ 95% | [TBD] | ⏳ |
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
