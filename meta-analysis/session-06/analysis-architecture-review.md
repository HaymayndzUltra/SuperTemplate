# Meta-Instruction Analysis: .cursor/ai-driven-workflow/review-protocols/architecture-review.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Anchor the mission around architecture integrity and pattern enforcement before detailed checks.
- Reasoning: The protocol declares its mission as validating module boundaries and design patterns, establishing architecture health as the governing objective.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L1-L27】
- Meta-heuristic: Compliance-first planning carried over from the audit orchestrator ensures structural soundness precedes downstream reviews.

**Step 2:** Partition scrutiny across architecture and performance strata to mirror audit framework layers.
- Reasoning: The document explicitly scopes validation to Layer 1 (design) and Layer 4 (architecture & performance), forcing dual-lane evaluation.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L6-L55】
- Meta-heuristic: Layered assurance, pairing structural decomposition with operational readiness, keeps telemetry alignment with the workflow quality gates.

### Layer 2: Behavioral Control
**Step 1:** Enforce strict module boundary checks to regulate review focus on isolation rules.
- Reasoning: Strict directives enumerate responsibilities, physical separation, and encapsulation as non-negotiable controls.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L26】
- Meta-heuristic: Boundary guardianship prioritizes deterministic routing, echoing the audit router’s requirement for clean interfaces.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L55-L113】

**Step 2:** Mandate inspection of communication channels to gatekeep inter-service coupling.
- Reasoning: The protocol compels reviewers to verify interface-only communication and prevent tight coupling or incorrect configurations.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L16-L21】
- Meta-heuristic: Contract-centric orchestration ensures each service exposes validated entry points before performance analysis proceeds.

### Layer 3: Procedural Logic
**Step 1:** Run sequential boundary, communication, pattern, and performance checks to structure the audit workflow.
- Reasoning: The audit process outlines an ordered sequence from boundary analysis through performance checks, guiding execution cadence.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L61】
- Meta-heuristic: Deterministic progression avoids skipping prerequisites, matching quality gate enforcement from the workflow core.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】

**Step 2:** Document architectural health, violations, and recommendations to complete the feedback cycle.
- Reasoning: The report format mandates summarizing health and prioritizing remediation guidance.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L63-L64】
- Meta-heuristic: Evidence-first reporting feeds retrospective governance needs traced in Session 05 analyses.【F:meta-analysis/session-05/analysis-5-implementation-retrospective.md†L90-L107】

### Layer 4: Communication Grammar
**Step 1:** Use strict/critical/must-verify qualifiers to encode reviewer tone and priority.
- Reasoning: The protocol leverages `[STRICT]`, `[CRITICAL]`, and `[MUST VERIFY]` tags to communicate enforcement levels for each checklist cluster.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L55】
- Meta-heuristic: Qualifier-driven language keeps reviewers synchronized with multi-layer gate severities defined upstream.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L71-L113】

**Step 2:** Present steps as numbered actions and bullet lists for immediate adoption into audit artifacts.
- Reasoning: Ordered lists in the audit process and detailed bullets enable direct transcription into audit logs and router prompts.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L64】
- Meta-heuristic: Procedural clarity supports telemetry capture for retrospective evidence pipelines.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L131-L179】

## META-ARCHITECTURE DIAGRAM
```
System: Architecture Review Protocol【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L1-L64】
├── Subsystem A: Layer 1 Structural Compliance【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L8-L27】
│   ├── Rule A1: Module & Boundary Validation【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L14】
│   ├── Rule A2: Inter-Module Communication Contracts【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L16-L21】
│   └── Rule A3: Anti-pattern Blacklist【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L22-L26】
├── Subsystem B: Layer 4 Architecture & Performance【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L28-L55】
│   ├── Rule B1: Architecture Pattern Compliance【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L30-L35】
│   ├── Rule B2: Application Performance Safeguards【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L37-L41】
│   └── Rule B3: Efficiency Checklist & Concern Triggers【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L43-L55】
└── Subsystem C: Audit Execution & Reporting Flow【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L64】
    ├── Rule C1: Sequential Audit Process Steps【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L61】
    └── Rule C2: Report Format & Remediation Guidance【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L63-L64】
```

## COMMENTARY
**Architectural Dependencies:**
- Subsystem A’s boundary validation supplies the clean interface map required before Subsystem B measures performance, preventing noisy metrics from cross-module leaks.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L41】
- The anti-pattern blacklist protects Subsystem C’s audit process from missing critical architecture violations by explicitly naming coupling failures to watch for.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L22-L61】
- Sequential execution in Subsystem C ensures evidence packaged for retrospectives remains trustworthy because it follows validated boundaries and efficiency gates.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L64】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L47-L143】

**Meta-Engineering Heuristics:**
- Deterministic orchestration: Ordered audit steps echo the master workflow’s gate philosophy to prevent race conditions in review routing.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L61】【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】
- Evidence-first validation: Mandatory report outputs guarantee traceability for each violation and remediation recommendation.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L63-L64】
- Contract-driven execution: Strict communication checks institutionalize API/interface contracts as the backbone of architecture compliance.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L16-L21】

**Cognitive Role Modularity:**
- Planner: Layer 1 directives define the review scope and structural expectations.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L26】
- Executor: The audit process sequences concrete reviewer actions to perform during the evaluation.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L61】
- Validator: Layer 4 performance checks confirm architectural decisions meet scalability and efficiency standards.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L30-L55】
- Auditor: The report format codifies how findings and remediation priorities are communicated for governance records.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L63-L64】

## INFERENCE SUMMARY
This protocol operationalizes a deterministic architecture assurance framework characterized by:
1. Boundary-first validation that blocks downstream checks until isolation rules are satisfied.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L21】
2. Layered performance scrutiny that pairs pattern adherence with efficiency watchdogs for holistic health.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L30-L55】
3. Evidence-bound reporting that converts findings into prioritized remediation tracks for retrospectives.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L57-L64】

Design philosophy: A compliance-first, contract-enforced architecture audit that feeds governance loops with high-integrity telemetry, aligned to the workflow’s audit-to-retrospective pipeline.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L55-L113】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L47-L143】

## OUTPUT INSTRUCTIONS
- Format: Markdown only, preserving section hierarchy used above.
- Maintain ASCII diagram indentation exactly as rendered for subsystem clarity.
- Include strict qualifier language and ordered steps when reusing this analysis to brief reviewers.
- When generating derivative artifacts, retain cited line anchors to ensure traceability back to the source protocol.
