# Script Renaming Manifest - Phase 1 Atomic Operations
**Generated**: November 5, 2025  
**Source**: plano.md audit table (lines 99-109)  
**Execution Mode**: ATOMIC RENAME REQUIRED

---

## CRITICAL RENAMING OPERATIONS

### Protocol 18 - Performance Optimization & Tuning
**Issue**: Currently using Protocol 14 scripts instead of Protocol 18

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_14.py | validate_prerequisites_18.py | Rename | scripts/validators/ |
| validate_gate_14_baseline.py | validate_gate_18_baseline.py | Rename | scripts/validators/ |
| validate_gate_14_optimization.py | validate_gate_18_optimization.py | Rename | scripts/validators/ |
| aggregate_evidence_14.py | aggregate_evidence_18.py | Rename | scripts/aggregators/ |

**Hook Updates Required**:
- .cursor/ai-driven-workflow/18-*.md - Update all script references
- CI/CD pipeline configurations
- Script registry entries

---

### Protocol 19 - Documentation & Knowledge Transfer
**Issue**: Currently using Protocol 16 scripts instead of Protocol 19

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_16.py | validate_prerequisites_19.py | Rename | scripts/validators/ |
| validate_gate_16_completeness.py | validate_gate_19_completeness.py | Rename | scripts/validators/ |
| validate_gate_16_enablement.py | validate_gate_19_enablement.py | Rename | scripts/validators/ |
| validate_gate_16_publication.py | validate_gate_19_publication.py | Rename | scripts/validators/ |
| aggregate_evidence_16.py | aggregate_evidence_19.py | Rename | scripts/aggregators/ |

**Hook Updates Required**:
- .cursor/ai-driven-workflow/19-*.md - Update all script references
- Documentation generation pipelines
- Registry mappings

---

### Protocol 20 - Project Closure & Handover
**Issue**: Currently using Protocol 17 scripts instead of Protocol 20

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_17.py | validate_prerequisites_20.py | Rename | scripts/validators/ |
| validate_gate_17_deliverables.py | validate_gate_20_deliverables.py | Rename | scripts/validators/ |
| validate_gate_17_handover.py | validate_gate_20_handover.py | Rename | scripts/validators/ |
| validate_gate_17_governance.py | validate_gate_20_governance.py | Rename | scripts/validators/ |
| aggregate_evidence_17.py | aggregate_evidence_20.py | Rename | scripts/aggregators/ |

**Hook Updates Required**:
- .cursor/ai-driven-workflow/20-*.md - Update all script references
- Closure checklist templates
- Handover automation

---

### Protocol 21 - Continuous Maintenance & Support Planning
**Issue**: Currently using Protocol 18 scripts instead of Protocol 21

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_18.py | validate_prerequisites_21.py | Rename | scripts/validators/ |
| validate_gate_18_backlog.py | validate_gate_21_backlog.py | Rename | scripts/validators/ |
| validate_gate_18_approvals.py | validate_gate_21_approvals.py | Rename | scripts/validators/ |
| validate_gate_18_governance.py | validate_gate_21_governance.py | Rename | scripts/validators/ |
| aggregate_evidence_18.py | aggregate_evidence_21.py | Rename | scripts/aggregators/ |
| run_protocol_18_gates.py | run_protocol_21_gates.py | Rename | scripts/ci/ |

**Hook Updates Required**:
- .cursor/ai-driven-workflow/21-*.md - Update all script references
- Maintenance backlog processors
- Support planning tools

---

### Protocol 22 - Implementation Retrospective  
**Issue**: Currently using Protocol 5 scripts instead of Protocol 22

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_5.py | validate_prerequisites_22.py | Rename | scripts/validators/ |
| validate_gate_5_participation.py | validate_gate_22_participation.py | Rename | scripts/validators/ |
| validate_gate_5_action_plan.py | validate_gate_22_action_plan.py | Rename | scripts/validators/ |
| validate_gate_5_integration.py | validate_gate_22_integration.py | Rename | scripts/validators/ |
| aggregate_evidence_5.py | aggregate_evidence_22.py | Rename | scripts/aggregators/ |

**Hook Updates Required**:
- .cursor/ai-driven-workflow/22-*.md - Update all script references
- Retrospective facilitator tools
- Action tracking systems

---

### Protocol 23 - Script Governance
**Issue**: Currently using Protocol 8 scripts instead of Protocol 23

| Current Name | New Name | Type | Location |
|-------------|----------|------|----------|
| validate_prerequisites_8.py | validate_prerequisites_23.py | Rename | scripts/validators/ |
| validate_gate_8_inventory.py | validate_gate_23_inventory.py | Rename | scripts/validators/ |
| validate_gate_8_artifacts.py | validate_gate_23_artifacts.py | Rename | scripts/validators/ |
| aggregate_evidence_8.py | aggregate_evidence_23.py | Rename | scripts/aggregators/ |

**Additional Scripts to Create**:
- validate_gate_23_static.py (NEW)
- validate_gate_23_reporting.py (NEW)

**Hook Updates Required**:
- .cursor/ai-driven-workflow/23-*.md - Update all script references
- Script registry validation
- Governance toolkit integration

---

## EXECUTION CHECKLIST

### Pre-Rename Validation
```bash
# 1. Backup current state
tar -czf scripts_backup_$(date +%Y%m%d_%H%M%S).tar.gz scripts/

# 2. Generate dependency map
grep -r "validate_prerequisites_14\|validate_gate_14\|aggregate_evidence_14" . > deps_protocol_18.txt
grep -r "validate_prerequisites_16\|validate_gate_16\|aggregate_evidence_16" . > deps_protocol_19.txt
grep -r "validate_prerequisites_17\|validate_gate_17\|aggregate_evidence_17" . > deps_protocol_20.txt
grep -r "validate_prerequisites_18\|validate_gate_18\|aggregate_evidence_18" . > deps_protocol_21.txt
grep -r "validate_prerequisites_5\|validate_gate_5\|aggregate_evidence_5" . > deps_protocol_22.txt
grep -r "validate_prerequisites_8\|validate_gate_8\|aggregate_evidence_8" . > deps_protocol_23.txt

# 3. Verify no active CI runs
# [Check CI/CD dashboard]
```

### Atomic Rename Script
```python
#!/usr/bin/env python3
# atomic_rename.py - Execute all renames in single transaction

import os
import json
from pathlib import Path

RENAME_MAP = {
    # Protocol 18
    "scripts/validators/validate_prerequisites_14.py": "scripts/validators/validate_prerequisites_18.py",
    "scripts/validators/validate_gate_14_baseline.py": "scripts/validators/validate_gate_18_baseline.py",
    "scripts/validators/validate_gate_14_optimization.py": "scripts/validators/validate_gate_18_optimization.py",
    "scripts/aggregators/aggregate_evidence_14.py": "scripts/aggregators/aggregate_evidence_18.py",
    
    # Protocol 19
    "scripts/validators/validate_prerequisites_16.py": "scripts/validators/validate_prerequisites_19.py",
    "scripts/validators/validate_gate_16_completeness.py": "scripts/validators/validate_gate_19_completeness.py",
    "scripts/validators/validate_gate_16_enablement.py": "scripts/validators/validate_gate_19_enablement.py",
    "scripts/validators/validate_gate_16_publication.py": "scripts/validators/validate_gate_19_publication.py",
    "scripts/aggregators/aggregate_evidence_16.py": "scripts/aggregators/aggregate_evidence_19.py",
    
    # Protocol 20
    "scripts/validators/validate_prerequisites_17.py": "scripts/validators/validate_prerequisites_20.py",
    "scripts/validators/validate_gate_17_deliverables.py": "scripts/validators/validate_gate_20_deliverables.py",
    "scripts/validators/validate_gate_17_handover.py": "scripts/validators/validate_gate_20_handover.py",
    "scripts/validators/validate_gate_17_governance.py": "scripts/validators/validate_gate_20_governance.py",
    "scripts/aggregators/aggregate_evidence_17.py": "scripts/aggregators/aggregate_evidence_20.py",
    
    # Protocol 21
    "scripts/validators/validate_prerequisites_18.py": "scripts/validators/validate_prerequisites_21.py",
    "scripts/validators/validate_gate_18_backlog.py": "scripts/validators/validate_gate_21_backlog.py",
    "scripts/validators/validate_gate_18_approvals.py": "scripts/validators/validate_gate_21_approvals.py",
    "scripts/validators/validate_gate_18_governance.py": "scripts/validators/validate_gate_21_governance.py",
    "scripts/aggregators/aggregate_evidence_18.py": "scripts/aggregators/aggregate_evidence_21.py",
    "scripts/ci/run_protocol_18_gates.py": "scripts/ci/run_protocol_21_gates.py",
    
    # Protocol 22
    "scripts/validators/validate_prerequisites_5.py": "scripts/validators/validate_prerequisites_22.py",
    "scripts/validators/validate_gate_5_participation.py": "scripts/validators/validate_gate_22_participation.py",
    "scripts/validators/validate_gate_5_action_plan.py": "scripts/validators/validate_gate_22_action_plan.py",
    "scripts/validators/validate_gate_5_integration.py": "scripts/validators/validate_gate_22_integration.py",
    "scripts/aggregators/aggregate_evidence_5.py": "scripts/aggregators/aggregate_evidence_22.py",
    
    # Protocol 23
    "scripts/validators/validate_prerequisites_8.py": "scripts/validators/validate_prerequisites_23.py",
    "scripts/validators/validate_gate_8_inventory.py": "scripts/validators/validate_gate_23_inventory.py",
    "scripts/validators/validate_gate_8_artifacts.py": "scripts/validators/validate_gate_23_artifacts.py",
    "scripts/aggregators/aggregate_evidence_8.py": "scripts/aggregators/aggregate_evidence_23.py",
}

def execute_rename():
    """Execute atomic rename operation"""
    success_log = []
    error_log = []
    
    print("Starting atomic rename operation...")
    
    for old_path, new_path in RENAME_MAP.items():
        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                success_log.append(f"✓ {old_path} → {new_path}")
            else:
                error_log.append(f"✗ Not found: {old_path}")
        except Exception as e:
            error_log.append(f"✗ Failed: {old_path} - {str(e)}")
    
    # Write results
    with open(".artifacts/phase-0-kickoff/rename_results.json", "w") as f:
        json.dump({
            "success": success_log,
            "errors": error_log,
            "total": len(RENAME_MAP),
            "success_count": len(success_log),
            "error_count": len(error_log)
        }, f, indent=2)
    
    print(f"Completed: {len(success_log)} success, {len(error_log)} errors")
    return len(error_log) == 0

if __name__ == "__main__":
    success = execute_rename()
    exit(0 if success else 1)
```

### Post-Rename Validation
```bash
# 1. Update all protocol files
python update_protocol_references.py

# 2. Update script registry
python update_script_registry.py

# 3. Run validation suite
python scripts/validate_all_protocols.py

# 4. Test CI pipeline
python scripts/ci/run_all_gates.py --dry-run
```

---

## ROLLBACK PLAN

In case of issues:

```bash
# 1. Stop all services
systemctl stop ci-runner

# 2. Restore from backup
tar -xzf scripts_backup_[timestamp].tar.gz

# 3. Revert protocol files
git checkout -- .cursor/ai-driven-workflow/

# 4. Clear caches
rm -rf .artifacts/cache/
python -m compileall -b scripts/

# 5. Restart services
systemctl start ci-runner
```

---

## AFFECTED SYSTEMS

### Direct Impact:
- CI/CD pipelines (Jenkins/GitHub Actions)
- Script registry database
- Protocol automation hooks
- Evidence aggregation systems

### Indirect Impact:
- Documentation generation
- Monitoring dashboards
- Audit reports
- Developer tooling

### Communication Required:
- All protocol owners
- DevOps team
- QA automation team
- Release management

---

## SUCCESS CRITERIA

1. **All scripts renamed** - 100% of listed renames completed
2. **No broken references** - grep shows no old script names
3. **CI passes** - All protocol gates execute successfully
4. **Registry updated** - Script registry reflects new names
5. **Evidence collected** - Rename audit trail archived

---

**Manifest Version**: 1.0  
**Status**: READY FOR REVIEW  
**Approval Required From**: Technical Lead, DevOps Lead, QA Lead
