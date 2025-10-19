# Action Roadmap

**Last Updated**: 2025-10-19  
**Status**: Wave 1 ✅ Complete | Wave 2 ✅ Complete | Wave 3 ✅ Complete | Wave 4 ⏳ Pending

This roadmap sequences remediation work for the next development cycle, aligning with the cross-PR analysis captured in `pr-comparison-analysis.md`.

---

## Wave 1 – Establish Accurate Telemetry ✅ COMPLETED

**Completion Date**: 2025-10-19

| Priority | Action | Status | Evidence |
|----------|--------|--------|----------|
| Critical | Implement automated script inventory tooling and publish JSON/CSV artefacts | ✅ Done | `scripts/inventory_protocols.py`, `documentation/protocol-script-inventory.json` |
| Critical | Generate machine-readable protocol scorecards | ✅ Done | `scripts/generate_protocol_scorecard.py`, `documentation/protocol-scorecard.json` |
| High | Define evidence manifest schema | ✅ Done | `documentation/evidence-manifest.schema.json`, `scripts/generate_evidence_manifest.py` |

**Summary**: All Wave 1 telemetry foundations established. Automation coverage now measured at protocol level with JSON/CSV outputs.

---

## Wave 2 – Restore Gate Automation ✅ COMPLETED

**Completion Date**: 2025-10-19

| Priority | Action | Status | Evidence |
|----------|--------|--------|----------|
| Critical | Build configuration-driven gate runner framework | ✅ Done | `scripts/run_protocol_gates.py`, `config/protocol_gates/*.yaml` |
| Critical | Implement validators for Phase 0-2 protocols | ✅ Done | 12 validator scripts, 3 aggregation scripts, 100% tests passing |
| High | Add change-control sub-protocol | ⏳ Deferred | To be addressed in future iteration |

**Summary**: Gate automation framework operational for Protocols 01-03. All validators produce schema-compliant evidence manifests. Integration tests passing at 100%.

**Deliverables**:
- 3 gate configuration files (YAML)
- 12 gate validator scripts (Python)
- 3 evidence aggregation scripts
- Gate runner framework with dynamic config loading
- Regression test suite (pytest + bash integration)
- Updated script registry

**Full Details**: `documentation/phase-2-gate-automation-summary.md`

---

## Wave 3 – Governance & Documentation Hardening ✅ COMPLETED

**Completion Date**: 2025-10-19

| Priority | Action | Status | Evidence |
|----------|--------|--------|----------|
| High | Extend script registry with governance and CI enforcement | ✅ Done | `scripts/validate_script_registry.py`, `.github/workflows/script-registry-enforcement.yml` |
| High | Publish Cursor-independent bootstrap and execution guides | ✅ Done | `documentation/cursor-independent-guide.md` (400+ lines) |
| Medium | Automate Protocol 23 artefacts | ✅ Done | `scripts/generate_protocol_23_artifacts.py`, 3 governance artifacts generated |

**Summary**: Comprehensive script governance established with automated validation, CI enforcement, and Cursor-independent execution. Protocol 23 artifacts now auto-generated.

**Deliverables**:
- Script registry validator with orphan detection
- Auto-registration tool for categorizing scripts
- GitHub Actions CI enforcement workflow
- Cursor-independent execution guide (all 28 protocols)
- Protocol 23 automation (script index, doc audit, remediation backlog)

**Current Governance Status**:
- Total Scripts: 115
- Registered: 32 (27.27% coverage)
- Target: ≥95% coverage
- Documentation Score: 80.95%
- **Action Required**: Run remediation (estimated 2-4 hours)

**Full Details**: `documentation/phase-3-governance-summary.md`

---

## Wave 4 – Testing & Scenario Validation ⏳ PENDING

**Target**: Week 5

| Priority | Action | Status | Estimated Effort |
|----------|--------|--------|------------------|
| High | Expand regression harness to cover gate runner and validator flows | 🔜 Ready | 3 days |
| Medium | Develop executable scenario playbooks (freelance, enterprise, startup) | 🔜 Ready | 3 days |
| Medium | Recalculate readiness scores using automated tooling | 🔜 Ready | 1 day |

**Prerequisites**:
- ✅ Gate automation framework operational (Wave 2)
- ✅ Evidence manifest schema defined (Wave 1)
- ✅ Governance automation in place (Wave 3)
- ⚠️ Script registry coverage remediation recommended

**Planned Activities**:
1. Extend `test_workflow_integration.sh` for Protocols 04-11
2. Create scenario playbooks with test fixtures
3. Run end-to-end validation across personas
4. Generate comprehensive readiness report
5. Update protocol scorecards

---

## Phase 3 Remediation Tasks (Optional)

**Before Wave 4**, consider completing these remediation tasks to establish a clean baseline:

### Registry Coverage Improvement
```bash
# Current: 27.27% | Target: 95%
python3 scripts/auto_register_scripts.py --dry-run  # Preview
python3 scripts/auto_register_scripts.py            # Apply
python3 scripts/validate_script_registry.py         # Verify
```

### Documentation Improvement
```bash
# Current: 80.95% | Target: 90%
# Review remediation backlog
cat .artifacts/protocol-23/remediation-backlog.json

# Address high-priority issues (20 scripts need attention)
# Estimated: 15-30 minutes per script
```

---

## Progress Tracking

### Completed Waves: 3/4 (75%)

**Wave 1** (Telemetry): ████████████████████ 100%  
**Wave 2** (Gate Automation): ████████████████████ 100%  
**Wave 3** (Governance): ████████████████████ 100%  
**Wave 4** (Testing): ░░░░░░░░░░░░░░░░░░░░ 0%

### Key Metrics

| Metric | Baseline | Current | Target | Progress |
|--------|----------|---------|--------|----------|
| Protocol Automation | 0% | 10.7% (3/28) | 39.3% (11/28) | ▓▓▓░░░░░░░ 27% |
| Script Registry Coverage | 0% | 27.27% | 95% | ▓▓▓░░░░░░░ 29% |
| Documentation Score | Unknown | 80.95% | 90% | ▓▓▓▓▓▓▓▓▓░ 90% |
| Evidence Manifest Compliance | 0% | 100% | 100% | ▓▓▓▓▓▓▓▓▓▓ 100% |
| CI Integration | 0% | 100% | 100% | ▓▓▓▓▓▓▓▓▓▓ 100% |

---

## Evidence Package

All artifacts include continuous evidence capture (logs, manifests, score outputs) to maintain auditability and align with quality gates.

**Artifact Locations**:
- Wave 1: `documentation/protocol-*.json`, `.csv`
- Wave 2: `.artifacts/protocol-01/`, `protocol-02/`, `protocol-03/`
- Wave 3: `.artifacts/protocol-23/`, `.artifacts/validation/`
- Wave 4: TBD

**Documentation Index**:
- Phase 2 Summary: `documentation/phase-2-gate-automation-summary.md`
- Phase 3 Summary: `documentation/phase-3-governance-summary.md`
- Gate Quick Reference: `documentation/gate-automation-quick-reference.md`
- Cursor-Independent Guide: `documentation/cursor-independent-guide.md`

---

## Next Steps

### Immediate (Wave 4 Prep)
1. ✅ Complete Wave 3 deliverables
2. 🔜 Remediate script registry coverage (optional but recommended)
3. 🔜 Extend gate automation to Protocols 04-11
4. 🔜 Develop scenario playbooks

### Short-term (Wave 4 Execution)
1. Expand integration test harness
2. Execute scenario validations
3. Generate readiness reports
4. Update protocol scorecards

### Long-term (Post-Wave 4)
1. Automation for remaining protocols (12-28)
2. Performance optimization
3. Dashboard development
4. Advanced analytics integration

---

**Roadmap Status**: On track | 3/4 waves complete | Phase 3 remediation optional
