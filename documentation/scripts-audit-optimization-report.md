# SCRIPTS AUDIT & OPTIMIZATION REPORT

## Executive Summary
- **Total Scripts**: 93 tracked automation entries in `scripts/` (Python + shell).【c0e3a8†L1-L90】
- **Registered Scripts**: 13 listed in `script-registry.json` (~14% coverage).【16ea5c†L1-L27】【aa5a1b†L1-L2】
- **Unregistered Scripts**: 69 executables are not registered (~86%).【c0e3a8†L1-L90】【aa5a1b†L1-L2】
- **Scripts Referenced by Protocols**: 25 real script paths are invoked across Protocols 01-23.【ba6862†L1-L3】
- **Unused Scripts**: 68+ existing scripts never appear in any protocol (93 total − 25 referenced).【c0e3a8†L1-L90】【ba6862†L1-L3】
- **Redundant/Missing References**: Protocols cite 185 script paths, but 160 have no implementation, leaving most gates unenforced.【ebb352†L1-L4】

## Script Inventory

### Registered Scripts (from script-registry.json)
| Script | Purpose (Docstring) | Used By Protocols | Status |
|--------|----------------------|-------------------|--------|
| scripts/classify_domain.py | Domain Classification Script.【ab3f41†L1-L4】 | – | ⚠️ Unused – not referenced by protocols.【686ce3†L1-L25】 |
| scripts/generate_from_brief.py | Brief-driven project orchestration that generates separate frontend and backend projects.【ab3f41†L2-L5】 | 04 | ✅ Implemented and referenced.【686ce3†L8-L9】 |
| scripts/normalize_project_rules.py | Normalize frontmatter for project rules under `.cursor/rules/project-rules/**.mdc`.【ab3f41†L3-L5】 | 04, 05 | ✅ Implemented; recommend registry retention.【686ce3†L12-L15】 |
| scripts/validate_prd_gate.py | Validate PRD gate artifacts before proceeding with generation.【ab3f41†L4-L6】 | 06 | ✅ Referenced and functioning.【686ce3†L20-L23】 |
| scripts/generate_prd_assets.py | Generate PRD and architecture summaries from planning artifacts.【ab3f41†L5-L6】 | 06 | ✅ Used in planning.【686ce3†L9-L23】 |
| scripts/enrich_tasks.py | Enrich tasks.json with personas and acceptance criteria.【ab3f41†L6-L7】 | 08 | ✅ Active reference.【686ce3†L6-L18】 |
| scripts/lifecycle_tasks.py | Utility helpers for lifecycle planning tasks.【ab3f41†L6-L8】 | – | ⚠️ Unused – referenced nowhere.【686ce3†L1-L25】 |
| scripts/run_workflow.py | CLI entry point for executing the workflow automation pipeline.【ab3f41†L7-L8】 | – | ⚠️ Unused in protocols.【686ce3†L1-L25】 |
| scripts/update_task_state.py | Update a task's state by id in tasks.json with validation and log note.【ab3f41†L8-L9】 | 10 | ✅ Needed for task execution.【686ce3†L17-L19】 |
| scripts/quality_gates.py | Quality Gates for Unified Developer Workflow.【ab3f41†L9-L10】 | – | ⚠️ Unused; protocols call non-existent validators instead.【837049†L1-L154】 |
| scripts/collect_coverage.py | Collect Python coverage into coverage.xml using pytest-cov if available.【ab3f41†L9-L11】 | – | ⚠️ Unused; could backfill quality protocols.【686ce3†L1-L25】 |
| scripts/evidence_report.py | Generate a consolidated evidence report from a workflow run.【ab3f41†L10-L11】 | – | ⚠️ Unused; add to retrospectives.【686ce3†L1-L25】 |
| scripts/trigger_plan.py | Policy-driven project generator helper (no docstring, stack selector logic).【ab3f41†L11-L13】【46211b†L9-L120】 | – | ⚠️ Unused; candidate for backlog.【686ce3†L1-L25】 |

### Unregistered Scripts (69)
| Script | Purpose | Should Register? | Recommendation |
|--------|---------|------------------|----------------|
| scripts/analyze_jobpost.py | NLP job post extraction with readability, tech stack, budget parsing.【ed8175†L1-L72】 | Yes | Register under proposal generation; critical for Protocol 01 evidence. |
| scripts/tone_mapper.py | Sentiment and tone classifier for proposal alignment.【27e8d8†L1-L88】 | Yes | Register with Protocol 01 validation suite. |
| scripts/validate_proposal.py | Proposal structure & empathy validator with grammar checks.【764a9d†L1-L120】 | Yes | Register and reuse for quality gates. |
| scripts/check_hipaa.py | Lightweight HIPAA compliance scan referenced in Phase 0.【c0e3a8†L19-L90】 | Maybe | Keep optional; add configuration flag for regulated projects. |
| scripts/enforce_gates.py | Numeric gate enforcement for coverage/security/perf thresholds.【53031b†L1-L118】 | Yes | Register for Phase 4+ gating to replace placeholder validators. |
| scripts/doctor.py | Environment diagnostics for bootstrap/setup.【9552fd†L63-L123】 | Yes | Register for Protocols 04/09 to standardize readiness checks. |
| scripts/scaffold_phase_artifacts.py | Scaffolds evidence folders for environment setup.【c0e3a8†L43-L72】 | Yes | Register to satisfy Protocol 09 automation hooks. |
| scripts/install_and_test.sh | Runs install/test smoke for environment validation.【c0e3a8†L43-L72】 | Yes | Register with environment phase. |
| scripts/deploy_backend.sh | Production/staging deployment script cited implicitly.【c0e3a8†L43-L72】 | Yes | Register for Phases 14-15 and document usage. |
| scripts/rollback_backend.sh | Rollback command referenced indirectly.【c0e3a8†L43-L72】 | Yes | Register with deployment contingency protocols. |
| scripts/collect_perf.py | Performance metric collector for monitoring gates.【0105a1†L1-L79】 | Yes | Register in Phase 5 operations to replace missing validators. |
| scripts/discover_automation_candidates.py | Automation discovery for maintenance backlog.【c0e3a8†L71-L93】 | Yes | Register in Protocol 21 to support automation recommendations. |
| scripts/validate_tasks.py | Task validation referenced by planning protocols.【c0e3a8†L61-L80】 | Yes | Register for Protocol 08 gating. |
| scripts/validate_workflow_integration.py | Workflow validation referenced by architecture protocol.【c0e3a8†L61-L90】 | Yes | Register for Protocol 07 integration checks. |
| scripts/validate_workflows.py | Global workflow validator used in bootstrap.【9552fd†L117-L180】 | Yes | Register to replace placeholder run scripts. |
| scripts/evidence_manager.py | Evidence manifest initializer required in Protocol 04.【9552fd†L109-L176】 | Yes | Register to enforce evidence tracking. |
| scripts/collect_change_context.py | Change context gatherer for audits.【837049†L55-L88】 | Evaluate | Add after verifying implementation quality. |
| scripts/validate_workflow_completeness.py | Global workflow completeness checker for governance.【c0e3a8†L71-L93】 | Yes | Register under Protocol 23. |
| scripts/workflow_automation.py | Automation orchestrator candidate for governance.【c0e3a8†L71-L93】 | Maybe | Evaluate overlap with run_workflow.py before registering. |
| scripts/aggregate_coverage.py | Coverage aggregator referenced in integration guide.【0a2433†L124-L138】 | Maybe | Document as support utility; register once quality protocols consume it. |

## Protocol-Script Mapping Matrix
| Protocol | Current Script(s) | Optimal Script(s) | Action Required |
|----------|-------------------|-------------------|-----------------|
| 01-client-proposal | References 11 scripts; only 5 exist (`analyze_jobpost`, `tone_mapper`, `validate_proposal`, `check_hipaa`, `enforce_gates`).【21e851†L18-L168】【686ce3†L1-L7】 | Register existing 5, author lightweight `validate_proposal_structure.py` or remove gate.【764a9d†L1-L120】 | Replace missing validators, add manual fallback guidance. |
| 02-client-discovery | All referenced validators (`validate_prerequisites_00B.py`, etc.) missing.【03e7a7†L211-L235】【837049†L7-L28】 | Reuse `validate_tasks.py`, `validate_workflows.py`, or document manual review checklists. | Build/replace automation before enforcing gates. |
| 03-project-brief | Validator suite entirely absent (`validate_brief_structure.py`, etc.).【837049†L13-L32】 | Align with existing `analyze_brief.py` and `validate_brief.py` outputs.【c0e3a8†L7-L34】 | Refactor gates to use real scripts. |
| 04-bootstrap-context | Uses real scripts (`doctor.py`, `generate_from_brief.py`, `normalize_project_rules.py`, etc.) but missing aggregator references.【9552fd†L35-L180】【686ce3†L8-L18】 | Register used scripts; replace phantom `aggregate_evidence_00.py`. | Update automation list and registry. |
| 05-bootstrap-project | Depends on non-existent validators (`validate_principles.py`, `validate_rule_metadata.py`).【837049†L25-L40】 | Leverage `rules_audit_quick.py` & `normalize_project_rules.py` instead.【c0e3a8†L33-L61】 | Rewrite gate instructions. |
| 06-create-prd | Mix of real (`generate_prd_assets.py`, `validate_prd_gate.py`) and missing validators (`validate_prd_context.py`).【b14faa†L105-L160】【837049†L33-L48】 | Register existing scripts and scope new validator backlog. | Document manual review until new scripts exist. |
| 07-technical-design | Calls `plan_from_brief.py`, `validate_workflow_integration.py` (real) plus missing `validate_design_handoff.py`.【686ce3†L12-L24】【837049†L41-L60】 | Add doc for `plan_from_brief.py`, draft design handoff checklist. | Replace missing automation with manual steps. |
| 08-generate-tasks | Uses `enrich_tasks.py`, `validate_tasks.py` but references missing decomposition validators.【837049†L45-L60】 | Register available scripts; backlog `validate_task_decomposition.py`. | Update gates to reference existing tooling. |
| 09-environment-setup | Real scripts exist (`doctor.py`, `install_and_test.sh`, etc.) but `package_environment_assets.py` missing.【837049†L57-L72】【686ce3†L10-L18】 | Write packaging helper or remove requirement. | Align automation list to actual scripts. |
| 10-process-tasks | Only `update_task_state.py` exists; other validators absent.【d57058†L35-L154】【837049†L60-L84】 | Register `update_task_state.py`, reuse `quality_gates.py` for audits. | Create manual QA checklist pending automation. |
| 11-integration-testing | All automation references missing (contract tests, manifest generator).【837049†L60-L88】 | Hook into `validate_workflow_integration.py` or stack-specific test runners. | Define new script backlog before enforcing gates. |
| 12-quality-audit | Validator list entirely missing implementations.【837049†L60-L92】 | Employ `quality_gates.py`, `collect_coverage.py`, `enforce_gates.py`. | Consolidate audit tooling. |
| 13-uat-coordination | Deploy/rollback placeholders unresolved.【837049†L73-L100】 | Map to `deploy_backend.sh`, create UAT checklist script. | Replace placeholder names. |
| 14-pre-deployment-staging | Similar placeholder usage and missing validators.【837049†L73-L110】 | Align with actual deployment scripts, add manual rehearsal steps. | Update gating instructions. |
| 15-production-deployment | References `scripts/deploy_*` wildcard and nonexistent validators; only `deploy_backend.sh` exists.【76a5dd†L11-L191】【686ce3†L3-L16】 | Register actual deploy/rollback scripts, create coverage for front-end if needed. | Correct automation list and gating thresholds. |
| 16-monitoring-observability | Only `collect_perf.py` exists; other validators missing.【0105a1†L1-L79】【837049†L111-L133】 | Register `collect_perf.py`, reuse `enforce_gates.py` for SLO enforcement. | Implement monitoring scripts backlog. |
| 17-incident-response | All validators missing.【837049†L111-L133】 | Provide manual incident playbooks; plan automation later. | Delay gating enforcement until scripts exist. |
| 18-performance-optimization | Validators absent; only generic gates referenced.【837049†L111-L140】 | Use `collect_perf.py` + analytics scripts once built. | Document manual measurement. |
| 19-documentation-knowledge-transfer | Mix of real (`check_doc_style.py` missing) and placeholder exports.【837049†L140-L154】 | Add doc-style linter or adjust instructions. | Register once tooling exists. |
| 20-project-closure | Validators missing for deliverables/governance gates.【837049†L140-L154】 | Use spreadsheets/manual checklists until automation exists. | Backlog automation. |
| 21-maintenance-support | Relies on nonexistent governance validators; only `discover_automation_candidates.py` exists.【837049†L140-L154】【c0e3a8†L71-L93】 | Register automation discovery script, create backlog integrity checker. | Adjust gating to manual review. |
| 22-retrospective | Calls missing retrospective validators; `trigger_plan.py` could serve improvement planning.【837049†L140-L154】【46211b†L9-L120】 | Map to `trigger_plan.py`, add manual facilitation script. | Replace placeholders. |
| 23-script-governance | References JSON/CSV “scripts” rather than executables.【837049†L121-L154】 | Point to `validate_workflow_completeness.py`, `workflow_automation.py`, or new governance tools. | Rewrite automation section entirely. |

## Script Optimization Recommendations

### 1. Script Replacements
- **Protocol 12 Quality Audit**: Replace nonexistent `run_comprehensive_review.py` with `scripts/quality_gates.py` + `scripts/enforce_gates.py` to enforce measurable coverage and dependency thresholds.【53031b†L1-L118】【837049†L60-L92】
- **Protocol 15 Deployment**: Substitute wildcard `scripts/deploy_*` references with `scripts/deploy_backend.sh` and add guidance for front-end deployments until equivalent scripts exist.【76a5dd†L18-L191】【c0e3a8†L43-L72】

### 2. Script Consolidations
- **Evidence Aggregators**: The `aggregate_evidence_*.py` placeholders repeat across phases.【837049†L1-L128】 Combine them into a single `scripts/evidence_manager.py` workflow already available and update protocols accordingly.【9552fd†L109-L176】
- **Validation Suites**: Collapse missing `validate_gate_*` scripts into parameterized invocations of `scripts/enforce_gates.py` and `scripts/quality_gates.py` until bespoke checks are authored.【53031b†L1-L118】【ab3f41†L9-L10】

### 3. New Scripts Needed
- **Protocol 02 Discovery Validator**: Implement `scripts/validate_discovery_scope.py` or revise protocol to reuse `scripts/validate_tasks.py`. Priority: High (blocks early lifecycle gates).【03e7a7†L213-L222】【837049†L7-L28】
- **Protocol 11 Integration Tests**: Create stack-aware runners (e.g., `scripts/run_contract_tests.py`) to replace missing automation. Priority: High for release readiness.【837049†L60-L88】
- **Protocol 23 Governance Audit**: Build `scripts/validate_script_inventory.py` to analyze registry coverage vs filesystem. Priority: Medium for long-term governance.【837049†L121-L154】

### 4. Scripts to Deprecate
- **Placeholder Aggregators**: `aggregate_evidence_*.py` references have no implementation; remove from protocols until created.【837049†L1-L128】
- **JSON/CSV “scripts”**: Entries like `scripts/script-index.json` are mislabeled artifacts; protocols should reference them as outputs rather than automation commands.【837049†L121-L154】

## Script Registry Update Recommendations

### Scripts to Add to Registry
```json
{
  "proposal": {
    "jobpost-analysis": "scripts/analyze_jobpost.py",
    "tone-mapping": "scripts/tone_mapper.py",
    "proposal-validation": "scripts/validate_proposal.py"
  },
  "bootstrap": {
    "environment-doctor": "scripts/doctor.py",
    "evidence-manager": "scripts/evidence_manager.py"
  },
  "planning": {
    "task-validation": "scripts/validate_tasks.py",
    "workflow-integration": "scripts/validate_workflow_integration.py"
  },
  "deployment": {
    "deploy-backend": "scripts/deploy_backend.sh",
    "rollback-backend": "scripts/rollback_backend.sh"
  },
  "operations": {
    "collect-performance": "scripts/collect_perf.py",
    "enforce-gates": "scripts/enforce_gates.py"
  }
}
```

### Scripts to Remove/Deprecate
- Placeholder `aggregate_evidence_*` references – no backing files.【837049†L1-L128】
- `scripts/script-categories.json` / `scripts/script-index.json` entries – classify as artifacts, not executables.【837049†L121-L154】

## Priority Actions
1. **Critical script fix**: Register proposal automation (`analyze_jobpost.py`, `tone_mapper.py`, `validate_proposal.py`) so Protocol 01 gates can run end-to-end.【ed8175†L1-L72】【27e8d8†L1-L88】【764a9d†L1-L120】
2. **Critical script fix**: Align deployment protocols with actual shell scripts and document missing front-end counterparts.【76a5dd†L18-L191】【c0e3a8†L43-L72】
3. **Registry update**: Expand `script-registry.json` to cover high-usage planning, execution, and operations scripts listed above.【16ea5c†L1-L27】【686ce3†L1-L25】
4. **Optimization**: Replace nonexistent gate validators with consolidated tooling from `scripts/enforce_gates.py` and `scripts/quality_gates.py`, adding manual fallbacks where automation is absent.【53031b†L1-L118】【ab3f41†L9-L10】
