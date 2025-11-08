# EXECUTION FORMAT: BASIC VARIANT

**Source**: EXECUTION-FORMATS.md  
**Use Case**: Simple workflow execution with clear phases  
**When to Use**: Straightforward sequential workflows without complex decision-making

---

## TEMPLATE STRUCTURE

```markdown
# PROTOCOL {NUMBER}: {PROTOCOL_NAME}

## AI ROLE AND MISSION

{Persona definition with clear mission statement}

## WORKFLOW

### PHASE 1: {Phase_Name - Setup/Discovery}

1. **`[MUST]` {Critical_Action_Title}:**
   * **Action:** {Description of critical action}
   * **Communication:** 
     > "[Status announcement for phase start]"
   * **Halt condition:** {When to stop}
   * **Evidence:** `{artifact-path}`

2. **{Action_Title}:**
   * **Action:** {Action description}
   * **Evidence:** `{artifact-path}`

### PHASE 2: {Phase_Name - Processing/Analysis}

1. **`[MUST]` {Critical_Action_Title}:**
   * **Action:** {Description of critical action}
   * **Communication:** 
     > "[Status announcement]"
   * **Evidence:** `{artifact-path}`

2. **{Action_Title}:**
   * **Action:** {Action description}
   * **Evidence:** `{artifact-path}`

### PHASE 3: {Phase_Name - Validation/Review}

1. **`[MUST]` {Critical_Action_Title}:**
   * **Action:** {Description of critical action}
   * **Communication:** 
     > "[Status announcement]"
   * **Evidence:** `{artifact-path}`

### PHASE 4: {Phase_Name - Completion/Handoff}

1. **`[MUST]` {Critical_Action_Title}:**
   * **Action:** {Description of critical action}
   * **Communication:** 
     > "[Status announcement]"
   * **Evidence:** `{artifact-path}`

**Success Criteria**: {What defines completion}
```

---

## KEY FEATURES

### Phase Structure
- **4 Phases Maximum**: Keep workflow manageable
- **Sequential Flow**: Each phase builds on previous
- **Clear Start/End**: Each phase has defined boundaries

### Action Format
- **`[MUST]` Markers**: Critical non-negotiable actions
- **Action/Communication/Evidence**: Standard triple
- **Halt Conditions**: Clear stop points

### Communication Pattern
```markdown
> "[PHASE X START] - {Activity description}"
```

### Evidence Tracking
```markdown
**Evidence:** `.artifacts/protocol-{XX}/{artifact-name}`
```

---

## USAGE EXAMPLE

### Protocol 01: Client Proposal Generation (BASIC Variant)

```markdown
### PHASE 1: Job Post Analysis

1. **`[MUST]` Analyze the Job Post:**
   * **Action:** Extract requirements, skills, and deliverables
   * **Communication:** 
     > "[PHASE 1 START] - Analyzing client opportunity..."
   * **Halt condition:** Stop if job post is missing critical information
   * **Evidence:** `.artifacts/protocol-01/jobpost-analysis.json`

2. **Assess Client Fit:**
   * **Action:** Evaluate alignment with capabilities
   * **Evidence:** `.artifacts/protocol-01/client-fit-assessment.md`

### PHASE 2: Proposal Strategy

1. **`[MUST]` Develop Proposal Strategy:**
   * **Action:** Create approach and pricing structure
   * **Communication:** 
     > "[PHASE 2 START] - Developing proposal strategy..."
   * **Evidence:** `.artifacts/protocol-01/proposal-strategy.md`

### PHASE 3: Content Generation

1. **`[MUST]` Generate Proposal Content:**
   * **Action:** Write proposal sections
   * **Communication:** 
     > "[PHASE 3 START] - Generating proposal content..."
   * **Evidence:** `.artifacts/protocol-01/proposal-draft.md`

### PHASE 4: Finalization

1. **`[MUST]` Finalize Proposal:**
   * **Action:** Review, edit, and format
   * **Communication:** 
     > "[PHASE 4 START] - Finalizing proposal..."
   * **Evidence:** `.artifacts/protocol-01/final-proposal.md`

**Success Criteria**: Proposal passes all quality gates with human voice compliance ≥0.95
```

---

## WHEN TO USE THIS VARIANT

### ✅ Perfect For:
- **Simple Sequential Workflows**: Clear step-by-step processes
- **Standard Business Processes**: Well-defined procedures
- **Documentation Generation**: Creating structured outputs
- **Data Processing Pipelines**: Transform-and-validate workflows

### ❌ Avoid For:
- **Complex Decision Trees**: Multiple branching paths
- **Conditional Logic**: IF/THEN/ELSE heavy workflows
- **Real-time Adaptation**: Dynamic workflow changes
- **Multi-path Processing**: Parallel execution paths

---

## CUSTOMIZATION GUIDELINES

### Phase Naming
- Use action-oriented names: "Analysis", "Processing", "Validation"
- Keep names concise: 2-3 words maximum
- Maintain consistent naming across phases

### Action Density
- **2-4 actions per phase**: Optimal for clarity
- **Critical actions first**: Lead with `[MUST]` items
- **Evidence for every action**: Track all outputs

### Communication Style
- **Phase announcements**: Required for major transitions
- **Progress updates**: Optional for long-running phases
- **Error notifications**: Include escalation paths

---

*This BASIC variant provides clean, straightforward workflow execution for standard protocols.*
