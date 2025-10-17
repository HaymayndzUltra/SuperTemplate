# Meta-Instruction Analysis: 00-generate-rules.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1: Establish mission to synthesize project-scoped rule set** (ref. L2-L33)
- Reasoning: The command sets purpose, scope, and phased discovery-analysis-generation structure to ensure rule emission aligns with repository realities.
- Meta-heuristic: Mission-scoped orchestration—define end goal and structural phases upfront.

**Step 2: Prioritize rule governance standards** (ref. L45-L84)
- Reasoning: Frontmatter requirements, precedence rules, and quality checklist codify compliance expectations before any rule is generated.
- Meta-heuristic: Governance-before-creation—set constraints that every output must satisfy.

### Layer 2: Behavioral Control
**Step 3: Mandate exhaustive context discovery** (ref. L8-L17)
- Reasoning: The agent must scan rule directories, legacy configs, AGENTS instructions, and project documents, ensuring comprehensive situational awareness.
- Meta-heuristic: Context saturation—accumulate all relevant signals before planning outputs.

**Step 4: Enforce analytical classification prior to generation** (ref. L18-L34)
- Reasoning: Detecting project type, frameworks, and gaps dictates which rule files to create and where to locate them.
- Meta-heuristic: Analytical gating—only generate after reasoned classification of needs.

**Step 5: Introduce optional modifiers for controlled execution** (ref. L36-L44)
- Reasoning: Command flags let operators scope outputs (frontend/backend, tests, stacks), balancing automation with operator intent.
- Meta-heuristic: Configurable autonomy—provide levers to tune generative breadth.

### Layer 3: Procedural Logic
**Step 6: Define structured output schemas** (ref. L24-L35, L61-L83)
- Reasoning: Specific filename patterns and content expectations (examples, conventions, testing) ensure consistent rule architecture across stacks.
- Meta-heuristic: Schema-driven authoring—standardize file naming and content blocks.

**Step 7: Implement verification and reporting loops** (ref. L71-L90, L121-L145)
- Reasoning: Checklists, output summaries, and trigger keywords create feedback mechanisms for verifying completeness and communicating results.
- Meta-heuristic: Closed-loop validation—pair generation with explicit verification messaging.

**Step 8: Provide migration and integration pathways** (ref. L92-L139)
- Reasoning: Legacy conversion, evidence artifacts, and CI integration steps embed the generator into broader systems, ensuring continuity and maintainability.
- Meta-heuristic: Ecosystem alignment—design outputs to slot into existing governance infrastructure.

### Layer 4: Communication Grammar
**Step 9: Prescribe operator interaction cues** (ref. L140-L150)
- Reasoning: Usage instructions, triggers, and concluding notes inform humans how to invoke and trust the command.
- Meta-heuristic: Instructional clarity—reduce ambiguity in human-agent collaboration via explicit cues.

**Step 10: Codify success/failure safeguards** (ref. L115-L120, L146-L150)
- Reasoning: Failure modes, fallback strategies, and reminders about evidence prioritization guide communication when anomalies occur.
- Meta-heuristic: Resilient messaging—anticipate exceptions and encode response patterns.

## META-ARCHITECTURE DIAGRAM
```
System: /Generate Cursor Rules Command
├── Mission & Scope Definition (L2-L35)
│   ├── Purpose & Scope (L4-L16)
│   └── Phase Definitions (L8-L34)
├── Governance Standards (L45-L84)
│   ├── Frontmatter Requirements (L45-L53)
│   ├── Rule Precedence Guidance (L54-L60)
│   └── Quality Checklist (L71-L84)
├── Execution Controls (L36-L44, L85-L120)
│   ├── Optional Flags (L36-L44)
│   ├── Output Format & Reporting (L85-L90)
│   └── Failure Safeguards (L115-L120)
├── Integration Pathways (L92-L139)
│   ├── Legacy Migration (L92-L102)
│   ├── Evidence Artifacts (L103-L107)
│   └── CI Integration (L108-L114)
└── Operator Interface (L121-L150)
    ├── Usage Examples (L121-L134)
    ├── Workflow Timing (L135-L139)
    └── Invocation & Triggers (L140-L150)
```

## COMMENTARY
**Architectural Dependencies:**
- Mission & Scope foundation dictates which governance standards apply; without the upfront definition, later checklists lack context.
- Execution Controls rely on Governance Standards to evaluate success; the checklist is the metric applied after generation.
- Integration Pathways depend on structured outputs from earlier layers to migrate legacy data and plug into CI.
- Operator Interface synthesizes decisions from all layers to instruct humans on correct usage and failure handling.

**Meta-Engineering Heuristics:**
- Context saturation ensures rule generation is data-driven rather than assumption-based.
- Governance-first design enforces compliance by embedding constraints before any creative step occurs.
- Configurable autonomy balances automation with operator oversight through flags and safeguards.
- Ecosystem integration treats rule generation as part of a continuous evidence and CI pipeline rather than a one-off action.

**Cognitive Role Modularity:**
- Planner: Discovery and analysis phases determine stack classification and rule coverage.
- Executor: Generation phase writes structured rule files following schemas.
- Validator: Quality checklist and reporting loop verify outputs.
- Auditor: Integration and evidence artifacts provide traceable records for future sessions.

## INFERENCE SUMMARY
The command embodies a deterministic rule-factory framework emphasizing governance, configurability, and integration:
1. Context gathering and analysis precede any generative work to ensure fidelity.
2. Strict formatting and checklists guarantee every output satisfies organizational standards.
3. Integration hooks align the generator with legacy assets and continuous validation systems.

Design philosophy: Compliance-driven automation where rule synthesis operates as a managed pipeline component within a larger orchestration ecosystem.

## OUTPUT INSTRUCTIONS
- Deliver analysis in Markdown with intact headings and bullet structures.
- Preserve ASCII hierarchy spacing exactly as rendered.
- Reference source line ranges for each major claim.
- Keep all five sections fully articulated without truncation.
