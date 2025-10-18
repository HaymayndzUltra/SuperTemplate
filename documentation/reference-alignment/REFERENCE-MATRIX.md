# Protocol Reference Matrix & Evidence Summary

## 1. Direct `@apply` Handoffs
The following table captures every explicit protocol handoff discovered in the current workflow implementation. Rows are sorted in execution order where possible, and missing or cyclical jumps are noted for remediation.

| Source protocol file | Target referenced by `@apply` | Notes |
| --- | --- | --- |
| 00a-client-proposal-generation.md | 00B-client-discovery-initiation.md | Formal handoff from proposal creation to discovery initiation.【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L250-L261】 |
| 00B-client-discovery-initiation.md | 01-project-brief-creation.md | Discovery initiation continues to the initial brief protocol.【F:.cursor/ai-driven-workflow/00B-client-discovery-initiation.md†L260-L269】 |
| 01-project-brief-creation.md | 00-project-bootstrap-and-context-engineering.md | Redirect loops back into bootstrap/context engineering rather than progressing to PRD.【F:.cursor/ai-driven-workflow/01-project-brief-creation.md†L245-L252】 |
| 00-project-bootstrap-and-context-engineering.md | 0-bootstrap-your-project.md | Chains foundation work into the bootstrap protocol.【F:.cursor/ai-driven-workflow/00-project-bootstrap-and-context-engineering.md†L275-L284】 |
| 0-bootstrap-your-project.md | 00-client-discovery.md | Handoff to the dedicated client discovery protocol, creating an extra branch before PRD creation.【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L304-L318】 |
| 00-client-discovery.md | 01-project-brief-creation.md | Returns to the brief protocol, creating the observed loop in the current chain.【F:.cursor/ai-driven-workflow/00-client-discovery.md†L282-L291】 |
| 1-create-prd.md | 6-technical-design-architecture.md | Primary transition from PRD to architecture design.【F:.cursor/ai-driven-workflow/1-create-prd.md†L255-L264】 |
| 6-technical-design-architecture.md | 2-generate-tasks.md | Architecture protocol launches downstream task generation.【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L248-L257】 |
| 2-generate-tasks.md | 7-environment-setup-validation.md | Task protocol flows into environment validation.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L248-L257】 |
| 7-environment-setup-validation.md | 3-process-tasks.md | Environment validation hands execution off to task processing.【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L244-L253】 |
| 3-process-tasks.md | 9-integration-testing.md | Execution protocol launches integration testing.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L246-L257】 |
| 9-integration-testing.md | 4-quality-audit.md | Integration testing defers to central quality audit protocol.【F:.cursor/ai-driven-workflow/9-integration-testing.md†L252-L261】 |
| 4-quality-audit.md | 15-uat-coordination.md | Quality audit triggers UAT coordination, aligning with proposed renumbering path.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L278-L287】 |
| 15-uat-coordination.md | 10-pre-deployment-staging.md | UAT transitions to staging preparations.【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L283-L292】 |
| 10-pre-deployment-staging.md | 11-production-deployment.md | Staging directly launches production deployment.【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L280-L289】 |
| 11-production-deployment.md | 12-monitoring-observability.md | Production to monitoring chain maintained.【F:.cursor/ai-driven-workflow/11-production-deployment.md†L284-L293】 |
| 12-monitoring-observability.md | 13-incident-response-rollback.md | Monitoring leads into incident response and rollback protocol.【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L279-L288】 |
| 13-incident-response-rollback.md | 14-performance-optimization.md | Incident workflow currently points to performance optimization.【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L285-L294】 |
| 14-performance-optimization.md | 5-implementation-retrospective.md | Performance optimization loops back to retrospective instead of documentation.【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L278-L287】 |
| 16-documentation-knowledge-transfer.md | 17-project-closure.md | Documentation protocol flows into project closure.【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L285-L294】 |
| 17-project-closure.md | 18-maintenance-support.md | Closure protocol hands off to maintenance support.【F:.cursor/ai-driven-workflow/17-project-closure.md†L255-L264】 |
| 18-maintenance-support.md | 5-implementation-retrospective.md | Maintenance currently loops back to retrospective, skipping the governance protocol in sequence.【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L260-L269】 |
| 5-implementation-retrospective.md | 8-script-governance-protocol.md | Retrospective directs into the governance protocol.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L254-L263】 |
| 8-script-governance-protocol.md | 4-quality-audit.md | Governance protocol circles back into quality audit, forming a governance-quality loop.【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L264-L273】 |

### Additional operational references
| File | Target | Context |
| --- | --- | --- |
| PROTOCOL-INTEGRATION-MAP.md | Multiple sequential mappings | Authoritative documentation for intended end-to-end flow, including proposed but not yet implemented handoffs such as 14 → 16 and 5 → 8.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】 |
| INTEGRATION-GUIDE.md | Protocol 00 → 5 | Automation architecture references legacy numbering across pipeline scripts.【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】 |
| AGENTS.md | Protocols 1, 3, 4 | Embedded Cursor shortcuts that invoke downstream protocols directly.【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】 |
| review-protocols/README.md | 4-quality-audit.md | Review router supports multiple quality audit modes via `@apply` directive.【F:.cursor/ai-driven-workflow/review-protocols/README.md†L63-L79】 |
| review-protocols/code-review.md | 3-process-tasks.md | Code review completion triggers the execution protocol for integration work.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L246-L259】 |
| review-protocols/architecture-review.md | 6-technical-design-architecture.md | Architecture review escalates into the design protocol.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L248-L261】 |
| review-protocols/security-check.md | 11-production-deployment.md | Security review hands off to production deployment for remediation tracking.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L252-L263】 |
| review-protocols/utils/_review-router.md | 4-quality-audit.md | Router script binds review flows back to the audit protocol under specific modes.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L170-L181】 |

## 2. Artifact Path Patterns
Each protocol anchors evidence into a numbered artifact directory that mirrors the current naming scheme. Representative examples are listed below.

| Protocol | Artifact path pattern | Evidence snippet |
| --- | --- | --- |
| 0-bootstrap-your-project.md | `.artifacts/protocol-0/…` | Numerous evidence items (tooling confirmation, rule migrations, repo mapping) align with `protocol-0` naming.【F:.cursor/ai-driven-workflow/0-bootstrap-your-project.md†L40-L87】 |
| 3-process-tasks.md | `.artifacts/protocol-3/…` | Execution artifacts cataloged under `protocol-3` for downstream quality use.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L263-L270】 |
| 4-quality-audit.md | `.artifacts/protocol-4/…` | Audit deliverables (CI outputs, quality metrics) live inside `protocol-4` paths.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L255-L259】 |
| 5-implementation-retrospective.md | `.artifacts/protocol-5/…` | Retrospective evidence stored with protocol-specific directory naming.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L52-L113】 |
| 6-technical-design-architecture.md | `.artifacts/protocol-6/…` | Architecture blueprints and decision logs leverage the `protocol-6` namespace.【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L44-L100】 |
| 7-environment-setup-validation.md | `.artifacts/protocol-7/…` | Environment validation logs saved under `protocol-7` paths.【F:.cursor/ai-driven-workflow/7-environment-setup-validation.md†L44-L97】 |
| 8-script-governance-protocol.md | `.artifacts/protocol-8/…` | Governance manual validation log stored with `protocol-8` identifier.【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L210-L245】 |
| 9-integration-testing.md | `.artifacts/protocol-9/…` | Integration test reports and coverage evidence reference `protocol-9` directories.【F:.cursor/ai-driven-workflow/9-integration-testing.md†L24-L93】 |
| 10-pre-deployment-staging.md | `.artifacts/protocol-10/…` | Staging readiness artifacts leverage `protocol-10` folder names.【F:.cursor/ai-driven-workflow/10-pre-deployment-staging.md†L261-L261】 |
| 11-production-deployment.md | `.artifacts/protocol-11/…` | Production deployment checklists tied to `protocol-11` directory naming.【F:.cursor/ai-driven-workflow/11-production-deployment.md†L265-L265】 |
| 12-monitoring-observability.md | `.artifacts/protocol-12/…` | Monitoring dashboards and runbooks reside under `protocol-12` folders.【F:.cursor/ai-driven-workflow/12-monitoring-observability.md†L260-L260】 |
| 13-incident-response-rollback.md | `.artifacts/protocol-13/…` | Incident records routed through `protocol-13` storage locations.【F:.cursor/ai-driven-workflow/13-incident-response-rollback.md†L266-L266】 |
| 14-performance-optimization.md | `.artifacts/protocol-14/…` | Performance tuning artifacts stored in `protocol-14` namespaced directories.【F:.cursor/ai-driven-workflow/14-performance-optimization.md†L259-L259】 |
| 15-uat-coordination.md | `.artifacts/protocol-15/…` | UAT evidence packages follow `protocol-15` naming convention.【F:.cursor/ai-driven-workflow/15-uat-coordination.md†L264-L264】 |
| 16-documentation-knowledge-transfer.md | `.artifacts/protocol-16/…` | Documentation kits saved with `protocol-16` identifier.【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L52-L129】 |
| 17-project-closure.md | `.artifacts/protocol-17/…` | Closure records stored with `protocol-17` path format.【F:.cursor/ai-driven-workflow/17-project-closure.md†L52-L106】 |
| 18-maintenance-support.md | `.artifacts/protocol-18/…` | Maintenance operations rely on `protocol-18` evidence directories.【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L52-L108】 |

## 3. Documentation & Guidance References
- **Integration philosophy** – PROTOCOL-INTEGRATION-MAP.md documents desired straight-line sequence, highlighting deltas versus actual code handoffs.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】
- **Automation bindings** – INTEGRATION-GUIDE.md enumerates automation hooks tied to existing numbering (00–5).【F:.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md†L12-L80】
- **Agent shortcuts** – AGENTS.md contains `@apply` helpers and phase summaries referencing old identifiers.【F:.cursor/ai-driven-workflow/AGENTS.md†L20-L112】【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】
- **Review ecosystems** – review-protocols/* cross-link to operational protocols via direct `@apply`, embedding quality gating dependencies.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L246-L259】【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L252-L263】

## 4. Observed Chain vs. Intended Flow
- **Implemented chain** – Current `@apply` graph forms: 00a → 00B → 01 → 00 → 0 → 00 (loop) → 1 → 6 → 2 → 7 → 3 → 9 → 4 → 15 → 10 → 11 → 12 → 13 → 14 → 5 → 8 → 4 (loop), with documentation branch 16 → 17 → 18 → 5.【F:.cursor/ai-driven-workflow/00a-client-proposal-generation.md†L250-L261】【F:.cursor/ai-driven-workflow/00-client-discovery.md†L282-L291】【F:.cursor/ai-driven-workflow/8-script-governance-protocol.md†L264-L273】【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L285-L294】【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L260-L269】
- **Documented intent** – Integration map expects linear 00a → … → 18 → 5 → 8 closure with 14 feeding 16 and 18 feeding 5 exactly once.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L8-L40】
- **Missing hop** – No `@apply` connects 00-generate-rules.md into the execution chain; the file currently has no downstream directive, leaving a dead-end in automation.【F:.cursor/ai-driven-workflow/00-generate-rules.md†L1-L200】

These findings provide the evidence base required for the renumbering and alignment initiative.
