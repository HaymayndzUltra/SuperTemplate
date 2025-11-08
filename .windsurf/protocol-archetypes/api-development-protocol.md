# Archetype: API Development Protocol

## WHEN TO USE

**Triggers:**
- "API endpoints"
- "REST API"
- "GraphQL API"
- "API implementation"
- "backend API"
- "service endpoints"

**Scenarios:**
- Implementing REST/GraphQL API endpoints
- Building backend services with APIs
- Creating microservice APIs
- Developing API-first applications

**Project Types:**
- Web applications (backend)
- Mobile app backends
- Microservices
- API-as-a-service platforms

---

## STANDARD SECTIONS

### Section 1: Identity & Ownership

```yaml
Protocol ID: {auto_assigned}
Protocol Name: {Technology} API Development
Phase: Implementation
Project: {from_PROJECT_BRIEF}
Version: 1.0
Owner: {from_PROJECT_BRIEF}
Created: {timestamp}
```

**Customization Points:**
- Protocol Name: Include specific technology (e.g., "Go REST API Development")
- Phase: Usually "Implementation" but could be "Core Features" or "Backend Development"

---

### Section 2: AI Role and Mission

```yaml
AI acts as: Backend API Developer
Mission: Implement production-ready API endpoints with {specific_requirements}

Context from Project Brief:
- API Type: {REST | GraphQL | gRPC}
- Technology: {Go | Node.js | Python | etc}
- Database: {PostgreSQL | MySQL | MongoDB | etc}
- Authentication: {JWT | OAuth | Session | etc}
- Performance Target: {response_time_requirement}

Capabilities:
- API endpoint implementation following {framework} conventions
- Request validation and error handling
- Database query optimization
- API documentation generation
- Integration with {specific_services}

Constraints:
- Must follow {API_spec} defined in Protocol {X}
- Must achieve {performance_target}
- Must maintain test coverage ≥{coverage_requirement}
- Must integrate with {existing_services}
```

**Customization Points:**
- Fill from Project Brief: API type, tech stack, database, auth method
- Performance targets from success criteria
- Integration requirements from technical baseline

---

### Section 3: Workflow (Steps)

```yaml
STEP 1: Load API Specification and Requirements
  Input:
    - Protocol {X}: API Design Specification
    - Protocol {Y}: Database Schema
    - .artifacts/protocol-03/PROJECT-BRIEF.md (business requirements)
  
  Process:
    - Review OpenAPI/GraphQL schema specification
    - Identify all endpoints to implement
    - Understand data models and relationships
    - Map business logic requirements to endpoints
  
  Output:
    - Implementation checklist
    - Endpoint priority order
    - Required business logic summary
  
  Validation:
    - [ ] All endpoints identified
    - [ ] Dependencies clear
    - [ ] Business logic understood

STEP 2: Implement Core Endpoint Handlers
  Input:
    - API specification from Step 1
    - Database schema (Protocol {Y})
    - {Framework} project structure
  
  Process:
    - Create endpoint handler functions
    - Implement request validation
    - Add business logic processing
    - Connect to database layer
    - Implement response formatting
  
  Output:
    - Implemented endpoint handlers
    - Request/response validation logic
    - Business logic functions
  
  Validation:
    - [ ] All endpoints callable
    - [ ] Request validation working
    - [ ] Response format matches spec

STEP 3: Implement Error Handling and Logging
  Input:
    - Endpoint handlers from Step 2
    - Error handling patterns from project structure
  
  Process:
    - Add try-catch/error handling to all endpoints
    - Implement standardized error responses
    - Add structured logging
    - Handle edge cases and invalid inputs
    - Add request tracing (if required)
  
  Output:
    - Comprehensive error handling
    - Structured logs
    - Error response standardization
  
  Validation:
    - [ ] All errors caught and handled
    - [ ] Error responses standardized
    - [ ] Logs structured and queryable

STEP 4: Implement Authentication and Authorization
  Input:
    - Auth specification (Protocol {X})
    - Endpoint handlers from Step 2
  
  Process:
    - Add authentication middleware
    - Implement token validation
    - Add authorization checks (RBAC if needed)
    - Secure sensitive endpoints
    - Add rate limiting (if required)
  
  Output:
    - Authentication middleware
    - Authorization logic
    - Secured endpoints
  
  Validation:
    - [ ] Auth working on all protected endpoints
    - [ ] Unauthorized requests rejected
    - [ ] Rate limiting operational (if applicable)

STEP 5: Write Unit and Integration Tests
  Input:
    - Implemented endpoints from Steps 2-4
    - Test framework setup
  
  Process:
    - Write unit tests for business logic
    - Write integration tests for endpoints
    - Test error handling paths
    - Test authentication/authorization
    - Measure test coverage
  
  Output:
    - Unit test suite
    - Integration test suite
    - Test coverage report
  
  Validation:
    - [ ] Test coverage ≥{coverage_requirement}
    - [ ] All critical paths tested
    - [ ] All tests passing

STEP 6: Optimize Performance
  Input:
    - Working endpoints from Steps 2-5
    - Performance requirements from Project Brief
  
  Process:
    - Profile API response times
    - Optimize database queries (N+1, indexes)
    - Add caching where appropriate
    - Optimize payload sizes
    - Run load tests
  
  Output:
    - Performance profiling report
    - Optimized endpoints
    - Load test results
  
  Validation:
    - [ ] Response times meet targets
    - [ ] No performance bottlenecks
    - [ ] Load tests passing

STEP 7: Generate API Documentation
  Input:
    - Implemented endpoints from Steps 2-6
    - API specification
  
  Process:
    - Generate API documentation from code/spec
    - Add usage examples
    - Document error responses
    - Add authentication guide
    - Create postman/curl examples
  
  Output:
    - API documentation (Swagger/Redoc/GraphQL Playground)
    - Usage examples
    - Integration guide
  
  Validation:
    - [ ] All endpoints documented
    - [ ] Examples working
    - [ ] Documentation accessible
```

**Customization Points:**
- Protocol references (X, Y) filled from dependency analysis
- Framework-specific implementation details
- Test coverage requirement from Project Brief
- Performance targets from success criteria

---

### Section 4: Quality Gates

```yaml
Gate 1: All Endpoints Operational
  Type: boolean
  Blocking: true
  Measurement: Manual testing + automated tests
  Threshold: 100% of specified endpoints working
  Context: {count} endpoints from API spec must be implemented

Gate 2: Test Coverage ≥{target}
  Type: percentage
  Blocking: true
  Measurement: Coverage tool (go test -cover, jest --coverage, pytest-cov)
  Threshold: ≥{coverage_requirement}% overall, ≥{critical_coverage}% critical paths
  Context: From Project Brief success criteria

Gate 3: API Response Time {operator} {threshold}
  Type: numeric
  Blocking: true
  Measurement: Load testing tool (k6, Artillery, Apache Bench)
  Threshold: p95 {threshold}ms, p99 {threshold2}ms
  Context: Performance requirement from Project Brief

Gate 4: Security Scan Passed
  Type: boolean
  Blocking: true
  Measurement: Security scanner (gosec, bandit, npm audit)
  Threshold: Zero critical/high vulnerabilities
  Context: Security compliance requirement

Gate 5: API Documentation Complete
  Type: boolean
  Blocking: false
  Measurement: Manual review
  Threshold: All endpoints documented with examples
  Context: Documentation deliverable requirement
```

**Customization Points:**
- Coverage targets from Project Brief (e.g., ≥80%)
- Performance thresholds from success criteria (e.g., p95 <200ms)
- Endpoint count from API specification
- Security requirements from compliance needs

---

### Section 5: Automation Hooks

```yaml
Script: implement_api_handlers.py (NEW)
Purpose: Generate boilerplate endpoint handlers from OpenAPI spec
Location: scripts/api/implement_api_handlers.py
Inputs: 
  - OpenAPI specification file
  - Target language/framework
Outputs:
  - Generated handler stubs
  - Request/response models
Registry: scripts/script-registry.json

Script: generate_api_tests.py (NEW)
Purpose: Generate test templates for all API endpoints
Location: scripts/testing/generate_api_tests.py
Inputs:
  - OpenAPI specification
  - Test framework
Outputs:
  - Test file templates
  - Mock data generators
Registry: scripts/script-registry.json

Script: measure_api_performance.py (NEW)
Purpose: Run load tests and measure API performance
Location: scripts/performance/measure_api_performance.py
Inputs:
  - API base URL
  - Endpoint list
  - Load profile
Outputs:
  - Performance report (p50, p95, p99)
  - Bottleneck identification
  - .artifacts/protocol-{ID}/performance-report.json
Registry: scripts/script-registry.json

Script: validate_api_coverage.py (NEW)
Purpose: Measure test coverage and identify gaps
Location: scripts/testing/validate_api_coverage.py
Inputs:
  - Source code directory
  - Test directory
Outputs:
  - Coverage report
  - Gap analysis
  - .artifacts/protocol-{ID}/coverage-report.json
Registry: scripts/script-registry.json

Script: generate_api_docs.py (REUSE)
Purpose: Generate API documentation from code/spec
Location: scripts/documentation/generate_api_docs.py
Inputs:
  - OpenAPI spec or code annotations
  - Documentation format
Outputs:
  - HTML/Markdown documentation
  - .artifacts/protocol-{ID}/api-docs/
Registry: scripts/script-registry.json
```

**Customization Points:**
- Script language based on project tech stack
- Framework-specific implementations
- Tool selection based on ecosystem

---

### Section 6: Evidence Summary

```yaml
Artifacts Required:
- .artifacts/protocol-{ID}/api-implementation-checklist.md
- .artifacts/protocol-{ID}/endpoint-test-results.json
- .artifacts/protocol-{ID}/coverage-report.json
- .artifacts/protocol-{ID}/performance-report.json
- .artifacts/protocol-{ID}/api-docs/ (directory)
- .artifacts/protocol-{ID}/security-scan-report.json
- .artifacts/protocol-{ID}/implementation-summary.md

Artifact Types:
- Documentation: Implementation checklist, summary, API docs
- Metrics: Test coverage, performance benchmarks, security scan
- Configuration: N/A
- Reports: Test results, performance analysis
```

**Customization Points:**
- Artifact paths use actual protocol ID
- Additional artifacts based on project requirements

---

### Section 7: Integration Points

```yaml
Input From: Protocol {X} (API Design & Specification)
  Data: OpenAPI/GraphQL schema, endpoint definitions, auth requirements
  Format: OpenAPI 3.0 YAML/JSON or GraphQL Schema Definition
  Location: .artifacts/protocol-{X}/api-specification.yaml

Input From: Protocol {Y} (Database Schema Design)
  Data: Database schema, table definitions, relationships
  Format: SQL DDL or ORM models
  Location: .artifacts/protocol-{Y}/schema.sql

Input From: Protocol {Z} (Authentication Implementation)
  Data: Auth middleware, token validation logic
  Format: Code library/module
  Location: src/middleware/auth.{ext}

Output To: Protocol {N} (Frontend Integration)
  Data: Working API endpoints, API documentation
  Format: HTTP endpoints + OpenAPI spec
  Location: .artifacts/protocol-{ID}/api-docs/

Output To: Protocol {M} (Integration Testing)
  Data: Implemented endpoints, test data
  Format: Running API + test fixtures
  Location: .artifacts/protocol-{ID}/

Dependencies:
- {Database}: Connection string, credentials
- {Auth Provider}: API keys, configuration
- {External APIs}: API keys, endpoints
- {Cache}: Redis/Memcached connection (if applicable)
```

**Customization Points:**
- Protocol IDs from dependency analysis
- Specific integrations from Project Brief
- File extensions based on language
- External dependencies from technical baseline

---

### Section 8: Communication Protocols

```yaml
Status Announcements:
[PROTOCOL {ID} | API DEVELOPMENT START]
[STEP 2 COMPLETE: {count} Endpoints Implemented]
[STEP 5 COMPLETE: Test Coverage {percentage}%]
[QUALITY GATE PASSED: Performance p95 {time}ms]
[QUALITY GATE PASSED: Test Coverage ≥{target}%]
[PROTOCOL {ID} | API DEVELOPMENT COMPLETE]

Progress Announcements:
[MILESTONE: Core CRUD Endpoints Complete]
[MILESTONE: Authentication Integrated]
[MILESTONE: All Tests Passing]

Error Announcements:
[PROTOCOL {ID} | GATE 2 FAILED: Test coverage {actual}% < {required}%]
[PROTOCOL {ID} | GATE 3 FAILED: Performance p95 {actual}ms > {threshold}ms]
[PROTOCOL {ID} | BLOCKED: Database connection unavailable]
```

**Customization Points:**
- Protocol ID filled dynamically
- Count, percentage, time values from actual measurements
- Thresholds from quality gates

---

### Section 9: Handoff Checklist

```yaml
Pre-handoff Validation:
[ ] All quality gates passed
[ ] All {count} endpoints implemented and tested
[ ] Test coverage ≥{requirement}% verified
[ ] Performance benchmarks met (p95 <{threshold}ms)
[ ] Security scan passed (zero critical issues)
[ ] API documentation generated and accessible
[ ] Error handling comprehensive
[ ] Authentication/authorization working

Handoff Deliverables:
[ ] Working API endpoints (deployed to {environment})
[ ] API documentation (.artifacts/protocol-{ID}/api-docs/)
[ ] Test suite (unit + integration)
[ ] Coverage report (.artifacts/protocol-{ID}/coverage-report.json)
[ ] Performance report (.artifacts/protocol-{ID}/performance-report.json)
[ ] Security scan report (.artifacts/protocol-{ID}/security-scan-report.json)
[ ] Implementation summary (.artifacts/protocol-{ID}/implementation-summary.md)
[ ] Integration guide for frontend/consumers

Technical Debt (If Any):
[ ] {debt_item_1} - Severity: {Low|Medium|High} - Plan: {remediation_plan}
[ ] {debt_item_2} - Severity: {Low|Medium|High} - Plan: {remediation_plan}
```

**Customization Points:**
- Endpoint count from specification
- Requirements from quality gates
- Environment from deployment strategy
- Actual protocol ID

---

### Section 10: Reasoning & Reflection

```yaml
Decision Logic:

Decision: API Framework Selection
  Context: {Framework} chosen for {reasons_from_project_brief}
  Reasoning: 
    - Aligns with team expertise
    - Performance characteristics meet requirements
    - Ecosystem maturity and library availability
    - Community support and documentation
  
Decision: Error Handling Strategy
  Context: Standardized error responses across all endpoints
  Reasoning:
    - Consistent client experience
    - Easier debugging and monitoring
    - Follows REST/GraphQL best practices
    - Supports internationalization if needed
  
Decision: Authentication Approach
  Context: {JWT | OAuth | Session} selected
  Reasoning:
    - Matches requirements from API Design protocol
    - Scalability considerations
    - Security requirements met
    - Integration with frontend/mobile apps

Decision: Performance Optimization Techniques
  Context: {Techniques applied}
  Reasoning:
    - Database query optimization (indexes, N+1 prevention)
    - Caching strategy ({Redis | in-memory | CDN})
    - Response payload optimization
    - Connection pooling configuration

Continuous Improvement:

Lessons Learned:
- {What worked well during implementation}
- {What challenges were encountered}
- {What would be done differently}

Optimization Opportunities:
- {Potential performance improvements}
- {Code refactoring opportunities}
- {Additional testing scenarios}

Technical Debt:
- {Known shortcuts or temporary solutions}
- {Missing features or edge cases}
- {Refactoring needs}
```

**Customization Points:**
- Framework name and reasoning from Project Brief
- Authentication method from technical baseline
- Caching strategy from infrastructure decisions
- Actual lessons learned during implementation

---

## CUSTOMIZATION GUIDE

### 1. Technology-Specific Adaptation

**For Go:**
- Framework: gorilla/mux, gin, echo, fiber
- Testing: testing package + testify
- Coverage: go test -cover
- Performance: pprof, go-bench

**For Node.js:**
- Framework: Express, Fastify, NestJS, Koa
- Testing: Jest, Mocha, Supertest
- Coverage: Istanbul/nyc, Jest --coverage
- Performance: clinic.js, autocannon

**For Python:**
- Framework: FastAPI, Flask, Django REST
- Testing: pytest, unittest
- Coverage: pytest-cov, coverage.py
- Performance: locust, py-spy

**For Java:**
- Framework: Spring Boot, Micronaut, Quarkus
- Testing: JUnit, Mockito, RestAssured
- Coverage: JaCoCo, Cobertura
- Performance: JMeter, Gatling

### 2. API Type Adaptation

**REST API:**
- OpenAPI/Swagger specification
- HTTP verbs (GET, POST, PUT, DELETE)
- Status codes (200, 201, 400, 404, 500)
- Resource-based routing

**GraphQL API:**
- GraphQL schema definition
- Resolvers and data loaders
- Query, Mutation, Subscription
- GraphQL Playground/GraphiQL

**gRPC API:**
- Protocol Buffers definition
- Service implementation
- Streaming support
- gRPC health checks

### 3. Scale Adaptation

**Simple API (< 10 endpoints):**
- Lightweight implementation
- Basic testing
- Simple documentation

**Medium API (10-50 endpoints):**
- Modular structure
- Comprehensive testing
- Detailed documentation
- Performance monitoring

**Large API (50+ endpoints):**
- Microservices architecture
- Advanced testing strategies
- API versioning
- Extensive monitoring and observability

---

## EXAMPLES

### Example 1: Go REST API for SaaS Platform

```yaml
Protocol Name: Go REST API Development
Context: Go 1.21+, PostgreSQL, JWT auth, p95 <200ms target
Quality Gates:
  - 15 endpoints operational
  - Test coverage ≥80%
  - p95 <200ms, p99 <500ms
  - Zero critical vulnerabilities
Automation:
  - implement_api_handlers.py (generates gorilla/mux handlers)
  - generate_api_tests.py (generates testify test suites)
  - measure_api_performance.py (k6 load testing)
```

### Example 2: Node.js GraphQL API for Mobile Backend

```yaml
Protocol Name: Node.js GraphQL API Development
Context: Node.js 18+, MongoDB, OAuth, mobile client support
Quality Gates:
  - All queries and mutations operational
  - Test coverage ≥85%
  - Query response <100ms
  - Security scan passed
Automation:
  - generate_graphql_resolvers.py
  - generate_apollo_tests.py
  - measure_graphql_performance.py
```

### Example 3: Python FastAPI for Data Platform

```yaml
Protocol Name: Python FastAPI Development
Context: FastAPI, PostgreSQL, async endpoints, data processing
Quality Gates:
  - 25 endpoints operational
  - Test coverage ≥90%
  - Async processing working
  - API docs complete
Automation:
  - implement_fastapi_handlers.py
  - generate_pytest_tests.py
  - measure_fastapi_performance.py
```

---

## VALIDATION CHECKLIST FOR THIS ARCHETYPE

When using this archetype, verify:

✅ **Technology Correctly Identified** - Language, framework, database
✅ **API Type Clear** - REST, GraphQL, or gRPC
✅ **Performance Targets Specified** - From Project Brief success criteria
✅ **Test Coverage Requirements** - From Project Brief quality targets
✅ **Authentication Method** - From API Design protocol
✅ **Integration Points Mapped** - Database, auth, external services
✅ **Automation Scripts Adapted** - Language and framework specific
✅ **Quality Gates Measurable** - Specific thresholds defined

---

**Archetype Version:** 1.0
**Last Updated:** 2025-11-07
**Applicable To:** Backend API development across all tech stacks
**Dependencies:** API Design Protocol, Database Schema Protocol
**Status:** Active

