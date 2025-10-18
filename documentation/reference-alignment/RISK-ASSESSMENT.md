# Reference Alignment Risk Assessment

## Summary
Renumbering the AI-driven workflow requires coordinated updates across protocol handoffs, artifact directories, and supporting documentation. The matrix analysis highlights several high-risk areas that can break the workflow if not remediated carefully.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L79】

## High-Risk Items
| Risk | Impact | Evidence |
| --- | --- | --- |
| Misaligned `@apply` targets after rename | Breaks protocol sequencing; automation shortcuts and review flows fail | Multiple protocols form loops or jump backwards (e.g., 00 → 0 → 00, 8 → 4) and must be realigned to the intended linear path.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L37】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】 |
| Stale artifact directories (`.artifacts/protocol-X/`) | Evidence ingestion scripts and CI jobs cannot locate required files | Every protocol embeds numbered artifact directories tied to legacy IDs, requiring synchronized replacements during renumbering.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L39-L68】 |
| Documentation automation references | Integration, validation, and agent guides hard-code legacy numbering, causing post-rename confusion or broken instructions | Core guidance still references Protocol 00–5 flows and must be rewritten for the new sequence.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L12-L86】【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L231】 |

## Medium-Risk Items
| Risk | Impact | Evidence |
| --- | --- | --- |
| Review ecosystem references | Review protocols could trigger obsolete filenames, blocking gated quality workflows | Review router and individual review docs include direct `@apply` calls to the legacy names.【F:.cursor/ai-driven-workflow/review-protocols/README.md†L63-L79】【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L252-L263】 |
| Integration text mentions | Narrative references (“Protocol 3”, “Protocol 9”) may drift from actual numbering, leading to operator confusion | Integration map and supporting copy include numerous textual references that must be updated alongside renames.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L70-L79】 |

## Low-Risk Items
| Risk | Impact | Evidence |
| --- | --- | --- |
| Script comments & README snippets | Minor documentation drift; easier to spot and fix post-rename | Less formal references exist mainly in comments or README sections but still warrant a sweep after bulk updates.【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L12-L86】 |

## Mitigation Strategy
1. Execute renames using the authoritative mapping before editing internals to keep diffs manageable.【F:protocol-renumbering-prompt.md†L50-L119】
2. Apply automated search-and-replace for artifact directories using the transformation table, then run the validation script to detect residual legacy paths.【F:protocol-renumbering-prompt.md†L62-L83】【F:documentation/reference-alignment/VALIDATION-SCRIPT-OUTLINE.md†L10-L54】
3. Update supporting docs and review workflows immediately after protocol edits to prevent knowledge base drift.【F:documentation/reference-alignment/ADJUSTMENT-PROMPT.md†L18-L56】
4. Re-run the validation checklist and integration tests described in the adjustment prompt to confirm end-to-end alignment.【F:documentation/reference-alignment/ADJUSTMENT-PROMPT.md†L62-L83】
