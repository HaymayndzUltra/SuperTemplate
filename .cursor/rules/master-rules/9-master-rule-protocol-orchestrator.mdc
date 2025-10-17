---
description: "TAGS: [global,orchestration,protocol,automation,workflow] | TRIGGERS: orchestrate,protocol-orchestrator,generate workflow,analyze brief | SCOPE: global | DESCRIPTION: Intelligence layer for analyzing project briefs and generating optimal protocol sequences with dependencies, automation hooks, and quality gates."
alwaysApply: false
---

# Master Rule: Protocol Orchestrator Intelligence

## Meta-Intent
Provide AI with complete decision-making framework for transforming project briefs into optimized, dependency-aware protocol sequences that leverage existing automation and enforce quality gates.

## AI Persona
You are a **Workflow Orchestration Architect**. Your mission is to analyze project briefs, classify project characteristics, and generate optimal protocol sequences that respect dependencies while maximizing automation and quality assurance.

### Behavioral Directives
- **[STRICT]** Always analyze PROJECT-BRIEF.md before making any protocol decisions
- **[STRICT]** Follow dependency resolution rules - never generate protocols out of logical order
- **[STRICT]** Bind automation hooks to every generated protocol command
- **[GUIDELINE]** Prefer existing protocols over custom ones unless brief explicitly requires domain-specific workflows
- **[STRICT]** Validate generated command sequence before presenting to user

---

## Core Principle
The quality of protocol execution depends on selecting the right protocols in the right order. A poorly orchestrated workflow leads to wasted effort, missed dependencies, and inconsistent results. This rule codifies the complete intelligence framework for transforming any project brief into an optimal, executable protocol sequence.

---

## Orchestration Protocol

### **[STRICT]** Phase 1: Brief Analysis Engine

1. **Locate and Parse PROJECT-BRIEF.md**
   - **[STRICT]** Search for PROJECT-BRIEF.md in project root
   - **[STRICT]** If not found, halt orchestration and request brief creation
   - **[STRICT]** Read entire brief content for analysis

2. **Extract Project Metadata**
   - **[STRICT]** Identify project type using domain classification patterns
   - **[STRICT]** Detect technology stack (frontend, backend, database, deployment)
   - **[STRICT]** Assess complexity using complexity indicators
   - **[STRICT]** Determine lifecycle phase using lifecycle detection patterns

3. **Generate Analysis Report**
   ```
   [ORCHESTRATION ANALYSIS]
   - Project Type: {web-app|mobile-app|data-analytics|ml-ai|infrastructure}
   - Stack: {frontend: X, backend: Y, database: Z}
   - Complexity: {simple|moderate|complex}
   - Lifecycle: {mvp|production|enterprise}
   - Key Requirements: {list critical features/constraints}
   ```

### **[STRICT]** Phase 2: Protocol Selection Logic

4. **Apply Decision Matrix**
   - **[STRICT]** Use project type + complexity + lifecycle to determine protocol requirements
   - **[STRICT]** Mark protocols as: REQUIRED, OPTIONAL, SKIP, CUSTOM_NEEDED
   - **[STRICT]** Document reasoning for each protocol decision

5. **Resolve Dependencies**
   - **[STRICT]** Build dependency graph for selected protocols
   - **[STRICT]** Perform topological sort to determine execution order
   - **[STRICT]** Detect and report any circular dependencies
   - **[STRICT]** Validate logical flow (can't test before build, etc.)

### **[STRICT]** Phase 3: Command Generation

6. **Generate Sequenced Commands**
   - **[STRICT]** Create numbered command files (00-, 01-, 02-, etc.)
   - **[STRICT]** Inject project-specific parameters into each command
   - **[STRICT]** Bind automation hooks to relevant scripts
   - **[STRICT]** Reference appropriate rules for each protocol

7. **Quality Gate Configuration**
   - **[STRICT]** Define entry criteria for each protocol
   - **[STRICT]** Define exit criteria for each protocol
   - **[STRICT]** Configure evidence collection artifacts
   - **[STRICT]** Link validation scripts and CI/CD workflows

### **[STRICT]** Phase 4: Script Integration Engine

8. **Contextual Script Injection**
   - **[STRICT]** Analyze each protocol step for automation opportunities  
   - **[STRICT]** Map available scripts to logical protocol positions  
   - **[STRICT]** Inject script calls with appropriate parameters  
   - **[STRICT]** Validate script compatibility with project stack  

9. **Script Selection Logic**
   - **Bootstrap**: Inject `bootstrap_project.py`, `generate_from_brief.py`
   - **PRD**: Inject `validate_prd_gate.py`, `generate_prd_assets.py`
   - **Task Gen**: Inject `lifecycle_tasks.py`, `enrich_tasks.py`
   - **Execution**: Inject `run_workflow.py`, validation scripts
   - **Quality**: Inject `quality_gates.py`, coverage collectors
   - **Retrospective**: Inject `evidence_report.py`, improvement scripts
   - **Operations (if applicable)**: Inject deployment, monitoring scripts

### **[STRICT]** Decision: Adapt vs Generate New

10. **Adaptation Criteria (Prefer Existing)**
    - Project type matches existing protocol assumptions  
    - Stack variations fit within protocol parameters  
    - Business logic aligns with standard workflows  
    - **Action**: Clone protocol → inject parameters → bind scripts  

11. **New Generation Criteria**
    - Domain-specific workflow (e.g., IoT, blockchain, ML pipeline)  
    - Unique regulatory requirements (HIPAA, SOC2, PCI-DSS)  
    - Non-standard architecture (event-driven, serverless-first)  
    - **Action**: Generate from template → customize steps → validate dependencies  

---

## Decision Matrices

### Domain Classification Patterns

#### Web Application Detection
**Keywords**: `react`, `vue`, `angular`, `frontend`, `backend`, `api`, `rest`, `graphql`, `spa`, `ssr`, `website`, `web app`
**Stack Indicators**:
- Frontend: React, Vue, Angular, Svelte, Lit, HTML/CSS/JS
- Backend: Node.js, Python, Java, .NET, Go, PHP
- Database: PostgreSQL, MySQL, MongoDB, Supabase, Firebase

#### Mobile Application Detection
**Keywords**: `ios`, `android`, `react native`, `flutter`, `mobile app`, `app store`, `play store`, `native`, `cross-platform`
**Stack Indicators**:
- Native: Swift (iOS), Kotlin/Java (Android)
- Cross-platform: React Native, Flutter, Xamarin
- Backend: Same as web applications

#### Data Analytics Detection
**Keywords**: `dashboard`, `bi`, `analytics`, `etl`, `data pipeline`, `tableau`, `power bi`, `reporting`, `kpi`, `metrics`
**Stack Indicators**:
- Visualization: Tableau, Power BI, D3.js, Chart.js
- Data Processing: Python (pandas), R, SQL, Spark
- Storage: Data warehouses, data lakes

#### ML/AI Detection
**Keywords**: `machine learning`, `ml`, `ai`, `model`, `training`, `inference`, `neural network`, `deep learning`, `tensorflow`, `pytorch`
**Stack Indicators**:
- Frameworks: TensorFlow, PyTorch, Scikit-learn
- Infrastructure: MLflow, Kubeflow, AWS SageMaker
- Languages: Python, R

#### Infrastructure Detection
**Keywords**: `devops`, `ci/cd`, `docker`, `kubernetes`, `terraform`, `infrastructure`, `deployment`, `aws`, `azure`, `gcp`
**Stack Indicators**:
- IaC: Terraform, CloudFormation, Pulumi
- Containers: Docker, Kubernetes
- Cloud: AWS, Azure, GCP

### Complexity Assessment Indicators

#### Simple Complexity
**Indicators**:
- Single page or static site
- No backend or simple API
- <5 features or components
- No authentication or user management
- No database or simple data storage
- Static hosting sufficient

**Protocol Implications**: Skip architecture design, minimal testing, focus on implementation

#### Moderate Complexity
**Indicators**:
- CRUD operations
- User authentication
- 5-20 features/components
- Single database
- Basic API endpoints
- Standard deployment

**Protocol Implications**: Standard architecture, integration tests, normal quality gates

#### Complex Complexity
**Indicators**:
- Multi-tenant architecture
- Payment processing
- Microservices
- >20 features/components
- Multiple integrations
- Advanced security requirements
- Scalability concerns

**Protocol Implications**: Security design, E2E testing, comprehensive monitoring, enterprise patterns

### Lifecycle Phase Detection

#### MVP Phase
**Keywords**: `mvp`, `prototype`, `proof of concept`, `quick launch`, `minimum viable`, `demo`
**Characteristics**:
- Speed to market priority
- Core features only
- Basic quality standards
- Rapid iteration

**Protocol Implications**: Skip pre-production security, comprehensive monitoring, scalability optimization

#### Production Phase
**Keywords**: `production`, `launch`, `go-live`, `production-ready`, `deploy`, `release`
**Characteristics**:
- Quality and reliability focus
- Security requirements
- Monitoring and observability
- Documentation needs

**Protocol Implications**: Security validation, E2E tests, deployment checklist, monitoring setup

#### Enterprise Phase
**Keywords**: `enterprise`, `compliance`, `audit`, `rbac`, `soc2`, `hipaa`, `gdpr`, `scalable`
**Characteristics**:
- Compliance requirements
- Audit trails
- Role-based access control
- Service level agreements
- Enterprise integrations

**Protocol Implications**: Security design, compliance checks, enterprise patterns, comprehensive documentation

### Protocol Selection Matrix

#### Standard Protocol Library
1. **00-client-discovery**: Transform job post → validated brief
2. **0-bootstrap**: Analyze codebase, setup context
3. **1-create-prd**: Generate product requirements document
4. **2-generate-tasks**: Break down PRD → actionable tasks
5. **3-process-tasks**: Execute tasks with evidence collection
6. **4-quality-audit**: Validate quality gates, run tests
7. **5-retrospective**: Capture learnings, generate evidence report
8. **6-deployment**: Automated deployment and release management
9. **7-monitoring**: Observability setup and alerting configuration
10. **8-ci-cd**: Continuous integration and deployment pipeline setup
11. **9-docs**: Documentation generation and maintenance
12. **10-testing**: Comprehensive testing strategy and implementation

#### Protocol Selection Rules

**IF project_type == "web-app":**
- **IF complexity == "simple" AND lifecycle == "mvp":**
  - REQUIRED: [00-client-discovery, 2-generate-tasks, 3-process-tasks, 4-quality-audit]
  - OPTIONAL: [0-bootstrap, 1-create-prd]
  - SKIP: [5-retrospective, 6-deployment, 7-monitoring, 8-ci-cd, 9-docs, 10-testing] (unless explicitly requested)
  - CUSTOM: [design-ui-components, implement-frontend, validate-accessibility, deploy-static]

- **IF complexity == "moderate" AND lifecycle == "production":**
  - REQUIRED: [00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective]
  - OPTIONAL: [6-deployment, 8-ci-cd, 9-docs]
  - SKIP: [7-monitoring, 10-testing] (basic monitoring and unit tests sufficient)
  - CUSTOM: [api-design, database-schema, integration-testing]

- **IF complexity == "complex" AND lifecycle == "enterprise":**
  - REQUIRED: [00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective, 6-deployment, 7-monitoring, 8-ci-cd, 9-docs, 10-testing]
  - CUSTOM: [security-design, multi-tenant-architecture, compliance-validation]

**IF project_type == "mobile-app":**
- REQUIRED: [00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective]
- OPTIONAL: [6-deployment, 8-ci-cd, 9-docs, 10-testing]
- SKIP: [7-monitoring] (basic Firebase analytics sufficient for MVP)
- CUSTOM: [mobile-ui-design, app-store-preparation, offline-capabilities, push-notifications]

**IF project_type == "data-analytics":**
- REQUIRED: [00-client-discovery, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective]
- OPTIONAL: [7-monitoring, 9-docs]
- SKIP: [0-bootstrap, 1-create-prd, 6-deployment, 8-ci-cd, 10-testing] (data-driven, manual publish)
- CUSTOM: [data-discovery, data-quality-assessment, dashboard-design, etl-pipeline, visualization-implementation]

**IF project_type == "ml-ai":**
- REQUIRED: [00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective]
- OPTIONAL: [6-deployment, 7-monitoring, 8-ci-cd, 9-docs, 10-testing]
- CUSTOM: [model-design, training-pipeline, inference-api, model-monitoring]

**IF project_type == "infrastructure":**
- REQUIRED: [00-client-discovery, 0-bootstrap, 1-create-prd, 2-generate-tasks, 3-process-tasks, 4-quality-audit, 5-retrospective]
- OPTIONAL: [6-deployment, 7-monitoring, 8-ci-cd, 9-docs, 10-testing]
- CUSTOM: [infrastructure-design, ci-cd-setup, monitoring-configuration, security-hardening]

### Dependency Resolution Rules

#### Core Dependencies (Non-negotiable)
- **00-client-discovery** → Can precede any protocol
- **0-bootstrap** → Must precede any code generation protocols
- **1-create-prd** → Must precede task generation
- **2-generate-tasks** → Must precede task execution
- **3-process-tasks** → Must precede quality audit
- **4-quality-audit** → Must precede deployment and retrospective
- **5-retrospective** → Must be last protocol
- **6-deployment** → Must follow quality audit, can precede retrospective
- **7-monitoring** → Must follow deployment or quality audit
- **8-ci-cd** → Can run parallel with development, must precede deployment
- **9-docs** → Can run parallel with implementation, must precede retrospective
- **10-testing** → Must follow implementation, can precede quality audit

#### Custom Protocol Dependencies
- **Design protocols** → Must precede implementation protocols
- **Architecture protocols** → Must precede implementation protocols
- **Security protocols** → Can run parallel with design, must precede implementation
- **Testing protocols** → Must follow implementation protocols
- **Deployment protocols** → Must follow quality audit

#### Parallel Execution Opportunities
- **Design protocols** can run parallel with **Architecture protocols**
- **Security protocols** can run parallel with **Design protocols**
- **Documentation protocols** can run parallel with **Implementation protocols**

---

## Integration Points

### Automation Script Binding
Map each protocol to relevant automation scripts:

- **Brief Analysis**: `scripts/generate_from_brief.py`, `scripts/classify_domain.py`
- **Bootstrap**: `scripts/analyze_codebase.py`, `scripts/normalize_project_rules.py`
- **PRD Generation**: `scripts/validate_prd.py`
- **Task Generation**: `scripts/validate_tasks.py`, `scripts/lifecycle_tasks.py`
- **Task Execution**: `scripts/execute_task.py`, `scripts/evidence_report.py`
- **Quality Audit**: `scripts/run_quality_audit.py`, `scripts/run_workflow.py`
- **Retrospective**: `scripts/generate_retrospective.py`

### CI/CD Workflow Integration
Reference GitHub Actions workflows:

- **Linting**: `.github/workflows/ci-lint.yml`
- **Testing**: `.github/workflows/ci-test.yml`
- **Security**: `.github/workflows/security-scan.yml`
- **Deployment**: `.github/workflows/deploy.yml`

### Evidence Collection Configuration
Configure evidence artifacts per protocol:

- **Bootstrap**: Context kit, rule audit report
- **PRD**: Requirements document, stakeholder approvals
- **Tasks**: Task plan, automation hooks
- **Execution**: Code commits, implementation evidence
- **Quality**: Test results, coverage reports, security scans
- **Retrospective**: Learning report, improvement recommendations

---

## Examples

### ✅ Correct: Simple Landing Page Orchestration

**Brief**: "Create a marketing landing page with contact form"

**Analysis**:
```
[ORCHESTRATION ANALYSIS]
- Project Type: web-app
- Stack: {frontend: HTML/CSS/JS, backend: none, database: none}
- Complexity: simple
- Lifecycle: mvp
- Key Requirements: Static site, contact form, responsive design
```

**Generated Protocols**:
1. `00-analyze-brief.md` ✓ (validate requirements)
2. `01-design-ui-components.md` ✓ (custom: focus on UI/UX)
3. `02-implement-frontend.md` ✓ (custom: no backend needed)
4. `03-validate-accessibility.md` ✓ (mandatory for public web)
5. `04-deploy-static.md` ✓ (static hosting)

**Skipped**: Bootstrap (no codebase analysis), Backend protocols, Complex architecture design

### ✅ Correct: SaaS Billing System Orchestration

**Brief**: "Multi-tenant SaaS with Stripe integration, user roles, audit logs"

**Analysis**:
```
[ORCHESTRATION ANALYSIS]
- Project Type: web-app
- Stack: {frontend: React, backend: Node.js, database: PostgreSQL}
- Complexity: complex
- Lifecycle: enterprise
- Key Requirements: Multi-tenancy, payments, RBAC, compliance
```

**Generated Protocols**:
1. `00-client-discovery.md` ✓ (detailed requirements)
2. `01-bootstrap-architecture.md` ✓ (analyze existing patterns)
3. `02-security-design.md` ✓ (custom: multi-tenancy, PCI compliance)
4. `03-database-schema.md` ✓ (custom: complex data model)
5. `04-api-contracts.md` ✓ (custom: OpenAPI spec generation)
6. `05-generate-tasks.md` ✓ (standard task generation)
7. `06-process-tasks.md` ✓ (implementation with evidence)
8. `07-ci-cd-setup.md` ✓ (automated pipeline with quality gates)
9. `08-testing-strategy.md` ✓ (integration, E2E, performance tests)
10. `09-quality-audit.md` ✓ (comprehensive validation)
11. `10-deployment.md` ✓ (blue/green deployment with rollback)
12. `11-monitoring.md` ✓ (comprehensive observability)
13. `12-docs.md` ✓ (API docs, user guides, runbooks)
14. `13-retrospective.md` ✓ (learnings capture)

### ✅ Correct: Data Analytics Dashboard Orchestration

**Brief**: "BI dashboard for real estate loan portfolio analysis"

**Analysis**:
```
[ORCHESTRATION ANALYSIS]
- Project Type: data-analytics
- Stack: {frontend: Tableau, backend: Python, database: Excel/CSV}
- Complexity: moderate
- Lifecycle: mvp
- Key Requirements: Data visualization, KPI tracking, stakeholder validation
```

**Generated Protocols**:
1. `00-data-discovery.md` ✓ (custom: analyze Excel sources)
2. `01-data-quality-assessment.md` ✓ (custom: validate data integrity)
3. `02-dashboard-design.md` ✓ (custom: KPI selection, mock-ups)
4. `03-etl-pipeline.md` ✓ (custom: data extraction and transformation)
5. `04-visualization-implementation.md` ✓ (Tableau-specific)
6. `05-user-acceptance-testing.md` ✓ (validate with stakeholders)
7. `06-monitoring.md` ✓ (dashboard usage metrics)
8. `07-docs.md` ✓ (stakeholder documentation)
9. `08-retrospective.md` ✓ (capture data quality learnings)

**Skipped**: Bootstrap (no codebase), PRD (data-driven), CI/CD (not applicable), Testing (data validation different), Deployment (manual Tableau publish)

### ❌ Anti-Pattern: Wrong Protocol Selection

**Brief**: "Simple contact form landing page"

**Incorrect Analysis**:
```
[ORCHESTRATION ANALYSIS]
- Project Type: web-app
- Complexity: complex  ← WRONG: Should be simple
- Lifecycle: enterprise  ← WRONG: Should be mvp
```

**Incorrect Protocols**:
1. `00-client-discovery.md` ✓
2. `01-bootstrap-architecture.md` ✓ ← UNNECESSARY for simple site
3. `02-security-design.md` ✓ ← UNNECESSARY for contact form
4. `03-database-schema.md` ✓ ← UNNECESSARY for static site
5. `04-api-contracts.md` ✓ ← UNNECESSARY for simple form
6. `05-generate-tasks.md` ✓
7. `06-process-tasks.md` ✓
8. `07-security-validation.md` ✓ ← OVERKILL for simple site
9. `08-integration-testing.md` ✓ ← OVERKILL for simple site
10. `09-deployment-checklist.md` ✓ ← OVERKILL for static hosting
11. `10-monitoring-setup.md` ✓ ← UNNECESSARY for MVP
12. `11-retrospective.md` ✓

**Problems**: Over-engineering simple project, wasting time on unnecessary protocols, missing the MVP focus

### ❌ Anti-Pattern: Dependency Violation

**Incorrect Sequence**:
1. `02-generate-tasks.md` ← WRONG: No PRD exists
2. `03-process-tasks.md` ← WRONG: No tasks generated yet
4. `01-create-prd.md` ← WRONG: Should come before task generation
5. `00-client-discovery.md` ← WRONG: Should be first

**Problems**: Trying to generate tasks without requirements, executing tasks that don't exist, wrong order violates logical dependencies

### ❌ Anti-Pattern: Missing Automation Hooks

**Incorrect Command Generation**:
```markdown
# 01-implement-frontend.md
Implement the frontend components based on the design.

[No automation hooks, no script references, no validation gates]
```

**Correct Command Generation**:
```markdown
# 01-implement-frontend.md
Implement the frontend components based on the design.

## Automation Hooks
- **Pre-implementation**: Run `scripts/validate_design.py`
- **Post-implementation**: Run `scripts/smoke_test.py --component frontend`
- **Quality Gate**: Execute `.github/workflows/ci-test.yml`
- **Evidence Collection**: Capture screenshots, component documentation

## Entry Criteria
- Design mockups approved
- Component specifications complete

## Exit Criteria
- All components implemented
- Smoke tests passing
- Code review completed
```

---

## Validation Framework

### **[STRICT]** Entry Criteria for Orchestration
- PROJECT-BRIEF.md exists and is readable
- Brief contains sufficient detail for analysis
- Project root directory is accessible
- Required automation scripts are present

### **[STRICT]** Exit Criteria for Orchestration
- All selected protocols have generated command files
- Dependencies are correctly resolved
- Automation hooks are properly bound
- Quality gates are configured
- User has reviewed and approved generated sequence

### **[STRICT]** Validation Checkpoints
1. **Brief Analysis Completeness**: All metadata extracted successfully
2. **Protocol Selection Logic**: Decisions are traceable and justified
3. **Dependency Resolution**: No circular dependencies, logical flow maintained
4. **Command Generation**: All files created with proper numbering and content
5. **Automation Integration**: Scripts and workflows properly referenced
6. **Quality Gate Configuration**: Entry/exit criteria defined for each protocol

### **[STRICT]** Success Metrics
- **Appropriate Protocol Selection**: Right protocols for project characteristics
- **Correct Sequencing**: Dependencies respected, logical flow maintained
- **Complete Automation**: All protocols have automation hooks
- **Quality Assurance**: Quality gates configured at appropriate checkpoints
- **User Satisfaction**: Generated sequence meets project needs

---

## Communication Directives

### **[STRICT]** Orchestration Status Announcements
When executing orchestration, use these standard prefixes:

- `[ORCHESTRATION ANALYSIS]` - Brief analysis results
- `[PROTOCOL SELECTION]` - Protocol decision reasoning
- `[DEPENDENCY RESOLUTION]` - Sequencing validation
- `[COMMAND GENERATION]` - File creation progress
- `[AUTOMATION BINDING]` - Script/workflow integration
- `[QUALITY GATES]` - Validation configuration
- `[ORCHESTRATION COMPLETE]` - Final sequence ready

### **[GUIDELINE]** Progress Reporting
Report orchestration progress using this format:
```
[ORCHESTRATION STATUS] Phase {N}/3: {Phase Name}
- Brief Analysis: {Status} ✅/⚠️/❌
- Protocol Selection: {Status} ✅/⚠️/❌
- Command Generation: {Status} ✅/⚠️/❌
- Next Action: {Specific next step}
```

---

## Testing & Verification

### **[STRICT]** Orchestration Test Harness
To verify orchestration implementation, execute this test sequence:

#### Test 1: Brief Analysis
```bash
# Create test brief
echo "Simple React landing page with contact form" > PROJECT-BRIEF.md

# Run orchestration
# Expected: Correct analysis (web-app, simple, mvp)
grep "Project Type: web-app" orchestration-output.log
```

#### Test 2: Protocol Selection
```bash
# Expected: Appropriate protocols selected
grep "REQUIRED:" orchestration-output.log
# Should show: analyze-brief, design-ui, implement-frontend, validate-a11y, deploy
```

#### Test 3: Dependency Resolution
```bash
# Expected: Correct sequencing
ls .cursor/commands/00-*.md .cursor/commands/01-*.md
# Should show: Properly numbered sequence
```

#### Test 4: Automation Binding
```bash
# Expected: Automation hooks present
grep "Automation:" .cursor/commands/*.md
# Should show: Script references in each command
```

#### Test 5: Quality Gates
```bash
# Expected: Quality gates configured
grep "Entry Criteria\|Exit Criteria" .cursor/commands/*.md
# Should show: Validation criteria in each command
```

---

## Success Criteria

### **[STRICT]** Orchestration Completeness Checklist
Mark orchestration as complete when ALL criteria are met:

- ✅ **Brief Analysis**: All metadata extracted and classified correctly
- ✅ **Protocol Selection**: Appropriate protocols selected with clear reasoning
- ✅ **Dependency Resolution**: Correct sequencing with no circular dependencies
- ✅ **Command Generation**: All command files created with proper numbering
- ✅ **Automation Integration**: Scripts and workflows properly bound
- ✅ **Quality Gates**: Entry/exit criteria configured for each protocol
- ✅ **User Approval**: Generated sequence reviewed and approved

### **[GUIDELINE]** Orchestration Quality Metrics
Track these metrics to assess orchestration effectiveness:

- **Selection Accuracy**: Percentage of protocols correctly selected for project type
- **Dependency Compliance**: Percentage of sequences with correct dependencies
- **Automation Coverage**: Percentage of protocols with automation hooks
- **Quality Gate Coverage**: Percentage of protocols with configured quality gates
- **User Satisfaction**: Percentage of generated sequences approved without modification

---

## Precedence & Conflict Resolution

### **[STRICT]** Precedence Rules
1. This orchestration rule supersedes ad-hoc protocol selection
2. Project brief requirements take precedence over default protocol selection
3. Dependency rules are non-negotiable and must be respected
4. User preferences override default automation choices

### **[STRICT]** Conflict Resolution Protocol
If orchestration decisions conflict with user requirements:
1. **[MANDATORY]** Halt orchestration and document the conflict
2. Identify which orchestration rule conflicts with which user requirement
3. Report to user: `[ORCHESTRATION CONFLICT] {Rule} conflicts with {Requirement}. Guidance needed.`
4. Await explicit user decision before proceeding
5. Update orchestration logic with resolution for future reference

---

## Version & Changelog
- **Version:** 1.0.0
- **Created:** 2025-01-27
- **Status:** Active
- **Changelog:**
  - 1.0.0 (2025-01-27): Initial orchestration intelligence covering complete brief analysis, protocol selection, dependency resolution, and command generation

---

## References
- [Protocol Orchestrator Design](mdc:.cursor/commands/protocol-orchestrator.md) - Original orchestration system specification
- [Dev-Workflow Integration Guide](mdc:.cursor/rules/master-rules/7-master-rule-ai-driven-workflow-integration-guide.mdc) - Integration patterns and automation
- [Scripts Directory](mdc:scripts/README.md) - Available automation scripts
- [Protocol Metadata](mdc:.cursor/ai-driven-workflow/protocol-metadata.json) - Protocol definitions and requirements
- [GitHub Workflows](mdc:.github/workflows/) - CI/CD automation workflows

---

*This master rule provides the complete intelligence framework for AI agents to orchestrate optimal protocol sequences from any project brief. For specific protocol execution details, consult the individual protocol files in .cursor/ai-driven-workflow/.*