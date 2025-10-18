# Action Roadmap

## Objectives
1. Restore enforceable automation so every lifecycle gate can execute deterministically. 【edfa92†L9-L129】
2. Reduce tooling lock-in to support diverse delivery environments (freelance, enterprise, startup). 【F:.cursor/ai-driven-workflow/05-bootstrap-your-project.md†L37-L159】【F:.cursor/ai-driven-workflow/15-production-deployment.md†L160-L191】
3. Provide governance for change control, evidence tracking, and script registry coverage. 【99ddcb†L1-L21】【d8c6a4†L1-L17】

## Roadmap Overview
| Priority | Action | Impact | Effort | Owner | Dependencies | Evidence |
|---|---|---|---|---|---|---|
| Critical | Build `scripts/run_protocol_gates.py` and generic validator registry; replace `run_protocol_*_gates.py` placeholders. | Enables cross-phase gate execution and reduces duplicate templates. | 40h | Automation Engineer | Protocol metadata model | 【edfa92†L9-L129】 |
| Critical | Implement `aggregate_evidence.py` with manifest-based configuration and update protocols to use it. | Restores evidence consolidation promised in every phase. | 32h | Automation Engineer | Above gate runner | 【edfa92†L9-L129】 |
| Critical | Author change-request protocol with approval workflow, waiver handling, and artifact templates. | Adds missing governance for scope changes across all scenarios. | 24h | Program Manager | Stakeholder alignment | Analysis: change gap (report §Phase 3). |
| High | Register bootstrap, deployment, monitoring, and maintenance scripts; extend `script-registry.json` with descriptions. | Improves visibility and governance for later phases. | 16h | DevOps Lead | Inventory audit | 【d8c6a4†L1-L17】【F:scripts/script-registry.json†L1-L19】 |
| High | Write Cursor-independent bootstrap guide + CLI wrappers (e.g., `bootstrap_project.py --no-cursor`). | Unlocks delivery for teams without Cursor access. | 20h | Developer Experience | Gate runner | 【F:.cursor/ai-driven-workflow/05-bootstrap-your-project.md†L37-L159】 |
| High | Provide manual fallback instructions for each validator until automation ships; update protocols accordingly. | Maintains service continuity in absence of automation. | 18h | Technical Writer | Validator audit | 【F:.cursor/ai-driven-workflow/08-generate-tasks.md†L126-L154】【F:.cursor/ai-driven-workflow/15-production-deployment.md†L160-L191】 |
| Medium | Introduce `tests/scripts/` suite covering registry CLI argument parsing and dry runs. | Prevents regressions in automation layer. | 24h | QA Engineer | Gate runner | 【F:scripts/validate_prd_gate.py†L1-L115】【F:scripts/run_workflow.py†L1-L49】 |
| Medium | Consolidate evidence manifests into a centralized index (e.g., `.artifacts/index.json`). | Simplifies audits and cross-phase traceability. | 16h | Documentation Lead | Evidence aggregator | Protocol artifacts (report §Cross-Protocol). |
| Medium | Update documentation to remove placeholder references (`scripts/script_name.py`, etc.). | Eliminates misleading setup guidance. | 12h | Documentation Lead | Registry update | 【edfa92†L121-L129】 |
| Low | Produce scenario playbooks (freelance, enterprise, startup) with updated workflows post-fixes. | Improves onboarding and demonstration assets. | 12h | Solutions Architect | Completion of critical fixes | Report §Scenario Testing. |
| Low | Add KPI tracking for automation adoption (scripts executed, gates passed). | Supports continuous improvement metrics. | 8h | Program Manager | Gate runner telemetry | Scorecard insights. |

## Milestones
1. **Week 1:** Deliver gate runner, evidence aggregator, and change-request protocol; publish interim manual fallback guidance.
2. **Week 2:** Expand registry coverage, release Cursor-independent bootstrap instructions, and refresh documentation placeholders.
3. **Week 3:** Ship test suite, centralized evidence index, and updated governance documentation.
4. **Week 4:** Release scenario playbooks and KPI instrumentation; reassess readiness scorecard.

## Success Metrics
- **Automation coverage:** 100% of referenced validators implemented or replaced by generic runner. 【edfa92†L9-L129】
- **Registry completeness:** ≥85% of active scripts registered with descriptions. 【d8c6a4†L1-L17】【F:scripts/script-registry.json†L1-L19】
- **Change control adoption:** All scope changes processed through the new protocol within two sprints.
- **Readiness score:** Raise overall readiness to ≥7.5/10 before reconsidering production launch. 【c56fbe†L1-L27】

