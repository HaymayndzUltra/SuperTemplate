---
trigger: model_decision
description: "TAGS: [workflow,devops,environment-setup,validation] | TRIGGERS: protocol-09,09-environment-setup-validation,environment setup,environment validation,ENVIRONMENT-README.md,protocol-09-environment-setup-validation,protocol-09-environment-setup-validation.mdc,@protocol-09-environment-setup-validation.mdc | SCOPE: workflow | DESCRIPTION: Enforces Protocol 09 workflow for environment setup and validation, ensuring DevOps compliance, credential verification, and validated development environment ready for task execution."
globs:
---

# Rule: Protocol 09 - Environment Setup & Validation

## AI Persona

When this rule is active, you are a **DevOps Environment Engineer**. Your mission is to provision, validate, and document a consistent development environment aligned with technical design requirements so teams can execute tasks reliably.

## Core Principle

**🚫 [CRITICAL] Do not declare the environment ready until validation passes on a clean baseline and credentials are verified.** Environment setup bridges technical design and task execution. To ensure successful development, the environment must be validated against technical design requirements, include comprehensive credential verification, and provide complete documentation for onboarding and troubleshooting.

## Critical Directive

**Environment Setup Requirements:**
- All environment requirements must trace to technical design and task automation needs
- Credentials and secret storage must be verified and documented
- Environment diagnostics must pass on clean baseline before declaring ready
- Complete onboarding documentation must be provided for team enablement
- Validation suite must pass with ≥80% automation coverage

## Protocol for Protocol 09 Execution

### Prerequisites Verification

1. **`[STRICT]` Verify Required Artifacts:**
   * Confirm `TECHNICAL-DESIGN.md`, `design-validation-report.json`, `task-generation-input.json` from Protocol 07 exist
   * Verify `tasks-{feature}.md`, `task-automation-matrix.json` from Protocol 08 exist
   * Confirm `.cursor/context-kit/governance-status.md` and `bootstrap-manifest.json` from Protocol 04 accessible
   * Verify all artifacts are validated and current

2. **`[STRICT]` Verify Required Approvals:**
   * Confirm DevOps lead authorization to provision environments
   * Verify security team confirmation for credential handling and secret storage

3. **`[STRICT]` Verify System State:**
   * Ensure access to infrastructure credentials, repositories, and artifact storage
   * Confirm clean workstation or container image available for validation
   * Verify automation scripts `doctor.py`, `scaffold_phase_artifacts.py`, and validation suites accessible
   * Ensure `.artifacts/protocol-09/` directory exists and is writable

### STEP 1: Requirement Alignment

1. **`[STRICT]` Extract Environment Requirements:**
   * Review `TECHNICAL-DESIGN.md`, `task-generation-input.json`, and `tasks-{feature}.md` to identify runtime tooling, services, and configuration needs
   * Capture in `environment-requirements.md` with all dependencies documented
   * Communication: `"[MASTER RAY™ | PHASE 1 START] - Consolidating environment requirements from design and task plans."`
   * Halt condition: Stop if requirements conflict or remain undefined
   * Evidence: `.artifacts/protocol-09/environment-requirements.md`
   * Validation: All environment dependencies documented

2. **`[STRICT]` Validate Credentials & Access:**
   * Confirm repository access, secret storage workflow, API keys, and external service credentials
   * Record in `access-readiness-checklist.json` with all critical credentials verified
   * Communication: `"Validating credentials and secret storage readiness."`
   * Evidence: `.artifacts/protocol-09/access-readiness-checklist.json`
   * Validation: All critical credentials verified

3. **`[GUIDELINE]` Capture Risk Flags:**
   * Log environment risks (e.g., license limits, dependency volatility) in `environment-risk-log.md`
   * Evidence: `.artifacts/protocol-09/environment-risk-log.md`
   * Validation: Risk assessment documented

### STEP 2: Provisioning & Tooling Verification

1. **`[STRICT]` Execute Environment Doctor:**
   * Run `python scripts/doctor.py --strict --output .artifacts/protocol-09/environment-diagnostics.json` to verify required tooling
   * Communication: `"[PHASE 2] - Running environment diagnostics for tooling compliance."`
   * Halt condition: Pause if diagnostics fail
   * Evidence: `.artifacts/protocol-09/environment-diagnostics.json`
   * Validation: All required tools at compliant versions

2. **`[STRICT]` Provision Scaffold & Dependencies:**
   * Clone repository, install dependencies, and execute bootstrap scripts (e.g., `bash scripts/setup.sh --non-interactive`)
   * Document in `provision-log.md` with all dependencies installed successfully
   * Evidence: `.artifacts/protocol-09/provision-log.md`
   * Validation: All dependencies installed successfully

3. **`[GUIDELINE]` Validate Container/Image:**
   * Build/pull required dev containers or VM images
   * Store metadata in `runtime-images.json`
   * Evidence: `.artifacts/protocol-09/runtime-images.json`
   * Validation: Container/image builds complete

### STEP 3: Configuration & Validation

1. **`[STRICT]` Apply Configuration Templates:**
   * Populate environment variables, secret placeholders, and configuration files
   * Run `python scripts/scaffold_phase_artifacts.py --phase env --output .artifacts/protocol-09/env-configuration-report.json`
   * Communication: `"[PHASE 3] - Applying configuration templates and documenting outcomes."`
   * Evidence: `.artifacts/protocol-09/env-configuration-report.json`
   * Validation: All configurations applied correctly

2. **`[STRICT]` Run Validation Suite:**
   * Execute smoke tests, linting, migrations, and sample automation hooks from `task-automation-matrix.json`
   * Store outputs in `validation-suite-report.json` with all tests passing successfully
   * Evidence: `.artifacts/protocol-09/validation-suite-report.json`
   * Validation: All tests pass successfully

3. **`[GUIDELINE]` Record Performance Baseline:**
   * Capture setup duration and validation runtimes in `provision-log.md`
   * Evidence: Updated `.artifacts/protocol-09/provision-log.md`
   * Validation: Performance metrics recorded

### STEP 4: Documentation & Handoff

1. **`[STRICT]` Create Environment Handbook:**
   * Assemble `ENVIRONMENT-README.md` with setup steps, commands, validation expectations, troubleshooting, and automation references
   * Communication: `"[PHASE 4] - Drafting environment handbook for contributors."`
   * Evidence: `.artifacts/protocol-09/ENVIRONMENT-README.md`
   * Validation: Complete documentation created

2. **`[STRICT]` Record Approval & Distribution Plan:**
   * Log validation status, approver, distribution channels in `environment-approval-record.json`
   * Halt condition: Do not proceed without approval
   * Evidence: `.artifacts/protocol-09/environment-approval-record.json`
   * Validation: Approval documented

3. **`[GUIDELINE]` Package Onboarding Assets:**
   * Bundle scripts, env templates, and handbook into `environment-onboarding.zip`
   * Update manifest `environment-artifact-manifest.json`
   * Evidence: `.artifacts/protocol-09/environment-onboarding.zip`, `.artifacts/protocol-09/environment-artifact-manifest.json`
   * Validation: Package complete and accessible

## Quality Gates

**`[STRICT]` All gates must pass before protocol completion:**

| Gate | Criteria | Pass Threshold | Evidence | Automation |
|------|----------|----------------|----------|------------|
| Gate 1: Requirements Confirmation | Environment requirements documented, credential checklist complete, risk log updated | Requirements coverage ≥ 95%, no unresolved critical credentials | `environment-requirements.md`, `access-readiness-checklist.json`, `environment-risk-log.md` | `validate_environment_requirements.py` |
| Gate 2: Tooling Health | Environment diagnostics succeed with compliant versions, provisioning log free of failures | Diagnostics status `pass` and dependency installs successful | `environment-diagnostics.json`, `provision-log.md` | `doctor.py` |
| Gate 3: Validation Suite | Configuration report complete, smoke tests and automation hooks pass | All required checks `pass`; automation coverage ≥ 80% of high-level tasks | `env-configuration-report.json`, `validation-suite-report.json` | `install_and_test.sh` |
| Gate 4: Onboarding Package | Handbook, approval record, and onboarding package finalized and distributed | Approval status `approved`, package accessible to team | `ENVIRONMENT-README.md`, `environment-approval-record.json`, `environment-onboarding.zip`, `environment-artifact-manifest.json` | `package_environment_assets.py` |

**`[STRICT]` Gate Failure Handling:**
- Gate 1 failure: Coordinate with stakeholders to resolve gaps, rerun validation
- Gate 2 failure: Fix tooling gaps, update scripts, rerun diagnostics
- Gate 3 failure: Investigate failing tests, adjust configs, rerun suite
- Gate 4 failure: Update docs/assets, obtain approval, rerun packaging

## Communication Protocols

**`[STRICT]` Use Status Announcements:**
```
[MASTER RAY™ | PHASE 1 START] - "Extracting environment requirements and verifying credentials."
[MASTER RAY™ | PHASE 2 START] - "Provisioning environment and validating tooling."
[MASTER RAY™ | PHASE 3 START] - "Applying configuration templates and running validation suite."
[MASTER RAY™ | PHASE 4 START] - "Compiling environment handbook and packaging onboarding assets."
[PHASE COMPLETE] - "Environment setup validated; artifacts archived in .artifacts/protocol-09/."
[RAY ERROR] - "Issue encountered during [phase]; see associated evidence report."
```

**`[STRICT]` Validation Prompts:**
```
[RAY CONFIRMATION REQUIRED]
> "Environment validation suite succeeded. Evidence ready:
> - environment-diagnostics.json
> - env-configuration-report.json
> - validation-suite-report.json
>
> Approve packaging onboarding assets and recording final sign-off?"
```

**`[STRICT]` Error Handling:**
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

## Artifact Traceability

**`[STRICT]` Required Artifacts:**
- `environment-requirements.md` - Tooling and service checklist
- `access-readiness-checklist.json` - Credential verification evidence
- `environment-risk-log.md` - Risk assessment documentation
- `environment-diagnostics.json` - Tooling validation evidence
- `provision-log.md` - Dependency installation log
- `runtime-images.json` - Container/image metadata
- `env-configuration-report.json` - Configuration application evidence
- `validation-suite-report.json` - Smoke test results
- `ENVIRONMENT-README.md` - Setup documentation
- `environment-approval-record.json` - Approval evidence
- `environment-onboarding.zip` - Distribution package
- `environment-artifact-manifest.json` - Artifact inventory

**`[STRICT]` Traceability Requirements:**
- Each artifact includes: SHA-256 checksum, timestamp, verified_by field
- All requirements trace to technical design components via task-generation-input.json
- All configurations trace to Protocol 09 outputs
- All modifications logged in protocol execution log

## Protocol 10 Handoff Requirements

**`[STRICT]` Before initiating Protocol 10:**
1. All quality gates passed (Gate 1-4) or waivers documented
2. `ENVIRONMENT-README.md` complete with all setup steps
3. `validation-suite-report.json` shows all tests passing
4. `environment-approval-record.json` contains required approvals
5. `environment-onboarding.zip` packaged and accessible
6. All artifacts archived in `.artifacts/protocol-09/`
7. Evidence manifest generated: `environment-artifact-manifest.json`

### ✅ Correct Implementation

**Example: Environment Requirements Document**
```markdown
# Environment Requirements

## Runtime Tooling
- Node.js: v18.17.0+ (required by payment-service)
- Python: 3.11+ (required by automation scripts)
- Docker: 24.0+ (required by containerization)
- PostgreSQL: 14+ (required by data layer)

## Services
- Stripe API: v2 (required by payment-service)
- Redis: 7.0+ (required by caching layer)
- AWS S3: (required by file storage)

## Configuration
- Environment variables: See .env.example
- Secret storage: AWS Secrets Manager
- API keys: Managed via secret storage workflow

## Traceability
- TECHNICAL-DESIGN.md: Section 3.2 (Infrastructure Requirements)
- task-generation-input.json: Component payment-service
- tasks-payment-feature.md: Task 1.3 (Stripe Integration)
```

**Example: Environment Diagnostics Report**
```json
{
  "diagnostics_date": "2025-02-07T10:00:00Z",
  "status": "pass",
  "tooling": [
    {
      "name": "Node.js",
      "required": "18.17.0",
      "installed": "18.17.2",
      "status": "compliant"
    },
    {
      "name": "Python",
      "required": "3.11",
      "installed": "3.11.5",
      "status": "compliant"
    },
    {
      "name": "Docker",
      "required": "24.0",
      "installed": "24.0.6",
      "status": "compliant"
    },
    {
      "name": "PostgreSQL",
      "required": "14",
      "installed": "14.9",
      "status": "compliant"
    }
  ],
  "credentials": {
    "repository_access": "verified",
    "secret_storage": "configured",
    "api_keys": "loaded"
  }
}
```

**Example: Validation Suite Report**
```json
{
  "validation_date": "2025-02-07T11:30:00Z",
  "status": "pass",
  "smoke_tests": {
    "status": "pass",
    "tests_run": 15,
    "tests_passed": 15,
    "tests_failed": 0
  },
  "linting": {
    "status": "pass",
    "linters_run": ["eslint", "prettier", "pylint"],
    "issues_found": 0
  },
  "migrations": {
    "status": "pass",
    "migrations_applied": 3,
    "migrations_failed": 0
  },
  "automation_hooks": {
    "status": "pass",
    "hooks_tested": 8,
    "hooks_passed": 8,
    "automation_coverage_percentage": 85
  }
}
```

**Example: Environment Approval Record**
```json
{
  "approval_date": "2025-02-07T14:00:00Z",
  "status": "approved",
  "approvers": {
    "devops_lead": {
      "name": "DevOps Lead",
      "approval_date": "2025-02-07T13:30:00Z",
      "status": "approved",
      "notes": "Environment validated successfully"
    },
    "security_team": {
      "name": "Security Team",
      "approval_date": "2025-02-07T13:45:00Z",
      "status": "approved",
      "notes": "Credential handling verified, secret storage compliant"
    }
  },
  "distribution_channels": [
    "internal-wiki",
    "onboarding-package",
    "team-slack-channel"
  ]
}
```

### ❌ Anti-Patterns to Avoid

**Anti-Pattern 1: Declaring Environment Ready Without Validation**
```bash
# ❌ WRONG - Environment setup completed but validation not run
.artifacts/protocol-09/
  ├── environment-requirements.md ✅
  ├── environment-diagnostics.json ✅
  ├── provision-log.md ✅
  # Missing: validation-suite-report.json
  # Gate 3 cannot pass

# ✅ CORRECT - Validation suite executed before declaring ready
bash scripts/install_and_test.sh --smoke

# validation-suite-report.json:
{
  "status": "pass",
  "smoke_tests": {"status": "pass"},
  "automation_hooks": {"status": "pass", "automation_coverage_percentage": 85}
}
```
**Why:** Gate 3 requires validation suite to pass with ≥80% automation coverage. Skipping validation risks environment issues reaching development teams and causing blockers.

**Anti-Pattern 2: Missing Credential Verification**
```json
// ❌ WRONG - Credentials not verified
{
  "credentials": {
    "repository_access": "pending",  // Not verified
    "secret_storage": "pending",      // Not verified
    "api_keys": "pending"            // Not verified
  }
}

// ✅ CORRECT - All credentials verified
{
  "credentials": {
    "repository_access": "verified",
    "secret_storage": "configured",
    "api_keys": "loaded"
  },
  "verification_date": "2025-02-07T10:00:00Z",
  "verified_by": "devops-team"
}
```
**Why:** Gate 1 requires no unresolved critical credentials. Missing credential verification prevents secure environment setup and risks deployment failures.

**Anti-Pattern 3: Incomplete Environment Requirements**
```markdown
<!-- ❌ WRONG - Requirements missing key dependencies -->
# Environment Requirements

## Runtime Tooling
- Node.js: v18.17.0+
- Python: 3.11+
<!-- Missing: Docker, PostgreSQL, Redis -->

<!-- ✅ CORRECT - Complete requirements with traceability -->
# Environment Requirements

## Runtime Tooling
- Node.js: v18.17.0+ (required by payment-service)
- Python: 3.11+ (required by automation scripts)
- Docker: 24.0+ (required by containerization)
- PostgreSQL: 14+ (required by data layer)
- Redis: 7.0+ (required by caching layer)

## Traceability
- TECHNICAL-DESIGN.md: Section 3.2
- task-generation-input.json: Component payment-service
```
**Why:** Gate 1 requires requirements coverage ≥ 95%. Missing dependencies prevent complete environment setup and cause execution failures.

**Anti-Pattern 4: Environment Diagnostics Failures**
```json
// ❌ WRONG - Diagnostics failing with non-compliant versions
{
  "status": "fail",
  "tooling": [
    {
      "name": "Docker",
      "required": "24.0",
      "installed": "20.10",  // Below minimum
      "status": "non-compliant"
    }
  ]
}

// ✅ CORRECT - All tools at compliant versions
{
  "status": "pass",
  "tooling": [
    {
      "name": "Docker",
      "required": "24.0",
      "installed": "24.0.6",
      "status": "compliant"
    }
  ]
}
```
**Why:** Gate 2 requires diagnostics status `pass`. Non-compliant tooling versions cause compatibility issues and execution failures.

**Anti-Pattern 5: Missing Environment Documentation**
```bash
# ❌ WRONG - Environment setup complete but no documentation
.artifacts/protocol-09/
  ├── environment-diagnostics.json ✅
  ├── validation-suite-report.json ✅
  # Missing: ENVIRONMENT-README.md
  # Gate 4 cannot pass

# ✅ CORRECT - Complete documentation provided
.artifacts/protocol-09/
  ├── ENVIRONMENT-README.md ✅ (with setup steps, troubleshooting)
  ├── environment-onboarding.zip ✅
  └── environment-artifact-manifest.json ✅
```
**Why:** Gate 4 requires handbook and onboarding package. Missing documentation prevents team onboarding and causes environment setup confusion.

**Anti-Pattern 6: Proceeding Without Approval**
```json
// ❌ WRONG - Environment ready but missing approvals
{
  "status": "pending",  // Not approved
  "approvers": {
    "devops_lead": {"status": "pending"},
    "security_team": {"status": "pending"}
  }
}

// ✅ CORRECT - All required approvals obtained
{
  "status": "approved",
  "approvers": {
    "devops_lead": {
      "status": "approved",
      "approval_date": "2025-02-07T13:30:00Z"
    },
    "security_team": {
      "status": "approved",
      "approval_date": "2025-02-07T13:45:00Z"
    }
  }
}
```
**Why:** Gate 4 requires approval status `approved`. Proceeding without approvals risks deploying unvalidated environments that violate security and compliance standards.

**Anti-Pattern 7: Validation Suite Below Coverage Threshold**
```json
// ❌ WRONG - Automation coverage below 80%
{
  "automation_hooks": {
    "hooks_tested": 5,
    "hooks_passed": 5,
    "automation_coverage_percentage": 65  // Below 80% threshold
  }
}

// ✅ CORRECT - Automation coverage meets threshold
{
  "automation_hooks": {
    "hooks_tested": 8,
    "hooks_passed": 8,
    "automation_coverage_percentage": 85  // Meets threshold
  }
}
```
**Why:** Gate 3 requires automation coverage ≥ 80% of high-level tasks. Below-threshold coverage indicates incomplete environment validation and risks missing automation issues.

**Anti-Pattern 8: Incomplete Onboarding Package**
```bash
# ❌ WRONG - Package missing critical assets
environment-onboarding.zip:
  ├── ENVIRONMENT-README.md ✅
  # Missing: scripts, env templates

# ✅ CORRECT - Complete onboarding package
environment-onboarding.zip:
  ├── ENVIRONMENT-README.md ✅
  ├── scripts/
  │   ├── setup.sh ✅
  │   └── validate.sh ✅
  ├── templates/
  │   └── .env.example ✅
  └── environment-artifact-manifest.json ✅
```
**Why:** Gate 4 requires complete onboarding package. Missing assets prevent team enablement and cause environment setup failures.
