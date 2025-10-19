# Scripts Audit & Optimization Report

## Executive Summary
- **Inventory breadth vs. registry reality.** The repository contains **93 automation scripts**, yet only **13** appear in `script-registry.json`, leaving **69 unregistered (84%)** without governance metadata. 【d8c6a4†L1-L17】【F:scripts/script-registry.json†L1-L19】
- **Protocol alignment is broken.** 47 of the 67 scripts referenced across protocols are missing entirely, including every `aggregate_evidence_*` collector and per-protocol gate runner, so lifecycle gates cannot execute. 【99ddcb†L1-L21】【edfa92†L1-L129】
- **Quality varies and documentation is sparse.** Representative registry scripts such as `validate_prd_gate.py` include docstrings and type hints, but many utilities (e.g., `ai_executor.py`, `workflow_automation` helpers) lack usage documentation, and no automated tests verify their behavior. 【F:scripts/validate_prd_gate.py†L1-L115】【F:scripts/run_workflow.py†L1-L49】
- **Redundant placeholders proliferate.** Multiple protocols reference placeholder commands like `scripts/run_protocol_XX_gates.py` and `scripts/aggregate_evidence_XX.py` that do not exist, duplicating pattern gaps across the lifecycle. 【edfa92†L9-L129】

## Inventory & Categorization
The table below lists every script with a coarse-grained category and registry status.

| Script | Category | Registered |
|---|---|---|
| scripts/__init__.py | Bootstrap & Context | No |
| scripts/aggregate_coverage.py | Execution & Automation | No |
| scripts/ai_executor.py | Execution & Automation | No |
| scripts/ai_orchestrator.py | Execution & Automation | No |
| scripts/analyze_brief.py | Planning & Documentation | No |
| scripts/analyze_jobpost.py | Utilities & Misc | No |
| scripts/analyze_project_rules.py | Governance & Compliance | No |
| scripts/backup_workflows.py | Execution & Automation | No |
| scripts/benchmark_generation.py | Quality & Testing | No |
| scripts/bootstrap_project.py | Bootstrap & Context | No |
| scripts/brief_processor.py | Planning & Documentation | No |
| scripts/build_submission_pack.sh | Deployment & Operations | No |
| scripts/check_compliance_docs.py | Governance & Compliance | No |
| scripts/check_hipaa.py | Governance & Compliance | No |
| scripts/classify_domain.py | Bootstrap & Context | Yes |
| scripts/collect_coverage.py | Execution & Automation | Yes |
| scripts/collect_perf.py | Execution & Automation | No |
| scripts/compare_pull_requests.py | Quality & Testing | No |
| scripts/compliance_validator.py | Governance & Compliance | No |
| scripts/deploy_backend.sh | Deployment & Operations | No |
| scripts/detect_instruction_conflicts.py | Utilities & Misc | No |
| scripts/doctor.py | Bootstrap & Context | No |
| scripts/e2e_from_brief.sh | Planning & Documentation | No |
| scripts/enforce_gates.py | Quality & Testing | No |
| scripts/enrich_tasks.py | Planning & Documentation | Yes |
| scripts/evidence_manager.py | Quality & Testing | No |
| scripts/evidence_report.py | Closure & Retrospective | Yes |
| scripts/evidence_schema_converter.py | Closure & Retrospective | No |
| scripts/external_services.py | Utilities & Misc | No |
| scripts/generate_client_project.py | Execution & Automation | No |
| scripts/generate_consistency_report.py | Utilities & Misc | No |
| scripts/generate_from_brief.py | Bootstrap & Context | Yes |
| scripts/generate_prd_assets.py | Planning & Documentation | Yes |
| scripts/generate_protocol_sequence.py | Utilities & Misc | No |
| scripts/init-project.sh | Bootstrap & Context | No |
| scripts/init_client_project.py | Bootstrap & Context | No |
| scripts/install_and_test.sh | Quality & Testing | No |
| scripts/lane_executor.py | Execution & Automation | No |
| scripts/lifecycle_tasks.py | Planning & Documentation | Yes |
| scripts/migrate_evidence_data.py | Closure & Retrospective | No |
| scripts/normalize_project_rules.py | Bootstrap & Context | Yes |
| scripts/optimize_project_rules.py | Governance & Compliance | No |
| scripts/plan_from_brief.py | Bootstrap & Context | No |
| scripts/pr-bundle.sh | Deployment & Operations | No |
| scripts/pre_lifecycle_plan.py | Planning & Documentation | No |
| scripts/project_generator_orchestration.py | Execution & Automation | No |
| scripts/quality_gates.py | Quality & Testing | Yes |
| scripts/real_external_validation.py | Deployment & Operations | No |
| scripts/real_monitoring_dashboard.py | Deployment & Operations | No |
| scripts/real_third_party_validator.py | Deployment & Operations | No |
| scripts/restore_workflows.py | Execution & Automation | No |
| scripts/retrospective_evidence_report.py | Closure & Retrospective | No |
| scripts/retrospective_rules_audit.py | Bootstrap & Context | No |
| scripts/review_protocol_loader.py | Utilities & Misc | No |
| scripts/rollback_backend.sh | Deployment & Operations | No |
| scripts/rollback_frontend.sh | Deployment & Operations | No |
| scripts/router_benchmark.py | Quality & Testing | No |
| scripts/rules_audit_quick.py | Bootstrap & Context | No |
| scripts/run_generate_rules.py | Governance & Compliance | No |
| scripts/run_workflow.py | Execution & Automation | Yes |
| scripts/scaffold_briefs.py | Bootstrap & Context | No |
| scripts/scaffold_phase_artifacts.py | Bootstrap & Context | No |
| scripts/scan_deps.py | Utilities & Misc | No |
| scripts/score_risks.py | Planning & Documentation | No |
| scripts/select_stacks.py | Bootstrap & Context | No |
| scripts/setup.sh | Bootstrap & Context | No |
| scripts/setup_template_tests.sh | Bootstrap & Context | No |
| scripts/simulate_protocol_execution.py | Utilities & Misc | No |
| scripts/standardize_frontmatter.py | Utilities & Misc | No |
| scripts/sync_from_scaffold.py | Bootstrap & Context | No |
| scripts/system_instruction_formatter.py | Utilities & Misc | No |
| scripts/test_circular_validation.py | Quality & Testing | No |
| scripts/test_policy_decisions.py | Quality & Testing | No |
| scripts/test_workflow_integration.sh | Execution & Automation | No |
| scripts/tone_mapper.py | Utilities & Misc | No |
| scripts/trigger_plan.py | Planning & Documentation | Yes |
| scripts/update_task_state.py | Planning & Documentation | Yes |
| scripts/validate_ai_directives.py | Quality & Testing | No |
| scripts/validate_brief.py | Planning & Documentation | No |
| scripts/validate_compliance_assets.py | Quality & Testing | No |
| scripts/validate_prd_gate.py | Planning & Documentation | Yes |
| scripts/validate_proposal.py | Quality & Testing | No |
| scripts/validate_protocol_handoffs.py | Quality & Testing | No |
| scripts/validate_protocol_steps.py | Quality & Testing | No |
| scripts/validate_protocols.py | Quality & Testing | No |
| scripts/validate_script_bindings.py | Quality & Testing | No |
| scripts/validate_tasks.py | Planning & Documentation | No |
| scripts/validate_workflow_completeness.py | Planning & Documentation | No |
| scripts/validate_workflow_integration.py | Execution & Automation | No |
| scripts/validate_workflows.py | Execution & Automation | No |
| scripts/validation_gates.py | Quality & Testing | No |
| scripts/workflow_automation.py | Execution & Automation | No |
| scripts/write_context_report.py | Closure & Retrospective | No |

### Category Distribution
- **Bootstrap & Context (17 scripts):** scaffolding, rule normalization, stack detection (e.g., `classify_domain.py`, `generate_from_brief.py`).
- **Planning & Documentation (14 scripts):** PRD, brief, and task utilities (`generate_prd_assets.py`, `enrich_tasks.py`).
- **Execution & Automation (15 scripts):** orchestration pipelines and coverage collection (`run_workflow.py`, `aggregate_coverage.py`).
- **Quality & Testing (17 scripts):** validation frameworks and gate controllers (`quality_gates.py`, `collect_coverage.py`).
- **Deployment & Operations (8 scripts):** deployment shell helpers and environment packagers (`deploy_backend.sh`, `install_and_test.sh`).
- **Closure & Retrospective (5 scripts):** evidence summarizers (`evidence_report.py`, `trigger_plan.py`).
- **Governance & Compliance (6 scripts):** HIPAA/compliance validators (`check_hipaa.py`, `compliance_validator.py`).
- **Utilities & Misc (11 scripts):** orchestration support, consistency reports, command helpers (`generate_protocol_sequence.py`, `detect_instruction_conflicts.py`).

## Protocol-Script Mapping Matrix
The matrix highlights the disconnect between protocol expectations and available automation.

| Protocol | Existing Scripts | Missing Scripts |
|---|---|---|
| 00 | — | — |
| 01 | scripts/analyze_jobpost.py, scripts/check_hipaa.py, scripts/enforce_gates.py,… | scripts/aggregate_evidence_01.py, scripts/run_protocol_01_gates.py,… |
| 02 | — | scripts/aggregate_evidence_02.py, scripts/check_client_confirmation.py,… |
| 03 | — | scripts/aggregate_evidence_01.py, scripts/run_protocol_01_gates.py,… |
| 04 | scripts/doctor.py, scripts/evidence_manager.py, scripts/generate_from_brief.py,… | scripts/aggregate_evidence_00.py, scripts/run_protocol_00_gates.py,… |
| 05 | scripts/normalize_project_rules.py, scripts/rules_audit_quick.py | scripts/aggregate_evidence_0.py, scripts/run_protocol_0_gates.py,… |
| 06 | scripts/generate_prd_assets.py, scripts/validate_prd_gate.py | scripts/aggregate_evidence_1.py, scripts/run_protocol_1_gates.py,… |
| 07 | scripts/plan_from_brief.py, scripts/validate_brief.py,… | scripts/aggregate_evidence_6.py, scripts/run_protocol_6_gates.py,… |
| 08 | scripts/enrich_tasks.py, scripts/validate_tasks.py | scripts/aggregate_evidence_2.py, scripts/run_protocol_2_gates.py,… |
| 09 | scripts/doctor.py, scripts/scaffold_phase_artifacts.py | scripts/aggregate_evidence_7.py, scripts/package_environment_assets.py,… |
| 10 | scripts/update_task_state.py | scripts/aggregate_evidence_3.py, scripts/run_protocol_3_gates.py,… |
| 11 | — | scripts/aggregate_evidence_9.py, scripts/generate_artifact_manifest.py,… |
| 12 | — | scripts/aggregate_evidence_4.py, scripts/collect_change_context.py,… |
| 13 | — | scripts/aggregate_evidence_15.py, scripts/build_uat_toolkit.py,… |
| 14 | — | scripts/aggregate_evidence_10.py, scripts/refresh_staging_data.py,… |
| 15 | — | scripts/aggregate_evidence_11.py, scripts/run_protocol_11_gates.py,… |
| 16 | scripts/collect_perf.py | scripts/aggregate_evidence_12.py, scripts/run_protocol_12_gates.py,… |
| 17 | — | scripts/aggregate_evidence_13.py, scripts/run_protocol_13_gates.py,… |
| 18 | — | scripts/aggregate_evidence_14.py, scripts/run_protocol_14_gates.py,… |
| 19 | — | scripts/aggregate_evidence_16.py, scripts/check_doc_style.py,… |
| 20 | — | scripts/aggregate_evidence_17.py, scripts/run_protocol_17_gates.py,… |
| 21 | — | scripts/aggregate_evidence_18.py, scripts/discover_automation_candidates.py,… |
| 22 | — | scripts/aggregate_evidence_5.py, scripts/generate_retrospective_report.py,… |
| 23 | — | scripts/aggregate_evidence_8.py, scripts/run_protocol_8_gates.py,… |
| 24 | — | scripts/aggregate_evidence_00CD.py, scripts/run_protocol_00CD_gates.py,… |
| 25 | — | — |
| 26 | scripts/aggregate_coverage.py, scripts/classify_domain.py,… | scripts/script_name.py |
| 27 | scripts/validate_brief.py, scripts/validate_prd_gate.py,… | scripts/script_name.py |

### Key Findings
1. **Missing core validators:** Every phase relies on non-existent gate runners (e.g., `run_protocol_1_gates.py`, `validate_gate_12_assurance.py`) and evidence aggregators (`aggregate_evidence_*.py`). Without implementations, protocol enforcement collapses. 【edfa92†L9-L129】
2. **Unbalanced registry:** Only six protocols benefit from registered scripts (`classify_domain.py`, `generate_from_brief.py`, `normalize_project_rules.py`, `generate_prd_assets.py`, `enrich_tasks.py`, `run_workflow.py`, `update_task_state.py`, `quality_gates.py`, `collect_coverage.py`, `evidence_report.py`, `trigger_plan.py`). Later phases (deployment, monitoring, maintenance) lack any registered automation.
3. **Placeholder documentation leaks:** Supporting guides still reference `scripts/script_name.py`, confirming that documentation updates never happened after template scaffolding. 【edfa92†L121-L129】
4. **Quality inconsistencies:** Some scripts ship with production-ready behavior (e.g., `collect_coverage.py` gracefully handles missing dependencies), while others import internal packages without safeguards (`run_workflow.py` assumes package availability and lacks CLI examples). 【F:scripts/collect_coverage.py†L1-L35】【F:scripts/run_workflow.py†L1-L49】

## Script Quality Assessment
| Criterion | Observations |
|---|---|
| **Documentation** | Only a handful of scripts contain docstrings or README references; most CLI interfaces omit usage examples beyond inline comments. 【F:scripts/run_workflow.py†L1-L49】 |
| **Maintainability** | Registry scripts leverage internal modules (`workflow_automation`), but no dependency checks exist and unhandled imports will crash when packages are missing in fresh environments. 【F:scripts/run_workflow.py†L1-L33】 |
| **Integration** | Registered scripts map to bootstrap, PRD, execution, quality, and retrospective categories only; deployment, monitoring, and governance phases have zero registered coverage. 【F:scripts/script-registry.json†L1-L19】 |
| **Testing** | No unit tests reside under `scripts/tests/` or similar; commands like `validate_prd_gate.py` rely on manual invocation without verification suites. 【F:scripts/validate_prd_gate.py†L1-L115】 |

## Redundancy & Gap Detection
- **Evidence aggregator family:** 15+ phantom `aggregate_evidence_*.py` files are referenced but not implemented; a single parameterized collector should replace the entire pattern once created. 【edfa92†L9-L129】
- **Gate runners:** `run_protocol_*_gates.py` duplicates the same pattern per protocol. Implementing a generic gate dispatcher (fed by metadata) would remove 20+ template placeholders.
- **Environment packaging:** Protocol 09 expects `package_environment_assets.py`, yet no equivalent exists. Extending `build_submission_pack.sh` or reusing `install_and_test.sh` with parameterization could cover the need without another bespoke script.
- **Doc export tooling:** Knowledge transfer expects `check_doc_style.py` and `export_sequence_diagrams.py`, but neither is implemented. Consider repurposing `evidence_report.py` or integrating standard linters (e.g., `markdownlint`) instead of inventing new scripts.

## Optimization Recommendations
1. **Create a canonical gate runner:** Build `scripts/run_protocol_gates.py` that consumes protocol metadata and executes registered validators. Update all protocols to reference the generic runner.
2. **Implement evidence aggregation library:** Introduce a single `aggregate_evidence.py` with configurable inputs to replace every protocol-specific variant.
3. **Expand the registry:** Register all actively used scripts (doctor, scaffold tools, deployment helpers) and publish descriptions to improve governance visibility.
4. **Add smoke tests:** Create a `tests/scripts/` suite verifying CLI argument parsing and basic execution paths for registry scripts to prevent regressions.
5. **Document invocation patterns:** Extend `scripts/README.md` with usage examples and prerequisites for each high-impact script to reduce onboarding friction.

