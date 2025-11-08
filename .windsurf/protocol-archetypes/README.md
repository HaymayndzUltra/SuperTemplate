# Protocol Archetype Library

## OVERVIEW

Protocol archetypes are **reusable templates** for common protocol patterns. Instead of creating every protocol from scratch, the Protocol Generation Workflow selects and customizes the appropriate archetype based on project requirements.

**Key Principle:** Archetypes provide structure, Project Brief provides specificity.

---

## HOW ARCHETYPES WORK

### 1. Archetype Selection
When analyzing a Project Brief, the AI matches project requirements to appropriate archetypes:

```
Project Brief mentions: "PostgreSQL database schema"
  → Selects: database-migration-protocol.md

Project Brief mentions: "Stripe payment integration"
  → Selects: payment-integration-protocol.md

Project Brief mentions: "REST API endpoints"
  → Selects: api-development-protocol.md
```

### 2. Customization
The archetype provides:
- ✅ Standard section structure
- ✅ Common workflow steps
- ✅ Typical quality gates
- ✅ Standard automation scripts

The Project Brief provides:
- ✅ Specific technology choices
- ✅ Project-specific requirements
- ✅ Custom success criteria
- ✅ Integration context

### 3. Output
Result = Archetype Template + Project Context = **Protocol**

---

## ARCHETYPE CATALOG

### 🏗️ ARCHITECTURE & DESIGN

#### `api-design-protocol.md`
**When to Use:** RESTful API, GraphQL API, gRPC service design
**Triggers:** "API", "REST", "GraphQL", "endpoints", "OpenAPI"
**Provides:**
- API specification structure
- Authentication design
- Endpoint documentation format
- Request/response schema patterns

---

#### `database-migration-protocol.md`
**When to Use:** Database schema design, migrations, data modeling
**Triggers:** "database", "schema", "migration", "PostgreSQL", "MySQL", "MongoDB"
**Provides:**
- Schema design workflow
- Migration script structure
- Index strategy
- Normalization guidelines

---

#### `frontend-architecture-protocol.md`
**When to Use:** Frontend application structure, component design
**Triggers:** "frontend", "UI", "React", "Next.js", "Vue", "Angular"
**Provides:**
- Component architecture
- State management patterns
- Routing structure
- Styling conventions

---

### 💻 IMPLEMENTATION

#### `backend-development-protocol.md`
**When to Use:** Backend service implementation
**Triggers:** "backend", "server", "API implementation", "business logic"
**Provides:**
- Service layer structure
- Error handling patterns
- Logging conventions
- Testing strategy

---

#### `frontend-development-protocol.md`
**When to Use:** Frontend application implementation
**Triggers:** "frontend implementation", "UI development", "components"
**Provides:**
- Component development workflow
- State management implementation
- API integration patterns
- Responsive design approach

---

#### `mobile-development-protocol.md`
**When to Use:** Mobile app development (iOS, Android, React Native, Flutter)
**Triggers:** "mobile", "iOS", "Android", "React Native", "Flutter"
**Provides:**
- Platform-specific considerations
- Native module integration
- App store deployment
- Mobile testing strategies

---

### 🔌 INTEGRATIONS

#### `payment-integration-protocol.md`
**When to Use:** Payment gateway integration (Stripe, PayPal, etc.)
**Triggers:** "payment", "Stripe", "PayPal", "checkout", "billing"
**Provides:**
- Payment flow implementation
- Webhook handling
- Transaction management
- Error recovery patterns

---

#### `storage-integration-protocol.md`
**When to Use:** Cloud storage integration (S3, GCS, Azure Blob)
**Triggers:** "storage", "S3", "file upload", "cloud storage"
**Provides:**
- Upload/download workflows
- Signed URL generation
- Access control patterns
- CDN integration

---

#### `authentication-protocol.md`
**When to Use:** Authentication and authorization implementation
**Triggers:** "auth", "authentication", "JWT", "OAuth", "session"
**Provides:**
- Auth flow implementation
- Token management
- Session handling
- Role-based access control

---

#### `queue-integration-protocol.md`
**When to Use:** Message queue integration (SQS, RabbitMQ, Kafka)
**Triggers:** "queue", "SQS", "message", "async processing"
**Provides:**
- Queue setup
- Message handling patterns
- Retry logic
- Dead letter queues

---

#### `caching-protocol.md`
**When to Use:** Caching layer implementation (Redis, Memcached)
**Triggers:** "cache", "Redis", "Memcached", "caching"
**Provides:**
- Cache strategy
- Invalidation patterns
- TTL management
- Cache warming

---

### ⚡ PERFORMANCE & OPTIMIZATION

#### `performance-tuning-protocol.md`
**When to Use:** Performance profiling and optimization
**Triggers:** "performance", "optimization", "latency", "response time"
**Provides:**
- Profiling methodology
- Bottleneck identification
- Optimization strategies
- Benchmark framework

---

#### `load-testing-protocol.md`
**When to Use:** Load and stress testing
**Triggers:** "load testing", "stress test", "scalability"
**Provides:**
- Test scenario design
- Load testing tools setup
- Metrics collection
- Analysis framework

---

### 🔒 SECURITY & COMPLIANCE

#### `security-audit-protocol.md`
**When to Use:** Security assessment and vulnerability scanning
**Triggers:** "security", "OWASP", "vulnerabilities", "audit"
**Provides:**
- Security scanning workflow
- OWASP Top 10 checklist
- Vulnerability remediation
- Security testing patterns

---

#### `compliance-protocol.md`
**When to Use:** Regulatory compliance (GDPR, HIPAA, SOC2)
**Triggers:** "compliance", "GDPR", "HIPAA", "SOC2", "audit"
**Provides:**
- Compliance checklist
- Documentation requirements
- Audit trail implementation
- Data privacy patterns

---

### 🧪 TESTING & QUALITY

#### `unit-testing-protocol.md`
**When to Use:** Unit test implementation
**Triggers:** "unit tests", "test coverage", "TDD"
**Provides:**
- Test structure patterns
- Mocking strategies
- Coverage targets
- Test naming conventions

---

#### `integration-testing-protocol.md`
**When to Use:** Integration test implementation
**Triggers:** "integration tests", "API tests", "contract tests"
**Provides:**
- Integration test patterns
- Test database setup
- API contract testing
- Service mocking

---

#### `e2e-testing-protocol.md`
**When to Use:** End-to-end test implementation
**Triggers:** "E2E", "Cypress", "Playwright", "Selenium"
**Provides:**
- E2E test framework setup
- Test scenario design
- Page object patterns
- Flaky test prevention

---

#### `test-coverage-protocol.md`
**When to Use:** Test coverage measurement and improvement
**Triggers:** "test coverage", "coverage report", "coverage target"
**Provides:**
- Coverage measurement
- Gap identification
- Coverage improvement strategy
- Quality gates

---

### 🚀 DEPLOYMENT & OPERATIONS

#### `cicd-setup-protocol.md`
**When to Use:** CI/CD pipeline implementation
**Triggers:** "CI/CD", "GitHub Actions", "pipeline", "automation"
**Provides:**
- Pipeline architecture
- Build automation
- Test automation
- Deployment automation

---

#### `deployment-protocol.md`
**When to Use:** Production deployment
**Triggers:** "deployment", "production", "release", "rollout"
**Provides:**
- Deployment checklist
- Rollback procedures
- Health checks
- Smoke tests

---

#### `monitoring-protocol.md`
**When to Use:** Monitoring and observability setup
**Triggers:** "monitoring", "observability", "metrics", "logging"
**Provides:**
- Metrics collection
- Log aggregation
- Alert configuration
- Dashboard design

---

#### `incident-response-protocol.md`
**When to Use:** Incident management and rollback
**Triggers:** "incident", "rollback", "emergency", "outage"
**Provides:**
- Incident detection
- Response procedures
- Communication plan
- Post-mortem structure

---

### 📚 DOCUMENTATION

#### `documentation-protocol.md`
**When to Use:** Documentation creation and maintenance
**Triggers:** "documentation", "API docs", "deployment guide"
**Provides:**
- Documentation structure
- API documentation format
- Runbook templates
- Knowledge base organization

---

### 🤖 AI/ML SPECIFIC

#### `ai-data-collection-protocol.md`
**When to Use:** ML data collection and ingestion
**Triggers:** "data collection", "dataset", "data ingestion", "ML data"
**Provides:**
- Data source identification
- Collection automation
- Data storage strategy
- Data profiling

---

#### `ai-model-training-protocol.md`
**When to Use:** ML model training and tuning
**Triggers:** "model training", "hyperparameter tuning", "ML training"
**Provides:**
- Training pipeline setup
- Hyperparameter optimization
- Experiment tracking
- Model versioning

---

#### `ai-model-deployment-protocol.md`
**When to Use:** ML model deployment and serving
**Triggers:** "model deployment", "model serving", "inference"
**Provides:**
- Model packaging
- Serving infrastructure
- API endpoint design
- Model monitoring

---

## ARCHETYPE STRUCTURE

Each archetype file follows this structure:

```markdown
# Archetype: {Name}

## WHEN TO USE
{Triggers and scenarios}

## STANDARD SECTIONS

### Section 1: Identity & Ownership
{Common patterns}

### Section 2: AI Role and Mission
{Typical roles for this protocol type}

### Section 3: Workflow (Steps)
{Standard steps - customize with project context}

### Section 4: Quality Gates
{Common quality gates for this type}

### Section 5: Automation Hooks
{Typical automation scripts needed}

### Section 6: Evidence Summary
{Standard artifacts for this protocol type}

### Section 7: Integration Points
{Common input/output patterns}

### Section 8: Communication Protocols
{Standard announcements}

### Section 9: Handoff Checklist
{Common checklist items}

### Section 10: Reasoning & Reflection
{Decision frameworks for this protocol type}

## CUSTOMIZATION GUIDE
{How to adapt this archetype to specific projects}

## EXAMPLES
{Real-world examples of this protocol type}
```

---

## CREATING NEW ARCHETYPES

When you identify a recurring protocol pattern:

1. **Identify the Pattern**
   - Used in 3+ projects
   - Clear trigger keywords
   - Reusable structure

2. **Extract Common Elements**
   - Standard workflow steps
   - Typical quality gates
   - Common automation scripts

3. **Document Customization Points**
   - What varies by project?
   - What needs Project Brief context?
   - What can be standardized?

4. **Create Archetype File**
   - Follow standard structure
   - Include examples
   - Document triggers

5. **Update Mapping Rules**
   - Add to mapping-rules.json
   - Define trigger keywords
   - Specify dependencies

---

## ARCHETYPE QUALITY CHECKLIST

✅ **Clear Triggers** - Obvious when to use this archetype
✅ **Complete Structure** - All 10 sections covered
✅ **Customization Guide** - How to adapt to projects
✅ **Examples** - Real-world usage examples
✅ **Dependencies** - Integration patterns documented
✅ **Quality Gates** - Measurable success criteria
✅ **Automation** - Standard scripts identified

---

## USAGE EXAMPLE

### Project Brief Contains:
```
"Implement Stripe payment processing with webhook handling
for subscription billing in the Go backend."
```

### AI Analysis:
```
Triggers detected: "Stripe", "payment", "webhook", "subscription"
Archetype selected: payment-integration-protocol.md
```

### Customization:
```
Archetype provides:
- Payment flow structure
- Webhook handling pattern
- Error recovery approach

Project Brief provides:
- Technology: Go
- Use case: Subscription billing
- Integration: Backend service

Result: Protocol 10 - Stripe Subscription Integration
```

---

## ARCHETYPE LIBRARY EVOLUTION

The archetype library should grow based on:
- New project types encountered
- Emerging technology patterns
- User feedback
- Protocol creation retrospectives

**Add new archetypes when:**
- Same protocol pattern needed 3+ times
- New technology category emerges
- Complex pattern becomes standardized
- User explicitly requests archetype

---

**Library Version:** 1.0
**Last Updated:** 2025-11-07
**Total Archetypes:** 25+
**Status:** Active

