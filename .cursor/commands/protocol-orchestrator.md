# Intelligent Protocol Generator for Project-Specific Workflows

## System Analysis Summary

Based on my analysis of the ai-driven-template, I've identified:

### Current Structure

- **7 Core Protocols**: 00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective
- **60+ automation scripts** in `/scripts/` for validation, evidence collection, CI/CD integration
- **3-tier rule system**: master-rules (8), common-rules (10), project-rules (custom)
- **Template-based project generation**: Scripts for generating projects from briefs
- **Existing automation hooks**: Task validation, brief validation, evidence aggregation, workflow execution

### Key Insights

1. **Not all protocols are mandatory** - they should be selected based on project lifecycle needs
2. **Logical sequencing matters** - dependencies must be respected (e.g., can't test what hasn't been built)
3. **Project brief is the source of truth** - all decisions flow from understanding the brief
4. **Automation exists but needs orchestration** - scripts are available but not connected to protocol generation

## Proposed Solution: Meta-Protocol Generator

### Core Concept

A new "Protocol 00.5" that sits between the template clone and actual execution - an intelligent **Protocol Orchestrator** that:

1. Reads the project brief
2. Analyzes project type, stack, complexity, and lifecycle requirements
3. Decides which protocols are needed (use existing, edit, or create new)
4. Determines logical sequencing with dependencies
5. Generates sequentially-numbered command files in `.cursor/commands/`

### Architecture

```
PROJECT-BRIEF.md (user input)
         ↓
[Protocol Orchestrator]
         ↓
    Analysis Engine
    - Domain classifier (web/mobile/data/ml/infra)
    - Stack detector (frontend/backend/fullstack)
    - Complexity assessor (simple/moderate/complex)
    - Lifecycle mapper (MVP/production/enterprise)
         ↓
   Decision Engine
   - Protocol selector (which protocols needed?)
   - Protocol customizer (edit existing or create new?)
   - Dependency resolver (what order?)
   - Validation checks (completeness, logical flow)
         ↓
  Command Generator
  - Sequential numbering (01-, 02-, 03-)
  - Parameter injection (project-specific values)
  - Automation hook binding (link to scripts)
  - Rule alignment (associate relevant rules)
         ↓
.cursor/commands/
├── 00-analyze-brief.md (always first)
├── 01-bootstrap-context.md (usually needed)
├── 02-generate-requirements.md (conditional)
├── 03-design-architecture.md (conditional)
├── 04-generate-tasks.md (conditional)
├── 05-execute-implementation.md (conditional)
├── 06-quality-validation.md (usually needed)
└── 07-deployment-retrospective.md (conditional)
```

## Implementation Plan

### Phase 1: Create Protocol Orchestrator Command

**File**: `.cursor/commands/orchestrate-workflow.md`

This command will:

- Accept a project brief path as input
- Execute the orchestration logic
- Generate all necessary protocol commands
- Output a workflow execution roadmap

**Key Components**:

1. **Brief Parser**: Extract project metadata (type, stack, requirements, constraints)
2. **Protocol Library**: Reference all available protocols with metadata (purpose, prerequisites, outputs)
3. **Decision Matrix**: Rules for protocol selection based on brief characteristics
4. **Sequencer**: Topological sort for dependency resolution
5. **Command Generator**: Template-based command file creation

### Phase 2: Extend Existing Scripts

#### 2.1 Brief Analysis Enhancement

**Extend**: `scripts/generate_from_brief.py` (already exists)

Current functionality: Brief → project generation

**Add orchestration logic**:

- Extract project metadata (type, stack, complexity, lifecycle)
- Output JSON for protocol decision engine
- Integrate with existing `scripts/classify_domain.py`

```json
{
  "project_type": "web-app",
  "stack": {"frontend": "react", "backend": "node"},
  "complexity": "moderate",
  "lifecycle_phase": "mvp",
  "required_protocols": [...],
  "optional_protocols": [...],
  "custom_protocols_needed": [...]
}
```

#### 2.2 Protocol Decision Engine

**Extend**: `scripts/classify_domain.py` (already exists)

Current functionality: Domain classification with ML

**Add protocol mapping logic**:

- Map project characteristics to protocol requirements
- Apply decision rules (e.g., "MVP web app" → skip pre-production security)
- Handle special cases (data projects, mobile apps, etc.)
- Output protocol selection with reasoning

#### 2.3 Protocol Customization

**Extend**: `scripts/validate_protocol_steps.py` (already exists)

Current functionality: Protocol validation

**Add customization capabilities**:

- Take existing protocol as template
- Inject project-specific parameters
- Add/remove sections based on brief
- Maintain protocol integrity (gates, automation hooks)

#### 2.4 Command Sequencing

**Extend**: `scripts/lifecycle_tasks.py` (already exists)

Current functionality: Task lifecycle management

**Add sequencing logic**:

- Build dependency graph for protocols
- Detect circular dependencies
- Perform topological sort
- Generate execution order with parallel opportunities
- Validate logical flow

### Phase 3: Protocol Metadata Enhancement

**Extend existing**: `.cursor/ai-driven-workflow/` directory (already exists)

Current structure: Contains all protocol files and integration guides

**Add metadata to existing structure**:

**File**: `.cursor/ai-driven-workflow/protocol-metadata.json`

```json
{
  "00-client-discovery": {
    "purpose": "Transform job post into validated project brief",
    "prerequisites": [],
    "outputs": ["brief.md", "acceptance-criteria.md"],
    "mandatory_for": ["all"],
    "skip_if": ["brief_exists"],
    "complexity": "low",
    "estimated_duration": "30min"
  },
  "0-bootstrap": {
    "purpose": "Analyze codebase and setup context",
    "prerequisites": ["project_structure"],
    "outputs": ["context-kit/", "rules/"],
    "mandatory_for": ["new_projects"],
    "skip_if": ["context_exists"],
    "complexity": "medium",
    "estimated_duration": "1-2h"
  }
  // ... all other protocols
}
```

### Phase 4: Integration with Existing Systems

#### 4.1 Link to Automation Scripts

**Leverage existing**: All 60+ scripts in `/scripts/` directory

- Map protocols to existing validation scripts (`validate_brief.py`, `validate_tasks.py`, etc.)
- Bind evidence collection hooks (`evidence_report.py`)
- Connect CI/CD workflow triggers (`run_workflow.py`)

#### 4.2 Rule Alignment

**Use existing**: 3-tier rule system (master-rules, common-rules, project-rules)

- Associate protocols with relevant rules
- Ensure rule discovery happens per protocol
- Validate rule compliance during execution

#### 4.3 Evidence Pipeline

**Extend existing**: Evidence collection system

- Configure evidence artifacts per protocol
- Setup retrospective data collection
- Enable quality gate validation

### Phase 5: Execution Interface

Create simple execution model:

```bash
# Step 1: User provides brief
cp docs/my-project-brief.md PROJECT-BRIEF.md

# Step 2: Generate workflow
cursor apply .cursor/commands/orchestrate-workflow.md

# Step 3: AI outputs generated commands
[ORCHESTRATOR] Analysis complete. Generated 6 protocols:
- 00-analyze-brief.md ✓
- 01-bootstrap-context.md ✓
- 02-create-requirements.md ✓
- 03-generate-implementation.md ✓
- 04-validate-quality.md ✓
- 05-retrospective.md ✓

# Step 4: User executes sequentially
cursor apply .cursor/commands/00-analyze-brief.md
# ... complete task, then next
cursor apply .cursor/commands/01-bootstrap-context.md
# ... and so on
```

## Decision Framework Examples

### Example 1: Simple Landing Page

**Brief**: "Create a marketing landing page with contact form"

**Analysis**:

- Type: web-app (frontend-only)
- Complexity: simple
- Lifecycle: MVP

**Generated Protocols**:

1. `00-analyze-brief.md` (validate requirements)
2. `01-design-ui-components.md` (custom: focus on UI/UX)
3. `02-implement-frontend.md` (custom: no backend needed)
4. `03-validate-accessibility.md` (mandatory for public web)
5. `04-deployment-guide.md` (static hosting)

**Skipped**:

- Bootstrap (no codebase analysis needed)
- Backend protocols
- Complex architecture design
- Pre-production security (simple use case)

### Example 2: SaaS Billing System

**Brief**: "Multi-tenant SaaS with Stripe integration, user roles, audit logs"

**Analysis**:

- Type: web-app (fullstack)
- Complexity: complex
- Lifecycle: production-grade

**Generated Protocols**:

1. `00-client-discovery.md` (detailed requirements)
2. `01-bootstrap-architecture.md` (analyze existing patterns)
3. `02-security-design.md` (custom: focus on multi-tenancy, PCI compliance)
4. `03-database-schema.md` (custom: complex data model)
5. `04-api-contracts.md` (custom: OpenAPI spec generation)
6. `05-implementation-tasks.md` (standard task generation)
7. `06-security-validation.md` (mandatory for payment systems)
8. `07-integration-testing.md` (E2E critical flows)
9. `08-deployment-checklist.md` (production readiness)
10. `09-monitoring-setup.md` (observability for SaaS)
11. `10-retrospective.md` (learnings capture)

**Custom Protocols Created**:

- Security design (tailored to multi-tenancy)
- Database schema (complex relationships)
- Integration testing (Stripe webhook handling)

### Example 3: Data Analytics Dashboard

**Brief**: "BI dashboard for real estate loan portfolio analysis"

**Analysis**:

- Type: data-bi
- Complexity: moderate
- Lifecycle: MVP

**Generated Protocols**:

1. `00-data-discovery.md` (custom: analyze Excel sources)
2. `01-data-quality-assessment.md` (custom: validate data integrity)
3. `02-dashboard-design.md` (custom: KPI selection, mock-ups)
4. `03-etl-pipeline.md` (custom: data extraction and transformation)
5. `04-visualization-implementation.md` (Tableau-specific)
6. `05-user-acceptance-testing.md` (validate with stakeholders)
7. `06-retrospective.md` (capture data quality learnings)

**Domain-Specific Customizations**:

- Data quality assessment (not in standard protocols)
- ETL pipeline design (data-specific)
- Visualization-first approach (vs code-first)

## Quality Gates & Validation

Each generated protocol will include:

1. **Entry Criteria**: What must be true to start this protocol
2. **Exit Criteria**: What must be true to proceed to next
3. **Automation Hooks**: Scripts to run for validation
4. **Evidence Artifacts**: What to capture for retrospective
5. **Rule References**: Which rules apply to this protocol

## Benefits of This Approach

### For Users:

- ✅ No guesswork - AI tells you exactly which protocols to run
- ✅ Logical flow - dependencies automatically resolved
- ✅ Time-efficient - skip unnecessary protocols
- ✅ Context-aware - protocols adapted to project needs

### For AI:

- ✅ Clear instructions - each command is self-contained
- ✅ Proper sequencing - no attempts to test before building
- ✅ Rule alignment - knows which rules to apply when
- ✅ Evidence-based - automation hooks provide objective feedback

### For Template Maintenance:

- ✅ Single source of truth - protocols remain unchanged
- ✅ Composable - mix and match as needed
- ✅ Extensible - easy to add new protocols
- ✅ Traceable - decisions documented in orchestrator logs

---

## Complete User Playbook

### Prerequisites Checklist

👤 **USER-MANUAL** - Setup Steps:
- [ ] Clone ai-driven-template repository
- [ ] Install Cursor IDE
- [ ] Configure Python environment (Python 3.9+)
- [ ] Initialize Git repository
- [ ] Create PROJECT-BRIEF.md with project description

✅ **AI-DRIVEN** - Automatic Validation:
- Scripts verify Python version
- Scripts check Git configuration
- Scripts validate PROJECT-BRIEF.md format

### Phase 1: Protocol Orchestration

🔄 **HYBRID** - Generate Protocol Sequence:

1. 👤 **USER**: Run command: `cursor apply .cursor/commands/protocol-orchestrator.md`

2. ✅ **AI**: Analyzes PROJECT-BRIEF.md
3. ✅ **AI**: Classifies project (type, stack, complexity, lifecycle)
4. ✅ **AI**: Selects appropriate protocols using decision matrix
5. ✅ **AI**: Resolves dependencies and sequences protocols
6. ✅ **AI**: Generates numbered command files in `.cursor/commands/`
7. 🔄 **AI**: Presents generated sequence for approval
8. 👤 **USER**: Reviews protocol list, approves or requests changes

**Expected AI Output:**
```
[ORCHESTRATION COMPLETE] Generated 8 protocols for your web-app project:
- 00-analyze-brief.md ✅ (validate requirements)
- 01-bootstrap-context.md ✅ (analyze codebase)
- 02-create-prd.md ✅ (detailed requirements)
- 03-generate-tasks.md ✅ (implementation plan)
- 04-process-tasks.md ✅ (execute development)
- 05-quality-audit.md ✅ (run tests and validation)
- 06-deployment.md ✅ (automated deployment setup)
- 07-retrospective.md ✅ (capture learnings)

SKIPPED: 7-monitoring (MVP, not needed), 8-ci-cd (simple project), 9-docs (self-explanatory), 10-testing (covered in quality audit)

👤 USER ACTION REQUIRED: Type "approve" to proceed or "modify" to adjust
```

### Phase 2: Execute Generated Protocols

For EACH generated protocol (00-, 01-, 02-, etc.):

🔄 **HYBRID** - Protocol Execution Loop:

1. 👤 **USER**: Load protocol: `cursor apply .cursor/commands/XX-protocol-name.md`

2. ✅ **AI**: Reads protocol instructions
3. ✅ **AI**: Loads relevant rules (context discovery)
4. ✅ **AI**: Executes protocol steps automatically
5. ✅ **AI**: Runs validation scripts (e.g., `scripts/validate_brief.py`)
6. ✅ **AI**: Collects evidence artifacts

7. ⚠️ **CONDITIONAL** - Manual Steps (if required by protocol):
   - 👤 **USER**: Stakeholder approval (for PRD sign-off)
   - 👤 **USER**: External service configuration (API keys, credentials)
   - 👤 **USER**: Production deployment approval
   - 👤 **USER**: Code review and PR merge

8. 🔄 **AI**: Reports completion status
9. 👤 **USER**: Verifies output, marks protocol complete
10. 👤 **USER**: Proceeds to next protocol

### Phase 3: Quality Gates & Validation

✅ **AI-DRIVEN** - Automated Validation:
- Run test suites: `python scripts/run_quality_audit.py`
- Check code coverage: `python scripts/aggregate_coverage.py`
- Security scanning: GitHub Actions workflows
- Linting and formatting: Automated in CI/CD

👤 **USER-MANUAL** - Required Approvals:
- Review quality audit report
- Approve deployment to production
- Confirm acceptance criteria met
- Sign off on protocol completion

⚠️ **CONDITIONAL** - Manual Intervention:
- If tests fail: User decides to fix or defer
- If coverage low: User decides acceptable threshold
- If security issues: User prioritizes and assigns fixes

### Reference: When User Manual Steps Are Required

#### Always Manual:
- 👤 Creating initial PROJECT-BRIEF.md
- 👤 Stakeholder communication and approvals
- 👤 Production deployment approval
- 👤 Configuring external services (API keys, credentials)
- 👤 Code review and PR merges (if team-based)
- 👤 Emergency hotfixes and rollbacks

#### Usually AI-Driven:
- ✅ Code generation and implementation
- ✅ Test writing and execution
- ✅ Documentation generation
- ✅ Dependency management
- ✅ Linting and formatting
- ✅ Evidence collection

#### Hybrid (AI proposes, User approves):
- 🔄 Architecture decisions
- 🔄 Protocol sequence selection
- 🔄 PRD content and requirements
- 🔄 Task breakdown and priorities
- 🔄 Quality gate thresholds
- 🔄 Deployment strategies

### Troubleshooting Guide

#### Common Issues and Solutions:

**Issue**: Orchestration fails to generate protocols
- **Cause**: PROJECT-BRIEF.md missing or invalid format
- **Solution**: 👤 User creates/validates PROJECT-BRIEF.md, then retry

**Issue**: Protocol execution fails with script errors
- **Cause**: Missing Python dependencies or incorrect environment
- **Solution**: 👤 User runs `pip install -r requirements.txt`, then retry

**Issue**: Quality audit fails with test errors
- **Cause**: Code implementation issues or missing test setup
- **Solution**: ⚠️ User reviews test output, decides to fix code or adjust test expectations

**Issue**: Deployment fails with environment errors
- **Cause**: Missing environment variables or incorrect configuration
- **Solution**: 👤 User configures deployment environment, then retry

---

## Protocol Acceptance Criteria Matrix

### Standard Protocol 0: Client Discovery

**When to Use:**
✅ Starting new project without existing brief
✅ Converting job post to structured requirements
✅ Need stakeholder alignment on scope

**When to Skip:**
❌ PROJECT-BRIEF.md already exists and validated

**Entry Criteria:**
- [ ] Job post or project idea documented
- [ ] Stakeholder contact information available
- [ ] Initial requirements communicated

**Exit Criteria:**
- [ ] PROJECT-BRIEF.md created and validated
- [ ] Key requirements documented
- [ ] Constraints and exclusions identified
- [ ] Stakeholder approval obtained

**Automation:**
✅ **AI-DRIVEN:**
- Brief structure generation
- Requirements extraction
- Validation script: `python scripts/validate_brief.py PROJECT-BRIEF.md`

👤 **USER-MANUAL:**
- Stakeholder interviews
- Requirement clarifications
- Final approval and sign-off

**Evidence Artifacts:**
- PROJECT-BRIEF.md
- acceptance-criteria.md
- stakeholder-approvals.md (if applicable)

**Common Failure Modes:**
- ❌ Incomplete requirements → Solution: AI prompts for missing sections
- ❌ Ambiguous constraints → Solution: AI flags unclear statements
- ❌ Scope creep detected → Solution: AI compares to original brief

---

### Standard Protocol 1: Bootstrap Context

**When to Use:**
✅ New projects requiring codebase analysis
✅ Existing projects needing context refresh
✅ Team onboarding to existing codebase

**When to Skip:**
❌ Simple static sites with no codebase
❌ Data analytics projects (no code to analyze)
❌ Context already exists and validated

**Entry Criteria:**
- [ ] Project structure exists
- [ ] Code files present (if applicable)
- [ ] Git repository initialized

**Exit Criteria:**
- [ ] Context kit generated
- [ ] Project rules created
- [ ] README.md files updated
- [ ] Architecture decisions documented

**Automation:**
✅ **AI-DRIVEN:**
- Codebase analysis: `python scripts/analyze_codebase.py`
- Rule generation and normalization
- README.md generation
- Context kit creation

👤 **USER-MANUAL:**
- Architecture decision approvals
- Rule customization requests
- Context validation

**Evidence Artifacts:**
- context-kit/README.md
- .cursor/rules/project-rules/
- Architecture decision records

**Common Failure Modes:**
- ❌ Missing dependencies → Solution: AI prompts for installation
- ❌ Unreadable code → Solution: AI flags problematic files
- ❌ No clear architecture → Solution: AI requests clarification

---

### Standard Protocol 2: Create PRD

**When to Use:**
✅ Complex projects requiring detailed requirements
✅ Multi-stakeholder projects
✅ Projects with unclear initial requirements

**When to Skip:**
❌ Simple MVPs with clear requirements
❌ Data analytics projects (requirements are data-driven)
❌ Prototypes with minimal scope

**Entry Criteria:**
- [ ] PROJECT-BRIEF.md validated
- [ ] Stakeholder contact information available
- [ ] Initial requirements documented

**Exit Criteria:**
- [ ] PRD document created and approved
- [ ] Functional requirements detailed
- [ ] Non-functional requirements specified
- [ ] Stakeholder sign-off obtained

**Automation:**
✅ **AI-DRIVEN:**
- PRD structure generation
- Requirements extraction from brief
- Validation script: `python scripts/validate_prd.py`

👤 **USER-MANUAL:**
- Stakeholder interviews
- Requirement clarifications
- PRD review and approval

**Evidence Artifacts:**
- prd-{feature-name}.md
- stakeholder-approvals.md
- Requirements traceability matrix

**Common Failure Modes:**
- ❌ Unclear requirements → Solution: AI prompts for clarification
- ❌ Missing stakeholders → Solution: AI flags missing approvals
- ❌ Scope creep → Solution: AI compares to original brief

---

### Standard Protocol 3: Generate Tasks

**When to Use:**
✅ All projects requiring implementation planning
✅ After PRD approval (if PRD was created)
✅ Before code implementation begins

**When to Skip:**
❌ Never (this is mandatory for all implementations)

**Entry Criteria:**
- [ ] Requirements documented (PRD or brief)
- [ ] Architecture decisions made
- [ ] Implementation scope defined

**Exit Criteria:**
- [ ] Task plan created with dependencies
- [ ] Sub-tasks broken down appropriately
- [ ] Automation hooks configured
- [ ] User approval obtained

**Automation:**
✅ **AI-DRIVEN:**
- Task breakdown from requirements
- Dependency analysis
- Automation hook binding
- Validation script: `python scripts/validate_tasks.py`

👤 **USER-MANUAL:**
- Task plan review
- Priority adjustments
- Final approval to proceed

**Evidence Artifacts:**
- tasks-{feature-name}.md
- Automation hook references
- Dependency graph

**Common Failure Modes:**
- ❌ Tasks too granular → Solution: AI groups related tasks
- ❌ Missing dependencies → Solution: AI analyzes task relationships
- ❌ No automation hooks → Solution: AI suggests appropriate scripts

---

### Standard Protocol 4: Process Tasks

**When to Use:**
✅ After task generation approval
✅ During implementation phase
✅ For each parent task in the plan

**When to Skip:**
❌ Never (this is the core implementation protocol)

**Entry Criteria:**
- [ ] Task plan approved
- [ ] Development environment ready
- [ ] Required tools and dependencies installed

**Exit Criteria:**
- [ ] All sub-tasks completed
- [ ] Code implemented and tested
- [ ] Evidence artifacts collected
- [ ] Quality gates passed

**Automation:**
✅ **AI-DRIVEN:**
- Code generation and implementation
- Test writing and execution
- Evidence collection
- Validation script: `python scripts/execute_task.py`

👤 **USER-MANUAL:**
- Code review and approval
- External service configuration
- Manual testing validation

**Evidence Artifacts:**
- Code commits with semantic messages
- Test results and coverage
- Implementation documentation

**Common Failure Modes:**
- ❌ Implementation incomplete → Solution: AI flags missing sub-tasks
- ❌ Tests failing → Solution: AI suggests fixes or user adjusts expectations
- ❌ External dependencies → Solution: AI prompts for manual configuration

---

### Standard Protocol 5: Quality Audit

**When to Use:**
✅ After task implementation completion
✅ Before deployment
✅ Mandatory for all projects

**When to Skip:**
❌ Never (this is mandatory for quality assurance)

**Entry Criteria:**
- [ ] Implementation tasks completed
- [ ] Code committed to repository
- [ ] Basic tests passing

**Exit Criteria:**
- [ ] Quality audit report generated
- [ ] Test coverage meets threshold
- [ ] Security scan completed
- [ ] Critical issues addressed

**Automation:**
✅ **AI-DRIVEN:**
- Test suite execution
- Code coverage analysis
- Security scanning
- Validation script: `python scripts/run_quality_audit.py`

👤 **USER-MANUAL:**
- Quality report review
- Issue prioritization
- Deployment approval

**Evidence Artifacts:**
- Quality audit report
- Test coverage reports
- Security scan results

**Common Failure Modes:**
- ❌ Low test coverage → Solution: User decides acceptable threshold
- ❌ Security vulnerabilities → Solution: User prioritizes fixes
- ❌ Performance issues → Solution: User decides optimization needs

---

### Standard Protocol 6: Deployment & Release Management

**When to Use:**
✅ Production or enterprise projects
✅ Web or mobile applications
✅ Automated deployment required

**When to Skip:**
❌ Simple MVPs with manual deployment
❌ Data analytics projects (manual Tableau/PowerBI publish)
❌ Prototypes without deployment needs

**Entry Criteria:**
- [ ] Quality audit passed
- [ ] All tests passing in CI/CD
- [ ] Deployment target configured
- [ ] Environment variables configured

**Exit Criteria:**
- [ ] Deployment automation configured
- [ ] Rollback procedures documented
- [ ] Release notes generated
- [ ] Post-deployment health checks passing

**Automation:**
✅ **AI-DRIVEN:**
- Deployment script generation
- CI/CD workflow configuration
- Release notes generation
- Health check endpoint creation

👤 **USER-MANUAL:**
- Production deployment approval
- DNS configuration
- SSL certificate setup
- Monitoring alert acknowledgment

**Evidence Artifacts:**
- deployment-config.yml
- rollback-procedure.md
- release-notes-v{version}.md
- deployment-verification.log

**Common Failure Modes:**
- ❌ Environment variable mismatch → Solution: AI validates against .env.example
- ❌ Deployment fails health check → Solution: AI triggers rollback
- ❌ Database migration fails → Solution: AI prompts for manual intervention

---

### Standard Protocol 7: Monitoring & Observability Setup

**When to Use:**
✅ Production or enterprise projects
✅ SaaS applications requiring uptime monitoring
✅ Applications with performance requirements

**When to Skip:**
❌ Simple MVPs (basic analytics sufficient)
❌ Prototypes without monitoring needs
❌ Static sites with minimal requirements

**Entry Criteria:**
- [ ] Application deployed
- [ ] Monitoring requirements defined
- [ ] Alert thresholds specified

**Exit Criteria:**
- [ ] Monitoring dashboards configured
- [ ] Alert rules set up
- [ ] Log aggregation working
- [ ] Performance metrics collected

**Automation:**
✅ **AI-DRIVEN:**
- Monitoring configuration
- Dashboard creation
- Alert rule setup
- Log aggregation setup

👤 **USER-MANUAL:**
- Monitoring service configuration
- Alert acknowledgment setup
- Dashboard customization

**Evidence Artifacts:**
- monitoring-config.yml
- dashboard-config.json
- alert-rules.yml
- monitoring-verification.log

**Common Failure Modes:**
- ❌ Too many alerts → Solution: AI suggests alert consolidation
- ❌ Missing critical metrics → Solution: AI identifies gaps
- ❌ Performance impact → Solution: User adjusts monitoring frequency

---

### Standard Protocol 8: CI/CD Pipeline Configuration

**When to Use:**
✅ All code-based projects
✅ Projects requiring automated testing
✅ Team-based development

**When to Skip:**
❌ Data analytics projects (not applicable)
❌ Solo projects with manual processes
❌ Prototypes without CI needs

**Entry Criteria:**
- [ ] Code repository established
- [ ] Test suite available
- [ ] Deployment target configured

**Exit Criteria:**
- [ ] CI/CD pipeline configured
- [ ] Automated testing working
- [ ] Deployment automation ready
- [ ] Quality gates enforced

**Automation:**
✅ **AI-DRIVEN:**
- Pipeline configuration
- Workflow generation
- Quality gate setup
- Integration testing

👤 **USER-MANUAL:**
- Repository secrets configuration
- Deployment environment setup
- Pipeline approval

**Evidence Artifacts:**
- .github/workflows/ci.yml
- pipeline-config.yml
- ci-test-results.log

**Common Failure Modes:**
- ❌ Pipeline fails → Solution: AI suggests fixes
- ❌ Slow builds → Solution: AI optimizes pipeline
- ❌ Missing secrets → Solution: AI prompts for configuration

---

### Standard Protocol 9: Documentation Generation

**When to Use:**
✅ Production or enterprise projects
✅ Open-source projects
✅ Projects requiring user documentation

**When to Skip:**
❌ Internal MVPs with self-explanatory code
❌ Prototypes without documentation needs
❌ Simple projects with minimal scope

**Entry Criteria:**
- [ ] Implementation completed
- [ ] API endpoints defined (if applicable)
- [ ] User workflows identified

**Exit Criteria:**
- [ ] API documentation generated
- [ ] User guides created
- [ ] Operator runbooks written
- [ ] Documentation published

**Automation:**
✅ **AI-DRIVEN:**
- API documentation generation
- Code documentation extraction
- User guide creation
- Documentation site generation

👤 **USER-MANUAL:**
- Documentation review
- User workflow validation
- Publication approval

**Evidence Artifacts:**
- api-docs/
- user-guides/
- operator-runbooks/
- documentation-site/

**Common Failure Modes:**
- ❌ Outdated documentation → Solution: AI suggests update triggers
- ❌ Missing user workflows → Solution: AI prompts for clarification
- ❌ Poor documentation quality → Solution: AI suggests improvements

---

### Standard Protocol 10: Testing Strategy & Implementation

**When to Use:**
✅ Moderate or complex projects
✅ Production or enterprise projects
✅ Projects requiring comprehensive testing

**When to Skip:**
❌ Simple MVPs (unit tests from quality audit sufficient)
❌ Prototypes with minimal testing needs
❌ Projects with existing comprehensive test coverage

**Entry Criteria:**
- [ ] Implementation completed
- [ ] Unit tests passing
- [ ] Testing requirements defined

**Exit Criteria:**
- [ ] Integration tests implemented
- [ ] E2E tests configured
- [ ] Performance tests created
- [ ] Test automation working

**Automation:**
✅ **AI-DRIVEN:**
- Test case generation
- Integration test implementation
- E2E test configuration
- Performance test setup

👤 **USER-MANUAL:**
- Test scenario validation
- Performance threshold setting
- Test data preparation

**Evidence Artifacts:**
- integration-tests/
- e2e-tests/
- performance-tests/
- test-results/

**Common Failure Modes:**
- ❌ Flaky tests → Solution: AI suggests test stabilization
- ❌ Slow test execution → Solution: AI optimizes test suite
- ❌ Missing test coverage → Solution: AI identifies gaps

---

### Standard Protocol 11: Retrospective

**When to Use:**
✅ After project completion
✅ After major milestones
✅ For continuous improvement

**When to Skip:**
❌ Never (this is mandatory for learning)

**Entry Criteria:**
- [ ] Project or milestone completed
- [ ] Evidence artifacts collected
- [ ] Quality gates passed

**Exit Criteria:**
- [ ] Retrospective report generated
- [ ] Learnings documented
- [ ] Improvement actions identified
- [ ] Knowledge captured

**Automation:**
✅ **AI-DRIVEN:**
- Evidence analysis
- Learning extraction
- Report generation
- Validation script: `python scripts/generate_retrospective.py`

👤 **USER-MANUAL:**
- Learning validation
- Improvement action approval
- Knowledge sharing

**Evidence Artifacts:**
- retrospective-report.md
- learnings-log.md
- improvement-actions.md

**Common Failure Modes:**
- ❌ Missing evidence → Solution: AI prompts for additional data
- ❌ Superficial analysis → Solution: AI suggests deeper investigation
- ❌ No actionable insights → Solution: AI suggests specific improvements

---

## Files to Create/Extend

### 🆕 Truly New Files
1. `.cursor/commands/orchestrate-workflow.md` - Main orchestrator command
2. `.cursor/ai-driven-workflow/decision-rules.md` - Decision framework documentation
3. `docs/ORCHESTRATOR-GUIDE.md` - User guide for workflow orchestration

### ✅ Already Exists (Extend)
4. `scripts/generate_from_brief.py` - Add orchestration logic
5. `scripts/classify_domain.py` - Add protocol mapping
6. `scripts/validate_protocol_steps.py` - Add customization capabilities
7. `scripts/lifecycle_tasks.py` - Add sequencing logic

### 🔧 Needs Enhancement
8. `.cursor/ai-driven-workflow/protocol-metadata.json` - Add to existing structure
9. `.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md` - Update with orchestrator info

### 📁 Integration Points
- `template-packs/` - Reference existing templates
- `project_generator/` - Use existing scaffolding
- `scripts/` - Leverage all 60+ existing automation scripts

## Next Steps

After plan approval, I will:

1. Create the orchestrator command with full AI instructions
2. **Extend existing Python scripts** with orchestration logic
3. **Add metadata to existing protocol structure**
4. Create decision framework documentation
5. Add example project brief → protocol mappings
6. Test with sample briefs (simple, moderate, complex)
7. Document the complete workflow in user guide

### Integration Strategy
- **Leverage existing**: 60+ automation scripts, template-packs, project_generator
- **Extend rather than duplicate**: Build on proven foundation
- **Maintain compatibility**: Work with existing 3-tier rule system
- **Preserve workflows**: Keep existing protocol files unchanged