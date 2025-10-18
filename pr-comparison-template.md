# PR Comparison Template

## Quick Comparison Template

### Basic Comparison Format
```
## PR Comparison Report - [Date]

### Summary
| PR | Title | Status | Lines | Risk | Priority | Action |
|----|-------|--------|-------|------|----------|--------|
| [PR#] | [Title] | [Status] | [Lines] | [Risk] | [Priority] | [Action] |

### Dependencies
- [PR A] → [PR B] (dependency relationship)
- [PR C] → Independent
- [PR D] → Conflicts with [PR E]

### Recommended Merge Order
1. [PR#] - [Reason]
2. [PR#] - [Reason]
3. [PR#] - [Reason]
4. [PR#] - [Reason]

### Risk Assessment
- **Low Risk**: [PR list]
- **Medium Risk**: [PR list]
- **High Risk**: [PR list]

### Action Items
- [ ] [PR#]: [Action needed]
- [ ] [PR#]: [Action needed]
- [ ] [PR#]: [Action needed]
- [ ] [PR#]: [Action needed]
```

## Detailed Comparison Template

### Comprehensive Analysis Format
```
## Comprehensive PR Analysis - [Date]

### Executive Summary
[Brief overview of all PRs and key findings]

### Individual PR Analysis

#### PR #[Number]: [Title]
- **Purpose**: [What this PR does]
- **Status**: [Current status]
- **Lines Changed**: [Additions/Deletions]
- **Files Modified**: [List of files]
- **Risk Level**: [Low/Medium/High]
- **Priority**: [Critical/High/Medium/Low]
- **Dependencies**: [What it depends on]
- **Review Status**: [Approvals/Comments]
- **Business Impact**: [Impact on users/business]
- **Technical Debt**: [Any technical debt introduced]
- **Performance Impact**: [Performance implications]
- **Security Considerations**: [Security implications]

### Cross-PR Analysis

#### Dependencies Map
```
[Visual representation of dependencies]
```

#### Conflict Analysis
- **File Conflicts**: [Files modified by multiple PRs]
- **Logic Conflicts**: [Conflicting business logic]
- **Integration Conflicts**: [API/interface conflicts]

#### Resource Impact
- **Team Capacity**: [How much team capacity needed]
- **Timeline Impact**: [How PRs affect each other's timelines]
- **Infrastructure Impact**: [Infrastructure changes needed]

### Risk Assessment Matrix

| PR | Technical Risk | Business Risk | Operational Risk | Overall Risk |
|----|----------------|---------------|------------------|--------------|
| [PR#] | [Level] | [Level] | [Level] | [Level] |
| [PR#] | [Level] | [Level] | [Level] | [Level] |
| [PR#] | [Level] | [Level] | [Level] | [Level] |
| [PR#] | [Level] | [Level] | [Level] | [Level] |

### Merge Strategy

#### Phase 1: Critical PRs
- [PR#]: [Reason for priority]
- [PR#]: [Reason for priority]

#### Phase 2: High Priority PRs
- [PR#]: [Reason for priority]
- [PR#]: [Reason for priority]

#### Phase 3: Medium Priority PRs
- [PR#]: [Reason for priority]

#### Phase 4: Low Priority PRs
- [PR#]: [Reason for priority]

### Timeline Estimates

| Phase | PRs | Estimated Time | Dependencies |
|-------|-----|----------------|--------------|
| Phase 1 | [PR list] | [Time] | [Dependencies] |
| Phase 2 | [PR list] | [Time] | [Dependencies] |
| Phase 3 | [PR list] | [Time] | [Dependencies] |
| Phase 4 | [PR list] | [Time] | [Dependencies] |

### Action Plan

#### Immediate Actions (Today)
- [ ] [Action item]
- [ ] [Action item]

#### Short Term (This Week)
- [ ] [Action item]
- [ ] [Action item]

#### Medium Term (Next Week)
- [ ] [Action item]
- [ ] [Action item]

#### Long Term (Next Month)
- [ ] [Action item]
- [ ] [Action item]

### Monitoring and Validation

#### Success Metrics
- [ ] All PRs merged successfully
- [ ] No production issues
- [ ] Performance maintained
- [ ] User satisfaction maintained

#### Rollback Plan
- [PR#]: [Rollback strategy]
- [PR#]: [Rollback strategy]
- [PR#]: [Rollback strategy]
- [PR#]: [Rollback strategy]

### Communication Plan

#### Stakeholder Updates
- **Engineering Team**: [Update frequency and content]
- **Product Team**: [Update frequency and content]
- **Management**: [Update frequency and content]
- **Users**: [Update frequency and content]

#### Escalation Procedures
- **Technical Issues**: [Escalation path]
- **Business Issues**: [Escalation path]
- **Timeline Issues**: [Escalation path]
- **Resource Issues**: [Escalation path]
```

## Quick Reference Templates

### Status Legend
- ✅ **Ready**: Approved and ready to merge
- ⚠️ **Review**: Needs review or has comments
- 🔄 **Draft**: In progress, not ready for review
- ❌ **Blocked**: Has blockers or conflicts
- 🚫 **Rejected**: Not approved or needs major changes

### Risk Levels
- **Low**: Minimal impact, well-tested, simple changes
- **Medium**: Moderate impact, some testing needed, moderate complexity
- **High**: Significant impact, extensive testing needed, complex changes

### Priority Levels
- **Critical**: Production issues, security vulnerabilities, blocking other work
- **High**: Important features, performance improvements, user-facing changes
- **Medium**: Nice-to-have features, internal improvements, technical debt
- **Low**: Future features, experimental work, non-essential changes

### Action Items
- **Merge**: Ready to merge immediately
- **Review**: Needs code review completion
- **Continue**: Continue development work
- **Blocked**: Resolve blockers before proceeding
- **Reject**: Not ready, needs major changes

## Usage Instructions

### For Quick Comparison
1. Copy the Basic Comparison Format
2. Fill in PR details
3. Analyze dependencies
4. Recommend merge order
5. List action items

### For Detailed Analysis
1. Copy the Comprehensive Analysis Format
2. Fill in detailed PR information
3. Perform cross-PR analysis
4. Create risk assessment matrix
5. Develop merge strategy
6. Create action plan
7. Set up monitoring

### Integration with Cursor
- Use with `/compare-prs` command
- Combine with `@codebase` for context
- Use with `@recent-changes` for timeline awareness
- Integrate with GitHub CLI for data retrieval

This template provides a structured approach to PR comparison analysis, ensuring comprehensive evaluation and informed decision-making.
