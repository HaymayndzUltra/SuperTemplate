# Generate Worktree Analysis Prompt (ENHANCED)

## PREREQUISITES & CONTEXT

### Required Knowledge
- **Git Worktree Operations**: Deep understanding of `git worktree` commands, worktree directory structure, and Git workflow management
- **Prompt Engineering Fundamentals**: Comprehensive knowledge of prompt structure, instruction clarity, validation requirements, and output formatting specifications
- **Code Quality Assessment**: Familiarity with evaluating code quality metrics, documentation standards, and implementation correctness
- **Comparative Analysis Methodology**: Systematic approach to comparing multiple outputs, scoring criteria, and ranking methodologies
- **Markdown Documentation**: Proficiency in markdown formatting, structured documentation, tables, and code block presentation

### Available Resources
- **Input File**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md` - Original prompt file to analyze (required input)
- **Git Commands**: Access to `git worktree list`, `git status`, `git diff` commands for worktree analysis
- **File System Access**: Ability to navigate worktree directories, read files, and analyze changes
- **Output Location**: Current worktree directory for saving analysis report (specified: `worktree-analysis-report.md`)

### Constraints & Assumptions
- **File Existence**: The original prompt file (`worktree-prompt1.md`) must exist and be readable; if missing, halt execution and report error
- **Worktree Availability**: At least one worktree must exist (beyond main repository); if none found, report "No worktrees to analyze" and exit gracefully
- **Scope Boundary**: Analysis is limited to worktrees created from the original prompt execution; exclude unrelated worktrees
- **Output Format**: Analysis report must be valid markdown format with proper structure and formatting

---

## YOUR ROLE

You are a **Prompt Generation Specialist** tasked with creating a comprehensive, actionable prompt that will enable systematic analysis and comparison of outputs from previous worktree agents. Your generated prompt must be:

- **Direct and Actionable**: Use imperative verbs ("Run", "Check", "Compare", "Document") with specific, executable instructions
- **Specific and Measurable**: Replace vague terms with concrete commands, exact file paths, and quantifiable criteria
- **Complete and Unambiguous**: Leave nothing to assumption; specify exact commands, file locations, validation criteria, and success thresholds
- **Structured and Validated**: Include validation checkpoints at logical breakpoints with measurable criteria and error handling procedures

**Core Competencies:**
- Systematic prompt decomposition into clear, sequential steps
- Translation of abstract requirements into concrete, executable instructions
- Integration of validation checkpoints and quality gates
- Specification of measurable success criteria and error handling procedures

---

## INPUT SPECIFICATION

### Input File
- **Primary Input**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`
  - **Format**: Markdown file containing the original prompt given to worktree agents
  - **Purpose**: Source of requirements, expected outcomes, and quality criteria for evaluation
  - **Validation**: **[STRICT]** Before proceeding, verify file exists and is readable. If file is missing or unreadable, halt execution and report: "Error: Cannot read input file `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`. Please verify file path and permissions."

### Input Validation Checkpoint
**[STRICT]** Before proceeding to Step 1, verify:
- ✓ Input file path is correct and accessible
- ✓ File exists and is readable (check file permissions)
- ✓ File contains readable content (not empty, not corrupted)
- ✓ File format is markdown (verify `.md` extension and markdown structure)

**If validation fails**: Report specific error with file path and suggested resolution, then halt execution.

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION

### STEP 1: Read and Understand the Original Prompt

**[STRICT]** Execute this step systematically with validation checkpoints:

1. **Read the Input File**
   - **Action**: Read the file: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`
   - **Method**: Use file reading capability to load complete file content
   - **Validation**: Verify file was read successfully (content length > 0, no read errors)

2. **Analyze Original Instruction**
   - **Action**: Parse and understand what the original instruction was asking the agents to do
   - **Method**: Identify primary task, secondary objectives, and implicit requirements
   - **Extract**: 
     - Primary task statement (one sentence)
     - List of explicit requirements (numbered list)
     - List of implicit requirements (inferred from context)
     - Expected deliverables or outputs
   - **Validation**: Ensure at least one primary task and one requirement identified

3. **Extract Requirements and Criteria**
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

4. **Document Evaluation Criteria**
   - **Action**: Document these requirements clearly as evaluation criteria
   - **Method**: Format requirements as evaluable criteria with:
     - Clear, testable statements
     - Measurable success indicators
     - Binary or scaled evaluation method (present/absent, or 1-10 scale)
   - **Output**: Structured list of evaluation criteria ready for use in generated prompt
   - **Validation**: Verify each criterion is:
     - Specific (not vague)
     - Testable (can be verified)
     - Measurable (has clear pass/fail or scoring method)

**Validation Checkpoint 1.1**
**[STRICT]** After completing Step 1, verify:
- ✓ Input file was read successfully (file content loaded, no errors)
- ✓ Primary task identified (single, clear statement of what original prompt asked for)
- ✓ At least 3 requirements extracted (minimum threshold for meaningful analysis)
- ✓ Evaluation criteria documented (structured list with testable criteria)
- ✓ All criteria are specific, testable, and measurable (no vague terms like "good" or "appropriate")

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

### STEP 2: Generate the Analysis Prompt

**[STRICT]** Generate a comprehensive prompt that instructs systematic worktree analysis. Follow this structure with embedded validation:

Think through this problem step-by-step:
1. **First**, identify the 4 worktrees from parallel execution cluster that need analysis (Part 1)
2. **Then**, analyze each worktree individually against requirements (Part 2)
3. **Next**, compare and rank the 4 worktrees using measurable criteria (Part 3)
4. **Finally**, declare winner with evidence-based justification and generate report (Parts 4-5)

For each part, execute → validate against criteria → proceed to next part.

#### Part 1: Identify Worktrees to Analyze

**[STRICT]** Include these exact instructions in your generated prompt:

1. **Execute Git Worktree Command**
   - **Action**: Run the command: `git worktree list`
   - **Purpose**: Retrieve list of all worktree directories and their associated branches
   - **Validation**: Verify command executed successfully (exit code 0, output contains worktree entries)
   - **Error Handling**: If command fails → report error: "Failed to execute `git worktree list`. Verify Git is installed and repository is valid. Error: [specific error message]"

2. **Parse Command Output**
   - **Action**: Parse the output to identify all worktree directories
   - **Method**: Extract worktree paths from command output (format: `[path] [commit-hash] [branch-name]`)
   - **Extract**: 
     - Worktree directory paths (absolute or relative paths)
     - Associated branch names (if available)
     - Commit hashes (if available)
   - **Validation**: Verify at least one worktree path extracted (excluding main repository); if none found → report "No worktrees found. Analysis cannot proceed."

3. **Determine Creation Timestamps**
   - **Action**: Get creation/modification timestamps for each worktree directory
   - **Method**: Use file system metadata to get timestamps (e.g., `stat -c '%Y [worktree-path]` or equivalent)
   - **Purpose**: Timestamps are needed to identify parallel execution clusters
   - **Output**: List of worktrees with their timestamps (Unix timestamp format)
   - **Validation**: Verify all worktrees have timestamps assigned

4. **Identify Parallel Execution Cluster**
   - **Action**: Identify the 4 worktrees created within a short time window (indicating parallel execution)
   - **Assumption**: 4 agents run in parallel, so look for 4 worktrees with close timestamps
   - **Method**: 
     - Sort all worktrees by creation time (most recent first)
     - Calculate time differences between consecutive worktrees
     - Identify cluster: Find 4 worktrees created within 5 minutes of each other
     - If multiple clusters exist, select the most recent cluster
     - If exactly 4 worktrees are found within 5 minutes, use those
     - If more than 4 worktrees are found within 5 minutes, select the 4 most recent ones
     - If fewer than 4 worktrees are found within 5 minutes, expand time window to 10 minutes, then 15 minutes, until 4 worktrees are found
   - **Output**: List exactly 4 worktree paths that form the parallel execution cluster
   - **Format**: Create numbered list: `1. [worktree-path-1]`, `2. [worktree-path-2]`, `3. [worktree-path-3]`, `4. [worktree-path-4]`
   - **Validation**: Verify exactly 4 worktrees identified with timestamps within the time window

5. **Scope Confirmation**
   - **Action**: Confirm that the 4 identified worktrees from the parallel execution cluster will be analyzed
   - **Instruction**: Explicitly state: "You MUST analyze ALL 4 worktrees listed above from the parallel execution cluster. Do not skip any worktree."
   - **Validation**: Verify instruction explicitly states "ALL 4 worktrees" with emphasis

**Validation Checkpoint 2.1**
**[STRICT]** After generating Part 1, verify:
- ✓ Exact command specified (`git worktree list`)
- ✓ Parsing instructions are specific (not vague "parse the output")
- ✓ Timestamp extraction method specified (how to get creation/modification times)
- ✓ Parallel execution cluster identification logic specified (4 worktrees within time window)
- ✓ Assumption stated: 4 agents run in parallel
- ✓ Time window expansion logic specified (5 min → 10 min → 15 min if needed)
- ✓ Error handling included (what to do if command fails or no worktrees found)
- ✓ Scope explicitly states "ALL 4 worktrees" from parallel execution cluster (not ambiguous)

#### Part 2: Analyze Each Worktree

**[STRICT]** Include detailed instructions with validation checkpoints:

1. **Navigate to Worktree Directory**
   - **Action**: Navigate to each worktree directory (iterate through the 4 worktrees from the parallel execution cluster identified in Part 1)
   - **Method**: Use `cd [worktree-path]` or equivalent navigation command
   - **Validation**: Verify navigation successful (current directory matches worktree path)
   - **Error Handling**: If navigation fails → report: "Cannot access worktree directory: [path]. Error: [specific error]. Skipping this worktree."

2. **Execute Git Status**
   - **Action**: Run `git status` to see what files were changed
   - **Purpose**: Identify modified, added, deleted, or untracked files
   - **Output Capture**: Save output for later analysis
   - **Validation**: Verify command executed (exit code 0 or meaningful Git status output)
   - **Error Handling**: If command fails → report: "Git status failed in worktree [path]. Error: [specific error]"

3. **Execute Git Diff**
   - **Action**: Run `git diff` to see what changes were made
   - **Purpose**: View actual code/content changes, additions, and deletions
   - **Output Capture**: Save diff output for detailed analysis
   - **Validation**: Verify diff output captured (output length > 0 or explicit "no changes" message)
   - **Note**: If no changes exist, explicitly state "No changes detected" rather than empty output

4. **List All Changed Files**
   - **Action**: List all files that were created, modified, or changed
   - **Method**: Parse `git status` and `git diff` output to extract file paths
   - **Categorize**: 
     - Created files (new files, not in original)
     - Modified files (existing files with changes)
     - Deleted files (files removed)
   - **Format**: Create structured list with categories: `Created: [file-list]`, `Modified: [file-list]`, `Deleted: [file-list]`
   - **Validation**: Verify file list is complete (matches git status/diff output)

5. **Evaluate Against Requirements**
   - **Action**: For each requirement from the original prompt (extracted in Step 1):
     - **Check Requirement Addressed**: Verify if requirement was addressed (binary: yes/no)
     - **Verify Implementation Correctness**: Assess if implementation is correct (scale: 1-10 or percentage)
     - **Assess Completion Level**: Determine if fully completed or partially done (scale: 0-100% or "complete"/"partial"/"missing")
     - **Note Missing Elements**: Document specific missing elements (list of gaps)
   - **Method**: For each requirement R1, R2, R3...:
     

     Requirement R1: [description]
Addressed: [Yes/No]
Correctness: [1-10 scale or percentage]
Completion: [0-100% or complete/partial/missing]
Missing Elements: [specific list or "None"]


   - **Validation**: Verify all requirements from Step 1 are evaluated (no requirements skipped)

6. **Evaluate Code Quality** (if code was produced)
   - **Action**: Assess code quality using measurable criteria
   - **Criteria**: 
     - Code structure and organization (scale: 1-10)
     - Error handling presence (binary: present/absent)
     - Documentation/comments (scale: 1-10)
     - Adherence to coding standards (scale: 1-10)
   - **Method**: Review code files, apply criteria, assign scores
   - **Output**: Code quality score (average of criteria scores) with justification
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
   - **Validation**: If documentation files exist, documentation quality must be evaluated; if no documentation, explicitly state "No documentation produced - documentation quality N/A"

8. **Check Standards Adherence**
   - **Action**: Check adherence to standards mentioned in the original prompt
   - **Method**: Compare worktree output against standards specified in original prompt (from Step 1 analysis)
   - **Criteria**: For each standard mentioned:
     - Adherence level (scale: 1-10 or percentage)
     - Specific violations (list of non-compliant items)
     - Compliance status (compliant/partially compliant/non-compliant)
   - **Output**: Standards adherence report with per-standard evaluation
   - **Validation**: Verify all standards from original prompt are checked (no standards skipped)

**Validation Checkpoint 2.2**
**[STRICT]** After generating Part 2, verify:
- ✓ All Git commands specified exactly (`git status`, `git diff`)
- ✓ File categorization method specified (created/modified/deleted)
- ✓ Requirement evaluation method is specific (not vague "check if addressed")
- ✓ Code quality criteria are measurable (scales or percentages, not "good/bad")
- ✓ Documentation quality criteria are measurable (scales or percentages)
- ✓ Standards adherence method is specific (what standards, how to check)

#### Part 3: Compare and Rank the 4 Worktrees

**[STRICT]** Include instructions with explicit comparison methodology:

1. **Create Comparison Matrix**
   - **Action**: Create a comparison matrix or checklist
   - **Format**: Table with structure:
     | Worktree | R1 Score | R2 Score | R3 Score | ... | Total Score | Rank |
     |----------|-----------|----------|----------|-----|-------------|------|
     | WT1      | [score]   | [score]  | [score]  | ... | [total]     | [rank]|
     | WT2      | [score]   | [score]  | [score]  | ... | [total]     | [rank]|
   - **Scoring Method**: Use 1-10 scale or percentage (0-100%) for each requirement
   - **Validation**: Verify matrix includes all 4 worktrees and all requirements

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
     - Total score: Sum of all requirement scores OR average of all requirement scores
   - **Validation**: Verify scoring method is consistent (same scale used for all worktrees and all requirements)

3. **Rank the 4 Worktrees**
   - **Action**: Rank the 4 worktrees from best to worst
   - **Method**: Sort worktrees by total score (highest score = rank 1, lowest score = rank 4)
   - **Output**: Ranked list: `1. [worktree-path] (score: [total])`, `2. [worktree-path] (score: [total])`, `3. [worktree-path] (score: [total])`, `4. [worktree-path] (score: [total])`
   - **Validation**: Verify ranking is complete (all 4 worktrees ranked, no ties in ranking unless explicitly handled)

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

**Validation Checkpoint 2.3**
**[STRICT]** After generating Part 3, verify:
- ✓ Comparison matrix format specified (table structure with columns)
- ✓ Scoring method is explicit (1-10 scale OR percentage, not ambiguous)
- ✓ Scoring method is consistent (same scale for all)
- ✓ Ranking method specified (sort by total score)
- ✓ Tie-breaking criteria specified (order: completeness > accuracy > quality > standards)
- ✓ Tie-breaking method is unambiguous (clear procedure)

#### Part 4: Declare Winner and Explain

**[STRICT]** Include instructions for evidence-based winner declaration:

1. **State Winner Explicitly**
   - **Action**: Clearly state which worktree produced the best output
   - **Format**: "WINNER: [worktree-path] with total score: [score]"
   - **Validation**: Verify winner statement is unambiguous (single worktree identified)

2. **Provide Final Score/Ranking**
   - **Action**: Provide the final score or ranking
   - **Format**: 
     - Final ranking table (all 4 worktrees with scores and ranks)
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

**Validation Checkpoint 2.4**
**[STRICT]** After generating Part 4, verify:
- ✓ Winner declaration format specified (explicit statement)
- ✓ Explanation requirements are specific (not vague "explain why")
- ✓ Evidence requirements specified (specific files, scores, comparisons)
- ✓ Generic statements are prohibited (explicit instruction to avoid vague language)
- ✓ Per-requirement analysis required (all requirements must be covered)

#### Part 5: Create Analysis Report

**[STRICT]** Include instructions for structured report generation:

1. **Save Report**
   - **Action**: Save the analysis report in the current worktree directory
   - **Filename**: `worktree-analysis-report.md` (exact filename, case-sensitive)
   - **Location**: Current worktree directory (where analysis is being performed)
   - **Validation**: Verify file path is correct and writable before saving

2. **Report Structure Requirements**
   - **Action**: Report structure must include these exact sections (in order):
     
     **Executive Summary**
     - Brief overview of findings (2-3 paragraphs maximum)
     - Key metrics: 4 worktrees analyzed (from parallel execution cluster), winner identification, overall scores
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
     - Side-by-side comparison of the 4 worktrees
     - Format: Table with worktrees as rows, requirements as columns, scores as cells
     - Include total scores and ranks
     - Visual comparison of scores (if possible, use markdown table formatting)
     
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
     - Use for Git commands
     - Use ```[language] for code files (specify language: python, javascript, etc.)
     - Use for Git diff output
   - **Tables**: Use tables for comparisons (markdown table syntax: `| column | column |`)
   - **Headers**: Use H2 for main sections, H3 for subsections, H4 for sub-subsections
   - **Lists**: Use numbered lists for sequential items, bulleted lists for non-sequential items
   - **Emphasis**: Use **bold** for key terms, *italic* for emphasis, `` `backticks` `` for file paths and commands
   - **Validation**: Verify markdown syntax is correct (test rendering if possible)

**Validation Checkpoint 2.5**
**[STRICT]** After generating Part 5, verify:
- ✓ Exact filename specified (`worktree-analysis-report.md`)
- ✓ Exact file location specified (current worktree directory)
- ✓ All required sections listed (Executive Summary, Methodology, Individual Analysis, Comparison Matrix, Winner Declaration, Detailed Reasoning, Recommendations)
- ✓ Formatting requirements specified (markdown, code blocks, tables, headers)
- ✓ Code block usage specified (when to use, what language tags)

---

### STEP 3: Format Your Generated Prompt

**[STRICT]** Your generated prompt must meet these formatting and quality criteria:

1. **Direct and Actionable**
   - **Requirement**: Use imperative verbs: "Run", "Check", "Compare", "Document", "Analyze", "Evaluate"
   - **Validation**: Verify all instructions use imperative mood (command form, not "you should" or "it would be good to")
   - **Example**: 
     - ❌ BAD: "You might want to analyze the worktrees"
     - ✅ GOOD: "Analyze the 4 worktrees from the parallel execution cluster using the following steps"

2. **Specific, Not Generic**
   - **Requirement**: Replace vague instructions with specific commands and file paths
   - **Validation**: Verify no vague terms like "analyze the output" without specifying how
   - **Example**:
     - ❌ BAD: "analyze the output"
     - ✅ GOOD: "Navigate to worktree directory `/path/to/worktree`, run `git status`, parse output to list all modified files, then run `git diff` to view changes"

3. **Exact Commands**
   - **Requirement**: Include exact commands to run (with proper syntax and options)
   - **Validation**: Verify all Git commands are specified exactly (`git worktree list`, `git status`, `git diff`)
   - **Example**: Specify `git worktree list` not "list worktrees" or "get worktree information"

4. **Explain Importance**
   - **Requirement**: Explain WHY each step is important
   - **Method**: For each major step, include a "Purpose" or "Why" statement
   - **Example**: "Run `git status` to identify all modified files. This is important because it shows what changes were made, which is required for requirement evaluation."
   - **Validation**: Verify each major step has purpose/justification

5. **Complete Coverage**
   - **Requirement**: Cover all aspects: identification, analysis, comparison, decision, explanation
   - **Validation**: Verify prompt includes:
     - ✓ Worktree identification (Part 1)
     - ✓ Individual analysis (Part 2)
     - ✓ Comparison and ranking (Part 3)
     - ✓ Winner declaration (Part 4)
     - ✓ Report generation (Part 5)

6. **No Assumptions**
   - **Requirement**: Nothing should be left to assumption
   - **Method**: Explicitly state:
     - Exact file paths
     - Exact commands
     - Exact evaluation criteria
     - Exact scoring methods
     - Exact output formats
   - **Validation**: Verify no ambiguous instructions (all paths, commands, criteria are explicit)

**Validation Checkpoint 3.1**
**[STRICT]** After completing Step 3, verify:
- ✓ All instructions use imperative verbs (command form)
- ✓ No vague terms (all instructions are specific)
- ✓ All commands are exact (proper Git command syntax)
- ✓ Each step has purpose/justification
- ✓ All aspects covered (identification, analysis, comparison, decision, explanation)
- ✓ No assumptions (all paths, commands, criteria explicit)

---

### STEP 4: Output Your Generated Prompt

**[STRICT]** Output the complete generated prompt that follows all instructions above.

**Output Requirements:**
1. **Completeness**: Include all parts (Part 1-5) with all instructions from Steps 1-3
2. **Structure**: Follow the structure specified in Step 2 (Part 1 → Part 2 → Part 3 → Part 4 → Part 5)
3. **Formatting**: Use markdown formatting with proper headers, lists, code blocks, and tables
4. **Validation**: Include all validation checkpoints and error handling from Steps 1-3
5. **Quality**: Ensure prompt is direct, specific, complete, and unambiguous (per Step 3 criteria)

**Output Format:**
- Markdown format (.md)
- Ready for immediate use by an LLM
- Complete and self-contained (no external dependencies beyond specified input file)

**Final Validation Checkpoint 4.1**
**[STRICT]** Before finalizing output, verify:
- ✓ All parts included (Part 1-5 complete)
- ✓ All validation checkpoints included (from Steps 1-3)
- ✓ All error handling included (from Steps 1-3)
- ✓ Formatting requirements met (markdown, headers, lists, code blocks)
- ✓ Quality criteria met (direct, specific, complete, unambiguous)
- ✓ Prompt is ready for LLM execution (self-contained, no missing information)

---

## VALIDATION & QUALITY GATES

### Success Criteria
- **Completeness**: All required sections present (Step 1-4, Part 1-5) with ≥95% coverage
- **Specificity**: All instructions are specific (no vague terms, all commands exact) with 100% specificity rate
- **Actionability**: Prompt can be executed by LLM without ambiguity (all inputs, outputs, criteria specified) with ≥90% actionability score
- **Validation**: All validation checkpoints included at logical breakpoints with measurable criteria

### Quality Gates
**[STRICT]** The generated prompt MUST meet:
- ✓ **Completeness ≥95%**: All required sections (Step 1-4, Part 1-5) present with all substeps
- ✓ **Specificity 100%**: Zero vague terms (all instructions specific, all commands exact, all paths explicit)
- ✓ **Actionability ≥90%**: Prompt is executable without external clarification (all inputs/outputs/criteria specified)
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
- **Header Hierarchy**: Use H1 for main title, H2 for major steps (Step 1-4), H3 for parts (Part 1-5), H4 for substeps
- **Organization**: Linear, sequential structure (Step 1 → Step 2 → Step 3 → Step 4) with hierarchical parts within Step 2
- **Section Order**: Preserve exact order: Step 1 → Step 2 (Part 1-5) → Step 3 → Step 4
- **Nesting Depth**: Maximum H4 level for substeps within parts

### Formatting
- **Code Blocks**: Use for Git commands, ```[language] for code examples, for diffs
- **Lists**: Use numbered lists for sequential steps, bulleted lists for non-sequential items
- **Tables**: Use markdown tables for comparison matrices (format: `| column | column |`)
- **Emphasis**: Use **bold** for key terms and requirements, *italic* for emphasis, `` `backticks` `` for file paths and commands
- **Directives**: Use [STRICT] for mandatory requirements, [GUIDELINE] for recommendations

### Required Elements
1. **Prerequisites Section**: Required knowledge, available resources, constraints (if not embedded in role)
2. **Role Definition**: Clear role statement with competencies
3. **Input Specification**: Input file path and validation
4. **Execution Protocol**: Step-by-step instructions with validation (Step 1-4, Part 1-5)
5. **Validation Checkpoints**: Checkpoints at logical breakpoints with measurable criteria
6. **Error Handling**: Error handling procedures for common failure modes
7. **Output Format**: Report structure and formatting requirements

### Length Guidelines
- **Minimum**: 200 lines for comprehensive prompt covering all aspects
- **Target**: 300-500 lines for detailed prompt with validation and error handling
- **Maximum**: 1000 lines (if exceeding, consider modularization)
- **Detail Level**: Exhaustive (complete treatment with all edge cases, error handling, validation procedures)

---

## EXECUTION MODE

**[STRICT]** This prompt operates in standard execution mode:
- ✓ All steps executed sequentially (Step 1 → Step 2 → Step 3 → Step 4)
- ✓ Validation checkpoints must pass before proceeding (no skipping validation)
- ✓ Error handling applied when errors occur (halt or skip based on error type)
- ✓ Final output is complete generated prompt (ready for LLM execution)

**Workflow Complete**: Generated prompt written and ready for use.---

