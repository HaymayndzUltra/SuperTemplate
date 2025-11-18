# META INSTRUCTION FOR AI PROMPT GENERATOR

## PREREQUISITES & CONTEXT

### Required Knowledge
- **Git Worktree Operations**: Understanding of `git worktree list` command, worktree directory structure, and output parsing
- **Prompt Engineering Fundamentals**: Knowledge of prompt structure, instruction clarity, validation requirements, and output formatting
- **File System Operations**: Ability to read files, follow file references, and validate file existence and readability
- **Analysis Prompt Design**: Understanding of how to create prompts that enable systematic analysis and comparison

### Available Resources
- **Input File**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md` - Original prompt file containing the instructions given to worktree agents
- **Git Commands**: Access to `git worktree list` command for retrieving worktree information
- **File System Access**: Ability to read files and navigate directory structure

### Constraints & Assumptions
- **File Existence**: The original prompt file (`worktree-prompt1.md`) must exist and be readable; if missing, halt execution and report error
- **Worktree Availability**: Worktree information will be provided via `git worktree list` command output
- **Scope Boundary**: Generated analysis prompt should enable comparison of worktree outputs against the original prompt requirements
- **Output Format**: Generated prompt must be in markdown format, ready for immediate use by an AI Analyzer

---

## YOUR ROLE

You are a **Prompt Generation Specialist** tasked with creating a comprehensive, actionable meta instruction that will enable an AI Prompt Generator to create effective analysis prompts. Your meta instruction must guide the Prompt Generator to:

- **Process Git Worktree Information**: Extract and structure worktree branch information from `git worktree list` output
- **Extract Original Prompt**: Read and extract the original prompt from `worktree-prompt1.md`, including following any file references
- **Generate High-Quality Analysis Prompt**: Create a well-structured analysis prompt that leverages AI capabilities effectively for systematic comparison

**Core Competencies:**
- Systematic instruction decomposition into clear, sequential steps
- Translation of abstract requirements into concrete, executable instructions
- Integration of validation checkpoints and error handling procedures
- Specification of prompt engineering best practices for AI effectiveness

---

## INPUT SPECIFICATION

### Input 1: Git Worktree Command Output
- **Source**: Output from `git worktree list` command
- **Format**: Text output with format `[path] [commit-hash] [branch-name]` per line
- **Purpose**: Identify worktree directories and associated branches to analyze
- **Validation**: **[STRICT]** Before proceeding, verify command output is available and parseable. If output is empty or malformed, report error and halt execution.

### Input 2: Original Prompt File
- **Primary Input**: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`
  - **Format**: Markdown file containing the original prompt given to worktree agents
  - **Purpose**: Source of requirements, expected outcomes, and quality criteria for evaluation
  - **File References**: May contain references to other files that must be followed and included
  - **Validation**: **[STRICT]** Before proceeding, verify file exists and is readable. If file is missing or unreadable, halt execution and report: "Error: Cannot read input file `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`. Please verify file path and permissions."

### Input Validation Checkpoint
**[STRICT]** Before proceeding to Step 1, verify:
- ✓ Git worktree command output is available (or instruction to execute `git worktree list` is provided)
- ✓ Input file path is correct and accessible
- ✓ File exists and is readable (check file permissions)
- ✓ File contains readable content (not empty, not corrupted)
- ✓ File format is markdown (verify `.md` extension and markdown structure)

**If validation fails**: Report specific error with file path and suggested resolution, then halt execution.

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION

### STEP 1: Process Git Worktree Information

**[STRICT]** Execute this step systematically with validation checkpoints:

1. **Execute or Receive Git Worktree Command Output**
   - **Action**: Either execute `git worktree list` command OR receive the command output from user
   - **Method**: 
     - If command output not provided: Run `git worktree list` command
     - If command output provided: Use the provided output directly
   - **Purpose**: Retrieve list of all worktree directories and their associated branches
   - **Validation**: Verify command executed successfully (exit code 0, output contains worktree entries) OR verify provided output is valid
   - **Error Handling**: If command fails → report error: "Failed to execute `git worktree list`. Verify Git is installed and repository is valid. Error: [specific error message]"

2. **Parse Command Output**
   - **Action**: Parse the output to identify all worktree directories
   - **Method**: Extract worktree paths from command output (format: `[path] [commit-hash] [branch-name]`)
   - **Extract**: 
     - Worktree directory paths (absolute or relative paths)
     - Associated branch names (if available)
     - Commit hashes (if available)
   - **Output**: Create structured list of worktrees with their paths, branches, and commit hashes
   - **Validation**: Verify at least one worktree path extracted (excluding main repository); if none found → report "No worktrees found. Analysis cannot proceed."

3. **Structure Worktree Information**
   - **Action**: Organize extracted worktree information for inclusion in generated analysis prompt
   - **Method**: Format worktree information as:
     - Numbered list of worktree paths
     - Associated branch names (if available)
     - Any relevant metadata (timestamps, commit hashes)
   - **Output**: Structured worktree list ready for inclusion in analysis prompt
   - **Validation**: Verify all extracted worktrees are included in structured format

**Validation Checkpoint 1.1**
**[STRICT]** After completing Step 1, verify:
- ✓ Git worktree command executed or output received (command output available)
- ✓ Command output parsed successfully (worktree paths extracted)
- ✓ At least one worktree identified (excluding main repository)
- ✓ Worktree information structured and ready for prompt inclusion

**If validation fails**: Re-execute failed substep, strengthen parsing logic, or report specific limitation with confidence level.

---

### STEP 2: Read and Extract Original Prompt

**[STRICT]** Execute this step systematically with validation checkpoints:

1. **Read the Input File**
   - **Action**: Read the file: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`
   - **Method**: Use file reading capability to load complete file content
   - **Validation**: Verify file was read successfully (content length > 0, no read errors)

2. **Follow File References**
   - **Action**: Identify and follow any file references within the original prompt file
   - **Method**: 
     - Scan file content for file path references (patterns like `/path/to/file`, `./file.md`, `file.md`)
     - For each reference found:
       - Verify referenced file exists and is readable
       - Read referenced file content
       - Include referenced content in extracted prompt (clearly marked as from reference)
       - Recursively follow any references within referenced files (up to 3 levels deep to prevent infinite loops)
   - **Validation**: Verify all referenced files are accessible; if any file is missing, report warning but continue with available content
   - **Error Handling**: If referenced file cannot be read → report warning: "Warning: Cannot read referenced file [path]. Continuing with available content."

3. **Extract Complete Original Prompt**
   - **Action**: Combine original file content with all referenced file contents
   - **Method**: 
     - Start with original file content
     - Append referenced file contents with clear markers (e.g., "--- Reference: [file-path] ---")
     - Maintain original structure and formatting
   - **Output**: Complete original prompt text including all referenced content
   - **Validation**: Verify extracted prompt contains meaningful content (not empty, has structure)

4. **Analyze Original Instruction**
   - **Action**: Parse and understand what the original instruction was asking the agents to do
   - **Method**: Identify primary task, secondary objectives, and implicit requirements
   - **Extract**: 
     - Primary task statement (one sentence)
     - List of explicit requirements (numbered list)
     - List of implicit requirements (inferred from context)
     - Expected deliverables or outputs
     - Quality criteria and evaluation standards
   - **Validation**: Ensure at least one primary task and one requirement identified

**Validation Checkpoint 2.1**
**[STRICT]** After completing Step 2, verify:
- ✓ Input file was read successfully (file content loaded, no errors)
- ✓ All file references followed (referenced files read and included, or warnings reported)
- ✓ Complete original prompt extracted (original + referenced content combined)
- ✓ Primary task identified (single, clear statement of what original prompt asked for)
- ✓ Requirements extracted (at least one explicit requirement identified)
- ✓ Quality criteria identified (evaluation standards extracted)

**If validation fails**: Re-execute failed substep, strengthen analysis, or report specific limitation with confidence level.

---

### STEP 3: Generate Analysis Prompt Structure

**[STRICT]** Generate a comprehensive analysis prompt structure that the Prompt Generator should follow. The generated prompt must enable systematic worktree analysis and comparison.

#### Part 1: Identify Worktrees to Analyze

**[STRICT]** Instruct the Prompt Generator to include these exact instructions in the generated analysis prompt:

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

3. **List Worktrees to Analyze**
   - **Action**: Create a numbered list of all worktree paths that need to be analyzed
   - **Format**: `1. [worktree-path-1]`, `2. [worktree-path-2]`, etc.
   - **Scope**: Include instruction: "You MUST analyze ALL identified worktrees. Do not skip any worktree."
   - **Validation**: Verify instruction explicitly states "ALL worktrees" with emphasis

#### Part 2: Analyze Each Worktree

**[STRICT]** Instruct the Prompt Generator to include detailed instructions for analyzing each worktree:

1. **Navigate to Worktree Directory**
   - **Action**: Navigate to each worktree directory (iterate through all identified worktrees)
   - **Method**: Use `cd [worktree-path]` or equivalent navigation command
   - **Validation**: Verify navigation successful (current directory matches worktree path)
   - **Error Handling**: If navigation fails → report: "Cannot access worktree directory: [path]. Error: [specific error]. Skipping this worktree."

2. **Execute Git Status**
   - **Action**: Run `git status` to see what files were changed
   - **Purpose**: Identify modified, added, deleted, or untracked files
   - **Output Capture**: Save output for later analysis
   - **Validation**: Verify command executed (exit code 0 or meaningful Git status output)

3. **Execute Git Diff**
   - **Action**: Run `git diff` to see what changes were made
   - **Purpose**: View actual code/content changes, additions, and deletions
   - **Output Capture**: Save diff output for detailed analysis
   - **Validation**: Verify diff output captured (output length > 0 or explicit "no changes" message)

4. **List All Changed Files**
   - **Action**: List all files that were created, modified, or changed
   - **Method**: Parse `git status` and `git diff` output to extract file paths
   - **Categorize**: 
     - Created files (new files, not in original)
     - Modified files (existing files with changes)
     - Deleted files (files removed)
   - **Format**: Create structured list with categories

5. **Evaluate Against Original Prompt Requirements**
   - **Action**: For each requirement from the original prompt (extracted in Step 2):
     - **Check Requirement Addressed**: Verify if requirement was addressed (binary: yes/no)
     - **Verify Implementation Correctness**: Assess if implementation is correct (scale: 1-10 or percentage)
     - **Assess Completion Level**: Determine if fully completed or partially done (scale: 0-100% or "complete"/"partial"/"missing")
     - **Note Missing Elements**: Document specific missing elements (list of gaps)
   - **Method**: For each requirement, create evaluation with:
     - Requirement ID and description
     - Addressed: [Yes/No]
     - Correctness: [1-10 scale or percentage]
     - Completion: [0-100% or complete/partial/missing]
     - Missing Elements: [specific list or "None"]
   - **Validation**: Verify all requirements from original prompt are evaluated (no requirements skipped)

6. **Evaluate Code Quality** (if code was produced)
   - **Action**: Assess code quality using measurable criteria
   - **Criteria**: 
     - Code structure and organization (scale: 1-10)
     - Error handling presence (binary: present/absent)
     - Documentation/comments (scale: 1-10)
     - Adherence to coding standards (scale: 1-10)
   - **Output**: Code quality score (average of criteria scores) with justification

7. **Evaluate Documentation Quality** (if documentation was produced)
   - **Action**: Assess documentation quality using measurable criteria
   - **Criteria**:
     - Completeness (covers all required topics: scale 1-10)
     - Clarity and readability (scale: 1-10)
     - Structure and organization (scale: 1-10)
     - Examples and use cases (scale: 1-10)
   - **Output**: Documentation quality score (average of criteria scores) with justification

8. **Check Standards Adherence**
   - **Action**: Check adherence to standards mentioned in the original prompt
   - **Method**: Compare worktree output against standards specified in original prompt
   - **Criteria**: For each standard mentioned:
     - Adherence level (scale: 1-10 or percentage)
     - Specific violations (list of non-compliant items)
     - Compliance status (compliant/partially compliant/non-compliant)

#### Part 3: Compare and Rank All Worktrees

**[STRICT]** Instruct the Prompt Generator to include instructions for comparison and ranking:

1. **Create Comparison Matrix**
   - **Action**: Create a comparison matrix or checklist
   - **Format**: Table with structure:
     | Worktree | R1 Score | R2 Score | R3 Score | ... | Total Score | Rank |
     |----------|-----------|----------|----------|-----|-------------|------|
     | WT1      | [score]   | [score]  | [score]  | ... | [total]     | [rank]|
   - **Scoring Method**: Use 1-10 scale or percentage (0-100%) for each requirement
   - **Validation**: Verify matrix includes all worktrees and all requirements

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

3. **Rank the Worktrees**
   - **Action**: Rank all worktrees from best to worst
   - **Method**: Sort worktrees by total score (highest score = rank 1, lowest score = last rank)
   - **Output**: Ranked list with scores

4. **Identify Highest Score**
   - **Action**: Identify which worktree has the highest score
   - **Method**: Compare total scores, select worktree with maximum total score
   - **Output**: Explicit statement: "Worktree [path] has the highest score: [total score]"

5. **Handle Ties**
   - **Action**: If there are ties (multiple worktrees with same total score), use tie-breaking criteria
   - **Tie-Breaking Order**: 
     1. **Completeness** (highest number of fully completed requirements wins)
     2. **Accuracy** (if still tied, highest average correctness score wins)
     3. **Quality** (if still tied, highest code/documentation quality score wins)
     4. **Standards Adherence** (if still tied, highest standards adherence score wins)
   - **Method**: Apply tie-breaking criteria in order until tie is broken

#### Part 4: Declare Winner and Explain

**[STRICT]** Instruct the Prompt Generator to include instructions for evidence-based winner declaration:

1. **State Winner Explicitly**
   - **Action**: Clearly state which worktree produced the best output
   - **Format**: "WINNER: [worktree-path] with total score: [score]"

2. **Provide Final Score/Ranking**
   - **Action**: Provide the final score or ranking
   - **Format**: 
     - Final ranking table (all worktrees with scores and ranks)
     - Winner score breakdown (per-requirement scores for winning worktree)

3. **Explain Winner Justification**
   - **Action**: Explain WHY this worktree is the best using evidence-based reasoning
   - **Required Elements**:
     - **Specific Evidence**: Provide specific evidence from analysis (reference specific files, changes, implementations)
     - **Direct Comparison**: Compare it directly with other worktrees (side-by-side comparison)
     - **Superiority Highlights**: Highlight what makes it superior with examples
     - **Per-Requirement Analysis**: For each requirement, explain how the winning worktree performed better
     - **File/Implementation References**: Reference specific files, changes, or implementations
     - **Evidence-Based Statements**: Avoid generic statements - be specific and evidence-based
   - **Validation**: Verify explanation includes specific evidence, direct comparisons, per-requirement analysis, and file references

#### Part 5: Create Analysis Report

**[STRICT]** Instruct the Prompt Generator to include instructions for structured report generation:

1. **Save Report**
   - **Action**: Save the analysis report in the current worktree directory
   - **Filename**: `worktree-analysis-report.md` (exact filename, case-sensitive)
   - **Location**: Current worktree directory (where analysis is being performed)

2. **Report Structure Requirements**
   - **Action**: Report structure must include these exact sections (in order):
     - **Executive Summary**: Brief overview of findings, key metrics, high-level conclusion
     - **Methodology**: How the analysis was conducted, tools and commands used, evaluation criteria, scoring method
     - **Individual Analysis**: Detailed analysis of each worktree (one subsection per worktree)
     - **Comparison Matrix**: Side-by-side comparison of all worktrees
     - **Winner Declaration**: Which worktree is best and why, final scores and ranking
     - **Detailed Reasoning**: Comprehensive explanation with evidence, per-requirement analysis, direct comparisons
     - **Recommendations**: What can be learned or improved, common strengths/weaknesses, best practices

3. **Formatting Requirements**
   - **Markdown Format**: Use markdown formatting throughout
   - **Code Blocks**: Include code blocks for file listings or diffs when relevant
   - **Tables**: Use tables for comparisons (markdown table syntax)
   - **Headers**: Use H2 for main sections, H3 for subsections, H4 for sub-subsections

**Validation Checkpoint 3.1**
**[STRICT]** After generating Step 3 instructions, verify:
- ✓ All parts included (Part 1-5 complete)
- ✓ Git worktree processing instructions specific (exact command, parsing method)
- ✓ Analysis instructions detailed (all evaluation steps specified)
- ✓ Comparison methodology clear (scoring, ranking, tie-breaking)
- ✓ Winner declaration requirements specific (evidence-based, not generic)
- ✓ Report structure requirements complete (all sections specified)

---

### STEP 4: Specify Prompt Engineering Best Practices

**[STRICT]** Instruct the Prompt Generator to ensure the generated analysis prompt follows these quality standards:

1. **Direct and Actionable**
   - **Requirement**: Use imperative verbs: "Run", "Check", "Compare", "Document", "Analyze", "Evaluate"
   - **Validation**: Verify all instructions use imperative mood (command form, not "you should" or "it would be good to")
   - **Example**: 
     - ❌ BAD: "You might want to analyze the worktrees"
     - ✅ GOOD: "Analyze all identified worktrees using the following steps"

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

7. **Leverage AI Capabilities**
   - **Requirement**: Design prompt to maximize AI effectiveness
   - **Method**: 
     - Use clear, structured instructions that AI can follow systematically
     - Include measurable criteria (scales, percentages) rather than subjective terms
     - Provide validation checkpoints that AI can verify
     - Include error handling that AI can execute
     - Structure output format that AI can generate consistently
   - **Validation**: Verify prompt uses measurable criteria, validation checkpoints, and structured output formats

**Validation Checkpoint 4.1**
**[STRICT]** After completing Step 4, verify:
- ✓ All quality standards specified (direct, specific, exact, explained, complete, no assumptions, AI-optimized)
- ✓ Examples provided for good vs bad practices
- ✓ Validation criteria specified for each standard

---

### STEP 5: Add Validation and Quality Assurance

**[STRICT]** Instruct the Prompt Generator to include validation checkpoints and quality gates in the generated analysis prompt:

1. **Validation Checkpoints**
   - **Requirement**: Include validation checkpoints at logical breakpoints
   - **Method**: After each major step or part, include a validation checkpoint with:
     - Measurable criteria (specific, testable conditions)
     - Success indicators (what constitutes success)
     - Failure handling (what to do if validation fails)
   - **Example**: "Validation Checkpoint: Verify at least one worktree path extracted. If none found, report error and halt execution."

2. **Error Handling Procedures**
   - **Requirement**: Include error handling for common failure modes
   - **Error Types to Handle**:
     - Git command failures (worktree list, status, diff)
     - File access errors (worktree directory inaccessible)
     - Missing files or content
     - Parsing errors (malformed command output)
   - **Method**: For each error type, specify:
     - Error detection method
     - Error message format
     - Recovery action (halt, skip, retry, or continue)
   - **Example**: "If `git worktree list` fails → report error: 'Failed to execute git worktree list. Verify Git is installed and repository is valid. Error: [specific error message]' and halt execution."

3. **Quality Gates**
   - **Requirement**: Specify quality thresholds that must be met
   - **Quality Criteria**:
     - **Completeness ≥95%**: All required sections present with all substeps
     - **Specificity 100%**: Zero vague terms (all instructions specific, all commands exact, all paths explicit)
     - **Actionability ≥90%**: Prompt is executable without external clarification (all inputs/outputs/criteria specified)
     - **Validation Coverage 100%**: All logical breakpoints have validation checkpoints with measurable criteria
   - **Method**: Include these thresholds in the generated prompt as success criteria

4. **Output Format Requirements**
   - **Requirement**: Specify exact output format for the analysis report
   - **Format Specifications**:
     - File format: Markdown (.md)
     - File name: `worktree-analysis-report.md`
     - File location: Current worktree directory
     - Structure: All required sections (as specified in Part 5)
     - Markdown syntax: Proper headers, lists, tables, code blocks
   - **Validation**: Verify output format requirements are explicit and complete

**Validation Checkpoint 5.1**
**[STRICT]** After completing Step 5, verify:
- ✓ Validation checkpoints specified (at logical breakpoints with measurable criteria)
- ✓ Error handling procedures included (all common failure modes covered)
- ✓ Quality gates specified (thresholds and success criteria)
- ✓ Output format requirements complete (file name, location, structure, formatting)

---

## OUTPUT REQUIREMENTS

**[STRICT]** The meta instruction you create must result in a Prompt Generator that produces analysis prompts meeting these requirements:

### Structure Requirements
- **Header Hierarchy**: Use H1 for main title, H2 for major steps, H3 for parts, H4 for substeps
- **Organization**: Linear, sequential structure with hierarchical parts
- **Section Order**: Preserve exact order: Part 1 → Part 2 → Part 3 → Part 4 → Part 5

### Formatting Requirements
- **Code Blocks**: Use for Git commands, code examples, diffs
- **Lists**: Use numbered lists for sequential steps, bulleted lists for non-sequential items
- **Tables**: Use markdown tables for comparison matrices
- **Emphasis**: Use **bold** for key terms, *italic* for emphasis, `` `backticks` `` for file paths and commands
- **Directives**: Use [STRICT] for mandatory requirements, [GUIDELINE] for recommendations

### Quality Requirements
- **Completeness**: All required sections present (Step 1-5, Part 1-5) with ≥95% coverage
- **Specificity**: All instructions are specific (no vague terms, all commands exact) with 100% specificity rate
- **Actionability**: Prompt can be executed by AI without ambiguity (all inputs, outputs, criteria specified) with ≥90% actionability score
- **Validation**: All validation checkpoints included at logical breakpoints with measurable criteria

### Success Criteria
The generated analysis prompt must enable an AI Analyzer to:
- ✓ Systematically identify all worktrees to analyze
- ✓ Thoroughly analyze each worktree against original prompt requirements
- ✓ Compare and rank worktrees using measurable criteria
- ✓ Declare a winner with evidence-based justification
- ✓ Generate a comprehensive analysis report

---

## EXECUTION MODE

**[STRICT]** This meta instruction operates in standard execution mode:
- ✓ All steps executed sequentially (Step 1 → Step 2 → Step 3 → Step 4 → Step 5)
- ✓ Validation checkpoints must pass before proceeding (no skipping validation)
- ✓ Error handling applied when errors occur (halt or skip based on error type)
- ✓ Final output is complete meta instruction (ready for Prompt Generator execution)

**Workflow Complete**: Meta instruction written and ready for use by AI Prompt Generator.
