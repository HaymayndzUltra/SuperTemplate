# Meta-Instruction Analysis: elaboration-specialist.mdc

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Align with the Clarification Specialist primary function focused on intent fidelity.
- Reasoning: The opening declares the persona’s sole mission—understand user meaning and restate it clearly without altering intent—setting the overarching decision frame.【F:.cursor/rules/elaboration-specialist.mdc†L6-L18】
- Meta-heuristic: Mission anchoring guards against speculative elaboration by enforcing fidelity-first thinking.

**Step 2:** Restrict activation to the elaborate command surface.
- Reasoning: Strict directives tie the rule to `.cursor/commands/elaborate.md`, ensuring scope isolation when the elaborate trigger appears.【F:.cursor/rules/elaboration-specialist.mdc†L9-L10】【F:.cursor/rules/elaboration-specialist.mdc†L69-L69】
- Meta-heuristic: Context binding prevents rule bleed into unrelated workflows, keeping elaboration behavior deterministic.

### Layer 2: Behavioral Control
**Step 1:** Enforce conversation pattern detection before structuring output.
- Reasoning: Operating Rules 1–2 compel scanning for casual conversational cues and responding directly if found, modulating behavior based on dialogue context.【F:.cursor/rules/elaboration-specialist.mdc†L21-L24】
- Meta-heuristic: Adaptive gating preserves natural conversation flow without over-structuring.

**Step 2:** If instructions remain unclear, follow the five-step clarification cascade leading to the structured format.
- Reasoning: Steps 3–7 describe parsing, understanding, expanding, preserving meaning, and outputting in the mandated Purpose/Action/Details/Outcome structure.【F:.cursor/rules/elaboration-specialist.mdc†L25-L37】
- Meta-heuristic: Progressive refinement ensures clarity emerges through deliberate checkpoints rather than ad-hoc rewriting.

### Layer 3: Procedural Logic
**Step 1:** Execute clarified instructions immediately after production.
- Reasoning: The strict command to perform the expected outcome instills an action bias, converting clarification into operational steps.【F:.cursor/rules/elaboration-specialist.mdc†L38-L39】
- Meta-heuristic: Clarify-to-act loop keeps elaboration connected to tangible results.

**Step 2:** Use examples as templates demonstrating faithful expansion.
- Reasoning: Example scenarios show how to translate vague Filipino/Taglish requests into structured outputs with preserved purpose, action, details, and outcomes.【F:.cursor/rules/elaboration-specialist.mdc†L41-L57】
- Meta-heuristic: Worked exemplars teach consistent formatting and level of detail expected during execution.

### Layer 4: Communication Grammar
**Step 1:** Uphold success metrics emphasizing clarity, fidelity, detail, and consistency.
- Reasoning: Success metrics define evaluation criteria for elaboration outputs, guiding communication tone and completeness.【F:.cursor/rules/elaboration-specialist.mdc†L58-L63】
- Meta-heuristic: Quality benchmarks standardize reporting standards for clarified instructions.

**Step 2:** Declare exception handling to manage ambiguous or conflicting input.
- Reasoning: Exceptions specify when to request more info and ban invention, preserving trust in the clarification channel.【F:.cursor/rules/elaboration-specialist.mdc†L64-L67】
- Meta-heuristic: Defensive communication rules safeguard against overreach when meaning is missing.

## META-ARCHITECTURE DIAGRAM
```
System: Elaboration Specialist Protocol
├── Mission Layer
│   ├── Clarification Specialist Role【F:.cursor/rules/elaboration-specialist.mdc†L6-L18】
│   └── Scope Binding to elaborate.md【F:.cursor/rules/elaboration-specialist.mdc†L9-L10】【F:.cursor/rules/elaboration-specialist.mdc†L69-L69】
├── Behavioral Gateways
│   ├── Conversation Pattern Check【F:.cursor/rules/elaboration-specialist.mdc†L21-L24】
│   └── Clarification Cascade Steps 3–7【F:.cursor/rules/elaboration-specialist.mdc†L25-L37】
├── Procedural Execution
│   ├── Immediate Outcome Execution【F:.cursor/rules/elaboration-specialist.mdc†L38-L39】
│   └── Structured Examples (API, CI/CD)【F:.cursor/rules/elaboration-specialist.mdc†L41-L57】
└── Communication Envelope
    ├── Success Metrics Checklist【F:.cursor/rules/elaboration-specialist.mdc†L58-L63】
    └── Exception Handling Rules【F:.cursor/rules/elaboration-specialist.mdc†L64-L67】
```

## COMMENTARY
**Architectural Dependencies:**
- The mission layer informs the behavioral gateways, dictating why clarification must prioritize user intent before structuring outputs.【F:.cursor/rules/elaboration-specialist.mdc†L6-L37】
- Procedural execution relies on the behavioral cascade to ensure any action taken stems from a validated clarified instruction.【F:.cursor/rules/elaboration-specialist.mdc†L25-L39】
- Communication metrics and exceptions depend on mission fidelity to evaluate whether clarifications remain accurate and safe.【F:.cursor/rules/elaboration-specialist.mdc†L58-L67】

**Meta-Engineering Heuristics:**
- Intent fidelity: The specialist never invents meaning, echoing the prohibition against assumption and the focus on user-provided intent.【F:.cursor/rules/elaboration-specialist.mdc†L6-L18】【F:.cursor/rules/elaboration-specialist.mdc†L65-L67】
- Structured articulation: Mandated Purpose/Action/Details/Outcome format ensures clarity without summarizing away nuance.【F:.cursor/rules/elaboration-specialist.mdc†L30-L37】
- Actionable closure: The requirement to execute clarified outcomes ties documentation to immediate utility.【F:.cursor/rules/elaboration-specialist.mdc†L38-L39】

**Cognitive Role Modularity:**
- Planner: Clarification cascade interprets ambiguous input into organized instruction sets.【F:.cursor/rules/elaboration-specialist.mdc†L25-L37】
- Executor: Immediate outcome execution and example adherence drive action post-clarification.【F:.cursor/rules/elaboration-specialist.mdc†L38-L57】
- Auditor: Success metrics and exceptions review the clarity and fidelity of outputs, flagging when more information is required.【F:.cursor/rules/elaboration-specialist.mdc†L58-L67】

## INFERENCE SUMMARY
This rule enforces a clarification-first service that converts ambiguous instructions into actionable guidance while preserving original intent:
1. Persona and scope binding keep the specialist laser-focused on interpretation rather than creation.【F:.cursor/rules/elaboration-specialist.mdc†L6-L18】【F:.cursor/rules/elaboration-specialist.mdc†L9-L10】
2. Behavioral gates and structured formats provide deterministic steps for handling unclear inputs and producing detailed outputs.【F:.cursor/rules/elaboration-specialist.mdc†L21-L37】
3. Execution mandates and evaluation metrics ensure every clarification immediately benefits downstream agents with auditable quality checks.【F:.cursor/rules/elaboration-specialist.mdc†L38-L67】

Design philosophy: Intent-preserving elaboration that prioritizes clarity, actionability, and guardrails against speculative additions.

## OUTPUT INSTRUCTIONS
- Format: Markdown only.
- Preserve ASCII diagram indentation exactly.
- Cite source line ranges for every structural claim.
- Maintain structured headings mirroring the mandated Purpose/Action/Details/Outcome ethos when referencing examples.
