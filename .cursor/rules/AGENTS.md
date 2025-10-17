# 🤖 AGENTS.md - External AI Agent Rules Interpretation Guide

## Purpose
This document provides **comprehensive instructions** for external cloud LLMs (ChatGPT, Claude, Gemini, etc.) on how to interpret and apply the `.mdc` (Markdown with Cursor) rule system used in this project. This ensures **consistent AI behavior** across different platforms.

## 🚨 CRITICAL: Mandatory First Steps

### Step 1: Rule Discovery Protocol
**[STRICT]** Before any other action, external AI agents MUST:

1. **Scan for Rules**: Look for `.cursor/rules/` directory
2. **Read All .mdc Files**: Parse YAML frontmatter of every `.mdc` file
3. **Apply Priority System**: Load rules based on priority (see below)
4. **Announce Loaded Rules**: Inform user which rules are active

### Step 2: Context Analysis
**[STRICT]** Analyze current context:
- **Working Directory**: Where is the user working?
- **File Types**: What technology stack is detected?
- **User Request**: What keywords and intent are present?
- **Project Scope**: What domain/scope applies?

## Understanding .mdc Format

### File Structure
```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary"
alwaysApply: true/false
globs: "file-patterns"
---

# Rule Title

## Rule Content
Detailed instructions for AI agents...
```

### Frontmatter Components

#### Description Field (MANDATORY)
**Format**: `TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary`

**Components**:
- **TAGS**: Categories for rule classification (e.g., `[ui,frontend,component]`)
- **TRIGGERS**: Keywords that activate this rule (e.g., `component,ui,react`)
- **SCOPE**: Where this rule applies (`global`, `frontend`, `backend`, `project-name`)
- **DESCRIPTION**: Brief summary of rule purpose

#### alwaysApply Property
- **`true`**: Rule is **MANDATORY** and must be loaded in every session
- **`false`**: Rule is **optional** and loaded based on relevance

#### globs Property (Optional)
- **File Patterns**: Specific file patterns this rule applies to
- **Examples**: `"*.tsx"`, `"**/components/**"`, `"*.md"`

## Rule Loading Logic

### Priority System (MANDATORY)
External AI agents MUST follow this **exact priority order**:

#### Priority 1: Absolute Directives (Kernel) - HIGHEST
- Rules with `alwaysApply: true`
- Core system rules (collaboration guidelines, context discovery)
- **CRITICAL**: Must be loaded FIRST, no exceptions

#### Priority 2: Scope Matching
- Rules whose `SCOPE` perfectly matches current context
- Perfect scope matches get highest relevance
- Examples: `frontend` scope for React work, `backend` scope for API work

#### Priority 3: Keyword Matching (TRIGGERS)
- Rules whose `TRIGGERS` contain keywords from user request
- Partial matches are acceptable
- Case-insensitive matching

#### Priority 4: Concept Matching (TAGS)
- Rules whose `TAGS` align with task intent
- Used as general guidance
- Broader category matching

### Loading Process Algorithm
```
1. SCAN: Find all .mdc files in .cursor/rules/ and subdirectories
2. PARSE: Read YAML frontmatter of each file
3. FILTER: Apply priority system to select relevant rules
4. LOAD: Load selected rules into context
5. ANNOUNCE: Inform user which rules are active
6. APPLY: Execute rule instructions when triggered
```

## Rule Application Logic

### Context Detection Triggers
Rules are applied based on:

1. **Directory Context**
   - Current working directory
   - Project structure detected
   - Technology stack identified

2. **File Context**
   - File types being worked on
   - File patterns matching `globs`
   - File content analysis

3. **Request Context**
   - Keywords in user request
   - Intent analysis
   - Task complexity assessment

4. **Technology Context**
   - Framework detection (React, Vue, Angular)
   - Language detection (TypeScript, Python, Go)
   - Platform detection (Web, Mobile, Desktop)

### Rule Execution Protocol
When a rule is triggered:

1. **Parse Instructions**: Extract actionable steps from rule content
2. **Validate Context**: Ensure rule applies to current situation
3. **Execute Steps**: Follow rule instructions precisely
4. **Collect Evidence**: Document compliance and results
5. **Report Results**: Provide feedback to user

## Master Rules Specific Logic

### Core Master Rules (alwaysApply: true)
These rules form the **kernel** and must ALWAYS be loaded:

1. **Context Discovery Protocol** - System initialization and rule loading
2. **AI Collaboration Guidelines** - Human-AI interaction protocols
3. **Code Quality Checklist** - Development standards and best practices
4. **Code Modification Safety** - Change management and validation
5. **Documentation Guidelines** - Documentation standards and updates

### Rule Dependencies
Some rules depend on others (load in order):
- **Context Discovery** → **Collaboration Guidelines**
- **Code Quality** → **Safety Protocol**
- **Documentation** → **Quality Checklist**

### Conflict Resolution Protocol
When rules conflict:
1. **Higher Priority Wins**: Kernel rules override others
2. **More Specific Wins**: Specific rules override general
3. **User Override**: User can explicitly override rules
4. **Context Override**: Context-specific rules override global

## Common Rules Logic

### Loading Criteria
Common rules are loaded when:
- **Scope Match**: Rule scope matches current context
- **Trigger Match**: Keywords in user request
- **Technology Match**: Rule applies to current tech stack
- **Domain Match**: Rule applies to current domain

### Application Patterns
Common rules follow these patterns:
- **UI Rules**: Applied when working on frontend components
- **Backend Rules**: Applied when working on APIs and services
- **Security Rules**: Applied when security-sensitive code
- **Performance Rules**: Applied when performance-critical code
- **Testing Rules**: Applied when writing or running tests

## Evidence Collection Protocol

### Required Evidence
Each rule application MUST collect:
- **Rule ID**: Which rule was applied
- **Context**: Why rule was triggered
- **Actions**: What was done
- **Results**: Outcome of rule application
- **Validation**: Evidence of compliance

### Evidence Format
```json
{
  "ruleId": "rule-name",
  "timestamp": "2024-01-01T00:00:00Z",
  "context": "description of context",
  "actions": ["action1", "action2"],
  "results": "outcome description",
  "evidence": "proof of compliance"
}
```

## Error Handling Protocol

### Malformed Rules
When a rule has malformed frontmatter:
1. **Skip Rule**: Don't load malformed rules
2. **Log Error**: Record the issue
3. **Continue**: Proceed with other rules
4. **Report**: Inform user of skipped rules

### Missing Dependencies
When required rules are missing:
1. **Halt Execution**: Stop if kernel rules missing
2. **Report Critical Error**: Inform user immediately
3. **Suggest Fix**: Provide guidance on fixing issue

### Rule Conflicts
When rules conflict:
1. **Apply Priority**: Use priority system to resolve
2. **Document Conflict**: Record conflicting rules
3. **Choose Winner**: Select rule with higher priority
4. **Report Decision**: Explain resolution to user

## External AI Agent Integration

### Platform-Agnostic Approach
External AI agents should:
- **Not Assume Tools**: Don't assume specific tools exist
- **Adapt to Environment**: Work with available capabilities
- **Provide Alternatives**: Suggest manual methods if tools unavailable
- **Document Limitations**: Inform user of constraints

### Tool Discovery Protocol
For any action that could be automated:
1. **Discovery**: Check if suitable tool is available
2. **Execution**: Use tool if found, manual method if not
3. **Documentation**: Explain approach taken

### Command Integration
External AI agents can integrate with:
- **File Operations**: Read/write files when possible
- **Code Analysis**: Analyze code structure and patterns
- **Documentation**: Generate and update documentation
- **Validation**: Check code quality and compliance

## Best Practices for External AI Agents

### Rule Interpretation
1. **Read Frontmatter First**: Always parse YAML first
2. **Validate Format**: Ensure proper structure
3. **Check Dependencies**: Verify required rules exist
4. **Apply Priority**: Follow priority system strictly

### Rule Execution
1. **Follow Instructions**: Execute steps precisely
2. **Collect Evidence**: Document all actions
3. **Validate Results**: Ensure compliance
4. **Report Status**: Provide clear feedback

### Rule Management
1. **Load Efficiently**: Only load relevant rules
2. **Cache Results**: Store rule analysis when possible
3. **Update Context**: Refresh when context changes
4. **Handle Errors**: Graceful error handling

## Troubleshooting Guide

### Common Issues
1. **Rules Not Loading**: Check file paths and format
2. **Conflicting Rules**: Apply priority system
3. **Missing Context**: Ensure proper context detection
4. **Malformed Rules**: Validate YAML syntax

### Debug Process
1. **List All Rules**: Scan `.cursor/rules/` directory
2. **Validate Format**: Check YAML frontmatter
3. **Test Loading**: Verify rule loading logic
4. **Check Dependencies**: Ensure required rules exist

### Error Messages
When issues occur, provide clear error messages:
- **File Not Found**: "Rule file not found at path: {path}"
- **Malformed YAML**: "Invalid YAML frontmatter in: {file}"
- **Missing Dependency**: "Required rule missing: {rule-name}"
- **Conflict Detected**: "Rule conflict between: {rule1} and {rule2}"

## Implementation Examples

### Example 1: Loading Rules
```python
# Pseudo-code for rule loading
def load_rules():
    rules = []
    
    # Scan for .mdc files
    for file in find_files(".cursor/rules", "*.mdc"):
        frontmatter = parse_yaml_frontmatter(file)
        
        # Apply priority system
        if frontmatter.get("alwaysApply"):
            rules.insert(0, load_rule(file))  # Highest priority
        elif scope_matches(frontmatter["scope"]):
            rules.append(load_rule(file))
        elif triggers_match(frontmatter["triggers"]):
            rules.append(load_rule(file))
    
    return rules
```

### Example 2: Rule Application
```python
# Pseudo-code for rule application
def apply_rules(user_request, context):
    applicable_rules = []
    
    for rule in loaded_rules:
        if rule.triggers_match(user_request):
            applicable_rules.append(rule)
    
    # Execute rules in priority order
    for rule in sorted(applicable_rules, key=lambda r: r.priority):
        rule.execute(context)
```

## Conclusion

The `.mdc` format provides a powerful way to define AI agent behavior through structured rules. By understanding the frontmatter format, priority system, and application logic, external AI agents can effectively interpret and apply these rules to provide consistent, high-quality assistance.

**Key Takeaways**:
- **Frontmatter is Critical**: YAML metadata drives rule behavior
- **Priority Matters**: Kernel rules must be loaded first
- **Context is Key**: Rules apply based on current context
- **Evidence Required**: Always document rule application
- **Error Handling**: Graceful handling of malformed rules
- **Platform Agnostic**: Adapt to available tools and capabilities

This system ensures that external AI agents can provide consistent, rule-based assistance while maintaining flexibility and adaptability to different contexts and requirements.

---

## Quick Reference Card

### Rule Loading Checklist
- [ ] Scan `.cursor/rules/` directory
- [ ] Parse YAML frontmatter
- [ ] Apply priority system
- [ ] Load kernel rules first
- [ ] Load context-relevant rules
- [ ] Announce loaded rules
- [ ] Execute when triggered

### Priority Order
1. `alwaysApply: true` (Kernel)
2. Scope matching
3. Trigger matching
4. Tag matching

### Evidence Collection
- Rule ID
- Context
- Actions
- Results
- Validation

### Error Handling
- Skip malformed rules
- Report missing dependencies
- Resolve conflicts by priority
- Provide clear error messages
