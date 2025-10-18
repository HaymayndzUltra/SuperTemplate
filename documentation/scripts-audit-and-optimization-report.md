# SCRIPTS AUDIT & OPTIMIZATION REPORT

## Executive Summary
- **Total Scripts**: 93 tracked automation assets under `/scripts` (Python + shell).【e7ac5b†L13-L94】
- **Registered Scripts**: 13 entries in `script-registry.json` (14% coverage).【680c67†L1-L13】
- **Unregistered Scripts**: 80 scripts lack registry entries and therefore governance mapping.【e7ac5b†L13-L94】【680c67†L1-L13】
- **Scripts Referenced by Protocols**: 197 unique script calls appear across Protocols 01-23, but only 31 exist in the repository; 166 references point to missing automation.【0b9c19†L1-L120】【5e5d4f†L18-L31】
- **Unused Scripts**: 62 repository scripts are never referenced by Protocols 01-23, highlighting misalignment between automation supply and protocol demand.【0b9c19†L1-L120】
- **Redundant Signals**: Multiple theoretical gate runners (`run_protocol_*.py`) appear in protocols but are absent in the codebase, while existing orchestrators (`ai_orchestrator.py`, `run_workflow.py`) are unreferenced, suggesting consolidation opportunities.【0b9c19†L1-L120】【8e174a†L13-L161】

## Script Inventory

### Registered Scripts (from script-registry.json)
| Script | Purpose | Used By Protocols | Status |
|--------|---------|-------------------|--------|
| `scripts/classify_domain.py` | Classifies project domain from job posts to guide stack selection.【a2a2a0†L1-L17】 | Referenced in Protocol 05 via integration guide, but absent from 01-23 flows; available for reuse. | Needs mapping to active protocols |
| `scripts/generate_from_brief.py` | Bootstraps repository assets from the project brief scaffold.【8e174a†L37-L95】 | Protocol 04 bootstrap. | ✅ Aligned |
| `scripts/normalize_project_rules.py` | Standardizes `.cursor/rules` artifacts before audits.【8e174a†L69-L97】 | Protocols 04-05. | ✅ Aligned |
| `scripts/validate_prd_gate.py` | Validates PRD structure and front matter prior to approval.【e1dda3†L105-L160】【893f6e†L1-L32】 | Protocol 06. | ✅ Aligned |
| `scripts/generate_prd_assets.py` | Generates derivative PRD artifacts (stories, schemas).【e1dda3†L105-L117】 | Protocol 06. | ✅ Aligned |
| `scripts/enrich_tasks.py` | Enhances generated tasks with metadata for execution.【8e174a†L81-L101】 | Protocol 08. | ✅ Aligned |
| `scripts/lifecycle_tasks.py` | Maps tasks across lifecycle (listed but not referenced in protocols).【680c67†L1-L13】 | Not referenced in Protocols 01-23. | ⚠️ Registry only |
| `scripts/run_workflow.py` | Generic workflow runner for orchestration.【5e5d4f†L23-L31】 | Referenced in supporting docs only. | ⚠️ Registry only |
| `scripts/update_task_state.py` | Syncs task tracker state after execution.【adcbb0†L83-L146】 | Protocol 10. | ✅ Aligned |
| `scripts/quality_gates.py` | Comprehensive audit runner (registered but unused in protocols).【680c67†L1-L13】 | Unreferenced. | ⚠️ Registry only |
| `scripts/collect_coverage.py` | Aggregates pytest coverage to XML for quality gates.【d3d247†L48-L54】【014a00†L1-L32】 | Protocol 12 prerequisites (indirect). | ✅ Partial |
| `scripts/evidence_report.py` | Builds retrospective evidence packages (registered but not invoked).【680c67†L1-L13】 | Planned for Protocol 22 but missing reference. | ⚠️ Registry only |
| `scripts/trigger_plan.py` | Generates improvement plan from retrospectives (registered but unreferenced).【680c67†L1-L13】 | Intended for Protocol 22. | ⚠️ Registry only |

### Unregistered Scripts (80)
| Script | Purpose Snapshot | Should Register? | Recommendation |
|--------|------------------|------------------|----------------|
| `scripts/analyze_jobpost.py` | Parses job posts for objectives, tech stack, readability, and risk cues.【2d0f28†L1-L34】 | Yes | Link to Protocol 01 gate; share outputs with tone mapping. |
| `scripts/tone_mapper.py` | Performs sentiment and tone classification on job post analysis results.【41a9c0†L1-L29】 | Yes | Register under proposal/communication to enforce tone gates. |
| `scripts/doctor.py` | Validates environment readiness (used in bootstrap).【8e174a†L37-L95】 | Yes | Map to Protocols 04 and 09 prerequisites. |
| `scripts/install_and_test.sh` | Provisions dependencies and runs smoke tests for env setup.【8e174a†L93-L125】 | Yes | Register for Protocol 09 environment validation. |
| `scripts/scaffold_phase_artifacts.py` | Produces environment manifests for setup.【8e174a†L93-L125】 | Yes | Register for Protocol 09 artifact generation. |
| `scripts/validate_workflows.py` | Validates workflow files for bootstrap readiness.【8e174a†L93-L125】 | Yes | Register as bootstrap gate. |
| `scripts/validate_workflow_integration.py` | Checks design artifacts for integration consistency.【8e174a†L65-L109】 | Yes | Register for Protocol 07 gating. |
| `scripts/validate_tasks.py` | Validates generated tasks for structure and coverage.【8e174a†L81-L109】 | Yes | Register to support Protocol 08 gates. |
| `scripts/test_workflow_integration.sh` | Executes integration smoke tests (currently unreferenced).【5e5d4f†L23-L31】 | Yes | Use as interim deployment validator for Phase 5. |
| `scripts/deploy_backend.sh` | Executes backend deployment flows for production rollouts.【8e174a†L141-L167】 | Yes | Register for Protocol 15 automation. |
| `scripts/collect_perf.py` | Captures performance metrics for monitoring baselines.【8e174a†L139-L167】 | Yes | Register for Protocol 16 instrumentation. |
| `scripts/evidence_manager.py` | Initializes evidence directories during bootstrap.【8e174a†L93-L115】 | Optional | Document as support utility; register if gating requires. |
| `scripts/ai_executor.py` & `scripts/ai_orchestrator.py` | Legacy workflow runners not referenced in protocols.【0b9c19†L1-L120】 | No (pending) | Evaluate consolidation with `run_workflow.py` before registering. |
| `scripts/backup_workflows.py` | Archives workflow files; unused by protocols.【0b9c19†L1-L120】 | Optional | Consider on-demand utility registration post-use case. |
| `scripts/validate_protocols.py` | Validates protocol structures globally.【8e174a†L133-L161】 | Yes | Register under governance (Protocol 23). |

> _Note_: Remaining unregistered scripts (see Appendix A) should be categorized during governance cleanup; most fall into orchestration, validation, or reporting utilities listed in `0b9c19`.

## Protocol-Script Mapping Matrix
| Protocol | Current Script References | Optimal Script(s) | Action Required |
|----------|--------------------------|-------------------|-----------------|
| 01-client-proposal-generation | `analyze_jobpost.py`, `tone_mapper.py`, `validate_proposal.py`, missing `validate_proposal_structure.py`.【667b41†L139-L155】【8e174a†L21-L41】 | Reuse existing trio; replace missing structure gate with enhanced `validate_proposal.py` or new lightweight checker. | Build/assign structure validator; register scripts. |
| 02-client-discovery-initiation | References `validate_discovery_*` scripts that do not exist.【4c337f†L136-L165】【8e174a†L43-L63】 | Adapt `validate_brief.py` for artifact presence; create checklist-based Python validator. | Develop new script set; update protocol references. |
| 03-project-brief-creation | Calls `validate_discovery_inputs.py`, `validate_brief_structure.py`, `verify_brief_approvals.py` (missing).【65f22c†L88-L149】【8e174a†L55-L65】 | Extend `validate_brief.py` with structure mode; build approval log validator. | Refactor gating to available automation; schedule new scripts. |
| 06-create-prd | Uses `generate_prd_assets.py`, `validate_prd_gate.py` (present) plus missing context/requirements validators.【e1dda3†L105-L160】【8e174a†L65-L83】 | Keep existing pair; create YAML-based context checker reused from PRD gate. | Implement new script; update registry. |
| 07-technical-design-architecture | Depends on missing `validate_design_handoff.py` and aggregated evidence scripts.【8e174a†L73-L109】 | Register `validate_workflow_integration.py`; add design handoff validator leveraging `plan_from_brief.py` outputs. | Author new validator; adjust protocol references. |
| 08-generate-tasks | Only `enrich_tasks.py` and `validate_tasks.py` exist; other validators missing.【8e174a†L81-L101】 | Formalize `validate_tasks.py` as gate and add coverage checks referencing `validate_prd_gate.py` outputs. | Register and integrate; build additional scripts if needed. |
| 09-environment-setup-validation | Calls `doctor.py`, `install_and_test.sh`, `scaffold_phase_artifacts.py` (exist) plus missing packaging validators.【8e174a†L93-L125】 | Register existing trio; add manifest validator using `evidence_manager.py`. | Register; develop packaging validator. |
| 10-process-tasks | Only `update_task_state.py` exists; all compliance validators missing.【adcbb0†L83-L153】【8e174a†L107-L133】 | Introduce markdown diff checker and reuse `validate_tasks.py` for subtask compliance. | Create validators; adjust artifact paths. |
| 11-integration-testing | References contract/environment validators not present.【9f8dc6†L11-L152】 | Build wrappers around `pytest` and `run_workflow.py`; create manifest generator script. | Develop new automation; sync prerequisites. |
| 12-quality-audit | Depends on router and reporting scripts absent from repo.【d3d247†L62-L183】【8e174a†L133-L161】 | Reuse `collect_coverage.py`, add CLI wrappers for CI/log aggregation, and introduce router manifest generator. | Implement missing tooling; trim unrealistic gates. |
| 15-production-deployment | Only `deploy_backend.sh` exists; validators missing.【8e174a†L141-L167】 | Pair `deploy_backend.sh` with `test_workflow_integration.sh` as release smoke; add YAML-based readiness checker. | Develop readiness scripts; register deployment assets. |
| 23-script-governance-protocol | Lists inventory/validation scripts absent from repo.【8e174a†L155-L167】 | Promote `validate_protocols.py` and create actual inventory scanners. | Prioritize governance automation build-out. |

## Script Optimization Recommendations

### 1. Script Replacements
- **Protocol 01**: Replace the fictional `validate_proposal_structure.py` with an enhanced mode inside `scripts/validate_proposal.py` that checks for mandatory sections and empathy tokens, leveraging existing validation logic.【667b41†L139-L155】【5e5d4f†L19-L31】
- **Protocol 09**: Substitute missing packaging validators with a new manifest check powered by `scripts/evidence_manager.py` to confirm evidence directory integrity.【8e174a†L93-L125】

### 2. Script Consolidations
- Merge orchestration utilities (`scripts/ai_executor.py`, `scripts/ai_orchestrator.py`, `scripts/run_workflow.py`) into a single maintained runner registered for Protocol 10 onwards, eliminating dead code paths.【0b9c19†L1-L120】【5e5d4f†L19-L31】
- Combine retrospective tooling (`scripts/evidence_report.py`, `scripts/retrospective_evidence_report.py`) into one pipeline feeding Protocol 22, reducing duplication.【0b9c19†L1-L120】

### 3. New Scripts Needed
- **Protocol 02**: `scripts/validate_discovery_artifacts.py` – verifies presence and approvals for discovery forms; priority **High** because current gates are non-functional.【4c337f†L136-L165】
- **Protocol 10**: `scripts/validate_subtask_evidence.py` – ensures subtask artifacts exist without manual review; priority **Medium**.【adcbb0†L56-L140】
- **Protocol 15**: `scripts/validate_release_readiness.py` – checks deployment checklist YAML for approvals and rollback paths; priority **High**.【15-production-deployment.md†L25-L191】

### 4. Scripts to Deprecate
- **`scripts/run_generate_rules.py`**: No protocol references; functionality overlaps with `generate_from_brief.py` scaffolding. Deprecate after confirming no external consumers.【0b9c19†L1-L120】
- **`scripts/router_benchmark.py`**: Not referenced and tangential to current lifecycle; recommend removal or archival until router tooling is implemented.【0b9c19†L1-L120】

## Script Registry Update Recommendations

### Scripts to Add to Registry
```json
{
  "proposal": {
    "jobpost-analysis": "scripts/analyze_jobpost.py",
    "tone-mapping": "scripts/tone_mapper.py"
  },
  "bootstrap": {
    "environment-diagnostics": "scripts/doctor.py",
    "workflow-validation": "scripts/validate_workflows.py"
  },
  "planning": {
    "task-validation": "scripts/validate_tasks.py"
  },
  "execution": {
    "task-state": "scripts/update_task_state.py"
  },
  "quality": {
    "coverage": "scripts/collect_coverage.py"
  },
  "deployment": {
    "backend-release": "scripts/deploy_backend.sh",
    "smoke-tests": "scripts/test_workflow_integration.sh"
  }
}
```

### Scripts to Remove/Deprecate
- `scripts/run_generate_rules.py`: superseded by scaffold utilities; no protocol references.【0b9c19†L1-L120】
- `scripts/router_benchmark.py`: benchmarking tool without workflow integration; archive until router is implemented.【0b9c19†L1-L120】

## Priority Actions
1. **Critical script fix 1**: Implement discovery validation scripts and update Protocol 02 references to unblock early-phase gates.【4c337f†L136-L165】【8e174a†L43-L63】
2. **Critical script fix 2**: Deliver minimum viable deployment validators (readiness + smoke) to stabilize Phase 5.【8e174a†L141-L167】【15-production-deployment.md†L25-L191】
3. **Registry update 1**: Register high-usage but currently unmanaged scripts (job post analysis, tone mapping, doctor, workflow validation).【8e174a†L23-L97】【2d0f28†L1-L34】
4. **Optimization 1**: Consolidate orchestration utilities into a single maintained runner and align protocols accordingly.【0b9c19†L1-L120】【5e5d4f†L19-L31】

## Appendix A – Additional Unregistered Scripts
See `0b9c19` for the full list of 62 scripts currently unused by Protocols 01-23; categorize them during the governance protocol overhaul to determine archival versus future integration.
