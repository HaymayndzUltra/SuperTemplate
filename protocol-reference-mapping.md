# Protocol Reference Mapping Analysis

## 1. Reference Inventory

### 1.1 Aggregate Counts
- **29 direct `@apply` handoffs** span the protocol set, review protocols, and integration guides, forming the backbone of the execution chain.【F:documentation/protocol-reference-summary.json†L2-L5】
- **610 textual mentions** of "Protocol X" appear across the corpus, driving prerequisite and dependency messaging that must be renumbered in lockstep.【F:documentation/protocol-reference-summary.json†L2-L5】
- **484 artifact path references** rely on the legacy `.artifacts/protocol-N/` convention and will need synchronized updates alongside any renumbering work.【F:documentation/protocol-reference-summary.json†L2-L5】
- **47 inline file-path references** (`.cursor/ai-driven-workflow/*.md`) tie documentation, review playbooks, and orchestration aides directly to protocol filenames.【F:documentation/protocol-reference-summary.json†L2-L5】

### 1.2 Protocol-Level Reference Matrix
The table below captures every protocol file’s downstream handoff, textual protocol mentions, artifact directory variants, and embedded path references. These metrics are sourced from the automated crawl stored in `documentation/protocol-reference-data.json` and confirm that each handoff is unique while artifact references remain tightly bound to the original numbering scheme.【F:documentation/protocol-reference-data.json†L2-L226】

| Protocol File | `@apply` Target | Protocol Mentions | Artifact Prefixes | File Path Refs |
| --- | --- | --- | --- | --- |
| 00a-client-proposal-generation.md | 00B-client-discovery-initiation.md | 15 | 00 | 1 |
| 00B-client-discovery-initiation.md | 01-project-brief-creation.md | 17 | 00 | 1 |
| 00-client-discovery.md | 01-project-brief-creation.md | 15 | 00 | 1 |
| 00-generate-rules.md | — | 0 | — | 0 |
| 00-project-bootstrap-and-context-engineering.md | 0-bootstrap-your-project.md | 16 | 00 | 1 |
| 0-bootstrap-your-project.md | 00-client-discovery.md | 15 | 0 | 1 |
| 01-project-brief-creation.md | 00-project-bootstrap-and-context-engineering.md | 17 | 00, 01 | 1 |
| 1-create-prd.md | 6-technical-design-architecture.md | 18 | 1 | 1 |
| 2-generate-tasks.md | 7-environment-setup-validation.md | 18 | 2 | 1 |
| 3-process-tasks.md | 9-integration-testing.md | 18 | 3 | 2 |
| 4-quality-audit.md | 15-uat-coordination.md | 25 | 4 | 1 |
| 5-implementation-retrospective.md | 8-script-governance-protocol.md | 24 | 5 | 1 |
| 6-technical-design-architecture.md | 2-generate-tasks.md | 18 | 6 | 1 |
| 7-environment-setup-validation.md | 3-process-tasks.md | 17 | 7 | 1 |
| 8-script-governance-protocol.md | 4-quality-audit.md | 21 | 8 | 1 |
| 9-integration-testing.md | 4-quality-audit.md | 22 | 9 | 1 |
| 10-pre-deployment-staging.md | 11-production-deployment.md | 24 | 10 | 1 |
| 11-production-deployment.md | 12-monitoring-observability.md | 28 | 11 | 1 |
| 12-monitoring-observability.md | 13-incident-response-rollback.md | 21 | 12 | 1 |
| 13-incident-response-rollback.md | 14-performance-optimization.md | 22 | 13 | 1 |
| 14-performance-optimization.md | 5-implementation-retrospective.md | 28 | 14 | 1 |
| 15-uat-coordination.md | 10-pre-deployment-staging.md | 27 | 15 | 1 |
| 16-documentation-knowledge-transfer.md | 17-project-closure.md | 35 | 16 | 1 |
| 17-project-closure.md | 18-maintenance-support.md | 23 | 17 | 1 |
| 18-maintenance-support.md | 5-implementation-retrospective.md | 22 | 18 | 1 |

### 1.3 Supporting Documentation and Review Links
Supporting guides and review workflows embed 18 additional filename and protocol references that must be coordinated with any renumbering activity.【F:documentation/protocol-reference-data.json†L226-L354】

| Supporting File | Protocol Mentions | File Path Refs | `@apply` Target |
| --- | --- | --- | --- |
| INTEGRATION-GUIDE.md | 39 | 7 | — |
| PROTOCOL-INTEGRATION-MAP.md | 12 | 0 | — |
| README.md | 0 | 0 | — |
| VALIDATION-GUIDE.md | 5 | 0 | — |

| Review Asset | Protocol Mentions | File Path Refs | `@apply` Target |
| --- | --- | --- | --- |
| review-protocols/README.md | 2 | 4 | 4-quality-audit.md |
| review-protocols/architecture-review.md | 16 | 1 | 6-technical-design-architecture.md |
| review-protocols/code-review.md | 14 | 1 | 3-process-tasks.md |
| review-protocols/security-check.md | 16 | 1 | 11-production-deployment.md |
| review-protocols/ui-accessibility.md | 0 | 1 | — |
| review-protocols/design-system.md | 0 | 1 | — |
| review-protocols/pre-production.md | 0 | 0 | — |
| review-protocols/utils/README.md | 0 | 1 | — |
| review-protocols/utils/_review-router.md | 0 | 3 | 4-quality-audit.md |
| review-protocols/utils/context-analyzer.md | 0 | 1 | — |
| review-protocols/utils/enhanced-static-template.md | 0 | 0 | — |
| review-protocols/utils/enhanced-static-validation.md | 0 | 0 | — |
| review-protocols/utils/rule-injection-system.md | 0 | 1 | — |

### 1.4 Artifact Path Patterns
Every protocol—except the rule generator—saves evidence under `.artifacts/protocol-N/`, reinforcing the need for a synchronized directory remap once sequential numbering is adopted.【F:documentation/protocol-reference-data.json†L2-L226】

| Protocol File | Artifact Prefixes |
| --- | --- |
| 00a-client-proposal-generation.md | 00 |
| 00B-client-discovery-initiation.md | 00 |
| 00-client-discovery.md | 00 |
| 00-project-bootstrap-and-context-engineering.md | 00 |
| 0-bootstrap-your-project.md | 0 |
| 01-project-brief-creation.md | 00, 01 |
| 1-create-prd.md | 1 |
| 2-generate-tasks.md | 2 |
| 3-process-tasks.md | 3 |
| 4-quality-audit.md | 4 |
| 5-implementation-retrospective.md | 5 |
| 6-technical-design-architecture.md | 6 |
| 7-environment-setup-validation.md | 7 |
| 8-script-governance-protocol.md | 8 |
| 9-integration-testing.md | 9 |
| 10-pre-deployment-staging.md | 10 |
| 11-production-deployment.md | 11 |
| 12-monitoring-observability.md | 12 |
| 13-incident-response-rollback.md | 13 |
| 14-performance-optimization.md | 14 |
| 15-uat-coordination.md | 15 |
| 16-documentation-knowledge-transfer.md | 16 |
| 17-project-closure.md | 17 |
| 18-maintenance-support.md | 18 |
| 5-implementation-retrospective.md | 5 |

## 2. Current Reference Chain

The live handoff chain extracted from `@apply` directives confirms a partially linear flow with two missing reintegration points, aligning with earlier observations that the transitions after `00-project-bootstrap-and-context-engineering` and `8-script-governance-protocol` require remediation before renumbering.【F:documentation/protocol-reference-data.json†L2-L226】 The chain materializes as:

```
00a → 00B → 01 → 00 → 0 → 00-client-discovery → 01 → 1 → 6 → 2 → 7 → 3 → 9 → 4 → 15 → 10 → 11 → 12 → 13 → 14 → 16 → 17 → 18 → 5 → 8
```

Integration artifacts such as `PROTOCOL-INTEGRATION-MAP.md` echo the same ordering while also documenting the dependency rationale between each phase of the lifecycle.【F:.cursor/ai-driven-workflow/PROTOCOL-INTEGRATION-MAP.md†L1-L92】

## 3. Proposed Sequential Mapping

The renumbering plan aligns the 27 workflow protocols (excluding `00-generate-rules.md`) with a clean `01-27` structure, preserving functional order while modernizing identifiers.【F:protocol-renumbering-prompt.md†L17-L78】

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

## 4. Reference Categories Requiring Updates

1. **Direct handoffs** – All `@apply` instructions across protocols and reviews must be retargeted to the new filenames once renumbered.【F:documentation/protocol-reference-data.json†L2-L354】
2. **Artifact directories** – Every `.artifacts/protocol-N/` path must be remapped to preserve automation outputs, particularly within execution and quality phases that depend on downstream evidence pull-through.【F:documentation/protocol-reference-data.json†L2-L226】
3. **Textual dependencies** – Mentions such as “Complete Protocol 7” within prerequisites or integration notes need global search-and-replace operations to avoid confusing implementers.【F:documentation/protocol-reference-data.json†L2-L354】
4. **Documentation call-outs** – Integration guides, review playbooks, and system README files include embedded filenames that must be aligned to prevent navigation breaks.【F:documentation/protocol-reference-data.json†L226-L354】

## 5. Risk Assessment

| Risk Class | Drivers | Potential Impact | Mitigation |
| --- | --- | --- | --- |
| High | Direct `@apply` handoffs (29 refs) and artifact directories (484 refs) | Broken protocol chaining and missing evidence artifacts | Execute staged search/replace with validation scripts before renaming files.【F:documentation/protocol-reference-summary.json†L2-L5】 |
| Medium | Textual “Protocol X” dependencies (610 refs) and supporting documentation cross-links (18 refs) | Conflicting instructions and onboarding confusion | Use controlled regex replacements and regenerate integration maps post-update.【F:documentation/protocol-reference-summary.json†L2-L5】【F:documentation/protocol-reference-data.json†L226-L354】 |
| Low | Static references in README or ancillary templates (limited counts) | Minor documentation drift | Schedule manual proofreading after automated updates.【F:documentation/protocol-reference-data.json†L226-L354】 |

---

**Next Steps:** Use the accompanying adjustment prompt, validation outline, and risk assessment deliverables to coordinate the renumbering rollout while preserving protocol integrity.
