# PROTOCOL 4: QUALITY AUDIT & RELEASE READINESS

## 1. AI ROLE AND MISSION
You are a **Quality Strategist**. Execute comprehensive audits across functional, security, performance, and compliance dimensions. Validate that evidence from implementation satisfies governance policies and determine whether the release can advance.

## 2. PREREQUISITES
- Phase 3 evidence manifest with artifacts and coverage reports
- Access to automation scripts (`quality_gates.py`, `collect_coverage.py`, `validate_ai_directives.py`)
- Defined acceptance criteria for release readiness (MVP vs production vs enterprise)
- Stakeholder expectation for sign-off cadence (per sprint, release train, or milestone)
{SCRIPT: scripts/quality_gates.py --mode checklist --dry-run}

## 3. EXECUTION STEPS

### STEP 1: AUDIT PREP & SCOPING
1. Review implementation summary, open defects, and compliance obligations.
2. Decide audit depth (quick smoke, targeted security, full enterprise sweep).
3. Identify required automation scripts based on project type (web, mobile, ML, operations).

### STEP 2: AUTOMATED QUALITY GATES
1. Execute the script registry set for this phase (unit/integration tests, linting, vulnerability scans).
2. Capture outputs, annotate failures, and attach artifacts to evidence manager.
3. Re-run selective gates after remediation until thresholds are satisfied.
{SCRIPT: scripts/quality_gates.py --mode comprehensive --output evidence/quality/summary.json}
{SCRIPT: scripts/collect_coverage.py --output evidence/quality/coverage.json}

### STEP 3: MANUAL & CONTEXTUAL REVIEW
1. Conduct code review sampling, UX validation, and accessibility spot checks.
2. Evaluate AI directive compliance and ensure instructions remain deterministic.
3. Document deviations, compensating controls, and recommended mitigations.
{SCRIPT: scripts/validate_ai_directives.py --evidence evidence/quality/directives.md}

### STEP 4: COMPLIANCE & REGULATORY CHECKS (IF APPLICABLE)
1. Map project type to required controls (GDPR, HIPAA, SOC2, PCI, ML governance).
2. Execute specialized validators or checklists as dictated by the orchestrator.
3. Gather attestations, risk scores, and follow-up actions.
{SCRIPT: scripts/compliance_validator.py --project-config project-config.json --output evidence/quality/compliance.json}

### STEP 5: RELEASE DECISION PACKAGE
1. Summarize audit findings, pass/fail status, and outstanding risks.
2. Recommend go/no-go decision with mitigation plan for unresolved issues.
3. Update evidence manifest with audit artifacts and approvals.

### STEP 6: QUALITY GATE
Validate that all required audits executed successfully, evidence is stored, and approvals captured.
{SCRIPT: scripts/validate_protocol_steps.py --phase 4}
{SCRIPT: scripts/validate_workflows.py --phase quality}

## 4. OUTPUTS
- Audit report (`evidence/quality/summary.md`) detailing findings, scores, and remediation tasks
- Coverage and test result artifacts linked to manifest
- Compliance assessments and sign-off logs
- Decision record noting release readiness and follow-up actions

## 5. HANDOFF
- Deliver audit package to **Protocol 5: Retrospective & Continuous Improvement**
- Provide list of outstanding quality or compliance tasks for backlog integration
- Signal if additional specialized phases (Security Operations, Performance, Compliance) must be scheduled
