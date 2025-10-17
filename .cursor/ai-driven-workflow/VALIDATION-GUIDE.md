# Validation Guide

## Overview

This guide documents the comprehensive validation system for the ai-driven-workflow automation integration. The validation system ensures that all protocols are aligned, connected, and conflict-free.

## Validation Components

### 1. Workflow Integration Validation Script

**File:** `scripts/validate_workflow_integration.py`

**Purpose:** Comprehensive validation script that checks:
- Protocol alignment
- Connectivity validation
- Conflict detection
- Script validation
- Documentation validation

**Usage:**
```bash
# Basic validation
python scripts/validate_workflow_integration.py

# Verbose output
python scripts/validate_workflow_integration.py --verbose

# Save results to file
python scripts/validate_workflow_integration.py --output validation-results.json

# Attempt to fix common issues
python scripts/validate_workflow_integration.py --fix
```

### 2. Integration Test Suite

**File:** `scripts/test_workflow_integration.sh`

**Purpose:** End-to-end integration test script that validates:
- All protocol automation hooks
- Evidence pipeline flow
- Script dependencies
- Protocol file structure

**Usage:**
```bash
# Run all tests
bash scripts/test_workflow_integration.sh

# Keep test artifacts for inspection
bash scripts/test_workflow_integration.sh --keep

# Clean up test artifacts
bash scripts/test_workflow_integration.sh --cleanup
```

### 3. CI Validation Workflow

**File:** `.github/workflows/validate-integration.yml`

**Purpose:** Automated validation on every commit that:
- Runs validation script
- Executes integration tests
- Posts results to PR comments
- Blocks merge on critical issues

## Validation Checks

### Protocol Alignment Checks

| Check | Description | Validation |
|-------|-------------|------------|
| Script Existence | All referenced scripts exist | File system check |
| Script Executability | Scripts are executable | Permission check |
| Script References | Scripts referenced in protocols | Content analysis |
| Integration Points | Automation hooks properly placed | Content analysis |

### Connectivity Validation

| Connection | From Protocol | To Protocol | Expected Output | Required Sections |
|------------|---------------|-------------|-----------------|-------------------|
| Discovery → Bootstrap | 00 | 0 | `brief.md` | project-overview, objectives, deliverables |
| Bootstrap → PRD | 0 | 1 | `context-kit/` | README.md, rules/ |
| PRD → Tasks | 1 | 2 | `prd-{name}.md` | functional-specifications, technical-specifications |
| Tasks → Execution | 2 | 3 | `tasks-{name}.md` | automation-hooks, why-statements |
| Execution → Quality | 3 | 4 | `.artifacts/` | test-results, coverage, evidence |
| Quality → Retrospective | 4 | 5 | `audit-report.md` | quality-scores, ci-results |

### Conflict Detection

| Conflict Type | Description | Detection Method |
|---------------|-------------|------------------|
| Directive Inconsistency | `[MUST]`, `[GUIDELINE]` usage varies | Content analysis |
| Announcement Format | `[AUTOMATION]` prefix standardization | Pattern matching |
| Duplicate Hooks | Same script referenced multiple times | Cross-protocol analysis |
| Gate Criteria | Pass/fail thresholds inconsistent | Content analysis |

### Script Validation

| Check | Description | Validation |
|-------|-------------|------------|
| File Existence | Script files exist | File system check |
| Executability | Scripts are executable | Permission check |
| Shebang | Proper shebang present | Content analysis |
| Dependencies | Required packages available | Import testing |

### Documentation Validation

| Check | Description | Validation |
|-------|-------------|------------|
| README Completeness | Required sections present | Content analysis |
| Integration Guide | INTEGRATION-GUIDE.md exists | File system check |
| Script Documentation | Docstrings match usage | Content analysis |
| Examples Accuracy | Examples are runnable | Execution testing |

## Validation Output Format

### JSON Output Structure

```json
{
  "status": "pass/fail/warning",
  "summary": {
    "total_checks": 50,
    "passed": 48,
    "failed": 2,
    "warnings": 3
  },
  "alignment": {
    "protocol_00": "✅ aligned",
    "protocol_0": "✅ aligned",
    "protocol_1": "❌ failed",
    "protocol_2": "⚠️ warnings"
  },
  "connectivity": {
    "00→0": "✅ connected",
    "0→1": "⚠️ incomplete",
    "1→2": "✅ connected"
  },
  "conflicts": [
    {
      "type": "duplicate_automation_hook",
      "script": "evidence_report.py",
      "protocols": ["3", "5"],
      "message": "Script evidence_report.py referenced in multiple protocols",
      "severity": "warning"
    }
  ],
  "issues": [
    {
      "severity": "error",
      "protocol": "protocol_1",
      "message": "Script path mismatch",
      "fix": "Update script path to scripts/validate_prd_gate.py"
    }
  ],
  "recommendations": [
    "Consider standardizing automation hook placement",
    "Add missing script documentation"
  ]
}
```

### Console Output Format

```
🔍 Dev-Workflow Integration Validation
==================================================
Status: PASS
Total Checks: 50
Passed: 48
Failed: 0
Warnings: 2

📋 Protocol Alignment:
  protocol_00: ✅ aligned
  protocol_0: ✅ aligned
  protocol_1: ✅ aligned
  protocol_2: ✅ aligned
  protocol_3: ✅ aligned
  protocol_4: ✅ aligned
  protocol_5: ✅ aligned

🔗 Connectivity:
  00→0: ✅ connected
  0→1: ✅ connected
  1→2: ✅ connected
  2→3: ✅ connected
  3→4: ✅ connected
  4→5: ✅ connected

⚠️ Issues:
  WARNING: Script missing shebang: scripts/validate_brief.py
    Fix: Add shebang to scripts/validate_brief.py
```

## Integration Test Scenarios

### Test Scenario 1: Mock Client Discovery Flow

**Purpose:** Validate Protocol 00 automation hooks

**Steps:**
1. Create test job post fixture
2. Run brief validation script
3. Run risk scoring script
4. Run domain classification script
5. Validate output artifacts

**Expected Results:**
- Brief validation score ≥ 80
- Risk scores generated
- Domain classified with confidence > 80%

### Test Scenario 2: Mock PRD Generation Flow

**Purpose:** Validate Protocol 1 automation hooks

**Steps:**
1. Use test brief fixture
2. Run PRD validation script
3. Run PRD asset generation script
4. Validate output artifacts

**Expected Results:**
- PRD validation score ≥ 85
- User stories generated
- Data schemas created
- API contracts defined

### Test Scenario 3: Mock Task Generation Flow

**Purpose:** Validate Protocol 2 automation hooks

**Steps:**
1. Use test PRD fixture
2. Run task validation script
3. Run task enrichment script
4. Validate output artifacts

**Expected Results:**
- Task file validation passes
- Tasks enriched with metadata
- Automation hooks present
- WHY statements complete

### Test Scenario 4: Mock Evidence Pipeline

**Purpose:** Validate evidence flow from execution to retrospective

**Steps:**
1. Create test artifacts
2. Run evidence capture
3. Run evidence aggregation
4. Validate retrospective loading

**Expected Results:**
- Evidence artifacts created
- Aggregation successful
- Retrospective data available

## Troubleshooting

### Common Issues

#### Issue 1: Script Not Found
**Symptom:** `python scripts/script_name.py: No such file or directory`
**Resolution:**
1. Check script exists in `scripts/` directory
2. Verify script is executable: `chmod +x scripts/script_name.py`
3. Check Python path and dependencies

#### Issue 2: Validation Gate Failure
**Symptom:** `[GATE FAILED] Automation Validation Complete`
**Resolution:**
1. Check automation script output for specific errors
2. Review gate criteria and thresholds
3. Address underlying issues before proceeding
4. Use manual fallback if automation unavailable

#### Issue 3: Evidence Pipeline Broken
**Symptom:** Missing evidence artifacts in retrospective
**Resolution:**
1. Verify evidence capture in Protocol 3
2. Check `.artifacts/` directory permissions
3. Ensure evidence aggregation in Protocol 5
4. Review evidence report generation

#### Issue 4: CI Workflow Integration Issues
**Symptom:** CI workflows not executing or results not captured
**Resolution:**
1. Verify GitHub Actions workflow files exist
2. Check `run_workflow.py` script configuration
3. Ensure proper authentication and permissions
4. Review workflow execution logs

### Debug Commands

#### Check Script Availability
```bash
ls -la scripts/
python scripts/script_name.py --help
```

#### Verify Automation Hooks
```bash
grep -r "python scripts/" .cursor/ai-driven-workflow/
```

#### Check Evidence Artifacts
```bash
ls -la .artifacts/
find .artifacts/ -name "*.json" -exec jq . {} \;
```

#### Validate CI Integration
```bash
gh run list --workflow=ci-test.yml --limit 5
gh run list --workflow=ci-lint.yml --limit 5
```

## Continuous Validation

### GitHub Actions Integration

The validation system integrates with GitHub Actions to provide:

1. **Automated Validation:** Runs on every commit
2. **PR Comments:** Posts validation results to pull requests
3. **Merge Protection:** Blocks merge on critical issues
4. **Artifact Storage:** Saves validation results for review

### Validation Triggers

- **Push to main/develop:** Full validation suite
- **Pull Request:** Validation + PR comment
- **Path Changes:** Only validate when ai-driven-workflow files change

### Quality Gates

- **Critical Issues:** Block merge (exit code 1)
- **Warnings:** Allow merge with notification (exit code 2)
- **Success:** Allow merge (exit code 0)

## Best Practices

### For Developers

1. **Run Validation Locally:** Always validate before pushing
2. **Fix Issues Promptly:** Address validation failures immediately
3. **Review Warnings:** Don't ignore validation warnings
4. **Test Integration:** Run integration tests before major changes

### For Maintainers

1. **Monitor CI Results:** Watch for validation failures
2. **Update Validation:** Keep validation checks current
3. **Document Changes:** Update validation guide when adding checks
4. **Review PR Comments:** Ensure validation feedback is helpful

## Validation Metrics

### Success Criteria

- **Protocol Alignment:** 100% of protocols aligned
- **Script Validation:** All scripts exist and executable
- **Connectivity:** All protocol connections validated
- **Conflict Detection:** No critical conflicts found
- **Documentation:** All required documentation present

### Performance Targets

- **Validation Time:** < 30 seconds for full validation
- **Test Execution:** < 2 minutes for integration tests
- **CI Runtime:** < 5 minutes for complete CI validation
- **Artifact Size:** < 10MB for validation artifacts

## Future Enhancements

### Phase 1: Advanced Analytics
- Machine learning for risk prediction
- Automated effort estimation
- Pattern recognition for common issues

### Phase 2: Integration Expansion
- Slack/Teams notifications for validation events
- Dashboard for validation metrics
- Automated reporting to stakeholders

### Phase 3: AI Enhancement
- Automated code review suggestions
- Intelligent test generation
- Automated documentation updates

---

*This validation guide ensures the ai-driven-workflow automation remains aligned, functional, and continuously validated.*
