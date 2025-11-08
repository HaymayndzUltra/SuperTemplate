# Template: Guidelines Format

**Source**: GUIDELINES-FORMATS.md  
**Use Case**: Master rules, coding standards, protocol guidelines  
**Key Features**:
- YAML frontmatter with metadata
- Step-based structure (Step 1-5)
- Phase sub-sections within steps
- [STRICT] and [GUIDELINE] markers
- DO/DON'T examples

---

## TEMPLATE STRUCTURE

```markdown
---
description: "{TAGS} | {TRIGGERS} | {SCOPE} | DESCRIPTION: {Description}"
alwaysApply: {boolean}
---

# {Protocol_Title}: {Protocol_Name}

## 1. {Section_1_Name}

{Section_1_Description}.

**[STRICT] {Critical_Directive}.**

## 2. {Section_2_Name}

{Section_2_Description}.

## 3. {Section_3_Name}

{Section_3_Description}:
-   `{Marker_1}`: {Marker_1_Description}
-   `{Marker_2}`: {Marker_2_Description}

## 4. {Section_4_Name}

### **[STRICT] {Subsection_4_1_Name}**
{Subsection_4_1_Description}:
1.  *"{Step_1_Placeholder}"*
2.  *"{Step_2_Placeholder}"*
3.  *"{Step_3_Placeholder}"*
4.  *"{Step_4_Placeholder}"*

**[STRICT]** {Follow_Up_Directive}.

### {Subsection_4_2_Name}
- **[STRICT]** {Principle_1}.
- **[STRICT]** {Principle_2}.

### {Subsection_4_3_Name}
**[STRICT]** {Protocol_Description}:
- **{Guideline_1}** - {Guideline_1_Description}
- **{Guideline_2}** - {Guideline_2_Description}

### Step 1: {Step_1_Name}
**[STRICT]** {Step_1_Description}.

1.  **Phase 1: {Phase_1_Name}**
    *   **Action:** {Action}.
    *   **Verification Required:** {Verification}.
    *   **Scope:** {Scope}.

2.  **Phase 2: {Phase_2_Name}**
    *   **Principle:** {Principle}.
    *   **Action:** {Action}.

### Step 2: {Step_2_Name}
**[STRICT]** {Step_2_Description}:
1.  {Element_1}.
2.  {Element_2}.
3.  **[STRICT]** {Element_3}.
4.  **[GUIDELINE]** {Element_4}.

### Step 3: {Step_3_Name}
**[STRICT]** {Step_3_Objective}.

1.  **Priority 1: {Priority_1_Name}**
    *   **[STRICT]** {Priority_1_Rule_1}.
    *   **[STRICT]** {Priority_1_Rule_2}.

2.  **Priority 2: {Priority_2_Name}**
    *   **[STRICT]** {Priority_2_Description}.

### Step 4: {Step_4_Name}
**[STRICT]** {Step_4_Primary_Directive}.

### Step 5: {Step_5_Name}
**[STRICT]** {Step_5_Description}:

1. **{Checkpoint_1_Name}:**
   - **[STRICT]** {Checkpoint_1_Condition} → {Checkpoint_1_Action}.

2. **{Checkpoint_2_Name}:**
   - **[STRICT]** {Checkpoint_2_Condition} → {Checkpoint_2_Action}.

#### ✅ {Correct_Format_Section}

> **Example 1:** *"{Example_1_Header}"*
> *"{Example_1_Message}"*

> **Example 2:** *"{Example_2_Header}"*
> *"{Example_2_Message}"*

#### ❌ {Incorrect_Format_Section}
> *"{Anti_Pattern_Example}"*
>
> **({Anti_Pattern_Reasoning})**

---

## VALIDATION CRITERIA
- [ ] {Validation_Criterion_1}
- [ ] {Validation_Criterion_2}
- [ ] {Validation_Criterion_3}
```

---

## WHEN TO USE

✅ **Use this template when:**
- Creating master rules for AI agents
- Defining coding standards and conventions
- Setting up protocol guidelines with strict enforcement
- Documenting behavioral constraints and requirements

❌ **Do NOT use this template when:**
- Executing workflow processes (use EXECUTION template)
- Creating project issues (use ISSUE template)
- Multi-agent orchestration (use PROMPT template)

---

## CUSTOMIZATION GUIDELINES

### YAML Frontmatter
```yaml
---
description: "data-strategy | planning | ai-workflow | DESCRIPTION: Comprehensive data strategy planning guidelines"
alwaysApply: false
---
```

### Directive Markers
- **`[STRICT]`**: Non-negotiable requirements
- **`[GUIDELINE]`**: Strong recommendations with flexibility
- **`[CRITICAL]`**: Safety-critical constraints

### Section Structure
- **Step-based**: Organize into logical steps (1-5)
- **Phase sub-sections**: Break complex steps into phases
- **Priority levels**: Distinguish between critical and optional requirements

### Examples Format
```markdown
#### ✅ Correct Approach
> **Example:** "Proper data source documentation"
> "Include source name, access method, update frequency, and quality metrics"

#### ❌ Common Mistakes  
> "Vague data references without specifics"
> **(Missing critical details for downstream implementation)**
```

---

## DATA STRATEGY SPECIFIC ADAPTATIONS

### For Data Strategy Guidelines:
```markdown
## 1. Data Source Identification
**[STRICT]** All data sources must be documented with access feasibility.

## 2. Volume Requirements
**[STRICT]** Calculate minimum viable dataset size per use case.

## 3. Quality Standards
### **[STRICT] Data Quality Framework**
1.  *"Completeness: Minimum 95% non-null values"*
2.  *"Accuracy: Validation against ground truth"*
3.  *"Consistency: Cross-source validation rules"*
4.  *"Timeliness: Maximum data age requirements"*

**[STRICT]** Document quality validation procedures.
```

---

*Guidelines Template - For rules, standards, and protocol guidelines*
