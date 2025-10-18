# Comprehensive Protocol Renumbering Adjustment Prompt

## Overview
The AI-driven workflow currently relies on 29 `@apply` directives, 610 textual protocol mentions, 484 artifact-path references, and 47 embedded filename links, all of which must transition coherently when the protocols are renumbered to a sequential `01-27` scheme.【F:documentation/protocol-reference-summary.json†L2-L5】 This prompt orchestrates the renumbering effort so that handoffs, evidence directories, and supporting documentation remain consistent throughout the lifecycle.【F:documentation/protocol-reference-mapping.md†L5-L114】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L92】

---

## SECTION 1: Reference Mapping Matrix

### 1.1 Old → New Filename Mapping
Use the following canonical mapping for all file renames and cross-reference updates.【F:protocol-reference-mapping.md†L117-L156】

| Legacy File | Sequential Target |
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
| INTEGRATION-GUIDE.md | 26-integration-guide.md |
| VALIDATION-GUIDE.md | 27-validation-guide.md |

### 1.2 Handoff Dependencies
Each protocol exposes a single `@apply` handoff pointing to its successor; update these references immediately after renaming to prevent cursor automation from breaking.【F:documentation/protocol-reference-data.json†L2-L354】

### 1.3 Artifact Path Transformations
Renumber `.artifacts/protocol-N/` directories in parallel with file renames to preserve automation outputs and validation records.【F:documentation/protocol-reference-mapping.md†L88-L114】

| Legacy File | New File | Artifact Update |
| --- | --- | --- |
| 00a-client-proposal-generation.md | 01-client-proposal-generation.md | `.artifacts/protocol-00/` → `.artifacts/protocol-01/` |
| 00B-client-discovery-initiation.md | 02-client-discovery-initiation.md | `.artifacts/protocol-00/` → `.artifacts/protocol-02/` |
| 01-project-brief-creation.md | 03-project-brief-creation.md | `.artifacts/protocol-01/` → `.artifacts/protocol-03/` |
| 00-project-bootstrap-and-context-engineering.md | 04-project-bootstrap-and-context-engineering.md | `.artifacts/protocol-00/` → `.artifacts/protocol-04/` |
| 0-bootstrap-your-project.md | 05-bootstrap-your-project.md | `.artifacts/protocol-0/` → `.artifacts/protocol-05/` |
| 1-create-prd.md | 06-create-prd.md | `.artifacts/protocol-1/` → `.artifacts/protocol-06/` |
| 6-technical-design-architecture.md | 07-technical-design-architecture.md | `.artifacts/protocol-6/` → `.artifacts/protocol-07/` |
| 2-generate-tasks.md | 08-generate-tasks.md | `.artifacts/protocol-2/` → `.artifacts/protocol-08/` |
| 7-environment-setup-validation.md | 09-environment-setup-validation.md | `.artifacts/protocol-7/` → `.artifacts/protocol-09/` |
| 3-process-tasks.md | 10-process-tasks.md | `.artifacts/protocol-3/` → `.artifacts/protocol-10/` |
| 9-integration-testing.md | 11-integration-testing.md | `.artifacts/protocol-9/` → `.artifacts/protocol-11/` |
| 4-quality-audit.md | 12-quality-audit.md | `.artifacts/protocol-4/` → `.artifacts/protocol-12/` |
| 15-uat-coordination.md | 13-uat-coordination.md | `.artifacts/protocol-15/` → `.artifacts/protocol-13/` |
| 10-pre-deployment-staging.md | 14-pre-deployment-staging.md | `.artifacts/protocol-10/` → `.artifacts/protocol-14/` |
| 11-production-deployment.md | 15-production-deployment.md | `.artifacts/protocol-11/` → `.artifacts/protocol-15/` |
| 12-monitoring-observability.md | 16-monitoring-observability.md | `.artifacts/protocol-12/` → `.artifacts/protocol-16/` |
| 13-incident-response-rollback.md | 17-incident-response-rollback.md | `.artifacts/protocol-13/` → `.artifacts/protocol-17/` |
| 14-performance-optimization.md | 18-performance-optimization.md | `.artifacts/protocol-14/` → `.artifacts/protocol-18/` |
| 16-documentation-knowledge-transfer.md | 19-documentation-knowledge-transfer.md | `.artifacts/protocol-16/` → `.artifacts/protocol-19/` |
| 17-project-closure.md | 20-project-closure.md | `.artifacts/protocol-17/` → `.artifacts/protocol-20/` |
| 18-maintenance-support.md | 21-maintenance-support.md | `.artifacts/protocol-18/` → `.artifacts/protocol-21/` |
| 5-implementation-retrospective.md | 22-implementation-retrospective.md | `.artifacts/protocol-5/` → `.artifacts/protocol-22/` |
| 8-script-governance-protocol.md | 23-script-governance-protocol.md | `.artifacts/protocol-8/` → `.artifacts/protocol-23/` |
| 00-client-discovery.md | 24-client-discovery.md | `.artifacts/protocol-00/` → `.artifacts/protocol-24/` |

---

## SECTION 2: File-by-File Update Instructions
Perform the following steps sequentially for each protocol.

1. **Rename the file** according to the mapping table in Section 1.1.
2. **Update the trailing `@apply` handoff** to point at the new filename for the downstream protocol.【F:documentation/protocol-reference-data.json†L2-L226】
3. **Search within the file** for textual mentions such as “Protocol 6” or `.cursor/ai-driven-workflow/*.md` references and adjust them to the new numbering scheme.【F:documentation/protocol-reference-data.json†L2-L226】
4. **Rewrite artifact paths** under `.artifacts/protocol-N/` to the new numeric identifier from Section 1.3.【F:documentation/protocol-reference-mapping.md†L88-L114】
5. **Revalidate prerequisites and integration sections** to ensure they reference the correct upstream/downstream protocols described in `PROTOCOL-INTEGRATION-MAP.md`.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L92】

> **Tip:** Perform the renumbering in dependency order (foundation → closure) to minimise merge conflicts and to keep the automation chain operational during the migration.【F:documentation/protocol-reference-mapping.md†L64-L86】

---

## SECTION 3: Artifact & Script Updates

1. **Directory renames** – Rename or recreate artifact folders under `.artifacts/` to match the new numbering before running any automation hooks.
2. **Script arguments** – Update all automation commands (e.g., `python scripts/*.py --output .artifacts/protocol-3/...`) embedded in protocols so that the output points to the new directory names.【F:documentation/protocol-reference-data.json†L2-L226】
3. **CI/CD workflows** – Review any external scripts or pipelines that hardcode `.artifacts/protocol-N/` and update them to match the sequential numbering.
4. **Manifest files** – Regenerate artifact manifests or manifests referenced in protocols after the rename to prevent stale references.

---

## SECTION 4: Supporting Documentation Updates

Target the ancillary documents that embed filename references or protocol numbers.

- **INTEGRATION-GUIDE.md** – Update location call-outs (`.cursor/ai-driven-workflow/<file>.md`) and narrative protocol numbers throughout the guide.【F:documentation/protocol-reference-data.json†L226-L244】
- **PROTOCOL-INTEGRATION-MAP.md** – Rewrite sequence lists and dependency annotations to reflect the new numbering.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L92】
- **VALIDATION-GUIDE.md** – Align quality gate numbering and checklists with the updated protocol IDs.【F:documentation/protocol-reference-data.json†L312-L320】
- **Review protocols** – Adjust `@apply` directives and embedded references inside `review-protocols/*` (especially quality, architecture, code, and security reviews).【F:documentation/protocol-reference-data.json†L244-L354】
- **Top-level README / AGENTS** – Refresh overview diagrams or bullet lists that describe the protocol order so they match the sequential numbering.【F:documentation/protocol-reference-mapping.md†L5-L86】

---

## SECTION 5: Validation Checklist
Use this checklist after executing the renumbering to guarantee alignment.

- [ ] All protocol files renamed according to Section 1.1
- [ ] Every `@apply` directive points to the new sequential filenames
- [ ] `.artifacts/protocol-*` references updated across all protocols and scripts
- [ ] Textual “Protocol X” mentions reflect the new numbering
- [ ] Supporting documentation (integration, validation, reviews, AGENTS/README) refreshed
- [ ] Automated validation script executed with zero failed checks (see validation outline deliverable)
- [ ] Spot-check evidence manifests to confirm outputs land in the correct directories

---

**Execution Note:** Run the validation script outline provided in `documentation/protocol-reference-validation-outline.md` after completing the renumbering. Address any reported discrepancies before finalising the branch.
