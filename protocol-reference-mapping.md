# Protocol Reference Mapping Analysis

## 1. Executive Summary
- The workflow currently depends on 24 direct `@apply` handoffs across primary protocols, review protocols, and automation guides, forming an incomplete chain that loops after Protocol 0 because `00-generate-rules.md` lacks a successor directive.【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L120-L122】【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L168-L175】【F:.cursor/ai-driven-workflow/00-generate-rules.md†L148-L155】
- Integration sections in every protocol enumerate explicit upstream inputs, downstream outputs, and artifact repositories, creating dense cross-dependencies that must be renumbered together with the file system to avoid breaking evidence trails.【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L114-L126】【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L108-L120】【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L139-L150】
- Supporting documentation (AGENTS, INTEGRATION-GUIDE, PROTOCOL-INTEGRATION-MAP, VALIDATION-GUIDE) embeds protocol numbers and file paths that mirror the current naming scheme, so any renumbering must propagate through these control documents to preserve orchestration guidance.【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L14-L37】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L9-L38】【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L10-L38】

## 2. Direct Handoff Matrix

### 2.1 Primary Workflow Protocols
| Source protocol file | Current `@apply` target(s) |
| --- | --- |
| 00a-client-proposal-generation.md | `.cursor/ai-driven-workflow/00B-client-discovery-initiation.md`【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L260-L260】 |
| 00B-client-discovery-initiation.md | `.cursor/ai-driven-workflow/01-project-brief-creation.md`【F:.cursor/ai-driven-workflow/00B-client-discovery-initiation.md†L268-L268】 |
| 01-project-brief-creation.md | `.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md`【F:.cursor/ai-driven-workflow/01-project-brief-creation.md†L251-L251】 |
| 00-project-bootstrap-and-context-engineering.md | `.cursor/ai-driven-workflow/0-bootstrap-your-project.md`【F:.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md†L283-L283】 |
| 0-bootstrap-your-project.md | `.cursor/ai-driven-workflow/00-client-discovery.md`【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L316-L316】 |
| 00-client-discovery.md | `.cursor/ai-driven-workflow/01-project-brief-creation.md`【F:.cursor/ai-driven-workflow/00-client-discovery.md†L290-L290】 |
| 1-create-prd.md | `.cursor/ai-driven-workflow/6-technical-design-architecture.md`【F:.cursor/ai-driven-workflow/1-create-prd.md†L263-L263】 |
| 6-technical-design-architecture.md | `.cursor/ai-driven-workflow/2-generate-tasks.md`【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L256-L256】 |
| 2-generate-tasks.md | `.cursor/ai-driven-workflow/7-environment-setup-validation.md`【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L256-L256】 |
| 7-environment-setup-validation.md | `.cursor/ai-driven-workflow/3-process-tasks.md`【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L252-L252】 |
| 3-process-tasks.md | `.cursor/ai-driven-workflow/9-integration-testing.md`【F:.cursor/ai-driven-workflow/3-process-tasks.md†L256-L256】 |
| 9-integration-testing.md | `.cursor/ai-driven-workflow/4-quality-audit.md`【F:.cursor/ai-driven-workflow/9-integration-testing.md†L260-L260】 |
| 4-quality-audit.md | `.cursor/ai-driven-workflow/15-uat-coordination.md`【F:.cursor/ai-driven-workflow/4-quality-audit.md†L286-L286】 |
| 15-uat-coordination.md | `.cursor/ai-driven-workflow/10-pre-deployment-staging.md`【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L291-L291】 |
| 10-pre-deployment-staging.md | `.cursor/ai-driven-workflow/11-production-deployment.md`【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L288-L288】 |
| 11-production-deployment.md | `.cursor/ai-driven-workflow/12-monitoring-observability.md`【F:.cursor/ai-driven-workflow/11-production-deployment.md†L292-L292】 |
| 12-monitoring-observability.md | `.cursor/ai-driven-workflow/13-incident-response-rollback.md`【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L287-L287】 |
| 13-incident-response-rollback.md | `.cursor/ai-driven-workflow/14-performance-optimization.md`【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L293-L293】 |
| 14-performance-optimization.md | `.cursor/ai-driven-workflow/5-implementation-retrospective.md`【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L286-L286】 |
| 16-documentation-knowledge-transfer.md | `.cursor/ai-driven-workflow/17-project-closure.md`【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L293-L293】 |
| 17-project-closure.md | `.cursor/ai-driven-workflow/18-maintenance-support.md`【F:.cursor/ai-driven-workflow/17-project-closure.md†L263-L263】 |
| 18-maintenance-support.md | `.cursor/ai-driven-workflow/5-implementation-retrospective.md`【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L268-L268】 |
| 5-implementation-retrospective.md | `.cursor/ai-driven-workflow/8-script-governance-protocol.md`【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L262-L262】 |
| 8-script-governance-protocol.md | `.cursor/ai-driven-workflow/4-quality-audit.md`【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L272-L272】 |

`00-generate-rules.md` terminates with `--- End Command ---` and does not define a successor, breaking the numeric flow after Protocol 0.【F:.cursor/ai-driven-workflow/00-generate-rules.md†L148-L155】

### 2.2 Review & Control Assets
| Source file | Current `@apply` target(s) |
| --- | --- |
| review-protocols/README.md | ``.cursor/ai-driven-workflow/4-quality-audit.md --mode [quick&#124;security&#124;architecture&#124;design&#124;ui&#124;deep-security&#124;comprehensive]``【F:.cursor/ai-driven-workflow/review-protocols/README.md†L73-L73】 |
| review-protocols/architecture-review.md | `.cursor/ai-driven-workflow/6-technical-design-architecture.md`【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L258-L258】 |
| review-protocols/code-review.md | `.cursor/ai-driven-workflow/3-process-tasks.md`【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L257-L257】 |
| review-protocols/security-check.md | `.cursor/ai-driven-workflow/11-production-deployment.md`【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L262-L262】 |
| review-protocols/utils/_review-router.md | `.cursor/ai-driven-workflow/4-quality-audit.md --mode security`【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L179-L179】 |
| .cursor/ai-driven-workflow/AGENTS.md | `.cursor/ai-driven-workflow/1-create-prd.md`, `.cursor/ai-driven-workflow/3-process-tasks.md @codebase`, `.cursor/ai-driven-workflow/4-quality-audit.md --mode comprehensive`【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】 |

## 3. Protocol Reference Inventory

### 3.1 Phase 0 — Foundation & Discovery
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 00a-client-proposal-generation.md | Protocol 00 `JOB-POST.md`; Protocol 00B `discovery-brief.md`【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L116-L118】 | Protocol 00B `PROPOSAL.md`; Protocol 01 `proposal-summary.json`【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L120-L122】 | `.artifacts/protocol-00A/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L124-L126】 |
| 00B-client-discovery-initiation.md | Protocol 00A proposal assets; Protocol 00 intake log【F:.cursor/ai-driven-workflow/00B-client-discovery-initiation.md†L122-L124】 | Protocol 01 discovery deliverables; Protocol 00 collaboration assets【F:.cursor/ai-driven-workflow/00B-client-discovery-initiation.md†L126-L128】 | `.artifacts/protocol-00B/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/00B-client-discovery-initiation.md†L130-L132】 |
| 01-project-brief-creation.md | Protocol 00A proposal package; Protocol 00B discovery bundle【F:.cursor/ai-driven-workflow/01-project-brief-creation.md†L115-L116】 | Protocol 00 context updates; Protocol 06 technical baseline【F:.cursor/ai-driven-workflow/01-project-brief-creation.md†L118-L120】 | `.artifacts/protocol-01/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/01-project-brief-creation.md†L122-L124】 |
| 00-project-bootstrap-and-context-engineering.md | Protocol 01 brief approvals【F:.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md†L138-L139】 | Protocol 0 governance kit; Protocol 02 technical baseline【F:.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md†L141-L143】 | `.artifacts/protocol-00/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md†L145-L147】 |
| 0-bootstrap-your-project.md | Protocol 00 governance status; Protocol 01 brief reference【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L169-L171】 | Protocol 2 context kit; Protocol 8 rule audit【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L173-L175】 | `.artifacts/protocol-0/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L177-L179】 |
| 00-client-discovery.md | Protocol 0 governance inputs; Protocol 00A proposal data【F:.cursor/ai-driven-workflow/00-client-discovery.md†L143-L145】 | Protocol 01 discovery brief; Protocol 1 traceability package【F:.cursor/ai-driven-workflow/00-client-discovery.md†L147-L149】 | `.artifacts/protocol-00-CD/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/00-client-discovery.md†L151-L153】 |

### 3.2 Phase 1-2 — Planning & Design
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 1-create-prd.md | Protocol 00 discovery evidence; Protocol 01 brief assets; Protocol 6 design seeds【F:.cursor/ai-driven-workflow/1-create-prd.md†L123-L130】 | Protocol 2 task inputs; Protocol 6 technical packages【F:.cursor/ai-driven-workflow/1-create-prd.md†L132-L137】 | `.artifacts/protocol-1/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/1-create-prd.md†L139-L141】 |
| 6-technical-design-architecture.md | Protocol 01 brief; Protocol 1 PRD; Protocol 00-CD risk set【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L108-L112】 | Protocol 2 planning package; Protocol 7 environment prerequisites【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L114-L116】 | `.artifacts/protocol-6/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L118-L120】 |
| 2-generate-tasks.md | Protocol 1 PRD artifacts; Protocol 6 design deliverables; Protocol 00 context kit【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L109-L114】 | Protocol 7 environment inputs; Protocol 3 execution bundle【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L116-L119】 | `.artifacts/protocol-2/`, `.cursor/tasks/` manifests【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L121-L123】 |
| 7-environment-setup-validation.md | Protocol 6 design baseline; Protocol 2 task automation; Protocol 00 governance data【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L105-L109】 | Protocol 3 environment package; Protocol 11 deployment readiness【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L111-L113】 | `.artifacts/protocol-7/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L115-L117】 |

### 3.3 Phase 3 — Development Execution
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 3-process-tasks.md | Protocol 2 task manifests; Protocol 7 environment readiness; Protocol 4 audit hooks【F:.cursor/ai-driven-workflow/3-process-tasks.md†L109-L116】 | Protocol 9 integration evidence; Protocol 4 quality hooks; Protocol 5 retrospectives【F:.cursor/ai-driven-workflow/3-process-tasks.md†L118-L121】 | `.artifacts/protocol-3/`, `.cursor/tasks/` updates【F:.cursor/ai-driven-workflow/3-process-tasks.md†L123-L124】 |
| 9-integration-testing.md | Protocol 3 execution artifacts; Protocol 6 design contracts; Protocol 7 environment diagnostics【F:.cursor/ai-driven-workflow/9-integration-testing.md†L106-L110】 | Protocol 4 audit package; Protocol 10 staging intake; Protocol 12 monitoring recommendations【F:.cursor/ai-driven-workflow/9-integration-testing.md†L112-L115】 | `.artifacts/protocol-9/`, `.cursor/context-kit/` integration notes【F:.cursor/ai-driven-workflow/9-integration-testing.md†L117-L119】 |

### 3.4 Phase 4 — Quality, Staging & UAT
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 4-quality-audit.md | Protocols 3, 8, 9, 10 evidence pipelines【F:.cursor/ai-driven-workflow/4-quality-audit.md†L136-L140】 | Protocols 15, 10, 5, 8 quality packages【F:.cursor/ai-driven-workflow/4-quality-audit.md†L142-L146】 | `.artifacts/quality-audit/`, `.cursor/context-kit/`【F:.cursor/ai-driven-workflow/4-quality-audit.md†L148-L150】 |
| 15-uat-coordination.md | Protocol 4 audit approvals; Protocol 9 integration logs; Protocol 10 staging report; Protocol 1 acceptance criteria【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L140-L148】 | Protocol 10 readiness confirmation; Protocol 16 documentation package; Protocol 5 retrospective inputs【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L150-L155】 | `.artifacts/protocol-15/`, `.cursor/context-kit/` UAT trackers【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L157-L159】 |
| 10-pre-deployment-staging.md | Protocol 9 integration results; Protocol 4 audit sign-offs; Protocol 15 UAT status【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L137-L143】 | Protocol 11 deployment gate package; Protocol 4 readiness updates; Protocol 5 retrospective data【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L145-L149】 | `.artifacts/protocol-10/`, `.cursor/context-kit/` staging manifests【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L151-L153】 |

### 3.5 Phase 5 — Deployment & Operations
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 11-production-deployment.md | Protocol 10 staging sign-off; Protocol 7 environment approvals; Protocol 4 audit evidence【F:.cursor/ai-driven-workflow/11-production-deployment.md†L145-L152】 | Protocol 12 monitoring baseline; Protocol 13 incident playbooks; Protocol 5 retrospective data【F:.cursor/ai-driven-workflow/11-production-deployment.md†L154-L160】 | `.artifacts/protocol-11/`, `.cursor/context-kit/` release logs【F:.cursor/ai-driven-workflow/11-production-deployment.md†L162-L164】 |
| 12-monitoring-observability.md | Protocol 11 deployment records; Protocol 4/9 quality data; Protocol 8 automation classes【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L141-L147】 | Protocol 13 incident readiness; Protocol 14 tuning backlog; Protocol 5 retrospective feed【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L149-L155】 | `.artifacts/protocol-12/`, `.cursor/context-kit/` telemetry configs【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L157-L159】 |
| 13-incident-response-rollback.md | Protocol 12 monitoring alerts; Protocol 11 deployment notes; Protocol 4 audit controls【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L143-L149】 | Protocol 14 performance backlog; Protocol 5 retrospective actions; Protocol 18 maintenance prep【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L151-L155】 | `.artifacts/protocol-13/`, `.cursor/context-kit/` incident ledgers【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L157-L159】 |
| 14-performance-optimization.md | Protocol 12 telemetry baselines; Protocol 13 incident findings; Protocol 11 deployment logs【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L139-L145】 | Protocol 5 retrospective lessons; Protocol 16 documentation updates; Protocol 18 maintenance guardrails【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L146-L150】 | `.artifacts/protocol-14/`, `.cursor/context-kit/` tuning data【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L152-L154】 |

### 3.6 Phase 6 — Knowledge Transfer, Closure & Maintenance
| Protocol | Upstream dependencies | Downstream outputs | Artifact repositories |
| --- | --- | --- | --- |
| 16-documentation-knowledge-transfer.md | Protocols 1, 6, 9, 11–14, 15 evidence sets【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L146-L152】 | Protocol 17 handover manifest; Protocol 18 improvement backlog; Organizational knowledge bases【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L154-L160】 | `.artifacts/protocol-16/`, `.cursor/context-kit/` knowledge assets【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L162-L167】 |
| 17-project-closure.md | Protocol 16 documentation package; Protocol 15 UAT sign-off; Protocol 11–14 operational records【F:.cursor/ai-driven-workflow/17-project-closure.md†L122-L128】 | Protocol 18 maintenance backlog; Finance/PMO systems【F:.cursor/ai-driven-workflow/17-project-closure.md†L130-L132】 | `.artifacts/protocol-17/`, `.cursor/context-kit/` closure archives【F:.cursor/ai-driven-workflow/17-project-closure.md†L134-L136】 |
| 18-maintenance-support.md | Protocol 17 handover manifest; Protocol 14 performance notes; Protocol 12 monitoring data【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L126-L133】 | Protocol 5 retrospective feed; Support coverage plans; Automation opportunities for Protocol 8【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L135-L141】 | `.artifacts/protocol-18/`, `.cursor/context-kit/` operations ledger【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L142-L151】 |
| 5-implementation-retrospective.md | Protocols 18, 17, 16, 14, 13, 4, 15, 3 evidence sets【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L120-L128】 | Protocol 8 automation backlog; Protocol 1 PRD updates; Continuous improvement register【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L130-L133】 | `.artifacts/protocol-5/`, `.cursor/context-kit/` retrospectives【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L135-L137】 |
| 8-script-governance-protocol.md | Protocol 4 audit summary; Protocol 3 automation tracker【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L122-L124】 | Protocols 4, 5, 12 compliance outputs【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L126-L129】 | `.artifacts/scripts/`, `.cursor/context-kit/` automation context【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L131-L133】 |

## 4. Supporting Documentation Cross-References
- **AGENTS.md** triggers workflow handoffs by loading Protocols 1, 3, and 4 as reusable commands, reinforcing the numbering scheme for automation entry points.【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】
- **INTEGRATION-GUIDE.md** cites Protocols 00 through 5 in canonical order with embedded file paths, mirroring the existing naming convention across bootstrap-to-retrospective flows.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L14-L37】
- **PROTOCOL-INTEGRATION-MAP.md** documents downstream dependencies spanning Protocols 6–18, confirming the multi-phase relay that must be renumbered consistently.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L9-L38】
- **VALIDATION-GUIDE.md** references Protocols 0–5 when describing gate enforcement, binding quality controls to the current identifiers.【F:.cursor/ai-driven-workflow/VALIDATION-GUIDE.md†L10-L38】

## 5. Artifact Path Patterns
- Every protocol stores evidence inside a dedicated `.artifacts/protocol-*` namespace that matches its current numeric identifier, such as `.artifacts/protocol-00A/` for Protocol 00A and `.artifacts/protocol-7/` for environment validation.【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L36-L105】【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L101-L118】
- Quality governance assets reuse shared directories like `.artifacts/quality-audit/` and `.artifacts/scripts/`, tying review infrastructure to Protocol 4 and Protocol 8 naming conventions.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L148-L150】【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L131-L133】
- Automation commands in multiple protocols reference scripts that emit evidence into their protocol-specific folders (e.g., `python scripts/validate_prd_gate.py --output .artifacts/protocol-1/prd-validation.json`).【F:.cursor/ai-driven-workflow/1-create-prd.md†L106-L115】

## 6. Risk Overview by Reference Type
- **Direct `@apply` directives:** Misaligned renumbering will sever phase transitions; e.g., Protocol 4 currently hands off to Protocol 15 for UAT entry, so the new numbering must preserve this dependency.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L286-L286】
- **Integration dependencies:** Each protocol enumerates specific upstream/downstream contracts; incorrect renumbering could orphan required evidence flows such as Protocol 6 feeding Protocol 2’s task generation inputs.【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L114-L116】
- **Artifact paths:** Scripts and manual steps rely on deterministic folder names; failing to update directories like `.artifacts/protocol-18/` would break maintenance validation automation.【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L90-L108】
- **Supporting guides:** Control documents direct agents to specific protocol identifiers; leaving them stale would misconfigure orchestrator commands and integration testing playbooks.【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L9-L38】
