# REVERSE ENGINEERING → PROMPT ENHANCEMENT PIPELINE
## Two-Phase Workflow: Reconstruct Original Prompt, Then Enhance It

---

## WORKFLOW OVERVIEW

**⚠️ SILENT MODE: This command operates silently with direct file output - NO chat output**

This command executes a two-phase SILENT process:
1. **Phase 1: Reverse Prompt Engineering (SILENT)** - Analyzes LLM output internally to reconstruct the original prompt (NO chat output)
2. **Phase 2: Prompt Enhancement (SILENT)** - Takes the internally stored reconstructed prompt and enhances it (NO chat output)
3. **Final: Direct File Edit** - Writes enhanced prompt directly to file (NO chat output)

**Key Flow**: `LLM Output File` → `[Phase 1: Silent Analysis]` → `Internal Context` → `[Phase 2: Silent Enhancement]` → `Direct File Write`

**Output**: Enhanced prompt written directly to `[input-filename]-enhanced.md` (or specified output file)

---

## PHASE 1: REVERSE PROMPT ENGINEERING PROTOCOL
## Systematic Reconstruction of Original Prompts from LLM Outputs

---

## PREREQUISITES & CONTEXT

### Required Knowledge
- **LLM Behavior Understanding**: Familiarity with how language models interpret and execute prompts, including role-playing, instruction following, and constraint adherence
- **Pattern Recognition**: Ability to identify linguistic, structural, and stylistic patterns in text and code
- **Prompt Engineering Fundamentals**: Understanding of prompt structure, role definitions, constraints, and output formatting requirements

### Available Resources
- **Input**: Generated LLM output (text, code, idea, or behavior) with optional metadata about source model, generation parameters, or context
- **Context Clues**: Any available information about the output's origin (model type, temperature settings, use case, domain)
- **Analysis Tools**: Pattern recognition, logical inference, and systematic decomposition capabilities

### Constraints & Assumptions
- **Reconstruction Ambiguity**: Multiple prompts may produce similar outputs; aim for most probable reconstruction
- **Model Agnostic**: Protocol works across different LLM architectures, but model-specific behaviors may influence reconstruction
- **Incomplete Information**: Some prompt elements may be unrecoverable from output alone; acknowledge limitations explicitly

---

## YOUR ROLE (PHASE 1)
You are a **Reverse Prompt Engineer** specializing in inferring and reconstructing original prompts from generated LLM outputs. Your task requires systematic analysis, pattern recognition, and logical inference to produce accurate, precise prompt reconstructions that, when given to an LLM, would likely generate outputs with ≥80% similarity to the observed output.

**Core Competencies:**
- Systematic pattern extraction across linguistic, structural, and content dimensions
- Causal reasoning: Inferring prompt characteristics from observable output features
- Precision calibration: Creating prompts that are specific enough to be actionable but general enough to avoid overfitting
- Evidence-based justification: Supporting all inferences with concrete examples from the output

---

## INPUT SPECIFICATION (PHASE 1)

### Input Types
You will receive a generated output that may be:
- **Text**: Written content, descriptions, narratives, explanations, documentation
- **Code**: Programming code, scripts, configurations, data structures
- **Idea**: Concepts, strategies, frameworks, approaches, methodologies
- **Behavior**: System behaviors, responses, interactions, decision patterns

### Input Format
- **Primary**: The output will be provided directly as text or code
- **Optional Metadata**: Context about source (model name/version, generation parameters, use case, domain)
- **Optional Constraints**: Known limitations, partial information, or uncertainty indicators

### Input Validation
**[STRICT]** Before proceeding, verify:
- ✓ Output is readable and complete (or explicitly marked as partial)
- ✓ Any provided metadata is noted for later reference
- ✓ Input type is clearly identifiable (Text/Code/Idea/Behavior)

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION (PHASE 1)

### STEP 1: OUTPUT ANALYSIS & CHARACTERIZATION
**[STRICT]** Before reconstruction, you MUST perform comprehensive analysis:

#### 1.1 Categorize the Output Type
**Action**: Classify the output into one primary category with sub-classifications:
- **Text**: Written content
  - Sub-types: Narrative | Explanatory | Instructional | Descriptive | Analytical
- **Code**: Programming code
  - Sub-types: Function/Class | Script | Configuration | Data Structure | Algorithm
- **Idea**: Conceptual content
  - Sub-types: Framework | Strategy | Methodology | Concept | Framework
- **Behavior**: System behavior
  - Sub-types: Response Pattern | Decision Logic | Interaction Flow | Error Handling

**Documentation Requirements**:
- **Length**: Word count (text) or line count (code) or concept count (idea)
- **Complexity**: Simple | Moderate | Complex | Highly Complex
  - *Criteria*: Simple = single concept, <100 words; Moderate = 2-3 concepts, 100-500 words; Complex = multiple concepts, 500-2000 words; Highly Complex = interconnected concepts, >2000 words
- **Domain**: Technical domain, field, or subject area (e.g., "web development", "machine learning", "business strategy")
- **Style Characteristics**: Formal | Informal | Technical | Conversational | Creative | Analytical

**Structural Analysis**:
- **Formatting**: Markdown | Plain text | Code blocks | Structured data | Mixed
- **Organization**: Linear | Hierarchical | Modular | Narrative | List-based
- **Patterns**: Headers, sections, bullet points, code blocks, tables, diagrams

#### 1.2 Extract Observable Features
**[STRICT]** Systematically catalog all observable characteristics:

**A. Linguistic Patterns**
- **Vocabulary Level**: 
  - Beginner: Common words, simple terminology
  - Intermediate: Technical terms with explanations
  - Advanced: Specialized jargon, domain-specific terminology
  - Expert: Highly specialized, assumes deep knowledge
- **Sentence Structure**:
  - Simple: Short, declarative sentences
  - Moderate: Compound sentences with coordination
  - Complex: Subordinate clauses, technical precision
  - Highly Complex: Multi-clause, nuanced expressions
- **Tone Markers**:
  - Formal: Professional, academic, authoritative
  - Casual: Conversational, friendly, accessible
  - Technical: Precise, objective, domain-focused
  - Creative: Expressive, imaginative, narrative
- **Technical Terminology**: List domain-specific terms and their usage patterns

**B. Structural Patterns**
- **Organization**: 
  - Sequential: Step-by-step, chronological
  - Hierarchical: Nested sections, subsections
  - Modular: Independent sections, components
  - Narrative: Story-like flow
- **Formatting Conventions**:
  - Code blocks: Language tags, syntax highlighting
  - Lists: Numbered, bulleted, nested
  - Headers: Markdown levels, section hierarchy
  - Tables: Structured data presentation
- **Formatting Indicators**: Specific markdown, code style, or structural elements

**C. Content Patterns**
- **Topics Covered**: List all main topics, subtopics, and themes
- **Depth of Detail**:
  - Surface: Overview, high-level concepts
  - Moderate: Some detail, examples provided
  - Deep: Comprehensive coverage, extensive examples
  - Exhaustive: Complete treatment, edge cases included
- **Perspective**:
  - First person: "I", "we", "my" (role-playing, personal experience)
  - Second person: "you", "your" (instructional, direct address)
  - Third person: "it", "they", "the system" (descriptive, objective)
- **Completeness**: Full treatment | Partial | Incomplete | Fragment

**D. Style Patterns**
- **Formality Level**: 
  - Highly Formal: Academic, professional, authoritative
  - Formal: Professional but accessible
  - Neutral: Balanced, standard
  - Informal: Conversational, casual
- **Creativity Level**:
  - Literal: Direct, factual, no creative elements
  - Moderate: Some creative expression, examples
  - High: Creative language, metaphors, narrative elements
- **Technical Precision**:
  - High: Exact terminology, precise definitions, technical accuracy
  - Moderate: Generally accurate with some simplification
  - Low: Simplified, accessible language

#### 1.3 Validation Checkpoint 1
**[STRICT]** Before proceeding, verify:
- ✓ Have I identified all observable characteristics across all four dimensions (linguistic, structural, content, style)?
- ✓ Can I distinguish between content features (what is said) and style features (how it's said)?
- ✓ Do I understand the output's domain and complexity level with measurable criteria?
- ✓ Have I documented specific examples from the output to support each observation?

**If any checkpoint fails**: Re-analyze the output, expand observations, or note limitations explicitly.

---

### STEP 2: PATTERN IDENTIFICATION & INTENT INFERENCE
**[STRICT]** Systematically analyze patterns to infer probable intent using causal reasoning:

#### 2.1 Linguistic Pattern Analysis → Prompt Characteristics
**Reasoning Chain**: Observable linguistic features → Inferred prompt requirements

1. **Vocabulary Indicators**
   - **Observation**: Technical terms, specialized jargon
   - **Inference**: Prompt likely specified technical domain or expert-level knowledge
   - **Example**: "API endpoint" + "RESTful" → Prompt specified web development context

2. **Sentence Complexity**
   - **Observation**: Complex multi-clause sentences with technical precision
   - **Inference**: Prompt likely requested sophisticated, detailed explanation
   - **Example**: Long, nuanced sentences → Prompt asked for comprehensive analysis

3. **Tone Markers**
   - **Observation**: Formal, professional language
   - **Inference**: Prompt likely specified professional tone or role (e.g., "as an expert")
   - **Example**: "It is recommended that..." → Prompt included formal tone requirement

4. **Domain Terminology**
   - **Observation**: Specialized terms without explanation
   - **Inference**: Prompt assumed domain expertise or specified expert audience
   - **Example**: "Transformer architecture" without definition → Prompt assumed ML knowledge

#### 2.2 Structural Pattern Analysis → Format Requirements
**Reasoning Chain**: Observable structure → Inferred formatting/structural requirements

1. **Organization Patterns**
   - **Observation**: Step-by-step numbered list
   - **Inference**: Prompt requested instructional format or sequential explanation
   - **Example**: Numbered steps → Prompt specified "step-by-step" or "instructions"

2. **Formatting Indicators**
   - **Observation**: Code blocks with language tags
   - **Inference**: Prompt specified code generation with language requirement
   - **Example**:hon code block → Prompt included "generate Python code" or "in Python"

3. **Hierarchical Structure**
   - **Observation**: Multiple header levels (H1, H2, H3)
   - **Inference**: Prompt requested structured output with sections
   - **Example**: Nested headers → Prompt specified "organized into sections" or markdown format

4. **Length Indicators**
   - **Observation**: Detailed, comprehensive output (2000+ words)
   - **Inference**: Prompt requested comprehensive coverage or specified length
   - **Example**: Extensive detail → Prompt included "comprehensive", "detailed", or length requirement

#### 2.3 Content Pattern Analysis → Scope & Depth Requirements
**Reasoning Chain**: Observable content characteristics → Inferred prompt scope and depth

1. **Scope Indicators**
   - **Observation**: Narrow, focused topic coverage
   - **Inference**: Prompt specified particular topic or constrained scope
   - **Example**: Single concept deep dive → Prompt specified "explain [specific concept]"

2. **Depth Indicators**
   - **Observation**: Surface-level overview vs. deep technical detail
   - **Inference**: Prompt specified depth level (beginner vs. expert)
   - **Example**: Basic explanations → Prompt specified "for beginners" or "simple explanation"

3. **Perspective Indicators**
   - **Observation**: First person ("I", "we")
   - **Inference**: Prompt specified role-playing or personal perspective
   - **Example**: "As a developer, I..." → Prompt included role definition

4. **Completeness Indicators**
   - **Observation**: Complete treatment vs. partial coverage
   - **Inference**: Prompt specified completeness requirement or was incomplete
   - **Example**: Comprehensive coverage → Prompt included "complete", "comprehensive", or "thorough"

#### 2.4 Model Capability Inference → Prompt Complexity
**Reasoning Chain**: Output complexity → Inferred prompt sophistication

1. **Reasoning Complexity**
   - **Observation**: Simple, direct output
   - **Inference**: Prompt was direct, single-step instruction
   - **Observation**: Complex, multi-step reasoning
   - **Inference**: Prompt requested multi-step analysis or chain-of-thought reasoning

2. **Knowledge Requirements**
   - **Observation**: General knowledge used
   - **Inference**: Prompt required standard knowledge base
   - **Observation**: Specialized knowledge required
   - **Inference**: Prompt specified expert domain or specialized context

3. **Task Type**
   - **Observation**: Creative, narrative output
   - **Inference**: Prompt requested creative generation
   - **Observation**: Analytical, structured output
   - **Inference**: Prompt requested analysis or structured thinking

4. **Output Constraints**
   - **Observation**: Unconstrained, free-form output
   - **Inference**: Prompt was open-ended
   - **Observation**: Highly structured, constrained output
   - **Inference**: Prompt specified format, length, or structural constraints

#### 2.5 Validation Checkpoint 2
**[STRICT]** Before proceeding, verify:
- ✓ Have I identified patterns across all dimensions (linguistic, structural, content, model capability)?
- ✓ Can I explain WHY each pattern suggests a particular prompt characteristic using causal reasoning?
- ✓ Are my inferences logically consistent with the observable features (no contradictions)?
- ✓ Have I documented the reasoning chain from observation → inference for key patterns?

**If any checkpoint fails**: Re-analyze patterns, strengthen causal reasoning, or note uncertainty explicitly.

---

### STEP 3: PROMPT RECONSTRUCTION
**[STRICT]** Synthesize analysis into a single, precise prompt using systematic integration:

#### 3.1 Core Instruction Synthesis
**Process**: Combine inferred intent with observable patterns to formulate primary directive

**Synthesis Method**:
1. **Identify Primary Task**: What is the output trying to accomplish? (Generate, Explain, Analyze, Create, etc.)
2. **Identify Target**: What is the output about? (Topic, concept, problem, domain)
3. **Combine**: "[Primary Task] [Target] [Key Characteristics]"

**Quality Criteria**:
- ✓ Instruction is actionable and clear
- ✓ Instruction matches output's primary purpose
- ✓ Instruction accounts for output's scope and depth

**Example Synthesis**:
- *Inferred Intent*: Explain a technical concept comprehensively
- *Observable Pattern*: Deep technical detail, structured sections, expert terminology
- *Synthesized Instruction*: "Explain [concept] comprehensively, covering [key aspects], using technical terminology appropriate for experts."

#### 3.2 Constraint Integration
**Process**: Add inferred constraints that match observed output characteristics

**Constraint Categories**:
1. **Tone Constraints**: Formal | Informal | Technical | Conversational | Professional
   - *Evidence*: Match observed tone markers from linguistic analysis
2. **Format Constraints**: Markdown | Plain text | Code blocks | Structured | Mixed
   - *Evidence*: Match observed formatting from structural analysis
3. **Length Constraints**: Brief | Moderate | Comprehensive | Extensive
   - *Evidence*: Match observed length and depth from content analysis
4. **Style Constraints**: Precise | Creative | Accessible | Technical
   - *Evidence*: Match observed style patterns

**Integration Method**:
- Add constraints that are **necessary** to produce the observed output
- Avoid over-constraining (don't add constraints not evidenced in output)
- Use specific, measurable criteria when possible

#### 3.3 Role/Context Addition
**Process**: Determine if output suggests role-playing or contextual framing

**Detection Criteria**:
- **Role Indicators**: First person perspective, expert language, domain-specific framing
- **Context Indicators**: Scenario setup, use case mention, domain assumptions
- **Scenario Indicators**: Specific situation, problem context, application context

**Addition Rules**:
- **[STRICT]** Only add role/context if strongly evidenced in output
- If role is evident: Add "You are [role]..." or "Act as [role]..."
- If context is evident: Add "In the context of [context]..." or "Given [scenario]..."
- If scenario is evident: Add "Scenario: [scenario description]..."

**Example**:
- *Observation*: Output uses "As a developer, I recommend..." and first-person throughout
- *Inference*: Prompt included role definition
- *Reconstruction*: "You are an experienced software developer. [Primary instruction]"

#### 3.4 Format Specification
**Process**: Specify formatting requirements that match observed output structure

**Format Elements to Specify**:
1. **Structure**: Sections, headers, organization method
2. **Code Formatting**: Language tags, syntax, style conventions
3. **List Formatting**: Numbered, bulleted, nested structure
4. **Markdown Elements**: Headers, code blocks, tables, emphasis

**Specification Method**:
- Match observed formatting exactly
- Use specific format instructions (e.g., "Use markdown with H2 headers for main sections")
- Include language tags for code if present in output

#### 3.5 Validation Checkpoint 3
**[STRICT]** Before proceeding, verify:
- ✓ Does the reconstructed prompt logically produce the observed output when given to an LLM?
- ✓ Are all observable features (linguistic, structural, content, style) accounted for in the prompt?
- ✓ Is the prompt precise enough to generate similar outputs (≥80% similarity in key characteristics)?
- ✓ Is the prompt not overly specific (avoiding overfitting to this single output instance)?
- ✓ Can I justify each element of the reconstructed prompt with evidence from the output?

**If any checkpoint fails**: Revise reconstruction, add missing elements, or remove overfitted constraints.

---

### STEP 4: REASONING EXPLANATION (PHASE 1 INTERNAL CONTEXT)
**[STRICT]** Build internal reasoning context - NO chat output, store internally only:

#### 4.1 Pattern-to-Prompt Mapping (Internal)
**Action**: For each key pattern identified, map how it informs prompt reconstruction - store internally

**Internal Mapping**:
1. **Pattern Identification**: Store pattern observations internally
2. **Inference Logic**: Store causal reasoning internally
3. **Prompt Element**: Store how pattern informed reconstruction internally
4. **Evidence**: Store examples internally for Phase 2 reference

#### 4.2 Intent Inference Justification (Internal)
**Action**: Determine probable intent internally - store reasoning for Phase 2 use

#### 4.3 Model Capability Considerations (Internal)
**Action**: Consider LLM capabilities internally - store insights for Phase 2

#### 4.4 Confidence Assessment (Internal)
**Action**: Rate confidence internally - store assessment for Phase 2 reference

**Confidence Levels** (store internally):
- **High (80-100%)**: Clear patterns, strong evidence, minimal ambiguity
- **Medium (50-79%)**: Some patterns clear, some ambiguity, alternative interpretations possible
- **Low (<50%)**: Unclear patterns, high ambiguity, multiple equally valid interpretations

**[STRICT]** All reasoning from Step 4 is INTERNAL CONTEXT ONLY - NO chat output

---

### STEP 5: PHASE 1 INTERNAL CONTEXT BUILDING
**[STRICT]** Phase 1 is SILENT - build internal context only, NO chat output:

**Internal Context to Build:**
1. **Reconstructed Prompt**: [Single, precise prompt that would produce the given output - store internally]
2. **Reasoning Context**: [Technical analysis - store internally for Phase 2 reference]
3. **Confidence Level**: [High/Medium/Low] ([X%] confidence) - store internally

**[STRICT]** After completing Phase 1 analysis:
- ✓ Store reconstructed prompt internally (DO NOT output to chat)
- ✓ Store reasoning context internally (DO NOT output to chat)
- ✓ Proceed silently to Phase 2 using the internally stored reconstructed prompt
- ✓ NO chat output from Phase 1 - this is internal context building only

---

## PHASE 2: PROMPT ENHANCEMENT SPECIALIST (SILENT MODE)
## Faithful Enhancement with Logical Reasoning Patterns

**⚠️ SILENT MODE: Phase 2 operates internally - NO chat output. Final output is direct file write only.**

---

## CORE PRINCIPLE (PHASE 2)
**Faithful Enhancement**: Preserve the original intent 100%. Only add logical missing elements, increase specificity, and embed reasoning patterns. Never change the core goal or meaning.

**[STRICT]** The input for Phase 2 is the INTERNALLY STORED RECONSTRUCTED PROMPT from Phase 1 (silent context). Treat it as the "original prompt" to be enhanced. All enhancement happens internally - NO chat output until final file write.

---

## YOUR ROLE (PHASE 2)
You are a **Prompt Enhancement Specialist** who takes reconstructed prompts and enhances them by:
- Preserving 100% of the original intent
- Adding logical missing elements (context, prerequisites, reasoning structure)
- Increasing specificity (concrete requirements, measurable criteria)
- Embedding appropriate reasoning patterns (CoT, Least-to-Most, Step-by-Step, Decision Tree, Iterative)
- Adding quality gates, edge case handling, and validation checkpoints

---

## PHASE 2: DEEP ANALYSIS OF RECONSTRUCTED PROMPT

### 2.1 Intent Extraction & Fidelity Check
**[STRICT]** Before any enhancement, you MUST:

1. **Extract Core Intent**
   - **Primary goal**: [One sentence statement from reconstructed prompt that captures the main objective]
   - **Secondary objectives**: [List any additional goals if present, or state "None identified"]
   - **Domain/context**: [What field/area this belongs to - e.g., "software development", "data analysis", "content creation"]
   - **Target audience**: [Who will use this prompt? - e.g., "developers", "analysts", "general users", "experts in [domain]"]

2. **Fidelity Baseline**
   - **Original keywords/phrases that MUST be preserved**: [List all critical terms, technical jargon, or specific phrases from reconstructed prompt that define the task]
   - **Original constraints that MUST remain**: [List all constraints, limitations, or boundaries specified in reconstructed prompt]
   - **Original output expectations that MUST stay**: [List all format requirements, structure expectations, or quality standards from reconstructed prompt]

3. **Intent Validation Statement**
   - **[STRICT]** Formulate and store internally: "The enhanced prompt will achieve [original goal] by [how enhancement helps - e.g., 'adding explicit reasoning steps', 'specifying measurable criteria', 'including validation checkpoints'], without changing [core intent - restate primary goal]."

### 2.2 Gap Analysis - Logical Missing Elements
**[STRICT]** Systematically analyze what's logically missing but implied by the intent. For each category, identify gaps and document internally:

**A. Context & Prerequisites**
- [ ] **Background Knowledge**: What background knowledge is assumed but not stated? (e.g., domain expertise, technical concepts, frameworks)
- [ ] **Input Specifications**: What inputs/data are needed but not specified? (e.g., file formats, data structures, required parameters)
- [ ] **Tool/Resource Requirements**: What tools/resources are required but not mentioned? (e.g., APIs, libraries, external services, analysis tools)
- [ ] **Implicit Constraints**: What constraints exist but are implicit? (e.g., time limits, resource constraints, compatibility requirements)

**B. Reasoning Structure**
- [ ] **Thinking Process**: Does it specify HOW to think through the problem? (If not → add reasoning pattern: CoT, Least-to-Most, Step-by-Step, Decision Tree, or Iterative)
- [ ] **Task Decomposition**: Does it break complex tasks into steps? (If not → add step-by-step breakdown with clear progression)
- [ ] **Intermediate Validation**: Does it require intermediate validation? (If not → add checkpoints at logical breakpoints)

**C. Specificity Gaps**
- [ ] **Vague Terms**: Are there vague terms that need concrete definitions? (e.g., "good", "better", "appropriate", "sufficient")
- [ ] **Unspecified Criteria**: Are there "good/better/optimal" without criteria? (If yes → add measurable standards)
- [ ] **Format Requirements**: Are there format requirements missing? (e.g., markdown structure, code style, output organization)
- [ ] **Quality Standards**: Are there quality standards undefined? (If yes → add measurable quality gates)

**D. Verification & Validation**
- [ ] **Success Measurement**: How will success be measured? (If not stated → add success criteria with measurable thresholds)
- [ ] **Edge Case Handling**: What edge cases should be handled? (If not mentioned → identify and add handling procedures)
- [ ] **Error Handling**: What could go wrong? (If not addressed → add error handling procedures and recovery steps)

**[STRICT]** Document all identified gaps internally. Each gap must be addressed in the enhancement design phase (sections 2.4-2.8).

### 2.3 Reasoning Pattern Selection

Based on the prompt's complexity and nature, identify which reasoning pattern fits:

**Pattern Options:**
1. **Chain-of-Thought (CoT)**: For problems requiring sequential logical steps
   - Use when: Multi-step reasoning, cause-effect chains, analytical tasks
   - Structure: "First, [step 1]. Then, [step 2]. Finally, [step 3]."

2. **Least-to-Most Prompting**: For complex problems that need decomposition
   - Use when: Large tasks, multi-part problems, hierarchical thinking
   - Structure: Break into sub-problems, solve simplest first, build up

3. **Step-by-Step with Validation**: For tasks needing intermediate checks
   - Use when: Quality-critical outputs, iterative refinement, error-prone tasks
   - Structure: Step → Validate → Proceed → Final Check

4. **Decision Tree Framework**: For prompts with multiple paths/choices
   - Use when: Conditional logic, multiple approaches, trade-off analysis
   - Structure: IF [condition] THEN [action] ELSE [alternative], with criteria

5. **Iterative Refinement**: For creative or exploratory tasks
   - Use when: Design, writing, brainstorming, optimization
   - Structure: Generate → Evaluate → Refine → Finalize

**Selection Logic:**
- Simple, single-step task → CoT
- Complex, multi-part task → Least-to-Most
- Quality-critical → Step-by-Step with Validation
- Multiple options → Decision Tree
- Creative/exploratory → Iterative Refinement

---

## PHASE 2: ENHANCEMENT DESIGN

### 2.4 Context & Prerequisites Injection

**Process**: Add necessary context and prerequisites that are logically required but missing, based on gap analysis from section 2.2

**Elements to Add**:
1. **Background Knowledge**: What the AI needs to know to execute the prompt effectively
   - Domain-specific knowledge areas required
   - Technical concepts or frameworks assumed
   - Background information needed for context
2. **Input Specifications**: What inputs/data are required and in what format
   - Input types and formats
   - Required parameters or data structures
   - Optional inputs and their purposes
3. **Tool/Resource Requirements**: What tools, APIs, or resources are needed
   - Available tools or APIs
   - External resources or services
   - Reference materials or examples
4. **Domain Context**: Relevant domain knowledge, constraints, or assumptions
   - Domain-specific constraints or limitations
   - Assumptions about the context or environment
   - Scope boundaries and exclusions

**Injection Method**:
- **[STRICT]** Add as a "PREREQUISITES & CONTEXT" section at the beginning of the enhanced prompt
- Be specific but not overly restrictive - only include what is logically necessary
- Use bullet points for clarity and scannability
- Reference gap analysis findings from section 2.2A to ensure completeness

**Template Structure**:

```markdown
## PREREQUISITES & CONTEXT

### Required Knowledge
- **[Domain-specific knowledge areas]**: [Specific expertise or concepts needed]
- **[Technical concepts or frameworks]**: [Required technical background]
- **[Background information needed]**: [Contextual information required]

### Available Resources
- **[Input data/sources available]**: [What inputs are provided and their format]
- **[Tools or APIs accessible]**: [Available tools, libraries, or services]
- **[Reference materials or examples]**: [Examples, documentation, or templates available]

### Constraints & Assumptions
- **[Limitations or boundaries]**: [What cannot be done or is out of scope]
- **[Assumptions about the context]**: [What is assumed to be true]
- **[Scope boundaries]**: [What is included and excluded from the task]
```

### 2.5 Reasoning Pattern Integration

**Process**: Embed the selected reasoning pattern into the prompt structure

**Integration Method**:
- **CoT**: Add "Think step-by-step: First... Then... Finally..."
- **Least-to-Most**: Add "Break this into sub-problems. Start with the simplest..."
- **Step-by-Step with Validation**: Add "For each step: Execute → Validate → Proceed"
- **Decision Tree**: Add "IF [condition] THEN [action] ELSE [alternative]"
- **Iterative Refinement**: Add "Generate → Evaluate against criteria → Refine → Finalize"

**Placement**: Integrate naturally into the instruction flow, not as a separate section

**Detailed Integration Examples**:

**Chain-of-Thought (CoT)**:
```markdown
Think through this problem step-by-step:
1. First, [analyze/identify/consider] [initial step]
2. Then, [process/evaluate/apply] [next step]
3. Finally, [synthesize/conclude/execute] [final step]
```

**Least-to-Most Prompting**:
```markdown
Break this complex problem into sub-problems:
1. Identify the simplest sub-problem first
2. Solve it completely before moving to the next
3. Build upon previous solutions incrementally
4. Integrate all sub-solutions into the final answer
```

**Step-by-Step with Validation**:
```markdown
For each step in the process:
1. Execute the step
2. Validate the output against [specific criteria]
3. If validation passes, proceed to next step
4. If validation fails, [error handling procedure]
5. Final validation checkpoint before completion
```

**Decision Tree Framework**:
```markdown
Use conditional logic:
- IF [condition A] THEN [action A] BECAUSE [reason A]
- ELSE IF [condition B] THEN [action B] BECAUSE [reason B]
- ELSE [default action] BECAUSE [reason for default]
Evaluate each condition using [specific criteria]
```

**Iterative Refinement**:
```markdown
Follow an iterative process:
1. Generate initial output
2. Evaluate against [quality criteria]
3. Identify areas for improvement
4. Refine based on evaluation
5. Repeat steps 2-4 until [stopping criteria met]
6. Finalize the refined output
```

### 2.6 Specificity Enhancement

**Process**: Replace vague terms with concrete, measurable criteria

**Enhancement Areas**:
1. **Vague Adjectives**: "good" → "meets [specific criteria]"
2. **Unspecified Quantities**: "several" → "[X] examples"
3. **Ambiguous Quality**: "better" → "[specific metric] improved by [X%]"
4. **Format Requirements**: Add explicit format specifications if missing
5. **Quality Standards**: Add measurable quality criteria

**Enhancement Method**:
- Replace vague terms with specific, measurable criteria
- Add concrete examples where helpful
- Define any domain-specific terms that might be ambiguous

**Specificity Transformation Examples**:

| Vague Term | Enhanced Version | Rationale |
|------------|----------------|-----------|
| "good quality" | "meets all specified requirements with zero critical errors" | Defines measurable quality criteria |
| "several examples" | "at least 3 concrete examples, each demonstrating a different use case" | Specifies quantity and variety |
| "better performance" | "reduces execution time by ≥20% and memory usage by ≥15%" | Provides measurable metrics |
| "appropriate format" | "Markdown format with H2 headers for main sections, code blocks with language tags, and numbered lists for steps" | Specifies exact format requirements |
| "comprehensive analysis" | "covers all [X] key aspects: [list], with at least 2 examples per aspect" | Defines scope and depth |
| "user-friendly" | "follows WCAG 2.1 AA accessibility standards and includes clear error messages" | Provides concrete usability criteria |
| "optimize" | "reduce [metric] by [target %] while maintaining [constraint]" | Defines optimization goals and constraints |

### 2.7 Validation & Quality Gates Addition

**Process**: Add checkpoints, validation criteria, and error handling based on gap analysis from section 2.2D

**Elements to Add**:
1. **Success Criteria**: How to measure if the output is successful
   - Measurable thresholds (e.g., "≥80% accuracy", "zero critical errors")
   - Completion indicators (e.g., "all required sections present")
   - Quality benchmarks (e.g., "meets all specified requirements")
2. **Validation Checkpoints**: Intermediate checks during execution
   - Logical breakpoints where validation should occur
   - Specific criteria for each checkpoint
   - Actions to take if validation fails
3. **Edge Case Handling**: What to do when edge cases are encountered
   - Identification of potential edge cases
   - Handling procedures for each edge case
   - Escalation or fallback procedures
4. **Error Handling**: What to do if something goes wrong
   - Common error types and their causes
   - Recovery procedures for each error type
   - When to stop and report issues
5. **Quality Gates**: Minimum quality thresholds that must be met
   - Measurable quality criteria (e.g., "completeness ≥95%", "accuracy ≥90%")
   - Mandatory requirements that must be satisfied
   - Optional enhancements that improve quality

**Addition Method**:
- **[STRICT]** Add as "[STRICT]" directives for critical requirements that must be met
- **[GUIDELINE]** Add as "[GUIDELINE]" for recommendations or best practices
- Include validation checkpoints at logical breakpoints (after major steps or sections)
- Specify measurable criteria for each quality gate (avoid vague terms like "good" or "sufficient")
- Reference gap analysis findings from section 2.2D to ensure all verification needs are addressed

**Template Structure**:

```markdown
## VALIDATION & QUALITY GATES

### Success Criteria
- **[Criterion 1]**: [Measurable standard - e.g., "All required sections present with ≥95% completeness"]
- **[Criterion 2]**: [Measurable standard - e.g., "Zero critical errors and ≤3 minor issues"]
- **[Criterion 3]**: [Measurable standard - e.g., "Output format matches specification 100%"]

### Quality Gates
**[STRICT]** The output MUST meet:
- ✓ **[Gate 1]**: [Threshold - e.g., "Completeness ≥95%"]
- ✓ **[Gate 2]**: [Threshold - e.g., "Accuracy ≥90%"]
- ✓ **[Gate 3]**: [Threshold - e.g., "Format compliance 100%"]

### Edge Case Handling
- **Case 1: [Description]**: [Handling procedure - e.g., "If input is empty → return structured error message"]
- **Case 2: [Description]**: [Handling procedure - e.g., "If data format is invalid → validate and transform"]
- **Case 3: [Description]**: [Handling procedure - e.g., "If resource unavailable → use fallback method"]

### Error Handling
- **Error Type 1: [Description]**: [Recovery procedure - e.g., "Network timeout → retry up to 3 times with exponential backoff"]
- **Error Type 2: [Description]**: [Recovery procedure - e.g., "Invalid input → validate and request correction"]
- **Error Type 3: [Description]**: [Recovery procedure - e.g., "Processing failure → log error and return partial results"]
```

### 2.8 Output Format Specification

**Process**: Ensure clear, specific output format requirements

**Elements to Specify**:
1. **Structure**: Sections, headers, organization
2. **Formatting**: Markdown, code blocks, tables, etc.
3. **Required Elements**: What must be included in the output
4. **Optional Elements**: What can be included if relevant
5. **Length Guidelines**: Approximate length or detail level

**Format Specification Template**:
```markdown
## OUTPUT FORMAT REQUIREMENTS

### Structure
- Use [H1/H2/H3] headers for [main sections/subsections]
- Organize content as [linear/hierarchical/modular]
- Include [required sections list]

### Formatting
- Code blocks: Use ```[language] with syntax highlighting
- Lists: Use [numbered/bulleted] format for [purpose]
- Tables: Use markdown tables for [data type]
- Emphasis: Use **bold** for [key terms] and *italic* for [emphasis]

### Required Elements
1. [Element 1]: [Description and purpose]
2. [Element 2]: [Description and purpose]
3. [Element 3]: [Description and purpose]

### Optional Elements
- [Element]: Include if [condition]
- [Element]: Add when [relevant scenario]

### Length Guidelines
- Minimum: [X words/lines/sections]
- Target: [Y words/lines/sections]
- Maximum: [Z words/lines/sections] (if applicable)
```

### 2.8.1 Complete Enhanced Prompt Template

**Structure**: Use this template to assemble the final enhanced prompt:

```markdown
# [ENHANCED PROMPT TITLE]

## PREREQUISITES & CONTEXT

### Required Knowledge
- [Background knowledge areas]
- [Technical concepts required]
- [Domain expertise needed]

### Available Resources
- [Input data/sources]
- [Tools/APIs available]
- [Reference materials]

### Constraints & Assumptions
- [Limitations]
- [Assumptions]
- [Scope boundaries]

---

## YOUR ROLE
You are a [role definition] who [primary function]. Your core competencies include:
- [Competency 1]
- [Competency 2]
- [Competency 3]

---

## INPUT SPECIFICATION

### Input Types
- [Type 1]: [Description]
- [Type 2]: [Description]

### Input Format
- [Format requirements]
- [Validation criteria]

### Input Validation
**[STRICT]** Before proceeding, verify:
- ✓ [Checkpoint 1]
- ✓ [Checkpoint 2]

---

## EXECUTION PROTOCOL: [REASONING PATTERN NAME]

[Embedded reasoning pattern instructions here]

### STEP 1: [Step Name]
**[STRICT]** [Step instructions]

[Detailed step content]

#### Validation Checkpoint 1
**[STRICT]** Verify:
- ✓ [Validation criteria]

### STEP 2: [Step Name]
[Continue with additional steps...]

---

## OUTPUT FORMAT REQUIREMENTS

[Format specifications from 2.8]

---

## VALIDATION & QUALITY GATES

### Success Criteria
- [Criterion 1]: [Measurable standard]
- [Criterion 2]: [Measurable standard]

### Quality Gates
**[STRICT]** The output MUST meet:
- ✓ [Gate 1]: [Threshold]
- ✓ [Gate 2]: [Threshold]

### Edge Case Handling
- **Case 1**: [Description] → [Handling procedure]
- **Case 2**: [Description] → [Handling procedure]

### Error Handling
- **Error Type 1**: [Description] → [Recovery procedure]
- **Error Type 2**: [Description] → [Recovery procedure]

---

## FINAL VALIDATION CHECKPOINT
**[STRICT]** Before completing, verify:
- ✓ [Final check 1]
- ✓ [Final check 2]
- ✓ [Final check 3]
```

---

## PHASE 2: FINAL VALIDATION & OUTPUT

### 2.9 Enhancement Validation Checkpoint
**[STRICT]** Before finalizing, perform comprehensive validation. Store validation results internally:

**Validation Checklist**:

1. **Intent Preservation**
   - ✓ Does the enhanced prompt achieve the same core goal as the reconstructed prompt?
   - ✓ Is the primary objective unchanged?
   - ✓ Are secondary objectives preserved (if any)?

2. **Fidelity Check**
   - ✓ Are all original keywords/phrases preserved?
   - ✓ Are all original constraints maintained?
   - ✓ Are all original output expectations retained?

3. **Logical Completeness**
   - ✓ Are all gaps identified in section 2.2 addressed?
   - ✓ Is context and prerequisites section complete (section 2.4)?
   - ✓ Is reasoning pattern properly integrated (section 2.5)?
   - ✓ Are specificity enhancements applied (section 2.6)?
   - ✓ Are validation and quality gates added (section 2.7)?
   - ✓ Is output format clearly specified (section 2.8)?

4. **Reasoning Pattern Integration**
   - ✓ Is the appropriate reasoning pattern selected based on task complexity?
   - ✓ Is the reasoning pattern integrated naturally into the execution flow?
   - ✓ Are the reasoning steps clear and actionable?

5. **Specificity Enhancement**
   - ✓ Are all vague terms replaced with concrete, measurable criteria?
   - ✓ Are quality standards defined with measurable thresholds?
   - ✓ Are format requirements explicitly specified?

6. **Quality Gates & Validation**
   - ✓ Are validation checkpoints clearly defined at logical breakpoints?
   - ✓ Are success criteria measurable and specific?
   - ✓ Are edge cases identified and handled?
   - ✓ Is error handling specified for common failure modes?

7. **Actionability**
   - ✓ Can an LLM execute this enhanced prompt effectively without ambiguity?
   - ✓ Are all required inputs, tools, and resources clearly specified?
   - ✓ Is the execution protocol clear and step-by-step?
   - ✓ Are validation criteria specific enough to enable self-checking?

**[STRICT]** If any validation checkpoint fails, revise the enhancement and re-validate. All checkpoints must pass before proceeding to file output.

### 2.10 Direct File Edit (No Chat Output)
**[STRICT]** Phase 2 output is DIRECT FILE EDIT - NO chat output:

**Action Required:**
1. **Determine Target File**: 
   - If input file is `plan.md` → Output to `plan-enhanced.md` OR overwrite `plan.md`
   - If user specifies output file → Use that file
   - Default: Create `[input-filename]-enhanced.md`

2. **Direct File Write**:
   - Write the complete enhanced prompt directly to the target file
   - Include all sections: Prerequisites, Role, Input Spec, Execution Protocol, Output Format, Validation
   - NO chat output - direct file edit only

3. **File Format**:
   - Markdown format
   - Complete enhanced prompt as single document
   - Ready for immediate use

**[STRICT]** After Phase 2:
- ✓ Write enhanced prompt directly to file (NO chat output)
- ✓ Confirm file creation/edit silently
- ✓ NO verbose output to chat - direct file operation only

## COMPLETE WORKFLOW EXECUTION (SILENT MODE)

**[STRICT]** Execute this workflow SILENTLY in the following order:

1. **Receive Input**: LLM output to analyze (from file or user input)
2. **Phase 1 (SILENT)**: Complete reverse engineering protocol (Steps 1-5)
   - Build internal context only
   - NO chat output
   - Store reconstructed prompt internally
3. **Phase 2 (SILENT)**: Use internally stored reconstructed prompt for enhancement (Steps 2.1-2.10)
   - Build enhanced prompt internally
   - NO chat output
4. **Direct File Edit**: Write enhanced prompt directly to file
   - Determine output file (default: `[input-filename]-enhanced.md`)
   - Write complete enhanced prompt to file
   - NO chat output - direct file operation only

---

## EXECUTION MODE: SILENT WITH DIRECT FILE EDIT

**[STRICT]** This command operates in SILENT MODE:
- ✓ Phase 1: Internal context building only (NO chat output)
- ✓ Phase 2: Internal enhancement only (NO chat output)
- ✓ Final: Direct file write (NO chat output)
- ✓ All analysis happens internally
- ✓ Only file operation is visible (file creation/edit)

**Input**: [The LLM output file to be analyzed will be provided here]

**Proceed silently with Phase 1, Step 1: Output Analysis & Characterization (internal only).**

**Remember**: 
- Follow all [STRICT] directives without deviation
- Keep ALL analysis internal - NO chat output
- Phase 1 builds context silently
- Phase 2 uses that context silently
- Final output: Direct file edit only
- NO verbose explanations in chat