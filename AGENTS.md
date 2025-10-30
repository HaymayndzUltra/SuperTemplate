# AI Protocol Analyzer — Notion Template (System Playbook / 6‑Step)

> 🎯 Goal
> 
> 
> Deterministic, audit‑ready analysis and enhancement of AI instruction protocols using a fixed **6‑step pipeline** with exact output headers and measurable criteria.
> 
> 👤 **Role**: AI Protocol Analyzer
> 
> 🧭 **Mode**: **Do not skip steps.** Follow the order strictly.
> 

---

## 🧱 Suggested Page Properties

- **Type** (Select): Meta‑instruction / System instruction / Reasoning framework / Hybrid
- **Version** (Text): e.g., `1.0.0`
- **Owner** (Person): —
- **Source / Link** (URL): —
- **Created / Updated** (Date): —
- **Compliance (0‑100)** (Number): —

---

## 🚀 Quick Use

1. Paste your **TARGET PROTOCOL** below.
2. Open each **Toggle Section** in order (Steps 1→6).
3. Complete the tables/checklists.
4. Deliver the **Enhanced Protocol** and **Change Log** exactly as specified.

---

## 📌 Output Headers (exact; copy/paste)

```
CLASSIFICATION
STRUCTURAL AUDIT
AMBIGUITY ANALYSIS
COMPLETENESS VERIFICATION
ENHANCED PROTOCOL
CHANGE LOG

```

---

## 🧩 STEP 1 — PROTOCOL CLASSIFICATION (Toggle)

**Instructions:** 1–2 sentences.

- **Protocol type:** [meta‑instruction | system instruction | reasoning framework | hybrid]
- **Primary objective:** [one sentence describing the achieved outcome]

**Example:**

> This is a system instruction protocol. Its primary objective is to generate API documentation from code comments with >90% completeness.
> 

---

## 🧱 STEP 2 — STRUCTURAL AUDIT (Toggle)

**Instructions:** Create a **numbered list** of every instruction. For each, extract:

- **Instruction ID**
- **Original text (quote)**
- **Action required** (verb phrase: "extract X", "classify Y as Z", "output format Q")
- **Input dependencies** (what must exist | "none" | **UNDEFINED**)
- **Success criteria** (how to verify | **MISSING**)

**Per‑Instruction Table (duplicate rows as needed):**

| ID | Original Quote | Action Required | Input Dependencies | Success Criteria | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | "…" | extract/classify/output… | none/UNDEFINED/… | metric or **MISSING** | — |

**Global Findings:**

- **Circular dependencies:** A↔B pairs → …
- **Undefined terms:** …
- **Implicit assumptions:** *The protocol assumes…*

---

## 🧭 STEP 3 — AMBIGUITY DETECTION (Toggle)

**Apply tests to each instruction from Step 2:**

**Test 1 — Action Clarity**

- Can it be executed via a specific algorithm/procedure?
    - **YES** → `[CLEAR]`
    - **NO** → `[AMBIGUOUS]` → *Unclear because …*

**Test 2 — Output Specification**

- Output format explicitly defined?
    - **YES** → list format
    - **NO** → `[OUTPUT UNDEFINED]`

**Test 3 — Branching Logic**

- Requires conditional execution?
    - **YES** but conditions missing → `[MISSING CONDITIONS]`
    - **NO** → `[LINEAR]`
    - **YES** with conditions → list conditions

**Per‑Instruction Tag Sheet (example):**

| ID | Action Clarity | Output Spec | Branching Logic | Comment |
| --- | --- | --- | --- | --- |
| 1 | CLEAR / AMBIGUOUS | DEFINED / **OUTPUT UNDEFINED** | LINEAR / **MISSING CONDITIONS** / CONDITIONS: … | … |

---

## 🧮 STEP 4 — COMPLETENESS CHECK (Toggle)

**Verify required components:**

| Component | Present? | Evidence / Gap |
| --- | --- | --- |
| Input format specification | Y/N | Quote or "Missing: no input format specified" |
| Processing steps (sequential) | Y/N | Count of steps or "Missing: only outcome described" |
| Output format specification | Y/N | Quote or "Missing: format not defined" |
| Success/failure criteria | Y/N | Quote or "Missing: no validation criteria" |
| Edge case handling | Y/N | Quote or "Missing: no error conditions addressed" |
| Termination conditions | Y/N | Quote or "Missing: completion state unclear" |

---

## 🔁 STEP 5 — ENHANCED PROTOCOL GENERATION (Toggle)

**Rewrite using the transformations below. Preserve original intent.**

**Transformation A — Concretize Abstract Verbs**

- "Analyze X" → `1) Extract [specific elements] from X 2) Classify into [category set] 3) Output as [format]`
- "Improve Y" → `1) Measure Y vs [metric with units] 2) IF < [threshold] THEN apply [technique] 3) Validate via [test]`
- "Evaluate Z" → `1) Score on [scale] using [rubric] 2) Document evidence as [format] 3) Compare to [baseline]`

**Transformation B — Externalize Implicit Information**

Add for every instruction missing Step‑4 components:

- **Input:** exact required data
- **Process:** numbered sub‑steps / algorithm
- **Output:** explicit format + example/template
- **Validation:** `Success if [measurable condition]`

**Transformation C — Eliminate Subjective Terms**

- "high quality" → `error rate < 2%`
- "comprehensive" → `includes all 8 required sections`
- "thorough" → `minimum 3 levels of hierarchy`
- "appropriate" → `matches pattern [X]`

**Transformation D — Specify Conditional Logic**

```
IF [measurable condition] THEN [specific action + output]
ELSE IF [measurable condition] THEN [specific action + output]
ELSE [default action + output]

```

**Enhanced Protocol Scaffold (repeat per instruction):**

```
ID N — [Short Title]
Input: …
Process: 1) … 2) … 3) …
Output: format + path/example
Validation: Success if [metric/threshold]; else trigger [fallback].

```

---

## 📝 STEP 6 — CHANGE DOCUMENTATION (Toggle)

**Exact table (≥ 3 entries when issues exist):**

| Original Instruction (quote) | Issue Category | Enhancement Applied | Measurable Improvement |
| --- | --- | --- | --- |
| "…" | Ambiguous verb / Undefined output / Missing validation / Implicit dependency | … | Before: X → After: Y |

> Note: If the source truly has <3 issues, state that and avoid fabricating entries.
> 

---

## 🛡️ Constraints (Callout)

> Preserve Original Intent — don’t add scope beyond objectives.Quote Precisely — include exact text (+ line refs if available).Flag Uncertainty — multiple interpretations → list all with INTERPRETATION AMBIGUITY.No Capability Inference — don’t assume unstated abilities.Evidence‑Based — every issue must cite protocol text.
> 

---

## 🚫 Anti‑Patterns to Avoid (Callout)

- Rating things as "good/bad" (use criteria).
- Adding scope beyond intent.
- Hedging ("might/could/possibly"): be definitive **or** mark **UNCERTAIN**.
- Skipping sections.
- Generic advice without quoting specific text.

---

## ✅ Execution Checklist

- [ ]  Steps **1→6** completed in order
- [ ]  Every claim cites **specific text**
- [ ]  Enhanced version has **zero subjective terms**
- [ ]  All conditionals use **IF / THEN / ELSE**
- [ ]  Change Log has **≥ 3** real entries (or explicitly justified fewer)
- [ ]  No assumptions about **unstated capabilities**

---

## 🗂️ TARGET PROTOCOL (paste here)

```
# Stage 1: Role & Intent Explainer

**Purpose:** Define the role and clarify the intent of your meta prompt. This is the foundation of your prompt building process.

---

## 📝 Role Definition

**Instructions:** Describe the specific role or persona the AI should adopt.

### Role Description

- **Template**
    
    *Example: "You are an expert data analyst specializing in financial modeling and predictive analytics..."*
    
    **[YOUR ROLE DESCRIPTION HERE]**
    

---

## 🎯 Intent Explanation

**Instructions:** Clearly articulate what you want to achieve with this prompt.

### Primary Intent

- **Template**
    
    *Example: "The primary intent is to analyze quarterly revenue data and identify emerging trends..."*
    
    **[YOUR PRIMARY INTENT HERE]**
    

### Secondary Objectives

- **Template**
    
    *Example: "Secondary objectives include identifying anomalies and providing actionable recommendations..."*
    
    **[YOUR SECONDARY OBJECTIVES HERE]**
    

---

## 🔤 User Input Section

**Instructions:** Enter your custom prompt or query that will be enhanced through this meta prompt system.

### Your Custom Prompt

> [PASTE YOUR INITIAL PROMPT/QUERY HERE]
> 

---

## 📤 Output: Intent Document

✅

**Copy this complete output and paste it into the Reasoning Synthesizer's input section.**

- **Generated Intent Document (Ready to Copy)**
    
    **Role:** [Your role description from above]
    
    **Primary Intent:** [Your primary intent from above]
    
    **Secondary Objectives:** [Your secondary objectives from above]
    
    **User Query:** [Your custom prompt from above]
    
    ---
    
    **Next Step:** Copy this entire document and proceed to **Meta-Prompt: Reasoning Synthesizer (RS)**
    

---

# Stage 2: Reasoning Synthesizer (RS)

📍

**Purpose:** Structure the logical reasoning approach based on the intent defined in Stage 1. This stage builds the cognitive framework for your meta prompt.

---

## 📥 Input from Previous Stage

**Instructions:** Paste the Intent Document output from the Role: Intent Explainer page.

### Intent Document Input

> [PASTE INTENT DOCUMENT FROM STAGE 1 HERE]
> 

---

## 🧠 Reasoning Framework

**Instructions:** Define the reasoning approach the AI should use.

### Reasoning Type

- **Select Approach**
    - [ ]  Deductive Reasoning (General principles → Specific conclusions)
    - [ ]  Inductive Reasoning (Specific observations → General principles)
    - [ ]  Abductive Reasoning (Best explanation for observations)
    - [ ]  Analogical Reasoning (Drawing parallels from similar cases)
    - [ ]  Causal Reasoning (Cause and effect relationships)
    
    **Selected Approach:** [Specify here]
    

### Reasoning Steps

- **Template**
    
    **Step 1:** [Define first reasoning step]
    
    **Step 2:** [Define second reasoning step]
    
    **Step 3:** [Define third reasoning step]
    
    **[Add more steps as needed]**
    

---

## 🔍 Analysis Parameters

### Key Considerations

- **Template**
    - **Context Analysis:** [What contextual factors should be considered?]
    - **Assumptions:** [What assumptions are acceptable?]
    - **Constraints:** [What limitations exist?]
    - **Success Criteria:** [How will success be measured?]

---

## 📤 Output: Reasoning Structure

✅

**Copy this complete output and paste it into the Logic Planner's input section.**

</aside>

- **Generated Reasoning Structure (Ready to Copy)**
    
    **Intent Reference:** [From Stage 1]
    
    **Reasoning Approach:** [Your selected approach]
    
    **Reasoning Steps:**
    
    [Your defined reasoning steps from above]
    
    **Analysis Parameters:**
    
    [Your key considerations from above]
    
    ---
    
    **Next Step:** Copy this entire document and proceed to **Meta-Prompt: Logic Planner (LP)**
    

---

# Stage 3: Logic Planner (LP)

**Purpose:** Map out the decision-making framework and logical pathways. This stage creates the execution blueprint for your meta prompt.

---

## 📥 Input from Previous Stage

**Instructions:** Paste the Reasoning Structure output from the Reasoning Synthesizer page.

### Reasoning Structure Input

> [PASTE REASONING STRUCTURE FROM STAGE 2 HERE]
> 

---

## 🗺️ Logic Mapping

**Instructions:** Define the logical flow and decision points.

### Decision Tree

- **Logical Pathways**
    
    **Primary Path:**
    
    - Condition 1: [If X, then Y]
    - Condition 2: [If A, then B]
    - Default: [Otherwise, Z]
    
    **[DEFINE YOUR LOGIC PATHWAYS HERE]**
    

### Conditional Logic

- **Template**
    
    **IF** [Condition]:
    
    **THEN** [Action/Output]
    
    **ELSE IF** [Alternative Condition]:
    
    **THEN** [Alternative Action]
    
    **ELSE**:
    
    **THEN** [Default Action]
    
    **[ADD YOUR CONDITIONAL LOGIC HERE]**
    

---

## ⚙️ Processing Sequence

### Execution Order

- **Template**
    1. **Initial Processing:** [What happens first?]
    2. **Analysis Phase:** [What gets analyzed and how?]
    3. **Evaluation Phase:** [What criteria are applied?]
    4. **Synthesis Phase:** [How are results combined?]
    5. **Finalization:** [What final steps occur?]
    
    **[DEFINE YOUR PROCESSING SEQUENCE HERE]**
    

---

## 🎲 Edge Cases & Exceptions

### Exception Handling

- **Template**
    - **Edge Case 1:** [Scenario] → [Handling approach]
    - **Edge Case 2:** [Scenario] → [Handling approach]
    - **Fallback Strategy:** [Default approach when edge cases aren't covered]
    
    **[DEFINE YOUR EDGE CASES HERE]**
    

---

## 📤 Output: Logic Blueprint

**Copy this complete output and paste it into the Format Designer's input section.**

- **Generated Logic Blueprint (Ready to Copy)**
    
    **Reasoning Reference:** [From Stage 2]
    
    **Logic Pathways:**
    
    [Your decision tree from above]
    
    **Conditional Logic:**
    
    [Your conditional statements from above]
    
    **Processing Sequence:**
    
    [Your execution order from above]
    
    **Exception Handling:**
    
    [Your edge cases from above]
    
    ---
    
    **Next Step:** Copy this entire document and proceed to **Meta-Prompt: Format Designer/Mapper (FD)**
    

---

# Stage 4: Format Designer/Mapper (FD)

📍

**Purpose:** Define the output structure, formatting, and presentation requirements. This stage ensures your meta prompt produces results in the desired format.

---

## 📥 Input from Previous Stage

**Instructions:** Paste the Logic Blueprint output from the Logic Planner page.

### Logic Blueprint Input

> [PASTE LOGIC BLUEPRINT FROM STAGE 3 HERE]
> 

---

## 🎨 Output Format Specification

**Instructions:** Define how the final output should be structured.

### Format Type

- **Select Format Family** *(use these curated templates as primary anchors; see `meta-analysis/examples/` references)*
    - [ ]  **Execution – Basic Protocol** (Phase 1-4 checklist with simple actions; ideal for linear workflows). Reference: `EXECUTION-FORMATS.md` → Template Format 2 @meta-analysis/examples/EXECUTION-FORMATS.md#1-167
    - [ ]  **Execution – Numbered Substeps** (Detailed substeps such as 1.1/1.2; use when precise tracking is required). Reference: `EXECUTION-FORMATS.md` → Template Format 3 @meta-analysis/examples/EXECUTION-FORMATS.md#168-353
    - [ ]  **Execution – Reasoning Blocks** (Includes `[REASONING]` sections for decisions; pick for audit-heavy or multi-alternative analysis). Reference: `EXECUTION-FORMATS.md` → Template Format 4 @meta-analysis/examples/EXECUTION-FORMATS.md#354-744
    - [ ]  **Guidelines – Rules & Standards** (YAML frontmatter plus `[STRICT]/[GUIDELINE]` markers; best for policy or coding standards). Reference: `GUIDELINES-FORMATS.md` @meta-analysis/examples/GUIDELINES-FORMATS.md#1-124
    - [ ]  **Issue Tracking – GitHub/Jira** (9-subtask issue breakdown with priority tags; use when output must become work items). Reference: `ISSUE-FORMATS.md` @meta-analysis/examples/ISSUE-FORMATS.md#1-65
    - [ ]  **Prompt Engineering – Multi-Role Pack** (System/Developer/User split; suited for multi-agent orchestration). Reference: `PROMPT-FORMATS.md` @meta-analysis/examples/PROMPT-FORMATS.md#1-58
    - [ ]  **Meta-System – Instruction Creator** (Generates protocol generators and input forms; choose for templating new protocol builders). Reference: `META-FORMATS.md` @meta-analysis/examples/META-FORMATS.md#1-137
    - [ ]  **Custom/Hybrid Format** (Document why existing families are insufficient; blend elements as needed and note validation impact). Reference decision matrix: `FORMAT-ANALYSIS.md` @meta-analysis/examples/FORMAT-ANALYSIS.md#90-212
    
    **Selected Format Family:** [Specify here]
    
- **Optional Output Container** *(choose presentation wrapper once the format family is set)*
    - [ ]  Structured Report / Narrative (long-form prose with sections)
    - [ ]  Markdown Document (H1-H3 headings, lists, callouts)
    - [ ]  Table / Spreadsheet (tabular data emphasis)
    - [ ]  JSON / YAML (machine-readable schema)
    - [ ]  Bullet / Checklist (condensed action items)
    - [ ]  CLI / Plain Text (minimal formatting for terminal outputs)
    - [ ]  Issue Export (one issue per deliverable)
    
    **Selected Output Container:** [Specify here]
    

### Structure Template

- **Output Structure**
    
    **Section 1: [Title]**
    
    - Component 1.1: [Description]
    - Component 1.2: [Description]
    
    **Section 2: [Title]**
    
    - Component 2.1: [Description]
    - Component 2.2: [Description]
    
    **[DEFINE YOUR OUTPUT STRUCTURE HERE]**
    

---

## 📏 Formatting Rules

### Style Guidelines

- **Template**
    
    **Tone:** [Professional / Casual / Technical / etc.]
    
    **Length:** [Brief / Moderate / Comprehensive]
    
    **Language Complexity:** [Simple / Intermediate / Advanced]
    
    **Point of View:** [First person / Third person]
    
    **[SPECIFY YOUR STYLE PREFERENCES HERE]**
    

### Presentation Elements

- **Template**
    - **Headings:** [H1, H2, H3 usage guidelines]
    - **Emphasis:** [Bold, italic, underline preferences]
    - **Lists:** [Numbered, bulleted, nested]
    - **Visual Elements:** [Tables, callouts, dividers]
    - **Citations:** [How to reference sources]
    
    **[DEFINE YOUR PRESENTATION RULES HERE]**
    

---

## 📊 Data Visualization Requirements

### Visual Format

- **Template**
    
    **If applicable:**
    
    - Chart Type: [Bar / Line / Pie / Table]
    - Data Labels: [Yes / No]
    - Legend Position: [Top / Bottom / Right]
    
    **[SPECIFY VISUALIZATION NEEDS HERE]**
    

---

## ✅ Quality Standards

### Output Criteria

- **Template**
    - **Completeness:** [What must be included?]
    - **Accuracy:** [What verification is needed?]
    - **Clarity:** [Readability requirements]
    - **Consistency:** [Formatting uniformity]
    
    **[DEFINE YOUR QUALITY STANDARDS HERE]**
    

---

## 📤 Output: Format Specification

✅

**Copy this complete output and paste it into the Concordance & Alignment Validator's input section.**

- **Generated Format Specification (Ready to Copy)**
    
    **Logic Reference:** [From Stage 3]
    
    **Output Format:**
    
    [Your format type and structure template from above]
    
    **Formatting Rules:**
    
    [Your style guidelines from above]
    
    **Presentation Elements:**
    
    [Your presentation rules from above]
    
    **Quality Standards:**
    
    [Your output criteria from above]
    
    ---
    
    **Next Step:** Copy this entire document and proceed to **Meta-Prompt: Concordance & Alignment Validator (CAV)**
    

---

# Stage 5: Concordance & Alignment Validator (CAV)

📍

**Purpose:** Validate consistency and alignment across all meta prompt components. This final stage ensures coherence and produces your complete, production-ready meta prompt.

---

## 📥 Input from Previous Stage

**Instructions:** Paste the Format Specification output from the Format Designer page.

### Format Specification Input

> [PASTE FORMAT SPECIFICATION FROM STAGE 4 HERE]
> 

---

## 🔍 Alignment Validation

**Instructions:** Review and validate alignment across all stages.

### Cross-Stage Consistency Check

- **Validation Checklist**
    - [ ]  **Intent ↔ Reasoning:** Does the reasoning approach support the stated intent?
    - [ ]  **Reasoning ↔ Logic:** Do the logic pathways follow the reasoning framework?
    - [ ]  **Logic ↔ Format:** Does the format accommodate the logical structure?
    - [ ]  **Overall Coherence:** Do all components work together seamlessly?
    
    **Notes on Alignment Issues:** [Document any inconsistencies found]
    

---

## ⚖️ Concordance Assessment

### Component Integration

- **Integration Review**
    
    **Role & Intent Alignment:**
    
    - Is the role appropriate for the intent? [Yes / No / Needs adjustment]
    - Notes: [Your assessment]
    
    **Reasoning & Logic Alignment:**
    
    - Do the logic pathways support the reasoning approach? [Yes / No / Needs adjustment]
    - Notes: [Your assessment]
    
    **Format & Purpose Alignment:**
    
    - Does the output format serve the intended purpose? [Yes / No / Needs adjustment]
    - Notes: [Your assessment]

---

## 🔧 Refinement Recommendations

### Optimization Suggestions

- **Template**
    
    **Identified Gaps:**
    
    1. [Gap or inconsistency found]
    2. [Gap or inconsistency found]
    
    **Recommended Adjustments:**
    
    1. [Suggested improvement]
    2. [Suggested improvement]
    
    **[ADD YOUR REFINEMENT NOTES HERE]**
    

---

## ✨ Final Meta Prompt Assembly

🎯

**This is your complete, validated meta prompt ready for use with AI systems.**

### Complete Meta Prompt Document

- **Production-Ready Meta Prompt (Ready to Copy)**
    
    ---
    
    **META PROMPT - FINAL VERSION**
    
    ---
    
    **ROLE & INTENT**
    
    [Paste from Stage 1]
    
    **REASONING FRAMEWORK**
    
    [Paste from Stage 2]
    
    **LOGIC STRUCTURE**
    
    [Paste from Stage 3]
    
    **OUTPUT FORMAT**
    
    [Paste from Stage 4]
    
    **VALIDATION STATUS**
    
    ✅ All components aligned and validated
    
    ---
    
    **USAGE INSTRUCTIONS:**
    
    Copy this entire meta prompt and submit it to your AI system. The AI will follow the structured framework to produce outputs that meet your specifications.
    
    ---
    

---

## 📋 Meta Prompt Template (Blank)

📝

**Quick-Copy Template:** Use this structure for direct AI submission after filling in your components.

- **Template Structure**

---

## 🔄 Iteration & Refinement

### Feedback Loop

- **Post-Execution Review**
    
    **After using your meta prompt:**
    
    - What worked well? [Document successes]
    - What needs improvement? [Document issues]
    - Adjustments to make: [Plan next iteration]
    
    **Return to:** [Role: Intent Explainer](https://www.notion.so/Role-Intent-Explainer-29cd71a8c0e981378210f00be1d0184a?pvs=21) to refine and iterate
    

---

## 🎉 Congratulations!

You've completed the meta prompt builder workflow. Your structured meta prompt is now ready to use with any AI system for enhanced, predictable, and aligned results.
```

---

## 📦 Deliverables (final paste section)

### CLASSIFICATION

*(Step 1 output — max 2 sentences)*

### STRUCTURAL AUDIT

*(Step 2 list/table)*

### AMBIGUITY ANALYSIS

*(Step 3 tags/results)*

### COMPLETENESS VERIFICATION

*(Step 4 table)*

### ENHANCED PROTOCOL

*(Step 5 rewrite with Input / Process / Output / Validation per instruction)*

### CHANGE LOG

*(Step 6 table)*

---

## 🔗 Reference Snippets

**Branching Logic**

```
IF [measurable condition] THEN [action + output]
ELSE IF [measurable condition] THEN [action + output]
ELSE [default action + output]

```

**Rubric Anchors (0–10)**

```
0–2: missing/incorrect • 3–5: partial • 6–7: adequate • 8–9: strong • 10: exemplary (evidence cited)

```

**Validation Line**

```
Success if [metric with units/threshold]; otherwise trigger [fallback].

```