# Comprehensive Protocol Renumbering Prompt

Use this prompt when executing the renumbering effort so all protocol references, artifacts, and documentation stay aligned.

---

## Section 1: Reference Mapping Matrix

### A. Old → New Filename Mapping (27 protocols)
| Current Filename | Proposed Filename |
| --- | --- |
| 00a-client-proposal-generation.md | 01-client-proposal-generation.md |
| 00B-client-discovery-initiation.md | 02-client-discovery-initiation.md |
| 01-project-brief-creation.md | 03-project-brief-creation.md |
| 00-project-bootstrap-and-context-engineering.md | 04-project-bootstrap-and-context-engineering.md |
| 0-bootstrap-your-project.md | 05-bootstrap-your-project.md |
| 00-client-discovery.md | 24-client-discovery.md |
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
| INTEGRATION-GUIDE.md | 26-integration-guide.md |
| VALIDATION-GUIDE.md | 27-validation-guide.md |
| PROTOCOL-INTEGRATION-MAP.md | 25-protocol-integration-map.md |

> Exclude `00-generate-rules.md` from renumbering; keep or sunset per governance decision.

### B. Reference Types to Update
1. `@apply .cursor/ai-driven-workflow/{filename}.md`
2. `Protocol X` textual mentions (numbers, alphanumeric variants)
3. Artifact paths `.artifacts/protocol-{id}/`
4. Integration prerequisites/outputs referencing numbered protocols
5. Review protocol references (README, utilities, code-review, architecture-review, security-check)
6. Supporting AGENTS instructions and system READMEs

### C. Artifact Path Transformation Rules
- Rename directories `.artifacts/protocol-XX` to new numeric identifiers, matching filename updates.
- Update automation commands, evidence tables, and manual validation notes referencing renamed directories.
- Ensure zipped or aggregated outputs (e.g., `aggregate_evidence_XX.py`) point to new protocol IDs.

---

## Section 2: File-by-File Update Instructions
For each file, apply the following adjustments. Preserve headings and descriptive language while updating numeric references.

1. **00a-client-proposal-generation.md → 01-client-proposal-generation.md**
   - Rename file and update self-references, evidence tables, and automation commands.
   - Update downstream mentions pointing to 00B.
2. **00B-client-discovery-initiation.md → 02-client-discovery-initiation.md**
   - Rename file and adjust references to 00A/01.
   - Update artifact namespace to `.artifacts/protocol-02/` and related scripts.
3. **01-project-brief-creation.md → 03-project-brief-creation.md**
   - Update prerequisites referencing 00B/00A/00-CD.
   - Refresh evidence tables and automation hooks with new IDs.
4. **00-project-bootstrap-and-context-engineering.md → 04-project-bootstrap-and-context-engineering.md**
   - Align automation commands (`validate_brief`, `doctor`, etc.) to `.artifacts/protocol-04/`.
   - Ensure integration references to PRD (now 06) and discovery (24) are consistent.
5. **0-bootstrap-your-project.md → 05-bootstrap-your-project.md**
   - Update prerequisites to call Protocol 24.
   - Refresh handoff references to Protocol 06.
6. **00-client-discovery.md → 24-client-discovery.md**
   - Align intake artifacts, evidence tables, and automation commands to `.artifacts/protocol-24/`.
   - Update cross-references pointing to Protocols 03 and 06.
7. **1-create-prd.md → 06-create-prd.md**
   - Update prerequisites pointing to Protocols 01/02/24.
   - Align evidence outputs consumed by Protocol 07.
8. **6-technical-design-architecture.md → 07-technical-design-architecture.md**
   - Update references to PRD (06) and downstream tasks (08) and environment (09).
   - Adjust automation filenames and artifact paths.
9. **2-generate-tasks.md → 08-generate-tasks.md**
   - Update prerequisites to reference 07.
   - Align evidence, automation scripts, and handoff to 09.
10. **7-environment-setup-validation.md → 09-environment-setup-validation.md**
    - Update evidence tables referencing protocols 10 and 11.
    - Align automation script names and manual validation logs.
11. **3-process-tasks.md → 10-process-tasks.md**
    - Update prerequisites pointing to 09 and outputs to 11.
    - Adjust integration notes in review protocols.
12. **9-integration-testing.md → 11-integration-testing.md**
    - Update references from Protocol 10 and to Protocol 12.
    - Align evidence tables and automation script calls.
13. **4-quality-audit.md → 12-quality-audit.md**
    - Update review router references and integration to Protocol 13.
    - Align quality gate descriptions and artifacts.
14. **15-uat-coordination.md → 13-uat-coordination.md**
    - Update prerequisites from 12 and outputs to 14.
    - Align communication matrices and automation tasks.
15. **10-pre-deployment-staging.md → 14-pre-deployment-staging.md**
    - Update inbound references from 13 and outbound to 15.
    - Align automation commands and artifact directories.
16. **11-production-deployment.md → 15-production-deployment.md**
    - Update inbound/outbound references (14 → 15 → 16).
    - Sync review protocol security-check references.
17. **12-monitoring-observability.md → 16-monitoring-observability.md**
    - Align dependencies from 15 and outputs to 17.
    - Update evidence checklists and automation.
18. **13-incident-response-rollback.md → 17-incident-response-rollback.md**
    - Update inbound/outbound references (16 → 17 → 18).
    - Sync artifact directories and runbook references.
19. **14-performance-optimization.md → 18-performance-optimization.md**
    - Update handoffs to 19 (documentation) rather than legacy 5 loop.
    - Adjust evidence requirements referencing retrospective.
20. **16-documentation-knowledge-transfer.md → 19-documentation-knowledge-transfer.md**
    - Update inbound from 18 and outbound to 20.
    - Align documentation packages and automation scripts.
21. **17-project-closure.md → 20-project-closure.md**
    - Update inbound from 19 and outbound to 21.
    - Sync governance references and evidence manifests.
22. **18-maintenance-support.md → 21-maintenance-support.md**
    - Update inbound from 20 and outbound to 22.
    - Align maintenance schedules and artifact paths.
23. **5-implementation-retrospective.md → 22-implementation-retrospective.md**
    - Update inbound from 21 and outbound to 23.
    - Align scenario references and evidence logs.
24. **8-script-governance-protocol.md → 23-script-governance-protocol.md**
    - Update inbound from 22 and outbound loops.
    - Align review router instructions.
25. **review-protocols/**/* (README, code-review, architecture-review, security-check, utils)**
    - Update `@apply` targets, embedded protocol numbers, and narrative references.
26. **PROTOCOL-INTEGRATION-MAP.md → 25-protocol-integration-map.md**
    - Update flow diagrams, lists, and evidence narratives.
27. **INTEGRATION-GUIDE.md → 26-integration-guide.md**
    - Update all protocol numbering, automation commands, and gating diagrams.
28. **VALIDATION-GUIDE.md → 27-validation-guide.md**
    - Align validation steps and cross-references.
29. **Root-level AGENTS.md and .cursor/ai-driven-workflow/AGENTS.md**
    - Update protocol listings, scope descriptions, and `@apply` commands.
30. **README.md, protocol-system-evaluation-prompt.md, protocol-reference-mapping.md**
    - Update enumerated sequences, scoring matrices, and mapping references.
31. **Scripts referencing `.artifacts/protocol-XX/` directories**
    - Rename script arguments and output paths after directory renaming.
32. **CI/CD or automation configs**
    - Update references within YAML/JSON if protocol IDs are embedded.

---

## Section 3: Artifact Path Updates
1. Rename `.artifacts/protocol-00A/` → `.artifacts/protocol-01/` and propagate to automation scripts.
2. Repeat renaming for every protocol namespace, preserving alphabetical suffixes when necessary (e.g., 00B → 02).
3. Update evidence tables to reference new directories and filenames.
4. Update automation snippets within protocols (inline code blocks) to call renamed directories.
5. Verify aggregated outputs (`aggregate_evidence_XX.py`) match the new numbering and regenerate scripts as required.
6. Adjust zipped package names (e.g., `CLOSURE-PACKAGE.zip`) if numbering is encoded in metadata files.

---

## Section 4: Supporting Documentation Updates
- **INTEGRATION-GUIDE.md**: Update sequence diagrams, integration responsibilities, quality gates, and automation checklists.
- **PROTOCOL-INTEGRATION-MAP.md**: Rewrite protocol lists, flow charts, and evidence mappings using new IDs.
- **Root & workflow AGENTS.md**: Align instructions, checklists, and scenario guidance to new numbering.
- **README.md & protocol-system-evaluation-prompt.md**: Refresh high-level sequence descriptions, scoring guidance, and scenario flow references.
- **Review protocols**: Update onboarding instructions, review router definitions, and example commands.
- **Scripts & checklists**: Adjust references within automation instructions and manual checklists.

---

## Section 5: Validation Checklist
- [ ] All filenames renamed to new numbering scheme.
- [ ] Every `@apply` directive resolves to the updated filenames.
- [ ] All textual "Protocol X" mentions reflect new numbering across markdown assets.
- [ ] Artifact directories and associated automation commands reference the new protocol IDs.
- [ ] Supporting documentation (guides, AGENTS, README) updated to the new sequence.
- [ ] Review protocol utilities reference correct targets.
- [ ] Scripts and CI/CD references updated for renamed directories.
- [ ] Automated validation scripts executed successfully (see validation outline).
- [ ] Manual spot checks performed on high-risk protocols (former 00a, 4, 14, 5).

Use this prompt as the authoritative checklist while executing the renumbering migration.
