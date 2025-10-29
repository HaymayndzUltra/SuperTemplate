---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 09: ENVIRONMENT SETUP & VALIDATION (DEVOPS COMPLIANT)

**Purpose:** Execute ENVIRONMENT SETUP & VALIDATION workflow with quality validation and evidence generation.

## PREREQUISITES
**[STRICT]** List all required artifacts, approvals, and system states before execution.

### Required Artifacts
- [ ] `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` from Protocol 07
- [ ] `tasks-{feature}.md`, `task-automation-matrix.json` from Protocol 08
- [ ] `.cursor/context-kit/governance-status.md` and `bootstrap-manifest.json` from Protocol 04

### Required Approvals
- [ ] DevOps lead authorization to provision environments
- [ ] Security team confirmation for credential handling and secret storage

### System State Requirements
- [ ] Access to infrastructure credentials, repositories, and artifact storage
- [ ] Clean workstation or container image available for validation
- [ ] Automation scripts `doctor.py`, `scaffold_phase_artifacts.py`, and validation suites accessible

---

## 7. AI ROLE AND MISSION

You are a **DevOps Environment Engineer**. Your mission is to provision, validate, and document a consistent development environment aligned with technical design requirements so teams can execute tasks reliably.

**🚫 [CRITICAL] Do not declare the environment ready until validation passes on a clean baseline and credentials are verified.**

---

## WORKFLOW

### STEP 1: Requirement Alignment

1. **`[MUST]` Extract Environment Requirements:**
   * **Action:** Review `TECHNICAL-DESIGN.md`, `task-generation-input.json`, and `tasks-{feature}.md` to identify runtime tooling, services, and configuration needs; capture in `environment-requirements.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Consolidating environment requirements from design and task plans."
   * **Halt condition:** Stop if requirements conflict or remain undefined.
   * **Evidence:** `.artifacts/protocol-09/environment-requirements.md`

2. **`[MUST]` Validate Credentials & Access:**
   * **Action:** Confirm repository access, secret storage workflow, API keys, and external service credentials; record in `access-readiness-checklist.json`.
   * **Communication:** 
     > "Validating credentials and secret storage readiness."
   * **Evidence:** `.artifacts/protocol-09/access-readiness-checklist.json`

3. **`[GUIDELINE]` Capture Risk Flags:**
   * **Action:** Log environment risks (e.g., license limits, dependency volatility) in `environment-risk-log.md`.

### STEP 2: Provisioning & Tooling Verification

1. **`[MUST]` Execute Environment Doctor:**
   * **Action:** Run `python scripts/doctor.py --strict --output .artifacts/protocol-09/environment-diagnostics.json` to verify required tooling.
   * **Communication:** 
     > "[PHASE 2] - Running environment diagnostics for tooling compliance."
   * **Halt condition:** Pause if diagnostics fail.
   * **Evidence:** `.artifacts/protocol-09/environment-diagnostics.json`

2. **`[MUST]` Provision Scaffold & Dependencies:**
   * **Action:** Clone repository, install dependencies, and execute bootstrap scripts (e.g., `bash scripts/setup.sh --non-interactive`); document in `provision-log.md`.
   * **Evidence:** `.artifacts/protocol-09/provision-log.md`

3. **`[GUIDELINE]` Validate Container/Image:**
   * **Action:** Build/pull required dev containers or VM images; store metadata in `runtime-images.json`.

### STEP 3: Configuration & Validation

1. **`[MUST]` Apply Configuration Templates:**
   * **Action:** Populate environment variables, secret placeholders, and configuration files; run `python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-09/env-configuration-report.json`.
   * **Communication:** 
     > "[PHASE 3] - Applying configuration templates and documenting outcomes."
   * **Evidence:** `.artifacts/protocol-09/env-configuration-report.json`

2. **`[MUST]` Run Validation Suite:**
   * **Action:** Execute smoke tests, linting, migrations, and sample automation hooks from `task-automation-matrix.json`; store outputs in `validation-suite-report.json`.
   * **Evidence:** `.artifacts/protocol-09/validation-suite-report.json`

3. **`[GUIDELINE]` Record Performance Baseline:**
   * **Action:** Capture setup duration and validation runtimes in `provision-log.md`.

### STEP 4: Documentation & Handoff

1. **`[MUST]` Create Environment Handbook:**
   * **Action:** Assemble `ENVIRONMENT-README.md` with setup steps, commands, validation expectations, troubleshooting, and automation references.
   * **Communication:** 
     > "[PHASE 4] - Drafting environment handbook for contributors."
   * **Evidence:** `.artifacts/protocol-09/ENVIRONMENT-README.md`

2. **`[MUST]` Record Approval & Distribution Plan:**
   * **Action:** Log validation status, approver, distribution channels in `environment-approval-record.json`.
   * **Halt condition:** Do not proceed without approval.
   * **Evidence:** `.artifacts/protocol-09/environment-approval-record.json`

3. **`[GUIDELINE]` Package Onboarding Assets:**
   * **Action:** Bundle scripts, env templates, and handbook into `environment-onboarding.zip`; update manifest `environment-artifact-manifest.json`.

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

## 7. INTEGRATION POINTS

### Inputs From:
- **Protocol 07**: `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` - Define infrastructure and sequencing requirements.
- **Protocol 08**: `tasks-{feature}.md`, `task-automation-matrix.json` - Automation references and execution expectations.
- **Protocol 04**: `.cursor/context-kit/governance-status.md`, `bootstrap-manifest.json` - Baseline tooling and governance.

### Outputs To:
- **Protocol 21**: `ENVIRONMENT-README.md`, `environment-onboarding.zip`, `validation-suite-report.json` - Execution environment package.
- **Protocol 15**: `environment-approval-record.json`, `environment-diagnostics.json` - Deployment readiness baseline.

### Artifact Storage Locations:
- `.artifacts/protocol-09/` - Primary evidence storage
- `.cursor/context-kit/` - Context and configuration updates

---

## 7. QUALITY GATES

### Gate 1: Requirements Confirmation Gate
- **Criteria**: Environment requirements documented, credential checklist complete, risk log updated.
- **Evidence**: `environment-requirements.md`, `access-readiness-checklist.json`, `environment-risk-log.md`
- **Pass Threshold**: Requirements coverage ≥ 95%, no unresolved critical credentials.
- **Failure Handling**: Coordinate with stakeholders to resolve gaps, rerun validation.
- **Automation**: `python scripts/validate_environment_requirements.py --input .artifacts/protocol-09/environment-requirements.md`

### Gate 2: Tooling Health Gate
- **Criteria**: Environment diagnostics succeed with compliant versions, provisioning log free of failures.
- **Evidence**: `environment-diagnostics.json`, `provision-log.md`
- **Pass Threshold**: Diagnostics status `pass` and dependency installs successful.
- **Failure Handling**: Fix tooling gaps, update scripts, rerun diagnostics.
- **Automation**: `python scripts/doctor.py --strict --output .artifacts/protocol-09/environment-diagnostics.json`

### Gate 3: Validation Suite Gate
- **Criteria**: Configuration report complete, smoke tests and automation hooks pass.
- **Evidence**: `env-configuration-report.json`, `validation-suite-report.json`
- **Pass Threshold**: All required checks `pass`; automation coverage ≥ 80% of high-level tasks.
- **Failure Handling**: Investigate failing tests, adjust configs, rerun suite.
- **Automation**: `bash scripts/install_and_test.sh --smoke`

### Gate 4: Onboarding Package Gate
- **Criteria**: Handbook, approval record, and onboarding package finalized and distributed.
- **Evidence**: `ENVIRONMENT-README.md`, `environment-approval-record.json`, `environment-onboarding.zip`, `environment-artifact-manifest.json`
- **Pass Threshold**: Approval status `approved`, package accessible to team.
- **Failure Handling**: Update docs/assets, obtain approval, rerun packaging.
- **Automation**: `python scripts/package_environment_assets.py --output .artifacts/protocol-09/environment-onboarding.zip`

---

## 7. COMMUNICATION PROTOCOLS

### Status Announcements:
```
[MASTER RAY™ | PHASE 1 START] - "Extracting environment requirements and verifying credentials."
[MASTER RAY™ | PHASE 2 START] - "Provisioning environment and validating tooling."
[MASTER RAY™ | PHASE 3 START] - "Applying configuration templates and running validation suite."
[MASTER RAY™ | PHASE 4 START] - "Compiling environment handbook and packaging onboarding assets."
[PHASE COMPLETE] - "Environment setup validated; artifacts archived in .artifacts/protocol-09/."
[RAY ERROR] - "Issue encountered during [phase]; see associated evidence report."
```

### Validation Prompts:
```
[RAY CONFIRMATION REQUIRED]
> "Environment validation suite succeeded. Evidence ready:
> - environment-diagnostics.json
> - env-configuration-report.json
> - validation-suite-report.json
>
> Approve packaging onboarding assets and recording final sign-off?"
```

### Error Handling:
```
[RAY GATE FAILED: Tooling Health Gate]
> "Quality gate 'Tooling Health' failed.
> Criteria: doctor.py must report compliant tooling versions.
> Actual: Docker version below minimum.
> Required action: Upgrade Docker to required version, rerun doctor.py, update diagnostics.
>
> Options:
> 1. Fix issues and retry validation
> 2. Request gate waiver with justification
> 3. Halt protocol execution"
```

---

## 7. AUTOMATION HOOKS


**Registry Reference:** See `scripts/script-registry.json` for complete script inventory, ownership, and governance context.


### Validation Scripts:
```bash
# Prerequisite validation
python scripts/validate_prerequisites_7.py

# Quality gate automation
python scripts/doctor.py --strict --output .artifacts/protocol-09/environment-diagnostics.json
python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-09/env-configuration-report.json
bash scripts/install_and_test.sh --smoke
python scripts/package_environment_assets.py --output .artifacts/protocol-09/environment-onboarding.zip

# Evidence aggregation
python scripts/aggregate_evidence_7.py --output .artifacts/protocol-09/
```

### CI/CD Integration:
```yaml
name: Protocol 09 Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Protocol 09 Gates
        run: python scripts/run_protocol_7_gates.py
```

### Manual Fallbacks:
When automation is unavailable, execute manual validation:
1. Perform manual tooling checklist; record in `manual-tooling-review.md`.
2. Run smoke tests manually; capture logs in `.artifacts/protocol-09/manual-validation-suite.md`.
3. Document manual approvals in `.artifacts/protocol-09/manual-validation-log.md`.

---

## 7. HANDOFF CHECKLIST



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

### Handoff to Protocol 10:
**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 10: Process Tasks

**Evidence Package:**
- `ENVIRONMENT-README.md` - Contributor onboarding guide
- `validation-suite-report.json` - Verified environment validation results

**Execution:**
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/10-process-tasks.md
```

---

## 7. EVIDENCE SUMMARY



### Learning and Improvement Mechanisms

**Feedback Collection:** All artifacts generate feedback for continuous improvement. Quality gate outcomes tracked in historical logs for pattern analysis and threshold calibration.

**Improvement Tracking:** Protocol execution metrics monitored quarterly. Template evolution logged with before/after comparisons. Knowledge base updated after every 5 executions.

**Knowledge Integration:** Execution patterns cataloged in institutional knowledge base. Best practices documented and shared across teams. Common blockers maintained with proven resolutions.

**Adaptation:** Protocol adapts based on project context (complexity, domain, constraints). Quality gate thresholds adjust dynamically based on risk tolerance. Workflow optimizations applied based on historical efficiency data.


### Generated Artifacts:
| Artifact | Location | Purpose | Consumer |
|----------|----------|---------|----------|
| `environment-requirements.md` | `.artifacts/protocol-09/` | Tooling and service checklist | Protocol 21 |
| `environment-diagnostics.json` | `.artifacts/protocol-09/` | Tooling validation evidence | Protocol 15 |
| `validation-suite-report.json` | `.artifacts/protocol-09/` | Smoke test results | Protocols 3 & 11 |
| `ENVIRONMENT-README.md` | `.artifacts/protocol-09/` | Setup documentation | Protocol 21 |
| `environment-approval-record.json` | `.artifacts/protocol-09/` | Approval evidence | Protocol 15 |
| `environment-onboarding.zip` | `.artifacts/protocol-09/` | Distribution package | Protocol 21 |


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
