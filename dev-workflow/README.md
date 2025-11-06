# The Governor Workflow: From Idea to Production

## 1. Why: A Structured Workflow for Predictable Results

Working with AI can sometimes feel unpredictable. The AI Governor Framework provides a development workflow designed to fix that, for both new and existing projects.

It provides a structured, sequential process that transforms your AI from a simple code generator into a reliable engineering partner. By following these five protocols, you ensure that both you and the AI are always aligned, moving from a high-level idea to a well-implemented feature with clarity, control, and consistency.

The goal is to make AI-powered development:
-   **Predictable:** Each step has a clear purpose and output.
-   **Controllable:** You are always in the loop for key decisions.
-   **Efficient:** The AI does the heavy lifting, you provide the strategic direction.

## 2. How it Works: The Optimized 5-Protocol Development Lifecycle

This workflow guides you through the entire development process, from initial setup to continuous improvement. Each protocol assigns a specific role to the AI, ensuring a structured and predictable collaboration with **intelligent session management**.

### Step 0: Bootstrap Your Project (One-Time Setup)
**Role:** The AI acts as a **Project Analyst**.

First, the AI analyzes your entire codebase to build a "Context Kit"—a set of foundational `READMEs` and project-specific rules. This is a one-time protocol that turns a generic AI into a project-specific expert.

```
Apply instructions from dev-workflow/0-bootstrap-your-project.md
```
*(For best results, Cursor users should use Max Mode for this step.)*

### Step 1: Create a Product Requirements Document (PRD)
**Role:** The AI acts as a **Product Manager**.

Next, you define the "what" and "why" of your feature. The AI interviews you to create a detailed Product Requirements Document (PRD), ensuring all requirements are captured before any code is written.

```
Apply instructions from dev-workflow/1-create-prd.md

Here's the feature I want to build: [Describe your feature in detail]
```
*(For best results, Cursor users should use Max Mode for this step.)*

### Step 2: Generate Your Task List
**Role:** The AI acts as a **Tech Lead**.

The AI then transforms the PRD into a granular, step-by-step technical execution plan. This ensures that both you and the AI are aligned on the implementation strategy.

```
Apply instructions from dev-workflow/2-generate-tasks.md to @prd-my-feature.md
```
*(Note: Replace `@prd-my-feature.md` with the actual filename of your PRD.)*

*(For best results, Cursor users should use Max Mode for this step.)*

### Step 3: Execute Tasks with Integrated Quality Gates
**Role:** The AI acts as a **Paired Developer** with built-in quality validation.

Here, the AI implements the plan one parent task at a time, within a dedicated chat session. Each session includes implementation + quality audit + retrospective for optimal context preservation.

**🔄 Per Parent Task (New Chat Session):**

1.  **Start a parent task in a fresh session:**
    ```
    Apply instructions from dev-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 1.
    ```
    *(Note: Replace `@tasks-my-feature.md` with the actual filename of your task list.)*

2.  **Implementation with Quick Reviews:**
    - AI implements sub-tasks with **integrated quick validation**
    - Critical issues are caught and fixed immediately
    - You review and approve: **"yes"** or **"continue"**

3.  **Protocol 4: Unified Quality Review (Same Session)**
    Once the parent task is complete, use the unified review system by calling the central orchestrator:
    
    **🎯 Tool-Agnostic Command:**
    ```
    Apply instructions from dev-workflow/4-quality-audit.md
    ```
    
    **The orchestrator provides an interactive selection interface:**
    - ☐ **Code Review** - DDD compliance + Code quality (quick feedback)
    - ☐ **🚀 Run All** - Comprehensive 6-layer validation
    - ☐ **Security Check** - Focus on auth/data/multi-tenant validation
    - ☐ **Architecture Review** - Focus on performance + DDD architecture
    - ☐ **Design System** - Component usage + Visual consistency
    - ☐ **UI/UX & Accessibility** - WCAG compliance + Responsive design
    - ☐ **Pre-Production Security** - Complete security validation
    
    **Automatic Fallback:** Custom protocols → Generic protocols (tool-agnostic)

4.  **Protocol 5: Implementation Retrospective (Same Session)**
    Capture learnings while context is fresh:
    ```
    Apply instructions from dev-workflow/5-implementation-retrospective.md
    ```

5.  **Start the next parent task in a new chat:**
    ```
    Apply instructions from dev-workflow/3-process-tasks.md to @tasks-my-feature.md. Start on task 2.
    ```

---

### A Note on the Revolutionary Unified Workflow

This streamlined 5-protocol workflow with a **unified review system** eliminates tool-specific complexity while maintaining all quality benefits. **Key improvements:**

- **Simplified entry point** with a single, central orchestrator
- **Tool-agnostic design** works across Claude Code, Cursor, Aider
- **Context optimization** through intelligent session management  
- **Smart protocol selection** with automatic custom/generic fallback
- **Interactive selection** prevents tool-specific confusion
- **6-layer validation** including Design + UX coverage

**Tool-Specific Usage:**

**Claude Code:** Use the `/review` command for interactive selection.
**Cursor:** Use `@review` for interactive selection.
**Aider:** Use `/load .ai-governor/dev-workflow/4-quality-audit.md`
**Universal:** All tools use the same underlying protocol system.

The initial structured approach pays off exponentially as the AI learns your codebase patterns and becomes a true expert companion for your project with **predictable, high-quality output across any development tool**.
