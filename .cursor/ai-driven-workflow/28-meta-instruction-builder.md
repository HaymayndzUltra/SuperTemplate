# Stage 1: Role & Intent Explainer

**Purpose:** Define the role and clarify the intent of your meta prompt. This is the foundation of your prompt building process.

---

## 📝 Role Definition

**Instruction ID 1 — Role Persona Definition**
- **Input:** Project brief or stakeholder notes describing the AI’s intended responsibilities, domain, audience, and tone.
- **Process:**
  1) Extract domain, primary responsibilities, target audience, and tone keywords from the supplied materials.
  2) If any field is missing, prompt the user to supply it before drafting.
  3) Compose a 2–3 sentence description covering all four elements.
- **Output:** Markdown paragraph labeled “Role” containing domain, responsibilities, audience, and tone in complete sentences.
- **Validation:** Success if all four elements appear explicitly; otherwise flag “Role description incomplete” and loop to step 2.

### Role Output Template
```
Role: [Describe domain, responsibilities, audience, tone in 2–3 sentences.]
```

---

## 🎯 Intent Explanation

**Instruction ID 2 — Primary Intent Statement**
- **Input:** User-provided goal statements or success criteria for the meta prompt.
- **Process:**
  1) List all stated goals.
  2) Consolidate into a single leading objective written as an outcome with measurable scope (e.g., deliverable + metric/timeline).
  3) Confirm the statement references the intended dataset or task context.
- **Output:** Single sentence labeled “Primary Intent” including deliverable, scope, and context.
- **Validation:** Success if sentence answers “What output?”, “For whom/what dataset?”, and “How measured?”; otherwise request clarification.

### Primary Intent Template
```
Primary Intent: [Outcome including deliverable, scope, context, and measurement.]
```

**Instruction ID 3 — Secondary Objectives Listing**
- **Input:** Additional goals gathered from stakeholders.
- **Process:**
  1) Capture each distinct supporting goal.
  2) Transform each into a bullet containing action, target, and desired impact.
  3) Limit list to top five items prioritized by user; if more provided, ask for ranking.
- **Output:** Bulleted list under “Secondary Objectives” where each bullet follows “Action → Target → Impact” structure.
- **Validation:** Success if at least one and no more than five bullets exist, each with the three fields; otherwise adjust.

### Secondary Objectives Template
```
Secondary Objectives:
- Action: [Action] → Target: [Target] → Impact: [Impact]
- ...
```

---

## 🔤 User Input Section

**Instruction ID 4 — Custom Prompt Capture**
- **Input:** Original user prompt or query text.
- **Process:**
  1) Paste supplied prompt verbatim into a fenced block.
  2) Annotate metadata line indicating source (e.g., “Provided by [name/date]”).
  3) If text exceeds 500 words, confirm truncation strategy with user.
- **Output:** Quoted block labeled “User Query” containing prompt plus metadata line.
- **Validation:** Success if block matches supplied text checksum and metadata line present; otherwise re-ingest.

### User Query Template
```
User Query:
> [Verbatim prompt text]
> Metadata: Provided by [name/date]
```

---

## 📤 Output: Intent Document

### Generated Intent Document (Ready to Copy)
```
Role: [From Role Output]
Primary Intent: [From Primary Intent Template]
Secondary Objectives:
- [Action → Target → Impact]
User Query:
> [Verbatim prompt text]
> Metadata: Provided by [name/date]
```

**Instruction ID 5 — Transfer Stage‑1 Output to Stage‑2**
- **Input:** Completed Stage‑1 Intent Document file.
- **Process:**
  1) Copy entire Stage‑1 markdown.
  2) Paste into Stage‑2 input field.
  3) Run diff to ensure paste length matches source length.
- **Output:** Stage‑2 input field populated with identical Stage‑1 document.
- **Validation:** Success if diff shows zero changes; otherwise repeat paste.

**Transfer Verification Log**
- Source File Path: __________________
- Destination Field: __________________
- Diff Result: __________________
- Timestamp: __________________

---

# Stage 2: Reasoning Synthesizer (RS)

📍

**Purpose:** Structure the logical reasoning approach based on the intent defined in Stage 1. This stage builds the cognitive framework for your meta prompt.

---

## 📥 Input from Previous Stage

**Instruction ID 6 — Stage‑2 Input Confirmation**
- **Input:** Stage‑1 document and Stage‑2 workspace.
- **Process:**
  1) Verify Stage‑2 input contains headings “Role,” “Primary Intent,” “Secondary Objectives,” and “User Query.”
  2) If any missing, re-paste Stage‑1 output.
- **Output:** Stage‑2 input validated checklist with four items marked complete.
- **Validation:** Success if all four headings present; otherwise block progression.

### Stage‑2 Input Checklist
- [ ] Role heading present
- [ ] Primary Intent heading present
- [ ] Secondary Objectives heading present
- [ ] User Query heading present
- Validation Timestamp: __________________

---

## 🧠 Reasoning Framework

**Instruction ID 7 — Reasoning Approach Selection**
- **Input:** Intent document and list of available reasoning approaches.
- **Process:**
  1) Evaluate intent requirements (analytical depth, data type).
  2) Map requirements to selection criteria table (e.g., Deductive for rule enforcement).
  3) Choose approach with highest match score; document justification in one sentence.
- **Output:** Entry “Selected Approach: [Option] — Rationale: [Sentence].”
- **Validation:** Success if rationale references at least one intent attribute and option is from provided list; otherwise reconsider.

### Reasoning Approach Scorecard
| Approach | Criteria Match Notes | Score (1-5) |
| --- | --- | --- |
| Deductive Reasoning | | |
| Inductive Reasoning | | |
| Abductive Reasoning | | |
| Analogical Reasoning | | |
| Causal Reasoning | | |

Selected Approach: __________________ — Rationale: __________________________________

**Instruction ID 8 — Reasoning Steps Definition**
- **Input:** Chosen reasoning approach and intent document.
- **Process:**
  1) Decompose task into minimum three sequential steps aligned with approach.
  2) For each, define input consumed and output produced.
  3) Ensure dependencies flow without gaps.
- **Output:** Numbered list “Step 1 … Step N” with input/output annotations.
- **Validation:** Success if ≥3 steps, each naming input and output; else refine.

### Reasoning Steps Template
1. Step Name — Input: ________ → Output: ________
2. Step Name — Input: ________ → Output: ________
3. Step Name — Input: ________ → Output: ________
4. ...

**Instruction ID 9 — Key Considerations Documentation**
- **Input:** Context notes, constraints, stakeholder requirements.
- **Process:**
  1) For Context Analysis, summarize environment factors (max 3 bullets).
  2) List assumptions each with justification.
  3) Enumerate constraints with source references.
  4) Define success criteria as measurable targets (metric + threshold).
- **Output:** Table with columns Context/Assumptions/Constraints/Success Criteria containing bullet entries.
- **Validation:** Success if each column has ≥1 entry and success metrics include numeric or boolean thresholds; otherwise revise.

### Key Considerations Table
| Context | Assumptions | Constraints | Success Criteria |
| --- | --- | --- | --- |
| - ... | - ... | - ... | - Metric: ___ ≥/≤ ___ |

---

## 📤 Output: Reasoning Structure

### Generated Reasoning Structure (Ready to Copy)
```
Selected Approach: [Option] — Rationale: [Sentence]

Reasoning Steps:
1. [Step details]
...

Analysis Parameters (Key Considerations):
- Context: [...]
- Assumptions: [...]
- Constraints: [...]
- Success Criteria: [...]
```

**Instruction ID 10 — Transfer Stage‑2 Output to Stage‑3**
- **Input:** Completed Stage‑2 Reasoning Structure.
- **Process:**
  1) Copy entire structure.
  2) Paste into Stage‑3 input.
  3) Run word-count comparison (difference ≤0).
- **Output:** Stage‑3 input populated with Stage‑2 document, plus log showing counts match.
- **Validation:** Success if counts identical; else redo.

**Instruction ID 11 — Stage‑3 Input Confirmation**
- **Input:** Stage‑2 output within Stage‑3 workspace.
- **Process:**
  1) Confirm presence of “Reasoning Approach,” “Reasoning Steps,” and “Analysis Parameters.”
  2) Mark checklist.
- **Output:** Signed checklist stored with timestamp.
- **Validation:** Success if all three headings present; otherwise re-import.

### Stage‑3 Transfer Log
- Stage‑2 Word Count: _______
- Stage‑3 Word Count: _______
- Match Status: [ ] Pass / [ ] Fail
- Checklist:
  - [ ] Reasoning Approach present
  - [ ] Reasoning Steps present
  - [ ] Analysis Parameters present
- Reviewer Signature: __________________
- Timestamp: __________________

---

# Stage 3: Logic Planner (LP)

**Purpose:** Map out the decision-making framework and logical pathways. This stage creates the execution blueprint for your meta prompt.

---

## 🗺️ Logic Mapping

**Instruction ID 12 — Logical Flow Construction**
- **Input:** Reasoning structure and problem requirements.
- **Process:**
  1) Identify primary decision nodes; ensure each ties to a reasoning step.
  2) Map conditions and outcomes in flow diagram or table.
  3) Verify coverage of all critical scenarios defined in intent.
- **Output:** Decision tree table listing Condition, Action, Outcome for each node.
- **Validation:** Success if every reasoning step has at least one linked node and no uncovered intent scenario; otherwise expand tree.

### Decision Tree Table
| Condition | Action | Outcome | Linked Reasoning Step |
| --- | --- | --- | --- |
| If ... | Then ... | Outcome ... | Step # |

**Instruction ID 13 — Conditional Logic Specification**
- **Input:** Decision tree from ID12.
- **Process:**
  1) Translate each branch into IF/THEN statements.
  2) Include ELSE path covering remaining cases.
  3) Label each statement with output artifact.
- **Output:** Ordered list of IF/THEN/ELSE IF/ELSE clauses with referenced outputs.
- **Validation:** Success if all nodes from ID12 represented and ELSE path documented; otherwise adjust.

### Conditional Logic Template
1. IF [Condition A] THEN [Action] → Output: _______
2. ELSE IF [Condition B] THEN [Action] → Output: _______
3. ELSE [Default Action] → Output: _______

**Instruction ID 14 — Execution Sequence Detailing**
- **Input:** Logic blueprint and reasoning steps.
- **Process:**
  1) Align steps from reasoning and decision tree.
  2) Enumerate phases with numbered order (Initial → Final).
  3) Attach expected duration or resource note for each phase (if not provided, state “TBD”).
- **Output:** Numbered execution sequence with phase name and required inputs/outputs.
- **Validation:** Success if sequence covers every reasoning step and includes at least three phases; otherwise refine.

### Execution Sequence Template
1. Phase Name — Inputs: ________ — Outputs: ________ — Duration/Resources: ________
2. Phase Name — Inputs: ________ — Outputs: ________ — Duration/Resources: ________
3. Phase Name — Inputs: ________ — Outputs: ________ — Duration/Resources: ________
4. ...

**Instruction ID 15 — Edge Case and Fallback Plan**
- **Input:** Risk analysis or historical issues.
- **Process:**
  1) Identify minimum two high-risk scenarios.
  2) For each, define detection trigger and handling action.
  3) Specify universal fallback when triggers unmet.
- **Output:** Table with columns Scenario, Trigger, Response, Owner.
- **Validation:** Success if ≥2 scenarios documented plus fallback row; otherwise expand.

### Edge Case Table
| Scenario | Trigger | Response | Owner |
| --- | --- | --- | --- |
| Edge Case 1 | | | |
| Edge Case 2 | | | |
| Fallback | Trigger: not met | Response: [Default handling] | Owner: |

---

## 📤 Output: Logic Blueprint

### Generated Logic Blueprint (Ready to Copy)
```
Reasoning Reference: [From Stage 2]

Logic Pathways:
| Condition | Action | Outcome | Linked Reasoning Step |
| --- | --- | --- | --- |
| ... |

Conditional Logic:
1. IF ...
2. ELSE IF ...
3. ELSE ...

Processing Sequence:
1. Phase ...

Exception Handling:
| Scenario | Trigger | Response | Owner |
| --- | --- | --- | --- |
| ... |
```

**Instruction ID 16 — Transfer Stage‑3 Output to Stage‑4**
- **Input:** Logic Blueprint document.
- **Process:**
  1) Copy blueprint.
  2) Paste into Stage‑4 input.
  3) Perform checksum comparison to ensure integrity.
- **Output:** Stage‑4 input containing identical blueprint; checksum report archived.
- **Validation:** Success if checksum matches; else repeat transfer.

**Instruction ID 17 — Stage‑4 Input Confirmation**
- **Input:** Stage‑3 blueprint in Stage‑4 workspace.
- **Process:**
  1) Verify presence of sections “Logic Pathways,” “Conditional Logic,” “Processing Sequence,” “Exception Handling.”
  2) Log verification result.
- **Output:** Verification log with four checked fields.
- **Validation:** Success if all sections detected; otherwise re-import.

### Stage‑4 Transfer Checklist
- Checksum Source: _______
- Checksum Destination: _______
- Match Status: [ ] Pass / [ ] Fail
- Section Verification:
  - [ ] Logic Pathways present
  - [ ] Conditional Logic present
  - [ ] Processing Sequence present
  - [ ] Exception Handling present
- Reviewer: __________________
- Timestamp: __________________

---

# Stage 4: Format Designer/Mapper (FD)

📍

**Purpose:** Define the output structure, formatting, and presentation requirements. This stage ensures your meta prompt produces results in the desired format.

---

## 📥 Input from Previous Stage

**Instruction ID 18 — Format Family Selection**
- **Input:** Logic blueprint and repository of format families.
- **Process:**
  1) Score each format family against criteria (alignment with logic complexity, audience, automation requirements).
  2) Select top-scoring family.
  3) Document scorecard.
- **Output:** Statement “Selected Format Family: [Name] (Score X/5)” plus score table.
- **Validation:** Success if chosen family has highest score and justification recorded; otherwise reconsider.

### Format Family Scorecard
| Format Family | Alignment Notes | Score (1-5) |
| --- | --- | --- |
| Execution – Basic Protocol | | |
| Execution – Numbered Substeps | | |
| Execution – Reasoning Blocks | | |
| Guidelines – Rules & Standards | | |
| Issue Tracking – GitHub/Jira | | |
| Prompt Engineering – Multi-Role Pack | | |
| Meta-System – Instruction Creator | | |
| Custom/Hybrid Format | | |

Selected Format Family: __________________ (Score __/5)

**Instruction ID 19 — Output Container Choice**
- **Input:** Selected format family and stakeholder delivery preferences.
- **Process:**
  1) Gather delivery constraints (e.g., platform, file type).
  2) Evaluate each optional container against constraints.
  3) Choose container meeting all mandatory constraints; if none, document exception.
- **Output:** Entry “Selected Output Container: [Option] — Constraints satisfied: [list].”
- **Validation:** Success if selection satisfies all mandatory constraints; otherwise request alternative.

### Output Container Assessment
| Container | Mandatory Constraints Met? | Notes |
| --- | --- | --- |
| Structured Report / Narrative | | |
| Markdown Document | | |
| Table / Spreadsheet | | |
| JSON / YAML | | |
| Bullet / Checklist | | |
| CLI / Plain Text | | |
| Issue Export | | |

Selected Output Container: __________________ — Constraints satisfied: __________________

---

## 🎨 Output Format Specification

**Instruction ID 20 — Output Structure Definition**
- **Input:** Format family blueprint.
- **Process:**
  1) Identify required sections from format guidelines.
  2) Populate structure template ensuring every decision node maps to at least one section component.
  3) Add numbering or identifiers for traceability.
- **Output:** Structured outline listing sections/components with IDs and descriptions.
- **Validation:** Success if every reasoning step and decision node references a component in the outline; otherwise revise.

### Output Structure Outline
1. Section ID: ________ — Title: ________ — Linked Decision Nodes: ________
   - Component 1.1: ________
   - Component 1.2: ________
2. Section ID: ________ — Title: ________ — Linked Decision Nodes: ________
   - Component 2.1: ________
   - Component 2.2: ________

**Instruction ID 21 — Style Guidelines Specification**
- **Input:** Audience preferences and organizational style guide.
- **Process:**
  1) Determine tone, length, complexity, POV from style guide.
  2) Document numeric or categorical values (e.g., “Length: 800–1000 words”).
  3) Note sources for each decision.
- **Output:** Table with Tone, Length (quantified), Language Complexity, Point of View, plus source column.
- **Validation:** Success if each field includes concrete value and source; else update.

### Style Guidelines Table
| Attribute | Requirement | Source |
| --- | --- | --- |
| Tone | | |
| Length | | |
| Language Complexity | | |
| Point of View | | |

**Instruction ID 22 — Presentation Elements Rules**
- **Input:** Publishing standards and format outline.
- **Process:**
  1) Define heading levels with examples.
  2) Specify allowed emphasis styles and frequency limits.
  3) List required tables/callouts and citation format reference.
- **Output:** Checklist detailing presentation rules with quantitative limits (e.g., “Max 3 callouts per section”).
- **Validation:** Success if checklist covers headings, emphasis, lists, visuals, citations with measurable constraints; otherwise extend.

### Presentation Checklist
- [ ] Heading Levels: __________________
- [ ] Emphasis Rules: __________________ (Limit: ___ per section)
- [ ] List Usage: __________________
- [ ] Visual Elements: __________________ (Max count: ___)
- [ ] Citation Format: __________________
- [ ] Verification Timestamp: __________________

---

## 📊 Data Visualization Requirements

**Instruction ID 23 — Visualization Requirements Definition**
- **Input:** Data visualization needs from stakeholders.
- **Process:**
  1) Determine if visuals required; record boolean.
  2) When required, specify chart type, data labels, legend position, and data source.
  3) Document rationale for each choice.
- **Output:** Visualization requirements table with fields Chart Type, Required?, Labels, Legend, Data Source, Rationale.
- **Validation:** Success if table completed for each planned visualization; otherwise mark “Visualization scope incomplete.”

### Visualization Requirements Table
| Visualization | Required? (Y/N) | Chart Type | Labels | Legend Position | Data Source | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| Viz 1 | | | | | | |
| Viz 2 | | | | | | |

---

## 📏 Quality Assurance

**Instruction ID 24 — Quality Standards Establishment**
- **Input:** Organizational QA criteria and format specification.
- **Process:**
  1) Translate Completeness, Accuracy, Clarity, Consistency into measurable checks (e.g., number of sections present, peer review performed).
  2) Define responsible reviewer.
- **Output:** QA matrix listing each criterion, metric, threshold, reviewer.
- **Validation:** Success if every criterion has quantitative threshold and assigned reviewer; else revise.

### QA Matrix
| Criterion | Metric | Threshold | Reviewer |
| --- | --- | --- | --- |
| Completeness | | | |
| Accuracy | | | |
| Clarity | | | |
| Consistency | | | |

---

## 📤 Output: Format Specification

### Generated Format Specification (Ready to Copy)
```
Selected Format Family: [Name] (Score X/5)
Selected Output Container: [Option] — Constraints satisfied: [list]

Output Structure Outline:
1. Section ...

Style Guidelines:
| Attribute | Requirement | Source |
| --- | --- | --- |
| ... |

Presentation Checklist:
- Heading Levels: ...

Visualization Requirements:
| Visualization | Required? | Chart Type | Labels | Legend Position | Data Source | Rationale |
| --- | --- | --- | --- | --- | --- | --- |
| ... |

QA Matrix:
| Criterion | Metric | Threshold | Reviewer |
| --- | --- | --- | --- |
| ... |
```

**Instruction ID 25 — Transfer Stage‑4 Output to Stage‑5**
- **Input:** Format Specification document.
- **Process:**
  1) Copy Stage‑4 output.
  2) Paste into Stage‑5 input.
  3) Verify via checksum or diff.
- **Output:** Stage‑5 input containing identical specification with verification log.
- **Validation:** Success if verification passes; otherwise repeat transfer.

**Instruction ID 26 — Stage‑5 Input Confirmation**
- **Input:** Stage‑4 content now in Stage‑5 workspace.
- **Process:**
  1) Confirm presence of “Output Format,” “Formatting Rules,” “Presentation Elements,” “Quality Standards.”
  2) Mark results.
- **Output:** Confirmation checklist stored with timestamp.
- **Validation:** Success if all sections present; else re-paste.

### Stage‑5 Transfer Checklist
- Verification Method: [Checksum/Diff]
- Result: [ ] Pass / [ ] Fail
- Section Confirmation:
  - [ ] Output Format present
  - [ ] Formatting Rules present
  - [ ] Presentation Elements present
  - [ ] Quality Standards present
- Reviewer: __________________
- Timestamp: __________________

---

# Stage 5: Concordance & Alignment Validator (CAV)

📍

**Purpose:** Validate consistency and alignment across all meta prompt components. This final stage ensures coherence and produces your complete, production-ready meta prompt.

---

## 🔍 Alignment Validation

**Instruction ID 27 — Cross-Stage Consistency Review**
- **Input:** Completed documents from Stages 1–4.
- **Process:**
  1) For each checklist item, compare referenced sections (Intent vs Reasoning, etc.).
  2) Record pass/fail per item with evidence lines.
  3) Summarize findings in notes.
- **Output:** Table with four checklist items, pass/fail status, supporting citations.
- **Validation:** Success if all items marked pass or flagged with corrective action; otherwise hold progression.

### Cross-Stage Consistency Table
| Alignment Item | Pass/Fail | Evidence Reference | Corrective Action |
| --- | --- | --- | --- |
| Intent ↔ Reasoning | | | |
| Reasoning ↔ Logic | | | |
| Logic ↔ Format | | | |
| Overall Coherence | | | |

**Instruction ID 28 — Component Integration Assessment**
- **Input:** Cross-stage review outputs.
- **Process:**
  1) For each alignment question, provide Yes/No/Adjust plus 1-sentence rationale referencing evidence.
  2) If “Needs adjustment,” log corrective task.
- **Output:** Integration report summarizing alignment decisions and rationales.
- **Validation:** Success if every component has decision and rationale recorded; else revise.

### Integration Report
- Role & Intent Alignment: [Yes/No/Adjust] — Rationale: __________________ — Corrective Task ID: _______
- Reasoning & Logic Alignment: [Yes/No/Adjust] — Rationale: __________________ — Corrective Task ID: _______
- Format & Purpose Alignment: [Yes/No/Adjust] — Rationale: __________________ — Corrective Task ID: _______

**Instruction ID 29 — Optimization Recommendations Log**
- **Input:** Alignment gaps and inconsistencies.
- **Process:**
  1) List each gap with severity (High/Med/Low).
  2) Pair each with specific recommendation and expected impact metric.
  3) Assign owner and due date.
- **Output:** Recommendation table (Gap, Severity, Action, Impact Metric, Owner, Due Date).
- **Validation:** Success if every identified gap has action with metric and owner; otherwise update.

### Optimization Log
| Gap | Severity | Recommended Action | Impact Metric | Owner | Due Date |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

---

## ✨ Final Meta Prompt Assembly

**Instruction ID 30 — Final Meta Prompt Assembly**
- **Input:** Stage outputs (1–4) and validation notes.
- **Process:**
  1) Merge sections into final document in prescribed order.
  2) Ensure validation status reflects latest checklist results.
  3) Run formatting lint to match style/presentation rules.
- **Output:** Final markdown document “META PROMPT – FINAL VERSION” with all sections populated and lint report attached.
- **Validation:** Success if lint report passes and document contains all required sections; otherwise correct.

### Final Assembly Template
```
META PROMPT – FINAL VERSION

ROLE & INTENT
[Paste from Stage 1]

REASONING FRAMEWORK
[Paste from Stage 2]

LOGIC STRUCTURE
[Paste from Stage 3]

OUTPUT FORMAT
[Paste from Stage 4]

VALIDATION STATUS
- Cross-Stage Consistency: [Pass/Fail]
- Integration Assessment: [Summary]
- QA Sign-off: [Reviewer + Timestamp]

Lint Report: [Attach results]
```

**Instruction ID 31 — Final Prompt Submission**
- **Input:** Production-ready meta prompt.
- **Process:**
  1) Submit document to chosen AI interface.
  2) Capture submission confirmation or response ID.
  3) Archive confirmation with timestamp.
- **Output:** Submission log including platform, time, confirmation ID.
- **Validation:** Success if confirmation ID recorded; otherwise re-submit or troubleshoot.

### Submission Log
| Platform | Submission Time | Confirmation ID | Notes |
| --- | --- | --- | --- |
| | | | |

**Instruction ID 32 — Post-Execution Review Log**
- **Input:** AI system outputs and stakeholder feedback.
- **Process:**
  1) Document successes with evidence snippet.
  2) Document issues with severity rating.
  3) Specify planned adjustments referencing affected sections.
- **Output:** Retrospective table (Successes, Issues, Adjustments) with evidence links.
- **Validation:** Success if each column contains at least one entry and issues include severity; otherwise follow up.

### Post-Execution Review Table
| Successes (Evidence) | Issues (Severity + Evidence) | Adjustments (Linked Section) |
| --- | --- | --- |
| | | |

**Instruction ID 33 — Iteration Trigger Back to Stage‑1**
- **Input:** Completed review log and outstanding adjustments.
- **Process:**
  1) Evaluate whether unresolved issues exist.
  2) If yes, reopen Stage‑1 template with updated requirements and note revision number.
  3) If no issues, record “No iteration needed” and schedule next review cycle date.
- **Output:** Iteration decision record stating whether Stage‑1 restart occurs and why.
- **Validation:** Success if decision record references review evidence and, when iterating, logs new cycle start date.

### Iteration Decision Record
- Outstanding Issues? [Yes/No]
- Decision: [Restart Stage 1 / No iteration needed]
- Evidence Reference: __________________
- Next Review Cycle Date: __________________
- Authorized By: __________________

---

## ✅ Validation Summary

All instruction IDs 1–33 updated to match enhanced Input/Process/Output/Validation requirements. Transfer, alignment, and termination checks now include explicit verification artifacts for compliance.

