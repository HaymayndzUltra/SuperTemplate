# Compare Multiple PRs

## Purpose
Compare and analyze multiple pull requests simultaneously to make informed decisions about merge priorities, dependencies, and risks.

## Usage
```
/compare-prs [PR1] [PR2] [PR3] [PR4]
```

## Examples
```
/compare-prs 1 3 4 8
/compare-prs 9 10 11 12
```

## GitHub URL Format
Para sa SuperTemplate repository:
```
https://github.com/HaymayndzUltra/SuperTemplate/pull/[PR-number]
```

**Sample URLs:**
- https://github.com/HaymayndzUltra/SuperTemplate/pull/1
- https://github.com/HaymayndzUltra/SuperTemplate/pull/3
- https://github.com/HaymayndzUltra/SuperTemplate/pull/4
- https://github.com/HaymayndzUltra/SuperTemplate/pull/8

## Comparison Criteria

### Technical Analysis
- **Code Quality**: Lines changed, complexity, test coverage
- **Risk Level**: Breaking changes, security vulnerabilities, performance impact
- **Dependencies**: Files modified, integration points, conflicts
- **Review Status**: Approval status, comments, blockers
- **ACTUAL CODE REVIEW**: Detailed analysis of file changes, code patterns, and implementation quality
- **FILE CONFLICT ANALYSIS**: Detection of overlapping file modifications between PRs

### Business Analysis
- **Priority**: Critical, High, Medium, Low
- **Impact**: User-facing, internal, infrastructure
- **Timeline**: Urgency, deadlines, dependencies
- **Resources**: Team capacity, effort required
- **DETAILED EXPLANATION**: Comprehensive explanation of what each PR does and why it matters

## Output Format

### 🏆 Executive Recommendation: Best PR to Merge

**Recommended PR**: #[number] - [title]

**Why This PR Wins**:
- **Code Quality Score**: [score]/10 - [explanation]
- **Implementation Excellence**: [specific technical strengths]
- **Business Value**: [clear business impact]
- **Risk Assessment**: [why it's safe to merge]
- **Dependency Impact**: [what it enables/unblocks]

**Comparison to Other PRs**:
- vs PR #[X]: [why recommended PR is better]
- vs PR #[Y]: [why recommended PR is better]
- vs PR #[Z]: [why recommended PR is better]

**Action**: Merge this PR first, then reassess remaining PRs.

### Individual PR Deep Dive

For each PR, provide:

#### Code Quality Analysis
- **Implementation Score**: [X]/10
  - Pattern consistency: [details]
  - Code elegance: [details]
  - Best practices adherence: [details]
  
- **FILE-BY-FILE BREAKDOWN**:
  - `path/to/file1.ts` (+X/-Y lines):
    - **What changed**: [function/logic description]
    - **Code patterns detected**: [architectural patterns used]
    - **Quality assessment**: [strengths and potential issues]
    - **Performance impact**: [analysis of algorithmic complexity]
  
  - `path/to/file2.ts` (+X/-Y lines):
    - [same detailed analysis]

#### Conflict Detection
- **Files modified by this PR**: [list]
- **Overlapping with other PRs**: [list conflicts with PR numbers]
- **Risk level**: [LOW/MEDIUM/HIGH with explanation]

#### Business Value
- **What this PR accomplishes**: [clear explanation]
- **User impact**: [direct user-facing benefits]
- **Technical impact**: [system improvements]

#### Recommendation Factor
- **Merge readiness**: [why this PR should/shouldn't be merged first]
- **Blocking other PRs**: [dependencies]
- **Code quality edge**: [what makes this PR stand out]

- **ACTUAL CODE REVIEW**: Detailed analysis of specific file changes
- **FILE-BY-FILE ANALYSIS**: What each file does and how it changes
- **CODE PATTERN ANALYSIS**: Implementation patterns, best practices, potential issues
- **DETAILED EXPLANATION**: What the PR accomplishes and business value
- **CONFLICT DETECTION**: Files modified by multiple PRs and potential conflicts

### Summary Table
| PR | Title | Status | Lines | Risk | Priority | Action | Code Review Status |
|----|-------|--------|-------|------|----------|--------|-------------------|
| 123 | Feature A | Ready | +150/-20 | Low | High | ✅ Merge | ✅ Reviewed |
| 124 | Bug Fix | Review | +50/-100 | Medium | Critical | ⚠️ Review | ⚠️ Needs Review |
| 125 | Refactor | Draft | +200/-180 | Low | Medium | 🔄 Continue | 🔄 In Progress |
| 126 | Feature B | Blocked | +300/-50 | High | Low | ❌ Blocked | ❌ Blocked |

### Dependencies Map
```
PR 123 (Feature A) → PR 124 (Bug Fix)
PR 125 (Refactor) → Independent
PR 126 (Feature B) → Conflicts with PR 125
```

### File Conflict Matrix

| File Path | PR #1 | PR #2 | PR #3 | PR #4 | Risk Level |
|-----------|-------|-------|-------|-------|------------|
| src/auth/login.ts | ✅ | ❌ | ✅ | ❌ | 🔴 HIGH - Manual Review Required |
| src/api/users.ts | ✅ | ❌ | ❌ | ❌ | 🟢 LOW - Single PR |
| src/utils/helpers.ts | ❌ | ✅ | ✅ | ✅ | 🔴 CRITICAL - 3 PRs conflict |

**🔴 HIGH RISK FILES**: [list files modified by 2+ PRs]
**🟡 MEDIUM RISK FILES**: [list files with function-level dependencies]
**🟢 LOW RISK FILES**: [list files modified by single PR]

### Recommended Merge Order
1. **PR 123** - Ready, low risk, enables PR 124
2. **PR 124** - Critical bug fix, depends on PR 123
3. **PR 125** - Independent refactor, can be merged anytime
4. **PR 126** - Blocked, needs conflict resolution

### Risk Assessment
- **Low Risk**: PR 123, PR 125
- **Medium Risk**: PR 124
- **High Risk**: PR 126

## Code Review Process

### Mandatory Code Review Steps
1. **Fetch Actual File Changes**: Use GitHub API/CLI to get detailed file diffs
2. **File-Level Analysis**: For each modified file, analyze:
   - Code patterns (architecture, design patterns, best practices)
   - Function signatures and logic flow changes
   - Variable naming conventions and code clarity
   - Error handling and edge case coverage
   - Performance implications (loops, queries, algorithms)
3. **Cross-PR Conflict Detection**: Build a file modification matrix to identify:
   - Files modified by multiple PRs (HIGH RISK - flag for manual review)
   - Function-level conflicts (same functions modified)
   - Dependency conflicts (imports, exports, API contracts)
4. **Code Quality Scoring**: Rate each PR on:
   - Implementation elegance (1-10)
   - Code maintainability (1-10)
   - Pattern consistency (1-10)
   - Test coverage quality (1-10)
5. **Business Value Assessment**: Evaluate:
   - User-facing impact clarity
   - Technical debt reduction
   - System reliability improvement
6. **Recommendation Engine**: Compare all 4 PRs and select the single best PR based on:
   - Highest code quality score
   - Lowest risk assessment
   - Maximum business value
   - Optimal dependency enablement

### Code Review Checklist
- [ ] **File Changes Analyzed**: Every modified file reviewed
- [ ] **Code Patterns Identified**: Implementation patterns documented
- [ ] **Conflicts Detected**: File conflicts between PRs identified
- [ ] **Quality Assessed**: Code quality and best practices evaluated
- [ ] **Business Value Explained**: Clear explanation of PR purpose and impact
- [ ] **Risk Factors Identified**: Potential issues and mitigation strategies

## Integration Points
- Uses GitHub CLI for PR data retrieval
- Integrates with @codebase for context analysis
- Leverages @recent-changes for timeline awareness
- Connects with quality audit protocols
- **MANDATORY**: Fetches and analyzes actual file changes for comprehensive review

## Quality Gates
- [ ] All PRs analyzed for technical quality with code pattern detection
- [ ] File-level analysis completed for every modified file
- [ ] Cross-PR conflict matrix generated
- [ ] Files modified by multiple PRs flagged as HIGH RISK
- [ ] Code quality scores calculated (implementation, maintainability, patterns, tests)
- [ ] Business value assessed for each PR
- [ ] Dependencies identified and mapped
- [ ] Risk levels assessed and documented
- [ ] **EXECUTIVE RECOMMENDATION generated with comparative reasoning**
- [ ] **SINGLE BEST PR identified with clear justification**
- [ ] **CONFLICT RESOLUTION strategy defined for high-risk files**
- [ ] Action items defined for each PR
- [ ] **ACTUAL CODE REVIEW completed for each PR**
- [ ] **FILE-BY-FILE ANALYSIS documented**
- [ ] **CONFLICT DETECTION performed**
- [ ] **DETAILED EXPLANATION provided for each PR**

## Communication Scripts

### For Team Updates
```
"Based on PR comparison analysis:
- PR 123 is ready for merge (low risk, high priority)
- PR 124 needs immediate review (critical bug fix)
- PR 125 can wait (independent refactor)
- PR 126 is blocked and needs attention"
```

### For Stakeholder Reports
```
"PR Analysis Summary:
- 4 PRs analyzed
- 2 ready for merge
- 1 needs review
- 1 blocked
- Estimated merge timeline: 3-5 days"
```

## Handoff Checklist
- [ ] PR comparison matrix generated
- [ ] Dependencies mapped and documented
- [ ] Risk assessment completed
- [ ] Merge order recommended
- [ ] Action items assigned
- [ ] Timeline estimated
- [ ] Stakeholders notified
- [ ] Next steps defined

## Automation Hooks
- GitHub CLI integration for PR data
- Automated risk scoring based on code analysis
- Dependency detection using file change analysis
- Timeline estimation based on historical data

## Evidence Requirements
- PR metadata (title, status, lines changed)
- Code quality metrics
- Review status and comments
- Dependency analysis results
- Risk assessment documentation
- Merge order justification
- Timeline estimates
- Action item assignments
- **ACTUAL FILE CHANGES**: Detailed analysis of each modified file
- **CODE PATTERN ANALYSIS**: Implementation patterns and quality assessment
- **CONFLICT EVIDENCE**: Specific file conflicts and resolution strategies
- **DETAILED EXPLANATIONS**: Comprehensive understanding of each PR's purpose and impact

---

**Next Steps**: Use this command to analyze your 4 PRs and get comprehensive comparison insights for better decision-making.
