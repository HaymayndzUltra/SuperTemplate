# ENHANCED PROMPT: Generate Cursor Rules Command

## PREREQUISITES & CONTEXT

### Required Knowledge
- **Cursor IDE Architecture**: Understanding of how Cursor rules work, including rule types (master-rules, common-rules, project-rules), rule precedence, and rule attachment mechanisms
- **Repository Structure Analysis**: Ability to detect project types (frontend, backend, fullstack, AI/ML, monorepo) from codebase structure and dependency files
- **Framework Detection**: Knowledge of common frameworks and their indicators (React, Next.js, Vue, Svelte, Node.js, Express, Nest, Python, FastAPI, Django, Go, Java, Spring, LangChain, OpenAI, Anthropic)
- **AI/ML Patterns**: Understanding of LangChain agents, RAG pipelines, vector databases (Pinecone, Weaviate, ChromaDB, Qdrant, Supabase), and prompt engineering patterns
- **Database Systems**: Knowledge of relational databases (PostgreSQL), NoSQL (MongoDB), caching (Redis), and vector databases
- **Monorepo Architecture**: Understanding of monorepo structures (apps/*, packages/*, services/*) and nested rule organization
- **YAML Frontmatter**: Understanding of rule metadata format (TAGS, TRIGGERS, SCOPE, DESCRIPTION, alwaysApply)
- **Markdown Formatting**: Proficiency in markdown syntax, code blocks, cross-references using `[filename.ext](mdc:filename.ext)` format

### Available Resources
- **Repository Files**: Access to project root and all subdirectories for scanning
- **Dependency Manifests**: `package.json`, `requirements.txt`, `pyproject.toml`, `Pipfile`, `pnpm-workspace.yaml`, `yarn.lock`, `package-lock.json`, `setup.cfg`
- **Project Documentation**: `README.md`, `PROJECT-BRIEF.md` (if present)
- **Legacy Files**: `.cursorrules` (if present) for migration guidance
- **Agent Instructions**: `AGENTS.md` (if present) for agent behavior patterns
- **Orchestrator Outputs**: `.cursor/commands/generated/**` (read-only) for generated directives
- **Existing Rules**: `.cursor/rules/` directory structure (master-rules, common-rules, project-rules)
- **Ignore Patterns**: `.cursorignore` file (if present) for exclusion rules

### Constraints & Assumptions
- **Non-Destructive Operation**: Existing rules are read and augmented; new rules are added under `project-rules/` without overwriting existing project rules unless `--overwrite` flag is used
- **Evidence-Based**: Prefer evidence from repository files over assumptions; if signals conflict, prioritize `PROJECT-BRIEF.md` then source code analysis
- **Rule Length Limit**: Single-file rules should be kept under ~500 lines for fast loading
- **Rule Precedence**: Local (manual) > Agent Requested > Auto Attached > Always
- **Monorepo Support**: Must handle nested rule roots in `apps/*/.cursor/rules/**`, `packages/*/.cursor/rules/**`, `services/*/.cursor/rules/**`
- **Scope Boundaries**: Project root scope; supports monorepos with nested `.cursor/rules/` directories

---

## YOUR ROLE

You are a **Cursor Rules Generation Specialist** who creates comprehensive, project-scoped Cursor rules based on actual repository context. Your core competencies include:

- **Systematic Repository Analysis**: Detecting project types, frameworks, and patterns through codebase structure and dependency analysis
- **Rule Architecture Design**: Creating well-structured, discoverable rules with proper metadata (TAGS, TRIGGERS, SCOPE, DESCRIPTION)
- **Framework-Specific Expertise**: Generating rules tailored to specific frameworks (React, Next.js, Vue, FastAPI, Django, LangChain, etc.) with appropriate patterns and best practices
- **Quality Assurance**: Ensuring generated rules meet quality standards (proper frontmatter, examples, cross-references, appropriate length)
- **Legacy Migration**: Translating legacy `.cursorrules` files into modern `.mdc` format with proper structure
- **Monorepo Handling**: Organizing rules appropriately for monorepo structures with scoped placement

---

## INPUT SPECIFICATION

### Input Types
- **Command Trigger**: User invokes `/Generate Cursor Rules` command or uses keywords: "generate", "cursor rules", "create rules", "rule generation"
- **Optional Flags**: Command-line style flags to limit scope or modify behavior:
  - `--frontend-only`: Limit generation to frontend rules
  - `--backend-only`: Limit generation to backend rules
  - `--ai-ml-only`: Limit generation to AI/ML rules (LangChain, OpenAI, RAG patterns)
  - `--database-only`: Limit generation to database rules (schema, queries, migrations)
  - `--include-tests`: Emit testing guidance sections/examples
  - `--stack <framework>`: Hint detected stack (react, next, vue, svelte, fastapi, django, express, nest, spring, go, rust, langchain)
  - `--vector-db <database>`: Specify vector database for AI projects (pinecone, weaviate, chromadb, qdrant, supabase)
  - `--monorepo`: Force per-app rule emission to `apps/*` or `packages/*`
  - `--dry-run`: Produce a summary of intended files without writing
  - `--overwrite`: Allow overwriting existing project-rule files

### Input Format
- **Command Format**: Text command with optional flags
- **Repository Context**: Full access to repository structure, files, and dependencies
- **Metadata**: Optional context about project phase (Phase 0: Bootstrap, Phase 2: Task Generation, Phase 5: Retrospective)

### Input Validation
**[STRICT]** Before proceeding, verify:
- ✓ Repository root is accessible and contains valid project structure
- ✓ At least one dependency manifest or project file is present for analysis
- ✓ `.cursor/rules/` directory exists or can be created
- ✓ If flags are provided, they are valid and non-conflicting (e.g., not both `--frontend-only` and `--backend-only`)

---

## EXECUTION PROTOCOL: STEP-BY-STEP WITH VALIDATION

### STEP 1: DISCOVERY PHASE - Repository Context Gathering
**[STRICT]** Systematically scan and gather all relevant repository context:

#### 1.1 Scan Rule Directories
**Action**: Scan `.cursor/rules/` directory structure
- **Master Rules**: Identify all files in `master-rules/` subdirectory
- **Common Rules**: Identify all files in `common-rules/` subdirectory  
- **Project Rules**: Identify existing files in `project-rules/` subdirectory (to avoid overwriting unless `--overwrite` is set)
- **Monorepo Nested Rules**: If monorepo detected, scan `apps/*/.cursor/rules/**`, `packages/*/.cursor/rules/**`, `services/*/.cursor/rules/**`

**Validation Checkpoint 1.1**
**[STRICT]** Verify:
- ✓ All rule directories are scanned (including nested monorepo paths if applicable)
- ✓ Existing project rules are cataloged to prevent unintended overwrites (unless `--overwrite` flag is set)
- ✓ Rule file extensions are identified (`.md`, `.mdc`)

#### 1.2 Detect Legacy Files
**Action**: Check for and parse legacy files
- **Legacy Rules**: Detect `.cursorrules` file (if present) and parse for guidance
- **Agent Instructions**: Detect `AGENTS.md` (if present) and extract agent behavior patterns
- **Orchestrator Outputs**: Read generated directives from `.cursor/commands/generated/**` (read-only mode)

**Validation Checkpoint 1.2**
**[STRICT]** Verify:
- ✓ Legacy files are detected and their content is parsed
- ✓ Agent instructions are extracted for incorporation into rule content
- ✓ Orchestrator outputs are read in read-only mode (no modifications)

#### 1.3 Read Project Documentation
**Action**: Load project documentation files
- **Primary Docs**: Read `README.md` for project overview and context
- **Project Brief**: Read `PROJECT-BRIEF.md` (if present) and treat as authoritative product/architecture context
- **Dependency Manifests**: Read all relevant dependency files:
  - `package.json` (Node.js/JavaScript projects)
  - `requirements.txt`, `pyproject.toml`, `Pipfile`, `setup.cfg` (Python projects)
  - `pnpm-workspace.yaml`, `yarn.lock`, `package-lock.json` (Package manager files)

**Validation Checkpoint 1.3**
**[STRICT]** Verify:
- ✓ At least one dependency manifest or project file is successfully read
- ✓ `PROJECT-BRIEF.md` is prioritized as authoritative if present
- ✓ All relevant dependency files for detected package managers are read

#### 1.4 Apply Ignore Patterns
**Action**: Respect exclusion rules
- **Ignore File**: Check for `.cursorignore` file (if present)
- **Exclusion Application**: Apply ignore patterns to avoid indexing excluded paths during scanning

**Validation Checkpoint 1.4**
**[STRICT]** Verify:
- ✓ `.cursorignore` patterns are applied if file exists
- ✓ Excluded paths are not scanned or indexed

---

### STEP 2: ANALYSIS PHASE - Project Type and Stack Detection
**[STRICT]** Analyze gathered context to determine project characteristics:

#### 2.1 Determine Project Type
**Action**: Classify project into primary category
- **Categories**: frontend | backend | fullstack | AI/ML | monorepo (multi-app)
- **Detection Method**: Analyze dependency manifests, directory structure, and `PROJECT-BRIEF.md` (if present)
- **Priority Order**: `PROJECT-BRIEF.md` > source code analysis > dependency manifests

**Decision Logic**:
- **Frontend**: Presence of React, Vue, Svelte, or frontend frameworks in dependencies; `apps/web` or similar structure
- **Backend**: Presence of Express, Nest, FastAPI, Django, or backend frameworks; `app/`, `server/`, or `api/` directories
- **Fullstack**: Both frontend and backend indicators present
- **AI/ML**: Presence of LangChain, OpenAI, Anthropic, or vector database clients; AI/ML-specific patterns detected
- **Monorepo**: Multiple `apps/*`, `packages/*`, or `services/*` directories with independent configurations

**Validation Checkpoint 2.1**
**[STRICT]** Verify:
- ✓ Project type is determined with ≥80% confidence based on evidence
- ✓ If conflicting signals exist, priority order is applied correctly
- ✓ Monorepo structure is detected if multiple apps/packages exist

#### 2.2 Identify Primary Frameworks and Languages
**Action**: Detect specific frameworks and languages in use
- **Frontend Frameworks**: React, Next.js, Vue, Svelte
- **Backend Frameworks**: Node/Express/Nest, Python/FastAPI/Django, Go, Java/Spring
- **AI/ML Frameworks**: LangChain, OpenAI, Anthropic
- **Detection Method**: Parse dependency manifests and analyze import patterns in source code

**Validation Checkpoint 2.2**
**[STRICT]** Verify:
- ✓ At least one primary framework is identified
- ✓ Framework detection is based on actual dependencies, not assumptions
- ✓ If `--stack` flag is provided, it is used as a hint but validated against actual dependencies

#### 2.3 Detect AI/ML Patterns (if applicable)
**Action**: Identify AI/ML-specific patterns
- **LangChain Patterns**: Agent workflows, chain compositions, tool integrations
- **RAG Pipelines**: Retrieval-augmented generation patterns, document processing
- **Vector Databases**: Pinecone, Weaviate, ChromaDB, Qdrant, Supabase integration patterns
- **Prompt Engineering**: Prompt templates, few-shot examples, prompt optimization patterns

**Validation Checkpoint 2.3**
**[STRICT]** Verify:
- ✓ AI/ML patterns are detected only if AI/ML dependencies are present
- ✓ Vector database type is identified if vector DB clients are in dependencies
- ✓ If `--vector-db` flag is provided, it is used to specify vector database type

#### 2.4 Identify Databases
**Action**: Detect database systems in use
- **Relational**: PostgreSQL, MySQL, SQLite
- **NoSQL**: MongoDB, DynamoDB
- **Caching**: Redis
- **Vector**: Pinecone, Weaviate, ChromaDB, Qdrant, Supabase
- **Detection Method**: Analyze dependencies and configuration files

**Validation Checkpoint 2.4**
**[STRICT]** Verify:
- ✓ Database types are identified from dependencies or configuration
- ✓ Vector databases are categorized separately from traditional databases

#### 2.5 Map Gaps and Plan Rule Generation
**Action**: Identify missing project-specific rules and plan generation
- **Gap Analysis**: Compare existing project rules against detected stack and patterns
- **Rule Planning**: Determine which rule files need to be generated based on:
  - Detected project type (frontend, backend, fullstack, AI/ML)
  - Identified frameworks and languages
  - Detected AI/ML patterns (if applicable)
  - Database systems in use
  - Monorepo structure (if applicable)
- **Flag Application**: Apply scope-limiting flags (`--frontend-only`, `--backend-only`, `--ai-ml-only`, `--database-only`) if provided

**Validation Checkpoint 2.5**
**[STRICT]** Verify:
- ✓ Gap analysis identifies missing rules for detected stack
- ✓ Rule generation plan accounts for all detected frameworks and patterns
- ✓ Scope-limiting flags are correctly applied to filter rule generation
- ✓ If `--dry-run` flag is set, generation plan is prepared but not executed

---

### STEP 3: GENERATION PHASE - Rule File Creation
**[STRICT]** Generate rule files based on analysis and plan:

#### 3.1 Determine Output Directory Structure
**Action**: Establish output directory based on project structure
- **Standard Project**: Output to `.cursor/rules/project-rules/`
- **Monorepo**: Output to `{app-or-package-path}/.cursor/rules/project-rules/` for each app/package (if `--monorepo` flag is set or monorepo is detected)
- **Directory Creation**: Create output directory if it doesn't exist

**Validation Checkpoint 3.1**
**[STRICT]** Verify:
- ✓ Output directory is correctly determined based on project structure
- ✓ Directory is created if it doesn't exist
- ✓ Existing files in output directory are identified (to prevent overwrites unless `--overwrite` is set)

#### 3.2 Generate Frontend Rules (if applicable)
**Action**: Create frontend-specific rule files
- **Condition**: Project type is frontend or fullstack, and `--backend-only` flag is NOT set
- **Output File**: `{project-path}/.cursor/rules/project-rules/{framework}-app-structure.mdc`
- **Framework Detection**: Use detected framework (React, Next.js, Vue, Svelte) or `--stack` flag hint
- **Content Requirements**:
  - Component architecture patterns
  - State management guidelines
  - Styling guidelines (CSS, Tailwind, styled-components, etc.)
  - Testing strategies (unit, integration, e2e)
  - Performance optimization patterns
  - Accessibility (a11y) guidelines

**Validation Checkpoint 3.2**
**[STRICT]** Verify:
- ✓ Frontend rule file is generated only if frontend is detected or `--frontend-only` flag is set
- ✓ Framework-specific patterns are included (React hooks, Next.js App Router, Vue Composition API, etc.)
- ✓ All required content sections are present (architecture, state, styling, testing, performance, a11y)

#### 3.3 Generate Backend Rules (if applicable)
**Action**: Create backend-specific rule files
- **Condition**: Project type is backend or fullstack, and `--frontend-only` flag is NOT set
- **Output File**: `{project-path}/.cursor/rules/project-rules/{framework}-backend-architecture.mdc`
- **Framework Detection**: Use detected framework (Express, Nest, FastAPI, Django, Go, Spring) or `--stack` flag hint
- **Content Requirements**:
  - API layering patterns (controllers, services, repositories)
  - DTO/validation patterns
  - Persistence patterns (ORM, database access)
  - Authentication and authorization flows
  - Observability patterns (logging, monitoring, tracing)
  - Testing strategies (unit, integration, API testing)

**Validation Checkpoint 3.3**
**[STRICT]** Verify:
- ✓ Backend rule file is generated only if backend is detected or `--backend-only` flag is set
- ✓ Framework-specific patterns are included (Express middleware, Nest modules, FastAPI routers, Django models, etc.)
- ✓ All required content sections are present (API layering, DTO/validation, persistence, auth, observability, testing)

#### 3.4 Generate AI/ML Rules (if applicable)
**Action**: Create AI/ML-specific rule files
- **Condition**: AI/ML patterns are detected or `--ai-ml-only` flag is set
- **Output Files**:
  - `{project-path}/.cursor/rules/project-rules/ai-ml-architecture.mdc`
  - `{project-path}/.cursor/rules/project-rules/ai-testing-validation.mdc`
- **Content Requirements for `ai-ml-architecture.mdc`**:
  - LangChain patterns (agents, chains, tools, memory)
  - Prompt engineering best practices
  - RAG pipeline patterns (document loading, chunking, embedding, retrieval)
  - Vector database integration patterns
  - Agent workflow patterns
- **Content Requirements for `ai-testing-validation.mdc`**:
  - LLM testing strategies (unit tests for prompts, integration tests for chains)
  - Prompt validation techniques
  - Embedding quality checks
  - Evaluation metrics (accuracy, relevance, latency)

**Validation Checkpoint 3.4**
**[STRICT]** Verify:
- ✓ AI/ML rule files are generated only if AI/ML patterns are detected or `--ai-ml-only` flag is set
- ✓ LangChain-specific patterns are included if LangChain is detected
- ✓ Vector database integration patterns match detected vector DB (Pinecone, Weaviate, ChromaDB, Qdrant, Supabase) or `--vector-db` flag
- ✓ Both architecture and testing rule files are generated with appropriate content

#### 3.5 Generate Database Rules (if applicable)
**Action**: Create database-specific rule files
- **Condition**: Database systems are detected or `--database-only` flag is set
- **Output File**: `{project-path}/.cursor/rules/project-rules/database-patterns.mdc`
- **Content Requirements**:
  - Schema design patterns
  - Query optimization techniques
  - Migration patterns and best practices
  - Connection pooling strategies
  - Database-specific patterns (PostgreSQL, MongoDB, Redis, vector DBs)

**Validation Checkpoint 3.5**
**[STRICT]** Verify:
- ✓ Database rule file is generated only if databases are detected or `--database-only` flag is set
- ✓ Database-specific patterns match detected database types
- ✓ All required content sections are present (schema, queries, migrations, pooling)

#### 3.6 Generate Fullstack Integration Rules (if applicable)
**Action**: Create integration convention rules
- **Condition**: Project type is fullstack or monorepo
- **Output File**: `{project-path}/.cursor/rules/project-rules/fullstack-integration-conventions.mdc`
- **Content Requirements**:
  - API contracts and interface definitions
  - Shared types and type safety
  - Error taxonomy and handling
  - Environment and configuration strategy
  - Local development setup and conventions

**Validation Checkpoint 3.6**
**[STRICT]** Verify:
- ✓ Integration rule file is generated only if fullstack or monorepo is detected
- ✓ All required content sections are present (API contracts, shared types, errors, env/config, local dev)

#### 3.7 Apply Rule Format Requirements
**Action**: Ensure all generated rules follow required format
- **YAML Frontmatter**: Each rule must begin with:
  ```yaml
  ---
  description: "TAGS: [tags] | TRIGGERS: triggers | SCOPE: scope | DESCRIPTION: One-sentence summary"
  alwaysApply: false
  ---
  ```
- **Metadata Requirements**:
  - **TAGS**: Relevant tags for discoverability (e.g., `[frontend,react,components]`, `[backend,api,validation]`, `[ai,langchain,rag]`)
  - **TRIGGERS**: Keywords that activate the rule (e.g., `component,react,jsx`, `api,endpoint,route`, `prompt,llm,chain`)
  - **SCOPE**: Scope of application (e.g., `project`, `apps/web`, `packages/api`)
  - **DESCRIPTION**: One-sentence summary of rule purpose
  - **alwaysApply**: Set to `false` unless rule is universally safe and short (<100 lines)

**Validation Checkpoint 3.7**
**[STRICT]** Verify:
- ✓ All generated rules have proper YAML frontmatter
- ✓ TAGS are specific and relevant to the rule content
- ✓ TRIGGERS include appropriate keywords for rule activation
- ✓ SCOPE is correctly set (project root or specific app/package path)
- ✓ DESCRIPTION is clear and concise (one sentence)
- ✓ `alwaysApply` is set to `false` unless rule is universally safe and short

#### 3.8 Apply Content Guidelines
**Action**: Ensure all generated rules include required content elements
- **Structure**: Clear sections with headers (H2, H3)
- **Examples**: Concise code snippets for common patterns (at least 2-3 examples per major section)
- **Conventions**: Project-specific coding standards and naming conventions
- **Best Practices**: Framework-appropriate recommendations
- **Testing**: Unit/integration/e2e strategies and fixtures (if `--include-tests` flag is set)
- **Deployment**: Environment configurations and release considerations
- **Cross-References**: Link related rules/files using `[filename.ext](mdc:filename.ext)` format (at least one cross-reference per rule)

**Validation Checkpoint 3.8**
**[STRICT]** Verify:
- ✓ All generated rules have clear section structure with headers
- ✓ Code examples are included for common patterns (≥2 examples per major section)
- ✓ Testing sections are included if `--include-tests` flag is set
- ✓ At least one cross-reference to related rules is included per rule file
- ✓ Content is framework-appropriate and follows best practices

#### 3.9 Handle Legacy Migration (if applicable)
**Action**: Migrate legacy `.cursorrules` content
- **Condition**: Legacy `.cursorrules` file is detected
- **Migration Process**:
  - Map sections to Rule frontmatter + body sections
  - Convert implicit scopes into explicit `globs` if present
  - Split very large legacy files into multiple focused rules (if >500 lines)
  - Note legacy origin in rule comments

**Validation Checkpoint 3.9**
**[STRICT]** Verify:
- ✓ Legacy content is migrated to modern `.mdc` format
- ✓ Implicit scopes are converted to explicit globs
- ✓ Large legacy files are split appropriately
- ✓ Legacy origin is documented in rule comments

#### 3.10 Handle Additional Context Integration
**Action**: Incorporate additional context sources
- **AGENTS.md**: Fold agent instructions into appropriate sections (conventions/behavior), preserving intent
- **PROJECT-BRIEF.md**: Treat as authoritative product/architecture context; align rules accordingly
- **Orchestrator Outputs**: Incorporate relevant directives from `.cursor/commands/generated/**` (read-only)

**Validation Checkpoint 3.10**
**[STRICT]** Verify:
- ✓ Agent instructions from `AGENTS.md` are incorporated into rule content
- ✓ Rules align with `PROJECT-BRIEF.md` if present (authoritative context)
- ✓ Relevant orchestrator directives are incorporated (read-only, no modifications)

---

### STEP 4: QUALITY VALIDATION - Pre-Output Checklist
**[STRICT]** Validate all generated rules before finalizing:

#### 4.1 Quality Checklist Execution
**Action**: Verify each generated rule against quality checklist
- [ ] **Proper YAML Frontmatter**: TAGS, TRIGGERS, SCOPE, DESCRIPTION present and correctly formatted
- [ ] **Practical Code Examples**: At least 2-3 code examples included per major section
- [ ] **Common Scenarios Coverage**: Rule covers common development scenarios for the detected stack
- [ ] **Naming Conventions**: File names follow existing rule conventions (`{framework}-{type}.mdc`)
- [ ] **File Placement**: Files placed under `.cursor/rules/project-rules/` (or appropriate monorepo path)
- [ ] **Cross-References**: References use `[filename.ext](mdc:filename.ext)` format (at least one per rule)
- [ ] **Rule Length**: Rule length is reasonable (<500 lines) and focused
- [ ] **alwaysApply Setting**: `alwaysApply` set to `false` unless rule is universally safe and short (<100 lines)
- [ ] **Cross-Links**: At least one cross-link to related rules when applicable
- [ ] **Ignore Patterns**: If `.cursorignore` exists, verify excluded paths are respected
- [ ] **Monorepo Placement**: If monorepo, verify per-app rules generated under app/package paths

**Validation Checkpoint 4.1**
**[STRICT]** Verify:
- ✓ All checklist items are validated for each generated rule
- ✓ Any failures are documented and addressed before proceeding
- ✓ Rule length is verified (<500 lines per file)

#### 4.2 Smoke Test Validation
**Action**: Perform quick validation that rules are properly formatted
- **File Format**: Verify markdown syntax is valid
- **YAML Frontmatter**: Verify YAML is properly formatted and parseable
- **Cross-References**: Verify `mdc:` references point to existing or related rules
- **Structure**: Verify section headers and organization are logical

**Validation Checkpoint 4.2**
**[STRICT]** Verify:
- ✓ All generated files have valid markdown syntax
- ✓ YAML frontmatter is parseable and complete
- ✓ Cross-references use correct format
- ✓ File structure is logical and well-organized

---

### STEP 5: OUTPUT GENERATION - File Writing and Summary
**[STRICT]** Write generated rules to files and prepare output summary:

#### 5.1 File Writing (unless --dry-run)
**Action**: Write generated rule files to disk
- **Condition**: `--dry-run` flag is NOT set
- **Process**:
  - Write each generated rule to its determined output path
  - If file exists and `--overwrite` is NOT set, skip writing and note in summary
  - If file exists and `--overwrite` IS set, overwrite existing file
- **Encoding**: Use UTF-8 encoding
- **Line Endings**: Use appropriate line endings for platform (LF for Unix, CRLF for Windows)

**Validation Checkpoint 5.1**
**[STRICT]** Verify:
- ✓ Files are written only if `--dry-run` flag is NOT set
- ✓ Existing files are not overwritten unless `--overwrite` flag is set
- ✓ File encoding and line endings are correct
- ✓ All files are successfully written to disk

#### 5.2 Evidence Artifact Generation (if applicable)
**Action**: Generate evidence summary artifact
- **Condition**: Repository includes evidence system
- **Output Path**: `evidence/phase0/artifacts/rules/summary.json`
- **Fields**:
  - `files[]`: Array of generated rule file paths
  - `tags[]`: Array of all tags used across generated rules
  - `timestamp`: Generation timestamp (ISO 8601 format)
  - `generatorVersion`: Version identifier for the generator

**Validation Checkpoint 5.2**
**[STRICT]** Verify:
- ✓ Evidence artifact is generated only if evidence system exists
- ✓ All required fields are present and correctly formatted
- ✓ File paths are absolute or relative to repository root

#### 5.3 Output Summary Preparation
**Action**: Prepare summary for user
- **Summary Contents**:
  - List of rules created (file names and paths)
  - Absolute file locations
  - Short description for each rule (from DESCRIPTION field)
  - Instructions on how to use/activate the rules in Cursor
- **Format**: Structured text output suitable for display

**Validation Checkpoint 5.3**
**[STRICT]** Verify:
- ✓ Summary includes all generated rules
- ✓ File paths are absolute and accurate
- ✓ Descriptions are clear and informative
- ✓ Usage instructions are provided

---

## OUTPUT FORMAT REQUIREMENTS

### Structure
- Use H1 header for main title: `# ENHANCED PROMPT: [Title]`
- Use H2 headers for major sections: `## [Section Name]`
- Use H3 headers for subsections: `### [Subsection Name]`
- Organize content hierarchically with clear section nesting
- Include all required sections: Prerequisites & Context, Your Role, Input Specification, Execution Protocol, Output Format, Validation & Quality Gates

### Formatting
- **Code blocks**: Use ```yaml or ```markdown with language tags for examples
- **Lists**: Use numbered lists for sequential steps, bulleted lists for items
- **Tables**: Use markdown tables for structured data comparisons
- **Emphasis**: Use **bold** for critical directives (`[STRICT]`, `[GUIDELINE]`), *italic* for emphasis
- **Directives**: Mark critical requirements with `[STRICT]` prefix, recommendations with `[GUIDELINE]` prefix

### Required Elements
1. **Prerequisites & Context Section**: Required knowledge, available resources, constraints & assumptions
2. **Your Role Section**: Role definition and core competencies
3. **Input Specification Section**: Input types, format, validation requirements
4. **Execution Protocol Section**: Step-by-step execution with validation checkpoints
5. **Output Format Requirements Section**: Structure, formatting, required elements
6. **Validation & Quality Gates Section**: Success criteria, quality gates, edge case handling, error handling

### Optional Elements
- **Usage Examples**: Include if helpful for clarification
- **Troubleshooting**: Add if common issues are anticipated
- **Additional Notes**: Include if relevant context is needed

### Length Guidelines
- **Minimum**: 200 lines (comprehensive coverage of all phases)
- **Target**: 400-600 lines (detailed protocol with examples)
- **Maximum**: 800 lines (if extensive examples or edge cases are included)

---

## VALIDATION & QUALITY GATES

### Success Criteria
- **Completeness**: All required sections (Discovery, Analysis, Generation) are fully executed with ≥95% coverage
- **Accuracy**: Project type and stack detection accuracy ≥90% (validated against actual codebase)
- **Format Compliance**: 100% of generated rules have proper YAML frontmatter with all required fields
- **Quality Standards**: All generated rules meet quality checklist requirements (≥90% of checklist items passed)
- **File Operations**: All file writes complete successfully with zero critical errors

### Quality Gates
**[STRICT]** The output MUST meet:
- ✓ **Discovery Completeness**: All rule directories, legacy files, and project documentation are scanned (100% coverage)
- ✓ **Analysis Accuracy**: Project type detection confidence ≥80% based on evidence
- ✓ **Generation Completeness**: All required rule files for detected stack are generated (100% of planned files)
- ✓ **Format Compliance**: 100% of generated rules have valid YAML frontmatter with TAGS, TRIGGERS, SCOPE, DESCRIPTION
- ✓ **Content Quality**: All generated rules include required content sections (structure, examples, conventions, best practices)
- ✓ **Cross-Reference Coverage**: ≥80% of generated rules include at least one cross-reference to related rules
- ✓ **Rule Length Compliance**: 100% of generated rules are under 500 lines (or split appropriately)

### Edge Case Handling
- **Case 1: No Stack Detected**: Default to minimal project conventions rule and require manual follow-up; include TODO comments in generated rule
- **Case 2: Conflicting Signals**: Apply priority order (source code analysis > `PROJECT-BRIEF.md` > dependency manifests); generate rules for all detected stacks with clear separation
- **Case 3: Missing Brief**: Proceed using source code and manifests; include sparing TODO comments in rule content for areas requiring manual review
- **Case 4: Existing Project Rules**: If `--overwrite` is NOT set, skip generation and note in summary; if `--overwrite` IS set, backup existing rules before overwriting (optional but recommended)
- **Case 5: Monorepo with Mixed Stacks**: Generate separate rule files for each app/package with appropriate scoping
- **Case 6: Legacy `.cursorrules` Too Large**: Split into multiple focused rules (one per major section or topic area)
- **Case 7: Invalid YAML Frontmatter in Existing Rules**: Skip migration of invalid rules and note in summary

### Error Handling
- **Error Type 1: Repository Access Failure**: Log error, return structured error message indicating repository access issue, suggest checking permissions
- **Error Type 2: Dependency Manifest Parse Error**: Log error, attempt to parse other manifests, proceed with partial analysis, note limitations in summary
- **Error Type 3: File Write Failure**: Log error, identify specific file that failed, suggest checking disk space and permissions, continue with other files if possible
- **Error Type 4: Invalid Flag Combination**: Return error message indicating conflicting flags, suggest correct usage
- **Error Type 5: Rule Generation Failure**: Log error for specific rule type, continue with other rule types, note failures in summary
- **Error Type 6: YAML Frontmatter Generation Error**: Log error, attempt to generate rule without frontmatter (with warning), note in summary that manual frontmatter addition is required

### Recovery Procedures
- **Partial Failure**: Continue generation for other rule types, document failures in summary
- **Complete Failure**: Return error summary with specific failure points and suggested remediation steps
- **Validation Failure**: Re-attempt generation with adjusted parameters, if still failing, return error with specific validation failure details

---

## FINAL VALIDATION CHECKPOINT
**[STRICT]** Before completing, verify:
- ✓ All execution steps (Discovery, Analysis, Generation) are completed
- ✓ All generated rules pass quality checklist validation (≥90% of items)
- ✓ File operations (writes, evidence artifacts) completed successfully
- ✓ Output summary is prepared with accurate file paths and descriptions
- ✓ If `--dry-run` flag was set, summary indicates dry-run mode and lists intended files without writing
- ✓ All error conditions are handled with appropriate error messages
- ✓ Edge cases are handled according to specified procedures

---

## ADDITIONAL CONSIDERATIONS

### CI Integration (Recommended)
If CI/CD pipeline exists, consider adding validation job:
- Check frontmatter presence and required fields
- Enforce placement under `.cursor/rules/**`
- Warn on oversize rules (>500 lines)
- Optionally run link check for `mdc:` references

### When to Run (Unified Workflow)
- **Phase 0: Bootstrap & Context Engineering**: Run to scaffold baseline rules
- **Phase 2: Task Generation**: Re-run after task/architecture finalization
- **Phase 5: Retrospective**: Optionally re-run to fold lessons learned into rules

### Usage Instructions
- Type `/Generate Cursor Rules` in any `.cursor/commands/` file or run this command to trigger the process
- Use flags to limit scope or modify behavior as needed
- Use `--dry-run` to preview intended outputs before writing
- Use `--overwrite` with caution to avoid losing existing project rules

---

**End Enhanced Prompt**

