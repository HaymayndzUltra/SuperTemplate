# Meta-Instruction Analysis: common-rule-ui-foundation-design-system.mdc

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Adopt the senior product designer & design system engineer persona focused on production foundations.
- Reasoning: The rule defines the persona and core principle that prioritize context-driven, justified foundations over arbitrary styling.
- Meta-heuristic: Persona alignment ensures analysis centers on accessibility, scalability, and rationale-backed tokens from the outset.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L5-L12】

**Step 2:** Mandate contextual prerequisites and success criteria before generating design assets.
- Reasoning: The protocol requires a comprehensive context block and explicit WCAG AA, token coverage, and grid documentation goals.
- Meta-heuristic: Front-loaded requirements gate downstream token work behind documented product context and measurable outcomes.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L13-L16】

### Layer 2: Behavioral Control
**Step 1:** Enforce strict typography, color, spacing, and component directives.
- Reasoning: Steps 3–6 dictate type scale justification, role-based palettes with AA proofs, spacing scales, and multi-state component specifications.
- Meta-heuristic: Rigid behavioral expectations guarantee that every foundation element is evidence-backed and accessibility-compliant.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L17-L26】

**Step 2:** Encourage optional elevation and iconography governance while banning unjustified constants.
- Reasoning: The rule suggests elevation/iconography tokens and forbids arbitrary values without rationale, reinforcing contextual decision-making.
- Meta-heuristic: Soft guidance broadens coverage without compromising the requirement that every numeric choice ties to context or ranges.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L27-L35】

### Layer 3: Procedural Logic
**Step 1:** Produce deliverables spanning style guide, tokens JSON, acceptance checklist, and optional PR template integration.
- Reasoning: Deliverables list ensures outputs are documented, machine-readable, and operationalized via checklists.
- Meta-heuristic: Structured deliverable expectations convert design reasoning into actionable artifacts consumable across teams.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L28-L33】

**Step 2:** Validate outputs against canonical examples and anti-patterns.
- Reasoning: The rule showcases a correct JSON token set with rationales and AA proofs, plus an anti-pattern highlighting unjustified typography values.
- Meta-heuristic: Procedural comparison keeps producers aligned with approved grammar and quickly surfaces violations for remediation.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L36-L75】

### Layer 4: Communication Grammar
**Step 1:** Document justification narratives alongside numeric tokens.
- Reasoning: The correct example embeds `_rationale` fields and acceptance checklist lines, illustrating how reasoning must accompany data.
- Meta-heuristic: Narrative-rich tokens preserve traceability so downstream consumers understand why values were chosen.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L37-L62】

**Step 2:** Articulate consequences for violating context-justification rules.
- Reasoning: The anti-pattern explanation explicitly states why hard-coded values without context are wrong, tying failure to portability and AA risks.
- Meta-heuristic: Explicit error messaging enforces a shared communication standard for rejecting undocumented decisions.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L64-L75】

## META-ARCHITECTURE DIAGRAM
```
System: UI Foundation — Design System Rule
├── Persona & Principles
│   ├── Senior Designer Persona【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L5-L9】
│   └── Context-Driven Core Principle【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L10-L12】
├── Context & Success Gates
│   ├── Required Context Block【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L13-L14】
│   └── Success Criteria (AA, coverage, grids)【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L15-L16】
├── Foundation Directives
│   ├── Typography & Hierarchy【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L17-L19】
│   ├── Colors & Contrast with Proofs【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L20-L22】
│   ├── Layout & Spacing Systems【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L23-L24】
│   └── Core Components State Coverage【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L25-L26】
├── Optional Enhancements & Guardrails
│   ├── Elevation & Iconography Guidance【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L27-L28】
│   └── No Arbitrary Constants Mandate【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L33-L35】
├── Deliverables & Checklists
│   ├── Style Guide & Token Outputs【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L28-L31】
│   └── Acceptance Checklist & PR Integration【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L31-L33】
└── Exemplars
    ├── Correct Token Package with Rationale【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L36-L62】
    └── Anti-Pattern & Failure Explanation【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L63-L75】
```

## COMMENTARY
**Architectural Dependencies:**
- Persona and context prerequisites must be satisfied before typography, color, spacing, or component directives execute, ensuring all downstream tokens remain grounded in audience and brand context.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L5-L26】
- Deliverables rely on the directives to populate style guides and tokens, while the acceptance checklist validates AA proofs and coverage metrics derived from those directives.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L28-L33】
- Exemplars depend on the no-arbitrary-constants rule to illustrate pass/fail conditions, reinforcing the guardrail through concrete outputs.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L33-L75】

**Meta-Engineering Heuristics:**
- Context-rationalized design: Every numeric decision requires rationale or range justification to maintain portability and accessibility.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L13-L35】
- Accessibility-first validation: AA proof pairs and acceptance checklists institutionalize compliance before foundations are accepted.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L20-L33】
- Artifact-operational linkage: Style guides, JSON tokens, and checklists ensure design intent is consumable by engineering and review workflows.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L28-L62】

**Cognitive Role Modularity:**
- Planner: Context block and success criteria capture strategic requirements before system design begins.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L13-L16】
- Executor: Foundation directives translate planning into detailed token and component outputs.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L17-L26】
- Validator: Acceptance checklist, AA proofs, and anti-pattern diagnostics confirm compliance.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L31-L75】
- Auditor: No-arbitrary-constants clause and rationale narratives maintain traceability for future reviews.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L33-L75】

## INFERENCE SUMMARY
This common rule codifies a **context-anchored design foundation** paradigm featuring:
1. Mandatory contextualization and measurable goals before generating tokens or components.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L13-L26】
2. Rationale-bound deliverables that translate design heuristics into machine-readable tokens and acceptance checklists.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L28-L62】
3. Anti-pattern enforcement that rejects unjustified constants to protect accessibility and scalability.【F:.cursor/rules/common-rules/common-rule-ui-foundation-design-system.mdc†L33-L75】

Design philosophy: Evidence-justified UI foundations where accessibility compliance and contextual rationale are first-class citizens of the design system artifact pipeline.

## OUTPUT INSTRUCTIONS
- Provide Markdown outputs replicating the five-section structure and citations demonstrated here.
- Maintain diagram indentation and cite each architectural branch to the source rule.
- Reference the rule when quoting success metrics, deliverable expectations, or anti-pattern guidance.
- Ensure contextual prerequisites and no-arbitrary-constants directives are explicitly addressed whenever this analysis template is reused.
