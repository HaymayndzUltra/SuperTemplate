# PROTOCOL: Generic Quick Review (Software Design Compliant)

## Mission
To perform a quick validation of code quality, craftsmanship, and compliance with core software design principles.

## AUDIT FRAMEWORK: LAYER 1 & 3 Validation

### LAYER 1: SOFTWARE DESIGN COMPLIANCE (Quick Check)

**[STRICT] Module & Boundary Validation:**
- Each module/component has a clear and single responsibility.
- Consistent terminology is used within the code for core concepts.
- Business logic is encapsulated with the data it operates on.

**[STRICT] Inter-Module/Service Communication:**
- Communication between modules/contexts uses well-defined interfaces or contracts.
- Avoids tight coupling (e.g., direct imports that violate module boundaries).

### LAYER 3: CODE QUALITY & CRAFTSMANSHIP

**[STRICT] Master Rules Compliance:**
- Any I/O operation is within a MANDATORY try/catch.
- Variables are explicit (`userList` vs `data`).
- Booleans use prefixes like `is`, `has`, `can`.
- Functions are concise (<30 lines, SRP compliance).
- Nesting is minimal (<3 levels maximum).

**[MUST VERIFY] Code Craftsmanship:**
- **Readability**: Code is self-documenting with clear naming conventions.
- **Structure**: Logical organization and appropriate separation of concerns.
- **Complexity**: Absence of over-engineering or unnecessarily complex solutions.
- **Documentation**: Inline comments explain complex logic.
- **Standards**: Adherence to language-specific conventions.

**[ANTI-PATTERNS] Code Quality:**
- Magic numbers or hard-coded strings without explanation.
- Functions that are too long or complex.
- Inconsistent naming conventions.
- Missing or obsolete documentation.
- Unjustified code duplication.

## Audit Process
1.  **Design Check:** Quickly verify that new code respects module boundaries and uses defined interfaces for communication.
2.  **Quality Scan:** Check for compliance with master rules (error handling, naming, complexity).
3.  **Craftsmanship Review:** Assess readability, structure, and for code smells like magic numbers or duplication.

## Report Format
The report should be concise, focusing on critical violations of code quality and design principles. It should provide clear examples of non-compliant code and specific instructions for remediation.