# PROTOCOL 05B PLACEMENT & NAMING GUIDE

## Recommended File Name
```
05b-project-protocol-orchestration.md
```

## Naming Rationale
- **"05b"** - Sub-protocol to Protocol 05 (uses "b" suffix convention)
- **"project"** - Emphasizes project-specific analysis
- **"protocol"** - Core subject matter
- **"orchestration"** - Key capability (routing/selection)

## Alternative Names (if preferred)
1. `05b-protocol-execution-planner.md`
2. `05b-intelligent-workflow-router.md`
3. `05b-protocol-selection-orchestration.md`

## Directory Placement

### Option A: Generic Workflow (Recommended)
```
/home/haymayndz/SuperTemplate/.cursor/ai-driven-workflow/
└── 05b-project-protocol-orchestration.md
```

**Pros:**
- Available to all project types
- Standard location for shared protocols

### Option B: AI Workflow
```
/home/haymayndz/SuperTemplate/AI-project-workflow/
└── 05b-project-protocol-orchestration.md
```

**Pros:**
- Co-located with AI protocols
- AI-first projects benefit

### Option C: Both (Recommended for Consistency)
- Add to BOTH directories
- Ensures availability regardless of entry point

## File Naming Convention

### Pattern
```
{number}{suffix}-{verb}-{noun}-{qualifier}.md
```

### Components
- **{number}**: 05 (phase 0 position)
- **{suffix}**: b (sub-protocol)
- **{verb}**: orchestration (action)
- **{noun}**: protocol (subject)
- **{qualifier}**: execution, planning (optional clarifier)

### Examples Following Pattern
- `05b-protocol-orchestration.md` ✅
- `05b-project-protocol-orchestration.md` ✅ (Recommended)
- `05b-workflow-router.md` ✅
- `05.5-protocol-planner.md` ⚠️ (Decimal may cause sorting issues)

## Version Control

### Initial Version
- **Version:** 1.0
- **Created:** 2025-11-08
- **Author:** Workflow Architect

### Version History Format
```yaml
versions:
  - version: 1.0
    date: 2025-11-08
    changes: Initial creation
    author: Workflow Architect
```

## Integration with Existing Protocols

### Update Required Files

1. **Protocol 05 Handoff**
   - Update Protocol 05 to hand off to 05b (not directly to 06)
   - Modify: `.cursor/ai-driven-workflow/05-bootstrap-your-project.md`
   - Section: HANDOFF CHECKLIST
   - Add: "Next Protocol: 05b (Project Protocol Orchestration)"

2. **Protocol Integration Map**
   - Update: `.cursor/ai-driven-workflow/25-protocol-integration-map-DOCUMENTATION.md`
   - Add 05b to dependency graph

3. **Script Registry**
   - Update: `scripts/script-registry.json`
   - Add Protocol 05b automation scripts

## File Header Template

```markdown
---
**MASTER RAY™ AI-Driven Workflow Protocol**
© 2025 - All Rights Reserved
---

# PROTOCOL 05B: PROJECT PROTOCOL ORCHESTRATION & EXECUTION PLANNING
```

## Recommended Implementation Steps

1. **Create Protocol File**
   ```bash
   # Combine the 3 parts created earlier
   cat .artifacts/protocol-generation/templates/protocol-05b-PART1-HEADER.md \
       .artifacts/protocol-generation/templates/protocol-05b-PART2-WORKFLOW.md \
       .artifacts/protocol-generation/templates/protocol-05b-PART3-GATES.md \
       > .cursor/ai-driven-workflow/05b-project-protocol-orchestration.md
   ```

2. **Validate Protocol**
   ```bash
   python validators-system/scripts/validate_all_protocols.py \
     --protocol-dir .cursor/ai-driven-workflow \
     --protocol-id 05b
   ```

3. **Update Protocol 05**
   - Modify handoff section to reference 05b

4. **Test Integration**
   - Run through Protocol 01-05
   - Execute 05b with sample PROJECT-BRIEF
   - Verify execution plan generation

## Success Criteria

- [ ] Protocol file created at correct location
- [ ] Validation score ≥0.95 across all 10 validators
- [ ] Protocol 05 updated to hand off to 05b
- [ ] Script registry updated
- [ ] Integration tested successfully
- [ ] Documentation updated
