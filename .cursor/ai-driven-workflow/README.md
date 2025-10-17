# The Governor Workflow: From Idea to Production

## 1. Why: A Structured Workflow for Predictable Results

Working with AI can sometimes feel unpredictable. The AI Governor Framework provides a development workflow designed to fix that, for both new and existing projects.

It provides a structured, sequential process that transforms your AI from a simple code generator into a reliable engineering partner. By following these protocols, you ensure that both you and the AI are always aligned, moving from a high-level idea to a well-implemented feature with clarity, control, and consistency.

The goal is to make AI-powered development:
-   **Predictable:** Each step has a clear purpose and output.
-   **Controllable:** You are always in the loop for key decisions.
-   **Efficient:** The AI does the heavy lifting, you provide the strategic direction.

## 2. Protocol Architecture Map

The workflow consists of **34 protocols** organized in **5 phases** with **dependency-based flow**:

```
Phase 0: Foundation (Bootstrap & Discovery)
├── 0-bootstrap-your-project.md (Project Analyst)
├── 00-client-discovery.md (Client Discovery Specialist)  
└── 00-generate-rules.md (Rule Generation Command)

Phase 1-2: Planning (PRD, Architecture & Tasks)
├── 1-create-prd.md (Product Manager)
├── 6-technical-design-architecture.md (Solutions Architect)
└── 2-generate-tasks.md (Tech Lead)

Phase 2.5: Environment Readiness
└── 7-environment-setup-validation.md (DevOps Environment Engineer)

Phase 3: Execution
└── 3-process-tasks.md (Paired Developer)

Phase 4: Quality Assurance
├── 4-quality-audit.md (Quality Orchestrator)
├── review-protocols/
│   ├── architecture-review.md
│   ├── code-review.md
│   ├── design-system.md
│   ├── pre-production.md
│   ├── security-check.md
│   ├── ui-accessibility.md
│   └── utils/
│       ├── _review-router.md
│       ├── context-analyzer.md
│       ├── enhanced-static-template.md
│       ├── enhanced-static-validation.md
│       └── rule-injection-system.md

Phase 4.5: Deployment & Operations
├── 11-production-deployment.md (Release Manager)
├── 12-monitoring-observability.md (Site Reliability Engineer)
└── 13-incident-response-rollback.md (Incident Commander)

Phase 5: Continuous Improvement
├── 5-implementation-retrospective.md (Process Improvement Lead)
└── 8-script-governance-protocol.md (Automation Compliance Auditor)
```

## 3. Phase 0: Foundation Protocols (Bootstrap & Discovery)

### Protocol 0: Project Bootstrap & Context Engineering
**Role:** AI Codebase Analyst & Context Architect  
**File:** `0-bootstrap-your-project.md`

#### Purpose
Perform initial analysis of project, configure AI Governor Framework, and propose foundational "Context Kit" to dramatically improve all future AI collaboration.

#### Prerequisites
- Project repository with basic structure
- Cursor editor (for optimal rule activation)
- Access to master-rules and common-rules directories

#### Execution Algorithm (7-Step Process)
1. **Tooling Configuration & Rule Activation**
   - Detect tooling and configure rules
   - Create `.cursor/rules/` structure
   - Rename rule files to `.mdc` format
   - Add metadata with `alwaysApply` properties

2. **Initial Codebase Mapping**
   - Perform recursive file listing
   - Propose analysis plan for key files
   - Validate plan with user
   - Analyze key files and confirm stack

3. **Thematic Investigation Plan**
   - Generate architectural questions by theme
   - Announce investigation plan to user
   - Focus on security, data flow, conventions

4. **Autonomous Deep Dive & Synthesis**
   - Perform deep semantic analysis
   - Synthesize findings into principles
   - Avoid over-engineering, favor pragmatic solutions

5. **Collaborative Validation (Checkpoint)**
   - Present consolidated report
   - Await user validation and corrections
   - Document validated principles

6. **Iterative Generation Phase 1: Documentation**
   - Generate/update README.md files
   - Create human-readable source of truth
   - Iterate with user approval

7. **Iterative Generation Phase 2: Project Rules**
   - Generate project-rules from READMEs
   - Follow rule creation guidelines
   - Validate with automation scripts

#### Quality Gates
- **Step 1:** All rules normalized and metadata validated
- **Step 2:** Stack detection complete and confirmed
- **Step 4:** All thematic questions answered with source quotes
- **Step 5:** User validates understanding
- **Step 6:** All READMEs generated and approved
- **Step 7:** All rules generated and validated

#### Automation Hooks
- `normalize_project_rules.py` - Rule metadata normalization
- `rules_audit_quick.py` - Rule compliance validation
- Template discovery and inventory generation

#### Outputs
- `.cursor/context-kit/` directory with project knowledge base
- Normalized rule files with proper metadata
- Project scaffolding (optional via Project Generator)
- Context Kit README with governance status

---

### Protocol 00: Client Discovery & Project Briefing
**Role:** Client Discovery Specialist  
**File:** `00-client-discovery.md`

#### Purpose
Transform any inbound job post, RFP, email, or partial brief into a structured, validated project brief with clear scope, constraints, risks, and acceptance criteria.

#### Prerequisites
- Raw job post or project requirements
- Access to project's architectural source of truth (README.md)

#### Execution Algorithm (6-Phase Process)
1. **Intake & Normalization**
   - Collect raw input between markers
   - Detect domain hints (#domain, #deadline, #budget, #must)
   - Normalize to raw-intake.md
   - Gate: Intake completeness validation

2. **Signal Extraction**
   - Extract core signals (objectives, users, deliverables, constraints, success metrics)
   - Classify domain (Web/Mobile, Data/BI, ML/AI, Infrastructure, Other)
   - Create evidence map with source quotes
   - Gate: Evidence map complete

3. **Clarification & Assumptions**
   - Generate ≤10 targeted questions
   - Propose assumptions v1 for gaps
   - Present Q&A package to user
   - Gate: Client Q&A ready

4. **Risks & Dependencies**
   - Identify risks (scope creep, data quality, compliance, technical, resource)
   - Map dependencies (access, data, integration, approval)
   - Create risk register with mitigations
   - Gate: Risk register complete

5. **Draft Brief Assembly**
   - Assemble project brief with all sections
   - Generate acceptance criteria (SMART)
   - Create supporting artifacts
   - Gate: Self-check complete

6. **Review Package**
   - Bundle all artifacts
   - Generate executive summary
   - Internal quality validation
   - Gate: Quality checks passed

#### Quality Gates
- **Phase 1:** All text captured, no truncation, hints extracted
- **Phase 2:** All signals extracted with source quotes
- **Phase 3:** ≤10 questions, clear assumptions documented
- **Phase 4:** All risks identified with mitigations and owners
- **Phase 5:** Brief complete, criteria measurable
- **Phase 6:** All quality gates satisfied

#### Automation Hooks
- `validate_brief.py` - Brief validation and quality scoring
- `score_risks.py` - Risk scoring by impact/likelihood
- `classify_domain.py` - Domain classification with ML

#### Outputs
- `brief.md` - Complete project brief
- `acceptance-criteria.md` - Measurable success criteria
- `open-questions.md` - ≤10 prioritized questions
- `stakeholders.md` - Roles and decision rights
- `constraints.md` - Detailed constraint analysis
- `risk-register.md` - Risks and mitigations
- `one-pager.md` - Executive summary

---

### Protocol 00: Generate Cursor Rules Command
**Role:** Rule Generation System  
**File:** `00-generate-rules.md`

#### Purpose
Generate comprehensive, project-scoped Cursor rules based on actual repository context with stack-specific templates and metadata normalization.

#### Prerequisites
- Project with `.cursor/rules/` directory structure
- Project documentation (README.md, package.json, etc.)
- Optional: PROJECT-BRIEF.md for enhanced context

#### Execution Algorithm (3-Phase Process)
1. **Discovery Phase**
   - Scan `.cursor/rules/` directory (master-rules, common-rules, project-rules)
   - Detect legacy `.cursorrules` and parse for guidance
   - Detect `AGENTS.md` and ingest agent instructions
   - Read project docs (README.md, package.json, requirements.txt, etc.)
   - Read `PROJECT-BRIEF.md` if present
   - Scan nested rule roots for monorepos

2. **Analysis Phase**
   - Determine project type (frontend, backend, fullstack, monorepo)
   - Identify primary frameworks/languages
   - Map gaps: missing project-specific rules
   - Plan rule set(s) to generate per detected stack

3. **Generation Phase**
   - Output to `.cursor/rules/project-rules/`
   - Create framework-specific rules (React, FastAPI, etc.)
   - Include YAML frontmatter with TAGS, TRIGGERS, SCOPE
   - Add practical code examples and conventions
   - Validate rule metadata and placement

#### Quality Gates
- Proper YAML frontmatter with required fields
- Practical code examples included
- Covers common development scenarios
- Files placed under `.cursor/rules/project-rules/`
- Rule length reasonable (<500 lines)
- References use `[filename.ext](mdc:filename.ext)` format

#### Automation Hooks
- Rule metadata validation
- CI job for rule file validation
- Link checking for `mdc:` references

#### Outputs
- Framework-specific rule files (e.g., `react-app-structure.mdc`)
- Backend architecture rules (e.g., `fastapi-backend-architecture.mdc`)
- Fullstack integration conventions
- Rule audit and validation reports

## 4. Phase 1-2: Planning Protocols (PRD & Tasks)

### Protocol 1: Implementation-Ready PRD Creation
**Role:** Product Manager  
**File:** `1-create-prd.md`

#### Purpose
Conduct focused interview to create implementation-ready PRD with complete technical specifications including data schemas, API contracts, UI workflows, and business logic.

#### Prerequisites
- Project's overall architecture understood (README.md or architecture guide)
- Clear feature requirements or modification request
- Access to Architectural Decision Matrix

#### Execution Algorithm (4-Phase Process)
1. **Analysis and Scoping**
   - Initial qualification: Creating new vs modifying existing feature
   - Path A (New): Core business need, feature type classification
   - Path B (Modify): Current behavior, desired behavior, involved files, regression risks
   - Announce detected implementation layer
   - Validate placement with user

2. **Specifications by Layer**
   - Frontend Application: User stories, wireframes, responsiveness, API integration
   - Backend Service: API routes, HTTP methods, request/response schemas, business logic
   - Central API: CRUD operations, database access patterns
   - Object Storage: File structure, caching strategy, versioning

3. **Architectural Constraints**
   - Verify proposed interactions respect communication rules
   - Validate allowed flows (UI → Central API: GET only, etc.)
   - Check prohibited flows (UI → Database: Direct access forbidden)

4. **Synthesis and Generation**
   - Summarize architecture with detected layer and communications
   - Final validation with user
   - Generate complete PRD with all sections

#### Quality Gates
- **Phase 1:** Implementation layer correctly identified and validated
- **Phase 2:** All layer-specific requirements captured
- **Phase 3:** Architectural constraints respected
- **Phase 4:** PRD complete and user-approved

#### Automation Hooks
- `generate_prd_assets.py` - Generate user stories, data schemas, API contracts
- `validate_prd_gate.py` - PRD completeness validation (score ≥ 85)

#### Outputs
- `prd-{feature-name}.md` - Complete PRD with technical specifications
- API contracts and data schemas
- Architecture diagrams and communication flows
- Implementation-ready artifacts for Protocol 2

---

### Protocol 2: Technical Task Generation
**Role:** Tech Lead  
**File:** `2-generate-tasks.md`

#### Purpose
Transform PRD into simple, actionable plan with minimum viable steps, guiding implementation with structured action list.

#### Prerequisites
- PRD file (e.g., `prd-my-cool-feature.md`)
- Information about primary implementation layer
- Access to project rules and context

#### Execution Algorithm (4-Phase Process)
1. **Rule Indexing and Context Preparation**
   - Build rule index: find all rule directories
   - Parse rule metadata from all files
   - Create in-memory index for compliance
   - Identify top LLM models & personas via web search
   - Identify implementation layers (primary + secondary)
   - Duplicate prevention for UI components
   - Git branch proposal (optional)

2. **High-Level Task Generation and Validation**
   - Create task file in `/tasks` or `/docs` directory
   - Generate high-level tasks (UI Component, Backend Route, Integration Testing, Documentation)
   - Add WHY context for each high-level task
   - Identify task dependencies with `[DEPENDS ON: ...]` format
   - Task complexity assessment (Simple/Complex)
   - High-level validation with user confirmation

3. **Detailed Breakdown by Layer**
   - Decomposition using templates (Frontend, Backend, Global State)
   - Apply rules to every sub-task with `[APPLIES RULES: ...]`
   - Assign model personas to high-level tasks
   - Populate placeholders with specific names from PRD
   - Finalize and save complete Markdown document

4. **Automation Hook Annotation**
   - Identify automation opportunities (testing, linting, deployment, reporting)
   - Add `Automation:` metadata to high-level tasks
   - Parameterize automation with placeholders
   - Validate automation references exist and are executable

#### Quality Gates
- **Phase 1:** Rule index complete, LLM models identified, layers mapped
- **Phase 2:** High-level tasks generated with WHY statements and dependencies
- **Phase 3:** All sub-tasks decomposed with rule applications
- **Phase 4:** Automation hooks validated and executable

#### Automation Hooks
- `validate_tasks.py` - Task file completeness and quality validation
- `enrich_tasks.py` - Add estimated effort, risk flags, automation coverage
- `validate_automation_hooks.py` - Verify automation references exist

#### Outputs
- `tasks-{prd-name}.md` - Complete technical execution plan
- High-level tasks with WHY statements and complexity assessments
- Detailed sub-tasks with rule applications and dependencies
- Automation hooks for CI/CD integration
- Model persona recommendations for execution

### Protocol 6: Technical Design & Architecture Specification
**Role:** Solutions Architect
**File:** `6-technical-design-architecture.md`

#### Purpose
Translate the approved Project Brief and discovery evidence into an implementation-ready technical architecture package with validated decisions, diagrams, and downstream-ready task inputs.

#### Prerequisites
- `PROJECT-BRIEF.md`, `BRIEF-APPROVAL-RECORD.json`
- Discovery artifacts (`client-discovery-form.md`, `scope-clarification.md`)
- Stakeholder alignment on scope and constraints

#### Execution Algorithm (4-Phase Process)
1. **Source Validation & Alignment** – Validate brief/discovery artifacts with `validate_brief.py` and create design input matrix.
2. **Architecture Decomposition** – Map boundaries using `plan_from_brief.py`, document ADRs, and generate interaction diagrams.
3. **Specification Packaging** – Assemble `TECHNICAL-DESIGN.md`, run `validate_workflow_integration.py`, and produce implementation roadmap.
4. **Review & Handoff** – Record stakeholder approval, archive artifacts, and export task-generation inputs.

#### Quality Gates
- **Source Alignment Gate:** All prerequisite artifacts validated.
- **Architecture Integrity Gate:** Boundaries, ADRs, diagrams complete.
- **Design Validation Gate:** Compliance checks pass, risks mitigated.
- **Stakeholder Approval Gate:** Approval recorded with timestamp and owner.

#### Automation Hooks
- `validate_brief.py`
- `plan_from_brief.py`
- `validate_workflow_integration.py`

#### Outputs
- `TECHNICAL-DESIGN.md`
- `.artifacts/design/design-validation-report.json`
- `.artifacts/design/task-generation-input.json`
- `.artifacts/design/design-approval-record.json`

### Protocol 7: Development Environment Setup & Validation
**Role:** DevOps Environment Engineer
**File:** `7-environment-setup-validation.md`

#### Purpose
Provision and validate a reproducible development environment aligned with the technical design, delivering a documented onboarding package for engineering teams.

#### Prerequisites
- Technical design artifacts (`TECHNICAL-DESIGN.md`, validation report)
- Bootstrap context kit (`.cursor/context-kit/`, `.artifacts/bootstrap/`)
- Access to repository credentials, secrets, and infrastructure endpoints

#### Execution Algorithm (4-Phase Process)
1. **Preflight Requirements Extraction** – Derive tooling/services from design artifacts and confirm credential readiness.
2. **Provisioning & Diagnostics** – Run `doctor.py --strict`, execute `scripts/setup.sh`, and document provisioning outputs.
3. **Configuration & Validation** – Apply configs with `scaffold_phase_artifacts.py` and execute `install_and_test.sh --smoke`.
4. **Documentation & Distribution** – Produce `ENVIRONMENT-README.md`, record approval, and publish onboarding archive.

#### Quality Gates
- **Requirements Confirmation Gate:** Requirements and credentials documented.
- **Tooling Health Gate:** Diagnostics succeed with compliant versions.
- **Validation Suite Gate:** Smoke/lint/migration suite passes on clean setup.
- **Onboarding Package Gate:** Handbook, approval, and onboarding bundle completed.

#### Automation Hooks
- `doctor.py --strict`
- `scripts/setup.sh --non-interactive`
- `scaffold_phase_artifacts.py --phase env`
- `install_and_test.sh --smoke`

#### Outputs
- `.artifacts/environment/environment-requirements.md`
- `.artifacts/environment/validation-suite-report.json`
- `ENVIRONMENT-README.md`
- `.artifacts/environment/environment-onboarding.zip`

## 5. Phase 3: Execution Protocol

### Protocol 3: Controlled Task Execution
**Role:** AI Paired Developer  
**File:** `3-process-tasks.md`

#### Purpose
Execute technical task plan from Markdown file sequentially and meticulously, following protocol strictly in execution loop until all tasks complete.

#### Prerequisites
- Task plan file (e.g., `tasks-my-feature.md`)
- Clean chat session for optimal context preservation
- Environment validation complete

#### Execution Algorithm (Execution Loop + Quality Gates)
**Pre-Execution Checks:**
1. **Environment Validation**
   - Check tool versions (`supabase`, `pnpm`, `wrangler`, `node`)
   - Test database connectivity (`supabase status`)
   - Announce detected infrastructure

2. **Production Readiness Validation**
   - Confirm implementation follows production-readiness standards
   - No mock data, proper validation, configuration management

3. **Model Check (Critical)**
   - Identify target parent task from user instruction
   - Verify recommended model from task file
   - Announce model and await confirmation
   - Halt until explicit user confirmation (`Go`)

**Main Execution Loop:**
```
WHILE there are unchecked [ ] sub-tasks for CURRENT parent task:
  1. Sub-Task Context Loading
     - Identify next unchecked sub-task
     - Load just-in-time rule context from [APPLIES RULES: ...]
     - Read each rule file into active context
     - Platform documentation check if needed
     - Announce task execution

  2. Execution
     - Execute task using available tools
     - Apply loaded rules strictly
     - Continuous rule compliance validation
     - Self-verification against task criteria
     - Integrated quick review for critical changes
     - Error handling: STOP on failure

  3. Update and Synchronize
     - Update task file: [ ] → [x]
     - Hybrid commit strategy: granular commits per sub-task
     - Parent task completion checkpoint
     - Mandatory quality gate execution
     - CI workflow status check
     - Evidence capture and state sync

  4. Enhanced Checkpoint
     - Single validation point
     - Execution mode awareness (Focus/Continuous)
     - Mandatory quality gate for parent task completion
     - Resume on user confirmation
```

#### Quality Gates
- **Pre-Execution:** Environment ready, production standards confirmed, model verified
- **Per Sub-Task:** Task complete, rule compliance verified, commit created
- **Per Parent Task:** All sub-tasks complete, quality audit passed, CI status checked
- **Error Handling:** Immediate stop on failure, await user instructions

#### Automation Hooks
- `update_task_state.py` - Task state synchronization to central tracker
- `evidence_report.py` - Evidence capture for current task
- CI workflow integration (`ci-test.yml`, `ci-lint.yml`, `ci-deploy.yml`)

#### Outputs
- Completed code implementation
- Granular commits with descriptive messages
- Evidence artifacts for retrospective
- Quality audit reports
- CI workflow status and results
- Task state synchronization data

## 6. Phase 4: Quality Assurance Protocols

### Protocol 4: Quality Audit Orchestrator
**Role:** Senior Quality Engineer / Audit Orchestrator  
**File:** `4-quality-audit.md`

#### Purpose
Orchestrate execution of specialized review protocols with intelligent routing, unified reporting, and comprehensive quality validation.

#### Prerequisites
- Implementation complete (Protocol 3 finished)
- Access to review protocols and utilities
- CI/CD workflows available for execution

#### Execution Algorithm (Orchestration Process)
1. **Pre-Audit: Automation Enhancement**
   - Execute CI workflows (`ci-test.yml`, `ci-lint.yml` via `run_workflow.py`)
   - Aggregate coverage data (`aggregate_coverage.py`)
   - Validate CI status and results

2. **Mode Determination**
   - Activated with `--mode` flag: `quick`, `security`, `architecture`, `design`, `ui`, `deep-security`, `comprehensive`
   - Default: Interactive selection interface
   - Tool-agnostic command execution

3. **Context Analysis & Protocol Routing**
   - Use `_review-router.md` for intelligent fallback
   - Custom protocols → Generic protocols
   - Context-aware protocol selection

4. **Protocol Execution**
   - Load determined protocol file
   - Execute specialized review instructions
   - Collect findings and evidence

5. **Unified Reporting**
   - Consolidate findings into standardized report
   - Include CI results and coverage data
   - Generate actionable recommendations

#### Quality Gates
- **Pre-Audit:** CI workflows executed successfully
- **Mode Selection:** Appropriate protocol determined
- **Execution:** All review layers completed
- **Reporting:** Comprehensive findings documented

#### Automation Hooks
- `run_workflow.py` - CI workflow orchestration
- `aggregate_coverage.py` - Coverage data aggregation
- Protocol-specific validation scripts

#### Outputs
- Comprehensive quality report
- CI workflow results and status
- Coverage data and metrics
- Actionable remediation steps
- Evidence artifacts for retrospective

---

### Review Protocols

#### Architecture Review Protocol
**File:** `review-protocols/architecture-review.md`

**Purpose:** Generic Architecture-Focused Validation  
**Audit Framework:** LAYER 1 (Software Design & Architecture Compliance) + LAYER 4 (Architecture & Performance)

**Execution Algorithm:**
1. **Boundary Analysis** - Module boundaries, service boundaries, data flow
2. **Communication Scan** - Inter-module communication, API contracts
3. **Pattern Review** - SOLID principles, design patterns, anti-patterns
4. **Performance Check** - Application performance, efficiency, concerns

**Quality Gates:** Architectural health score, critical violations identified, recommendations prioritized

**Outputs:** Architecture health report, violation list, performance recommendations

---

#### Code Review Protocol
**File:** `review-protocols/code-review.md`

**Purpose:** Generic Quick Review  
**Audit Framework:** LAYER 1 (Software Design Compliance) + LAYER 3 (Code Quality & Craftsmanship)

**Execution Algorithm:**
1. **Design Check** - Module boundaries, inter-module communication
2. **Quality Scan** - Master rules compliance, code craftsmanship
3. **Craftsmanship Review** - Anti-patterns, best practices

**Quality Gates:** Code quality score, critical violations identified, remediation steps defined

**Outputs:** Code quality report, anti-pattern identification, craftsmanship recommendations

---

#### Design System Review Protocol
**File:** `review-protocols/design-system.md`

**Purpose:** Generic Design System Review  
**Audit Framework:** LAYER 1 (DDD) + LAYER 5 (Design) with design token compliance

**Execution Algorithm:**
1. **Component Architecture** - Component usage, consistency, reusability
2. **Brand Guidelines** - Visual consistency, brand compliance
3. **Design Token Usage** - Token implementation, consistency
4. **Design System Compliance** - System adherence, patterns

**Quality Gates:** Design system score, brand compliance status, component analysis complete

**Outputs:** Design system health report, brand compliance status, component recommendations

---

#### Pre-Production Security Protocol
**File:** `review-protocols/pre-production.md`

**Purpose:** Generic Deep Security Audit  
**Audit Framework:** LAYER 2 (Security & Multi-Tenant Assurance) + LAYER 7 (Testing & Maintainability)

**Execution Algorithm:**
1. **Deep Security Scan** - Module security, multi-tenant protection, vulnerability assessment
2. **Testing Coverage Analysis** - Test coverage, maintainability review
3. **Dependency Audit** - Security vulnerabilities, dependency management

**Quality Gates:** Security audit complete, test coverage analyzed, dependencies validated

**Outputs:** Production readiness assessment, security audit report, test coverage analysis

---

#### Security Check Protocol
**File:** `review-protocols/security-check.md`

**Purpose:** Generic Security-Focused Audit  
**Audit Framework:** LAYER 2 (Security & Multi-Tenant Assurance)

**Execution Algorithm:**
1. **Boundary Security Check** - Module security, boundary validation
2. **Data Protection Scan** - Multi-tenant data protection, RLS policies
3. **Vulnerability Scan** - SQL injection, auth bypass, security holes
4. **Communication Security** - Secure communication patterns

**Quality Gates:** Security vulnerabilities identified, critical findings documented, remediation steps defined

**Outputs:** Security vulnerability report, critical findings, actionable remediation steps

---

#### UI Accessibility Review Protocol
**File:** `review-protocols/ui-accessibility.md`

**Purpose:** Generic UI/UX Accessibility Review  
**Audit Framework:** LAYER 1 (DDD) + LAYER 6 (UI/UX) with WCAG AA+ compliance

**Execution Algorithm:**
1. **WCAG Compliance** - AA+ standards, accessibility patterns
2. **Responsive Design** - Mobile-first, breakpoint validation
3. **UX Patterns** - User experience patterns, interaction flow
4. **Performance UX** - Core Web Vitals, loading performance
5. **Multi-Tenant UX** - Tenant isolation, user experience consistency

**Quality Gates:** WCAG compliance verified, responsive design validated, UX patterns assessed

**Outputs:** Accessibility score, WCAG metrics, Core Web Vitals analysis, UX improvement recommendations

---

### Review Utilities

#### Review Router Protocol
**File:** `review-protocols/utils/_review-router.md`

**Purpose:** Centralized Review Router for Portfolio Dashboard Stack  
**Algorithm:** Intelligent custom ↔ generic fallback logic

**Execution Algorithm:**
1. **Environment Detection** - Check for `custom/` directory existence
2. **Protocol-Specific Selection** - Select custom or generic protocol based on availability
3. **Tool Adapter Integration** - Standard usage pattern for `/review` command
4. **Fallback Logic** - Automatic fallback from custom to generic protocols

**Quality Gates:** Protocol selection complete, fallback logic validated, tool integration confirmed

**Outputs:** Selected protocol path, execution mode, fallback decisions

---

#### Context Analyzer Protocol
**File:** `review-protocols/utils/context-analyzer.md`

**Purpose:** Enhanced Static Review: Context Analyzer  
**Algorithm:** Intelligent context analysis for Enhanced Static Review

**Execution Algorithm:**
1. **Change Pattern Detection** - Analyze git changes for context (auth, security, data, ui, api, config, test, docs)
2. **Rule Relevance Matching** - Map changes to relevant master rules
3. **Smart Protocol Selection** - Recommend appropriate review protocol based on context

**Quality Gates:** Context analysis complete, rule relevance mapped, protocol recommendation generated

**Outputs:** ChangeContext analysis, RelevantRules mapping, ProtocolRecommendation with confidence

---

#### Enhanced Static Template Protocol
**File:** `review-protocols/utils/enhanced-static-template.md`

**Purpose:** Template for Enhanced Static Protocol for MicroSaaS Custom Protocols  
**Algorithm:** Template structure for Enhanced Static Review

**Execution Algorithm:**
1. **Header Definition** - Protocol name, mode, layers, duration, usage
2. **Context Analysis** - MicroSaaS-specific context analysis
3. **Enhanced Validation** - Rule injection, critical rules, context-triggered rules
4. **Static Framework** - Existing content enhanced with intelligence

**Quality Gates:** Template structure complete, context analysis integrated, validation enhanced

**Outputs:** Protocol template structure, protocol-specific mappings, enhanced execution instructions

---

#### Enhanced Static Validation Protocol
**File:** `review-protocols/utils/enhanced-static-validation.md`

**Purpose:** Enhanced Static Review: Validation & Testing Framework  
**Algorithm:** Baseline comparison → Performance benchmark → Reliability stress → UX validation

**Execution Algorithm:**
1. **Baseline Comparison Testing** - Test metrics (efficiency, accuracy, reliability)
2. **Performance Benchmarking** - Static baseline vs enhanced targets
3. **Reliability Stress Testing** - Edge case scenarios, degradation testing
4. **User Experience Validation** - UX flow testing, satisfaction metrics

**Quality Gates:** Test scenarios complete, performance benchmarks established, reliability validated

**Outputs:** Test metrics, performance benchmarks, UX satisfaction scores, success criteria

---

#### Rule Injection System Protocol
**File:** `review-protocols/utils/rule-injection-system.md`

**Purpose:** Enhanced Static Review: Rule Injection System  
**Algorithm:** Rule registry → Context filtering → Protocol enhancement → Execution

**Execution Algorithm:**
1. **Rule Registry System** - Master rule interface, rule categories
2. **Context-Based Rule Filtering** - Rule match engine, analyze context, filter relevant rules
3. **Protocol Enhancement System** - Enhanced protocol template, implementation examples

**Quality Gates:** Rule registry complete, context filtering validated, protocol enhancement confirmed

**Outputs:** FilteredRules (critical/high/medium/low), EnhancedProtocol with injected rules

---

## 6.5 Deployment & Operations Protocols

### Protocol 11: Production Deployment & Release Management
**Role:** Release Manager
**File:** `11-production-deployment.md`

#### Purpose
Execute controlled deployments by validating readiness, orchestrating staging and production releases, and documenting every action for auditability and recovery.

#### Prerequisites
- Protocol 10 artifacts (staging validation, rollback rehearsal, deployment checklist)
- Protocol 7 environment validation report
- Quality audit approvals and stakeholder sign-off

#### Execution Algorithm (4-Phase Process)
1. **Readiness Verification & Approval** – Confirm prerequisite evidence, finalize release manifest, schedule communication plan.
2. **Staging Deployment Execution** – Run deployment scripts against staging, validate with `validate_workflows.py`, capture UAT snapshot.
3. **Production Deployment & Monitoring** – Request approval, execute production rollout with `deploy_backend.sh`, and run immediate checks using `collect_perf.py`.
4. **Release Review & Documentation** – Monitor stabilization window, compile `DEPLOYMENT-REPORT.md`, deliver retrospective inputs.

#### Quality Gates
- **Readiness Confirmation Gate** – All prerequisites and approvals recorded.
- **Staging Validation Gate** – Staging deployment successful with tests/UAT approved.
- **Production Launch Gate** – Production approval captured, deployment successful, post-checks pass.
- **Stabilization Gate** – Health window metrics within thresholds, release report completed.

#### Automation Hooks
- `deploy_backend.sh`
- `validate_workflows.py --mode staging`
- `collect_perf.py --env production`
- `rollback_backend.sh` / `rollback_frontend.sh`

#### Outputs
- `.artifacts/deployment/deployment-readiness-checklist.json`
- `.artifacts/deployment/staging-deployment-report.json`
- `.artifacts/deployment/production-deployment-report.json`
- `DEPLOYMENT-REPORT.md` and retrospective inputs

---

### Protocol 12: Post-Deployment Monitoring & Observability
**Role:** Site Reliability Engineer (SRE)
**File:** `12-monitoring-observability.md`

#### Purpose
Activate, validate, and tune observability systems immediately after deployment to ensure incidents are detected and triaged within agreed service objectives.

#### Prerequisites
- Deployment evidence (`post-deployment-validation.json`, `deployment-health-log.md`)
- Monitoring requirements from quality audit or compliance teams

#### Execution Algorithm (4-Phase Process)
1. **Instrumentation Alignment & Baseline Capture** – Review deployment outputs, run `collect_perf.py --audit`, record baseline metrics.
2. **Monitoring Activation & Alert Validation** – Configure dashboards, execute alert tests via `workflow_automation.py --workflow alert-test`, update runbooks.
3. **Continuous Observability Assurance** – Schedule checks, correlate alerts with incidents, generate tuning report using `aggregate_coverage.py`.
4. **Handoff & Improvement Loop** – Deliver monitoring package, record approvals, queue improvement actions.

#### Quality Gates
- **Instrumentation Coverage Gate** – No high-risk telemetry gaps remain.
- **Alert Validation Gate** – Synthetic alerts reach on-call responders within SLA.
- **Observability Assurance Gate** – Automation schedule and tuning report documented.
- **Handoff Package Gate** – Monitoring package manifest and approvals completed.

#### Automation Hooks
- `collect_perf.py --env production --audit`
- `workflow_automation.py --workflow alert-test`
- `aggregate_coverage.py --scope monitoring`

#### Outputs
- `.artifacts/monitoring/instrumentation-audit.json`
- `.artifacts/monitoring/alert-test-results.json`
- `.artifacts/monitoring/observability-scorecard.md`
- `.artifacts/monitoring/monitoring-package-manifest.json`

---

### Protocol 13: Incident Response & Rollback
**Role:** Incident Commander
**File:** `13-incident-response-rollback.md`

#### Purpose
Coordinate rapid mitigation of production incidents triggered after deployment, execute rollback when necessary, and deliver complete evidence for postmortem analysis.

#### Prerequisites
- Monitoring package outputs (`monitoring-package-manifest.json`, `alert-test-results.json`)
- Deployment rollback plan and production deployment logs

#### Execution Algorithm (4-Phase Process)
1. **Incident Detection & Severity Assessment** – Monitor alerts, classify severity, log communications.
2. **Containment & Mitigation Planning** – Draft mitigation/rollback plan, validate readiness, capture decision log.
3. **Execution & Verification** – Run mitigation or rollback scripts, validate recovery with `validate_workflows.py --mode recovery`, update incident timeline.
4. **Resolution & Documentation** – Confirm resolution, collect root-cause evidence, compile `INCIDENT-REPORT.md`.

#### Quality Gates
- **Severity Alignment Gate** – Severity documented, stakeholders notified.
- **Mitigation Readiness Gate** – Plan approved, rollback prerequisites confirmed.
- **Recovery Validation Gate** – Mitigation executed with successful recovery validation.
- **Resolution & Documentation Gate** – Resolution summary, RCA inputs, incident report completed.

#### Automation Hooks
- `rollback_backend.sh` / `rollback_frontend.sh`
- `validate_workflows.py --mode recovery`
- `restore_workflows.py`
- `retrospective_evidence_report.py --scope incident`

#### Outputs
- `.artifacts/incidents/severity-assessment.json`
- `.artifacts/incidents/mitigation-execution-report.json`
- `.artifacts/incidents/recovery-validation.json`
- `INCIDENT-REPORT.md` and `rca-manifest.json`

---

## 7. Phase 5: Continuous Improvement Protocol

### Protocol 5: Implementation Retrospective
**Role:** Process Improvement Lead  
**File:** `5-implementation-retrospective.md`

#### Purpose
Perform quick code review, focused retrospective, and generate concrete improvement actions for future AI collaboration.

#### Prerequisites
- Final task sign-off complete
- Evidence artifacts available
- Access to rule audit and evidence reports

#### Execution Algorithm (2-Phase Process)
**Pre-Retrospective: Automation Enhancement**
1. **Evidence Aggregation**
   - Execute `retrospective_rules_audit.py` for rule compliance analysis
   - Execute `retrospective_evidence_report.py` for evidence aggregation
   - Aggregate evidence artifacts from all phases
   - Include CI/CD outcomes and quality reports

**Phase 1: Technical Self-Review and Compliance Analysis**
1. **Context Discovery**
   - Invoke Context Discovery protocol (`1-master-rule-context-discovery`)
   - Load all relevant rules and protocols

2. **Rule Compliance Verification**
   - Verify rule location and classification
   - Check rule naming conventions
   - Validate discovery protocol compliance

3. **Conversation Review**
   - Identify manual interventions and corrections
   - Analyze AI performance and accuracy
   - Document process improvements

4. **Source Code Audit**
   - Audit source code against loaded rules
   - Identify rule coverage gaps
   - Document compliance issues

5. **Synthesis**
   - Generate hypotheses about rule effectiveness
   - Analyze rule creation and maintenance issues
   - Identify over-engineering patterns

**Phase 2: Collaborative Retrospective with User**
1. **Retrospective Initiation**
   - Present self-review findings
   - Conduct process analysis
   - Propose concrete improvement actions

2. **Process Analysis**
   - Communication efficiency
   - Technical execution quality
   - Process flow optimization
   - Rule/guideline effectiveness
   - User experience assessment
   - Outcome quality evaluation

3. **Improvement Actions**
   - Generate specific, actionable improvements
   - Validate with user
   - Document lessons learned

#### Quality Gates
- **Pre-Retrospective:** Evidence aggregated, rule audit complete
- **Phase 1:** Self-review complete, compliance verified, synthesis generated
- **Phase 2:** Process analysis complete, improvements validated

#### Automation Hooks
- `retrospective_rules_audit.py` - Rule audit for retrospective analysis
- `retrospective_evidence_report.py` - Evidence aggregation and analysis

#### Outputs
- Retrospective report with findings and recommendations
- Rule updates and improvements
- Process optimization actions
- Lessons learned documentation
- Evidence-based improvement plan

---

### Protocol 8: Script Governance (Quality Compliant)
**Role:** Automation Compliance Auditor  
**File:** `8-script-governance-protocol.md`

#### Purpose
Establish a governance layer that validates, audits, and enforces consistency across all operational scripts in the `/scripts/` directory.

#### Prerequisites
- Scripts directory with operational scripts
- Access to static analysis tools (pylint, shellcheck, yamllint)
- Protocol 4 quality gates available for extension

#### Execution Algorithm (3-Phase Process)
**Phase 1: Script Discovery and Indexing**
1. **Script Indexing**
   - Locate all `.py`, `.sh`, and `.yml` files in `/scripts/`
   - Build inventory with file name, description, and last modified date
   - Create comprehensive script registry with metadata completeness > 95%
   - Store inventory in `.artifacts/scripts/script-index.json`

2. **Registry Validation**
   - Cross-reference discovered scripts with existing `script-registry.json` if present
   - Validate registry completeness and accuracy
   - Gate: All scripts indexed and validated

**Phase 2: Script Validation and Compliance Check**
1. **Documentation and Structure Validation**
   - Ensure each script has docstring describing purpose, input/output, and expected result
   - Validate script naming conventions and structure
   - Gate: All scripts meet documentation standards

2. **Static Analysis Execution**
   - Run read-only static analysis tools without execution:
     - `pylint` for Python scripts (syntax, style, security flags)
     - `shellcheck` for Shell scripts (syntax, best practices)
     - `yamllint` for YAML files (structure, formatting)
   - Store analysis results in `.artifacts/scripts/static-analysis-report.json`

3. **Artifact Output Compliance**
   - Verify scripts generate evidence files in `.artifacts/` with correct structure and naming
   - Validate JSON artifacts against predefined schemas
   - Gate: All scripts meet artifact compliance standards

4. **Protocol 4 Quality Gates Extension**
   - Apply Protocol 4 quality gates to script-specific compliance:
     - Documentation completeness (from Protocol 4)
     - Artifact integrity validation (from Protocol 4)
     - Traceability requirements (from Protocol 4)
   - Gate: Quality gates successfully extended

**Phase 3: Compliance Reporting and Handoff**
1. **Compliance Summary Generation**
   - Compile script validation results into compliance scorecard
   - Store scorecard in `.cursor/context-kit/script-compliance.json`
   - Include static analysis results and quality gate outcomes

2. **Data Structure Validation**
   - Ensure compliance scorecard contains valid JSON structure with required fields
   - Validate data integrity and completeness
   - Gate: Compliance data structure valid

#### Quality Gates
- **Phase 1:** All scripts discovered and indexed with metadata completeness > 95%
- **Phase 2:** All scripts meet documentation, naming, and artifact compliance standards
- **Phase 3:** Compliance summary successfully generated with valid data structure

#### Automation Hooks
- Static analysis tools integration (pylint, shellcheck, yamllint)
- JSON schema validation for artifacts
- Protocol 4 quality gates extension
- Compliance scorecard generation

#### Outputs
- Script inventory file (`.artifacts/scripts/script-index.json`)
- Static analysis report (`.artifacts/scripts/static-analysis-report.json`)
- Script compliance scorecard (`.cursor/context-kit/script-compliance.json`)
- Validation compliance report (`.artifacts/scripts/validation-report.json`)

#### Integration Points
**Inputs From:**
- Protocol 4 (Quality Audit): Quality audit reports and evidence from previous validation phases
- Usage: Validate that scripts adhere to previously defined quality gates

**Outputs To:**
- Protocol 5 (Implementation Retrospective): script-compliance.json
- Purpose: Enable retrospective analysis of automation quality

## 8. Automation Integration Architecture

The ai-driven-workflow includes comprehensive automation integration across all protocols, ensuring alignment, eliminating gaps, and creating a connected pipeline from client discovery to retrospective.

### Automation Flow Map

```
Protocol 00 (Discovery) → validate_brief.py, score_risks.py, classify_domain.py
                        ↓
Protocol 0 (Bootstrap)  → normalize_project_rules.py, rules_audit_quick.py
                        ↓
Protocol 1 (PRD)        → validate_prd_gate.py, generate_prd_assets.py
                        ↓
Protocol 2 (Tasks)     → validate_tasks.py, enrich_tasks.py
                        ↓
Protocol 3 (Execution) → update_task_state.py, evidence_report.py, run_workflow.py
                        ↓
Protocol 4 (Quality)   → run_workflow.py, aggregate_coverage.py
                        ↓
Protocol 8 (Script Gov) → pylint, shellcheck, yamllint, script-compliance.json
                        ↓
Protocol 5 (Retrospective) → rules_audit_quick.py, evidence_report.py (aggregate mode)
```

### Script Reference Table

| Protocol | Script | Purpose | Integration Point |
|----------|--------|---------|-------------------|
| 00 | `validate_brief.py` | Brief validation & quality scoring | Phase 5.5 |
| 00 | `score_risks.py` | Risk scoring by impact/likelihood | Phase 5.5 |
| 00 | `classify_domain.py` | Domain classification with ML | Phase 5.5 |
| 0 | `normalize_project_rules.py` | Rule metadata normalization | Steps 6.5, 7.5 |
| 0 | `rules_audit_quick.py` | Rule compliance validation | Steps 6.5, 7.5 |
| 1 | `validate_prd_gate.py` | PRD completeness validation | Phase 4.5 |
| 1 | `generate_prd_assets.py` | Generate user stories, schemas | Phase 4.5 |
| 2 | `validate_tasks.py` | Task file validation | Phase 4.5 |
| 2 | `enrich_tasks.py` | Task metadata enhancement | Phase 4.5 |
| 3 | `update_task_state.py` | Task state synchronization | Steps 3.5, 3.6 |
| 3 | `evidence_report.py` | Evidence capture & aggregation | Steps 3.5, 3.6 |
| 4 | `run_workflow.py` | CI workflow orchestration | Pre-Audit |
| 4 | `aggregate_coverage.py` | Coverage data aggregation | Pre-Audit |
| 8 | `pylint` | Python script static analysis | Phase 2 |
| 8 | `shellcheck` | Shell script static analysis | Phase 2 |
| 8 | `yamllint` | YAML file static analysis | Phase 2 |
| 8 | `script-compliance.json` | Compliance scorecard generation | Phase 3 |
| 5 | `rules_audit_quick.py` | Rule audit for retrospective | Pre-Retrospective |
| 5 | `evidence_report.py` | Evidence aggregation | Pre-Retrospective |

### Integration Checkpoints

Each protocol includes automation checkpoints that validate:
- **Script Execution**: All automation scripts run successfully
- **Quality Gates**: Validation scores meet thresholds
- **Evidence Capture**: Artifacts are properly stored
- **State Synchronization**: Task state is updated correctly

### Quality Gates per Protocol

| Protocol | Gate Criteria | Validation Threshold |
|----------|---------------|---------------------|
| 00 | Brief validation, risks scored, domain classified | Brief score ≥ 80 |
| 0 | Rules normalized, audit report generated | All rules validated |
| 1 | Assets generated, PRD validation complete | PRD score ≥ 85 |
| 2 | Tasks validated and enriched | All tasks enhanced |
| 3 | Task state synced, evidence captured | State synchronized |
| 4 | CI workflows executed, coverage aggregated | CI status checked |
| 8 | Scripts indexed, static analysis complete, compliance scorecard generated | Script compliance validated |
| 5 | Rule audit complete, evidence aggregated | Audit complete |

## 9. Quick Start Guide

### Step 0: Client Discovery
**Role:** Client Discovery Specialist

Transform any job post into a structured project brief:

```
Apply instructions from ai-driven-workflow/00-client-discovery.md

--- JOB POST START ---
[Your job post content here]
--- JOB POST END ---
```

### Step 1: Bootstrap Your Project
**Role:** Project Analyst

```
Apply instructions from ai-driven-workflow/0-bootstrap-your-project.md
```

### Step 2: Create PRD
**Role:** Product Manager

```
Apply instructions from ai-driven-workflow/1-create-prd.md

Here's the feature I want to build: [Describe your feature in detail]
```

### Step 3: Generate Tasks
**Role:** Tech Lead

```
Apply instructions from ai-driven-workflow/2-generate-tasks.md to @prd-my-feature.md
```

### Step 4: Execute Tasks
**Role:** Paired Developer

```
Apply instructions from ai-driven-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 1.
```

### Step 5: Quality Audit
**Role:** Quality Engineer

```
Apply instructions from ai-driven-workflow/4-quality-audit.md
```

### Step 6: Script Governance
**Role:** Automation Compliance Auditor

```
Apply instructions from ai-driven-workflow/8-script-governance-protocol.md
```

### Step 7: Retrospective
**Role:** Process Improvement Lead

```
Apply instructions from ai-driven-workflow/5-implementation-retrospective.md
```

## 10. Protocol Selection Guide

### When to Use Which Protocol

| Phase | Protocol | When to Use | Prerequisites |
|-------|----------|-------------|---------------|
| 0 | Bootstrap | New project setup, rule configuration | Project repository |
| 0 | Client Discovery | Job post analysis, requirement gathering | Raw requirements |
| 0 | Generate Rules | Project-specific rule creation | Bootstrap complete |
| 1 | Create PRD | Feature specification, technical design | Brief validated |
| 2 | Generate Tasks | Implementation planning, task breakdown | PRD complete |
| 3 | Process Tasks | Code implementation, execution | Tasks generated |
| 4 | Quality Audit | Code review, quality validation | Implementation complete |
| 8 | Script Governance | Script validation, compliance audit | Quality audit complete |
| 5 | Retrospective | Process improvement, lessons learned | Script governance complete |

### Dependencies and Prerequisites

- **Phase 0** (Foundation): No dependencies, entry point
- **Phase 1-2** (Planning): Requires Phase 0 completion
- **Phase 3** (Execution): Requires Phase 1-2 completion
- **Phase 4** (Quality): Requires Phase 3 completion
- **Phase 8** (Script Governance): Requires Phase 4 completion
- **Phase 5** (Retrospective): Requires Phase 8 completion

## 11. Troubleshooting

### Common Issues

**Issue:** Script not found
```
Error: python scripts/script_name.py: No such file or directory
```
**Fix:** Check script exists and is executable: `chmod +x scripts/script_name.py`

**Issue:** Automation gate failure
```
[GATE FAILED] Automation Validation Complete
```
**Fix:** Check automation script output for specific errors and address underlying issues

**Issue:** Evidence pipeline broken
```
Missing evidence artifacts in retrospective
```
**Fix:** Verify evidence capture in Protocol 3 and aggregation in Protocol 5

**Issue:** CI workflow integration issues
```
CI workflows not executing or results not captured
```
**Fix:** Verify GitHub Actions workflow files exist and `run_workflow.py` configuration

### Validation Commands

```bash
# Validate entire workflow integration
python scripts/validate_workflow_integration.py

# Run integration tests
bash scripts/test_workflow_integration.sh

# Check specific protocol
python scripts/validate_brief.py brief.md --verbose
```

## 12. Documentation References

- **[INTEGRATION-GUIDE.md](INTEGRATION-GUIDE.md)** - Complete automation integration documentation
- **[VALIDATION-GUIDE.md](VALIDATION-GUIDE.md)** - Validation system documentation
- **[Protocol Files](.)** - Individual protocol documentation

## 13. Continuous Validation

The workflow includes continuous validation through:
- **GitHub Actions**: Automated validation on every commit
- **Integration Tests**: End-to-end workflow testing
- **Quality Gates**: Validation at each protocol checkpoint
- **Evidence Pipeline**: Traceable execution history

---

## 14. Folder Overview and Key Files

This directory contains the end-to-end ai-driven-workflow protocols and the unified quality review system used throughout the repository.

### Directory structure (high level)

- `README.md` – Overview and usage of the 33-protocol lifecycle with automation
- `INTEGRATION-GUIDE.md` – Detailed automation integration guide
- `VALIDATION-GUIDE.md` – Validation and quality gate details
- `0-bootstrap-your-project.md` – Protocol 0 bootstrap procedure
- `00-client-discovery.md` – Protocol 00 client discovery
- `00-generate-rules.md` – Protocol 00 rule generation command
- `1-create-prd.md` – Protocol 1 PRD creation
- `6-technical-design-architecture.md` – Protocol 6 technical design & architecture specification
- `2-generate-tasks.md` – Protocol 2 task generation
- `7-environment-setup-validation.md` – Protocol 7 environment setup & validation
- `3-process-tasks.md` – Protocol 3 controlled execution
- `4-quality-audit.md` – Unified review orchestrator and entry point
- `11-production-deployment.md` – Protocol 11 deployment & release management
- `12-monitoring-observability.md` – Protocol 12 monitoring & observability
- `13-incident-response-rollback.md` – Protocol 13 incident response & rollback
- `5-implementation-retrospective.md` – Protocol 5 retrospective
- `review-protocols/` – Library of specialized review protocols and utilities

### Key interactions

- Orchestrated reviews are invoked via `4-quality-audit.md` and leverage utilities under `review-protocols/utils/`.
- Protocol 3 mandates running Protocol 4 (comprehensive audit) and then Protocol 5 (retrospective) per parent task.

### Quick links (protocol entry points)

- Bootstrap → `0-bootstrap-your-project.md`
- Discovery → `00-client-discovery.md`
- Rules → `00-generate-rules.md`
- PRD → `1-create-prd.md`
- Architecture → `6-technical-design-architecture.md`
- Tasks → `2-generate-tasks.md`
- Environment → `7-environment-setup-validation.md`
- Execute → `3-process-tasks.md`
- Review → `4-quality-audit.md`
- Deploy → `11-production-deployment.md`
- Monitor → `12-monitoring-observability.md`
- Incident Response → `13-incident-response-rollback.md`
- Retro → `5-implementation-retrospective.md`

### Notes on advanced features

- Interactive, tool‑agnostic review selection is centralized in `4-quality-audit.md` and routes through `_review-router.md` for automatic custom↔generic fallback.
- Automation checkpoints and evidence capture are integrated across protocols to maintain auditable execution.
- All 34 protocols documented with complete execution logic, quality gates, automation hooks, and outputs.
