# Protocol Gate Automation - Quick Reference Guide

> **For**: Developers, QA Engineers, CI/CD Administrators  
> **Version**: 1.1 (Phase 3 Release)  
> **Last Updated**: 2025-10-19

---

## Quick Start

### Run All Gates for a Protocol
```bash
python3 scripts/run_protocol_gates.py 01  # Client Proposal
python3 scripts/run_protocol_gates.py 02  # Client Discovery
python3 scripts/run_protocol_gates.py 03  # Project Brief
```

### Aggregate Evidence
```bash
python3 scripts/aggregate_evidence_01.py
python3 scripts/aggregate_evidence_02.py
python3 scripts/aggregate_evidence_03.py
```

---

## Phase 3 Additions (NEW)

### Script Registry Validation
```bash
# Validate registry coverage
python3 scripts/validate_script_registry.py \
  --output .artifacts/validation/script-registry-report.json \
  --min-coverage 95.0

# Auto-register orphaned scripts
python3 scripts/auto_register_scripts.py --dry-run  # Preview
python3 scripts/auto_register_scripts.py            # Apply
```

### Protocol 23 Governance Artifacts
```bash
# Generate all governance artifacts
python3 scripts/generate_protocol_23_artifacts.py

# Output:
#   .artifacts/protocol-23/script-index.json
#   .artifacts/protocol-23/documentation-audit.json
#   .artifacts/protocol-23/remediation-backlog.json
```

---

## CLI Reference

### Individual Validators

**Protocol 01:**
```bash
python3 scripts/validate_gate_01_jobpost.py
python3 scripts/validate_gate_01_tone.py
python3 scripts/validate_gate_01_structure.py
python3 scripts/validate_gate_01_compliance.py
python3 scripts/validate_gate_01_final.py
```

**Protocol 02:**
```bash
python3 scripts/validate_gate_02_objectives.py
python3 scripts/validate_gate_02_requirements.py
python3 scripts/validate_gate_02_expectations.py
python3 scripts/validate_gate_02_confirmation.py
```

**Protocol 03:**
```bash
python3 scripts/validate_gate_03_discovery.py
python3 scripts/validate_gate_03_structure.py
python3 scripts/validate_gate_03_approvals.py
```

---

## Output Formats

### Validator Output (JSON)
```json
{
  "status": "pass",
  "score": 0.95,
  "notes": "Validation passed with score 0.95"
}
```

### Evidence Manifest
```json
{
  "protocol_id": "01",
  "protocol_title": "Client Proposal Generation",
  "generated_at": "2025-10-19T02:00:00Z",
  "automation_coverage": {
    "coverage": 1.0
  },
  "artifacts": [...],
  "validators": [...]
}
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All validations passed |
| 1 | One or more validations failed |
| 2+ | Script error |

---

## CI/CD Integration

### GitHub Actions
```yaml
name: Protocol Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: python3 scripts/run_protocol_gates.py 01
```

### Script Registry Enforcement
```yaml
# Auto-enforced via .github/workflows/script-registry-enforcement.yml
# Fails build if coverage < 95%
# Comments on PRs with remediation guidance
```

---

## Cursor-Independent Execution

See full guide: `documentation/cursor-independent-guide.md`

**Quick example:**
```bash
# Without Cursor IDE
python3 scripts/bootstrap_project.py --project-name "My Project"
python3 scripts/run_protocol_gates.py 01
python3 scripts/generate_evidence_manifest.py 01
```

---

## Troubleshooting

### Missing Config
**Error**: `Missing gate config`  
**Solution**: Ensure YAML file exists in `config/protocol_gates/`

### Orphaned Scripts
**Error**: Registry validation fails  
**Solution**: Run auto-registration
```bash
python3 scripts/auto_register_scripts.py
```

### Missing Artifacts
**Error**: Validator returns "Missing artifact"  
**Solution**: Run protocol workflow first to generate artifacts

---

## Reference Links

- **Phase 2 Summary**: `documentation/phase-2-gate-automation-summary.md`
- **Phase 3 Summary**: `documentation/phase-3-governance-summary.md`
- **Cursor-Independent Guide**: `documentation/cursor-independent-guide.md`
- **Action Roadmap**: `documentation/action-roadmap.md`
- **Script Registry**: `scripts/script-registry.json`

---

**Version History**
- **1.1** (2025-10-19): Added Phase 3 governance tools
- **1.0** (2025-10-19): Initial release with Protocols 01-03
