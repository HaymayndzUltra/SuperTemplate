# Action Roadmap

| Priority | Action | Impact | Effort | Timeline | Owner |
|---|---|---|---|---|---|
| Critical | Build missing `aggregate_evidence_*`, `run_protocol_*_gates.py`, and `validate_gate_*` families for Protocols 01–23, matching the artifacts and thresholds defined in each quality gate. | Restores automated gating across every phase; unblocks readiness scoring. | 80 hrs | Immediate | Automation Lead |
| High | Expand `script-registry.json` to register all reusable scripts (doctor, rule audits, deployment, monitoring) with protocol metadata and evidence outputs. | Enables orchestrators to discover automation and reduces manual routing. | 24 hrs | Week 1 | Workflow Engineer |
| High | Implement Protocol 23 governance helpers (`script-index.json`, `inventory-validation-report.json`, `documentation-audit.csv`, `static-analysis-report.json`, `remediation-backlog.csv`). | Provides audit artifacts for enterprise compliance and script governance. | 40 hrs | Week 1–2 | Governance Engineer |
| Medium | Consolidate rule/template tooling into a single governance CLI (normalize, audit, optimize, standardize) with shared logging. | Reduces duplication and stabilizes Protocols 04–05 execution. | 32 hrs | Week 2 | Platform Engineer |
| Medium | Add regression harnesses for new gate/evidence scripts using `test_workflow_integration.sh` patterns and CI hooks. | Prevents regression of automation families and documents expectations. | 24 hrs | Week 3 | QA Lead |

## Evidence Links
- Missing automation families across protocols.【b5f2c8†L18-L193】
- Registry coverage limited to 13 scripts while critical tools remain unregistered.【e51091†L1-L20】【6c0539†L1-L7】
- Governance protocol requires inventory, documentation, static analysis, and remediation outputs not yet implemented.【b0f694†L24-L104】
- Rule tooling overlap across normalization, audit, and optimization scripts.【0a9f31†L49-L85】【5b16d5†L185-L211】
- Existing integration harness for reference when adding regression tests.【0bf469†L1-L4】
