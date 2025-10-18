# Protocol Renumbering Execution Plan

## Current State Analysis
- **25 protocol files** with inconsistent numbering
- **29 @apply handoffs** need updating
- **610 protocol mentions** need updating
- **484 artifact references** need updating

## Systematic Renaming Plan

### Phase 0: Foundation & Discovery (01-05)
- `00a-client-proposal-generation.md` → `01-client-proposal-generation.md`
- `00B-client-discovery-initiation.md` → `02-client-discovery-initiation.md`
- `01-project-brief-creation.md` → `03-project-brief-creation.md`
- `00-project-bootstrap-and-context-engineering.md` → `04-project-bootstrap-and-context-engineering.md`
- `0-bootstrap-your-project.md` → `05-bootstrap-your-project.md`

### Phase 1-2: Planning & Design (06-09)
- `1-create-prd.md` → `06-create-prd.md`
- `6-technical-design-architecture.md` → `07-technical-design-architecture.md`
- `2-generate-tasks.md` → `08-generate-tasks.md`
- `7-environment-setup-validation.md` → `09-environment-setup-validation.md`

### Phase 3: Development (10-11)
- `3-process-tasks.md` → `10-process-tasks.md`
- `9-integration-testing.md` → `11-integration-testing.md`

### Phase 4: Quality & Testing (12-14)
- `4-quality-audit.md` → `12-quality-audit.md`
- `15-uat-coordination.md` → `13-uat-coordination.md`
- `10-pre-deployment-staging.md` → `14-pre-deployment-staging.md`

### Phase 5: Deployment & Operations (15-18)
- `11-production-deployment.md` → `15-production-deployment.md`
- `12-monitoring-observability.md` → `16-monitoring-observability.md`
- `13-incident-response-rollback.md` → `17-incident-response-rollback.md`
- `14-performance-optimization.md` → `18-performance-optimization.md`

### Phase 6: Closure & Maintenance (19-23)
- `16-documentation-knowledge-transfer.md` → `19-documentation-knowledge-transfer.md`
- `17-project-closure.md` → `20-project-closure.md`
- `18-maintenance-support.md` → `21-maintenance-support.md`
- `5-implementation-retrospective.md` → `22-implementation-retrospective.md`
- `8-script-governance-protocol.md` → `23-script-governance-protocol.md`

### Supporting Protocols (24-27)
- `00-client-discovery.md` → `24-client-discovery.md`
- `INTEGRATION-GUIDE.md` → `26-integration-guide.md`
- `VALIDATION-GUIDE.md` → `27-validation-guide.md`
- `PROTOCOL-INTEGRATION-MAP.md` → `25-protocol-integration-map.md`

## Execution Steps
1. **Rename files** using git mv to preserve history
2. **Update @apply handoffs** in each file
3. **Update artifact paths** (.artifacts/protocol-N/)
4. **Update textual mentions** ("Protocol X")
5. **Update supporting documentation**
6. **Run validation script**

## Risk Mitigation
- Backup current state
- Execute in dependency order
- Validate after each phase
- Test workflow continuity
