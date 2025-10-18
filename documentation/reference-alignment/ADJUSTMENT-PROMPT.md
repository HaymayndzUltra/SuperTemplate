# Reference Alignment Adjustment Prompt

## Section 1 – Reference Mapping Matrix
1. **Old → New filenames** (apply before editing internals):
   - Follow the renaming plan from the existing renumbering prompt so that legacy identifiers (00a–18) map to sequential 01–23 plus supporting docs.【F:protocol-renumbering-prompt.md†L50-L119】
2. **Reference types to update for each file**:
   - Direct `@apply` handoffs listed in the discovery matrix must be retargeted to the new filenames once files are renamed.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L37】
   - Artifact directories referencing `.artifacts/protocol-X/` require synchronized renumbering to their new two-digit identifiers.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L39-L68】【F:protocol-renumbering-prompt.md†L62-L83】
   - Textual mentions (“Protocol X”, prerequisite references, integration notes) in support docs (`INTEGRATION-GUIDE.md`, `PROTOCOL-INTEGRATION-MAP.md`, `AGENTS.md`, review protocols) must mirror the renamed assets.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L231】【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L246-L259】

## Section 2 – File-by-File Update Instructions
For each asset, perform the following after renaming:

1. **Workflow protocols (all 23 primary files)**
   - Update front-matter protocol identifiers, headings, and any inline “Protocol N” references.
   - Rewrite `@apply` directives to reference the new sequential filenames from Section 1.
   - Refactor artifact paths using the mapping in Section 3.
   - Validate prerequisite/integration text so upstream/downstream references cite the correct new numbers (e.g., “Protocol 07” instead of “Protocol 6”).

2. **Supporting documents (`INTEGRATION-GUIDE.md`, `PROTOCOL-INTEGRATION-MAP.md`, `AGENTS.md`, `VALIDATION-GUIDE.md`, `README.md`)**
   - Refresh diagrams, tables, and flow descriptions to match the renumbered order and fixed loops documented in the matrix.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L70-L79】
   - Update all script call examples to use the new artifact directories and filenames.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】

3. **Review protocols (`review-protocols/*.md`)**
   - Replace `@apply` targets with the new filenames and adjust descriptive text (“Protocol 10” → “Protocol 11”, etc.).【F:.cursor/ai-driven-workflow/review-protocols/README.md†L63-L79】【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L252-L263】

4. **Cursor automation helpers (`AGENTS.md`, root automation docs)**
   - Align helper commands to the renamed files and ensure any contextual descriptions reference the corrected protocol order.【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L231】

5. **Scripted tooling and CI manifests**
   - Search for `.artifacts/protocol-X/` references in scripts (`scripts/*.py`, shell utilities) and update to the new directory names in lockstep with protocol docs.

## Section 3 – Artifact Path Updates
Use the following global replacements (execute only after file renames to avoid collisions):

| Old path | New path |
| --- | --- |
| `.artifacts/protocol-0/` | `.artifacts/protocol-05/` |
| `.artifacts/protocol-3/` | `.artifacts/protocol-10/` |
| `.artifacts/protocol-4/` | `.artifacts/protocol-12/` |
| `.artifacts/protocol-5/` | `.artifacts/protocol-22/` |
| `.artifacts/protocol-6/` | `.artifacts/protocol-07/` |
| `.artifacts/protocol-7/` | `.artifacts/protocol-09/` |
| `.artifacts/protocol-8/` | `.artifacts/protocol-23/` |
| `.artifacts/protocol-9/` | `.artifacts/protocol-11/` |
| `.artifacts/protocol-10/` | `.artifacts/protocol-14/` |
| `.artifacts/protocol-11/` | `.artifacts/protocol-15/` |
| `.artifacts/protocol-12/` | `.artifacts/protocol-16/` |
| `.artifacts/protocol-13/` | `.artifacts/protocol-17/` |
| `.artifacts/protocol-14/` | `.artifacts/protocol-18/` |
| `.artifacts/protocol-15/` | `.artifacts/protocol-13/` |
| `.artifacts/protocol-16/` | `.artifacts/protocol-19/` |
| `.artifacts/protocol-17/` | `.artifacts/protocol-20/` |
| `.artifacts/protocol-18/` | `.artifacts/protocol-21/` |

_Source: Artifact transformation plan in renumbering prompt.【F:protocol-renumbering-prompt.md†L62-L83】_

## Section 4 – Supporting Documentation Updates
- **Integration map** – Rebuild the flow so it matches the corrected sequence (14 → 16, 18 → 22, etc.), eliminating loops noted in the matrix.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L70-L79】
- **Integration & validation guides** – Refresh automation tables, connectivity matrices, and validation checklists to reference new protocol numbers and artifact directories.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L12-L86】
- **Review ecosystem** – Ensure review protocols and router utilities point to the updated protocol filenames in both prose and code snippets.【F:.cursor/ai-driven-workflow/review-protocols/README.md†L63-L79】【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L170-L181】

## Section 5 – Validation Checklist
Before finalizing the renumbering, confirm the following:
- [ ] All `@apply` references resolved to new filenames without loops or dead ends.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L6-L37】
- [ ] Every artifact path now matches the new numbering scheme, and scripts reference the updated directories.【F:documentation/reference-alignment/REFERENCE-MATRIX.md†L39-L68】
- [ ] Supporting documentation (integration map, guides, AGENTS) reflects the corrected sequence and numbering.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L231】
- [ ] Review workflows trigger the intended downstream protocols after renaming.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L252-L263】
- [ ] No residual references to legacy protocol identifiers remain in text, automation, or scripts (perform `rg "Protocol [0-9A-Za-z]+"`).
