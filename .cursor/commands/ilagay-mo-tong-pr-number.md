# SYSTEM INSTRUCTION: PR Analysis and Selection Protocol

## Core Directive
# [STRICT] This system instruction defines the protocol for analyzing multiple GitHub Pull Requests 
# and selecting the most logical and suitable one for the AI-Driven Template Testing codebase.

## Analysis Protocol

### Phase 1: PR Discovery and Initial Assessment
# [STRICT] Before any analysis, you MUST:

# 1. Fetch all 4 PRs from the repository HaymayndzUltra/SuperTemplate:
#    - PR #<PR_NUMBER_1>
#    - PR #<PR_NUMBER_2>  
#    - PR #<PR_NUMBER_3>
#    - PR #<PR_NUMBER_4>

# 2. Extract key metadata for each PR:
#    - Title and description
#    - Files changed
#    - Lines added/removed
#    - Author and creation date
#    - Current status (open/merged/closed)

### Phase 2: Comprehensive PR Analysis
# [STRICT] For each PR, perform a 4-layer analysis:

#### Layer 1: Content Analysis
# - Type Classification: Implementation, Analysis, Inventory, Documentation, Bug Fix, Feature Addition
# - Scope Assessment: Core system, Scripts, Protocols, Templates, Documentation
# - Complexity Rating: Simple (1-3), Medium (4-6), Complex (7-10)

#### Layer 2: Codebase Alignment Analysis
# - Relevance Score: How well does this PR align with the AI-Driven Template Testing system?
# - Dependency Check: Does this PR depend on existing codebase components?
# - Integration Impact: Will this PR enhance or disrupt existing workflows?

#### Layer 3: Quality Assessment
# - Code Quality: Clean, well-structured, follows patterns
# - Documentation: Adequate comments, README updates, changelog entries
# - Testing: Unit tests, integration tests, validation scripts
# - Security: No security vulnerabilities introduced

#### Layer 4: Strategic Value Analysis
# - Immediate Value: Does this solve current pain points?
# - Future Value: Does this enable future improvements?
# - Maintenance Impact: Easy to maintain and extend?
# - Risk Assessment: Low, Medium, High risk of introducing issues

### Phase 3: Comparative Analysis Matrix
# [STRICT] Create a comparison matrix:

# | PR | Type | Scope | Complexity | Relevance | Quality | Strategic Value | Risk | Total Score |
# |----|------|-------|------------|-----------|---------|-----------------|------|-------------|
# | <PR_NUMBER_1> | [Type] | [Scope] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [Score] |
# | <PR_NUMBER_2> | [Type] | [Scope] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [Score] |
# | <PR_NUMBER_3> | [Type] | [Scope] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [Score] |
# | <PR_NUMBER_4> | [Type] | [Scope] | [1-10] | [1-10] | [1-10] | [1-10] | [1-10] | [Score] |

### Phase 4: Selection Criteria and Decision Logic
# [STRICT] Apply these decision criteria in order:

# 1. Codebase Alignment Priority: PRs that enhance the AI-Driven Template Testing system get highest priority
# 2. Quality Gate: PRs must pass minimum quality threshold (7/10)
# 3. Risk Assessment: Prefer low-risk PRs unless high-value justifies medium risk
# 4. Strategic Value: Prioritize PRs that solve immediate needs and enable future growth
# 5. Maintenance Sustainability: Choose PRs that are easy to maintain and extend

### Phase 5: Final Selection and Justification
# [STRICT] After analyzing all PRs:

# 1. Select the winning PR based on highest total score
# 2. Provide detailed justification explaining why this PR was chosen
# 3. Document rejected PRs with reasons for rejection
# 4. Create implementation plan for the selected PR

## Quality Gates
# [STRICT] Before finalizing selection, verify:

# 1. All 4 PRs analyzed: No PR skipped or overlooked
# 2. Consistent scoring: Same criteria applied to all PRs
# 3. Justification complete: Clear reasoning for selection and rejections
# 4. Implementation ready: Selected PR can be immediately implemented
# 5. Risk acceptable: Selected PR doesn't introduce unacceptable risks

## Success Criteria
# - ✅ All 4 PRs thoroughly analyzed
# - ✅ Clear selection criteria applied consistently
# - ✅ Detailed justification provided
# - ✅ Implementation plan created
# - ✅ Quality gates passed
# - ✅ Decision documented and traceable

# ========================================
# PR SETUP AND EXECUTION COMMANDS
# ========================================

# 1) Gumawa ng folder + file
mkdir -p .ai-review
cat > .ai-review/prs.txt <<'EOF'

<PR_NUMBER_1>
<PR_NUMBER_2>
<PR_NUMBER_3>
<PR_NUMBER_4>

EOF

# 2) Suriin kung tama ang format (apat na linya, puro number)
nl -ba .ai-review/prs.txt
grep -E '^[0-9]+$' .ai-review/prs.txt | wc -l   # dapat 4 ang output

# 3) Patakbuhin ang runner (hal. run_review.sh mo)
bash run_review.sh

# ========================================
# ANALYSIS EXECUTION PROTOCOL
# ========================================

# Step 1: Execute Analysis
python scripts/analyze_prs.py --prs "<PR_NUMBER_1>,<PR_NUMBER_2>,<PR_NUMBER_3>,<PR_NUMBER_4>" --repo "HaymayndzUltra/SuperTemplate"

# Step 2: Generate Report
python scripts/generate_pr_analysis_report.py --output "pr-analysis-report.md"

# Step 3: Create Selection Summary
python scripts/create_selection_summary.py --selected-pr <SELECTED_PR_NUMBER> --output "selected-pr-summary.md"

# ========================================
# EXPECTED OUTPUT FORMAT
# ========================================

# Executive Summary
# SELECTED PR: #<SELECTED_PR_NUMBER> - [TITLE]
# SCORE: [X]/10
# JUSTIFICATION: [Brief explanation]
# 
# REJECTED PRs:
# - PR #<REJECTED_PR_1>: [Reason for rejection]
# - PR #<REJECTED_PR_2>: [Reason for rejection]
# - PR #<REJECTED_PR_3>: [Reason for rejection]

# Detailed Analysis Report
# ## PR #<PR_NUMBER_X> Analysis
# 
# ### Content Analysis
# - Type: [Implementation/Analysis/Inventory/etc.]
# - Scope: [Core/Scripts/Protocols/Templates/Documentation]
# - Complexity: [1-10]
# 
# ### Codebase Alignment
# - Relevance Score: [1-10]
# - Dependency Impact: [Description]
# - Integration Impact: [Description]
# 
# ### Quality Assessment
# - Code Quality: [1-10]
# - Documentation: [1-10]
# - Testing: [1-10]
# - Security: [1-10]
# 
# ### Strategic Value
# - Immediate Value: [Description]
# - Future Value: [Description]
# - Maintenance Impact: [Description]
# - Risk Level: [Low/Medium/High]
# 
# ### Final Score: [X]/10