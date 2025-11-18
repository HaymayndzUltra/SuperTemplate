---
name: analyze-worktrees
description: Analyze and compare multiple git worktrees to determine which implementation is best
allow_tools:
  - Bash(git worktree:*), Bash(git status:*), Bash(git diff:*), Bash(git log:*)
  - Read, Glob, Grep, LS, Task
  - mcp__supabase__*
  - mcp__cloudflare-bindings__*
---

# 🔍 UNIFIED `/analyze-worktrees` COMMAND

**Intelligent worktree analysis and comparison system!**

**IMPORTANT**: This command analyzes multiple git worktrees that executed the same prompt and determines which implementation is the best based on completeness, correctness, quality, and standards adherence.

## 📋 Usage

```
/analyze-worktrees <worktree-names> <prompt-file>
```

**Parameters:**
- `<worktree-names>`: Space-separated list of worktree identifiers (paths, branch names, or unique suffixes)
- `<prompt-file>`: Path to the original prompt file that was used to create the worktrees

**Examples:**
```
/analyze-worktrees E8eNo GSLTP H3gmt worktree-prompt1.md
/analyze-worktrees chore-cleanup-artifacts-docs-KjSDH chore-cleanup-artifacts-docs-Q28Pw worktree-prompt1.md
/analyze-worktrees /home/haymayndz/.cursor/worktrees/.../E8eNo worktree-prompt1.md
```

## 🎯 Execution Protocol

### Step 1: Parse Input Parameters

**[STRICT]** Extract and validate inputs:

1. **Worktree Identifiers**: Parse space-separated worktree names from command arguments
2. **Prompt File Path**: Extract the last argument as the prompt file path
3. **Validation**: 
   - Verify prompt file exists and is readable
   - Verify at least one worktree identifier provided
   - If validation fails → Report error and halt execution

### Step 2: Resolve Worktree Paths

**[STRICT]** For each worktree identifier, resolve to full path:

1. **Execute**: `git worktree list --porcelain`
2. **Match Strategy** (in order of priority):
   - **Exact Path Match**: If identifier is a full path, use directly
   - **Branch Name Match**: Match against branch names (e.g., `refs/heads/chore-cleanup-artifacts-docs-KjSDH`)
   - **Suffix Match**: Match against unique directory suffixes (e.g., `KjSDH` matches `.../KjSDH`)
   - **Partial Path Match**: Match against last path components
3. **Validation**: 
   - Each identifier must resolve to exactly one worktree
   - If ambiguous → Report: "Ambiguous worktree identifier: [name]. Found: [list]. Please be more specific."
   - If not found → Report: "Worktree not found: [name]. Available worktrees: [list]"
4. **Output**: List of resolved worktree paths

### Step 3: Read Original Prompt

**[STRICT]** Load and parse the original prompt file:

1. **Action**: Read the prompt file specified in arguments
2. **Extract**:
   - Requirements and expected outcomes
   - Quality criteria and standards
   - Success metrics
   - Any specific evaluation criteria
3. **Validation**: 
   - File must exist and be readable
   - File must contain meaningful content
   - If validation fails → Report error and halt execution

### Step 4: Analyze Each Worktree

**[STRICT]** For each resolved worktree path, execute systematic analysis:

#### 4.1 Navigate and Check Status

```bash
cd <worktree-path>
git status
git status --short
```

**Capture:**
- Modified files
- Added files
- Deleted files
- Untracked files
- Uncommitted changes
- Branch name
- Commit hash

#### 4.2 Analyze Changes

```bash
cd <worktree-path>
git diff
git diff --stat
git diff --name-status
```

**Capture:**
- All code/documentation changes
- Files modified/created/deleted
- Change statistics (lines added/removed)

#### 4.3 Check Commit History

```bash
cd <worktree-path>
git log --oneline -10
git log --stat -5
```

**Capture:**
- Commit messages
- Files changed per commit
- Implementation approach

#### 4.4 Evaluate Against Requirements

For each requirement from the original prompt:

- ✓ **Addressed**: Was the requirement addressed? (Yes/No/Partial)
- ✓ **Correctness**: Is the implementation correct? (1-10 scale)
- ✓ **Completeness**: How complete is the implementation? (1-10 scale)
- ✓ **Quality**: Code/documentation quality? (1-10 scale)
- ✓ **Standards**: Adherence to standards/guidelines? (1-10 scale)

**Evidence Collection:**
- List specific files that address each requirement
- Quote relevant code/documentation snippets
- Note any missing elements or issues

### Step 5: Comparative Analysis

**[STRICT]** Create comparison matrix:

1. **Requirement Matrix**: 
   - Rows: Each requirement from original prompt
   - Columns: Each worktree being analyzed
   - Cells: Score (1-10) + Evidence summary

2. **Overall Scoring**:
   - **Completeness Score**: Average of completeness scores (weight: 30%)
   - **Correctness Score**: Average of correctness scores (weight: 30%)
   - **Quality Score**: Average of quality scores (weight: 25%)
   - **Standards Score**: Average of standards scores (weight: 15%)
   - **Total Score**: Weighted average of all scores

3. **Ranking**: Sort worktrees by Total Score (descending)

### Step 6: Generate Analysis Report

**[STRICT]** Create comprehensive markdown report:

**Report Structure:**

```markdown
# Worktree Analysis Report

## Executive Summary
- Date: [timestamp]
- Prompt File: [path]
- Worktrees Analyzed: [count]
- Winner: [worktree-name] (Score: [X]/10)

## Original Prompt Requirements
[Extracted requirements from prompt file]

## Individual Worktree Analysis

### Worktree 1: [name/path]
- **Branch**: [branch-name]
- **Commit**: [commit-hash]
- **Status**: [clean/modified/uncommitted]
- **Files Changed**: [list]
- **Requirements Coverage**:
  - Requirement 1: [Addressed/Correctness/Completeness/Quality/Standards scores]
  - Requirement 2: [scores]
  - ...
- **Evidence**: [specific examples]
- **Overall Score**: [X]/10

[Repeat for each worktree]

## Comparative Analysis

### Requirement Matrix
| Requirement | Worktree 1 | Worktree 2 | Worktree 3 | ... |
|------------|-----------|-----------|-----------|-----|
| Req 1      | 8/10      | 7/10      | 9/10      | ... |
| Req 2      | 9/10      | 6/10      | 8/10      | ... |
| ...        | ...       | ...       | ...       | ... |

### Overall Scores
| Worktree | Completeness | Correctness | Quality | Standards | **Total** |
|----------|-------------|------------|---------|-----------|-----------|
| Worktree 1 | 8.5/10 (30%) | 8.0/10 (30%) | 7.5/10 (25%) | 8.0/10 (15%) | **8.0/10** |
| Worktree 2 | 7.0/10 (30%) | 7.5/10 (30%) | 8.0/10 (25%) | 7.5/10 (15%) | **7.5/10** |
| ... | ... | ... | ... | ... | ... |

## Winner Declaration

**🏆 Best Implementation: [Worktree Name]**

**Total Score**: [X]/10

**Justification**:
- [Specific reason 1 with evidence]
- [Specific reason 2 with evidence]
- [Specific reason 3 with evidence]

**Strengths**:
- [Strength 1]
- [Strength 2]
- ...

**Areas for Improvement**:
- [Improvement 1]
- [Improvement 2]
- ...

## Detailed Findings

### Requirement-by-Requirement Analysis

#### Requirement 1: [Name]
- **Best Implementation**: [Worktree Name] (Score: [X]/10)
- **Comparison**: [Detailed comparison]
- **Evidence**: [Code/documentation snippets]

[Repeat for each requirement]

## Recommendations

1. **For Winner**: [Recommendations to further improve]
2. **For Others**: [What they can learn from the winner]
3. **General**: [Overall project recommendations]
```

**Output Location**: Save report as `worktree-analysis-report.md` in the current directory

### Step 7: Present Results

**[STRICT]** Display summary to user:

1. **Quick Summary**: 
   - Number of worktrees analyzed
   - Winner declaration with score
   - Top 3 rankings

2. **Report Location**: 
   - Full report saved at: `worktree-analysis-report.md`

3. **Key Findings**: 
   - Highlight most significant differences
   - Note any critical issues found

## 🔄 Smart Features

### Automatic Worktree Discovery

If worktree names are not provided, the system can:

1. **List all worktrees**: `git worktree list`
2. **Filter by criteria**:
   - Recent worktrees (by timestamp)
   - Worktrees with specific branch name patterns
   - Worktrees with uncommitted changes
3. **Present selection interface**: Let user choose which to analyze

### Intelligent Matching

The system handles various identifier formats:

- **Full paths**: `/home/user/.cursor/worktrees/.../E8eNo`
- **Branch names**: `chore-cleanup-artifacts-docs-KjSDH`
- **Unique suffixes**: `KjSDH`, `E8eNo`
- **Partial matches**: `cleanup-artifacts` (matches multiple, reports ambiguity)

### Context-Aware Analysis

The system adapts analysis based on:

- **Prompt type**: Code changes vs Documentation vs Configuration
- **File types changed**: Code files → Focus on code quality; Docs → Focus on clarity
- **Change scope**: Small changes → Quick analysis; Large changes → Deep analysis

## 🎯 Output Format

All analysis results follow a **unified report format** ensuring:

- **Consistent structure** across different prompt types
- **Quantitative scoring** for objective comparison
- **Evidence-based conclusions** with specific examples
- **Actionable recommendations** for improvement

---

**🚀 Revolutionary DX**: Single `/analyze-worktrees` command with **intelligent worktree resolution**, **systematic analysis**, **quantitative comparison**, and **comprehensive reporting**. **Zero manual work** required - just provide worktree names and prompt file!

