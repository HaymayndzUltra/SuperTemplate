# Stage 4: Format Designer/Mapper (FD)

<aside>
📍

**Purpose:** Define the output structure, formatting, and presentation requirements. This stage ensures your meta prompt produces results in the desired format.

</aside>

---

## 📥 Input from Previous Stage

**Instructions:** Paste the Logic Blueprint output from the Logic Planner page.

### Logic Blueprint Input

> **[PASTE LOGIC BLUEPRINT FROM STAGE 3 HERE]**
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

<aside>
✅

**Copy this complete output and paste it into the Concordance & Alignment Validator's input section.**

</aside>

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

## ⬅️ Previous Stage | ➡️ Next Stage

[Meta-Prompt: Logic Planner (LP)](https://www.notion.so/Meta-Prompt-Logic-Planner-LP-29cd71a8c0e9812d8471e2eb663f7597?pvs=21) | [Meta-Prompt: Concordance & Alignment Validator (CAV)](https://www.notion.so/Meta-Prompt-Concordance-Alignment-Validator-CAV-29cd71a8c0e981e28340fd8d0a5b7ce2?pvs=21)