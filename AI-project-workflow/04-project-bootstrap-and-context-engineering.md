# PROTOCOL 04: PROJECT BOOTSTRAP & CONTEXT ENGINEERING

**Version**: 3.0.0 (Consolidated from Protocol 04 + 05)  
**Phase**: Phase 0: Foundation & Discovery  
**Purpose**: Complete project bootstrap with environment setup, scaffold generation, codebase analysis, and context engineering

---

## PREREQUISITES

### Required Artifacts
**[STRICT]** All artifacts must be present before execution:

- **PROJECT-BRIEF.md** from Protocol 03
  - Format: Validated project summary document
  - Validation: Structure and content completeness
  - Location: Project root

- **project-brief-validation-report.json** from Protocol 03
  - Format: JSON validation report
  - Requirements: Status = "PASS", score ≥ 0.95
  - Location: `.artifacts/protocol-03/`

- **BRIEF-APPROVAL-RECORD.json** from Protocol 03
  - Format: JSON record of approvals
  - Requirements: All required signatures present
  - Location: `.artifacts/protocol-03/`

### Required Approvals
**[STRICT]** Following approvals must be documented:

- **Delivery Lead Authorization**
  - Purpose: Permission to bootstrap repository
  - Documentation: Recorded in approval log

- **DevOps Confirmation**
  - Purpose: Confirm environment isolation from production
  - Documentation: Environment separation attestation

### System State Requirements
**[STRICT]** System must meet requirements:

- **Script Access**: Read/execute access to `scripts/` directory
- **Write Permissions**: Write access to `.cursor/` and `.artifacts/` directories
- **Environment Health**: `scripts/doctor.py` returning success (exit code 0)

---

## AI ROLE AND MISSION

### Role Definition
You are an **AI Codebase Analyst & Context Architect**. Your mission is to:
1. Bootstrap project infrastructure (new projects)
2. Analyze existing codebase (existing projects)
3. Extract architecture principles
4. Configure governance tooling
5. Create comprehensive context kit

### Critical Directive
**🚫 [CRITICAL] Never modify existing production application code or delete repository assets outside governed directories.**

### Operational Boundaries
- **Permitted**: Modify `.cursor/`, `.artifacts/`, generated scaffold files, documentation
- **Prohibited**: Alter existing application code, production configs, user data
- **Validation**: All operations logged and reversible

---

## WORKFLOW

### STEP 1: Brief Validation & Environment Setup

1. **`[MUST]` Validate Project Brief:**
   ```bash
   python scripts/validate_brief.py \
     --path PROJECT-BRIEF.md \
     --output .artifacts/protocol-04/brief-validation-report.json
   ```
   * **Communication**: "[MASTER RAY™ | PHASE 1 START] - Validating Project Brief and environment"
   * **Evidence**: `.artifacts/protocol-04/brief-validation-report.json`
   * **Validation**: Exit code 0 and validation score ≥ 0.95
   * **Halt condition**: Stop if validation fails

2. **`[MUST]` Run Environment Doctor:**
   ```bash
   python scripts/doctor.py --strict
   ```
   * **Communication**: "Validating local environment and dependencies"
   * **Evidence**: `.artifacts/protocol-04/environment-report.json`
   * **Validation**: All checks passing (green status)
   * **Halt condition**: Stop if doctor reports missing critical dependencies

3. **`[MUST]` Confirm Tooling Requirements:**
   * **Action**: Ask whether team uses Cursor editor
   * **Communication**: "Confirming editor tooling for governance rules"
   * **Evidence**: `.artifacts/protocol-04/tooling-confirmation.log`
   * **Validation**: Tooling choice documented
   * **Halt condition**: Pause until tooling confirmation received

---

### STEP 2: Project Type Detection & Scaffold Generation

1. **`[MUST]` Detect Project Type:**
   * **Action**: Determine if NEW project (needs scaffold) or EXISTING project (needs analysis)
   * **Detection Logic**:
     - NEW: No existing source code, only PROJECT-BRIEF.md
     - EXISTING: Has source code directories (src/, app/, etc.)
   * **Communication**: "Detecting project type: NEW or EXISTING"
   * **Evidence**: `.artifacts/protocol-04/project-type-detection.json`
   * **Validation**: Project type clearly identified

2. **`[IF NEW PROJECT]` Generate Scaffold:**
   ```bash
   python scripts/generate_from_brief.py \
     --brief PROJECT-BRIEF.md \
     --output-root . \
     --in-place \
     --no-subdir \
     --no-cursor-assets \
     --force \
     --yes
   ```
   * **Communication**: "[PHASE 2] - Generating project scaffold from brief"
   * **Evidence**: `.artifacts/protocol-04/bootstrap-manifest.json`
   * **Validation**: Manifest completeness and accuracy
   * **Halt condition**: Stop if generator exits with non-zero status

3. **`[IF NEW PROJECT]` Validate Scaffold:**
   ```bash
   python scripts/validate_scaffold.py \
     --manifest .artifacts/protocol-04/bootstrap-manifest.json
   ```
   * **Communication**: "Validating scaffold integrity"
   * **Evidence**: `.artifacts/protocol-04/scaffold-validation-report.json`
   * **Validation**: Compliance score ≥ 98%

4. **`[IF EXISTING PROJECT]` Map Repository Structure:**
   * **Action**: Generate comprehensive tree of repository
   * **Communication**: "Mapping existing repository structure"
   * **Evidence**: `.artifacts/protocol-04/repo-structure.txt`
   * **Validation**: Structure completeness verified
   * **Halt condition**: Await user validation of key files

5. **`[IF EXISTING PROJECT]` Detect Tech Stack:**
   * **Action**: Analyze files to determine languages, frameworks, build tooling
   * **Communication**: "Detecting technology stack from codebase"
   * **Evidence**: `.cursor/bootstrap/detected-stack.json`
   * **Validation**: Stack detection coverage ≥ 90%

---

### STEP 3: Governance Rules Configuration

1. **`[IF CURSOR]` Configure Cursor Rule Structure:**
   * **Action**: Locate `master-rules` and `common-rules`, move to `.cursor/rules/`, rename `.md` → `.mdc`
   * **Communication**: "Migrating rules to Cursor-compatible `.mdc` format"
   * **Evidence**: `.artifacts/protocol-04/rule-migration-report.md`
   * **Validation**: All rules contain valid frontmatter

2. **`[MUST]` Normalize Project Rules:**
   ```bash
   python scripts/normalize_project_rules.py --target .cursor/rules/
   ```
   * **Communication**: "Normalizing governance rules"
   * **Evidence**: Rule files updated in `.cursor/rules/project-rules/`
   * **Validation**: Frontmatter normalized

3. **`[MUST]` Audit Rules:**
   ```bash
   python scripts/rules_audit_quick.py \
     --output .artifacts/protocol-04/rule-audit-report.md
   ```
   * **Communication**: "Auditing rule metadata integrity"
   * **Evidence**: `.artifacts/protocol-04/rule-audit-report.md`
   * **Validation**: Audit severity ≤ Medium

4. **`[GUIDELINE]` Generate Cursor Rules (if applicable):**
   * **Action**: If PROJECT-BRIEF.md exists, run `/Generate Cursor Rules --dry-run`, review, then run without `--dry-run`
   * **Evidence**: Generated rule files in `.cursor/rules/`
   * **Validation**: Rules align with project context

---

### STEP 4: Architecture Analysis & Principle Extraction

1. **`[IF EXISTING PROJECT]` Define Investigation Themes:**
   * **Action**: Generate thematic questions (security, data flow, conventions) based on detected stack
   * **Communication**: "[PHASE 4] - Establishing thematic investigation plan"
   * **Evidence**: `.artifacts/protocol-04/investigation-themes.md`
   * **Validation**: Themes cover critical aspects

2. **`[IF EXISTING PROJECT]` Perform Semantic Analysis:**
   * **Action**: Use search tools to examine code implementing each theme
   * **Communication**: "Executing semantic analysis to uncover architectural principles"
   * **Evidence**: `.artifacts/protocol-04/theme-findings.json`
   * **Validation**: Findings documented with code references

3. **`[MUST]` Synthesize Architecture Principles:**
   * **Action**: Translate findings into pragmatic principles
   * **Communication**: "Synthesizing architecture principles"
   * **Evidence**: `architecture-principles.md` (workspace root)
   * **Validation**: Principles actionable and specific
   * **Example**:
     ```markdown
     - Authentication relies on HMAC middleware (`src/middleware/validateHmac.ts`)
     - Error responses standardize `{ success: false, error }` envelope
     ```

4. **`[MUST]` Present Findings for Validation:**
   * **Action**: Share summary and outstanding questions; pause for user feedback
   * **Communication**: "Presenting bootstrap findings for validation"
   * **Evidence**: `.artifacts/protocol-04/validation-brief.md`
   * **Validation**: User feedback incorporated
   * **Halt condition**: Wait for user confirmation or corrections

---

### STEP 5: Context Kit Initialization

1. **`[MUST]` Initialize Context Kit Structure:**
   * **Action**: Create `.cursor/context-kit/` directories
   * **Communication**: "Initializing context kit with validated principles"
   * **Evidence**: `.cursor/context-kit/README.md`
   * **Validation**: Context kit structure created

2. **`[MUST]` Create Governance Status:**
   * **Action**: Document stack summary, governance status, next steps
   * **Communication**: "Creating governance status document"
   * **Evidence**: `.cursor/context-kit/governance-status.md`
   * **Validation**: Document completeness
   * **Example**:
     ```markdown
     ## Bootstrap Summary
     - Stack: Next.js + FastAPI + PostgreSQL
     - Governance: Rules normalized 2025-01-10
     - Next: Protocol 05b (Orchestration)
     ```

3. **`[GUIDELINE]` Inventory Template Packs:**
   * **Action**: List available template packs using TemplateRegistry
   * **Communication**: "Cataloging available template packs"
   * **Evidence**: `.cursor/context-kit/template-inventory.md`
   * **Validation**: Template inventory complete

4. **`[MUST]` Initialize Evidence Manager:**
   ```bash
   python scripts/evidence_manager.py init --path .artifacts/protocol-04/
   ```
   * **Communication**: "Initializing evidence tracking"
   * **Evidence**: `.artifacts/protocol-04/evidence-manifest.json`
   * **Validation**: Manifest initialization successful

---

### STEP 6: Documentation & Workflow Validation

1. **`[MUST]` Generate Documentation Plan:**
   * **Action**: Identify READMEs requiring creation or updates
   * **Communication**: "[PHASE 6] - Planning README updates"
   * **Evidence**: `.artifacts/protocol-04/documentation-plan.md`
   * **Validation**: Plan covers all necessary documentation

2. **`[MUST]` Produce or Update READMEs:**
   * **Action**: Create targeted READMEs capturing architecture, workflows, conventions
   * **Communication**: "Publishing README updates"
   * **Evidence**: `.artifacts/protocol-04/readme-updates/`
   * **Validation**: Each README approved by user

3. **`[MUST]` Validate Workflow Integration:**
   ```bash
   python scripts/validate_workflows.py \
     --mode bootstrap \
     --output .artifacts/protocol-04/workflow-validation-report.json
   ```
   * **Communication**: "Running workflow validation"
   * **Evidence**: `.artifacts/protocol-04/workflow-validation-report.json`
   * **Validation**: Status = "pass" in report
   * **Halt condition**: Stop if validation fails

4. **`[GUIDELINE]` Snapshot Context for Rollback:**
   * **Action**: Archive current `.cursor/context-kit/` for rollback
   * **Communication**: "Creating rollback snapshot"
   * **Evidence**: `.artifacts/protocol-04/pre-bootstrap-context.zip`
   * **Validation**: Archive integrity check

---

## QUALITY GATES

### Gate 1: Brief & Environment Validation
**Type**: Prerequisite  
**Purpose**: Verify approved Project Brief and environment readiness

**Pass Criteria**:
- Validation score ≥0.95 in `brief-validation-report.json`
- Environment doctor compliance score ≥0.92
- All critical tools available (Node, Python, npm/pip)

**Automation**:
```bash
python scripts/validate_prerequisites_04.py \
  --log .artifacts/protocol-04/prerequisites-log.json
```

**Failure Handling**:
- **Rollback**: Return to Protocol 03, remediate discrepancies
- **Notification**: Notify solutions architect when validation <0.95
- **Waiver**: Recorded in `.artifacts/protocol-04/gate-waivers.json` with approval

---

### Gate 2: Scaffold/Analysis Validation
**Type**: Execution  
**Purpose**: Ensure scaffold generation (NEW) or repository analysis (EXISTING) completed successfully

**Pass Criteria**:
- **NEW**: Scaffold compliance ≥98%, checksum variance = 0
- **EXISTING**: Stack detection coverage ≥90%, analysis plan approved

**Automation**:
```bash
# For NEW projects
python scripts/validate_scaffold.py \
  --manifest .artifacts/protocol-04/bootstrap-manifest.json

# For EXISTING projects
python scripts/validate_repo_mapping.py \
  --structure .artifacts/protocol-04/repo-structure.txt
```

**Failure Handling**:
- **Rollback**: Regenerate scaffold or re-run analysis
- **Notification**: Ping product owner when compliance <98%
- **Waiver**: Not applicable for NEW projects (mandatory)

---

### Gate 3: Governance Alignment
**Type**: Execution  
**Purpose**: Confirm rule normalization and audit outcomes

**Pass Criteria**:
- Rule audit severity ≤ Medium
- Metadata compliance score ≥0.95
- YAML frontmatter completeness = pass

**Automation**:
```bash
python scripts/rules_audit_quick.py \
  --output .artifacts/protocol-04/rule-audit-report.md
```

**Failure Handling**:
- **Rollback**: Re-run migration with corrected metadata
- **Notification**: Alert governance steward when compliance <0.95
- **Waiver**: Requires CTO approval, logged in `gate-waivers.json`

---

### Gate 4: Context & Workflow Validation
**Type**: Completion  
**Purpose**: Validate context kit, architecture principles, and workflow readiness

**Pass Criteria**:
- Workflow validation score ≥0.96
- Evidence manifest completeness = 100%
- Architecture principles documented
- Context kit complete (README, governance-status, template-inventory)

**Automation**:
```bash
python scripts/validate_workflows.py \
  --mode bootstrap \
  --output .artifacts/protocol-04/workflow-validation-report.json

python scripts/aggregate_evidence_04.py \
  --output .artifacts/protocol-04 \
  --protocol-id 04
```

**Failure Handling**:
- **Rollback**: Re-run context synchronization, rebuild evidence manifest
- **Notification**: Inform Protocol 05b owner if readiness <threshold
- **Waiver**: Only for sandbox environments with documented mitigation

---

## COMMUNICATION PROTOCOLS

### Status Announcements
```
[MASTER RAY™ | PHASE 1 START] - "Validating brief and environment"
[MASTER RAY™ | PHASE 2 START] - "Generating scaffold / Analyzing codebase"
[MASTER RAY™ | PHASE 3 START] - "Configuring governance rules"
[MASTER RAY™ | PHASE 4 START] - "Extracting architecture principles"
[MASTER RAY™ | PHASE 5 START] - "Initializing context kit"
[MASTER RAY™ | PHASE 6 START] - "Validating workflow integration"
[PHASE COMPLETE] - "Bootstrap complete; artifacts stored in .artifacts/protocol-04/"
[RAY ERROR] - "Issue encountered during [phase]; see report for remediation"
```

### Validation Prompts
```
[RAY CONFIRMATION REQUIRED]
> "Bootstrap operations complete. Evidence available:
> - brief-validation-report.json
> - environment-report.json
> - bootstrap-manifest.json (NEW) OR repo-structure.txt (EXISTING)
> - architecture-principles.md
> - workflow-validation-report.json
>
> Confirm readiness to activate Protocol 05b: Protocol Orchestration."
```

---

## INTEGRATION POINTS

### Inputs From
- **Protocol 03**:
  - `PROJECT-BRIEF.md` - Project requirements and scope
  - `project-brief-validation-report.json` - Validation evidence
  - `BRIEF-APPROVAL-RECORD.json` - Authorization records

### Outputs To
- **Protocol 05b** (Orchestration):
  - `bootstrap-manifest.json` - Generated scaffold inventory (NEW projects)
  - `architecture-principles.md` - Extracted principles (ALL projects)
  - `.cursor/context-kit/governance-status.md` - Context baseline
  - `.cursor/context-kit/README.md` - Context summary
  - `.cursor/bootstrap/detected-stack.json` - Tech stack (EXISTING projects)

- **Protocol 06** (Create PRD):
  - `architecture-principles.md` - Required for PRD alignment

- **Protocol 08** (Task Generation):
  - `.cursor/context-kit/` - Context for task generation
  - `template-inventory.md` - Available templates

---

## EVIDENCE SUMMARY

### Artifact Generation Table

| Artifact | Metrics | Location | Gate |
|----------|---------|----------|------|
| brief-validation-report.json | Score ≥0.95 | `.artifacts/protocol-04/` | Gate 1 |
| environment-report.json | Compliance ≥0.92 | `.artifacts/protocol-04/` | Gate 1 |
| bootstrap-manifest.json | Compliance ≥98% | `.artifacts/protocol-04/` | Gate 2 (NEW) |
| repo-structure.txt | Coverage ≥90% | `.artifacts/protocol-04/` | Gate 2 (EXISTING) |
| detected-stack.json | Coverage ≥90% | `.cursor/bootstrap/` | Gate 2 (EXISTING) |
| rule-audit-report.md | Severity ≤Medium | `.artifacts/protocol-04/` | Gate 3 |
| architecture-principles.md | Complete | Workspace root | Gate 4 |
| workflow-validation-report.json | Score ≥0.96 | `.artifacts/protocol-04/` | Gate 4 |
| evidence-manifest.json | Completeness 100% | `.artifacts/protocol-04/` | Gate 4 |
| governance-status.md | Status: synchronized | `.cursor/context-kit/` | Gate 4 |

### Storage Structure
- **Primary Evidence**: `.artifacts/protocol-04/` - All protocol artifacts
- **Context Assets**: `.cursor/context-kit/` - Context and configuration
- **Rule Files**: `.cursor/rules/` - Governance rules
- **Bootstrap Data**: `.cursor/bootstrap/` - Stack detection (EXISTING projects)

---

## HANDOFF CHECKLIST

### Pre-Handoff Validation
- [ ] All prerequisites met
- [ ] All workflow steps completed
- [ ] All quality gates passed (or waivers documented)
- [ ] All evidence artifacts captured
- [ ] All integration outputs generated
- [ ] Communication log complete

### Handoff to Protocol 05b

**[MASTER RAY™ | PROTOCOL COMPLETE]** Ready for Protocol 05b: Protocol Orchestration & Execution Planning

**Evidence Package**:
- `bootstrap-manifest.json` - Scaffold inventory (NEW) or analysis results (EXISTING)
- `architecture-principles.md` - Extracted principles for all projects
- `governance-status.md` - Context kit baseline
- `workflow-validation-report.json` - Readiness evidence

**Execution**:
```bash
# Trigger next protocol
@apply .cursor/ai-driven-workflow/05b-project-protocol-orchestration-v2.md
```

---

**END OF PROTOCOL 04**
