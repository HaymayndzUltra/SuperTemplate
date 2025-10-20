# PROMPT-ENGINEERING FORMATS

Para sa multi-agent systems at role-based LLM orchestration.

---

## FORMAT: MULTI-ROLE PROMPT PACK

**Source:** FORMATS2.md (lines 1051-1063)  
**Use When:** Setting up multi-agent AI systems with role separation

### Template Structure:

```markdown
**System:** Use Protocol 2. Preserve `[STRICT]` & `[GUIDELINES]`. Insert `[REASONING]` under every item. Halt after Phase 2 until user types `Go`.

**Developer:** Provide scaffolds only, no invented facts. Bind decisions to PRD sections and `@rules`. Output in the format the user requests (Markdown/JSON/YAML/CLI/Issues).

**User:**
* PRD: {link or inline}
* Primary layer: {Frontend|Backend|GlobalState}
* Output format: {markdown|json|yaml|cli|issues}
* Reply `Go` to proceed beyond Phase 2.
```

### Role Definitions:

**System Role:**
- Protocol compliance instructions
- Preservation rules for [STRICT]/[GUIDELINES]
- Halt-and-await patterns
- Quality gates

**Developer Role:**
- Output format requirements
- Constraint specifications
- Evidence binding rules
- No-invention policies

**User Role:**
- Input requirements
- Layer selection
- Format preferences
- Interaction triggers

### Output Format Options:
- **markdown**: Full Markdown execution plan
- **json**: Structured JSON with metadata
- **yaml**: YAML configuration format
- **cli**: Plain text checklist
- **issues**: GitHub/Jira issue format

### When to Use:
- Multi-agent AI systems
- LLM orchestration with role separation
- Interactive protocol execution with user gates
- Systems requiring flexible output formats
