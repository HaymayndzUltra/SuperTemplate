# PROTOCOL: Generic Deep Security Audit (Software Design Compliant)

## Mission
To conduct a comprehensive security and production-readiness audit, focusing on deep security validation, testing coverage, and overall system maintainability.

## AUDIT FRAMEWORK: LAYER 2 & 7 Validation

### LAYER 2: SECURITY & MULTI-TENANT ASSURANCE (Deep Dive)

**[STRICT] Module/Boundary Security:**
- Each module/component manages its own authentication where applicable.
- Secrets are isolated by functional area.
- Input validation occurs at each module/component boundary.
- Secure error handling is compliant with Master Rules.

**[CRITICAL] Multi-Tenant Data Protection:**
- MANDATORY data access policies (e.g., RLS) for all tenant tables.
- `tenant_id` validation is performed at each database operation.
- No data leakage between tenants.
- A complete audit trail of cross-tenant access exists.

**[CRITICAL] Security Audit Points:**
- SQL injection in database queries.
- Cross-Site Scripting (XSS) in user-generated content.
- Missing input validation.
- Authentication/authorization bypass vulnerabilities.
- Exposure of secrets in logs or error messages.
- Overly permissive CORS policies.
- Missing security headers.

**[STRICT] Secure Communication:**
- Service entrypoints have access validation.
- RPC methods are secure (stateless, validated).
- Service configuration does not expose secrets.
- Environment variables are correctly scoped.

### LAYER 7: TESTING & MAINTAINABILITY

**[MUST VERIFY] Testing Coverage:**
- Unit tests for critical business logic.
- Integration tests for inter-module/service communication.
- End-to-end tests for complete user workflows.
- Security tests covering common vulnerabilities (e.g., OWASP Top 10).
- Performance tests for critical endpoints.

**[MUST VERIFY] Code Organization & Maintainability:**
- Clear modular structure.
- Well-managed dependencies (no known vulnerabilities).
- Organized and secure configuration files.
- Up-to-date architecture documentation.
- Appropriate monitoring and logging in place.
- Defined and tested rollback strategies for deployments.

## Audit Process
1.  **Deep Security Scan:** Perform all checks from the standard `security-check` protocol.
2.  **Testing Coverage Analysis:** Review test suites to ensure critical paths, security concerns, and integration points are adequately covered.
3.  **Maintainability Review:** Inspect code organization, documentation, and operational readiness (logging, monitoring, rollback).
4.  **Dependency Audit:** Scan all project dependencies for known vulnerabilities.

## Report Format
The report will be a comprehensive assessment of production-readiness. It will include all findings from the standard security audit, plus a detailed analysis of test coverage and maintainability risks.