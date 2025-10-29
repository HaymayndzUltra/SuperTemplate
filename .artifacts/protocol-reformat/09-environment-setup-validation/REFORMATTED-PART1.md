---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 09: ENVIRONMENT SETUP & VALIDATION (DEVOPS COMPLIANT)

**Purpose:** Execute ENVIRONMENT SETUP & VALIDATION workflow with quality validation and evidence generation.

## 1. PREREQUISITES
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Setting rules and standards for required artifacts, approvals, and system states before execution -->

**[STRICT]** List all required artifacts, approvals, and system states before execution.

### 1.1 Required Artifacts
- **`[MUST]`** `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` from Protocol 07
- **`[MUST]`** `tasks-{feature}.md`, `task-automation-matrix.json` from Protocol 08
- **`[MUST]`** `.cursor/context-kit/governance-status.md` and `bootstrap-manifest.json` from Protocol 04

### 1.2 Required Approvals
- **`[MUST]`** DevOps lead authorization to provision environments
- **`[MUST]`** Security team confirmation for credential handling and secret storage

### 1.3 System State Requirements
- **`[MUST]`** Access to infrastructure credentials, repositories, and artifact storage
- **`[MUST]`** Clean workstation or container image available for validation
- **`[MUST]`** Automation scripts `doctor.py`, `scaffold_phase_artifacts.py`, and validation suites accessible

---

## 2. AI ROLE AND MISSION
<!-- [Category: GUIDELINES-FORMATS] -->
<!-- Why: Establishing role definition and mission standards -->

**`[STRICT]` Role Definition:**
You are a **DevOps Environment Engineer**. Your mission is to provision, validate, and document a consistent development environment aligned with technical design requirements so teams can execute tasks reliably.

**🚫 [CRITICAL] Directive:**
Do not declare the environment ready until validation passes on a clean baseline and credentials are verified.

---

## 3. WORKFLOW
<!-- [Category: EXECUTION-FORMATS - Mixed variants by step] -->

### STEP 1: Requirement Alignment
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple workflow steps for extracting requirements and validating access -->

1. **`[MUST]` Extract Environment Requirements:**
   * **Action:** Review `TECHNICAL-DESIGN.md`, `task-generation-input.json`, and `tasks-{feature}.md` to identify runtime tooling, services, and configuration needs; capture in `environment-requirements.md`.
   * **Communication:** 
     > "[MASTER RAY™ | PHASE 1 START] - Consolidating environment requirements from design and task plans."
   * **Halt condition:** Stop if requirements conflict or remain undefined.
   * **Evidence:** `.artifacts/protocol-09/environment-requirements.md`
   * **Validation:** All environment dependencies documented

2. **`[MUST]` Validate Credentials & Access:**
   * **Action:** Confirm repository access, secret storage workflow, API keys, and external service credentials; record in `access-readiness-checklist.json`.
   * **Communication:** 
     > "Validating credentials and secret storage readiness."
   * **Evidence:** `.artifacts/protocol-09/access-readiness-checklist.json`
   * **Validation:** All critical credentials verified

3. **`[GUIDELINE]` Capture Risk Flags:**
   * **Action:** Log environment risks (e.g., license limits, dependency volatility) in `environment-risk-log.md`.
   * **Evidence:** `.artifacts/protocol-09/environment-risk-log.md`
   * **Validation:** Risk assessment documented

### STEP 2: Provisioning & Tooling Verification
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward provisioning and diagnostic execution -->

1. **`[MUST]` Execute Environment Doctor:**
   * **Action:** Run `python scripts/doctor.py --strict --output .artifacts/protocol-09/environment-diagnostics.json` to verify required tooling.
   * **Communication:** 
     > "[PHASE 2] - Running environment diagnostics for tooling compliance."
   * **Halt condition:** Pause if diagnostics fail.
   * **Evidence:** `.artifacts/protocol-09/environment-diagnostics.json`
   * **Validation:** All required tools at compliant versions

2. **`[MUST]` Provision Scaffold & Dependencies:**
   * **Action:** Clone repository, install dependencies, and execute bootstrap scripts (e.g., `bash scripts/setup.sh --non-interactive`); document in `provision-log.md`.
   * **Evidence:** `.artifacts/protocol-09/provision-log.md`
   * **Validation:** All dependencies installed successfully

3. **`[GUIDELINE]` Validate Container/Image:**
   * **Action:** Build/pull required dev containers or VM images; store metadata in `runtime-images.json`.
   * **Evidence:** `.artifacts/protocol-09/runtime-images.json`
   * **Validation:** Container/image builds complete

### STEP 3: Configuration & Validation
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Simple configuration application and validation suite execution -->

1. **`[MUST]` Apply Configuration Templates:**
   * **Action:** Populate environment variables, secret placeholders, and configuration files; run `python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-09/env-configuration-report.json`.
   * **Communication:** 
     > "[PHASE 3] - Applying configuration templates and documenting outcomes."
   * **Evidence:** `.artifacts/protocol-09/env-configuration-report.json`
   * **Validation:** All configurations applied correctly

2. **`[MUST]` Run Validation Suite:**
   * **Action:** Execute smoke tests, linting, migrations, and sample automation hooks from `task-automation-matrix.json`; store outputs in `validation-suite-report.json`.
   * **Evidence:** `.artifacts/protocol-09/validation-suite-report.json`
   * **Validation:** All tests pass successfully

3. **`[GUIDELINE]` Record Performance Baseline:**
   * **Action:** Capture setup duration and validation runtimes in `provision-log.md`.
   * **Evidence:** Updated `.artifacts/protocol-09/provision-log.md`
   * **Validation:** Performance metrics recorded

### STEP 4: Documentation & Handoff
<!-- [Category: EXECUTION-BASIC] -->
<!-- Why: Straightforward documentation creation and handoff preparation -->

1. **`[MUST]` Create Environment Handbook:**
   * **Action:** Assemble `ENVIRONMENT-README.md` with setup steps, commands, validation expectations, troubleshooting, and automation references.
   * **Communication:** 
     > "[PHASE 4] - Drafting environment handbook for contributors."
   * **Evidence:** `.artifacts/protocol-09/ENVIRONMENT-README.md`
   * **Validation:** Complete documentation created

2. **`[MUST]` Record Approval & Distribution Plan:**
   * **Action:** Log validation status, approver, distribution channels in `environment-approval-record.json`.
   * **Halt condition:** Do not proceed without approval.
   * **Evidence:** `.artifacts/protocol-09/environment-approval-record.json`
   * **Validation:** Approval documented

3. **`[GUIDELINE]` Package Onboarding Assets:**
   * **Action:** Bundle scripts, env templates, and handbook into `environment-onboarding.zip`; update manifest `environment-artifact-manifest.json`.
   * **Evidence:** `.artifacts/protocol-09/environment-onboarding.zip`, `.artifacts/protocol-09/environment-artifact-manifest.json`
   * **Validation:** Package complete and accessible

---

## 4. REFLECTION & LEARNING
<!-- [Category: META-FORMATS] -->
<!-- Why: Meta-level retrospective and continuous improvement tracking -->

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
