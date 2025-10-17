# AI-Orchestrated Development Workflow System

## Overview

This system provides comprehensive AI-assisted project orchestration with human oversight, compliance validation, and protocol governance. It transforms project briefs into production-ready applications through structured phases with evidence tracking, quality gates, and automated compliance checking. The system integrates reasoning, validation, generation, and compliance automation into a unified AI-to-human collaboration framework.

## Module Map

### **Core Orchestration** (High Importance)
- **`run_workflow.py`** - CLI entry point, configuration loading, main execution hub (orchestration)
- **`ai_orchestrator.py`** - Central AI coordination engine for 7-phase workflow execution (orchestration)
- **`workflow_automation.py`** - Adapter bridging orchestration and quality/validation gates (orchestration)
- **`ai_executor.py`** - Main orchestrator executing complete unified workflow from bootstrap to operations (orchestration)

### **Human Oversight & Validation** (High Importance)
- **`validation_gates.py`** - Human validation checkpoints, approval workflows, evidence tracking (validation)
- **`validate_prd_gate.py`** - Validates PRD sign-off metadata and supporting architecture notes (validation)
- **`validate_workflow_integration.py`** - Validates end-to-end workflow integration (validation)
- **`validate_ai_directives.py`** - Validates AI directive structure and compliance (validation)
- **`detect_instruction_conflicts.py`** - Detects ambiguous, conflicting, or contradictory instructions in protocols (validation)
- **`generate_consistency_report.py`** - Generates comprehensive consistency reports across all protocols (validation)
- **`validate_protocol_steps.py`** - Validates logical flow and sequence of steps within each protocol (validation)
- **`validate_protocol_handoffs.py`** - Validates protocol transitions and handoff logic between phases (validation)
- **`validate_script_bindings.py`** - Validates automation script bindings for unified protocols (validation)
- **`simulate_protocol_execution.py`** - Simulates AI execution of protocols to detect runtime issues (validation)
- **`test_policy_decisions.py`** - Policy router regression test runner with YAML-based fixtures (validation)
- **`check_hipaa.py`** - Lightweight HIPAA compliance checks for session timeout, RBAC, audit logging (validation)
- **`router_benchmark.py`** - Benchmarks router route_decision performance with and without cache (validation)

### **Brief & Generation** (High Importance)
- **`analyze_brief.py`** - Extracts structured metadata, maps protocols, classifies domains (core)
- **`brief_processor.py`** - Unified brief analysis and project generator integration (core)
- **`generate_from_brief.py`** - Generates separate frontend/backend projects with curated Cursor rules (core)
- **`generate_client_project.py`** - Main CLI script for industry-specific, compliance-ready projects (core)
- **`generate_prd_assets.py`** - Generates PRD and architecture summaries from planning artifacts (core)

### **Compliance & Evidence** (High Importance)
- **`compliance_validator.py`** - Performs HIPAA/GDPR/SOX/PCI compliance checks (validation)
- **`evidence_manager.py`** - Comprehensive evidence tracking with SHA-256 checksums and audit trails (evidence)
- **`evidence_schema_converter.py`** - Converts legacy evidence formats to unified schema (evidence)
- **`evidence_report.py`** - Generates comprehensive evidence reports (evidence)
- **`aggregate_coverage.py`** - Aggregates frontend (Jest) and backend (pytest) coverage results (evidence)
- **`collect_coverage.py`** - Collects Python coverage using pytest-cov for CI gating (evidence)
- **`migrate_evidence_data.py`** - Migrates historical evidence data from legacy to unified format (evidence)

### **Workflow & Lifecycle** (Medium Importance)
- **`lifecycle_tasks.py`** - Builds comprehensive task plans from brief specifications (supporting)
- **`update_task_state.py`** - Manages task state transitions and progress tracking (supporting)
- **`enrich_tasks.py`** - Enhances task specifications with additional context (supporting)
- **`plan_from_brief.py`** - Renders structured planning documents from briefs (supporting)

### **Protocol & Instruction Systems** (Medium Importance)
- **`generate_protocol_sequence.py`** - Builds command sequences and integrates with script registry (supporting)
- **`system_instruction_formatter.py`** - Manages authoring, validation, and versioning of system instructions (supporting)
- **`review_protocol_loader.py`** - Loads and parses review playbooks (supporting)
- **`project_generator_orchestration.py`** - Unified project generator adapter for legacy integration (supporting)

### **External Integration** (Medium Importance)
- **`external_services.py`** - Integrates Git, AI Governor, Policy DSL services (supporting)
- **`trigger_plan.py`** - Emits guided trigger/command plan for project generation (supporting)
- **`run_generate_rules.py`** - Lightweight rules generator following generation phase protocols (supporting)

### **Quality Assurance** (Medium Importance)
- **`quality_gates.py`** - Multi-layer quality validation with specialized protocols (validation)
- **`enforce_gates.py`** - Enforces numeric quality gates (coverage, deps, perf) for CI/CD pipelines (validation)

### **Project Initialization & Bootstrapping** (High Importance)
- **`doctor.py`** - Environment health check for Docker, Node, Python, Go with strict mode validation (core)
- **`bootstrap_project.py`** - One-command bootstrap for project initialization from config (core)
- **`init_client_project.py`** - High-level orchestrator for initializing client projects from briefs (core)

### **Domain Analysis & Classification** (Medium Importance)
- **`classify_domain.py`** - Classifies project domain (web-mobile, data-bi, ml-ai, infrastructure) from brief content (supporting)
- **`select_stacks.py`** - Preflight stack selection with engine version validation and substitution support (supporting)
- **`score_risks.py`** - Scores risks by impact and likelihood, generates risk matrix and recommendations (supporting)

### **Planning & Lifecycle Management** (Medium Importance)
- **`pre_lifecycle_plan.py`** - Pre-lifecycle roadmap generator with dynamic gating and validation (supporting)
- **`lane_executor.py`** - Executes tasks by lane respecting dependencies and concurrency limits (supporting)

### **Rules & Documentation Management** (Medium Importance)
- **`analyze_project_rules.py`** - Analyzes and validates project rule documents structure and completeness (supporting)
- **`normalize_project_rules.py`** - Normalizes project rule formatting for consistency (supporting)
- **`optimize_project_rules.py`** - Optimizes project rules for performance and readability (supporting)
- **`standardize_frontmatter.py`** - Standardizes YAML frontmatter across workflow and rule documents (supporting)
- **`rules_audit_quick.py`** - Lightweight quality audit for rule documents (supporting)

### **Retrospective & Audit** (Medium Importance)
- **`retrospective_evidence_report.py`** - Generates retrospective evidence reports for phase review (supporting)
- **`retrospective_rules_audit.py`** - Audits rules from retrospective phase for compliance (supporting)

### **Scaffolding & Template Management** (Low Importance)
- **`scaffold_briefs.py`** - Scaffolds brief templates for new projects (utility)
- **`scaffold_phase_artifacts.py`** - Scaffolds phase-specific artifacts and evidence structures (utility)
- **`sync_from_scaffold.py`** - Syncs project structure from scaffold templates (utility)

### **Dependency & Performance Analysis** (Medium Importance)
- **`scan_deps.py`** - Scans dependencies for vulnerabilities using pip-audit and npm audit (validation)
- **`collect_perf.py`** - Collects performance metrics for quality gate enforcement (validation)

### **Workflow Management & Utilities** (Medium Importance)
- **`backup_workflows.py`** - Backs up workflow configurations and state (utility)
- **`restore_workflows.py`** - Restores workflow configurations from backup (utility)
- **`validate_workflows.py`** - Validates workflow configuration completeness (validation)
- **`validate_tasks.py`** - Validates task specifications and dependencies (validation)
- **`validate_brief.py`** - Validates project brief completeness and structure (validation)
- **`validate_compliance_assets.py`** - Validates compliance asset completeness (validation)
- **`write_context_report.py`** - Writes context analysis reports for governance (supporting)
- **`check_compliance_docs.py`** - Checks compliance documentation completeness (validation)

### **Benchmarking & Testing** (Low Importance)
- **`benchmark_generation.py`** - Benchmarks project generation performance (utility)

### **Shell Automation Scripts** (Medium Importance)
- **`e2e_from_brief.sh`** - End-to-end workflow execution from brief to delivery (orchestration)
- **`init-project.sh`** - Project initialization and setup automation (orchestration)
- **`setup.sh`** - Environment setup automation script (utility)
- **`install_and_test.sh`** - Installation and testing automation for CI/CD (validation)
- **`test_workflow_integration.sh`** - Tests workflow integration end-to-end (validation)
- **`setup_template_tests.sh`** - Sets up template testing environment (utility)
- **`build_submission_pack.sh`** - Builds submission package for deployment (deployment)
- **`deploy_backend.sh`** - Deploys backend services to AWS ECS (deployment)
- **`rollback_backend.sh`** - Rolls back backend deployment to previous version (deployment)
- **`rollback_frontend.sh`** - Rolls back frontend deployment to previous version (deployment)

## Execution Flow

### Step-by-Step Project Pipeline

1. **Project Initialization & Environment Setup**
   - `doctor.py` → validates environment (Docker, Node, Python, Go)
   - `bootstrap_project.py` → one-command project bootstrap from configuration
   - `init_client_project.py` → initializes client project from brief
   - `run_workflow.py` → loads configuration and initializes workflow
   - `ai_executor.py` → creates project directory and loads project config
   - `external_services.py` → initializes Git repository and external integrations

2. **Brief Analysis & Domain Classification**
   - `analyze_brief.py` → extracts structured metadata from project brief
   - `classify_domain.py` → classifies project domain (web-mobile, data-bi, ml-ai, etc.)
   - `score_risks.py` → scores risks by impact and likelihood
   - `brief_processor.py` → processes brief and generates planning artifacts
   - `validate_brief.py` → validates brief completeness and structure

3. **Stack Selection & Pre-Lifecycle Planning**
   - `select_stacks.py` → performs preflight stack selection with engine validation
   - `pre_lifecycle_plan.py` → generates pre-lifecycle roadmap with gating
   - `lifecycle_tasks.py` → builds comprehensive task plans from brief
   - `scan_deps.py` → scans dependencies for vulnerabilities

4. **Protocol Generation & Validation**
   - `generate_protocol_sequence.py` → builds command sequences from brief analysis
   - `trigger_plan.py` → creates guided trigger plan for project generation
   - `validate_protocol_steps.py` → validates protocol step completeness
   - `validate_protocol_handoffs.py` → validates protocol transitions between phases
   - `detect_instruction_conflicts.py` → detects conflicting instructions
   - `simulate_protocol_execution.py` → simulates AI execution to detect runtime issues

5. **AI Validation & Human Approval**
   - `ai_orchestrator.py` → executes AI-driven phases with external service integration
   - `validation_gates.py` → enforces human validation checkpoints at each phase
   - `validate_prd_gate.py` → validates PRD sign-off metadata and architecture
   - `validate_ai_directives.py` → validates AI directive structure and compliance

6. **Project Generation**
   - `generate_from_brief.py` → generates separate frontend/backend projects
   - `generate_client_project.py` → creates industry-specific, compliance-ready projects
   - `generate_prd_assets.py` → generates PRD and architecture summaries
   - `run_generate_rules.py` → generates project-specific Cursor rules
   - `scaffold_phase_artifacts.py` → scaffolds phase-specific artifacts

7. **Task Execution & Progress Tracking**
   - `lane_executor.py` → executes tasks by lane respecting dependencies
   - `update_task_state.py` → manages task state transitions
   - `enrich_tasks.py` → enhances task specifications with context

8. **Compliance & Evidence Reporting**
   - `compliance_validator.py` → performs HIPAA/GDPR/SOX/PCI compliance checks
   - `check_hipaa.py` → lightweight HIPAA compliance checks
   - `evidence_manager.py` → tracks all artifacts with SHA-256 checksums and timestamps
   - `evidence_report.py` → generates comprehensive evidence reports
   - `collect_coverage.py` → collects Python test coverage
   - `aggregate_coverage.py` → aggregates frontend and backend coverage

9. **Quality Gates & Final Validation**
   - `quality_gates.py` → executes multi-layer quality validation
   - `enforce_gates.py` → enforces numeric quality gates for CI/CD
   - `collect_perf.py` → collects performance metrics
   - `validate_workflow_integration.py` → validates end-to-end workflow integration
   - `validate_compliance_assets.py` → validates compliance asset completeness
   - `evidence_schema_converter.py` → ensures evidence format consistency

10. **Retrospective & Continuous Improvement**
    - `retrospective_evidence_report.py` → generates retrospective evidence reports
    - `retrospective_rules_audit.py` → audits rules from retrospective phase
    - `generate_consistency_report.py` → generates consistency reports across protocols
    - `write_context_report.py` → writes context analysis reports

11. **Deployment & Operations**
    - `e2e_from_brief.sh` → end-to-end workflow from brief to delivery
    - `build_submission_pack.sh` → builds submission package
    - `deploy_backend.sh` → deploys backend to AWS ECS
    - `rollback_backend.sh` → rolls back backend deployment
    - `rollback_frontend.sh` → rolls back frontend deployment

## Key Subsystems

### **Human Oversight & Validation**
- **`validation_gates.py`** - Manages human validation checkpoints with approval workflows
- **`validate_prd_gate.py`** - Validates PRD sign-off metadata and architecture requirements
- **`validate_workflow_integration.py`** - Ensures end-to-end workflow integration integrity
- **`validate_ai_directives.py`** - Validates AI directive structure and compliance standards

### **Brief & Generation**
- **`analyze_brief.py`** - Extracts structured metadata and maps protocols from briefs
- **`brief_processor.py`** - Provides unified brief analysis and project generator integration
- **`generate_from_brief.py`** - Generates separate frontend/backend projects with curated rules
- **`generate_client_project.py`** - Main CLI for industry-specific, compliance-ready projects
- **`generate_prd_assets.py`** - Generates PRD and architecture summaries from planning artifacts

### **Compliance & Evidence**
- **`compliance_validator.py`** - Performs HIPAA/GDPR/SOX/PCI compliance validation
- **`evidence_schema_converter.py`** - Converts legacy evidence formats to unified schema
- **`evidence_report.py`** - Generates comprehensive evidence reports for audit trails
- **`aggregate_coverage.py`** - Aggregates frontend and backend test coverage
- **`collect_coverage.py`** - Collects Python test coverage using pytest-cov
- **`check_compliance_docs.py`** - Checks compliance documentation completeness

### **Workflow & Lifecycle**
- **`run_workflow.py`** - CLI entry point and main execution hub
- **`lifecycle_tasks.py`** - Builds comprehensive task plans from brief specifications
- **`update_task_state.py`** - Manages task state transitions and progress tracking
- **`enrich_tasks.py`** - Enhances task specifications with additional context

### **Protocol & Instruction Systems**
- **`generate_protocol_sequence.py`** - Builds command sequences and integrates with script registry
- **`system_instruction_formatter.py`** - Manages authoring, validation, and versioning of system instructions
- **`review_protocol_loader.py`** - Loads and parses review playbooks for quality gates
- **`project_generator_orchestration.py`** - Unified project generator adapter for legacy integration

### **External Integration**
- **`external_services.py`** - Integrates Git, AI Governor, Policy DSL services
- **`trigger_plan.py`** - Emits guided trigger/command plan for project generation
- **`run_generate_rules.py`** - Lightweight rules generator following generation phase protocols
- **`ai_executor.py`** - Main orchestrator executing complete unified workflow

## Human Oversight Layer

### **Validation Gates System**
The `validation_gates.py` script enforces manual checkpoints at critical workflow phases:

- **Phase 0**: Bootstrap completion validation (technical lead, product owner approval)
- **Phase 1**: PRD approval (product owner, stakeholder approval) 
- **Phase 2**: Task generation confirmation (technical lead, developer approval)
- **Phase 3**: Implementation review (technical lead, code reviewer approval)
- **Phase 4**: Quality audit results review (quality engineer, technical lead approval)
- **Phase 5**: Retrospective validation (process owner, team lead approval)
- **Phase 6**: Operations readiness (operations lead, technical lead approval)

### **PRD Gate Validation**
The `validate_prd_gate.py` script ensures PRD artifacts meet quality standards:

- Validates YAML frontmatter with sign-off metadata
- Checks required sections: Overview, Functional Specifications, Technical Specifications, Out of Scope
- Verifies architecture summary completeness
- Ensures proper timestamp and approver information

### **Evidence Tracking & Audit Support**
The evidence system provides comprehensive audit visibility:

- **`evidence_manager.py`** - Tracks all artifacts with SHA-256 checksums and ISO8601 timestamps
- **`evidence_report.py`** - Generates comprehensive evidence reports for compliance audits
- **`evidence_schema_converter.py`** - Ensures evidence format consistency across workflow versions
- **`aggregate_coverage.py`** - Aggregates frontend (Jest) and backend (pytest) coverage results
- **`collect_coverage.py`** - Collects Python test coverage using pytest-cov for CI gating

## Usage

### **Environment Setup & Validation**
```bash
# Check environment health (Docker, Node, Python, Go)
python scripts/doctor.py --strict

# One-command project bootstrap
python scripts/bootstrap_project.py --name my-project --industry healthcare --frontend react --backend nestjs --database postgresql

# Initialize client project from brief
python scripts/init_client_project.py --brief PROJECT-BRIEF.md --generate-scaffold
```

### **Brief Analysis & Domain Classification**
```bash
# Classify project domain from brief
python scripts/classify_domain.py PROJECT-BRIEF.md --output domain-classification.json --verbose

# Score risks by impact and likelihood
python scripts/score_risks.py PROJECT-BRIEF.md --output risk-scores.json --verbose

# Validate brief completeness
python scripts/validate_brief.py --brief PROJECT-BRIEF.md
```

### **Stack Selection & Planning**
```bash
# Select technology stack with engine validation
python scripts/select_stacks.py \
  --industry healthcare \
  --project-type microservices \
  --frontend react \
  --backend nestjs \
  --database postgresql \
  --compliance hipaa,gdpr \
  --output selection.json

# Generate pre-lifecycle roadmap
python scripts/pre_lifecycle_plan.py --brief PROJECT-BRIEF.md --output roadmap.json

# Scan dependencies for vulnerabilities
python scripts/scan_deps.py
```

### **Complete Workflow Execution**
```bash
# End-to-end workflow from brief to delivery
bash scripts/e2e_from_brief.sh

# Complete workflow execution from brief
python scripts/run_workflow.py --brief ./path/to/brief.json

# Initialize project and execute full workflow
python scripts/ai_executor.py init --project my-project
python scripts/ai_executor.py full-workflow --project my-project

# Execute single phase with validation
python scripts/ai_executor.py phase --project my-project --phase 1

# Execute tasks by lane with dependency management
python scripts/lane_executor.py --lane backend --cap 3 --input tasks.json
```

### **What Happens Next**
1. **Auto-generation**: System analyzes brief and generates protocol sequence
2. **Compliance Check**: Automated HIPAA/GDPR/SOX/PCI validation runs
3. **Validation Gates**: Human approval checkpoints are enforced at each phase
4. **Project Generation**: Industry-specific, compliance-ready projects are created
5. **Evidence Collection**: All artifacts are tracked with checksums and timestamps
6. **Quality Gates**: Multi-layer validation ensures production readiness

### **Quality Gates & Validation**
```bash
# Enforce numeric quality gates for CI/CD
python scripts/enforce_gates.py

# Validate PRD gate
python scripts/validate_prd_gate.py --prd PRD.md --architecture ARCHITECTURE.md

# Execute validation gates
python scripts/validation_gates.py request-validation --phase 1
python scripts/validation_gates.py approve-validation --phase 1 --approver "John Doe"

# Validate workflow integration
python scripts/validate_workflow_integration.py

# Validate protocol steps and handoffs
python scripts/validate_protocol_steps.py
python scripts/validate_protocol_handoffs.py

# Detect instruction conflicts
python scripts/detect_instruction_conflicts.py

# Simulate protocol execution
python scripts/simulate_protocol_execution.py
```

### **Evidence & Compliance Reporting**
```bash
# Collect test coverage
python scripts/collect_coverage.py

# Aggregate frontend and backend coverage
python scripts/aggregate_coverage.py

# Collect performance metrics
python scripts/collect_perf.py

# Generate evidence report
python scripts/evidence_report.py --project my-project --output evidence-report.json

# Generate retrospective evidence report
python scripts/retrospective_evidence_report.py

# Check HIPAA compliance
python scripts/check_hipaa.py

# Validate compliance assets
python scripts/validate_compliance_assets.py
```

### **Deployment & Rollback**
```bash
# Build submission package
bash scripts/build_submission_pack.sh

# Deploy backend to AWS ECS
bash scripts/deploy_backend.sh production

# Rollback backend deployment
bash scripts/rollback_backend.sh production

# Rollback frontend deployment
bash scripts/rollback_frontend.sh production
```

### **Rules & Documentation Management**
```bash
# Analyze project rules
python scripts/analyze_project_rules.py

# Normalize project rules formatting
python scripts/normalize_project_rules.py

# Optimize project rules
python scripts/optimize_project_rules.py

# Standardize YAML frontmatter
python scripts/standardize_frontmatter.py

# Quick audit of rule documents
python scripts/rules_audit_quick.py
```

### **Workflow Management**
```bash
# Backup workflows
python scripts/backup_workflows.py

# Restore workflows from backup
python scripts/restore_workflows.py

# Validate workflow configurations
python scripts/validate_workflows.py

# Validate task specifications
python scripts/validate_tasks.py
```

## Extensibility

### **Adding New Compliance Validators**
1. Extend `compliance_validator.py` with new control sets and validation logic
2. Add new compliance standards to the validation matrix
3. Update `validate_prd_gate.py` to include new compliance requirements
4. Integrate with `evidence_manager.py` for audit trail tracking

### **Adding New Workflow Rules**
1. Create new protocol files in `unified_workflow/phases/`
2. Update `generate_protocol_sequence.py` with new phase definitions
3. Add automation hooks to `scripts/script-registry.json`
4. Extend `validation_gates.py` with new checkpoint types

### **Adding New Quality Gates**
1. Extend `quality_gates.py` with new audit modes
2. Create new review protocols in `.cursor/ai-driven-workflow/review-protocols/`
3. Integrate with `review_protocol_loader.py` for protocol management
4. Update `evidence_manager.py` to track new quality metrics

### **Integration Points**
- **Rule System**: Extend `system_instruction_formatter.py` for new instruction types
- **External Services**: Add new service integrations to `external_services.py`
- **Evidence Tracking**: Add new artifact categories to `evidence_manager.py`
- **Workflow Automation**: Add new gate types to `workflow_automation.py`

### **Breaking Change Prevention**
- Maintain backward compatibility in evidence schema conversions
- Preserve existing CLI interfaces while adding new options
- Use feature flags for experimental functionality
- Implement proper error handling and graceful degradation
- Maintain comprehensive test coverage for critical paths

This system provides a robust foundation for AI-driven development workflows while maintaining human oversight and ensuring production readiness through comprehensive validation and compliance checking.