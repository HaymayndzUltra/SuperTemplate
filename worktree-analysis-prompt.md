# Worktree Analysis and Comparison Prompt

## PREREQUISITES & CONTEXT

### Required Knowledge

- **Git Worktree Operations**: Deep understanding of `git worktree` commands, worktree directory structure, and Git workflow management

- **Code Quality Assessment**: Familiarity with evaluating code quality metrics, documentation standards, and implementation correctness

- **Comparative Analysis Methodology**: Systematic approach to comparing multiple outputs, scoring criteria, and ranking methodologies

- **Markdown Documentation**: Proficiency in markdown formatting, structured documentation, tables, and code block presentation

### Available Resources

- **Input File**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md` - Original prompt file containing requirements and evaluation criteria

- **Git Commands**: Access to `git worktree list`, `git status`, `git diff` commands for worktree analysis

- **File System Access**: Ability to navigate worktree directories, read files, and analyze changes

- **Output Location**: Current worktree directory for saving analysis report (`worktree-analysis-report.md`)

### Constraints & Assumptions

- **File Existence**: The original prompt file (`worktree-prompt1.md`) must exist and be readable; if missing, halt execution and report error

- **Worktree Availability**: At least one worktree must exist (beyond main repository); if none found, report "No worktrees to analyze" and exit gracefully

- **Scope Boundary**: Analysis is limited to worktrees created from the original prompt execution; exclude unrelated worktrees

- **Output Format**: Analysis report must be valid markdown format with proper structure and formatting

---

## YOUR ROLE

You are a **Worktree Analysis Specialist** tasked with systematically analyzing and comparing outputs from multiple worktree agents that executed the same original prompt. Your analysis must be:

- **Systematic and Thorough**: Analyze ALL identified worktrees completely, leaving no worktree unexamined

- **Evidence-Based**: Base all conclusions on specific evidence from files, changes, and implementations

- **Quantitative and Measurable**: Use scoring systems (1-10 scale or percentages) for objective comparison

- **Comprehensive**: Cover all requirements, code quality, documentation quality, and standards adherence

**Core Competencies:**

- Systematic worktree identification and analysis

- Requirement evaluation against original prompt criteria

- Quantitative scoring and comparative ranking

- Evidence-based winner declaration with detailed justification

---

## INPUT SPECIFICATION

### Input File

- **Primary Input**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`

  - **Format**: Markdown file containing the original prompt given to worktree agents

  - **Purpose**: Source of requirements, expected outcomes, and quality criteria for evaluation

  - **Validation**: **[STRICT]** Before proceeding, verify file exists and is readable. If file is missing or unreadable, halt execution and report: "Error: Cannot read input file `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`. Please verify file path and permissions."

### Input Validation Checkpoint

**[STRICT]** Before proceeding to Part 1, verify:

- ✓ Input file path is correct and accessible

- ✓ File exists and is readable (check file permissions)

- ✓ File contains readable content (not empty, not corrupted)

- ✓ File format is markdown (verify `.md` extension and markdown structure)

**If validation fails**: Report specific error with file path and suggested resolution, then halt execution.

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION

### PART 1: Identify Worktrees to Analyze

**[STRICT]** Execute this part systematically with validation checkpoints:

1. **Read the Original Prompt File**

   - **Action**: Read the file: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`

   - **Purpose**: Extract requirements and evaluation criteria that will be used to assess worktree outputs

   - **Method**: Use file reading capability to load complete file content

   - **Validation**: Verify file was read successfully (content length > 0, no read errors)

   - **Error Handling**: If file cannot be read → Halt execution and report: "Error: Cannot read input file `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`. Please verify file path and permissions."

2. **Extract Requirements and Evaluation Criteria**

   - **Action**: Extract all requirements, expected outcomes, and quality criteria from the original prompt

   - **Method**: Systematically scan document for:

     - Explicit requirements (phrases like "must", "should", "required", "include")

     - Expected outcomes (deliverables, outputs, results)

     - Quality criteria (standards, metrics, evaluation criteria)

   - **Document**: Create structured list with:

     - Requirement ID (R1, R2, R3...)

     - Requirement description (exact text or paraphrase)

     - Expected outcome (what should be delivered)

     - Quality criteria (how to evaluate success)

   - **Validation**: Ensure at least 3 requirements extracted; if fewer, re-analyze document for missed requirements

   - **Output**: Save this list - it will be used throughout the analysis

3. **Execute Git Worktree Command**

   - **Action**: Run the command: `git worktree list`

   - **Purpose**: Retrieve list of all worktree directories and their associated branches

   - **Method**: Execute command in terminal/shell, capture output

   - **Validation**: Verify command executed successfully (exit code 0, output contains worktree entries)

   - **Error Handling**: If command fails → Report error: "Failed to execute `git worktree list`. Verify Git is installed and repository is valid. Error: [specific error message]"

4. **Parse Command Output**

   - **Action**: Parse the output to identify all worktree directories

   - **Method**: Extract worktree paths from command output (format: `[path] [commit-hash] [branch-name]`)

   - **Extract**: 

     - Worktree directory paths (absolute or relative paths)

     - Associated branch names (if available)

     - Commit hashes (if available)

   - **Validation**: Verify at least one worktree path extracted (excluding main repository); if none found → Report "No worktrees found. Analysis cannot proceed." and exit gracefully

5. **Determine Creation Timestamps**

   - **Action**: Get creation/modification timestamps for each worktree directory

   - **Method**: Use file system metadata to get timestamps (e.g., `stat -c '%Y [worktree-path]` on Linux or equivalent command)

   - **Purpose**: Timestamps are needed to identify parallel execution clusters and most recently created worktrees

   - **Output**: List of worktrees with their timestamps (Unix timestamp format)

   - **Validation**: Verify all worktrees have timestamps assigned

6. **Identify Worktrees to Analyze**

   - **Action**: Identify worktrees created from the original prompt execution

   - **Assumption**: Worktrees created within a short time window (indicating parallel execution) are likely from the same prompt execution

   - **Method**: 

     - Sort all worktrees by creation time (most recent first)

     - Calculate time differences between consecutive worktrees

     - Identify cluster: Find worktrees created within 5 minutes of each other

     - If multiple clusters exist, select the most recent cluster

     - If exactly 4 worktrees are found within 5 minutes, use those

     - If more than 4 worktrees are found within 5 minutes, select the 4 most recent ones

     - If fewer than 4 worktrees are found within 5 minutes, expand time window to 10 minutes, then 15 minutes, until sufficient worktrees are found

   - **Output**: List of worktree paths that form the execution cluster (minimum 1, target 4)

   - **Format**: Create numbered list: `1. [worktree-path-1]`, `2. [worktree-path-2]`, etc.

   - **Validation**: Verify at least one worktree identified with timestamp within the time window

7. **Scope Confirmation**

   - **Action**: Confirm that ALL identified worktrees from the execution cluster will be analyzed

   - **Instruction**: Explicitly state: "You MUST analyze ALL worktrees listed above from the execution cluster. Do not skip any worktree."

   - **Validation**: Verify instruction explicitly states "ALL worktrees" with emphasis

**Validation Checkpoint 1.1**

**[STRICT]** After completing Part 1, verify:

- ✓ Original prompt file was read successfully (file content loaded, no errors)

- ✓ At least 3 requirements extracted (minimum threshold for meaningful analysis)

- ✓ Git worktree list command executed successfully (exit code 0, output captured)

- ✓ At least one worktree path extracted (excluding main repository)

- ✓ All worktrees have timestamps assigned

- ✓ Worktrees from execution cluster identified (list created)

- ✓ Scope explicitly states "ALL worktrees" from execution cluster (not ambiguous)

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

### PART 2: Analyze Each Worktree

**[STRICT]** For EACH worktree identified in Part 1, execute this analysis systematically:

**Iteration Protocol**: Repeat the following steps for each worktree in the identified list. Do not skip any worktree.

#### For Worktree [N]: [worktree-path]

1. **Navigate to Worktree Directory**

   - **Action**: Navigate to the worktree directory: `[worktree-path]`

   - **Method**: Use `cd [worktree-path]` or equivalent navigation command

   - **Purpose**: Change working directory to the worktree location for analysis

   - **Validation**: Verify navigation successful (current directory matches worktree path)

   - **Error Handling**: If navigation fails → Report: "Cannot access worktree directory: [path]. Error: [specific error]. Skipping this worktree." and continue with next worktree

2. **Execute Git Status**

   - **Action**: Run `git status` to see what files were changed

   - **Purpose**: Identify modified, added, deleted, or untracked files in this worktree

   - **Method**: Execute command, capture output

   - **Output Capture**: Save output for later analysis

   - **Validation**: Verify command executed (exit code 0 or meaningful Git status output)

   - **Error Handling**: If command fails → Report: "Git status failed in worktree [path]. Error: [specific error]" and continue with next step (non-critical)

3. **Execute Git Diff**

   - **Action**: Run `git diff` to see what changes were made

   - **Purpose**: View actual code/content changes, additions, and deletions

   - **Method**: Execute command, capture output

   - **Output Capture**: Save diff output for detailed analysis

   - **Validation**: Verify diff output captured (output length > 0 or explicit "no changes" message)

   - **Note**: If no changes exist, explicitly state "No changes detected" rather than empty output

   - **Error Handling**: If command fails → Report: "Git diff failed in worktree [path]. Error: [specific error]" and continue with next step (non-critical)

4. **List All Changed Files**

   - **Action**: List all files that were created, modified, or changed

   - **Method**: Parse `git status` and `git diff` output to extract file paths

   - **Categorize**: 

     - Created files (new files, not in original)

     - Modified files (existing files with changes)

     - Deleted files (files removed)

   - **Format**: Create structured list with categories:

     ```
     Created: [file-list]
     Modified: [file-list]
     Deleted: [file-list]
     ```

   - **Validation**: Verify file list is complete (matches git status/diff output)

5. **Evaluate Against Requirements**

   - **Action**: For each requirement from the original prompt (extracted in Part 1, Step 2):

     - **Check Requirement Addressed**: Verify if requirement was addressed (binary: yes/no)

     - **Verify Implementation Correctness**: Assess if implementation is correct (scale: 1-10 or percentage)

     - **Assess Completion Level**: Determine if fully completed or partially done (scale: 0-100% or "complete"/"partial"/"missing")

     - **Note Missing Elements**: Document specific missing elements (list of gaps)

   - **Method**: For each requirement R1, R2, R3...:

     ```
     Requirement R1: [description]
     Addressed: [Yes/No]
     Correctness: [1-10 scale or percentage]
     Completion: [0-100% or complete/partial/missing]
     Missing Elements: [specific list or "None"]
     ```

   - **Validation**: Verify all requirements from Part 1 are evaluated (no requirements skipped)

6. **Evaluate Code Quality** (if code was produced)

   - **Action**: Assess code quality using measurable criteria

   - **Criteria**: 

     - Code structure and organization (scale: 1-10)

     - Error handling presence (binary: present/absent)

     - Documentation/comments (scale: 1-10)

     - Adherence to coding standards (scale: 1-10)

   - **Method**: Review code files, apply criteria, assign scores

   - **Output**: Code quality score (average of criteria scores) with justification

   - **Example**: "Code Quality: 7.5/10 (Structure: 8/10, Error Handling: 7/10, Documentation: 6/10, Standards: 9/10)"

   - **Validation**: If code files exist, code quality must be evaluated; if no code files, explicitly state "No code produced - code quality N/A"

7. **Evaluate Documentation Quality** (if documentation was produced)

   - **Action**: Assess documentation quality using measurable criteria

   - **Criteria**:

     - Completeness (covers all required topics: scale 1-10)

     - Clarity and readability (scale: 1-10)

     - Structure and organization (scale: 1-10)

     - Examples and use cases (scale: 1-10)

   - **Method**: Review documentation files, apply criteria, assign scores

   - **Output**: Documentation quality score (average of criteria scores) with justification

   - **Example**: "Documentation Quality: 8.0/10 (Completeness: 9/10, Clarity: 8/10, Structure: 8/10, Examples: 7/10)"

   - **Validation**: If documentation files exist, documentation quality must be evaluated; if no documentation, explicitly state "No documentation produced - documentation quality N/A"

8. **Check Standards Adherence**

   - **Action**: Check adherence to standards mentioned in the original prompt

   - **Method**: Compare worktree output against standards specified in original prompt (from Part 1, Step 2)

   - **Criteria**: For each standard mentioned:

     - Adherence level (scale: 1-10 or percentage)

     - Specific violations (list of non-compliant items)

     - Compliance status (compliant/partially compliant/non-compliant)

   - **Output**: Standards adherence report with per-standard evaluation

   - **Example**: "Standards Adherence: 85% (Standard A: 9/10 compliant, Standard B: 8/10 compliant, Standard C: 7/10 partially compliant)"

   - **Validation**: Verify all standards from original prompt are checked (no standards skipped)

9. **Document Strengths and Weaknesses**

   - **Action**: Identify specific strengths and weaknesses for this worktree

   - **Method**: Based on analysis above, list:

     - **Strengths**: Specific examples of what was done well (reference files, implementations, features)

     - **Weaknesses**: Specific examples of what was missing or done poorly (reference gaps, errors, incomplete implementations)

   - **Format**: 

     ```
     Strengths:
     [Specific strength with file reference]
     [Specific strength with implementation detail]
     
     Weaknesses:
     [Specific weakness with missing element]
     [Specific weakness with incorrect implementation]
     ```

   - **Validation**: Verify strengths and weaknesses are specific (not generic) and reference actual files/implementations

**Validation Checkpoint 2.1**

**[STRICT]** After completing analysis for each worktree, verify:

- ✓ All Git commands executed (`git status`, `git diff`)

- ✓ All files categorized (created/modified/deleted)

- ✓ All requirements evaluated (no requirements skipped)

- ✓ Code quality assessed (if code exists) or explicitly stated as N/A

- ✓ Documentation quality assessed (if documentation exists) or explicitly stated as N/A

- ✓ All standards checked (no standards skipped)

- ✓ Strengths and weaknesses documented with specific examples

**If validation fails**: Re-execute failed substep for that worktree, or report specific limitation with confidence level.

---

### PART 3: Compare and Rank All Worktrees

**[STRICT]** Execute this part systematically with explicit comparison methodology:

1. **Create Comparison Matrix**

   - **Action**: Create a comparison matrix or checklist

   - **Format**: Table with structure:

     | Worktree | R1 Score | R2 Score | R3 Score | ... | Code Quality | Doc Quality | Standards | Total Score | Rank |
     |----------|----------|---------|----------|-----|--------------|-------------|-----------|-------------|------|
     | WT1      | [score]  | [score] | [score]  | ... | [score]      | [score]     | [score]   | [total]     | [rank]|
     | WT2      | [score]  | [score] | [score]  | ... | [score]      | [score]     | [score]   | [total]     | [rank]|
     | ...      | ...      | ...     | ...      | ... | ...          | ...         | ...       | ...         | ...  |

   - **Scoring Method**: Use 1-10 scale OR percentage (0-100%) for each requirement and quality metric

   - **Consistency**: Apply the SAME scoring method across all worktrees (same scale for all)

   - **Validation**: Verify matrix includes all worktrees from Part 1 and all requirements from Part 1, Step 2

2. **Score Each Worktree**

   - **Action**: For each worktree, score how well it meets each requirement

   - **Method**: 

     - Use 1-10 scale (1 = completely missing, 10 = fully meets requirement) OR

     - Use percentage (0-100%, where 100% = fully meets requirement)

     - Apply consistent scoring method across all worktrees (same scale for all)

   - **Calculation**: For each worktree:

     - Requirement R1 score: [1-10 or 0-100%]

     - Requirement R2 score: [1-10 or 0-100%]

     - ... (all requirements)

     - Code quality score: [1-10 or 0-100%] (if applicable)

     - Documentation quality score: [1-10 or 0-100%] (if applicable)

     - Standards adherence score: [1-10 or 0-100%]

     - Total score: Sum of all requirement scores + quality scores OR average of all scores

   - **Validation**: Verify scoring method is consistent (same scale used for all worktrees and all requirements)

3. **Rank the Worktrees**

   - **Action**: Rank all worktrees from best to worst

   - **Method**: Sort worktrees by total score (highest score = rank 1, lowest score = last rank)

   - **Output**: Ranked list: 

     ```
     1. [worktree-path] (total score: [total])
     2. [worktree-path] (total score: [total])
     3. [worktree-path] (total score: [total])
     ```

   - **Validation**: Verify ranking is complete (all worktrees ranked, no ties in ranking unless explicitly handled)

4. **Identify Highest Score**

   - **Action**: Identify which worktree has the highest score

   - **Method**: Compare total scores, select worktree with maximum total score

   - **Output**: Explicit statement: "Worktree [path] has the highest score: [total score]"

   - **Validation**: Verify highest score is correctly identified (mathematical verification)

5. **Handle Ties**

   - **Action**: If there are ties (multiple worktrees with same total score), use tie-breaking criteria

   - **Tie-Breaking Order**: 

     1. **Completeness** (highest number of fully completed requirements wins)

     2. **Accuracy** (if still tied, highest average correctness score wins)

     3. **Quality** (if still tied, highest code/documentation quality score wins)

     4. **Standards Adherence** (if still tied, highest standards adherence score wins)

   - **Method**: Apply tie-breaking criteria in order until tie is broken

   - **Output**: If tie exists, explicitly state: "Tie detected between [worktrees]. Applying tie-breaking: [criteria applied], winner: [worktree]"

   - **Validation**: Verify tie-breaking logic is clear and unambiguous

**Validation Checkpoint 3.1**

**[STRICT]** After completing Part 3, verify:

- ✓ Comparison matrix created (table format with all worktrees and all requirements)

- ✓ Scoring method is explicit (1-10 scale OR percentage, not ambiguous)

- ✓ Scoring method is consistent (same scale for all)

- ✓ Ranking method specified (sort by total score)

- ✓ Tie-breaking criteria specified (order: completeness > accuracy > quality > standards)

- ✓ Tie-breaking method is unambiguous (clear procedure)

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

### PART 4: Declare Winner and Explain

**[STRICT]** Execute this part with evidence-based winner declaration:

1. **State Winner Explicitly**

   - **Action**: Clearly state which worktree produced the best output

   - **Format**: "WINNER: [worktree-path] with total score: [score]"

   - **Validation**: Verify winner statement is unambiguous (single worktree identified)

2. **Provide Final Score/Ranking**

   - **Action**: Provide the final score or ranking

   - **Format**: 

     - Final ranking table (all worktrees with scores and ranks)

     - Winner score breakdown (per-requirement scores for winning worktree)

   - **Validation**: Verify scores are provided (numerical values, not vague descriptions)

3. **Explain Winner Justification**

   - **Action**: Explain WHY this worktree is the best using evidence-based reasoning

   - **Required Elements**:

     - **Specific Evidence**: Provide specific evidence from your analysis (reference specific files, changes, implementations)

     - **Direct Comparison**: Compare it directly with other worktrees (side-by-side comparison)

     - **Superiority Highlights**: Highlight what makes it superior with examples:

       - "Worktree X completed all requirements while Worktree Y missed requirement 3"

       - "Worktree X's documentation is more comprehensive (score: 9/10 vs Worktree Y's 6/10)"

       - "Worktree Y's implementation is more accurate (correctness: 95% vs Worktree X's 80%)"

     - **Per-Requirement Analysis**: For each requirement, explain how the winning worktree performed better:

       - Requirement R1: "Winner scored 10/10 because [specific reason], while others scored [scores] because [reasons]"

       - Requirement R2: [similar analysis]

     - **Side-by-Side Comparisons**: Show side-by-side comparisons where relevant (table format)

     - **File/Implementation References**: Reference specific files, changes, or implementations:

       - "Winner's implementation in `[file-path]` demonstrates [specific strength]"

       - "Winner added [specific feature] in `[file-path]` that others missed"

     - **Evidence-Based Statements**: Avoid generic statements - be specific and evidence-based:

       - ❌ BAD: "Worktree X is better"

       - ✅ GOOD: "Worktree X scored 95/100 total (R1: 10/10, R2: 9/10, R3: 10/10) vs Worktree Y's 78/100 (R1: 8/10, R2: 7/10, R3: 8/10), with specific strengths in [area] demonstrated by [evidence]"

   - **Validation**: Verify explanation includes:

     - ✓ Specific evidence (not generic statements)

     - ✓ Direct comparisons (winner vs others)

     - ✓ Per-requirement analysis (all requirements covered)

     - ✓ File/implementation references (specific examples)

     - ✓ Measurable differences (scores, percentages, not "better/worse")

**Validation Checkpoint 4.1**

**[STRICT]** After completing Part 4, verify:

- ✓ Winner declaration format specified (explicit statement)

- ✓ Explanation requirements are specific (not vague "explain why")

- ✓ Evidence requirements specified (specific files, scores, comparisons)

- ✓ Generic statements are prohibited (explicit instruction to avoid vague language)

- ✓ Per-requirement analysis required (all requirements must be covered)

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

### PART 5: Create Analysis Report

**[STRICT]** Execute this part with structured report generation:

1. **Save Report**

   - **Action**: Save the analysis report in the current worktree directory

   - **Filename**: `worktree-analysis-report.md` (exact filename, case-sensitive)

   - **Location**: Current worktree directory (where analysis is being performed)

   - **Validation**: Verify file path is correct and writable before saving

2. **Report Structure Requirements**

   - **Action**: Report structure must include these exact sections (in order):

     **Executive Summary**

     - Brief overview of findings (2-3 paragraphs maximum)

     - Key metrics: Number of worktrees analyzed, winner identification, overall scores

     - High-level conclusion: Which worktree won and why (one sentence)

     **Methodology**

     - How the analysis was conducted (step-by-step process)

     - Tools and commands used (`git worktree list`, `git status`, `git diff`)

     - Evaluation criteria (requirements from original prompt)

     - Scoring method (1-10 scale or percentage, specify which)

     **Individual Analysis**

     - Detailed analysis of each worktree (one subsection per worktree)

     - For each worktree, include:

       - Worktree path and identification

       - Files created/modified/deleted (categorized lists)

       - Requirement evaluation (per-requirement scores with justification)

       - Code quality assessment (if applicable, with score and justification)

       - Documentation quality assessment (if applicable, with score and justification)

       - Standards adherence (per-standard evaluation)

       - Strengths and weaknesses (specific examples)

     **Comparison Matrix**

     - Side-by-side comparison of all worktrees

     - Format: Table with worktrees as rows, requirements as columns, scores as cells

     - Include total scores and ranks

     - Visual comparison of scores (use markdown table formatting)

     **Winner Declaration**

     - Which worktree is best and why (explicit statement)

     - Final scores and ranking (complete ranking table)

     - Winner identification with total score

     **Detailed Reasoning**

     - Comprehensive explanation with evidence

     - Per-requirement analysis (how winner performed better for each requirement)

     - Direct comparisons (winner vs other worktrees, side-by-side)

     - Specific evidence (file references, implementation details, code examples)

     - Measurable differences (scores, percentages, quantitative comparisons)

     **Recommendations**

     - What can be learned or improved (actionable insights)

     - Common strengths across worktrees (what worked well)

     - Common weaknesses across worktrees (what needs improvement)

     - Best practices identified (lessons learned)

     - Suggestions for future worktree agents (improvement recommendations)

   - **Validation**: Verify all required sections are included (checklist: Executive Summary, Methodology, Individual Analysis, Comparison Matrix, Winner Declaration, Detailed Reasoning, Recommendations)

3. **Formatting Requirements**

   - **Markdown Format**: Use markdown formatting throughout

   - **Code Blocks**: Include code blocks for file listings or diffs when relevant:

     - Use ```bash for Git commands

     - Use ```[language] for code files (specify language: python, javascript, etc.)

     - Use ```diff for Git diff output

   - **Tables**: Use tables for comparisons (markdown table syntax: `| column | column |`)

   - **Headers**: Use H2 for main sections, H3 for subsections, H4 for sub-subsections

   - **Lists**: Use numbered lists for sequential items, bulleted lists for non-sequential items

   - **Emphasis**: Use **bold** for key terms, *italic* for emphasis, `` `backticks` `` for file paths and commands

   - **Validation**: Verify markdown syntax is correct (test rendering if possible)

**Validation Checkpoint 5.1**

**[STRICT]** After completing Part 5, verify:

- ✓ Exact filename specified (`worktree-analysis-report.md`)

- ✓ Exact file location specified (current worktree directory)

- ✓ All required sections listed (Executive Summary, Methodology, Individual Analysis, Comparison Matrix, Winner Declaration, Detailed Reasoning, Recommendations)

- ✓ Formatting requirements specified (markdown, code blocks, tables, headers)

- ✓ Code block usage specified (when to use, what language tags)

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

## VALIDATION & QUALITY GATES

### Success Criteria

- **Completeness**: All required sections present (Part 1-5) with ≥95% coverage

- **Specificity**: All instructions are specific (no vague terms, all commands exact) with 100% specificity rate

- **Actionability**: Prompt can be executed by LLM without ambiguity (all inputs, outputs, criteria specified) with ≥90% actionability score

- **Validation**: All validation checkpoints included at logical breakpoints with measurable criteria

### Quality Gates

**[STRICT]** The analysis MUST meet:

- ✓ **Completeness ≥95%**: All required sections (Part 1-5) present with all substeps

- ✓ **Specificity 100%**: Zero vague terms (all instructions specific, all commands exact, all paths explicit)

- ✓ **Actionability ≥90%**: Analysis is executable without external clarification (all inputs/outputs/criteria specified)

- ✓ **Validation Coverage 100%**: All logical breakpoints have validation checkpoints with measurable criteria

### Edge Case Handling

- **Case 1: Input File Missing**: If `worktree-prompt1.md` is missing → Halt execution, report error: "Input file not found: [path]. Cannot proceed without original prompt file."

- **Case 2: No Worktrees Found**: If `git worktree list` returns no worktrees → Report "No worktrees found. Analysis cannot proceed." and exit gracefully

- **Case 3: Worktree Directory Inaccessible**: If worktree directory cannot be accessed → Report error: "Cannot access worktree: [path]. Error: [specific error]. Skipping this worktree." and continue with other worktrees

- **Case 4: Git Command Failure**: If Git command fails → Report error: "Git command failed: [command]. Error: [specific error]." and provide recovery suggestion or skip step if non-critical

### Error Handling

- **Error Type 1: File Read Error**: If input file cannot be read → Halt execution, report: "Cannot read input file: [path]. Verify file exists and permissions are correct. Error: [specific error]"

- **Error Type 2: Git Command Error**: If Git command fails → Report error with command, path, and specific error message. If critical (worktree list), halt. If non-critical (status/diff for single worktree), skip and continue.

- **Error Type 3: Validation Failure**: If validation checkpoint fails → Re-execute failed step, strengthen analysis, or report limitation with confidence level. Do not proceed until validation passes or limitation is explicitly documented.

- **Error Type 4: Output Generation Error**: If report cannot be saved → Report error: "Cannot save analysis report: [path]. Verify directory is writable. Error: [specific error]" and provide alternative (output to console or different location)

---

## OUTPUT FORMAT REQUIREMENTS

### Structure

- **Header Hierarchy**: Use H1 for main title, H2 for major parts (Part 1-5), H3 for substeps, H4 for sub-substeps

- **Organization**: Linear, sequential structure (Part 1 → Part 2 → Part 3 → Part 4 → Part 5) with hierarchical substeps

- **Section Order**: Preserve exact order: Part 1 → Part 2 → Part 3 → Part 4 → Part 5

- **Nesting Depth**: Maximum H4 level for sub-substeps within parts

### Formatting

- **Code Blocks**: Use ```bash for Git commands, ```[language] for code examples, ```diff for diffs

- **Lists**: Use numbered lists for sequential steps, bulleted lists for non-sequential items

- **Tables**: Use markdown tables for comparison matrices (format: `| column | column |`)

- **Emphasis**: Use **bold** for key terms and requirements, *italic* for emphasis, `` `backticks` `` for file paths and commands

- **Directives**: Use [STRICT] for mandatory requirements, [GUIDELINE] for recommendations

### Required Elements

1. **Prerequisites Section**: Required knowledge, available resources, constraints

2. **Role Definition**: Clear role statement with competencies

3. **Input Specification**: Input file path and validation

4. **Execution Protocol**: Step-by-step instructions with validation (Part 1-5)

5. **Validation Checkpoints**: Checkpoints at logical breakpoints with measurable criteria

6. **Error Handling**: Error handling procedures for common failure modes

7. **Output Format**: Report structure and formatting requirements

---

## EXECUTION MODE

**[STRICT]** This prompt operates in standard execution mode:

- ✓ All parts executed sequentially (Part 1 → Part 2 → Part 3 → Part 4 → Part 5)

- ✓ Validation checkpoints must pass before proceeding (no skipping validation)

- ✓ Error handling applied when errors occur (halt or skip based on error type)

- ✓ Final output is complete analysis report (ready for review)

**Workflow Complete**: Analysis report written to `worktree-analysis-report.md` and ready for review.
