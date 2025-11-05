# Actionable Task List

**Total Tasks**: 87 | **Timeline**: 16-20 weeks | **Critical Path**: 12 weeks

---

## Immediate Actions (Week 1) - 5 BLOCKERS

### IA-1: Fix Corrupted Markdown (10 min)
- [ ] Remove "github.com" from lines 61, 91, 106, 113, 168-169
- [ ] Validate: `mdl plano.md`

### IA-2: Create Renaming Manifest (2 hrs)
- [ ] Generate `renaming-manifest.json` with all 68 scripts
- [ ] Create `batch_rename_scripts.py`
- [ ] Test dry-run

### IA-3: Recalculate Automation Scores (1 hr)
- [ ] Define formula with semantic validation weight
- [ ] Recalculate 10 protocols
- [ ] Update plano.md table

### IA-4: Document API Dependencies (3 hrs)
- [ ] Create `docs/api-integrations.md`
- [ ] Specify: Calendar, APM, Monitoring, Transcription APIs
- [ ] Define auth, rate limits, error handling

### IA-5: Build Dependency Graph (4 hrs)
- [ ] Analyze 52 scripts for dependencies
- [ ] Create mermaid/graphviz graph
- [ ] Sequence into 4 waves

---

## Phase 1: Script Renaming (Week 1-2)

### P1-1: Prepare (4 hrs)
- [ ] Backup scripts/
- [ ] Export registry
- [ ] Create test environment

### P1-2: Execute Renaming (1 hr)
- [ ] Run dry-run
- [ ] Execute rename (68 scripts)
- [ ] Commit atomically

### P1-3: Update Registry (2 hrs)
- [ ] Run auto_register_scripts.py
- [ ] Validate registry
- [ ] Update protocol hooks

### P1-4: Update CI/CD (3 hrs)
- [ ] Update workflows, configs
- [ ] Replace hard-coded paths
- [ ] Commit changes

### P1-5: Test (4 hrs)
- [ ] Run CI for all 23 protocols
- [ ] Verify evidence aggregation
- [ ] Fix failures

### P1-6: Deploy (2 hrs)
- [ ] Merge to main
- [ ] Tag v1.0.0-script-renaming
- [ ] Monitor 24h

---

## Phase 2: Missing Gate Validators (Week 2-3)

15 scripts to create:
1. validate_gate_14_rehearsal.py (3h)
2. validate_gate_14_security.py (6h)
3. validate_gate_15_freeze.py (4h)
4. validate_gate_15_reporting.py (3h)
5. validate_gate_16_alerts.py (4h)
6. validate_gate_16_assurance.py (3h)
7. validate_gate_17_mitigation.py (3h)
8. validate_gate_17_recovery.py (4h)
9. validate_gate_23_static.py (4h)
10. validate_gate_23_reporting.py (3h)

**Total**: 37 hours

---

## Phase 3: High-ROI Scripts (Week 3-6)

Priority order:
1. validate_prd_traceability.py (12h) - UNBLOCKS Protocol 08
2. validate_task_to_prd_mapping.py (8h) - BLOCKED by #1
3. validate_brief_content.py (10h)
4. validate_execution_security.py (12h)
5. maintenance_backlog_aggregator.py (12h)
6. freeze_window_validator.py (6h)
7. generate_audit_summary.py (8h)

**Total**: 68 hours

---

## Phase 4: External Integrations (Week 6-12)

### Calendar Integration (24h)
- Build shared module (16h)
- schedule_discovery_call.py (8h)
- uat_schedule_assistant.py (10h)

### APM Integration (42h)
- Build shared module (20h)
- performance_baseline_collector.py (12h)
- alert_threshold_checker.py (10h)

### Other Integrations (20h)
- rollback_orchestrator.py (12h)
- doc_generator.py (8h)

**Total**: 86 hours

---

## Phase 5: AI/ML Components (Week 12-20)

1. ML Infrastructure setup (24h)
2. validate_discovery_transcript.py (32h)
3. incident_severity_classifier.py (28h)
4. retrospective_analysis.py (36h)
5. style_calibrator.py (32h)

**Total**: 152 hours

---

## Resource Allocation

| Role | Hours/Week | Duration | Total Hours |
|------|-----------|----------|-------------|
| DevOps Lead | 20 | 6 weeks | 120 |
| Backend Dev 1-4 | 20 each | 8 weeks | 640 |
| Security Engineer | 15 | 4 weeks | 60 |
| Integration Engineer | 20 | 6 weeks | 120 |
| ML Engineer | 25 | 8 weeks | 200 |
| QA Lead | 10 | 12 weeks | 120 |

**Total Effort**: 1,260 hours (~7.5 FTE for 4 months)

---

## Success Metrics

- [ ] 68 scripts renamed, CI green
- [ ] 15 missing gate validators created
- [ ] 52 new scripts implemented
- [ ] Automation scores recalculated
- [ ] All 23 protocols tested end-to-end
- [ ] Documentation complete
- [ ] Zero breaking changes in production

---

**Status**: Ready for execution  
**Next**: Assign owners and schedule kickoff
