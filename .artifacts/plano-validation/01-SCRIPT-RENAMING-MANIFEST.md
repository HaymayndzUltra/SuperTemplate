# Complete Script Renaming Manifest

**Purpose**: Corrects all script numbering misalignments identified in plano.md  
**Scope**: 68 scripts across 18 protocols (06-23)  
**Status**: REQUIRED - Blocker for all other work

---

## Quick Reference

| Metric | Value |
|--------|-------|
| Total Scripts to Rename | 68 |
| Protocols Affected | 18 (06-23) |
| Correctly Named Protocols | 5 (01-05) |
| Script Categories | 5 types |

---

## Renaming by Protocol

### Protocol 06 → Create PRD
**Current State**: Uses Protocol 1 scripts  
**Scripts to Rename**: 2

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_1.py | validate_prerequisites_06.py | Prerequisite |
| aggregate_evidence_1.py | aggregate_evidence_06.py | Evidence |

**Additional Actions**:
- Keep: validate_prd_context.py, validate_prd_requirements.py, validate_prd_gate.py (already correct)

---

### Protocol 07 → Technical Design
**Current State**: Uses Protocol 6 scripts  
**Scripts to Rename**: 2

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_6.py | validate_prerequisites_07.py | Prerequisite |
| aggregate_evidence_6.py | aggregate_evidence_07.py | Evidence |

**Additional Actions**:
- Keep: validate_workflow_integration.py, validate_design_handoff.py, plan_from_brief.py

---

### Protocol 08 → Technical Task Generation
**Current State**: Uses Protocol 2 scripts  
**Scripts to Rename**: 2

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_2.py | validate_prerequisites_08.py | Prerequisite |
| aggregate_evidence_2.py | aggregate_evidence_08.py | Evidence |

**Additional Actions**:
- Keep: validate_rule_index.py, validate_high_level_tasks.py, validate_task_decomposition.py, validate_tasks.py, enrich_tasks.py

---

### Protocol 09 → Environment Setup
**Current State**: Uses Protocol 7 scripts  
**Scripts to Rename**: 2

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_7.py | validate_prerequisites_09.py | Prerequisite |
| aggregate_evidence_7.py | aggregate_evidence_09.py | Evidence |

**Additional Actions**:
- Keep: doctor.py, scaffold_phase_artifacts.py, install_and_test.sh, package_environment_assets.py

---

### Protocol 10 → Controlled Task Execution
**Current State**: Uses Protocol 3 scripts  
**Scripts to Rename**: 3

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_3.py | validate_prerequisites_10.py | Prerequisite |
| aggregate_evidence_3.py | aggregate_evidence_10.py | Evidence |
| run_protocol_3_gates.py | run_protocol_10_gates.py | CI Script |

**Additional Actions**:
- Keep: validate_preflight.py, validate_subtask_compliance.py, validate_quality_gate.py, validate_session_closeout.py

---

### Protocol 12 → Quality Audit
**Current State**: Uses Protocol 4 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_4.py | validate_prerequisites_12.py | Prerequisite |
| validate_gate_4_pre_audit.py | validate_gate_12_pre_audit.py | Gate |
| validate_gate_4_reporting.py | validate_gate_12_reporting.py | Gate |
| aggregate_evidence_4.py | aggregate_evidence_12.py | Evidence |

**Additional Actions**:
- Keep: collect_change_context.py, run_comprehensive_review.py, validate_router_mapping.py, verify_specialized_execution.py

---

### Protocol 13 → UAT Coordination
**Current State**: Uses Protocol 15 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_15.py | validate_prerequisites_13.py | Prerequisite |
| validate_gate_15_entry.py | validate_gate_13_entry.py | Gate |
| validate_gate_15_defects.py | validate_gate_13_defects.py | Gate |
| aggregate_evidence_15.py | aggregate_evidence_13.py | Evidence |

**Additional Actions**:
- Keep: build_uat_toolkit.py, generate_release_notes.py

---

### Protocol 14 → Pre-Deployment Staging
**Current State**: Uses Protocol 10 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_10.py | validate_prerequisites_14.py | Prerequisite |
| validate_gate_10_intake.py | validate_gate_14_intake.py | Gate |
| validate_gate_10_readiness.py | validate_gate_14_readiness.py | Gate |
| aggregate_evidence_10.py | aggregate_evidence_14.py | Evidence |

**Missing Scripts** (Create New):
- validate_gate_14_rehearsal.py (mentioned in quality gates)
- validate_gate_14_security.py (mentioned in quality gates)

---

### Protocol 15 → Production Deployment
**Current State**: Uses Protocol 11 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_11.py | validate_prerequisites_15.py | Prerequisite |
| validate_gate_11_readiness.py | validate_gate_15_readiness.py | Gate |
| validate_gate_11_launch.py | validate_gate_15_launch.py | Gate |
| aggregate_evidence_11.py | aggregate_evidence_15.py | Evidence |

**Keep (Already Correct)**:
- run_protocol_15_gates.py ✅

**Missing Scripts** (Create New):
- validate_gate_15_freeze.py
- validate_gate_15_reporting.py

---

### Protocol 16 → Post-Deployment Monitoring
**Current State**: Uses Protocol 12 scripts  
**Scripts to Rename**: 5

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_12.py | validate_prerequisites_16.py | Prerequisite |
| validate_gate_12_instrumentation.py | validate_gate_16_instrumentation.py | Gate |
| validate_gate_12_handoff.py | validate_gate_16_handoff.py | Gate |
| aggregate_evidence_12.py | aggregate_evidence_16.py | Evidence |

**Missing Scripts** (Create New):
- validate_gate_16_alerts.py
- validate_gate_16_assurance.py

---

### Protocol 17 → Incident Response
**Current State**: Uses Protocol 13 scripts  
**Scripts to Rename**: 5

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_13.py | validate_prerequisites_17.py | Prerequisite |
| validate_gate_13_severity.py | validate_gate_17_severity.py | Gate |
| validate_gate_13_resolution.py | validate_gate_17_resolution.py | Gate |
| aggregate_evidence_13.py | aggregate_evidence_17.py | Evidence |

**Missing Scripts** (Create New):
- validate_gate_17_mitigation.py
- validate_gate_17_recovery.py

---

### Protocol 18 → Performance Optimization
**Current State**: Uses Protocol 14 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_14.py | validate_prerequisites_18.py | Prerequisite |
| validate_gate_14_baseline.py | validate_gate_18_baseline.py | Gate |
| validate_gate_14_optimization.py | validate_gate_18_optimization.py | Gate |
| aggregate_evidence_14.py | aggregate_evidence_18.py | Evidence |

**Logic Updates Required**:
- validate_prerequisites_18.py: Change to validate telemetry packages, incident reports, baseline metrics (not pre-deployment requirements)
- validate_gate_18_baseline.py: Adjust threshold to ≥95% baseline completeness (performance domain)
- validate_gate_18_optimization.py: Set improvement threshold to ≥15%

---

### Protocol 19 → Documentation & Knowledge Transfer
**Current State**: Uses Protocol 16 scripts  
**Scripts to Rename**: 5

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_16.py | validate_prerequisites_19.py | Prerequisite |
| validate_gate_16_completeness.py | validate_gate_19_completeness.py | Gate |
| validate_gate_16_enablement.py | validate_gate_19_enablement.py | Gate |
| validate_gate_16_publication.py | validate_gate_19_publication.py | Gate |
| aggregate_evidence_16.py | aggregate_evidence_19.py | Evidence |

**Logic Updates Required**:
- validate_prerequisites_19.py: Verify documentation artifacts instead of monitoring assets

---

### Protocol 20 → Project Closure
**Current State**: Uses Protocol 17 scripts  
**Scripts to Rename**: 5

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_17.py | validate_prerequisites_20.py | Prerequisite |
| validate_gate_17_deliverables.py | validate_gate_20_deliverables.py | Gate |
| validate_gate_17_handover.py | validate_gate_20_handover.py | Gate |
| validate_gate_17_governance.py | validate_gate_20_governance.py | Gate |
| aggregate_evidence_17.py | aggregate_evidence_20.py | Evidence |

**Logic Updates Required**:
- Update to validate closure artifacts, financial reconciliation

---

### Protocol 21 → Continuous Maintenance
**Current State**: Uses Protocol 18 scripts  
**Scripts to Rename**: 6

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_18.py | validate_prerequisites_21.py | Prerequisite |
| validate_gate_18_backlog.py | validate_gate_21_backlog.py | Gate |
| validate_gate_18_approvals.py | validate_gate_21_approvals.py | Gate |
| validate_gate_18_governance.py | validate_gate_21_governance.py | Gate |
| aggregate_evidence_18.py | aggregate_evidence_21.py | Evidence |
| run_protocol_18_gates.py | run_protocol_21_gates.py | CI Script |

**Logic Updates Required**:
- Adapt to maintenance planning context (backlog consolidation, approval confirmation)

---

### Protocol 22 → Implementation Retrospective
**Current State**: Uses Protocol 5 scripts  
**Scripts to Rename**: 5

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_5.py | validate_prerequisites_22.py | Prerequisite |
| validate_gate_5_participation.py | validate_gate_22_participation.py | Gate |
| validate_gate_5_action_plan.py | validate_gate_22_action_plan.py | Gate |
| validate_gate_5_integration.py | validate_gate_22_integration.py | Gate |
| aggregate_evidence_5.py | aggregate_evidence_22.py | Evidence |

**Logic Updates Required**:
- Adjust for retrospective context (participation tracking, action readiness, CI integration)

---

### Protocol 23 → Script Governance
**Current State**: Uses Protocol 8 scripts  
**Scripts to Rename**: 4

| Current Name | New Name | Type |
|-------------|----------|------|
| validate_prerequisites_8.py | validate_prerequisites_23.py | Prerequisite |
| validate_gate_8_inventory.py | validate_gate_23_inventory.py | Gate |
| validate_gate_8_artifacts.py | validate_gate_23_artifacts.py | Gate |
| aggregate_evidence_8.py | aggregate_evidence_23.py | Evidence |

**Keep (Already Correct)**:
- validate_script_registry.py
- auto_register_scripts.py
- generate_protocol_23_artifacts.py

**Missing Scripts** (Create New):
- validate_gate_23_static.py
- validate_gate_23_reporting.py

---

## Summary by Script Type

### Prerequisites (18 scripts)
| Old Number | New Numbers | Count |
|-----------|-------------|-------|
| _1 | _06 | 1 |
| _2 | _08 | 1 |
| _3 | _10 | 1 |
| _4 | _12 | 1 |
| _5 | _22 | 1 |
| _6 | _07 | 1 |
| _7 | _09 | 1 |
| _8 | _23 | 1 |
| _10 | _14 | 1 |
| _11 | _15 | 1 |
| _12 | _16 | 1 |
| _13 | _17 | 1 |
| _14 | _18 | 1 |
| _15 | _13 | 1 |
| _16 | _19 | 1 |
| _17 | _20 | 1 |
| _18 | _21 | 1 |

### Gate Validators (27 scripts existing + 15 missing)
**Existing scripts to rename**: 27  
**New scripts to create**: 15

### Evidence Aggregators (18 scripts)
All 18 protocols need their evidence aggregators renumbered.

### CI Scripts (3 scripts)
- run_protocol_3_gates.py → run_protocol_10_gates.py
- run_protocol_18_gates.py → run_protocol_21_gates.py
- run_protocol_15_gates.py → Keep (already correct)

---

## Implementation Strategy

### Phase 1: Preparation (No File Changes)
1. ✅ Create backup of entire scripts/ directory
2. ✅ Export current script registry to JSON
3. ✅ Create test plan for CI pipeline validation
4. ✅ Document rollback procedure

### Phase 2: Atomic Renaming (Blocking Operations)
⚠️ **Critical**: All renames must happen atomically to avoid partial state

**Option A: Git-based (Recommended)**
```bash
# Create feature branch
git checkout -b fix/script-numbering-alignment

# Rename all 68 scripts in single commit
for rename in renaming_manifest.txt; do
  git mv $old_name $new_name
done

# Update script registry
python scripts/update_registry.py --apply-renaming-manifest

# Update all protocol automation hooks
python scripts/update_protocol_hooks.py --protocols 06-23

# Commit atomically
git commit -m "fix: align script numbers with protocol numbers (68 scripts)"
```

**Option B: Script-based**
```bash
./scripts/batch_rename_scripts.sh renaming_manifest.txt --dry-run
./scripts/batch_rename_scripts.sh renaming_manifest.txt --execute
```

### Phase 3: Registry Updates
1. Update scripts/script-registry.json with new names
2. Update all protocol AUTOMATION HOOKS sections
3. Update CI/CD pipeline configurations
4. Update documentation references

### Phase 4: Validation
1. Run: `python scripts/validate_script_registry.py`
2. Run: `./scripts/validate_all_protocols.py`
3. Execute CI pipeline in test environment
4. Verify all 23 protocols can locate their scripts

### Phase 5: Deployment
1. Merge feature branch to main
2. Tag release: `v1.0.0-script-renaming`
3. Deploy to CI environment
4. Monitor for 24 hours
5. Execute rollback if failures detected

---

## Risk Mitigation

### Risk 1: CI Pipeline Failures
**Mitigation**: 
- Test in isolated CI environment first
- Keep rollback script ready: `./scripts/rollback_rename.sh v1.0.0-script-renaming`

### Risk 2: In-Flight Protocol Executions
**Mitigation**:
- Schedule renaming during maintenance window
- Verify no active protocol runs: `ps aux | grep validate_`

### Risk 3: Hard-Coded Script Paths
**Mitigation**:
- Grep entire codebase for old script names
- Update any hard-coded references

```bash
# Find all references to old names
rg "validate_prerequisites_(1|2|3|4|5|6|7|8|10|11|12|13|14|15|16|17|18)\.py"
rg "validate_gate_(4|5|8|10|11|12|13|14|15|16|17|18)_"
```

---

## Acceptance Criteria

- [ ] All 68 scripts renamed successfully
- [ ] Script registry updated and validates clean
- [ ] All protocol automation hooks updated
- [ ] CI pipeline executes without errors
- [ ] All 23 protocols can run end-to-end
- [ ] No orphaned scripts in scripts/ directory
- [ ] Documentation updated with new names
- [ ] Rollback procedure tested

---

**Status**: ⚠️ READY FOR IMPLEMENTATION  
**Estimated Time**: 4-6 hours (with testing)  
**Required Approvals**: DevOps Lead, QA Lead  
**Rollback Time**: <15 minutes
