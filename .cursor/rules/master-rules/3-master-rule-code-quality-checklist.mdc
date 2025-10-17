---
description: "TAGS: [global,quality,development,best-practices] | TRIGGERS: code,develop,refactor,implement,fix,quality | SCOPE: global | DESCRIPTION: A strict checklist for code quality, focusing on robustness, reliability, security, clarity, and adherence to high-level project standards."
alwaysApply: false
---
# Master Rule: Code Quality Checklist

## Section 1: Code Quality (Implementation Checklist)
For any new code or modification, the Agent **MUST** validate every point on this checklist.

### 1.1 Robustness and Reliability
- **[STRICT]** **Error Handling:**
    - Any I/O operation, API call, or parsing action (e.g., `JSON.parse`) **MUST** be wrapped in a `try...catch` block.
    - The `catch` block **MUST** log the error informatively and **MUST NOT** be left empty.
- **[STRICT]** **Input Validation:**
    - Any function exposed to an external source (API, user input) **MUST** begin with a guard-clause block to validate arguments.
    - **NEVER** trust external data.

### 1.2 Simplicity and Clarity
- **[GUIDELINE]** **Single Responsibility Principle (SRP):**
    - A function **SHOULD NOT** exceed 20-30 lines (excluding comments/whitespace). If it does, propose a refactor to break it down into smaller functions.
- **[STRICT]** **Naming Conventions:**
    - Variable and function names **MUST** be explicit (e.g., `userList` instead of `data`).
    - Booleans **MUST** start with a prefix like `is`, `has`, or `can` (e.g., `isUserAdmin`).
- **[GUIDELINE]** **Nesting:**
    - The nesting depth of `if`/`for` blocks **SHOULD NOT** exceed 3 levels. Use guard clauses to reduce complexity.
- **[GUIDELINE]** **Critical Dependencies:**
    - When introducing security-critical dependencies (e.g., DOMPurify, bcrypt libraries), briefly document their purpose in comments or commit messages.

## Section 2: High-Level Project Standards

**[STRICT]** This master rule provides a global quality baseline. However, it **MUST** be complemented by project-specific rules (`project-rules`).

When working within a specific project (e.g., a microservice, a UI application), you **MUST** ensure that any relevant `project-rules` have been loaded by the `context-discovery` protocol. These project rules contain the specific, non-negotiable conventions for that particular codebase (e.g., "All API calls must use the `restApiClient.js` wrapper").

This master rule ensures *how* the code is written; the `project-rules` ensure *what* conventions are followed for a given tech stack.

## Section 3: Examples and Anti-Patterns

<example>
**VALID Error Handling**
```javascript
async function getUser(userId) {
  if (!userId) {
    console.error("User ID is required.");
    return null; // Guard clause
  }
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Failed to fetch user:", error);
    return null;
  }
}
```
</example>

<example type="invalid">
**INVALID Error Handling (too vague)**
```javascript
// AVOID
async function getUser(userId) {
  try {
    const data = await fetch(`/api/users/${userId}`);
    return data.json();
  } catch (e) {
    // This catch is empty or too generic, information is lost
    return null;
  }
}
```
</example>
