Proposal: eksaktong chain na gusto mo (+ dagdag ko pero aligned)
0) Canonical Data Shapes (para pare-pareho hand-off)

IntentDoc: { goal, outcomes, constraints, actors, scope, risks[], examples? }

ReasoningMap: { premises[], alternatives[], decisions[], evidence[], tradeoffs[] }

WorkGraph: { tasks[], deps[], phases[], rulesets[], acceptance[], risk_mitigations[] }

FormatSpec: { target: 'CHECKLIST_Z'|'RULES_GUIDE'|'TICKET_RFC'|'PHASED_PLAYBOOK', options{} }

Lahat ng module sa ibaba I/O-typed sa mga shape na ’yan.

1) Meta-Prompt: Intent Explainer (IE)

Goal: basahin ang raw input mo, i-echo at i-linaw, walang dagdag.
Output: IntentDoc.

Prompt (ready-to-use, strict JSON):

Role: Intent Explainer
Task: Basahin ang user brief. Ibalik ang INTENT nang walang dagdag o interpretative claims.
Rules:
- Mirror only. Identify explicit constraints & risks if literally present.
- List exact unknowns as "open_questions".
Output JSON ONLY:
{
  "goal": "...",
  "outcomes": ["..."],
  "constraints": ["..."],
  "actors": ["..."],
  "scope": {"in": ["..."], "out": ["..."]},
  "risks": ["..."],
  "examples": [],
  "open_questions": ["..."]
}
Fail if any field missing.

2) Meta-Prompt: Reasoning Synthesizer (RS)

Goal: gumawa ng ReasoningMap mula sa IntentDoc.
Output: ReasoningMap.

Prompt:

Role: Reasoning Synthesizer
Inputs: IntentDoc
Task: Derive a reasoning map that preserves WHY.
Output JSON ONLY:
{
  "premises": ["..."], 
  "alternatives": [{"option":"...","pros":["..."],"cons":["..."]}],
  "decisions": [{"decision":"...","because":["premise#","evidence#"]}],
  "evidence": ["..."],
  "tradeoffs": [{"choice":"...","give_up":"...","gain":"..."}]
}
Constraints: Decisions must reference premises/evidence; no hallucinated facts.

3) Meta-Prompt: Logic Planner (LP)

Goal: gawing step-by-step na may IDs, deps, at rules na naka-attach (para sa [APPLIES RULES: ...]).
Output: WorkGraph.

Prompt:

Role: Logic Planner
Inputs: IntentDoc, ReasoningMap
Task: Produce a typed WorkGraph: tasks with IDs, phases, dependencies, rulesets, and acceptance criteria.
Output JSON ONLY:
{
  "phases": [{"id":"Z","name":"...", "description":"..."}],
  "tasks": [
    {"id":"Z.0","name":"Task_Description","phase":"Z","rules_applied":["rule-..."],"acceptance":["..."]},
    {"id":"Z.1","name":"Subtask_1_Name","description":"Subtask_1_Description","phase":"Z",
     "subtasks":[
        {"id":"Z.1.1","description":"...","rules_applied":["rule-..."]},
        {"id":"Z.1.2","description":"...","rules_applied":["rule-...","rule-..."]}
     ]
    }
  ],
  "deps": [{"from":"Z.1","to":"Z.2"}],
  "rulesets":[
    {"id":"rule-atomic","label":"Atomic steps only","type":"STRICT"},
    {"id":"rule-safety","label":"Safety checks present","type":"MUST"}
  ],
  "acceptance": ["coverage_of_goals>=0.9","no_cycles","each_task_has_acceptance"]
}
Constraints: IDs must be hierarchical (Z, Z.1, Z.1.1...). Subtasks only reference rules in rulesets.

4) Meta-Prompt: Format Designer/Mapper (FD)

Goal: i-render ang WorkGraph + ReasoningMap sa napiling format (isa sa 4 na binigay mo).
Output: FormattedDoc (plain text/markdown), walang nagbabago sa content, layout lang.

Prompt (with format switch):

Role: Format Designer
Inputs: WorkGraph, ReasoningMap, FormatSpec
Task: Render the content into the target format WITHOUT altering semantics.
Output: Plain text ONLY.

If target == "CHECKLIST_Z":
- Render as:
  - [ ] Z.0 {Task_Description}
  - [ ] Z.1 **{Subtask_1_Name}:** {Subtask_1_Description}:
      - [ ] Z.1.1 {desc}. [APPLIES RULES: {rule-id, ...}]
      - ...

If target == "RULES_GUIDE":
- YAML frontmatter (type: GUIDELINES), then sections:
  - [STRICT] vs [GUIDELINE] markers
  - Step 1-5 with Phase subsections
  - DO/DON'T examples drawn from WorkGraph.acceptance and rulesets

If target == "TICKET_RFC":
- Title: [P{priority}] {Feature}: {High-Level Task}
- Body:
  [STRICT] DO example
  [GUIDELINES]
  [REASONING] (Premises/Constraints/Alternatives/Decision/Evidence/Risks & Mitigations/Acceptance Link)

If target == "PHASED_PLAYBOOK":
- PHASE 1..N
- Mark CRITICAL/MUST/Optional based on rulesets.type (STRICT→CRITICAL, MUST→MUST, others→Optional)

5) Meta-Prompt: Concordance & Alignment Validator (CAV) (dagdag ko para solid)

Goal: awtomatikong i-check kung tugma Intent ↔ Reasoning ↔ WorkGraph ↔ Format.
Output: {verdict, defects[], drift_score, coverage}

Prompt:

Role: Concordance & Alignment Validator
Inputs: IntentDoc, ReasoningMap, WorkGraph
Task: Check: (a) all goals are covered by tasks, (b) no contradictions between decisions and tasks,
(c) rules applied match constraints, (d) IDs well-formed, (e) deps acyclic.
Output JSON ONLY:
{"verdict":"pass|revise","coverage":0.xx,"drift_score":0.xx,"defects":[{"where":"Z.2.1","issue":"missing acceptance","fix":"add ..."}]}
Pass if coverage>=0.9, drift<=0.1, no High-severity defects.

6) Meta-Prompt: Format Selector (FS) (yung “isang meta-prompt na mag-aanalyze at magre-recommend” na gusto mo)

Goal: pumili ng format batay sa scenario, at maglabas ng recipe (anong modules at order).
Output: {target, recipe, options}

Prompt:

Role: Format Selector
Inputs: IntentDoc
Task: Recommend target format + module sequence.
Rules:
- If goal involves execution tracking → CHECKLIST_Z.
- If goal is policy/process codification → RULES_GUIDE.
- If goal is team alignment/decision record → TICKET_RFC.
- If goal is operations or runbook → PHASED_PLAYBOOK.
Output JSON ONLY:
{
  "target": "CHECKLIST_Z|RULES_GUIDE|TICKET_RFC|PHASED_PLAYBOOK",
  "recipe": ["IE","RS","LP","CAV","FD"],
  "options": {"priority":"P2","phase_names":["Discovery","Build","Verify"]}
}

End-to-end FLOW (exact sa gusto mo)

IE → IntentDoc (echo/linaw ng gusto mo).

RS → ReasoningMap (why/decisions/evidence).

LP → WorkGraph (Z / Z.1 / Z.1.1 + rules & acceptance).

FS → pumili ng format + recipe.

FD → render sa CHECKLIST_Z / RULES_GUIDE / TICKET_RFC / PHASED_PLAYBOOK.

CAV → final tugma check (fail → balik sa LP o RS auto-revise loop kung gusto mo).

Result: eksakto: may nag-a-analyze ng intent, may gumagawa ng reasoning, may logical steps, may nagde-design sa target format mo, at may validator ng tugma.