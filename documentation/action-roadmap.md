# Action Roadmap

**Assessment date:** 2025-01-18  
**Analyst:** AI-Driven Workflow Engineering Partner

---

| Priority | Action | Impact | Effort | Timeline | Owner |
|----------|--------|--------|--------|----------|-------|
| Critical | Implement missing validation scripts for Protocols 02-05 and register them (`validate_discovery_scope.py`, `validate_discovery_inputs.py`, `validate_scaffold.py`). | High | 80 hrs | Immediate | Automation Lead |
| Critical | Create deployment, monitoring, and incident automation suites aligned with Protocols 15-17 (GitHub Actions workflows, alert integrations, rollback tooling). | High | 120 hrs | Immediate | DevOps Lead |
| High | Build evidence generation CLI to emit required manifests (`project-brief-validation-report.json`, `execution-artifact-manifest.json`) and enforce storage policy. | High | 60 hrs | Week 1-2 | Platform Engineer |
| High | Expand `script-registry.json` to include discovery, operations, and governance categories; add CI validation for registry coverage. | Medium | 24 hrs | Week 1-2 | Automation Lead |
| High | Author change-control processes for task execution, UAT, and closure protocols, including negotiation and variance handling templates. | Medium | 40 hrs | Week 2-3 | Delivery Manager |
| Medium | Consolidate scaffold generators (`generate_from_brief.py`, `bootstrap_project.py`) into a governed tool with tests. | Medium | 36 hrs | Week 3-4 | Platform Engineer |
| Medium | Document and add docstrings/tests for operational scripts (`deploy_backend.sh`, `backup_workflows.py`, `build_submission_pack.sh`). | Medium | 32 hrs | Week 3-4 | DevOps Lead |
| Medium | Integrate evidence tooling (`evidence_manager.py`, `evidence_report.py`) into protocol automation and add regression tests. | Medium | 40 hrs | Week 3-4 | Quality Lead |
| Low | Develop monitoring dashboards and runbooks for ongoing maintenance (Protocols 21-23), including SLA trackers. | Medium | 48 hrs | Backlog | Reliability Engineer |
| Low | Produce example playbooks and templates demonstrating end-to-end workflow execution for freelance, enterprise, and startup scenarios. | Medium | 40 hrs | Backlog | Product Enablement |

Actions prioritize closure of automation and governance gaps identified in lifecycle and scripts audits.【F:documentation/protocol-script-reference-report.md†L5-L38】【F:documentation/scripts-audit-optimization-report.md†L1-L125】
