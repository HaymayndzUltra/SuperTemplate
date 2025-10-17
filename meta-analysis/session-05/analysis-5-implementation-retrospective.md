# Meta-Instruction Analysis: .cursor/ai-driven-workflow/5-implementation-retrospective.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Assign the agent as Process Improvement Lead focusing on code review and learning capture.
- Reasoning: The opening defines the role, dual mission, and requirement to run only after implementation completion.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L3-L10】
- Meta-heuristic: Post-implementation stewardship to convert execution outcomes into process intelligence.

**Step 2:** Enforce a `[CRITICAL]` gate that blocks retrospectives without final task sign-off.
- Reasoning: The protocol forbids starting until merged evidence is stable, preventing premature analysis.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L9-L12】
- Meta-heuristic: Stability gating so feedback loops operate on finalized telemetry.

**Step 3:** Structure work as a two-phase pipeline where Phase 1 feeds Phase 2.
- Reasoning: Section 2 mandates sequential execution, making self-review insights prerequisite for collaborative discussion.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L15-L18】
- Meta-heuristic: Layered reflection ensuring data gathering precedes facilitation.

### Layer 2: Behavioral Control
**Step 4:** Run automation scripts to audit rules and aggregate evidence before reflection.
- Reasoning: Pre-retrospective automation commands produce rule audits and evidence bundles stored in `.artifacts/` with standardized messaging.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L19-L46】
- Meta-heuristic: Automated evidence harvesting to ground analysis in objective data.

**Step 5:** Load, filter, and cite evidence artifacts alongside CI/CD outcomes.
- Reasoning: Evidence review requires reusing aggregated JSON, referencing coverage and deployment data, and archiving additional artifacts with retrospective prefixes.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L47-L62】
- Meta-heuristic: Context saturation via telemetry reuse from audit stages.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】

**Step 6:** Invoke context discovery and verify rule compliance before generating hypotheses.
- Reasoning: Phase 1 mandates running the master rule protocol, checking new rule hygiene, and reviewing conversations for weak signals.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L63-L76】
- Meta-heuristic: Governance alignment to ensure retrospectives reflect rule integrity.

### Layer 3: Procedural Logic
**Step 7:** Audit source code against scoped rules to detect compliance gaps.
- Reasoning: Detailed steps outline scope identification, rule filtering, and per-file verification against master/common guidelines.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L77-L88】
- Meta-heuristic: Rule-driven inspection to tie outcomes back to governance artifacts.

**Step 8:** Formulate hypotheses, analyze rule coverage, and capture metadata feedback loops.
- Reasoning: Self-review synthesis demands hypotheses, over-engineering checks, and rule metadata feedback based on `[APPLIES RULES]` annotations.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L89-L100】
- Meta-heuristic: Reflective diagnostics to evolve rule taxonomy and precision.【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L36-L68】

**Step 9:** Facilitate collaborative retrospective through scripted prompts and evidence-backed analysis.
- Reasoning: Phase 2 supplies initiation phrasing, presentation guidance, and strict self-assessment dimensions using execution data.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L132】
- Meta-heuristic: Evidence-led facilitation to turn telemetry into shared insights.【F:.cursor/ai-driven-workflow/3-process-tasks.md†L154-L183】

**Step 10:** Translate findings into action items, secure validation, and conclude.
- Reasoning: Steps prescribe action synthesis, optional diffs, validation with user preferences, and closure messaging.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L133-L143】
- Meta-heuristic: Commitment-driven wrap-up to embed improvements into future workflows.

### Layer 4: Communication Grammar
**Step 11:** Announce automation outcomes using `[AUTOMATION]` templates.
- Reasoning: Both rule audit and evidence aggregation steps specify canonical messages with placeholders for counts.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L28-L45】
- Meta-heuristic: Consistent telemetry broadcasts bridging execution and reflection.

**Step 12:** Present process analysis in mandated markdown block format.
- Reasoning: The protocol provides a template requiring labeled bullet assessments across collaboration dimensions.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L121-L130】
- Meta-heuristic: Structured narrative ensures evidence aligns with stakeholder expectations.

**Step 13:** Use "OBJECTIVE ANALYSIS" framing when correcting biased findings.
- Reasoning: Communication section enforces a specific label when self-evaluation identifies earlier errors.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L171-L179】
- Meta-heuristic: Transparency grammar to maintain trust in retrospective adjustments.

## META-ARCHITECTURE DIAGRAM
```
System: Protocol 5 - Implementation Retrospective
├── Subsystem: Role & Gatekeeping
│   ├── Process Improvement Persona [Lines 3-12]
│   └── Two-Phase Workflow Mandate [Lines 15-18]
├── Subsystem: Evidence Acquisition
│   ├── Automation Scripts & Announcements [Lines 19-46]
│   └── Evidence Loading & Archival Rules [Lines 47-62]
├── Subsystem: Technical Self-Review
│   ├── Rule Context Loading [Lines 63-76]
│   ├── Compliance Audits [Lines 77-88]
│   └── Hypothesis & Metadata Feedback Loop [Lines 89-100]
├── Subsystem: Collaborative Retrospective
│   ├── Facilitation Script & Analysis Template [Lines 101-132]
│   └── Action Synthesis & Validation [Lines 133-143]
└── Subsystem: Self-Evaluation Safeguards
    ├── Validity & Bias Checks [Lines 148-163]
    └── Corrective Communication Protocol [Lines 164-179]
```

## COMMENTARY
**Architectural Dependencies:**
- Evidence acquisition depends on the automation and reporting infrastructure produced in Protocol 4, reusing `.artifacts/` outputs for retrospective grounding.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L19-L62】【F:.cursor/ai-driven-workflow/4-quality-audit.md†L22-L70】
- Rule audits rely on master rule discovery to ensure execution adhered to governance kernels defined earlier in the series.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L63-L94】【F:.cursor/rules/master-rules/1-master-rule-context-discovery.mdc†L1-L120】
- Collaborative actions convert self-review hypotheses into process adjustments, informing future task plans and audit focuses.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L143】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L36-L87】

**Meta-Engineering Heuristics:**
- Closed-loop telemetry: automation evidence, CI outcomes, and rule audits form a feedback loop that re-informs planning heuristics.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L19-L143】【F:.cursor/ai-driven-workflow/2-generate-tasks.md†L71-L127】
- Bias-aware reflection: dedicated self-evaluation and bias detection steps prevent over-engineering or misapplied rules from distorting learnings.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L148-L179】
- Actionability-first retrospectives: mandated action synthesis and validation ensure insights translate into concrete framework updates.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L133-L143】

**Cognitive Role Modularity:**
- Planner: Self-review stages identify future rule and process changes.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L89-L143】
- Executor: Automation scripts and evidence loaders gather the raw data for analysis.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L19-L62】
- Validator: Validity and bias checks stress-test conclusions before presentation.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L148-L179】
- Facilitator: Collaborative retrospective guides user dialogue and consensus-building.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L143】

## INFERENCE SUMMARY
This protocol embodies a telemetry-driven continuous improvement framework defined by:
1. Automated evidence aggregation that anchors retrospectives in verified artifacts.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L19-L62】
2. Governance-aligned self-review ensuring rule compliance insights precede user discussions.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L63-L100】
3. Bias-checked facilitation that converts findings into validated action plans.【F:.cursor/ai-driven-workflow/5-implementation-retrospective.md†L101-L179】

Design philosophy: Evidence-governed retrospection emphasizing objective telemetry, rule fidelity, and actionable process optimization.

## OUTPUT INSTRUCTIONS
- Format: Markdown with the five required sections fully expanded.
- Preserve ASCII diagram indentation exactly.
- Cite all references back to source protocols and related governance rules.
- Highlight telemetry continuity with preceding workflow phases in narrative sections.
