
Command: /Generate Cursor Rules

Purpose
- Generate comprehensive, project-scoped Cursor rules based on actual repository context.
 - Scope: Project root (supports monorepos with nested `.cursor/rules/`).

Discovery Phase
- Scan `.cursor/rules/` directory (master-rules, common-rules, project-rules).
- Detect legacy `.cursorrules` (if present) and parse for guidance.
- Detect `AGENTS.md` (if present) and ingest its agent instructions.
- Read project docs if present: `README.md`, `package.json`, `requirements.txt`, `pyproject.toml`, `Pipfile`, `pnpm-workspace.yaml`, `yarn.lock`, `package-lock.json`, `setup.cfg`.
- Read `PROJECT-BRIEF.md` (if present) and incorporate guidance.
- If orchestrator exists, read generated directives (read-only): `.cursor/commands/generated/**`.
 - For monorepos, also scan nested rule roots: `apps/*/.cursor/rules/**`, `packages/*/.cursor/rules/**`, `services/*/.cursor/rules/**`.
 - Respect `.cursorignore` when present to avoid indexing excluded paths.

Analysis Phase
- Determine project type: frontend, backend, fullstack, or monorepo (multi-app).
- Identify primary frameworks/languages (e.g., React, Next.js, Vue, Svelte, Node/Express/Nest, Python/FastAPI/Django, Go, Java/Spring, etc.).
- Map gaps: missing project-specific rules, unclear areas from brief/agents.
- Plan rule set(s) to generate per detected stack and structure.

Generation Phase
- Output directory: `.cursor/rules/project-rules/`.
- For frontend projects, create:
  - `{project-path}/.cursor/rules/project-rules/{framework}-app-structure.mdc`
    - Component architecture patterns, state management, styling guidelines, testing strategies, performance & a11y.
- For backend projects, create:
  - `{project-path}/.cursor/rules/project-rules/{framework}-backend-architecture.mdc`
    - API layering, DTO/validation, persistence patterns, auth flows, observability, testing.
- For fullstack/monorepo projects, create both frontend and backend rule files, plus integration conventions:
  - `{project-path}/.cursor/rules/project-rules/fullstack-integration-conventions.mdc`
    - API contracts, shared types, error taxonomy, env/config strategy, local dev.

Flags & Options (optional)
- `--frontend-only`: Limit generation to frontend rules.
- `--backend-only`: Limit generation to backend rules.
- `--include-tests`: Emit testing guidance sections/examples.
- `--stack <react|next|vue|svelte|fastapi|django|express|nest|spring|go|rust>`: Hint detected stack.
- `--monorepo`: Force per-app rule emission to `apps/*` or `packages/*`.
- `--dry-run`: Produce a summary of intended files without writing.
- `--overwrite`: Allow overwriting existing project-rule files.

Rule Format Requirements
Each generated rule must begin with YAML frontmatter:
```yaml
---
description: "TAGS: [tags] | TRIGGERS: triggers | SCOPE: scope | DESCRIPTION: One-sentence summary"
alwaysApply: false
---
```

Rule Types & Precedence
- Local (manual) > Agent Requested > Auto Attached > Always
- Guidance:
  - Prefer `alwaysApply: false` unless the rule is universally safe and short.
  - Use precise TAGS/TRIGGERS/SCOPE to minimize irrelevant attachments.
  - Keep single-file rules under ~500 lines for fast loading.

Content Guidelines (each rule)
- Structure: clear sections with headers.
- Examples: concise code snippets for common patterns.
- Conventions: project-specific coding standards and naming.
- Best Practices: framework-appropriate recommendations.
- Testing: unit/integration/e2e strategies and fixtures.
- Deployment: environments, config, and release considerations.
- References: link related rules/files using `[filename.ext](mdc:filename.ext)` when applicable.
 - Scoped Organization: in monorepos, prefer placing rules next to code (e.g., `apps/web/.cursor/rules/`).

Quality Checklist (validate before finishing)
- [ ] Proper YAML frontmatter with TAGS, TRIGGERS, SCOPE, DESCRIPTION
- [ ] Practical code examples included
- [ ] Covers common development scenarios for the stack
- [ ] Naming follows existing rule conventions
- [ ] Files placed under `.cursor/rules/project-rules/`
- [ ] References use `[filename.ext](mdc:filename.ext)` format
 - [ ] Rule length reasonable (< 500 lines) and focused
 - [ ] `alwaysApply` set only when universally safe
 - [ ] At least one cross-link to related rules when applicable
 - [ ] Quick smoke test: Open rule file in Cursor and verify it attaches where expected
 - [ ] If `.cursorignore` exists, verify excluded paths are respected
 - [ ] If monorepo, verify per-app rules generated under app/package paths

Output Format (return to user)
- Summary of rules created
- Absolute file locations
- Short description for each rule
- Instructions on how to use/activate the rules in Cursor

Additional Handling
- If `.cursorrules` exists: migrate salient guidance into generated project rules; note legacy origin.
- If `AGENTS.md` exists: fold agent instructions into appropriate sections (conventions/behavior), preserving intent.
- If `PROJECT-BRIEF.md` exists: treat as authoritative product/architecture context; align rules accordingly.
- If `.cursor/commands/generated/` contains orchestrator outputs: incorporate relevant directives (read-only).

Legacy Migration
- Detect legacy `.cursorrules` and translate to `.mdc`:
  - Map sections to Rule frontmatter + body sections
  - Convert implicit scopes into explicit `globs` if present
  - Split very large legacy files into multiple focused rules

Evidence Artifacts (optional)
- If the repository includes an evidence system, emit a summary artifact:
  - Path: `evidence/phase0/artifacts/rules/summary.json`
  - Fields: `files[]`, `tags[]`, `timestamp`, `generatorVersion`

CI Integration (recommended)
- Add a CI job to validate rule files:
  - Check frontmatter presence and required fields
  - Enforce placement under `.cursor/rules/**`
  - Warn on oversize rules (> 500 lines)
  - Optionally run a link check for `mdc:` references

Failure Modes & Safeguards
- No stack detected: default to minimal project conventions and require manual follow-up
- Conflicting signals (e.g., multiple frameworks): prefer source code analysis > `PROJECT-BRIEF.md` > dependency manifests
- Missing brief: proceed using source and manifests; include TODOs in rule comments sparingly
- Use `--dry-run` to preview planned outputs before writing

Usage Examples
1) Frontend-only (React)
   - Inputs detected: `package.json` with `react`, `vite`, `apps/web`
   - Outputs:
     - `.cursor/rules/project-rules/react-app-structure.mdc`
     - `.cursor/rules/project-rules/fullstack-integration-conventions.mdc` (if API present)
   - Notes: includes state management, styling, testing, a11y sections

2) Backend-only (FastAPI)
   - Inputs detected: `pyproject.toml` with `fastapi`, `uvicorn`, `app/`
   - Outputs:
     - `.cursor/rules/project-rules/fastapi-backend-architecture.mdc`
   - Notes: API layering, validation, persistence, auth, observability

When to Run (Unified Workflow)
- Phase 0: Bootstrap & Context Engineering — run to scaffold baseline rules
- Phase 2: Task Generation — re-run after task/architecture finalization
- Phase 5: Retrospective — optionally re-run to fold lessons learned

Usage
- Type `/Generate Cursor Rules` in any `.cursor/commands/` file or run this command to trigger the process.

Triggers
- Keywords: "generate", "cursor rules", "create rules", "rule generation".

Notes
- This command is non-destructive: existing rules are read and augmented; new rules are added under `project-rules/`.
- Prefer evidence from repository files over assumptions. If signals conflict, prioritize `PROJECT-BRIEF.md` then source code.

--- End Command ---


