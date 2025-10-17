# Meta-Instruction Analysis: .cursor/ai-driven-workflow/review-protocols/utils/_review-router.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Elevate the router as the centralized authority that mediates every review entrypoint before protocol execution.
- Reasoning: The opening mission statement declares the router as the fallback brain for the unified `/review` orchestrator and flags portfolio-dashboard optimization scope.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L1-L8】
- Meta-heuristic: Reinforces the deterministic orchestration spine mapped in the Process Tasks protocol by routing all executions through a single governance surface.【F:meta-analysis/session-04/analysis-3-process-tasks.md†L70-L98】

**Step 2:** Institute environment detection as the first gate so downstream selections inherit a validated capability context.
- Reasoning: Step 1 scripts a directory probe that toggles `CUSTOM_AVAILABLE`, printing explicit telemetry for whether tailored protocols exist.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L9-L22】
- Meta-heuristic: Mirrors the pre-flight gating pattern used in quick code reviews—confirming prerequisites before dispatching reviewers preserves audit reliability.【F:meta-analysis/session-06/analysis-code-review.md†L9-L17】

### Layer 2: Behavioral Control
**Step 1:** Encode per-protocol decision trees that privilege custom stacks but degrade gracefully to generics.
- Reasoning: Each `####` subsection repeats the conditional, preferring `custom_*` files when available and logging the chosen path for six review modes.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L114】
- Meta-heuristic: Implements boundary guardianship by ensuring stack-specific heuristics only trigger when verified, preventing context bleed noted in prior design system reviews.【F:meta-analysis/session-07/analysis-design-system.md†L12-L23】

**Step 2:** Bind behavioral expectations to router-driven reporting so automation consumers receive uniform telemetry.
- Reasoning: The usage guidance mandates that adapters rely on the router and enumerates the four automated actions (detect, check, select, execute).【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L116-L132】
- Meta-heuristic: Sustains evidence-first reporting by guaranteeing every invocation emits consistent decision traces for retrospective telemetry loops.【F:meta-analysis/session-06/analysis-architecture-review.md†L58-L82】

### Layer 3: Procedural Logic
**Step 1:** Summarize routing permutations into a reference table that operationalizes mode-to-protocol bindings.
- Reasoning: The Router Logic Summary tabulates modes, custom sources, fallbacks, and stack features, encoding the algorithm in a human-scannable artifact.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L134-L144】
- Meta-heuristic: Procedural transparency converts branching logic into deterministic checklists aligned with the quality audit orchestrator.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L113】

**Step 2:** Close the execution loop with scripted usage samples that demonstrate router-mediated workflows.
- Reasoning: The Claude, Cursor, and result snippets show how commands resolve through the router and log the chosen custom asset before execution.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L168-L188】
- Meta-heuristic: Scenario anchoring provides reproducible scripts similar to the Process Tasks automation runbooks, ensuring operators can validate router outcomes end-to-end.【F:meta-analysis/session-04/analysis-3-process-tasks.md†L62-L89】

### Layer 4: Communication Grammar
**Step 1:** Maintain celebratory glyphs and severity cues to make routing state machine outputs instantly legible.
- Reasoning: Console echoes include `🎯`, `🌐`, and `✅` tokens describing decisions, reinforcing status semantics for human and machine parsing.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L32-L188】
- Meta-heuristic: Consistent glyph vocabulary keeps the communication grammar synchronized with severity cues defined in design and accessibility reviews, supporting router telemetry ingestion.【F:meta-analysis/session-07/analysis-ui-accessibility.md†L70-L99】

**Step 2:** Use emphatic bolding and Markdown callouts to highlight critical operator notes.
- Reasoning: Sections apply bold emphasis (e.g., `**IMPORTANT**`, `**Focus**`) to signal non-negotiable behaviors and the router’s mission.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L5-L192】
- Meta-heuristic: Marking must-read clauses upholds the communication discipline established across prior protocols, ensuring mission-critical instructions survive compression when summarized downstream.【F:meta-analysis/session-05/analysis-4-quality-audit.md†L80-L108】

## META-ARCHITECTURE DIAGRAM
```
System: Centralized Review Router【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L1-L192】
├── Subsystem A: Environment Capability Detection【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L9-L22】
│   └── Rule A1: Toggle Custom Availability Telemetry【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L15-L21】
├── Subsystem B: Protocol Selection Switchboard【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L114】
│   ├── Rule B1: Code Review Custom→Generic Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L26-L39】
│   ├── Rule B2: Security Check Custom→Generic Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L41-L53】
│   ├── Rule B3: Architecture Review Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L56-L69】
│   ├── Rule B4: Pre-Production Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L71-L84】
│   ├── Rule B5: Design System Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L86-L99】
│   └── Rule B6: UI Accessibility Cascade【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L101-L114】
├── Subsystem C: Tool Adapter Contract【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L116-L132】
│   └── Rule C1: Four-Step Router Assurance Loop【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L127-L131】
├── Subsystem D: Mode Reference Matrix【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L134-L144】
│   └── Rule D1: Mode→Protocol Binding Table【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L136-L144】
└── Subsystem E: Operator Playbooks & Telemetry Output【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L168-L192】
    ├── Rule E1: Adapter Invocation Examples【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L168-L180】
    └── Rule E2: Result Log Illustration【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L182-L188】
```

## COMMENTARY
**Architectural Dependencies:**
- Environment detection (Subsystem A) sets the `CUSTOM_AVAILABLE` state consumed by every cascade in Subsystem B, ensuring selections respect real filesystem capabilities before branching.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L15-L114】
- The selection switchboard feeds the tool adapter contract (Subsystem C) so that downstream orchestrators can emit consistent telemetry, tying into the quality audit controller documented earlier.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L132】【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L113】
- The reference matrix (Subsystem D) and operator playbooks (Subsystem E) serve as human-facing projections of the same routing logic, enabling auditors to validate router decisions against recorded outputs.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L134-L192】

**Meta-Engineering Heuristics:**
- Deterministic routing: Every branch follows the same conditionals, preventing configuration drift across tools.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L132】
- Graceful degradation: Custom logic is optional; the router promises seamless fallbacks, preserving reliability under constrained environments.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L32-L144】
- Evidence-first automation: Log messages and command snippets keep the routing process auditable for retrospective telemetry loops.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L32-L188】

**Cognitive Role Modularity:**
- Planner: Subsystem A verifies strategic capability assumptions before mode planning begins.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L9-L22】
- Executor: Subsystem B runs the operational cascades that determine which protocol executes.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L114】
- Validator: Subsystem C enforces the four-step assurance loop, checking that routing behavior matches expectations.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L127-L131】
- Auditor: Subsystems D and E publish artifacts—tables and logs—that allow reviewers to audit routing choices post-execution.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L134-L192】

## INFERENCE SUMMARY
The router operationalizes a compliance-first selection framework characterized by:
1. Capability-aware gating that blocks protocol dispatch until environment assumptions are validated.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L9-L22】
2. Symmetric custom-to-generic cascades that preserve specialized intelligence without sacrificing portability.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L24-L114】
3. Telemetry-rich outputs that keep every routing decision observable for audit and retrospective loops.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L116-L192】

Design philosophy: deterministic orchestration with graceful degradation—the router guarantees consistent behavior across heterogeneous environments while maintaining audit-ready transparency.【F:.cursor/ai-driven-workflow/review-protocols/utils/_review-router.md†L1-L192】【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L113】

## OUTPUT INSTRUCTIONS
- Deliver this analysis in Markdown, preserving heading hierarchy and bullet indentation.
- Maintain ASCII diagram indentation exactly to support tooling ingestion.
- Retain line-referenced citations for every architectural claim to uphold traceability.
- Reuse router glyph vocabulary (`✅`, `🎯`, `🌐`) when summarizing behavior so telemetry semantics remain intact.
