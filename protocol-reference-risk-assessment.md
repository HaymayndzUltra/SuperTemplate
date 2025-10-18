# Protocol Reference Risk Assessment

## High-Risk Dependencies
- **Phase transition handoffs:** Protocol 4 routes directly into UAT (Protocol 15), so a broken `@apply` would halt the release pipeline and sever downstream quality gates.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L136-L146】【F:.cursor/ai-driven-workflow/4-quality-audit.md†L286-L286】
- **Operations evidence loops:** Protocol 18 aggregates maintenance approvals and feeds retrospectives; incorrect artifact paths would invalidate automation scripts that confirm governance cadence.【F:.cursor/ai-driven-workflow/18-maintenance-support.md†L135-L168】
- **Documentation closure:** Protocol 16 hands off to closure and maintenance; renumbering errors would orphan the knowledge transfer manifest relied upon by Protocol 17 and 18 owners.【F:.cursor/ai-driven-workflow/16-documentation-knowledge-transfer.md†L146-L167】

## Medium-Risk Areas
- **Planning lineage:** Protocol 6 exports design artifacts consumed by Protocols 2 and 7; numbering drift risks causing conflicting references in task generation and environment setup documentation.【F:.cursor/ai-driven-workflow/6-technical-design-architecture.md†L108-L120】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L109-L119】
- **Integration reporting:** Protocol 9 produces evidence bundles for both staging and monitoring; inconsistent naming could misdirect `.artifacts/protocol-9/` consumers in Protocols 10 and 12.【F:.cursor/ai-driven-workflow/9-integration-testing.md†L106-L119】
- **Review automation:** Review protocols map to specific workflow files; partial updates could send auditors to outdated playbooks.【F:.cursor/ai-driven-workflow/review-protocols/README.md†L64-L82】【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L230-L268】

## Low-Risk Considerations
- **Command orchestration:** AGENTS.md loads curated protocol shortcuts; while easy to update, stale entries would confuse slash-command users.【F:.cursor/ai-driven-workflow/AGENTS.md†L225-L231】
- **Shared narrative content:** Some protocols include historical references to prior numbering in examples or commentary; these can be adjusted with simple search-and-replace but should be tracked to avoid regressions.【F:.cursor/ai-driven-workflow/00-client-discovery.md†L147-L149】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L120-L133】
- **Validation scripts:** Planned automation must be synchronized with final mappings; until implemented, manual review is required but overall impact is low if caught early.【F:protocol-reference-validation-outline.md†L1-L60】
