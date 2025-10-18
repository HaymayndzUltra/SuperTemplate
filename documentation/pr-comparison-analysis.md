# External PR Comparison Analysis

## Purpose
This report compares repository state in `work` (current branch) against four external pull requests (PRs #29-#32) published on the upstream project. It captures material differences in reporting depth, automation coverage, and governance guidance so the next delivery cycle can integrate the strongest ideas while avoiding previously observed gaps.

## Baseline Snapshot (Current Branch)
- Lifecycle reporting synthesises scores and qualitative analysis across Protocols 01-23 with a consistent 5-dimension rubric, but data is maintained manually in Markdown tables without machine-readable exports. 【F:documentation/protocol-lifecycle-verification-report.md†L1-L112】
- Script audit focuses on tabular inventory captured manually inside Markdown, omitting JSON inventories or automation hooks for keeping the data fresh. 【F:documentation/scripts-audit-and-optimization-report.md†L1-L111】
- Real-world readiness assessment summarises scenario outcomes but lacks structured scorecards or generated artefacts for regression tracking. 【F:documentation/real-world-readiness-assessment.md†L1-L54】
- Action roadmap prioritises automation rebuilds, registry coverage, and change-control governance but is defined in a single static table. 【F:documentation/action-roadmap.md†L1-L34】

## PR #29 – "Add workflow readiness analysis and remediation roadmap"
- Provides concise markdown-only reports similar to the baseline but emphasises failure of `simulate_protocol_execution.py` and highlights scenario verdicts for freelance, enterprise, and startup flows.
- Focuses on the absence of ~160 validator scripts yet does not supply automation to locate or track them, keeping remediation manual.
- Readiness score reported as **3.70/10**, slightly below our baseline (5.2/10), signalling a harsher qualitative judgement without new evidence sources.

### Gaps vs Baseline
- No structured datasets to reconcile conflicting counts of missing scripts or protocol scores.
- Lacks actionable tooling to validate claims about failing simulators or gating scripts.

## PR #30 – "Add comprehensive workflow verification and automation audit reports"
- Reframes roadmap with objectives, milestone plan, and success metrics, adding dependencies, evidence columns, and alignment with Cursor-independent execution.
- Reinforces need for manual fallback instructions while automation is rebuilt, a nuance absent from our baseline.
- Maintains manual data capture; there is still no automation or JSON output.

### Gaps vs Baseline
- Introduces strategic detail (objectives/milestones) not yet reflected in our action roadmap.
- Still dependent on manual updates; automation debt quantification remains approximate.

## PR #31 – "Add workflow verification reports and automation audits"
- Adds JSON datasets (`analysis-scorecard.json`, `protocol-scores.json`) to back scoring tables and script inventory, enabling machine-driven reconciliation and regression tracking.
- Supplies Python utilities (`generate_script_inventory_report.py`, `analyze_protocol_script_references.py`, `generate_scorecard_summary.py`) to compute inventories and scorecards directly from repository sources, addressing governance drift root causes.
- Expands documentation to include detailed protocol-by-protocol findings, script reference matrix, and cross-phase evidence chains.

### Gaps vs Baseline
- Current branch lacks all automation scripts and JSON datasets introduced in PR #31.
- Baseline markdown tables diverge from PR #31 values (e.g., 47 missing scripts vs. 160 references), signalling inconsistent counting methodologies.

## PR #32 – "Add comprehensive workflow readiness analysis reports"
- Streamlines content but still emphasises missing `aggregate_evidence_*`, `run_protocol_*_gates.py`, and governance artefacts for Protocol 23.
- Highlights need for regression harnesses referencing `test_workflow_integration.sh`, tying readiness to executable tests.
- Does not include the automation tooling from PR #31, suggesting multiple parallel remediation strategies.

### Gaps vs Baseline
- Reinforces missing automation families and governance assets not yet delivered locally.
- Introduces requirement for regression harnesses that our repository does not currently implement.

## Cross-PR Observations
1. **Automation Inventory Drift** – Reported counts of missing scripts vary (baseline: 47; PR #29/#30: 160; PR #31: 160 of 205 references). Without automated inventory generation, we cannot adjudicate the true deficit.
2. **Evidence Artefact Governance** – All PRs call for aggregated evidence manifests and governance outputs, yet only PR #31 proposes generators. Current branch has none.
3. **Change-Control & Scenario Handling** – Multiple PRs identify absent change-request workflows and scenario-specific playbooks. Baseline documentation acknowledges the gap but provides no implementation path.
4. **Testing Strategy** – PR #32 stresses regression harnesses; our branch does not extend beyond narrative assessments.
5. **Cursor Dependency** – PR #30 requests Cursor-independent bootstrap guidance; existing protocols still rely heavily on Cursor commands.

## Risk & Gap Summary
- **Data Integrity Risk:** Manual tables risk divergence from reality; we need generated datasets to ensure auditability.
- **Automation Deficit:** Validator, gate-runner, and evidence aggregator scripts remain unimplemented locally, blocking readiness.
- **Governance Weakness:** Script registry coverage and governance artefacts (inventories, remediation backlogs) are missing.
- **Change-Control Deficiency:** No defined workflow for scope changes, client approvals, or rollback handling mid-execution.
- **Testing Void:** Lack of automated regression harnesses undermines confidence in lifecycle claims.

## Implementation Plan for Next Development Session
The following plan merges actionable ideas from PRs #29-#32 with baseline priorities. Tasks are grouped into four waves aligned with the next development cycle.

### Wave 1 – Establish Accurate Telemetry (Week 1)
1. **Adopt Automated Inventory Scripts** – Port or reimplement tooling equivalent to `generate_script_inventory_report.py` and `analyze_protocol_script_references.py` to produce authoritative JSON/CSV inventories. Store outputs under `documentation/` and integrate into CI so drift is flagged automatically.
2. **Generate Machine-Readable Scorecards** – Create a reproducible pipeline (CLI or Make target) that emits protocol score JSON consistent with Markdown tables, enabling validation of manual edits.
3. **Baseline Evidence Catalogue** – Draft schema and placeholder generator for evidence manifests required by protocols, ensuring future automation can populate them.

### Wave 2 – Restore Gate Automation (Weeks 2-3)
4. **Design Generic Gate Runner Framework** – Implement shared runners for `run_protocol_*_gates.py`, `validate_gate_*`, and `aggregate_evidence_*` families, with configuration-driven mapping from protocols to validators.
5. **Prioritise Validator Delivery** – Deliver validators for Phase 0-2 first (proposal, discovery, brief, PRD), then extend to development and deployment phases. Each validator must log evidence conforming to the manifest schema from Wave 1.
6. **Integrate Change-Request Governance** – Add a new protocol or subroutine covering scope changes, client approvals, and rollback handling; update Protocols 08-11 to reference it.

### Wave 3 – Governance & Documentation Hardening (Weeks 3-4)
7. **Expand Script Registry Coverage** – Update `scripts/script-registry.json` with all active automation, add descriptions, and build validation to fail CI when unregistered scripts are introduced.
8. **Cursor-Independent Execution Guides** – Produce CLI-first bootstrap instructions and revise protocols to include non-Cursor fallbacks so teams without Cursor access can comply.
9. **Governance Artefact Generation** – Implement automation for Protocol 23 outputs (script index, documentation audit, remediation backlog) leveraging inventory data from Wave 1.

### Wave 4 – Testing & Scenario Validation (Week 5)
10. **Regression Harness** – Extend `test_workflow_integration.sh` or equivalent to exercise new gate runners and validators with fixture data.
11. **Scenario Playbooks** – Create executable scenario suites (freelance, enterprise, startup) that invoke the automation stack and verify evidence output.
12. **Readiness Reassessment** – Recompute scorecards and readiness metrics using automated tooling; update documentation and roadmap accordingly.

Each task should capture evidence artefacts (logs, manifests, score outputs) to support end-to-end testing and compliance-ready reporting.
