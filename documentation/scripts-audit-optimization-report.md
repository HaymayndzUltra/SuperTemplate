# SCRIPTS AUDIT & OPTIMIZATION REPORT

## Executive Summary
- **Total Scripts**: 96 repository scripts were inventoried at `/scripts` (Python + shell).【48495c†L1-L96】
- **Registered Scripts**: 18 entries are defined in `script-registry.json`, covering bootstrap, PRD, task generation, execution, quality, and retrospective categories.【F:scripts/script-registry.json†L1-L20】
- **Unregistered Scripts**: 64 scripts exist without registry entries, including automation orchestrators (`ai_executor.py`, `workflow_automation.py`) and governance utilities (`validate_workflow_integration.py`, `validate_protocols.py`).【397fb9†L1-L23】
- **Scripts Referenced by Protocols**: Protocols 01-23 call 197 unique script paths, but 166 of them are missing from the repository, so most gate automation is currently non-functional.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L125-L207】【397fb9†L1-L22】
- **Unused Scripts**: 65 stored scripts are never referenced by protocols 01-23 (e.g., `ai_executor.py`, `compare_pull_requests.py`, `detect_instruction_conflicts.py`).【397fb9†L1-L23】
- **Redundant Scripts**: Numerous gate helpers share identical prefixes (`aggregate_evidence_*.py`, `validate_prerequisites_*.py`) but none exist; these should be consolidated into reusable utilities rather than bespoke per-protocol files.【397fb9†L1-L22】

## Script Inventory

### Registered Scripts (from script-registry.json)
| Script | Purpose | Used By Protocols | Status |
|--------|---------|-------------------|--------|
| classify_domain.py | Stack / domain detection | Not referenced in protocols 01-23 | ⚠️ Defined but unused【F:scripts/script-registry.json†L2-L6】【5b28d3†L1-L1】 |
| generate_from_brief.py | Bootstrap scaffold generation | Protocol 04 | ✅ Appropriate【F:scripts/script-registry.json†L3-L8】【fe08e7†L1-L5】 |
| normalize_project_rules.py | Normalize rule packs | Protocols 04 & 05 | ✅ Appropriate【F:scripts/script-registry.json†L3-L8】【F:.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md†L73-L118】 |
| generate_prd_assets.py | Produce PRD appendices | Protocol 06 | ✅ Optimal【F:scripts/script-registry.json†L8-L12】【F:.cursor/ai-driven-workflow/06-create-prd.md†L101-L113】 |
| validate_prd_gate.py | Validate PRD completeness | Protocol 06 | ✅ Optimal【F:scripts/script-registry.json†L8-L12】【F:.cursor/ai-driven-workflow/06-create-prd.md†L112-L160】 |
| enrich_tasks.py | Add metadata to task files | Protocol 08 | ✅ Optimal【F:scripts/script-registry.json†L12-L16】【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L148-L207】 |
| lifecycle_tasks.py | Map tasks to lifecycle | Not referenced | ⚠️ Defined but unused【F:scripts/script-registry.json†L12-L16】【c9c470†L1-L1】 |
| run_workflow.py | Workflow runner | Not referenced in protocols 01-23 (documentation only) | ⚠️ Defined but unused【F:scripts/script-registry.json†L16-L20】【50232c†L1-L9】 |
| update_task_state.py | Task tracker updates | Protocol 10 | ✅ Optimal【F:scripts/script-registry.json†L16-L20】【F:.cursor/ai-driven-workflow/10-process-tasks.md†L82-L153】 |
| quality_gates.py | Quality audit aggregator | Not referenced | ⚠️ Candidate for QA automation replacement【F:scripts/script-registry.json†L16-L20】【50232c†L1-L9】 |
| collect_coverage.py | Coverage collection | Referenced only in documentation | ⚠️ Needs integration or removal【F:scripts/script-registry.json†L16-L20】【50232c†L1-L9】 |
| evidence_report.py | Evidence synthesis | Not referenced in protocols 01-23 | ⚠️ Underused asset【F:scripts/script-registry.json†L20-L23】【50232c†L1-L9】 |
| trigger_plan.py | Improvement plan trigger | Not referenced in protocols 01-23 | ⚠️ Underused asset【F:scripts/script-registry.json†L20-L23】【50232c†L1-L9】 |

### Unregistered Scripts (sample of 64+)
| Script | Purpose | Should Register? | Recommendation |
|--------|---------|------------------|----------------|
| ai_executor.py | Generic automation harness | Yes | Register under execution to replace missing `aggregate_evidence_*` family.【397fb9†L10-L23】 |
| analyze_project_rules.py | Rule analysis | Yes | Map to Protocol 05 governance checks for reuse.【48495c†L1-L40】 |
| compare_pull_requests.py | PR comparison | No | Document as tooling utility; keep outside protocol automation.【48495c†L1-L40】 |
| detect_instruction_conflicts.py | Rule conflict detection | Yes | Integrate with discovery/bootstrap to flag contradictory client inputs.【48495c†L1-L44】 |
| evidence_manager.py | Evidence repo manager | Yes | Register for protocols with heavy artifact packaging (12, 15, 20).【48495c†L1-L48】 |
| validate_workflow_integration.py | Workflow validation | Yes | Already used in Protocol 07; add to registry and QA toolkit.【F:.cursor/ai-driven-workflow/07-technical-design-architecture.md†L81-L145】 |
| validate_protocols.py | Protocol linting | No | Keep as meta-tool; document in governance playbook.【48495c†L1-L92】 |
| workflow_automation.py | Task automation orchestration | Yes | Candidate to consolidate missing gate validators.【48495c†L1-L96】 |

## Protocol-Script Mapping Matrix
| Protocol | Current Script(s) | Optimal Script(s) | Action Required |
|----------|-------------------|-------------------|-----------------|
| 01-client-proposal-generation | analyze_jobpost.py, tone_mapper.py, validate_proposal.py, check_hipaa.py, enforce_gates.py, validate_compliance_assets.py | Keep analyze/tone/proposal validators; swap HIPAA/compliance scripts for risk-tiered checklist | Replace compliance suite with conditional script or manual checklist.【F:.cursor/ai-driven-workflow/01-client-proposal-generation.md†L139-L160】 |
| 04-project-bootstrap-and-context-engineering | validate_brief.py, generate_from_brief.py, normalize_project_rules.py, rules_audit_quick.py, validate_scaffold.py, validate_workflows.py | Keep validate_brief / generate_from_brief / normalize rules; add evidence_manager.py for artifact tracking | Add `evidence_manager.py` to manage bootstrap artifacts and retire missing `validate_scaffold.py` placeholder.【F:.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md†L40-L118】【397fb9†L1-L22】 |
| 06-create-prd | generate_prd_assets.py, validate_prd_gate.py, validate_prd_context.py, validate_prd_requirements.py | Keep existing PRD scripts; add analyze_project_rules.py for governance traceability | Register existing validators and add `analyze_project_rules.py` to auto-link governance constraints.【F:.cursor/ai-driven-workflow/06-create-prd.md†L101-L160】【48495c†L1-L40】 |
| 08-generate-tasks | validate_rule_index.py*, validate_high_level_tasks.py*, validate_task_decomposition.py*, validate_tasks.py, enrich_tasks.py | Replace missing validators with validate_tasks.py + ai_executor.py orchestrations | Build composite `task_plan_validator.py` using existing scripts; remove nonexistent file references.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L125-L207】【397fb9†L1-L22】 |
| 10-process-tasks | validate_preflight.py*, validate_subtask_compliance.py*, validate_quality_gate.py*, validate_session_closeout.py*, update_task_state.py | Use ai_executor.py to orchestrate available linters/tests; keep update_task_state.py | Implement shared execution gate script and delete phantom validators, or build them atop ai_executor.py.【F:.cursor/ai-driven-workflow/10-process-tasks.md†L125-L153】【397fb9†L1-L22】 |
| 15-production-deployment | validate_gate_11_*.py*, validate_gate_11_launch.py*, validate_gate_11_reporting.py*, deploy_backend.sh | Introduce deploy orchestration via workflow_automation.py + existing shell scripts | Author `deployment_gate.py` leveraging real shell scripts; remove missing gate references.【F:.cursor/ai-driven-workflow/15-production-deployment.md†L165-L191】【48495c†L1-L96】 |

`*` indicates scripts referenced in the protocol but absent from `/scripts`.

## Script Optimization Recommendations

### 1. Script Replacements
- **Protocol 01**: Replace `check_hipaa.py`/`enforce_gates.py` combo with a configurable compliance checklist script that activates only when risk flags exist. This restores realism for general-purpose proposals while still supporting regulated engagements.【F:.cursor/ai-driven-workflow/01-client-proposal-generation.md†L139-L160】
- **Protocol 08**: Replace the nonexistent `validate_rule_index.py`, `validate_high_level_tasks.py`, and `validate_task_decomposition.py` with a single `task_plan_validator.py` that wraps `validate_tasks.py`, `enrich_tasks.py`, and manual governance checks. Reduces maintenance overhead and removes broken references.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L125-L207】【397fb9†L1-L22】

### 2. Script Consolidations
- Merge the missing `aggregate_evidence_*.py` family into `evidence_manager.py` plus per-phase configuration files. This eliminates dozens of phantom scripts while delivering the same packaging capability.【397fb9†L1-L22】【48495c†L1-L48】
- Combine `validate_prerequisites_*.py` placeholders into a reusable `prerequisite_checker.py` that reads YAML manifests for each protocol, enabling maintainable validation without bespoke files.【397fb9†L1-L22】

### 3. New Scripts Needed
- **Protocol 08**: `task_plan_validator.py` – orchestrates existing task validation and enrichment to enforce gating without nonexistent files. **Priority**: High.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L125-L207】
- **Protocol 10**: `execution_gate_runner.py` – runs lint/tests, captures logs, and updates manifests to replace missing gate validators. **Priority**: High.【F:.cursor/ai-driven-workflow/10-process-tasks.md†L125-L153】
- **Protocol 15**: `deployment_gate.py` – wraps deployment smoke tests, approvals, and rollback verification using the real shell scripts. **Priority**: High.【F:.cursor/ai-driven-workflow/15-production-deployment.md†L165-L191】
- **Protocol 20**: `closure_package_builder.py` – assembles documentation, approvals, and SLA evidence to replace phantom aggregate scripts. **Priority**: Medium.【F:.cursor/ai-driven-workflow/20-project-closure.md†L45-L155】

### 4. Scripts to Deprecate
- Remove references to every `aggregate_evidence_*.py` and `validate_prerequisites_*.py` placeholder until real implementations exist; the current references create false assurance and block automation pipelines.【397fb9†L1-L22】
- Deprecate unused registry entries (`classify_domain.py`, `lifecycle_tasks.py`, `run_workflow.py`, `collect_coverage.py`, `quality_gates.py`) or map them to concrete protocol steps so the registry reflects actual automation coverage.【F:scripts/script-registry.json†L2-L20】【5b28d3†L1-L1】【c9c470†L1-L1】【50232c†L1-L9】

## Script Registry Update Recommendations

### Scripts to Add to Registry
```json
{
  "execution": {
    "evidence-manager": "scripts/evidence_manager.py",
    "ai-executor": "scripts/ai_executor.py"
  },
  "quality": {
    "workflow-integration": "scripts/validate_workflow_integration.py",
    "protocol-lint": "scripts/validate_protocols.py"
  },
  "deployment": {
    "deployment-gate": "scripts/deployment_gate.py"
  }
}
```

### Scripts to Remove/Deprecate
- classify_domain.py: unused by protocols 01-23; relocate to discovery toolkit or remove from registry.【F:scripts/script-registry.json†L2-L6】【5b28d3†L1-L1】
- lifecycle_tasks.py: no references; replace with documented task estimation guidance before reenabling.【F:scripts/script-registry.json†L12-L16】【c9c470†L1-L1】
- run_workflow.py: referenced only in documentation; keep as optional utility outside mandatory registry to avoid misleading coverage.【F:scripts/script-registry.json†L16-L20】【50232c†L1-L9】

## Priority Actions
1. **Critical script fix**: Build consolidated gate validators (`task_plan_validator.py`, `execution_gate_runner.py`, `deployment_gate.py`) and update protocols to reference them instead of missing files.【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L125-L207】【F:.cursor/ai-driven-workflow/15-production-deployment.md†L165-L191】
2. **Critical script fix**: Implement `evidence_manager.py`-driven packaging to replace the phantom `aggregate_evidence_*` suite and ensure every phase can archive outputs consistently.【F:.cursor/ai-driven-workflow/04-project-bootstrap-and-context-engineering.md†L112-L118】【397fb9†L1-L22】
3. **Registry update**: Expand `script-registry.json` to include actual automation assets (ai_executor, evidence_manager, validate_workflow_integration) and drop unused entries, so the registry mirrors reality.【F:scripts/script-registry.json†L1-L20】【50232c†L1-L9】
4. **Optimization**: Document fallback manual procedures within protocols whenever referenced scripts are optional, preventing workflow dead-ends when automation is unavailable.【F:.cursor/ai-driven-workflow/13-uat-coordination.md†L160-L187】【F:.cursor/ai-driven-workflow/20-project-closure.md†L45-L135】
