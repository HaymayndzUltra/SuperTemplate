# Scripts Audit & Optimization Report

## Executive Summary
The scripts directory contains 93 Python and shell utilities, but only 18 (22%) are registered in `script-registry.json`, leaving 75 automation assets unmanaged. Protocols reference 160 validators that do not exist, and several flagship utilities simulate behaviour rather than executing real checks. Without registration, documentation, and testing, the automation layer cannot support the protocol quality gates.

Highlights:
- **Registry coverage is incomplete** – the registry lists eight functional groups with only 18 script bindings, omitting most validation tools referenced by the protocols.【F:scripts/script-registry.json†L1-L22】
- **Critical scripts are placeholders** – `quality_gates.py` synthesizes findings instead of executing real checks, and `simulate_protocol_execution.py` dereferences an undefined attribute, causing runtime failures.【F:scripts/quality_gates.py†L70-L193】【F:scripts/simulate_protocol_execution.py†L125-L220】
- **Documentation over-promises** – `scripts/README.md` describes extensive capabilities, yet many promised validators are missing or unregistered, highlighting governance drift.【F:scripts/README.md†L1-L200】

## Script Inventory & Categorization
The table below captures every executable script, a heuristically assigned category, and registry status.

| Name | Relative Path | Category | Registered | Notes |
|------|---------------|----------|------------|-------|
| `__init__.py` | `__init__.py` | bootstrap | No | - |
| `aggregate_coverage.py` | `aggregate_coverage.py` | generation | No | - |
| `ai_executor.py` | `ai_executor.py` | other | No | - |
| `ai_orchestrator.py` | `ai_orchestrator.py` | execution | No | - |
| `analyze_brief.py` | `analyze_brief.py` | other | No | - |
| `analyze_jobpost.py` | `analyze_jobpost.py` | other | No | - |
| `analyze_project_rules.py` | `analyze_project_rules.py` | governance | No | - |
| `backup_workflows.py` | `backup_workflows.py` | execution | No | - |
| `benchmark_generation.py` | `benchmark_generation.py` | other | No | - |
| `bootstrap_project.py` | `bootstrap_project.py` | bootstrap | No | - |
| `brief_processor.py` | `brief_processor.py` | other | No | - |
| `build_submission_pack.sh` | `build_submission_pack.sh` | generation | No | - |
| `check_compliance_docs.py` | `check_compliance_docs.py` | validation | No | - |
| `check_hipaa.py` | `check_hipaa.py` | validation | No | - |
| `classify_domain.py` | `classify_domain.py` | bootstrap | Yes | - |
| `collect_coverage.py` | `collect_coverage.py` | generation | Yes | - |
| `collect_perf.py` | `collect_perf.py` | generation | No | - |
| `compare_pull_requests.py` | `compare_pull_requests.py` | other | No | - |
| `compliance_validator.py` | `compliance_validator.py` | validation | No | - |
| `deploy_backend.sh` | `deploy_backend.sh` | deployment | No | - |
| `detect_instruction_conflicts.py` | `detect_instruction_conflicts.py` | validation | No | - |
| `doctor.py` | `doctor.py` | validation | No | - |
| `e2e_from_brief.sh` | `e2e_from_brief.sh` | other | No | - |
| `enforce_gates.py` | `enforce_gates.py` | validation | No | - |
| `enrich_tasks.py` | `enrich_tasks.py` | other | Yes | - |
| `evidence_manager.py` | `evidence_manager.py` | governance | No | - |
| `evidence_report.py` | `evidence_report.py` | governance | Yes | - |
| `evidence_schema_converter.py` | `evidence_schema_converter.py` | governance | No | - |
| `external_services.py` | `external_services.py` | other | No | - |
| `generate_client_project.py` | `generate_client_project.py` | generation | No | - |
| `generate_consistency_report.py` | `generate_consistency_report.py` | generation | No | - |
| `generate_from_brief.py` | `generate_from_brief.py` | generation | Yes | - |
| `generate_prd_assets.py` | `generate_prd_assets.py` | generation | Yes | - |
| `generate_protocol_sequence.py` | `generate_protocol_sequence.py` | generation | No | - |
| `init-project.sh` | `init-project.sh` | bootstrap | No | - |
| `init_client_project.py` | `init_client_project.py` | bootstrap | No | - |
| `install_and_test.sh` | `install_and_test.sh` | other | No | - |
| `lane_executor.py` | `lane_executor.py` | execution | No | - |
| `lifecycle_tasks.py` | `lifecycle_tasks.py` | other | Yes | - |
| `migrate_evidence_data.py` | `migrate_evidence_data.py` | governance | No | - |
| `normalize_project_rules.py` | `normalize_project_rules.py` | bootstrap | Yes | - |
| `optimize_project_rules.py` | `optimize_project_rules.py` | governance | No | - |
| `plan_from_brief.py` | `plan_from_brief.py` | bootstrap | No | - |
| `pr-bundle.sh` | `pr-bundle.sh` | generation | No | - |
| `pre_lifecycle_plan.py` | `pre_lifecycle_plan.py` | bootstrap | No | - |
| `project_generator_orchestration.py` | `project_generator_orchestration.py` | other | No | - |
| `quality_gates.py` | `quality_gates.py` | validation | Yes | - |
| `real_external_validation.py` | `real_external_validation.py` | other | No | - |
| `real_monitoring_dashboard.py` | `real_monitoring_dashboard.py` | validation | No | - |
| `real_third_party_validator.py` | `real_third_party_validator.py` | other | No | - |
| `restore_workflows.py` | `restore_workflows.py` | execution | No | - |
| `retrospective_evidence_report.py` | `retrospective_evidence_report.py` | governance | No | - |
| `retrospective_rules_audit.py` | `retrospective_rules_audit.py` | validation | No | - |
| `review_protocol_loader.py` | `review_protocol_loader.py` | governance | No | - |
| `rollback_backend.sh` | `rollback_backend.sh` | deployment | No | - |
| `rollback_frontend.sh` | `rollback_frontend.sh` | deployment | No | - |
| `router_benchmark.py` | `router_benchmark.py` | other | No | - |
| `rules_audit_quick.py` | `rules_audit_quick.py` | validation | No | - |
| `run_generate_rules.py` | `run_generate_rules.py` | generation | No | - |
| `run_workflow.py` | `run_workflow.py` | execution | Yes | - |
| `scaffold_briefs.py` | `scaffold_briefs.py` | bootstrap | No | - |
| `scaffold_phase_artifacts.py` | `scaffold_phase_artifacts.py` | bootstrap | No | - |
| `scan_deps.py` | `scan_deps.py` | validation | No | - |
| `score_risks.py` | `score_risks.py` | validation | No | - |
| `select_stacks.py` | `select_stacks.py` | other | No | - |
| `setup.sh` | `setup.sh` | bootstrap | No | - |
| `setup_template_tests.sh` | `setup_template_tests.sh` | bootstrap | No | - |
| `simulate_protocol_execution.py` | `simulate_protocol_execution.py` | execution | No | - |
| `standardize_frontmatter.py` | `standardize_frontmatter.py` | other | No | - |
| `sync_from_scaffold.py` | `sync_from_scaffold.py` | bootstrap | No | - |
| `system_instruction_formatter.py` | `system_instruction_formatter.py` | generation | No | - |
| `test_circular_validation.py` | `test_circular_validation.py` | validation | No | - |
| `test_policy_decisions.py` | `test_policy_decisions.py` | validation | No | - |
| `test_workflow_integration.sh` | `test_workflow_integration.sh` | validation | No | - |
| `tone_mapper.py` | `tone_mapper.py` | other | No | - |
| `trigger_plan.py` | `trigger_plan.py` | other | Yes | - |
| `update_task_state.py` | `update_task_state.py` | execution | Yes | - |
| `validate_ai_directives.py` | `validate_ai_directives.py` | validation | No | - |
| `validate_brief.py` | `validate_brief.py` | validation | No | - |
| `validate_compliance_assets.py` | `validate_compliance_assets.py` | validation | No | - |
| `validate_prd_gate.py` | `validate_prd_gate.py` | validation | Yes | - |
| `validate_proposal.py` | `validate_proposal.py` | validation | No | - |
| `validate_protocol_handoffs.py` | `validate_protocol_handoffs.py` | validation | No | - |
| `validate_protocol_steps.py` | `validate_protocol_steps.py` | validation | No | - |
| `validate_protocols.py` | `validate_protocols.py` | validation | No | - |
| `validate_script_bindings.py` | `validate_script_bindings.py` | validation | No | - |
| `validate_tasks.py` | `validate_tasks.py` | validation | No | - |
| `validate_workflow_completeness.py` | `validate_workflow_completeness.py` | validation | No | - |
| `validate_workflow_integration.py` | `validate_workflow_integration.py` | validation | No | - |
| `validate_workflows.py` | `validate_workflows.py` | validation | No | - |
| `validation_gates.py` | `validation_gates.py` | other | No | - |
| `workflow_automation.py` | `workflow_automation.py` | execution | No | - |
| `write_context_report.py` | `write_context_report.py` | generation | No | - |

## Script-Protocol Mapping Matrix
| Protocol | Referenced Scripts | Purpose Match | Optimal Script | Alternative | Action |
|----------|-------------------|---------------|----------------|------------|--------|
| 01 Client Proposal Generation | `analyze_jobpost.py`, `tone_mapper.py`, `validate_proposal.py`, **missing** `validate_proposal_structure.py` | Partial – gating validator absent | `validate_proposal.py` | Build structure validator | Implement `validate_proposal_structure.py` and register gate.【F:.cursor/ai-driven-workflow/01-client-proposal-generation.md†L134-L167】 |
| 02 Client Discovery Initiation | `validate_discovery_objectives.py`, `validate_discovery_scope.py`, `validate_discovery_expectations.py` (**all missing**) | No | – | Adapt `validate_brief.py` for discovery scope | Ship discovery validators or repurpose existing validation framework.【F:.cursor/ai-driven-workflow/02-client-discovery-initiation.md†L138-L157】 |
| 03 Project Brief Creation | `validate_brief_structure.py`, `validate_discovery_inputs.py` (**missing**) | No | – | Extend `validate_brief.py` | Create structural validator and register outputs.【F:.cursor/ai-driven-workflow/03-project-brief-creation.md†L23-L201】 |
| 04 Project Bootstrap & Context Engineering | `doctor.py`, `normalize_project_rules.py`, `rules_audit_quick.py`, **missing** `validate_scaffold.py` | Partial – scaffold validation missing | `normalize_project_rules.py` | Add real scaffold validator | Build scaffold validator and register evidence export.【F:.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md†L40-L233】 |
| 05 Bootstrap Your Project | `normalize_project_rules.py`, `rules_audit_quick.py`, `validate_repo_mapping.py` (**missing**), `run_protocol_0_gates.py` (**missing**) | Partial | `normalize_project_rules.py` | Extend `validate_workflows.py` for mapping | Deliver mapping validator and quality gate runner.【F:.cursor/ai-driven-workflow/05-bootstrap-your-project.md†L122-L203】 |
| 06 Create PRD | `validate_prd_gate.py`, **missing** `validate_prd_requirements.py`, `aggregate_evidence_1.py` | Partial | `validate_prd_gate.py` | Use `validate_tasks.py` for backlog cross-check | Build requirements validator and evidence aggregator.【F:.cursor/ai-driven-workflow/06-create-prd.md†L139-L210】 |
| 07 Technical Design Architecture | **Missing** `validate_design_handoff.py`, `run_protocol_6_gates.py` | No | – | Extend `validate_protocol_handoffs.py` | Author architecture validators and integrate with registry.【F:.cursor/ai-driven-workflow/07-technical-design-architecture.md†L133-L206】 |
| 08 Generate Tasks | `enrich_tasks.py`, `lifecycle_tasks.py`, **missing** `validate_task_decomposition.py`, `validate_rule_index.py` | Partial | `enrich_tasks.py` | Use `validate_tasks.py` with new checks | Build decomposition validator and register automation.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L127-L212】 |
| 09 Environment Setup Validation | **Missing** `package_environment_assets.py`, `run_protocol_7_gates.py` | No | – | Use `doctor.py` with environment profile | Create packaging command and gate runner.【F:.cursor/ai-driven-workflow/09-environment-setup-validation.md†L126-L210】 |
| 10 Process Tasks | `update_task_state.py`, **missing** `validate_preflight.py`, `validate_session_closeout.py` | Partial | `update_task_state.py` | Extend `validate_tasks.py` for subtask compliance | Implement preflight and close-out validators.【F:.cursor/ai-driven-workflow/10-process-tasks.md†L127-L154】 |
| 11 Integration Testing | **Missing** `validate_environment.py`, `run_contract_tests.py`, `generate_artifact_manifest.py` | No | – | Repurpose `test_workflow_integration.sh` | Build integration validator suite and register outputs.【F:.cursor/ai-driven-workflow/11-integration-testing.md†L47-L152】 |
| 12 Quality Audit | `quality_gates.py`, **missing** `run_comprehensive_review.py`, `validate_gate_4_pre_audit.py` | Partial – simulated findings | `quality_gates.py` | Use review protocols directly | Replace simulation with executable checks and add missing gates.【F:.cursor/ai-driven-workflow/12-quality-audit.md†L129-L216】 |
| 13 UAT Coordination | **Missing** `build_uat_toolkit.py`, `validate_gate_15_entry.py`, etc. | No | – | Use `generate_consistency_report.py` for evidence snapshot | Develop UAT toolkit and acceptance validators.【F:.cursor/ai-driven-workflow/13-uat-coordination.md†L136-L215】 |
| 14 Pre-Deployment Staging | **Missing** `validate_gate_10_security.py`, `aggregate_evidence_10.py` | No | – | Extend `real_monitoring_dashboard.py` | Create staging validators and register packaging scripts.【F:.cursor/ai-driven-workflow/14-pre-deployment-staging.md†L129-L226】 |
| 15 Production Deployment | `deploy_backend.sh`, `rollback_backend.sh`, **missing** `validate_gate_11_launch.py` | Partial | `deploy_backend.sh` | Add Terraform/Helm automation | Implement launch validator and evidence aggregator.【F:.cursor/ai-driven-workflow/15-production-deployment.md†L128-L221】 |
| 16 Monitoring & Observability | **Missing** `validate_gate_12_alerts.py`, `aggregate_evidence_12.py` | No | – | Use `collect_perf.py` for interim metrics | Build alert coverage validator and register dashboards.【F:.cursor/ai-driven-workflow/16-monitoring-observability.md†L125-L214】 |
| 17 Incident Response & Rollback | **Missing** `validate_gate_13_resolution.py`, `aggregate_evidence_13.py` | No | – | Extend `rollback_backend.sh` to emit evidence | Implement incident drill validators and evidence aggregator.【F:.cursor/ai-driven-workflow/17-incident-response-rollback.md†L123-L212】 |
| 18 Performance Optimization | **Missing** `validate_gate_14_baseline.py`, `aggregate_evidence_14.py` | No | – | Expand `collect_perf.py` | Ship baseline validator and register optimization reports.【F:.cursor/ai-driven-workflow/18-performance-optimization.md†L124-L212】 |
| 19 Documentation & Knowledge Transfer | **Missing** `validate_gate_16_completeness.py`, `export_sequence_diagrams.py` | No | – | Use `write_context_report.py` | Create documentation completeness validator and export tool.【F:.cursor/ai-driven-workflow/19-documentation-knowledge-transfer.md†L123-L213】 |
| 20 Project Closure | **Missing** `validate_gate_17_deliverables.py`, `aggregate_evidence_17.py` | No | – | Extend `generate_consistency_report.py` | Implement closure validators tied to deliverables checklist.【F:.cursor/ai-driven-workflow/20-project-closure.md†L125-L212】 |
| 21 Maintenance Support | **Missing** `discover_automation_candidates.py`, `validate_gate_18_governance.py` | No | – | Reuse `rules_audit_quick.py` | Build maintenance backlog analyzers and SLA validators.【F:.cursor/ai-driven-workflow/21-maintenance-support.md†L125-L209】 |
| 22 Implementation Retrospective | **Missing** `generate_retrospective_report.py`, `validate_gate_5_action_plan.py` | No | – | Adapt `retrospective_evidence_report.py` | Deliver retrospective automation and action plan validator.【F:.cursor/ai-driven-workflow/22-implementation-retrospective.md†L120-L211】 |
| 23 Script Governance | `normalize_project_rules.py`, **missing** `validate_gate_8_inventory.py`, `run_protocol_8_gates.py` | Partial | `normalize_project_rules.py` | Use `validate_script_bindings.py` once completed | Build inventory validator tied to registry and enforce registration policy.【F:.cursor/ai-driven-workflow/23-script-governance-protocol.md†L118-L211】 |

## Script Quality Assessment
- **quality_gates.py** logs simulated findings and hard-coded recommendations, so CI/CD enforcement never inspects the real repository. Replace simulation hooks with actual review protocol execution and attach evidence outputs.【F:scripts/quality_gates.py†L70-L193】
- **simulate_protocol_execution.py** references `self.dev_workflow_dir`, an attribute that is never set, causing every simulation run to raise `AttributeError` before it can collect insights.【F:scripts/simulate_protocol_execution.py†L125-L190】
- **normalize_project_rules.py** provides robust frontmatter normalization with clear CLI behaviour; it should become the pattern for new validators (docstring, dry-run support, safe writes).【F:scripts/normalize_project_rules.py†L1-L132】

## Redundancy & Gap Detection
- Numerous validation scripts (`validate_protocols.py`, `validate_protocol_steps.py`, `validate_protocol_handoffs.py`) overlap in responsibility yet remain unregistered and unreferenced by protocols, suggesting consolidation into a single protocol linter suite.【F:scripts/README.md†L16-L28】
- Deployment scripts exist for rollback but lack complementary validators, leaving production gates unsupervised.【F:scripts/README.md†L118-L127】【F:.cursor/ai-driven-workflow/15-production-deployment.md†L128-L221】
- No automation exists for the 160 protocol-referenced validators, representing the most critical automation gap.

## Optimization Recommendations
1. **Registry Expansion** – Register every actively referenced automation script, beginning with existing utilities (`validate_brief.py`, `validate_tasks.py`, `scan_deps.py`) to satisfy gating prerequisites.【F:scripts/script-registry.json†L1-L22】
2. **Validator Implementation Sprint** – Implement missing validators per the mapping matrix, mirroring the structure and CLI ergonomics of `normalize_project_rules.py` to guarantee maintainability.【F:scripts/normalize_project_rules.py†L1-L132】
3. **Quality Gate Refactor** – Replace simulated quality gate logic with concrete execution pipelines that call the new validators and collect evidence artefacts.【F:scripts/quality_gates.py†L70-L193】
4. **Simulation Fixes** – Repair `simulate_protocol_execution.py`, add tests, and wire it into CI to detect protocol drift promptly.【F:scripts/simulate_protocol_execution.py†L125-L220】
5. **Documentation Alignment** – Update `scripts/README.md` once automation exists to ensure advertised capabilities reflect the registered, tested toolchain.【F:scripts/README.md†L1-L200】
