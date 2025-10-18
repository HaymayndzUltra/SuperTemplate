# Protocol Reference Renumbering Risk Assessment

## 1. Executive Overview
Renumbering the AI-driven workflow protocols introduces coordinated changes across 29 automation handoffs, 610 textual dependencies, 484 artifact directories, and 47 embedded file paths.【F:documentation/protocol-reference-summary.json†L2-L5】 The following assessment prioritises remediation activities to minimise disruption to protocol execution, evidence collection, and supporting documentation.

## 2. High-Risk Areas

| Risk | Description | Impact | Recommended Controls |
| --- | --- | --- | --- |
| Broken handoff chain | Any missed update to an `@apply` directive severs the execution sequence, causing Cursor to open the wrong protocol or fail entirely.【F:documentation/protocol-reference-data.json†L2-L226】 | Loss of workflow continuity; automation scripts fail to trigger next phase. | Update handoffs immediately after renaming, then run the validation script to confirm every link is correct.【F:documentation/protocol-reference-validation-outline.md†L31-L66】 |
| Artifact orphaning | Legacy `.artifacts/protocol-N/` references prevent downstream phases from locating evidence bundles.【F:documentation/protocol-reference-data.json†L2-L226】 | Quality gates and audits reference stale or missing evidence. | Batch-update artifact paths during the rename and regenerate manifests before validation runs.【F:protocol-renumbering-prompt.md†L24-L62】 |
| Integration guide desync | INTEGRATION-GUIDE and PROTOCOL-INTEGRATION-MAP govern cross-team coordination; outdated numbering misguides implementers.【F:documentation/protocol-reference-data.json†L226-L312】 | Teams follow incorrect prerequisites or skip required validations. | Refresh supporting docs in tandem with protocol updates and perform manual proofreading before release.【F:protocol-renumbering-prompt.md†L74-L90】 |

## 3. Medium-Risk Areas

| Risk | Description | Impact | Recommended Controls |
| --- | --- | --- | --- |
| Residual “Protocol X” mentions | Lingering textual references to the legacy numbers introduce ambiguity in prerequisites, evidence sections, and communication templates.【F:documentation/protocol-reference-summary.json†L2-L5】 | Conflicting instructions, inconsistent reporting, and onboarding friction. | Execute targeted search-and-replace operations, then spot-check critical protocols (PRD, architecture, quality audit).【F:protocol-reference-mapping.md†L5-L114】 |
| Review protocol drift | Review playbooks reference specific execution protocols; missed updates break the escalation flow.【F:documentation/protocol-reference-data.json†L244-L354】 | Reviewers open outdated guidance or initiate the wrong workflow. | Update review assets alongside primary protocols and validate using the automated checker. |
| Script parameter mismatches | Embedded automation commands (e.g., validation scripts) may still point at old artifact directories.【F:documentation/protocol-reference-data.json†L2-L226】 | Automated checks fail or produce incomplete evidence bundles. | Grep for `.artifacts/protocol-` within scripts and adjust parameters as part of Section 3 tasks in the adjustment prompt.【F:protocol-renumbering-prompt.md†L64-L72】 |

## 4. Low-Risk Areas

| Risk | Description | Impact | Recommended Controls |
| --- | --- | --- | --- |
| README drift | Top-level summaries and AGENTS instructions may lag behind the renumbered flow.【F:protocol-reference-mapping.md†L5-L86】 | Minor confusion for new contributors. | Update overview text after primary renumbering and include in final proofreading pass. |
| Legacy screenshots or diagrams | Visual assets that display the old numbering persist until manually refreshed. | Cosmetic inconsistency only. | Regenerate diagrams or annotate them with the new numbering during documentation QA. |

## 5. Mitigation Roadmap
1. **Execute renumbering using the adjustment prompt** to keep file, handoff, and artifact updates in sync.【F:protocol-renumbering-prompt.md†L14-L90】
2. **Run the validation script outline** to detect any missed updates before merging.【F:documentation/protocol-reference-validation-outline.md†L15-L83】
3. **Review high-priority documents manually** (Integration Guide, Protocol Integration Map, review playbooks) to ensure narrative coherence.【F:protocol-reference-mapping.md†L98-L156】
4. **Log remediation actions** in release notes so downstream teams understand the new numbering scheme.

## 6. Residual Risk Statement
After executing the mitigation roadmap, residual risk is limited to minor documentation inconsistencies. Automated validation combined with manual proofreading provides sufficient assurance that the renumbered protocol suite will operate without regression.
