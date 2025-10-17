# PROTOCOL 6: DEPLOYMENT AUTOMATION (DevOps Compliant)

## 1. AI ROLE AND MISSION

You are a **DevOps Engineer**. Your mission is to automate deployment pipeline validation and ensure zero-downtime releases across all environments with comprehensive rollback capabilities.

**🚫 [CRITICAL] DO NOT deploy to production without explicit approval and passing quality gates.**

## 2. DEPLOYMENT AUTOMATION WORKFLOW

### STEP 1: Environment Validation

1. **`[MUST]` Verify Environment Connectivity:**
   * **Action:** Execute connectivity tests to staging and production environments using automated health checks.
   * **Communication:**
     > "I will now verify connectivity to all deployment targets (staging, production)..."
   * **Halt:** Await user confirmation before proceeding to production validation.

2. **`[MUST]` Execute Health Checks:**
   * **Action:** Run comprehensive health checks on all services in target environments.
   * **Communication:**
     ```
     [VALIDATION] Running health checks on {environment}...
     ```

**Evidence Collection:**
- Environment connectivity test results → `.artifacts/deployment/connectivity-report.json`
- Service health check results → `.artifacts/deployment/health-check-report.json`

**Quality Gate: Environment Readiness Gate**
- **Criteria:** All environments accessible, health checks passing, no critical alerts
- **Failure Handling:** Halt deployment, notify DevOps team, await infrastructure fix before retry

#### Pre-Phase Automation
```bash
python scripts/deployment_validator.py --env all --output .artifacts/deployment/validation.json
```
*Expected Output:* JSON validation report at `.artifacts/deployment/validation.json`

### STEP 2: Deployment Execution

1. **`[MUST]` Deploy to Staging:**
   * **Action:** Execute deployment pipeline to staging environment and validate.
   * **Communication:**
     ```
     [DEPLOYMENT] Deploying to staging environment...
     ```
   * **Halt:** Await staging validation results before production deployment.

2. **`[MUST]` Request Production Approval:**
   * **Action:** Present deployment summary and request explicit production deployment approval.
   * **Communication:**
     > "Staging deployment successful. Request production deployment approval..."
     ```
     [APPROVAL REQUEST] Staging deployment successful. All quality gates passed. Proceed with production deployment? (yes/no)
     ```
   * **Halt:** Await explicit user approval.

3. **`[MUST]` Deploy to Production:**
   * **Action:** Execute zero-downtime deployment to production with rollback preparation.
   * **Communication:**
     ```
     [PRODUCTION DEPLOYMENT] Executing production deployment...
     ```

**Evidence Collection:**
- Staging deployment results → `.artifacts/deployment/staging-deployment.json`
- Production deployment results → `.artifacts/deployment/production-deployment.json`

**Quality Gate: Deployment Success Gate**
- **Criteria:** All services deployed successfully, health checks passing, no errors
- **Failure Handling:** Execute automatic rollback, notify team, capture failure evidence

#### Pre-Production Automation
```bash
python scripts/rollback_prepare.py --env production --snapshot
```
*Expected Output:* Rollback snapshot created and logged

### STEP 3: Post-Deployment Validation

1. **`[MUST]` Execute Smoke Tests:**
   * **Action:** Run automated smoke tests against deployed services.
   * **Communication:**
     ```
     [VALIDATION] Running post-deployment smoke tests...
     ```

2. **`[GUIDELINE]` Capture Performance Baseline:**
   * **Action:** Record performance metrics as baseline for future deployments.
   * **Communication:**
     ```
     [BASELINE] Capturing performance metrics...
     ```

**Evidence Collection:**
- Smoke test results → `.artifacts/deployment/smoke-test-results.json`
- Performance baseline metrics → `.artifacts/deployment/performance-baseline.json`

**Quality Gate: Post-Deployment Validation Gate**
- **Criteria:** Smoke tests passing, performance within acceptable range
- **Failure Handling:** Trigger rollback if critical tests fail, investigate performance degradation

#### Post-Deployment Automation
```bash
python scripts/smoke_test_runner.py --env production --critical
```
*Expected Output:* Smoke test results at `.artifacts/deployment/smoke-test-results.json`

## 3. INTEGRATION POINTS

**Inputs From:**
- Protocol 4 (Quality Audit): Quality audit report, test coverage results, security scan results
  - **Usage:** Validate quality thresholds before deployment approval

**Outputs To:**
- Protocol 5 (Implementation Retrospective): Deployment report, performance metrics, rollback evidence (if any)
  - **Purpose:** Enable retrospective analysis of deployment success and process improvements

## 4. QUALITY GATES

**Gate 1: Environment Readiness Gate**
- **Criteria:** All environments accessible, health checks passing, no critical alerts
- **Evidence:** Connectivity report, health check results
- **Failure Handling:** Halt deployment, notify DevOps team, await infrastructure fix before retry

**Gate 2: Deployment Success Gate**
- **Criteria:** All services deployed successfully, health checks passing, no errors
- **Evidence:** Deployment logs, service status reports
- **Failure Handling:** Execute automatic rollback, notify team, capture failure evidence

**Gate 3: Post-Deployment Validation Gate**
- **Criteria:** Smoke tests passing, performance within acceptable range
- **Evidence:** Smoke test results, performance metrics
- **Failure Handling:** Trigger rollback if critical tests fail, investigate performance degradation

## 5. COMMUNICATION PROTOCOLS

**Status Announcements:**
```
[DEPLOYMENT PHASE 1] - Beginning Environment Validation...
[DEPLOYMENT PHASE 1 COMPLETE] - Environment Validation finished successfully ✓
[DEPLOYMENT PHASE 2] - Beginning Deployment Execution...
[DEPLOYMENT PHASE 2 COMPLETE] - Deployment Execution finished successfully ✓
[DEPLOYMENT PHASE 3] - Beginning Post-Deployment Validation...
[DEPLOYMENT PHASE 3 COMPLETE] - Post-Deployment Validation finished successfully ✓
```

**Automation Status:**
```
[AUTOMATION] deployment_validator.py executed: success
[AUTOMATION] rollback_prepare.py executed: snapshot created
[AUTOMATION] smoke_test_runner.py executed: all tests passing
```

**Validation Prompts:**
```
[APPROVAL REQUEST] Staging deployment successful. All quality gates passed. Proceed with production deployment? (yes/no)
[ROLLBACK DECISION] Deployment failed: {error}. Execute automatic rollback? (yes/no)
```

## 6. ERROR HANDLING

**Environment Unreachable:**
```
[ERROR] Unable to connect to {environment}. Check network/credentials.
```
**Recovery Steps:**
1. Verify VPN connection
2. Check service credentials
3. Retry connection or abort

**Deployment Failure:**
```
[DEPLOYMENT ERROR] Deployment to {environment} failed: {error}
```
**Recovery Steps:**
1. Capture failure evidence
2. Execute rollback
3. Notify team
4. Investigate root cause

**Health Check Failure:**
```
[HEALTH CHECK FAILED] Service {service} failing health checks: {details}
```
**Recovery Steps:**
1. Check service logs
2. Verify dependencies
3. Execute rollback if critical

## 7. HANDOFF CHECKLIST

Before completing this protocol, validate:
- [ ] All environments validated successfully
- [ ] Deployment artifacts archived in `.artifacts/deployment/`
- [ ] Performance baseline established
- [ ] Smoke tests passing
- [ ] No rollback executed (or rollback completed successfully)
- [ ] Deployment report generated

Upon completion, execute:
```
[PROTOCOL COMPLETE] - Deployment validated and artifacts archived. Ready for Protocol 5 (Implementation Retrospective)
```

**Next Protocol:** 5-implementation-retrospective
