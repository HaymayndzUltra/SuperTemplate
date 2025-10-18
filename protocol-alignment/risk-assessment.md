# Protocol Reference Renumbering Risk Assessment

## Summary
Renumbering touches 32+ automation handoffs, hundreds of artifact references, and every integration guide. High-risk areas concentrate around automation-critical protocols (00-series, 4, 14, 5) and documentation hubs (INTEGRATION-GUIDE, PROTOCOL-INTEGRATION-MAP).【9b875e†L1-L65】【fbba9c†L1-L150】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L72】

## Risk Matrix
| Risk Level | Area | Impact | Mitigation |
| --- | --- | --- | --- |
| High | `@apply` handoffs (26 targets) | Broken protocol execution flow halts automation and reviews. | Update all handoffs post-renumbering and validate via automated `@apply` check script.【9b875e†L1-L65】 |
| High | Artifact path namespaces (`.artifacts/protocol-XX/`) | Automation scripts and evidence archives misaligned, causing data loss or validation failure. | Bulk rename directories, update inline code snippets, and run artifact path scanner to confirm replacements.【fbba9c†L1-L150】 |
| High | Integration guidance docs (INTEGRATION-GUIDE, PROTOCOL-INTEGRATION-MAP) | Teams follow outdated flow, creating dependency mismatches across phases. | Prioritize document rewrites, then run validation script to ensure sequences read 01→27 consecutively.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L72】【5e96ed†L4-L20】 |
| Medium | Protocol text mentions (`Protocol X`) | Confusing instructions and misaligned checklists. | Use search-and-replace mapping plus validation script to detect legacy tokens.【5e96ed†L1-L36】 |
| Medium | Review protocols & AGENTS instructions | Review routing may call deprecated filenames. | Update review protocol `@apply` commands and AGENTS prompts alongside main renumbering.【9b875e†L68-L87】 |
| Medium | Scenario and scoring documentation | Stakeholders misinterpret phase alignment. | Refresh README, evaluation prompt, and scoring references after renumbering. |
| Low | Script filenames (e.g., `aggregate_evidence_XX.py`) | Scripts may reference old IDs but easy to adjust. | Audit script names during artifact path rename and adjust as needed.【fbba9c†L1-L150】 |
| Low | Historical references in reports | Archival documents may use old numbering but low operational impact. | Annotate historical docs or leave as-is with note on renumbering epoch. |

## Recommended Sequencing
1. **Freeze automation**: pause any workflows relying on `.cursor/ai-driven-workflow` while renumbering occurs.
2. **Rename files & directories**: update filenames and artifact directories first to prevent new references from using legacy IDs.
3. **Run automated checks**: execute validation script outline after each batch (filenames, `@apply`, artifact paths, text mentions).
4. **Update documentation**: once files pass checks, rewrite integration guides, AGENTS, and review protocols using new numbering.
5. **Manual verification**: spot-check high-risk protocols (former 00a, 4, 14, 5) to ensure evidence chains and quality gates remain intact.
6. **Release communication**: publish change log summarizing new numbering for downstream consumers.

## Residual Risks
- **Human references**: Stakeholders may recall legacy IDs; provide mapping quick reference (see reference-mapping.md).
- **External integrations**: Any external tooling referencing `.artifacts/protocol-*` requires coordinated updates; confirm via stakeholder outreach.
- **Partial adoption**: If teams update only subsets (e.g., rename files but skip guides), dependency mismatches persist; enforce via CI validation.

By sequencing remediation and leveraging automated validation, teams can minimize downtime and ensure a clean transition to the unified numbering scheme.
