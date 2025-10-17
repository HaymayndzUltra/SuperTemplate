# Meta-Instruction Analysis: .cursor/ai-driven-workflow/review-protocols/code-review.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Position the protocol as a rapid compliance screen across design and craftsmanship layers.
- Reasoning: The mission frames a "quick validation" across code quality and design principles, signaling lightweight yet strict coverage.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L1-L19】
- Meta-heuristic: Speed-to-signal aligns with the audit router’s narrow-scope modes, providing early warnings before deeper reviews.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L71-L113】

**Step 2:** Bind the review scope to Layer 1 and Layer 3 to complement architecture and retrospective protocols.
- Reasoning: The audit framework explicitly calls out Layer 1 (design compliance) and Layer 3 (code quality & craftsmanship).【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L6-L41】
- Meta-heuristic: Layer complementarity ensures coverage continuity with the architecture review (Layer 4) and retrospective evidence loop.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L6-L55】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L47-L143】

### Layer 2: Behavioral Control
**Step 1:** Enforce strict module boundary and communication checks even within quick reviews.
- Reasoning: `[STRICT]` directives require verifying single responsibility, consistent terminology, and contract-based interactions despite the abbreviated format.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L18】
- Meta-heuristic: Consistency with architecture gatekeeping prevents regressions slipping through quick passes.

**Step 2:** Apply master rule compliance as non-negotiable craftsmanship guards.
- Reasoning: The Layer 3 checklist mandates try/catch around I/O, explicit naming, short functions, and shallow nesting as strict requirements.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L27】
- Meta-heuristic: Governance anchoring keeps rapid reviews aligned with master rules discovered during retrospectives.【F:.cursor/rules/master-rules/3-master-rule-code-quality-checklist.mdc†L1-L120】

### Layer 3: Procedural Logic
**Step 1:** Sequence design check, quality scan, and craftsmanship review to maximize signal extraction per minute.
- Reasoning: The audit process enumerates three ordered steps to execute, balancing structural, compliance, and readability checks.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L45】
- Meta-heuristic: Deterministic triage ensures quick reviews still log actionable findings in the correct order.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】

**Step 2:** Capture concise remediation-ready findings in the report output.
- Reasoning: Report guidance demands focused summaries of critical violations with specific remediation instructions.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L47-L48】
- Meta-heuristic: Action-first feedback accelerates downstream fixes and primes data for retrospective action validation.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L143】

### Layer 4: Communication Grammar
**Step 1:** Utilize strict/must-verify/anti-pattern tags to codify reviewer tone.
- Reasoning: Section headers embed `[STRICT]`, `[MUST VERIFY]`, and `[ANTI-PATTERNS]` to communicate severity levels in shorthand.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L40】
- Meta-heuristic: Shared vocabulary with other protocols maintains cross-review linguistic cohesion for the router.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L55-L113】

**Step 2:** Mix bullet lists and bold cues for quick scan adoption.
- Reasoning: The checklist uses bullet lists with bolded attributes (e.g., **Readability**, **Structure**) to guide reviewer attention during rapid passes.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L28-L40】
- Meta-heuristic: Visual cueing minimizes cognitive load, sustaining efficiency without sacrificing rigor.

## META-ARCHITECTURE DIAGRAM
```
System: Quick Code Review Protocol【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L1-L48】
├── Subsystem A: Layer 1 Design Compliance Sweep【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L8-L18】
│   ├── Rule A1: Single Responsibility & Terminology Check【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L13】
│   └── Rule A2: Interface-Only Communication Enforcement【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L15-L17】
├── Subsystem B: Layer 3 Master Rule Enforcement【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L27】
│   ├── Rule B1: Error Handling & Naming Discipline【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L24】
│   └── Rule B2: Function Size & Nesting Constraints【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L25-L27】
├── Subsystem C: Craftsmanship Evaluation Matrix【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L28-L40】
│   ├── Rule C1: Readability & Structure Review【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L28-L33】
│   └── Rule C2: Anti-Pattern Detection Checklist【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L35-L40】
└── Subsystem D: Execution & Reporting Loop【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L48】
    ├── Rule D1: Sequential Triage Steps【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L45】
    └── Rule D2: Concise Remediation Reporting【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L47-L48】
```

## COMMENTARY
**Architectural Dependencies:**
- Subsystem A’s boundary assurances prevent Subsystem B’s master rule checks from operating on misaligned module structures.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L27】
- Craftsmanship evaluation (Subsystem C) interprets findings from Subsystems A and B to identify readability gaps aggravated by structural or rule failures.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L40】
- The execution loop (Subsystem D) packages the triage outputs into concise reports ready for architecture review escalation or retrospective synthesis.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L48】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L143】

**Meta-Engineering Heuristics:**
- Rapid signal extraction: Ordered triage maintains velocity while respecting mandatory checks.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L45】
- Governance continuity: Master rule enforcement keeps the quick review synchronized with the broader rule corpus.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L27】【F:.cursor/rules/master-rules/3-master-rule-code-quality-checklist.mdc†L1-L120】
- Evidence-ready communication: Report instructions guarantee each finding is paired with remediation guidance, supporting downstream automation.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L47-L48】

**Cognitive Role Modularity:**
- Planner: Layer selection defines what the quick review must cover to stay aligned with the workflow lattice.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L6-L19】
- Executor: Triaged steps guide reviewers through a consistent quick-pass script.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L45】
- Validator: Master rule compliance and craftsmanship checks confirm adherence to governance and quality expectations.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L40】
- Auditor: Reporting instructions ensure findings are documented for audits and retrospectives.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L47-L48】

## INFERENCE SUMMARY
The quick review protocol exemplifies a governance-aligned rapid triage framework featuring:
1. Tight structural scrutiny that protects architecture integrity even under time constraints.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L18】
2. Mandatory master rule enforcement to maintain craftsmanship standards across fast iterations.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L21-L27】
3. Action-oriented reporting to keep telemetry flowing into audits and retrospectives without delay.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L48】

Design philosophy: Accelerated yet uncompromising quality governance that feeds the workflow’s continuous improvement loop with immediately actionable insights.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L71-L113】【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L47-L143】

## OUTPUT INSTRUCTIONS
- Render this analysis in Markdown preserving heading order and bullet indentation.
- Retain ASCII diagram indentation for subsystem clarity when briefing reviewers or tooling.
- Keep severity tags (`[STRICT]`, `[MUST VERIFY]`, `[ANTI-PATTERNS]`) in derivative outputs to maintain linguistic consistency.
- Preserve explicit line references when citing the source protocol to uphold traceability.
