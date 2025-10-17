# PROTOCOL: Generic Architecture-Focused Validation (Software Design Compliant)

## Mission
Validate the architectural integrity, module boundaries, and established design patterns in modern software implementations.

## AUDIT FRAMEWORK: LAYER 1 & 4 Validation

### LAYER 1: SOFTWARE DESIGN & ARCHITECTURE COMPLIANCE

**[STRICT] Module & Boundary Validation:**
- Each module/component has a clear and single responsibility.
- Physical separation of apps/modules/libs is respected.
- Consistent terminology is used within the code for core concepts.
- Business logic is encapsulated with the data it operates on (avoids anemic objects).

**[STRICT] Inter-Module/Service Communication:**
- Communication between modules/contexts via well-defined interfaces or contracts ONLY.
- Avoid tight coupling (e.g., direct database access across boundaries).
- A clear entrypoint/API is implemented for each major module/service.
- Correct module/service interaction configuration.

**[STRICT] Common Design Anti-patterns:**
- Direct import between modules/services (isolation violation)
- "God" Objects/Modules holding too many responsibilities.
- Chaotic communication (encapsulation violation)
- Leaking abstraction between component boundaries.

### LAYER 4: ARCHITECTURE & PERFORMANCE

**[MUST VERIFY] Architecture Patterns:**
- Pattern consistency: Implementation follows established patterns.
- SOLID Principles: SRP, OCP, LSP, ISP, DIP.
- Coupling & Cohesion: Appropriate levels of interdependence.
- Abstraction Levels: Proper use of interfaces, inheritance, composition.
- Scalability: Design decisions support future growth.

**[CRITICAL] Application Performance:**
- Minimal application startup time.
- Optimized service/module bundle size.
- Strategic caching.
- Resilience patterns (circuit breaker).

**[MUST VERIFY] Performance & Efficiency:**
- Algorithmic Efficiency: Appropriate time/space complexity.
- Resource Utilization: Efficient use of memory, CPU, I/O.
- Caching Strategy: Proper use of caching where beneficial.
- Database Optimization: Efficient queries, indexing strategies.
- Network Efficiency: Minimal API calls, optimal payload sizes.

**[PERFORMANCE CONCERNS]:**
- N+1 query problems in database interactions.
- Unnecessary API calls or redundant network requests.
- Memory leaks or inefficient data structures.
- Missing pagination for large datasets.
- Blocking operations in asynchronous contexts.

## Audit Process
1.  **Boundary Analysis:** Verify module responsibilities and physical separation.
2.  **Communication Scan:** Check for direct imports or coupling anti-patterns.
3.  **Pattern Review:** Ensure implementation follows established architectural patterns (SOLID, etc.).
4.  **Performance Check:** Analyze bundle size, startup time, and resource utilization. Look for common performance bottlenecks (N+1 queries, etc.).

## Report Format
The report should include a summary of architectural health, a list of any critical design or performance violations found, and prioritized recommendations for improvement.
