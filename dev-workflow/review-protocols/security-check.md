# PROTOCOL: Generic Security-Focused Audit (Software Design Compliant)

## Mission
To perform a focused security audit, validating data protection, secure communication patterns, and multi-tenancy safeguards.

## AUDIT FRAMEWORK: LAYER 2 Validation

### LAYER 2: SECURITY & MULTI-TENANT ASSURANCE

**[STRICT] Module/Boundary Security:**
- Each module/component manages its own authentication where applicable.
- Secrets are isolated by functional area (violation if shared inappropriately).
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
- Overly permissive Cross-Origin Resource Sharing (CORS) policies.
- Missing security headers.

**[STRICT] Secure Communication:**
- Service entrypoints have access validation.
- RPC methods are secure (stateless, validated).
- Service configuration does not expose secrets.
- Environment variables are correctly scoped.

## Audit Process
1.  **Boundary Security Check:** Verify secret isolation and input validation at module boundaries.
2.  **Data Protection Scan:** Check for mandatory RLS policies and `tenant_id` usage in all database operations.
3.  **Vulnerability Scan:** Look for common vulnerabilities like SQL injection, XSS, and auth bypass patterns.
4.  **Communication Security:** Review service entrypoints and configurations for potential security leaks.

## Report Format
The report must highlight critical security vulnerabilities with clear, actionable remediation steps. It should classify findings by severity and provide specific code examples for fixes.