# Sample PR Comparison Analysis

## Sample PR Data for Demonstration

## Sample PR Data for SuperTemplate Repository

### PR #1: Batch 1 design-to-operations protocols
- **Title**: "Add Batch 1 design-to-operations protocols and generator assets"
- **Status**: Open
- **URL**: https://github.com/HaymayndzUltra/SuperTemplate/pull/1
- **Risk Level**: Medium
- **Priority**: High
- **Dependencies**: None
- **Review Status**: Open, needs review

### PR #3: Architecture and environment protocols
- **Title**: "Add architecture, environment, and operations workflow protocols"
- **Status**: Open
- **URL**: https://github.com/HaymayndzUltra/SuperTemplate/pull/3
- **Risk Level**: Low
- **Priority**: High
- **Dependencies**: Depends on PR #1
- **Review Status**: Open, needs review

### PR #4: Critical deployment protocols
- **Title**: "Add Batch 1 critical deployment and operations protocols"
- **Status**: Open
- **URL**: https://github.com/HaymayndzUltra/SuperTemplate/pull/4
- **Risk Level**: High
- **Priority**: Critical
- **Dependencies**: Depends on PR #3
- **Review Status**: Open, needs review

### PR #8: Protocol reference mapping
- **Title**: "Add protocol reference mapping and validation collateral"
- **Status**: Open
- **URL**: https://github.com/HaymayndzUltra/SuperTemplate/pull/8
- **Risk Level**: Low
- **Priority**: Medium
- **Dependencies**: Independent
- **Review Status**: Open, needs review

## Comparison Analysis

### Summary Table
| PR | Title | Status | Risk | Priority | Action |
|----|-------|--------|------|----------|--------|
| 1 | Batch 1 protocols | Open | Medium | High | ⚠️ Review |
| 3 | Architecture protocols | Open | Low | High | ⚠️ Review |
| 4 | Deployment protocols | Open | High | Critical | ⚠️ Review |
| 8 | Reference mapping | Open | Low | Medium | ⚠️ Review |

### Dependencies Map
```
PR 1 (Batch 1) → PR 3 (Architecture)
PR 3 (Architecture) → PR 4 (Deployment)
PR 8 (Reference) → Independent
```

### Risk Assessment
- **Low Risk**: PR 3, PR 8
- **Medium Risk**: PR 1
- **High Risk**: PR 4

### Recommended Merge Order
1. **PR 1** - Batch 1 protocols (Foundation, enables PR 3)
2. **PR 3** - Architecture protocols (Depends on PR 1, enables PR 4)
3. **PR 4** - Deployment protocols (Critical, depends on PR 3)
4. **PR 8** - Reference mapping (Independent, can be merged anytime)

### Timeline Estimates
- **PR 1**: 2-3 days (needs review completion)
- **PR 3**: 1-2 days (depends on PR 1)
- **PR 4**: 3-5 days (depends on PR 3, critical)
- **PR 8**: 1-2 days (independent)

### Action Items
- [ ] **PR 1**: Complete review process, address comments
- [ ] **PR 3**: Wait for PR 1, then review
- [ ] **PR 4**: Wait for PR 3, prioritize review (critical)
- [ ] **PR 8**: Can be reviewed independently

### Resource Allocation
- **Protocol Team**: Focus on PR 1, 3, 4 (core protocols)
- **Documentation Team**: Focus on PR 8 (reference mapping)
- **Review Team**: Prioritize PR 4 (critical deployment)
- **QA Team**: Test PR 1, 3, 4 after merge

## Usage Example

To use this sample data with the `/compare-prs` command:

```
/compare-prs 1 3 4 8
```

## GitHub URLs for Quick Access
- https://github.com/HaymayndzUltra/SuperTemplate/pull/1
- https://github.com/HaymayndzUltra/SuperTemplate/pull/3
- https://github.com/HaymayndzUltra/SuperTemplate/pull/4
- https://github.com/HaymayndzUltra/SuperTemplate/pull/8

This will generate a comprehensive comparison analysis similar to the above, helping you make informed decisions about merge priorities and resource allocation.

## Integration with Cursor Commands

### With @codebase Context
```
@codebase /compare-prs 123 124 125 126
```

### With @recent-changes Context
```
@recent-changes /compare-prs 123 124 125 126
```

### With Multiple Contexts
```
@codebase @recent-changes /compare-prs 123 124 125 126
```

This sample demonstrates how the `/compare-prs` command can provide comprehensive analysis for multiple PRs, enabling better decision-making and resource planning.
