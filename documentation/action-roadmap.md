# Action Roadmap

This roadmap sequences remediation work for the next development cycle, aligning with the cross-PR analysis captured in `pr-comparison-analysis.md`.

## Wave 1 – Establish Accurate Telemetry (Week 1)
| Priority | Action | Impact | Effort | Owner | Evidence Requirements |
|----------|--------|--------|--------|-------|------------------------|
| Critical | Implement automated script inventory tooling and publish JSON/CSV artefacts alongside Markdown reports. | Creates authoritative baseline for automation coverage and reconciles conflicting counts from external PRs. | 2d | Automation Lead | Commit history with new CLI, generated artefacts stored under `documentation/`. |
| Critical | Generate machine-readable protocol scorecards from repository data to validate Markdown tables. | Prevents drift between manual summaries and actual scoring inputs. | 1.5d | Workflow Analyst | JSON outputs plus updated CI command in `README` or scripts. |
| High | Define evidence manifest schema and stub generator consumed by downstream protocols. | Unlocks future validators that must emit structured evidence. | 1d | Quality Engineer | Schema definition, sample manifest, documentation update. |

## Wave 2 – Restore Gate Automation (Weeks 2-3)
| Priority | Action | Impact | Effort | Owner | Evidence Requirements |
|----------|--------|--------|--------|-------|------------------------|
| Critical | Build configuration-driven gate runner framework powering `run_protocol_*_gates.py`, `validate_gate_*`, and `aggregate_evidence_*` families. | Replaces missing automation families highlighted across PRs #29-#32. | 4d | Automation Lead | Executable CLI, unit tests, configuration docs. |
| Critical | Implement validators for Phase 0-2 protocols with evidence logging that conforms to manifest schema. | Enables first tranche of enforceable quality gates and proves framework viability. | 3d | Protocol Engineer | Validator modules, tests, sample output attached to protocols. |
| High | Add change-control sub-protocol covering approvals, rollback triggers, and documentation updates; integrate with Protocols 08-11. | Closes iteration governance gap noted by every external review. | 2d | Delivery Manager | Updated protocol docs, decision tree, acceptance criteria. |

## Wave 3 – Governance & Documentation Hardening (Weeks 3-4)
| Priority | Action | Impact | Effort | Owner | Evidence Requirements |
|----------|--------|--------|--------|-------|------------------------|
| High | Extend `scripts/script-registry.json` with full inventory metadata and enforce coverage via CI. | Prevents new orphan scripts and aligns with governance expectations. | 2d | Governance Engineer | Registry diff, CI rule, documentation of process. |
| High | Publish Cursor-independent bootstrap and execution guides; update protocols with fallback instructions. | Expands usability for teams without Cursor access, matching PR #30 recommendations. | 2d | Developer Experience | New guide, protocol updates, validated walkthrough. |
| Medium | Automate Protocol 23 artefacts (script index, documentation audit, remediation backlog) using inventory data. | Delivers governance evidence demanded in PR #32. | 3d | Governance Engineer | Generated artefacts, CLI usage docs, integration tests. |

## Wave 4 – Testing & Scenario Validation (Week 5)
| Priority | Action | Impact | Effort | Owner | Evidence Requirements |
|----------|--------|--------|--------|-------|------------------------|
| High | Expand regression harness (e.g., `test_workflow_integration.sh`) to cover gate runner and validator flows with fixtures. | Provides executable confidence in automation stack. | 3d | QA Lead | Updated test scripts, CI logs demonstrating pass/fail criteria. |
| Medium | Develop executable scenario playbooks (freelance, enterprise, startup) that run against automation and collect manifests. | Demonstrates end-to-end readiness across target personas. | 3d | Solutions Architect | Playbook scripts, sample outputs, documentation. |
| Medium | Recalculate readiness scores using automated tooling and refresh reports. | Confirms remediation impact and prepares for go/no-go review. | 1d | Workflow Analyst | Updated JSON+Markdown outputs, comparison summary. |

Progress through these waves should include continuous evidence capture (logs, manifests, score outputs) to maintain auditability and align with quality gates.
