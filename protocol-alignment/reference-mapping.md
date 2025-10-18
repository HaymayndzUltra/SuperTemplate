# Protocol Reference Mapping and Dependency Analysis

## Executive Summary
- Identified all 26 direct `@apply` handoffs across workflow and review protocols, establishing the current operational chain and surfacing two missing links (between Protocol 14 → 16 and final handoff beyond Protocol 8).【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L260-L260】【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L286-L286】【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L272-L272】
- Catalogued protocol number mentions and artifact path namespaces to scope renumbering impact across 35 markdown assets, including INTEGRATION-GUIDE, PROTOCOL-INTEGRATION-MAP, and review protocol utilities.【5e96ed†L1-L36】【fbba9c†L1-L150】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L44】
- Validated dependency flow against documented integration logic, confirming the proposed 01-27 remap aligns with prerequisites while highlighting the bootstrap → discovery → PRD insertion requirement.【F:protocol-reference-mapping.md†L12-L109】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L48】

## 1. Cross-Reference Discovery

### 1.1 `@apply` Handoff Matrix
| Source Protocol | Target Reference |
| --- | --- |
| 00a-client-proposal-generation.md | 00B-client-discovery-initiation.md【9b875e†L31-L34】 |
| 00B-client-discovery-initiation.md | 01-project-brief-creation.md【9b875e†L1-L6】 |
| 01-project-brief-creation.md | 00-project-bootstrap-and-context-engineering.md【9b875e†L8-L12】 |
| 00-project-bootstrap-and-context-engineering.md | 0-bootstrap-your-project.md【9b875e†L14-L18】 |
| 0-bootstrap-your-project.md | 00-client-discovery.md【9b875e†L36-L39】 |
| 00-client-discovery.md | 01-project-brief-creation.md【9b875e†L58-L61】 |
| 1-create-prd.md | 6-technical-design-architecture.md【9b875e†L26-L29】 |
| 6-technical-design-architecture.md | 2-generate-tasks.md【9b875e†L20-L24】 |
| 2-generate-tasks.md | 7-environment-setup-validation.md【9b875e†L64-L67】 |
| 7-environment-setup-validation.md | 3-process-tasks.md【9b875e†L48-L51】 |
| 3-process-tasks.md | 9-integration-testing.md【9b875e†L4-L7】 |
| 9-integration-testing.md | 4-quality-audit.md【9b875e†L22-L25】 |
| 4-quality-audit.md | 15-uat-coordination.md【9b875e†L16-L19】 |
| 15-uat-coordination.md | 10-pre-deployment-staging.md【9b875e†L18-L21】 |
| 10-pre-deployment-staging.md | 11-production-deployment.md【9b875e†L52-L55】 |
| 11-production-deployment.md | 12-monitoring-observability.md【9b875e†L56-L59】 |
| 12-monitoring-observability.md | 13-incident-response-rollback.md【9b875e†L10-L13】 |
| 13-incident-response-rollback.md | 14-performance-optimization.md【9b875e†L6-L9】 |
| 14-performance-optimization.md | 5-implementation-retrospective.md【9b875e†L40-L43】 |
| 16-documentation-knowledge-transfer.md | 17-project-closure.md【9b875e†L70-L73】 |
| 17-project-closure.md | 18-maintenance-support.md【9b875e†L60-L63】 |
| 18-maintenance-support.md | 5-implementation-retrospective.md【9b875e†L42-L45】 |
| 5-implementation-retrospective.md | 8-script-governance-protocol.md【9b875e†L62-L65】 |
| 8-script-governance-protocol.md | 4-quality-audit.md【9b875e†L44-L47】 |
| Review router utilities | Quality audit, architecture, process, and deployment protocols (5 references)【9b875e†L74-L87】 |

### 1.2 Protocol Number Mentions
The renumbering effort must reconcile protocol numbering strings across 34 markdown assets; counts per file extracted via `rg -o 'Protocol [0-9A-Za-z]+'` highlight high-frequency updates in INTEGRATION-GUIDE (40) and key lifecycle protocols (15–35 occurrences each).【5e96ed†L1-L36】

### 1.3 Artifact Path Patterns
Protocol artifacts follow dedicated namespaces such as `.artifacts/protocol-00A/`, `.artifacts/protocol-00B/`, `.artifacts/protocol-00/`, `.artifacts/protocol-7/`, `.artifacts/protocol-17/`, and `.artifacts/protocol-6/`, with automation scripts and evidence references tightly coupled to those directories; these require renumbered path updates in lockstep with filename changes.【fbba9c†L1-L150】

### 1.4 Supporting Documentation References
- **PROTOCOL-INTEGRATION-MAP.md** enumerates the cross-phase chain from 00a through 8, embedding numerous protocol name references that must align with the new numbering.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L48】
- **INTEGRATION-GUIDE.md** and **VALIDATION-GUIDE.md** contain 40 and 10 protocol-number references respectively, governing integration duties and validation checklists.【5e96ed†L4-L20】
- **.cursor/ai-driven-workflow/AGENTS.md** injects actionable `@apply` directives for protocols 1, 3, and 4 that must reference renumbered filenames.【9b875e†L68-L73】

## 2. Current Reference Chain Assessment
The present chain runs `00a → 00B → 01 → 00 → 0 → 00-client-discovery → 01 → 1 → 6 → 2 → 7 → 3 → 9 → 4 → 15 → 10 → 11 → 12 → 13 → 14 → 16 → 17 → 18 → 5 → 8 → 4`, looping back to the quality audit review sequence. Missing direct `@apply` transitions between Protocol 14 and the documentation phase and a terminal handoff after Protocol 8 require remediation to prevent dead ends during automation-driven execution.【9b875e†L14-L65】

## 3. Proposed Old → New Mapping
The proposed renumbering realigns 27 protocols (excluding `00-generate-rules.md`) into a consecutive 01–27 flow across foundation, planning, development, quality, deployment, and closure phases.【F:protocol-reference-mapping.md†L36-L105】 The mapping preserves logical dependencies documented in the integration map while inserting `00-client-discovery.md` between bootstrap and PRD to close the observed gap.【F:protocol-reference-mapping.md†L12-L32】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L32】

## 4. Dependency Flow Validation
Prerequisite narratives in PROTOCOL-INTEGRATION-MAP confirm the sequencing of discovery → brief → PRD → architecture → tasks → environment through deployment, documentation, and retrospective phases, matching the proposed numbering. The absence of a direct 14 → 16 handoff and reliance on retrospective loops emphasizes the need to script post-renumbering validations to catch lingering back-edges or missing prerequisites.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L20-L72】【9b875e†L40-L73】
