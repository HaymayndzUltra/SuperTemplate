# Generate Worktree Analysis Prompt

You are tasked to generate a detailed prompt that will analyze and compare outputs from previous worktree agents.

## Step 1: Read and Understand the Original Prompt

1. Read the file: `/home/haymayndz/SuperTemplate-1/worktree-prompt1.md`
2. Analyze what the original instruction was asking the agents to do
3. Extract all requirements, expected outcomes, and quality criteria from the original prompt
4. Document these requirements clearly - these will be your evaluation criteria

## Step 2: Generate the Analysis Prompt

Generate a prompt that instructs to:

### Part 1: Identify Worktrees to Analyze

Include this instruction in your generated prompt:
- Run the command: `git worktree list`
- Parse the output to identify all worktree directories
- Determine which worktrees are the most recently created
- List all worktree paths that need to be analyzed
- Analyze ALL identified worktrees, not just one

### Part 2: Analyze Each Worktree

Include detailed instructions for:
- Navigate to each worktree directory
- Run `git status` to see what files were changed
- Run `git diff` to see what changes were made
- List all files that were created, modified, or changed
- For each requirement from the original prompt:
  - Check if the requirement was addressed
  - Verify if the implementation is correct
  - Assess if it was fully completed or partially done
  - Note any missing elements
- Evaluate code quality (if code was produced)
- Evaluate documentation quality (if documentation was produced)
- Check adherence to standards mentioned in the original prompt

### Part 3: Compare and Rank All Worktrees

Include instructions to:
- Create a comparison matrix or checklist
- For each worktree, score how well it meets each requirement (use 1-10 scale or percentage)
- Rank all worktrees from best to worst
- Identify which worktree has the highest score
- If there are ties, use tie-breaking criteria: completeness > accuracy > quality > adherence to standards

### Part 4: Declare Winner and Explain

Include instructions to:
- Clearly state which worktree produced the best output
- Provide the final score or ranking
- Explain WHY this worktree is the best:
  - Provide specific evidence from your analysis
  - Compare it directly with other worktrees
  - Highlight what makes it superior (e.g., "Worktree X completed all requirements while Worktree Y missed requirement 3")
  - Point out specific strengths (e.g., "Worktree X's documentation is more comprehensive", "Worktree Y's implementation is more accurate")
  - For each requirement, explain how the winning worktree performed better
  - Show side-by-side comparisons where relevant
  - Reference specific files, changes, or implementations
  - Avoid generic statements - be specific and evidence-based

### Part 5: Create Analysis Report

Include instructions to:
- Save the analysis report in the current worktree directory
- Filename: `worktree-analysis-report.md`
- Report structure must include:
  - **Executive Summary:** Brief overview of findings
  - **Methodology:** How the analysis was conducted
  - **Individual Analysis:** Detailed analysis of each worktree
  - **Comparison Matrix:** Side-by-side comparison of all worktrees
  - **Winner Declaration:** Which worktree is best and why
  - **Detailed Reasoning:** Comprehensive explanation with evidence
  - **Recommendations:** What can be learned or improved
- Use markdown formatting
- Include code blocks for file listings or diffs when relevant
- Use tables for comparisons

## Step 3: Format Your Generated Prompt

Your generated prompt should be:
- Direct and actionable (use imperative verbs: "Run", "Check", "Compare", "Document")
- Specific, not generic (don't say "analyze the output" - say "navigate to worktree directory X, run git status, list all modified files")
- Include exact commands to run
- Explain WHY each step is important
- Cover all aspects: identification, analysis, comparison, decision, explanation
- Nothing should be left to assumption

## Step 4: Output Your Generated Prompt

Output the complete generated prompt that follows all the instructions above.
