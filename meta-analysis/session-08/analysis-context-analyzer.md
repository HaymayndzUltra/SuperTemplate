# Meta-Instruction Analysis: .cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md

## PHASE MAP
### Layer 1: System-Level Decisions
**Step 1:** Frame the analyzer as an intelligence layer that augments static protocols without compromising their reliability.
- Reasoning: The mission and persona sections articulate an enhanced static review engine that keeps proven protocols intact while adding smart targeting.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L1-L24】
- Meta-heuristic: Extends the compliance-first planning philosophy emphasized during the architecture review—innovation is permitted only when it safeguards baseline rigor.【F:meta-analysis/session-06/analysis-architecture-review.md†L12-L27】

**Step 2:** Partition the solution into a three-stage framework (change detection, rule relevance, protocol selection) before integration.
- Reasoning: Section headers organize the analyzer into Change Pattern Detection, Rule Relevance Matching, and Smart Protocol Selection prior to integration directives.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L9-L132】
- Meta-heuristic: Mirrors the staged execution loops from Process Tasks, ensuring each layer feeds validated data into the next stage without cross-contamination.【F:meta-analysis/session-04/analysis-3-process-tasks.md†L70-L94】

### Layer 2: Behavioral Control
**Step 1:** Codify detectors that gate context flags before any rule or protocol recommendations occur.
- Reasoning: TypeScript interfaces describe boolean context toggles, change magnitude metrics, and domain impact classifications used to regulate analyzer behavior.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L48】
- Meta-heuristic: Boundary sensors resemble the severity vocabularies cataloged in the design system protocol, guarding against overreaching recommendations.【F:meta-analysis/session-07/analysis-design-system.md†L15-L33】

**Step 2:** Bind behavioral thresholds to rule filtering so only relevant governance checks are surfaced.
- Reasoning: The rule mapping YAML defines priority levels, while the `analyzeRuleRelevance` function slices results into critical, recommended, optional, and skippable sets.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L50-L90】
- Meta-heuristic: Aligns with the master rule governance documented in quick code reviews—classification ensures reviewers focus on evidence-backed priorities.【F:meta-analysis/session-06/analysis-code-review.md†L18-L29】

### Layer 3: Procedural Logic
**Step 1:** Operationalize recommendation outputs with structured contracts that explain rationale, confidence, and focus areas.
- Reasoning: The `ProtocolRecommendation` interface and YAML cases specify how contexts map to primary/secondary protocols, rationale, and confidence scores.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L94-L132】
- Meta-heuristic: Procedure-first design aligns with the quality audit orchestrator’s mode-driven dispatch, ensuring analyzer outputs are directly consumable by the router.【F:.cursor/ai-driven-workflow/4-quality-audit.md†L71-L113】

**Step 2:** Describe integration steps that merge analyzer signals with enhanced protocol templates and execution commands.
- Reasoning: The integration section presents Markdown templates, interface extensions, and CLI command patterns that pipe context, rules, and focus directives into review runs.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L134-L200】
- Meta-heuristic: Replicates the automation synchronization loops from Process Tasks—context, rules, and focus payloads are handed off systematically to maintain audit trails.【F:meta-analysis/session-04/analysis-3-process-tasks.md†L62-L89】

### Layer 4: Communication Grammar
**Step 1:** Quantify benefits and success metrics using bold callouts and bulletized deltas to keep stakeholders aligned.
- Reasoning: Benefit and success criteria sections declare percentage improvements, accuracy targets, and satisfaction goals using emphasized numerics.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L203-L253】
- Meta-heuristic: Evidence-forward messaging supports the retrospective telemetry loops captured in Session 05 retrospectives, anchoring improvements to measurable outcomes.【F:meta-analysis/session-05/analysis-5-implementation-retrospective.md†L66-L107】

**Step 2:** Employ narrative result statements that reiterate mission impact with bolded themes.
- Reasoning: The concluding paragraph summarizes the analyzer’s effect—"40% more efficient" and "laser-focused validation"—using bold styling to reinforce key promises.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L205-L262】
- Meta-heuristic: Maintains the communicative cadence established across review protocols, ensuring operators can quickly echo mission-critical outcomes in reports.【F:meta-analysis/session-07/analysis-pre-production.md†L70-L98】

## META-ARCHITECTURE DIAGRAM
```
System: Enhanced Static Review Context Analyzer【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L1-L262】
├── Subsystem A: Change Signal Detection Layer【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L48】
│   ├── Rule A1: File Pattern Flagging Matrix【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L24】
│   ├── Rule A2: Change Magnitude Metrics Capture【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L27-L38】
│   └── Rule A3: Domain Boundary Impact Scan【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L40-L48】
├── Subsystem B: Rule Relevance Engine【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L50-L90】
│   ├── Rule B1: Context→Master Rule Mapping Catalog【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L52-L75】
│   └── Rule B2: Priority-Stratified Filtering Function【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L77-L90】
├── Subsystem C: Protocol Recommendation Core【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L94-L132】
│   ├── Rule C1: Recommendation Payload Contract【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L95-L104】
│   └── Rule C2: Context Scenario Mapping Table【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L106-L132】
├── Subsystem D: Protocol Integration Template【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L134-L166】
│   ├── Rule D1: Enhanced Protocol Markdown Template【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L138-L155】
│   └── Rule D2: Context Injection Interface Extension【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L157-L166】
└── Subsystem E: Execution & Impact Loop【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L170-L262】
    ├── Rule E1: Context Detection Git Workflow【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L170-L182】
    ├── Rule E2: Rule Filtering Command Flow【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L184-L191】
    ├── Rule E3: Enhanced Execution Invocation Script【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L193-L200】
    └── Rule E4: Benefit & KPI Communication Block【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L203-L262】
```

## COMMENTARY
**Architectural Dependencies:**
- Change detection (Subsystem A) produces the context flags consumed by the rule relevance engine, ensuring recommendations are anchored in actual diffs before priority scoring begins.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L90】
- Protocol recommendation payloads (Subsystem C) depend on accurate rule filtering (Subsystem B) to populate critical vs optional checks, keeping downstream enhanced templates context-aware.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L50-L155】
- Execution scripts and benefit reporting (Subsystem E) require integration templates (Subsystem D) to attach analyzer metadata into the `/review` workflow for telemetry tracking.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L134-L262】

**Meta-Engineering Heuristics:**
- Context-first governance: Analyzer decisions start with observable change patterns, preventing speculative recommendations.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L90】
- Priority stratification: Rule outputs are graded into tiers so reviewers spend time on the highest-value checks, echoing governance heuristics from quick code reviews.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L52-L90】【F:meta-analysis/session-06/analysis-code-review.md†L18-L29】
- Closed-loop measurement: Success criteria and KPIs ensure enhancements are validated quantitatively before broad rollout, sustaining audit-centric execution.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L203-L262】

**Cognitive Role Modularity:**
- Planner: Subsystem A gathers situational awareness to inform downstream planning decisions.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L48】
- Executor: Subsystems B and C compute rule sets and protocol recommendations to direct review execution.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L50-L132】
- Validator: Subsystem D embeds analyzer results into enhanced protocols, ensuring validations execute with the right context.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L134-L166】
- Auditor: Subsystem E documents commands, benefits, and KPIs, producing evidence for retrospectives and rollout decisions.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L170-L262】

## INFERENCE SUMMARY
The context analyzer embodies a context-governed augmentation strategy defined by:
1. Structured change sensing that informs every downstream recommendation without bypassing static protocol safeguards.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L13-L48】
2. Tiered rule alignment translating domain impacts into prioritized validations for the router ecosystem.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L50-L132】
3. Telemetry-linked execution scripts that capture performance gains and user satisfaction metrics for governance review.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L170-L262】

Design philosophy: intelligence with accountability—smart context analysis is only acceptable when its recommendations are explainable, measurable, and fully traceable through the enhanced static workflow.【F:.cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md†L1-L262】【F:meta-analysis/session-05/analysis-5-implementation-retrospective.md†L90-L107】

## OUTPUT INSTRUCTIONS
- Publish the analysis in Markdown with all five sections intact and clearly labeled.
- Preserve ASCII diagram indentation to keep subsystem boundaries machine-readable.
- Cite source line ranges for every factual assertion to maintain evidence standards.
- When briefing future sessions, reuse quantified benefit statements so improvement claims remain tethered to documented KPIs.
