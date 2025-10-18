# Action Roadmap

| Priority | Action | Impact | Effort | Timeline | Owner |
|----------|--------|--------|--------|----------|-------|
| Critical | Implement missing validator scripts for all referenced quality gates (start with Protocols 01-11) | Restores automation backbone and enables evidence collection | 4-6 weeks | Immediate kickoff | Platform Automation Lead |【F:documentation/scripts-audit-and-optimization-report.md†L110-L179】
| Critical | Replace simulated quality gate logic with real review execution and evidence packaging | Enables compliance-grade QA and audit readiness | 3-4 weeks | Immediate kickoff | QA Engineering Lead |【F:scripts/quality_gates.py†L70-L193】
| High | Add change-control and feedback loops to task execution protocol (scope pivots, approvals, rollback) | Improves adaptability for freelance and agile teams | 2 weeks | Sprint 1 | Workflow Architect |【F:.cursor/ai-driven-workflow/10-process-tasks.md†L35-L154】
| High | Fix `simulate_protocol_execution.py`, add regression tests, and integrate into CI | Detects protocol drift early and prevents silent failures | 1 week | Sprint 1 | Tooling Engineer |【F:scripts/simulate_protocol_execution.py†L125-L190】
| Medium | Register existing validation utilities (`validate_brief.py`, `validate_tasks.py`, etc.) in `script-registry.json` and enforce registration via governance protocol | Reduces orphan scripts and ensures discoverability | 1 week | Sprint 2 | Script Governance Owner |【F:scripts/script-registry.json†L1-L22】【F:documentation/scripts-audit-and-optimization-report.md†L5-L108】
| Medium | Update `scripts/README.md` and protocol docs once automation parity is achieved | Aligns documentation with real capabilities | 1 week | Sprint 3 | Documentation Lead |【F:scripts/README.md†L1-L200】
| Low | Create scenario-driven acceptance tests for freelance, enterprise, and startup flows after automation rebuild | Provides ongoing production-readiness signal | 2 weeks | Sprint 4 | Solutions Engineer |【F:documentation/real-world-readiness-assessment.md†L33-L90】
