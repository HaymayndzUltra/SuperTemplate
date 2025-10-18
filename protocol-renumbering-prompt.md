# Comprehensive Protocol Renumbering Adjustment Prompt

## Overview
Use this prompt to renumber the AI-driven workflow protocols from the current mixed identifiers (00a, 00B, 01, 0, 1–18) to the proposed sequential set (01–27). The plan preserves existing automation, evidence chains, and orchestration logic identified in the reference mapping analysis.【F:protocol-reference-mapping.md†L1-L176】

---

## SECTION 1: Reference Mapping Matrix

### 1.1 Old → New Filename Sequence (27 protocols + guides)
| Current name | Proposed name |
| --- | --- |
| 00a-client-proposal-generation.md | 01-client-proposal-generation.md |
| 00B-client-discovery-initiation.md | 02-client-discovery-initiation.md |
| 01-project-brief-creation.md | 03-project-brief-creation.md |
| 00-project-bootstrap-and-context-engineering.md | 04-project-bootstrap-and-context-engineering.md |
| 0-bootstrap-your-project.md | 05-bootstrap-your-project.md |
| 1-create-prd.md | 06-create-prd.md |
| 6-technical-design-architecture.md | 07-technical-design-architecture.md |
| 2-generate-tasks.md | 08-generate-tasks.md |
| 7-environment-setup-validation.md | 09-environment-setup-validation.md |
| 3-process-tasks.md | 10-process-tasks.md |
| 9-integration-testing.md | 11-integration-testing.md |
| 4-quality-audit.md | 12-quality-audit.md |
| 15-uat-coordination.md | 13-uat-coordination.md |
| 10-pre-deployment-staging.md | 14-pre-deployment-staging.md |
| 11-production-deployment.md | 15-production-deployment.md |
| 12-monitoring-observability.md | 16-monitoring-observability.md |
| 13-incident-response-rollback.md | 17-incident-response-rollback.md |
| 14-performance-optimization.md | 18-performance-optimization.md |
| 16-documentation-knowledge-transfer.md | 19-documentation-knowledge-transfer.md |
| 17-project-closure.md | 20-project-closure.md |
| 18-maintenance-support.md | 21-maintenance-support.md |
| 5-implementation-retrospective.md | 22-implementation-retrospective.md |
| 8-script-governance-protocol.md | 23-script-governance-protocol.md |
| 00-client-discovery.md | 24-client-discovery.md |
| 00-generate-rules.md | (retain / isolate outside numbered flow) |
| INTEGRATION-GUIDE.md | 26-integration-guide.md |
| VALIDATION-GUIDE.md | 27-validation-guide.md |

### 1.2 Direct `@apply` Adjustments
Update every `@apply` directive to reference the new filenames, keeping the existing sequence. Confirm the gap between Protocol 05 (bootstrap) and Protocol 06 (create PRD) by adding an explicit successor for `00-generate-rules.md` that hands off to `06-create-prd.md` or another agreed entry point to restore continuity.【F:protocol-reference-mapping.md†L13-L61】 Prepare replacements such as:
- `@apply .cursor/ai-driven-workflow/00B-client-discovery-initiation.md` → `@apply .cursor/ai-driven-workflow/02-client-discovery-initiation.md`
- `@apply .cursor/ai-driven-workflow/15-uat-coordination.md` → `@apply .cursor/ai-driven-workflow/13-uat-coordination.md`
- Review protocols and `.cursor/ai-driven-workflow/AGENTS.md` must also be repointed to the renumbered targets.【F:protocol-reference-mapping.md†L63-L94】

### 1.3 Integration Contract Remapping
For each protocol, map the upstream/downstream dependencies documented in the integration sections to their new identifiers. Use the phase tables in the reference report as the source of truth so that every “Inputs From” and “Outputs To” bullet migrates correctly.【F:protocol-reference-mapping.md†L96-L176】 Capture these mappings in a spreadsheet to track completion and identify cascading edits.

---

## SECTION 2: File-by-File Update Instructions
1. **Rename files** according to Section 1.1 (use `git mv` so history is preserved).
2. **Search and replace inside each protocol**:
   - Update headings (e.g., `# PROTOCOL 00A` → `# PROTOCOL 01`).
   - Refresh prerequisites, inputs, outputs, and quality gate references to the new protocol numbers.
   - Adjust automation commands pointing at `.artifacts/protocol-*` directories once Section 3 is applied.
3. **Insert the missing handoff** in `00-generate-rules.md` so the sequence flows into the numbered lifecycle (recommend `@apply .cursor/ai-driven-workflow/06-create-prd.md`).
4. **Review review-protocols/** files and `.cursor/ai-driven-workflow/AGENTS.md` for embedded `@apply`, file-path, and protocol-number references.
5. **Update supporting YAML, JSON, and scripts** under `generators/` or `scripts/` if they reference the legacy names (use `rg "protocol-[0-9A-Za-z]+"` to locate).
6. **Document manual edits** in a change log so validation can trace each adjustment.

For each file, record:
- The original identifier and new identifier.
- Lines where protocol numbers changed.
- Artifacts and automation commands touched.
- Any manual rewrite of prose required to keep the narrative accurate.

---

## SECTION 3: Artifact Path Updates
- Rename evidence folders to match new protocol IDs (e.g., `.artifacts/protocol-00A/` → `.artifacts/protocol-01/`, `.artifacts/protocol-7/` → `.artifacts/protocol-09/`).
- Update shared directories used by multiple protocols:
  - `.artifacts/quality-audit/` remains but any references to Protocol 4 must align with the new identifier (12-quality-audit.md).
  - `.artifacts/scripts/` consumers need the new script governance protocol number (23).
- Adjust automation command flags so every `--output .artifacts/protocol-*` option writes to the updated location (search for `--output .artifacts/protocol` and replace systematically).
- If folder renames are performed on disk, run `git add -A` to capture directory moves before content edits.

Provide a mapping sheet linking each legacy artifact directory to its new name so teams can migrate historical evidence without ambiguity.

---

## SECTION 4: Supporting Documentation Updates
1. **AGENTS.md** – Update the protocol file list, `@apply` commands, and any numbered references in phase descriptions to the new identifiers.【F:protocol-reference-mapping.md†L178-L184】
2. **INTEGRATION-GUIDE.md** – Rewrite the sequence overview and inline file paths to match the new numbering. Confirm the phase narrative (Foundation → Closure) remains consistent.【F:protocol-reference-mapping.md†L178-L184】
3. **PROTOCOL-INTEGRATION-MAP.md** – Update every node and edge label so the map reflects the renumbered chain, including UAT, deployment, and maintenance dependencies.【F:protocol-reference-mapping.md†L178-L184】
4. **VALIDATION-GUIDE.md** – Renumber quality gates and protocol references to keep validation checklists synchronized.【F:protocol-reference-mapping.md†L178-L184】
5. **Review Protocols** – Ensure each review profile points to the correct renumbered workflow file and that inline guidance references the new IDs.【F:protocol-reference-mapping.md†L63-L94】
6. **Generators & prompts** – Inspect `generators/` and `template-packs/` for textual references (e.g., “Protocol 7” in forms) and update them to the new numbering so autogenerated material aligns.

Create a documentation diff checklist capturing each supporting asset, the sections edited, and the validation status.

---

## SECTION 5: Validation Checklist
- [ ] Run a repository-wide search (`rg "Protocol [0-9]"`) to confirm no stale protocol numbers remain.
- [ ] Execute the validation script outline (see `protocol-reference-validation-outline.md`) to verify:
  - All `@apply` directives point to existing files.
  - All artifact paths reference the new numbering.
  - Supporting docs contain updated identifiers.
- [ ] Run project automation smoke tests (lint/unit tests or `scripts/validate_*.py`) to ensure CLI arguments referencing artifact folders still succeed.
- [ ] Generate a diff report of renamed files to confirm Git history and folder structures match the target sequence.
- [ ] Compile a final cross-reference report showing old → new mappings, updated evidence folders, and validation outcomes for archival.

Once the checklist passes, prepare a PR summary referencing the updated numbering scheme and attach the mapping matrices for reviewers.
