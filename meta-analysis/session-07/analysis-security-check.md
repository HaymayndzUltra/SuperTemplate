# Meta-Instruction Analysis: .cursor/ai-driven-workflow/review-protocols/security-check.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Establish the mission as a focused security audit targeting data protection and multi-tenancy safeguards.
- Reasoning: The mission statement scopes the protocol to security validation, data protection, and multi-tenant defenses.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L5】
- Meta-heuristic: Compliance-first scoping aligns the review with the security pillar of the workflow before enumerating checks.【F:meta-analysis/session-06/analysis-architecture-review.md†L4-L18】

**Step 2:** Anchor the protocol at Layer 2 to ensure alignment with the audit framework’s security layer.
- Reasoning: The document explicitly declares itself a Layer 2 validation artifact, signaling priority on boundary and tenant safety.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L6-L8】
- Meta-heuristic: Layer-specific anchoring maintains deterministic orchestration across specialized audits, reinforcing the telemetry mapping defined in prior sessions.【F:meta-analysis/session-05/analysis-4-quality-audit.md†L32-L67】

### Layer 2: Behavioral Control
**Step 1:** Impose strict module and boundary security behaviors.
- Reasoning: `[STRICT]` controls require module-specific authentication, secret isolation, and boundary validation to prevent leakage.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L14】
- Meta-heuristic: Boundary guardianship continues the architecture review’s emphasis on isolation, now focused on security posture.【F:meta-analysis/session-06/analysis-architecture-review.md†L12-L23】

**Step 2:** Mandate tenant isolation and vulnerability sweeps as critical behaviors.
- Reasoning: `[CRITICAL]` directives enumerate tenant policies, `tenant_id` enforcement, and a checklist of common vulnerabilities to eliminate.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L16-L29】
- Meta-heuristic: Evidence-first security ensures auditors inspect each threat surface explicitly, supporting severity-tagged reporting.【F:meta-analysis/session-06/analysis-code-review.md†L56-L83】

### Layer 3: Procedural Logic
**Step 1:** Sequence audit steps from boundary checks to communication security.
- Reasoning: The audit process outlines four ordered steps, beginning with boundary security and concluding with communication review, guiding execution cadence.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L42】
- Meta-heuristic: Deterministic progression prevents bypassing prerequisites, echoing the workflow’s gate architecture.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】

**Step 2:** Require classification and remediation detail within reports.
- Reasoning: The report format instructs auditors to highlight critical vulnerabilities, classify severity, and provide fixes with code references.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L43-L44】
- Meta-heuristic: Evidence-first reporting ensures remediation guidance is available for downstream code and architecture reviews.【F:meta-analysis/session-06/analysis-code-review.md†L56-L83】

### Layer 4: Communication Grammar
**Step 1:** Use `[STRICT]` and `[CRITICAL]` qualifiers to encode urgency and enforce language consistency.
- Reasoning: The checklists rely on these qualifiers to convey enforcement strength, shaping reviewer tone.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L29】
- Meta-heuristic: Severity-aligned vocabulary sustains the audit router’s lexicon, enabling consistent telemetry tagging across protocols.【F:meta-analysis/session-06/analysis-code-review.md†L14-L35】

**Step 2:** Direct concise yet actionable reporting to ensure remediation clarity.
- Reasoning: The report guidance demands highlighted vulnerabilities with actionable steps, preventing ambiguous communication.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L43-L44】
- Meta-heuristic: Communication economy supports rapid routing of fixes to implementation teams, mirroring quick review expectations.【F:meta-analysis/session-06/analysis-code-review.md†L36-L55】

## META-ARCHITECTURE DIAGRAM
```
System: Security-Focused Audit
├── Subsystem A: Mission & Layer Context
│   ├── Rule A1: Mission alignment with data protection & multi-tenancy【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L5】
│   └── Rule A2: Layer 2 anchoring within the audit framework【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L6-L8】
├── Subsystem B: Boundary & Tenant Controls
│   ├── Rule B1: Module/boundary security directives【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L14】
│   └── Rule B2: Tenant isolation and vulnerability mandates【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L16-L29】
├── Subsystem C: Communication Security
│   └── Rule C1: Secure communication requirements for entrypoints and RPC methods【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L31-L35】
└── Subsystem D: Procedural & Reporting Flow
    ├── Rule D1: Ordered audit process from boundary to communication checks【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L42】
    └── Rule D2: Report emphasis on severity classification and remediation guidance【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L43-L44】
```

## COMMENTARY
**Architectural Dependencies:**
- Subsystem A ensures the audit remains synchronized with the workflow’s security layer, feeding upstream orchestration logic.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L8】
- Subsystem B’s controls supply the evidence prerequisites needed before communication security or release readiness can be validated.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L35】
- Subsystem D packages outputs that feed both pre-production audits and architecture remediations with actionable data.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L44】【F:meta-analysis/session-07/analysis-pre-production.md†L73-L96】

**Meta-Engineering Heuristics:**
- Security-first boundary enforcement prevents lateral movement and data leakage by default.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L20】
- Threat-focused enumeration ensures reviewers systematically address high-risk vectors like SQL injection and XSS.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L22-L29】
- Communication hardening keeps service-to-service interactions aligned with secure-by-design principles.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L31-L35】

**Cognitive Role Modularity:**
- Planner: Establishes mission scope and layer context through Subsystem A.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L8】
- Executor: Performs boundary and tenant checks under Subsystem B.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L29】
- Validator: Confirms secure communication patterns within Subsystem C.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L31-L35】
- Auditor: Compiles severity-classified findings guided by Subsystem D.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L44】

## INFERENCE SUMMARY
This protocol instantiates a security hardening framework centered on:
1. Layer 2 alignment that guarantees mission focus on tenant-safe boundary enforcement.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L8】
2. Strict behavioral mandates for authentication, secret isolation, and vulnerability sweeps across all modules.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L10-L29】
3. Procedural discipline that sequences checks and mandates actionable reporting for remediation pipelines.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L44】

Design philosophy: Evidence-driven security governance—ensuring every module demonstrates boundary integrity, tenant isolation, and hardened communication before release workflows proceed.【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L3-L44】

## OUTPUT INSTRUCTIONS
- When executing this protocol, retain the ordered four-step audit flow to maintain telemetry consistency.
- Preserve qualifier tags and severity classifications in generated reports for integration with audit routing systems.
- Provide explicit remediation guidance with references to affected modules or code paths to support rapid fixes.
- Cross-link outputs with pre-production audits to confirm layered security requirements remain satisfied downstream.
