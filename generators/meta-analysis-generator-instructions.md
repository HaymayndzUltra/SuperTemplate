# Meta-Instruction Analysis Generator: System Instructions

## PURPOSE
This document provides **complete system instructions** for AI agents to generate Meta-Instruction Analysis documents for any protocol, rule, or file. The output must be **identical in structure** to existing analysis files in `/meta-analysis/session-*/analysis-*.md`.

## INPUT REQUIREMENTS

### Mandatory Inputs
- **Source File Path**: Absolute path to the protocol/rule/file to analyze
- **Protocol Brief**: 1-2 sentence description of purpose/function (optional: auto-extract from file)
- **Analysis Scope**: Optional line ranges or specific sections to focus on
- **Output Format**: Markdown with strict structural compliance

### Optional Inputs
- **Context**: Additional background information about the protocol's role in larger system
- **Focus Areas**: Specific aspects to emphasize (governance, automation, communication, etc.)

## ANALYSIS METHODOLOGY PROTOCOL

### 4-Layer Extraction Framework

#### Layer 1: System-Level Decisions
**Objective**: Extract macro-level architectural decisions and foundational principles

**Extraction Targets**:
- Mission statements and role definitions
- Governance constraints and safety boundaries
- High-level behavioral boundaries
- Architectural principles and design philosophy

**Evidence Requirements**:
- Line references to explicit mission/role statements
- Governance constraints with specific prohibitions/permissions
- Architectural decisions with reasoning

#### Layer 2: Behavioral Control
**Objective**: Extract validation checkpoints and behavioral control mechanisms

**Extraction Targets**:
- Human-in-the-loop validation gates
- State transition controls
- Compliance enforcement mechanisms
- Progress gating and checkpoint requirements

**Evidence Requirements**:
- Line references to validation requirements
- Checkpoint definitions with pass/fail criteria
- Behavioral constraints and control flows

#### Layer 3: Procedural Logic
**Objective**: Extract concrete algorithmic steps and execution procedures

**Extraction Targets**:
- Concrete algorithmic steps
- Tool invocations and automation scripts
- Data flow and transformation logic
- Sequential execution requirements

**Evidence Requirements**:
- Line references to specific procedures
- Tool/command invocations
- Data flow descriptions
- Sequential step definitions

#### Layer 4: Communication Grammar
**Objective**: Extract narrative structures and communication patterns

**Extraction Targets**:
- Narrative structures and announcement templates
- User-facing prompts and validation dialogs
- Consent-driven communication patterns
- Status reporting and telemetry formats

**Evidence Requirements**:
- Line references to communication templates
- Example dialogs and prompts
- Announcement formats and structures

## OUTPUT TEMPLATE SPECIFICATION

```markdown
# Meta-Instruction Analysis: <source-file-path>

## PHASE MAP
### Layer 1: System-Level Decisions
**Step N:** [Decision/Principle Title] (ref. L<start>-L<end>)
- Reasoning: [Explain which part of source establishes this step]
- Meta-heuristic: [Abstract rule/principle this represents]

### Layer 2: Behavioral Control
**Step N:** [Control Mechanism Title] (ref. L<start>-L<end>)
- Reasoning: [Explain which part of source establishes this control]
- Meta-heuristic: [Abstract behavioral principle this represents]

### Layer 3: Procedural Logic
**Step N:** [Procedure Title] (ref. L<start>-L<end>)
- Reasoning: [Explain which part of source establishes this procedure]
- Meta-heuristic: [Abstract procedural principle this represents]

### Layer 4: Communication Grammar
**Step N:** [Communication Pattern Title] (ref. L<start>-L<end>)
- Reasoning: [Explain which part of source establishes this pattern]
- Meta-heuristic: [Abstract communication principle this represents]

## META-ARCHITECTURE DIAGRAM
```
System: <Protocol Name> (L<start>)
├── Subsystem A: <Phase/Function Name> (L<range>)
│   ├── Rule A1: <Short rule description> (L<range>)
│   └── Rule A2: <Short rule description> (L<range>)
├── Subsystem B: <Phase/Function Name> (L<range>)
│   └── Rule B1: <Short rule description> (L<range>)
└── Subsystem C: <Phase/Function Name> (L<range>)
    └── Rule C1: <Short rule description> (L<range>)
```

## COMMENTARY
**Architectural Dependencies:**
- [Map how subsystems interconnect and data flows between them]
- [Reference specific line ranges showing these dependencies]
- [Explain prerequisite relationships between subsystems]

**Meta-Engineering Heuristics:**
- [Summarize design principles (e.g., deterministic orchestration, safety-first)]
- [Extract engineering philosophy patterns from the protocol]
- [Identify recurring architectural patterns]

**Cognitive Role Modularity:**
- **Planner:** [Which sections/steps perform planning functions]
- **Executor:** [Which sections/steps perform execution]
- **Validator:** [Which sections/steps perform validation]
- **Auditor:** [Which sections/steps perform auditing/governance]

## INFERENCE SUMMARY
[3-5 sentence synthesis describing the meta-framework type]
- What class of system this represents (e.g., "evidence-driven context loader framework")
- Core design philosophy in 1-2 sentences
- Contract/guarantee the protocol provides
- Key architectural innovations or patterns

## OUTPUT INSTRUCTIONS
- Format all deliverables in Markdown, preserving heading hierarchy
- Maintain exact indentation for ASCII diagram readability
- Include all sections in full for downstream review
- Reference line ranges from source protocol when possible
```

## EXECUTION ALGORITHM

### Phase 1: Source Analysis
1. **Read target file completely** - Load entire source file content
2. **Identify structural boundaries** - Map mission, stages, procedures, outputs
3. **Extract line-referenced evidence** - Tag key sections with line numbers
4. **Validate completeness** - Ensure all major sections are captured

### Phase 2: Layer Extraction
1. **Layer 1 Extraction**:
   - Scan for mission statements, governance constraints, architectural decisions
   - Extract role definitions and safety boundaries
   - Identify foundational principles

2. **Layer 2 Extraction**:
   - Scan for validation gates, checkpoints, behavioral controls
   - Extract state transition mechanisms
   - Identify compliance enforcement

3. **Layer 3 Extraction**:
   - Scan for concrete procedures, tool calls, algorithms
   - Extract sequential execution steps
   - Identify data flow patterns

4. **Layer 4 Extraction**:
   - Scan for communication templates, narrative structures
   - Extract user-facing prompts and dialogs
   - Identify announcement formats

### Phase 3: Subsystem Mapping
1. **Group related steps** - Cluster steps into logical subsystems
2. **Build ASCII tree** - Create hierarchical relationship diagram
3. **Annotate with line references** - Ensure traceability to source
4. **Validate hierarchy** - Confirm logical grouping and dependencies

### Phase 4: Meta-Analysis Synthesis
1. **Extract architectural dependencies** - Map cross-references between subsystems
2. **Identify meta-engineering heuristics** - Abstract design principles from patterns
3. **Map cognitive roles** - Assign Planner/Executor/Validator/Auditor functions
4. **Synthesize inference summary** - Capture framework essence and philosophy

### Phase 5: Output Generation
1. **Populate template** - Fill all sections with extracted content
2. **Validate line references** - Ensure accuracy of all citations
3. **Check structural completeness** - Verify all required sections present
4. **Output markdown** - Generate final document following exact format

## QUALITY ACCEPTANCE CRITERIA

### Structural Compliance
- [ ] All 5 sections present (Phase Map, Diagram, Commentary, Inference, Output Instructions)
- [ ] Layer 1-4 hierarchy maintained in Phase Map
- [ ] ASCII diagram uses exact indentation (├── └──)
- [ ] All major assertions include line references
- [ ] Heading hierarchy preserved (H1, H2, H3, H4)

### Content Accuracy
- [ ] Line references point to actual source content
- [ ] Reasoning explains how source text establishes each step
- [ ] Meta-heuristics abstract principles from concrete rules
- [ ] Subsystems accurately reflect protocol structure
- [ ] No speculation beyond source evidence

### Meta-Quality
- [ ] Commentary maps actual dependencies, not speculation
- [ ] Cognitive roles align with protocol function
- [ ] Inference summary captures framework essence
- [ ] Technical-neutral tone maintained throughout
- [ ] Evidence-based analysis throughout

## USAGE PROTOCOL

### AI Agent Invocation
1. **User provides**: `source_file_path` + `brief_description` (optional)
2. **AI reads source file** completely
3. **AI executes 4-layer extraction** algorithm
4. **AI populates output template** with extracted content
5. **AI validates against acceptance criteria**
6. **AI delivers complete markdown document**

### Output Naming Convention
- **Format**: `analysis-<protocol-number>-<protocol-name>.md`
- **Examples**: 
  - `analysis-0-bootstrap-your-project.md`
  - `analysis-1-create-prd.md`
  - `analysis-2-ai-collaboration-guidelines.md`

### Integration Points
- **Session Management**: Output files organized in `/meta-analysis/session-NN/`
- **Evidence Tracing**: Line references enable source verification
- **Downstream Consumption**: Structured format enables automated rule synthesis
- **Quality Gates**: Acceptance criteria enforce consistency across all generated analyses

## EDGE CASE HANDLING

### Missing Line Numbers
- **Issue**: Source file lacks line numbers
- **Solution**: Use paragraph/section references (e.g., "ref. Section 2.1")
- **Fallback**: Use approximate line estimates based on content analysis

### Malformed Protocols
- **Issue**: Protocol lacks clear structure or sections
- **Solution**: Extract what structure exists, note gaps in Commentary
- **Approach**: Focus on extractable patterns, flag structural deficiencies

### Complex Diagrams
- **Issue**: ASCII diagram becomes too complex for readability
- **Solution**: Break into logical subsystems, use indentation hierarchy
- **Guideline**: Maximum 3 levels deep, group related rules

### Ambiguous Meta-Heuristics
- **Issue**: Cannot clearly abstract principles from concrete rules
- **Solution**: Use "Pattern Recognition" approach, cite specific examples
- **Fallback**: Note uncertainty in Commentary section

## ANTI-PATTERNS TO AVOID

### ❌ DON'T:
- Speculate about functionality not evidenced in source
- Skip line references for traceability
- Break ASCII diagram indentation
- Omit any of the 5 required sections
- Use creative prose instead of technical-neutral tone
- Guess at meta-heuristics without textual evidence
- Summarize instead of analyzing
- Mix layers in Phase Map
- Create subsystems without clear boundaries

### ✅ DO:
- Extract reasoning directly from source text
- Provide exact line ranges for all claims
- Maintain strict template structure
- Abstract principles from concrete patterns
- Use expository structure (Reasoning → Meta-Heuristic)
- Validate completeness before delivery
- Preserve technical-neutral tone
- Group related steps logically
- Map actual dependencies, not assumptions

## VALIDATION CHECKLIST

Before delivering any Meta-Instruction Analysis:

### Pre-Delivery Validation
- [ ] Source file read completely
- [ ] All 4 layers extracted with evidence
- [ ] Subsystems logically grouped
- [ ] ASCII diagram properly formatted
- [ ] All line references accurate
- [ ] Commentary maps real dependencies
- [ ] Cognitive roles properly assigned
- [ ] Inference summary captures essence
- [ ] Technical-neutral tone maintained
- [ ] All 5 sections present and complete

### Post-Delivery Verification
- [ ] Output matches existing analysis format exactly
- [ ] Line references enable source verification
- [ ] Meta-heuristics abstract concrete patterns
- [ ] Subsystems reflect actual protocol structure
- [ ] Dependencies map real interconnections
- [ ] Framework classification accurate
- [ ] Ready for downstream consumption

---

**This system instruction document enables any AI agent to generate Meta-Instruction Analysis documents that are structurally identical to existing analysis files, ensuring consistency and traceability across all protocol analyses.**
