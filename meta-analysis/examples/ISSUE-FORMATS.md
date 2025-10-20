# ISSUE-TRACKING FORMATS

Para sa pag-break down ng protocol tasks into trackable issues sa GitHub/Jira/Linear.

---

## FORMAT: GITHUB/JIRA ISSUE SPLIT

**Source:** FORMATS2.md (lines 1019-1047)  
**Use When:** Converting protocol tasks to project management issues

### Template Structure:

```markdown
**Title:** [P{Priority}] {Feature}: {High-Level Task}

**Body:**

[STRICT] Provide a "DO" Example:
[GUIDELINES]:
[REASONING]
- Premises:
- Constraints:
- Alternatives Considered:
- Decision:
- Evidence:
- Risks & Mitigations:
- Acceptance Link:

**Subtasks**
- [ ] {X}.1 File Scaffolding
- [ ] {X}.2 Interface/Schema
- [ ] {X}.3 Surface/Entry
- [ ] {X}.4 Logic/Orchestration
- [ ] {X}.5 State/Coordination
- [ ] {X}.6 Policy/Theming/A11y
- [ ] {X}.7 Security/Observability
- [ ] {X}.8 Testing
- [ ] {X}.9 Docs/Runbooks
```

### Priority Levels:
- **[P0]**: Critical blocker
- **[P1]**: High priority
- **[P2]**: Medium priority
- **[P3]**: Low priority
- **[P4]**: Backlog

### Standard 9-Subtask Breakdown:
1. **File Scaffolding**: Directory structure and base files
2. **Interface/Schema**: Data structures, types, contracts
3. **Surface/Entry**: Public API, UI components, route handlers
4. **Logic/Orchestration**: Core business logic
5. **State/Coordination**: State management, caching
6. **Policy/Theming/A11y**: Styling, accessibility, i18n
7. **Security/Observability**: Security, logging, monitoring
8. **Testing**: Unit, integration, E2E tests
9. **Docs/Runbooks**: Documentation and operational guides

### When to Use:
- Creating issues in GitHub/Jira/Linear
- Breaking large tasks into manageable subtasks
- Maintaining decision history in issue tracker
- Coordinating work across multiple developers
