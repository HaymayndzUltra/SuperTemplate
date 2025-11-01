# Risk Log - Surfa Production Completion

**Project:** Surfa - AI-powered Local SEO SaaS Platform  
**Generated:** 2025-10-31  
**Protocol:** 02 - Client Discovery Initiation

---

## Risk Assessment Summary

**Total Risks Identified:** 11  
**Critical:** 3  
**High:** 4  
**Medium:** 3  
**Low:** 1

---

## Critical Risks

### RISK-001: Data Isolation Failure (Cross-Account Leakage)
**Severity:** CRITICAL  
**Probability:** MEDIUM  
**Impact:** HIGH (compliance violation, loss of trust, potential data breach)

**Description:**  
Client has experienced keyword bleeding across accounts in the past. Incomplete RLS policies could allow users to access reviews/keywords from other accounts.

**Root Cause:**  
Supabase RLS policies are "partially implemented" - unclear which tables lack proper isolation.

**Mitigation Strategy:**
1. **Immediate:** Audit all multi-tenant tables (reviews, keywords, gbp_accounts, subscriptions)
2. **Implementation:** Complete RLS policies before any production data touches system
3. **Validation:** Write automated tests that attempt cross-account access (must fail)
4. **Monitoring:** Add logging for any RLS policy violations

**Contingency Plan:**  
If RLS gaps found late: Halt production deployment, complete policies, re-test isolation on staging with all 8 test accounts.

**Owner:** Technical Lead  
**Status:** OPEN  
**Review Date:** Monday (start of M1)

---

### RISK-002: Stripe Webhook Replay Attacks
**Severity:** CRITICAL  
**Probability:** MEDIUM  
**Impact:** HIGH (duplicate charges, incorrect subscription states, revenue loss)

**Description:**  
Without idempotency checks, Stripe webhook retries could process same event multiple times, causing payment state drift.

**Root Cause:**  
Stripe retries webhooks for failed/timeout responses. No idempotency table = duplicate processing.

**Mitigation Strategy:**
1. **Implementation:** Create `stripe_webhook_events` table with unique constraint on `event_id`
2. **Logic:** Check `event_id` exists before processing any webhook
3. **Testing:** Simulate webhook replay on staging (manually trigger same event_id twice)
4. **Monitoring:** Log all webhook processing attempts (success/duplicate/failure)

**Contingency Plan:**  
If duplicate processing detected in production: Implement event_id deduplication immediately, audit affected subscriptions, issue refunds if necessary.

**Owner:** Backend Developer  
**Status:** OPEN  
**Review Date:** M2 start (Week 2)

---

### RISK-003: Performance Target Miss (<500ms)
**Severity:** CRITICAL  
**Probability:** LOW  
**Impact:** HIGH (user churn, failed acceptance criteria, client dissatisfaction)

**Description:**  
Current dashboard loads in ~2.3s. Achieving <500ms requires 78% improvement - aggressive target.

**Root Cause:**  
Unknown bottlenecks (no profiling data provided). Optimization without data = guesswork.

**Mitigation Strategy:**
1. **Discovery:** Request current profiling data from client (Chrome DevTools Performance tab)
2. **Analysis:** Identify top 3 bottlenecks (API calls, bundle size, SSR time)
3. **Prioritization:** Focus on highest-impact optimizations first
4. **Incremental:** Target 1.0s first, then 0.7s, then <0.5s (avoid premature optimization)
5. **Fallback:** If <500ms unrealistic, negotiate target (e.g., <750ms acceptable?)

**Contingency Plan:**  
If <500ms unachievable: Document bottlenecks, propose phased optimization (hit 1.0s for M2, continue improving post-launch).

**Owner:** Frontend Developer  
**Status:** OPEN - Needs profiling data  
**Review Date:** Monday (request data from client)

---

## High Risks

### RISK-004: GBP API Write Permission Failure
**Severity:** HIGH  
**Probability:** MEDIUM  
**Impact:** MEDIUM (blocks M1.2 review reply feature)

**Description:**  
Current OAuth scopes include `BUSINESS_PROFILE_REVIEWS`, but write access hasn't been validated across all 8 test accounts. Scope mismatch could block reply posting.

**Assumptions:**  
GBP API allowlist is active, OAuth grants write permissions.

**Mitigation Strategy:**
1. **Validation:** Test write operation (post dummy reply) on all 8 test accounts in Week 1
2. **Early Detection:** Identify scope issues before M1.2 implementation
3. **Escalation:** If scope insufficient, request additional permissions via GBP Console

**Contingency Plan:**  
If write fails: Escalate to Google support, request scope adjustment. Worst case: Delay M1.2 until resolved.

**Owner:** Integration Developer  
**Status:** OPEN  
**Review Date:** Week 1, Day 2

---

### RISK-005: DataForSEO Rate Limit Exhaustion
**Severity:** HIGH  
**Probability:** LOW  
**Impact:** MEDIUM (blocks keyword feature temporarily)

**Description:**  
Testing with 8 GBP accounts could consume significant DataForSEO requests. Current usage: 2k/5k (40%), buffer: 3k requests. Heavy testing could exhaust monthly quota.

**Mitigation Strategy:**
1. **Monitoring:** Track request count daily during testing
2. **Throttling:** Implement request batching (queue keyword refreshes)
3. **Alert:** Warn at 80% usage (4,000 requests)
4. **Testing Efficiency:** Use cached responses for repeated tests (avoid duplicate API calls)

**Contingency Plan:**  
If quota exceeded: Pause keyword testing until next billing cycle, upgrade DataForSEO plan if critical, or mock API responses for remaining tests.

**Owner:** API Integration Lead  
**Status:** OPEN  
**Review Date:** Week 1 (establish baseline request usage)

---

### RISK-006: Vercel Hobby → Pro Upgrade Timing
**Severity:** HIGH  
**Probability:** LOW  
**Impact:** MEDIUM (blocks production deployment)

**Description:**  
Vercel Pro upgrade required for advanced caching and production features. If upgrade delayed, deployment blocked.

**Assumption:**  
Client will upgrade before M3 production deployment.

**Mitigation Strategy:**
1. **Communication:** Confirm upgrade timeline Monday (during kickoff)
2. **Dependency:** Mark M3 deployment as dependent on Pro upgrade
3. **Early Upgrade:** Recommend upgrading during M2 (Week 2) to allow time for configuration

**Contingency Plan:**  
If upgrade delayed: Deploy to staging only until Pro active. Worst case: Use current Hobby plan with degraded performance (not recommended).

**Owner:** Client (Account Owner)  
**Status:** OPEN - Confirmation needed  
**Review Date:** Monday kickoff

---

### RISK-007: Incomplete RLS Policy Performance Impact
**Severity:** HIGH  
**Probability:** MEDIUM  
**Impact:** LOW (performance degradation if RLS adds query overhead)

**Description:**  
RLS policies add SQL WHERE clauses to every query. Complex policies on large datasets could slow queries beyond acceptable limits.

**Mitigation Strategy:**
1. **Testing:** Load test with realistic data volume (1,000+ reviews per account)
2. **Monitoring:** Measure query execution time with RLS enabled
3. **Optimization:** Add database indexes on RLS filter columns (`user_id`, `gbp_account_id`)
4. **Threshold:** If query time >100ms, investigate query plan and optimize

**Contingency Plan:**  
If RLS causes slowdown: Optimize indexes, denormalize data if needed, or implement application-layer filtering (less secure but faster).

**Owner:** Database Architect  
**Status:** OPEN  
**Review Date:** M1 (during RLS implementation)

---

## Medium Risks

### RISK-008: GBP API Timeout Handling
**Severity:** MEDIUM  
**Probability:** MEDIUM  
**Impact:** LOW (UX degradation, retry logic needed)

**Description:**  
GBP API can be slow (timeouts observed in proposal analysis). Without retry logic, users see errors instead of graceful degradation.

**Mitigation Strategy:**
1. **Timeout Configuration:** Set 10s timeout for GBP API calls
2. **Retry Logic:** Exponential backoff (3 retries max)
3. **User Feedback:** Show "Syncing reviews..." spinner instead of error
4. **Queue:** Implement background job queue for slow sync operations

**Contingency Plan:**  
If timeouts persist: Increase timeout to 30s, implement async polling (user gets email when sync completes).

**Owner:** Backend Developer  
**Status:** OPEN  
**Review Date:** Week 1 (during M1.1 implementation)

---

### RISK-009: Staging Environment Configuration Mismatch
**Severity:** MEDIUM  
**Probability:** LOW  
**Impact:** MEDIUM (false confidence from staging tests)

**Description:**  
If staging doesn't mirror production (different Supabase project, env vars, Vercel config), tests may pass on staging but fail in production.

**Mitigation Strategy:**
1. **Audit:** Confirm staging matches production (same Next.js version, Supabase tier, env variables)
2. **Parity:** Use same Stripe test mode webhooks on staging
3. **Checklist:** Document environment parity requirements

**Contingency Plan:**  
If mismatch discovered: Fix configuration before M3 deployment, re-run integration tests.

**Owner:** DevOps/Client  
**Status:** OPEN - Needs confirmation  
**Review Date:** Monday (request staging details from client)

---

### RISK-010: OAuth Token Refresh Failure
**Severity:** MEDIUM  
**Probability:** LOW  
**Impact:** MEDIUM (users can't sync reviews until re-auth)

**Description:**  
GBP OAuth tokens expire. If refresh token logic missing or fails, users lose API access.

**Mitigation Strategy:**
1. **Implementation:** Store refresh tokens securely in Supabase
2. **Logic:** Detect 401 errors, attempt token refresh, fallback to re-auth prompt
3. **Testing:** Simulate expired token scenario

**Contingency Plan:**  
If refresh fails: Prompt user to re-authorize GBP connection (minor UX friction but not blocking).

**Owner:** OAuth Integration Developer  
**Status:** OPEN  
**Review Date:** Week 1 (during M1.1 OAuth validation)

---

## Low Risks

### RISK-011: Third-Party API Deprecation
**Severity:** LOW  
**Probability:** LOW  
**Impact:** LOW (future maintenance, not immediate threat)

**Description:**  
GBP API, DataForSEO, or Stripe could deprecate endpoints during project timeline (unlikely in 2-3 weeks).

**Mitigation Strategy:**
1. **Monitoring:** Subscribe to API changelog/announcements
2. **Versioning:** Pin API versions where possible
3. **Testing:** Use latest stable API versions

**Contingency Plan:**  
If deprecation announced: Migrate to new endpoints as part of ongoing maintenance.

**Owner:** Technical Lead  
**Status:** OPEN (monitoring)  
**Review Date:** Ongoing

---

## Assumptions Requiring Validation

### ASSUMPTION-001: GBP API Allowlist Active
**Status:** ASSUMED (client mentioned it's active)  
**Validation Needed:** Confirm on Monday via API test  
**Impact if False:** Blocks all GBP integration (M1 fails)

### ASSUMPTION-002: No GBP Rate Limit Issues
**Status:** ASSUMED (proposal stated "rate limits won't throttle")  
**Validation Needed:** Request client's observed rate limits  
**Impact if False:** Delays sync operations, need queueing

### ASSUMPTION-003: DataForSEO Supports Location Context
**Status:** ASSUMED (API likely supports location_code param)  
**Validation Needed:** Review DataForSEO API docs Monday  
**Impact if False:** Keyword context degraded (less relevant suggestions)

### ASSUMPTION-004: Staging Mirrors Production
**Status:** ASSUMED  
**Validation Needed:** Confirm staging config with client  
**Impact if False:** Test results unreliable

### ASSUMPTION-005: RLS Performance Acceptable
**Status:** ASSUMED (<50ms overhead)  
**Validation Needed:** Load test during M1  
**Impact if False:** Query optimization required

---

## Open Questions Requiring Client Input

1. **GBP API Quotas:** What are the observed rate limits per account?
2. **Profiling Data:** Can you share Chrome DevTools performance snapshot of current 2.3s dashboard load?
3. **RLS Status:** Which specific Supabase tables still need RLS policies?
4. **Staging Config:** Does staging environment match production (Supabase project, env vars)?
5. **Error Monitoring:** Is Sentry or similar tool already configured?
6. **Deployment Process:** Is staging deployment manual or automated (CI/CD)?

---

## Risk Review Cadence

- **Daily Standup:** Quick review of any new risks discovered
- **End of Week 1:** Formal risk review after M1 completion
- **End of Week 2:** Risk review after M2 completion
- **Pre-Production:** Final risk audit before M3 deployment

---

**Evidence:** `.artifacts/protocol-02/risk-log.md`  
**Status:** ✅ PHASE 2.3 Complete - Risks and assumptions documented
