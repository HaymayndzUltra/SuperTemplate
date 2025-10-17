# Meta-Instruction Analysis: common-rule-ui-interaction-a11y-perf.mdc

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Assume the Interaction Designer + Accessibility Specialist persona with performance accountability.
- Reasoning: The persona directive fuses interaction craft, inclusive access, and perf vigilance, establishing the governing mindset for every downstream rule.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L7-L11】
- Meta-heuristic: Persona priming anchors the analyst in dual-track empathy (behavior + access) before specifying mechanics.

**Step 2:** Encode premium UX as balanced feedback, inclusion, and responsiveness targets.
- Reasoning: The core principle frames success as simultaneous clarity, accessibility, and speed, requiring every decision to respect these three forces.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L10-L11】
- Meta-heuristic: Triadic objective setting ensures later requirements never optimize one pillar at the expense of the others.

### Layer 2: Behavioral Control
**Step 1:** Gate execution on exhaustive context capture and inclusive interaction mandates.
- Reasoning: Steps 1–5 collect critical flows, platform constraints, focus states, keyboard maps, gesture sizing, and resilient states so behavior design operates on verified constraints.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L13-L25】
- Meta-heuristic: Context-first orchestration prevents generic solutions by forcing scenario-specific accessibility scaffolding.

**Step 2:** Bind performance and deliverable expectations to measurable artifacts.
- Reasoning: Steps 7–8 disallow harmful lazy-loading, set explicit LCP/INP ceilings, and demand JSON interaction specs, acceptance tables, and perf checklists to materialize intent.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L34】
- Meta-heuristic: Evidence-driven deliverables translate abstract goals into auditable assets.

### Layer 3: Procedural Logic
**Step 1:** Model compliant behaviors via structured interaction JSON.
- Reasoning: The ✅ example demonstrates component states, ARIA roles, keyboard traps, and timing budgets within a canonical schema, offering a ready-made template for execution.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L36-L51】
- Meta-heuristic: Pattern exemplars standardize implementation grammar so teams can replicate accessible motion specs consistently.

**Step 2:** Flag failure modes triggered by uniform timing, indiscriminate lazy-loading, and keyboard neglect.
- Reasoning: The ❌ anti-pattern exposes brittle assumptions that degrade performance metrics and exclude keyboard users, reinforcing why each strict rule exists.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L53-L63】
- Meta-heuristic: Contrastive diagnostics cement guardrails by showing the consequence of skipping required data and accessibility coverage.

### Layer 4: Communication Grammar
**Step 1:** Articulate validation storytelling through success and error narratives.
- Reasoning: The correct and incorrect JSON paired with the closing explanation trains communicators to report outcomes with evidence and consequence framing.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L36-L63】
- Meta-heuristic: Narrative pairing elevates status reporting from raw metrics to user-impact storytelling.

**Step 2:** Maintain instruction clarity with structured bulleting and emphasized strictness.
- Reasoning: Bracketed `[STRICT]` callouts, bullet hierarchies, and specific ranges provide repeatable grammar for subsequent briefs and specs.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L13-L34】
- Meta-heuristic: Consistent syntax codifies expectations so future updates stay aligned with interaction doctrine.

## META-ARCHITECTURE DIAGRAM
```
System: UI Interaction — Accessibility & Performance
├── Persona & Principle Core
│   ├── AI Persona Definition【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L7-L9】
│   └── Premium UX Core Principle【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L10-L11】
├── Behavioral Protocol Stack
│   ├── Context Intake & Accessibility Mandates【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L13-L25】
│   └── Performance & Deliverable Requirements【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L34】
├── Execution Patterns
│   ├── Interaction Spec JSON Template【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L36-L51】
│   └── Anti-Pattern Warning JSON【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L53-L59】
└── Validation Narratives
    ├── Failure Explanation Notes【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L62-L63】
    └── Checklist Integration Guidance【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L33-L34】
```

## COMMENTARY
**Architectural Dependencies:**
- Persona framing informs the context intake questions, ensuring the designer gathers the right accessibility and performance variables from the outset.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L7-L25】
- Performance targets rely on the deliverable stack so teams can trace metrics back to specific specs and acceptance evidence.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L34】
- The anti-pattern warning depends on the strict mandates to illustrate the consequences of skipping required keyboard, timing, or loading safeguards.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L15-L63】

**Meta-Engineering Heuristics:**
- Evidence-first interaction design: every strict rule either references measurement budgets or produces artifacts that encode them.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L51】
- Accessibility as default: keyboard, focus, and ARIA requirements appear before motion and performance, signalling non-negotiable inclusion.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L15-L24】
- Differential timing control: exit versus enter timing rules mandate nuanced motion tuning instead of blanket durations.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L18-L20】

**Cognitive Role Modularity:**
- Planner: Context intake questions determine which flows, devices, and accessibility needs govern the spec.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L13-L17】
- Executor: JSON interaction specs and deliverables dictate concrete build instructions.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L30-L51】
- Validator: Performance targets, acceptance tables, and anti-pattern warnings support QA teams in verifying compliance.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L63】

## INFERENCE SUMMARY
This rule promotes an interaction governance framework grounded in inclusive motion design with measurable performance accountability:
1. Accessibility-first sequencing ensures focus states, keyboard access, and ARIA semantics lead every interaction decision.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L15-L24】
2. Motion behaviors are constrained by calibrated timing ranges and platform-specific touch targets to maintain polish without excess.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L18-L22】
3. Verification culture emerges from structured deliverables, perf budgets, and narrative validation of success versus failure.【F:.cursor/rules/common-rules/common-rule-ui-interaction-a11y-perf.mdc†L26-L63】

Design philosophy: Deterministic interaction orchestration that marries inclusive UX with quantifiable performance thresholds.

## OUTPUT INSTRUCTIONS
- Format: Markdown only.
- Preserve ASCII diagram indentation exactly.
- Include all sections completely with citations referencing source lines.
- Maintain JSON and bullet formatting from the original guidance when referencing examples.
