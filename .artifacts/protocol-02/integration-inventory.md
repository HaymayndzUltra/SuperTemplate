---
status: draft
last_updated: 2025-11-06T05:40:00Z
prepared_by: Discovery Lead
protocol_id: "02"
---

# Integration & Dependency Inventory

## Integration Summary

| System | Purpose | Owner | Data Availability | Risk | Next Action |
|--------|---------|-------|-------------------|------|-------------|
| OpenAI API | AI-powered features (chat/embeddings) | @ASK_CLIENT | @ASK_CLIENT (API keys?) | **HIGH** - Blocks Week 1 | Q-TECH-002 (credentials) |
| Stripe | Billing, subscriptions, webhooks | @ASK_CLIENT | @ASK_CLIENT (account access?) | **HIGH** - Blocks Week 3 | Q-TECH-002 (account details) |
| PostgreSQL | User data, subscriptions, billing records | @ASK_CLIENT | @ASK_CLIENT (schema/ERD?) | **MEDIUM** - Affects architecture | Q-TECH-004 (schema review) |
| FastAPI Backend | Core application framework | @ASK_CLIENT | @ASK_CLIENT (repo access?) | **HIGH** - Blocks Day 1 | Q-TECH-003 (repo access) |
| Next.js Frontend | User interface (optional) | @ASK_CLIENT | @ASK_CLIENT | **LOW** - Post-MVP | Q-TECH-006 (scope clarification) |
| GitHub | Code collaboration & version control | @ASK_CLIENT | @ASK_CLIENT (repo invite?) | **HIGH** - Blocks Day 1 | GAP-003 (access request) |
| Discord | Daily communication & updates | @ASK_CLIENT | @ASK_CLIENT (server invite?) | **HIGH** - Blocks communication | GAP-004 (server invite) |
| [TBD] Email/SMS Service | Notifications (if needed) | @ASK_CLIENT | @ASK_CLIENT | **UNKNOWN** | Q-INT-001 (dependency discovery) |
| [TBD] Monitoring Tool | Error tracking, observability (optional) | @ASK_CLIENT | @ASK_CLIENT | **LOW** - Post-MVP | Q-TECH-005 (monitoring discussion) |

## Detailed Integration Specifications

### INT-001: OpenAI API

**System Information:**
- **Type:** External REST API
- **Documentation:** https://platform.openai.com/docs/api-reference
- **Environment:** @ASK_CLIENT (test/production API keys)
- **Authentication:** Bearer token (API key)

**Integration Requirements:**
- **Endpoints Needed:** @ASK_CLIENT (via Q-BUS-002, Q-TECH-001)
  - Likely: `/v1/chat/completions` for chat-based AI
  - Possible: `/v1/embeddings` for semantic search
  - Unknown: Assistants API, Fine-tuning, etc.
- **Data Flow:** User request → FastAPI → OpenAI API → Response parsing → Database storage (?)
- **Rate Limits:** @ASK_CLIENT (plan tier, quota management strategy)
- **Error Handling:** Timeout management, rate limit retries, malformed response handling

**Access Requirements:**
- **Credentials:** OpenAI API key (test + production)
- **Owner:** @ASK_CLIENT (via Q-INT-002)
- **Secrets Management:** @ASK_CLIENT (env vars, AWS Secrets Manager, etc.)

**Data Mapping:**
- **Input:** User prompt/query from frontend → FastAPI request body
- **Output:** OpenAI response → Parsed content → @ASK_CLIENT (stored where?)
- **Logging:** @ASK_CLIENT (log requests/responses for debugging?)

**Risk Indicators:**
- ⚠️ No API key access → **BLOCKER** for Week 1 development
- ⚠️ Unclear endpoint scope → May build wrong features
- ⚠️ Rate limit unknown → Cannot design retry logic appropriately

**Linked Questions:** Q-BUS-002, Q-TECH-001, Q-TECH-002, Q-TECH-005

---

### INT-002: Stripe Billing

**System Information:**
- **Type:** External REST API + Webhooks
- **Documentation:** https://stripe.com/docs/api
- **Environment:** @ASK_CLIENT (test mode vs. production account)
- **Authentication:** Bearer token (API secret key) + Webhook signing secret

**Integration Requirements:**
- **Endpoints Needed:**
  - `/v1/customers` - Customer management
  - `/v1/subscriptions` - Subscription lifecycle
  - `/v1/checkout/sessions` - Payment flow (if applicable)
  - Webhooks: @ASK_CLIENT (which events?) via Q-USER-002
    - Likely: `invoice.paid`, `invoice.payment_failed`, `customer.subscription.updated`, `customer.subscription.deleted`
- **Data Flow:**
  - Outbound: FastAPI → Stripe API (create subscription, update customer)
  - Inbound: Stripe → Webhook endpoint → Event processing → Database update
- **Webhook Signature Validation:** **CRITICAL** - Must verify Stripe signatures to prevent spoofing

**Access Requirements:**
- **Credentials:**
  - Stripe API secret key (test + production)
  - Webhook signing secret (test + production)
- **Owner:** @ASK_CLIENT (via Q-INT-002)
- **Account Access:** @ASK_CLIENT (Stripe dashboard access for testing/debugging)

**Data Mapping:**
- **User Table:** Map PostgreSQL user ID ↔ Stripe Customer ID
- **Subscription Table:** @ASK_CLIENT (schema exists?) via Q-TECH-004
  - Fields: subscription_id (Stripe), plan_id, status, current_period_end, cancel_at_period_end
- **Payment Events:** @ASK_CLIENT (log webhook events?) via Q-TECH-005

**Testing Strategy:**
- **Stripe CLI:** Use for local webhook testing (proposal mentions this)
- **Test Subscriptions:** Create test customers and subscriptions
- **Idempotency:** Handle duplicate webhook events (Stripe retries)

**Risk Indicators:**
- ⚠️ No Stripe account access → **BLOCKER** for Week 3 development
- ⚠️ Unclear subscription model → May design wrong schema
- ⚠️ Webhook security not addressed → Vulnerability risk

**Linked Questions:** Q-USER-002, Q-TECH-002, Q-TECH-004, Q-INT-002

---

### INT-003: PostgreSQL Database

**System Information:**
- **Type:** Relational database
- **Version:** @ASK_CLIENT (PostgreSQL version?)
- **Environment:** @ASK_CLIENT (local, staging, production)
- **Authentication:** Username/password or connection string

**Integration Requirements:**
- **Schema Review:** @ASK_CLIENT (via Q-TECH-004)
  - Users table: ID, email, stripe_customer_id (?)
  - Subscriptions table: @ASK_CLIENT (exists? schema?)
  - OpenAI interactions table: @ASK_CLIENT (log AI requests/responses?)
- **ORM:** @ASK_CLIENT (SQLAlchemy? raw SQL? other?)
- **Migrations:** @ASK_CLIENT (Alembic? manual? who manages?)

**Access Requirements:**
- **Credentials:** Database connection string (dev, staging, production)
- **Owner:** @ASK_CLIENT (via Q-INT-002)
- **Permissions:** Read/write access to relevant tables

**Data Mapping:**
- **User Management:** How are users created/updated?
- **Stripe Integration:** stripe_customer_id stored in users table?
- **OpenAI Integration:** Log requests/responses? Separate table?

**Risk Indicators:**
- ⚠️ No schema visibility → Cannot validate integration design
- ⚠️ Schema changes needed → May require migration approval/delay
- ⚠️ No database access → Cannot test queries or validate data

**Linked Questions:** Q-TECH-004, Q-INT-002

---

### INT-004: FastAPI Backend (Existing Codebase)

**System Information:**
- **Type:** Python web framework
- **Version:** @ASK_CLIENT (FastAPI version?)
- **Repository:** @ASK_CLIENT (GitHub URL?) via GAP-003
- **Deployment:** @ASK_CLIENT (local, staging, production) via Q-OPS-004

**Integration Requirements:**
- **Code Review:** Understand existing route structure, middleware, error handling
- **Dependency Management:** @ASK_CLIENT (Poetry? pip? requirements.txt?)
- **Configuration:** @ASK_CLIENT (environment variables? config files?)

**Access Requirements:**
- **Repository Access:** GitHub repository URL + permissions (GAP-003)
- **Local Setup:** Instructions for running locally (README?)
- **Credentials:** Database, API keys for local development

**Code Patterns to Follow:**
- **Route Organization:** @ASK_CLIENT (blueprint structure? routers?)
- **Error Handling:** @ASK_CLIENT (existing patterns?) via Q-TECH-005
- **Testing:** @ASK_CLIENT (existing test suite?) via Q-COMP-002
- **Logging:** @ASK_CLIENT (logging framework?) via Q-TECH-005

**Risk Indicators:**
- ⚠️ No repository access → **BLOCKER** for Day 1
- ⚠️ Significant tech debt → Timeline underestimated
- ⚠️ No documentation → Steep learning curve

**Linked Questions:** Q-TECH-003, Q-TECH-005, Q-COMP-002, Q-OPS-004

---

### INT-005: Next.js Frontend (Optional)

**System Information:**
- **Type:** React-based frontend framework
- **Repository:** @ASK_CLIENT (same repo as backend, or separate?)
- **Scope:** @ASK_CLIENT (in scope for initial project?) via Q-TECH-006

**Integration Requirements:**
- **API Contracts:** If frontend integration is post-MVP, design backend APIs to be frontend-friendly
- **Documentation:** OpenAPI/Swagger docs for frontend team
- **CORS:** Configure CORS settings for frontend domain

**Access Requirements:**
- **Repository Access:** If in scope, request frontend repo access
- **Frontend Developer Contact:** @ASK_CLIENT (who to coordinate with?)

**Risk Indicators:**
- ⚠️ Unclear scope → May need frontend milestone if client expects it
- ⚠️ No frontend coordination → API contract mismatches

**Linked Questions:** Q-TECH-006, Q-INT-001

---

### INT-006: GitHub (Code Collaboration)

**System Information:**
- **Type:** Version control platform
- **Repository:** @ASK_CLIENT (GitHub URL?)
- **Access:** @ASK_CLIENT (permissions level needed?)

**Integration Requirements:**
- **Access Level:** Write access for branches, PR creation
- **Branching Strategy:** @ASK_CLIENT (main/dev? feature branches?) via Q-OPS-002
- **PR Review Process:** @ASK_CLIENT (who reviews? approval required?) via Q-OPS-002

**Access Requirements:**
- **Repository URL:** @ASK_CLIENT (via GAP-003)
- **Permissions:** Contributor or Maintainer role
- **Timeline:** Within 24 hours of contract start

**Risk Indicators:**
- ⚠️ No access → **BLOCKER** for Day 1
- ⚠️ Unclear workflow → May cause merge conflicts or process friction

**Linked Questions:** Q-TECH-003 (repo access), Q-OPS-002 (workflow)

---

### INT-007: Discord (Communication)

**System Information:**
- **Type:** Team communication platform
- **Server:** @ASK_CLIENT (server name/invite?)
- **Channels:** @ASK_CLIENT (which channels for updates?)

**Integration Requirements:**
- **Daily Updates:** Post daily progress in designated channel (job-post.md:5)
- **Format:** @ASK_CLIENT (standup format? PR links?) via Q-OPS-001
- **Availability:** @ASK_CLIENT (timezone overlap for sync) via Q-OPS-001

**Access Requirements:**
- **Server Invite:** @ASK_CLIENT (via GAP-004)
- **Timeline:** Within 24 hours of contract start

**Risk Indicators:**
- ⚠️ No access → Cannot communicate effectively
- ⚠️ Unclear update format → Misaligned expectations

**Linked Questions:** Q-OPS-001

---

### INT-008: Additional Services (TBD)

**Potential Integrations to Clarify:**
- **Email Service:** SendGrid, AWS SES, Mailgun (for user notifications?)
- **SMS Service:** Twilio (for 2FA or payment alerts?)
- **Monitoring:** Sentry, DataDog, New Relic (for error tracking?)
- **Analytics:** Mixpanel, Amplitude (for user behavior?)
- **Health-Tech Platforms:** @ASK_CLIENT (any B2B integrations?) via Q-INT-001

**Discovery Questions:**
- Q-INT-001: Third-party service dependencies
- Q-TECH-005: Monitoring and observability tools

**Risk Indicators:**
- ⚠️ Hidden integrations not disclosed → Scope creep risk
- ⚠️ Complex B2B integrations → May need specialized knowledge

---

## Integration Dependencies Matrix

| Integration | Blocks Week 1 | Blocks Week 3 | Affects Architecture | Post-MVP |
|-------------|---------------|---------------|---------------------|----------|
| OpenAI API | ✅ **BLOCKER** | - | ✅ Yes | - |
| Stripe | - | ✅ **BLOCKER** | ✅ Yes | - |
| PostgreSQL | ⚠️ Schema needed | ✅ **CRITICAL** | ✅ Yes | - |
| FastAPI Repo | ✅ **BLOCKER** | - | - | - |
| Next.js | - | - | ⚠️ API design | ✅ Yes |
| GitHub | ✅ **BLOCKER** | - | - | - |
| Discord | ✅ **BLOCKER** (communication) | - | - | - |
| Email/SMS | - | - | ⚠️ Maybe | ✅ Likely |
| Monitoring | - | - | - | ✅ Yes |

## Critical Path Items (Must Resolve Before Week 1)

1. **GitHub Repository Access** (GAP-003, Q-TECH-003)
2. **Discord Server Invite** (GAP-004, Q-OPS-001)
3. **OpenAI API Keys** (GAP-001, Q-TECH-002)
4. **FastAPI Codebase Review** (Q-TECH-003)

## Critical Path Items (Must Resolve Before Week 3)

1. **Stripe Account Access** (GAP-002, Q-TECH-002)
2. **PostgreSQL Schema/ERD** (GAP-008, Q-TECH-004)
3. **Subscription Model Clarification** (ASSUMPTION-002, Q-USER-002)

## Discovery Call Priority

**P0 (Must Address):**
- INT-001: OpenAI API (credentials, endpoints)
- INT-002: Stripe (account access, subscription model)
- INT-004: FastAPI Backend (repository access)
- INT-006: GitHub (repository URL, access)
- INT-007: Discord (server invite)

**P1 (Should Address):**
- INT-003: PostgreSQL (schema review, access)
- INT-008: Additional Services (identify hidden dependencies)

**P2 (Nice to Address):**
- INT-005: Next.js Frontend (scope clarification)
- Monitoring/observability tools (Q-TECH-005)

## Post-Discovery Actions

1. **Update all @ASK_CLIENT tags** with confirmed information
2. **Assign Owner and Due Date** for each access requirement
3. **Document credentials handoff process** in communication-plan.md
4. **Create access tracking checklist** for Day 1 setup
5. **Flag any newly discovered integrations** not in original proposal scope

