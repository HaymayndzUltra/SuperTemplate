# Scripts Audit & Automation Optimization Report

## Executive Summary
- **Inventory scale:** 96 executable scripts live in `/scripts`, but only 13 are registered for orchestration, leaving 83 untracked by the workflow runtime.【873450†L1-L6】【6c0539†L1-L7】
- **Coverage imbalance:** Quality and planning utilities dominate the catalog (21 and 14 files respectively), while maintenance and deployment automation remain sparse, mirroring the weak later-phase scores.【89d047†L1-L31】
- **Protocol mismatch:** Every production protocol (01–23) cites orchestration and evidence collectors that are missing, so the advertised automation paths are broken despite mature building blocks like `analyze_jobpost.py`, `doctor.py`, `generate_prd_assets.py`, and `collect_perf.py`.【e3745d†L1-L33】【5906f2†L134-L167】【79179f†L153-L250】【b5f2c8†L18-L149】
- **Governance stall:** Script governance (Protocol 23) expects inventory, documentation, and static-analysis artifacts that cannot be produced today because none of the mandated helper scripts or CSV/JSON outputs exist.【b0f694†L24-L104】【b5f2c8†L150-L193】

## Inventory & Categorization
| Category | Script Count |
|---|---|
| bootstrap | 12 |
| planning | 14 |
| execution | 10 |
| quality | 21 |
| deployment | 5 |
| maintenance | 2 |
| tooling | 9 |
| other | 23 |
【89d047†L1-L31】

Key registered entries focus on bootstrap, PRD validation, task enrichment, workflow execution, quality gates, and retrospectives, leaving integration testing, deployment, and maintenance unregistered despite being critical to later phases.【e51091†L1-L20】

Representative mature scripts include:
- `analyze_jobpost.py` – real NLP analysis for proposals.【605912†L1-L78】
- `collect_coverage.py` – CI-friendly coverage gathering with graceful fallbacks.【ef3b7c†L1-L31】
- `update_task_state.py` – task tracker updates with validation.【bc8b86†L1-L44】
- `doctor.py`, `rules_audit_quick.py`, and `collect_perf.py` provide reusable health checks, rule audits, and performance baselines used across early phases.【79179f†L153-L179】【5b16d5†L185-L212】【b5f2c8†L45-L149】

## Protocol-to-Script Mapping Matrix
| Protocol | Current Automation | Purpose Match | Optimal Script Plan | Alternative | Action |
|---|---|---|---|---|---|
| 01 | analyze_jobpost.py, check_hipaa.py (+4 more) / Missing: aggregate_evidence_00A.py, run_protocol_00A_gates.py (+2 more) | Partial | Build aggregate_evidence_00A.py or extend analyze_jobpost.py | analyze_jobpost.py | Add automation & register |
| 02 | None / Missing: aggregate_evidence_00B.py, check_client_confirmation.py (+5 more) | No | Build aggregate_evidence_00B.py or extend new validator | n/a | Add automation & register |
| 03 | None / Missing: aggregate_evidence_01.py, run_protocol_01_gates.py (+4 more) | No | Build aggregate_evidence_01.py or extend new validator | n/a | Add automation & register |
| 04 | doctor.py, evidence_manager.py (+5 more) / Missing: aggregate_evidence_00.py, run_protocol_00_gates.py (+2 more) | Partial | Build aggregate_evidence_00.py or extend doctor.py | doctor.py | Add automation & register |
| 05 | normalize_project_rules.py, rules_audit_quick.py / Missing: aggregate_evidence_0.py, run_protocol_0_gates.py (+4 more) | Partial | Build aggregate_evidence_0.py or extend normalize_project_rules.py | normalize_project_rules.py | Add automation & register |
| 06 | generate_prd_assets.py, validate_prd_gate.py / Missing: aggregate_evidence_1.py, run_protocol_1_gates.py (+3 more) | Partial | Build aggregate_evidence_1.py or extend generate_prd_assets.py | generate_prd_assets.py | Add automation & register |
| 07 | plan_from_brief.py, validate_brief.py (+1 more) / Missing: aggregate_evidence_6.py, run_protocol_6_gates.py (+2 more) | Partial | Build aggregate_evidence_6.py or extend plan_from_brief.py | plan_from_brief.py | Add automation & register |
| 08 | enrich_tasks.py, validate_tasks.py / Missing: aggregate_evidence_2.py, run_protocol_2_gates.py (+4 more) | Partial | Build aggregate_evidence_2.py or extend enrich_tasks.py | enrich_tasks.py | Add automation & register |
| 09 | doctor.py, install_and_test.sh (+2 more) / Missing: aggregate_evidence_7.py, package_environment_assets.py (+3 more) | Partial | Build aggregate_evidence_7.py or extend doctor.py | doctor.py | Add automation & register |
| 10 | update_task_state.py / Missing: aggregate_evidence_3.py, run_protocol_3_gates.py (+5 more) | Partial | Build aggregate_evidence_3.py or extend update_task_state.py | update_task_state.py | Add automation & register |
| 11 | None / Missing: aggregate_evidence_9.py, generate_artifact_manifest.py (+4 more) | No | Build aggregate_evidence_9.py or extend new validator | n/a | Add automation & register |
| 12 | None / Missing: aggregate_evidence_4.py, collect_change_context.py (+8 more) | No | Build aggregate_evidence_4.py or extend new validator | n/a | Add automation & register |
| 13 | None / Missing: aggregate_evidence_15.py, build_uat_toolkit.py (+7 more) | No | Build aggregate_evidence_15.py or extend new validator | n/a | Add automation & register |
| 14 | None / Missing: aggregate_evidence_10.py, deploy_ (+9 more) | No | Build aggregate_evidence_10.py or extend new validator | n/a | Add automation & register |
| 15 | deploy_backend.sh / Missing: aggregate_evidence_11.py, deploy_ (+7 more) | Partial | Build aggregate_evidence_11.py or extend deploy_backend.sh | deploy_backend.sh | Add automation & register |
| 16 | collect_perf.py / Missing: aggregate_evidence_12.py, run_protocol_12_gates.py (+5 more) | Partial | Build aggregate_evidence_12.py or extend collect_perf.py | collect_perf.py | Add automation & register |
| 17 | None / Missing: aggregate_evidence_13.py, run_protocol_13_gates.py (+5 more) | No | Build aggregate_evidence_13.py or extend new validator | n/a | Add automation & register |
| 18 | None / Missing: aggregate_evidence_14.py, run_protocol_14_gates.py (+5 more) | No | Build aggregate_evidence_14.py or extend new validator | n/a | Add automation & register |
| 19 | None / Missing: aggregate_evidence_16.py, check_doc_style.py (+6 more) | No | Build aggregate_evidence_16.py or extend new validator | n/a | Add automation & register |
| 20 | None / Missing: aggregate_evidence_17.py, run_protocol_17_gates.py (+4 more) | No | Build aggregate_evidence_17.py or extend new validator | n/a | Add automation & register |
| 21 | None / Missing: aggregate_evidence_18.py, discover_automation_candidates.py (+5 more) | No | Build aggregate_evidence_18.py or extend new validator | n/a | Add automation & register |
| 22 | None / Missing: aggregate_evidence_5.py, generate_retrospective_report.py (+5 more) | No | Build aggregate_evidence_5.py or extend new validator | n/a | Add automation & register |
| 23 | None / Missing: aggregate_evidence_8.py, artifact-compliance-report.json (+12 more) | No | Build aggregate_evidence_8.py or extend new validator | n/a | Add automation & register |
【e3745d†L1-L33】

**Observations:**
- Protocols 01, 04, 05, 06, 07, 08, 09, 10, 15, and 16 have at least one mature script available, but each still requires new evidence aggregators and gate runners to close the loop.【e3745d†L1-L33】【5906f2†L134-L167】【79179f†L153-L250】
- Protocols 02, 03, 11–14, and 17–23 depend entirely on nonexistent automation, so their quality gates cannot execute at all.【e3745d†L1-L33】【b5f2c8†L26-L193】

## Script Quality Assessment
- **Documentation:** Core scripts feature meaningful docstrings and usage instructions (`analyze_jobpost.py`, `collect_coverage.py`, `update_task_state.py`), but most unregistered validators lack README coverage, preventing onboarding to the automation suite.【605912†L1-L78】【ef3b7c†L1-L31】【bc8b86†L1-L44】【0a9f31†L1-L88】
- **Maintenance:** Many utilities import external libraries specified in `requirements.txt`, yet protocols demanding HIPAA, incident, or performance validation call nonexistent wrappers, implying stalled maintenance for critical automation families.【a71262†L1-L6】【b5f2c8†L118-L149】
- **Integration:** Only 13 scripts appear in the registry, so orchestrators cannot automatically surface the rest. High-value assets such as `doctor.py`, `rules_audit_quick.py`, and `collect_perf.py` must be registered with context metadata to enable reuse across phases.【e51091†L1-L20】【79179f†L153-L250】【b5f2c8†L45-L149】
- **Testing:** The repository contains `test_workflow_integration.sh` and validation harnesses, but protocols cite `run_protocol_*_gates.py`, `validate_gate_*`, and `aggregate_evidence_*` families that have no implementations, leaving automated regression coverage impossible.【0bf469†L1-L4】【b5f2c8†L18-L149】

## Redundancy & Gap Detection
- **Redundancy:** Scripts for rule normalization (`normalize_project_rules.py`, `rules_audit_quick.py`, `optimize_project_rules.py`, `standardize_frontmatter.py`) overlap heavily; consolidating into a single governance package would reduce maintenance while keeping specialized checks available for Protocols 04–05.【0a9f31†L49-L85】【5b16d5†L185-L211】
- **Gap:** No automation exists for `aggregate_evidence_*`, `run_protocol_*_gates.py`, or governance outputs demanded by Protocol 23, leaving evidence aggregation, gate orchestration, and remediation reporting entirely manual.【b5f2c8†L18-L193】【b0f694†L24-L104】
- **Registry gap:** Deploy, monitoring, maintenance, and retrospective utilities are absent from the registry, so orchestrators cannot discover them during later phases despite being essential for readiness.【e51091†L1-L20】【b5f2c8†L134-L193】

## Optimization Recommendations
1. **Build evidence & gate families:** Implement `aggregate_evidence_*`, `run_protocol_*_gates.py`, and `validate_gate_*` scripts across all phases, following the data contract implied by the protocols (artifact paths, pass thresholds, halt conditions).【b5f2c8†L18-L193】
2. **Expand registry coverage:** Register all existing reusable automation (health checks, audits, deployment scripts, monitoring collectors) with metadata that maps them to protocols and outputs, aligning with Protocol 23’s governance expectations.【e51091†L1-L20】【b0f694†L24-L104】
3. **Consolidate governance tooling:** Refactor rule- and template-related utilities into a shared module with consistent CLI signatures to simplify Protocols 04–05 execution and reduce duplication.【0a9f31†L49-L106】【5b16d5†L185-L211】
4. **Instrument governance outputs:** Deliver the missing inventory, documentation audit, static analysis, and remediation backlog scripts so Protocol 23 can produce measurable governance evidence without manual spreadsheets.【b0f694†L24-L104】【b5f2c8†L150-L193】
5. **Add regression harnesses:** Create integration tests for new gate runners and evidence aggregators using `test_workflow_integration.sh` as a template to ensure sustainable maintenance once automation is restored.【0bf469†L1-L4】【b5f2c8†L18-L149】
