# ECOSYSTEM INTEGRATION MAP FOR PROTOCOL 05B

## Integration Architecture

```
Foundation (01-05) → [05B Router] → Generic Workflow (06-23)
                                  → AI Workflow (06-28)
                                  → Hybrid (Mix both)
```

## UPSTREAM INPUTS

### From Protocol 03
- **Artifact:** `PROJECT-BRIEF.md`
- **Usage:** Parse requirements, goals, tech stack
- **Phase:** PHASE 1, STEP 1.2

### From Protocol 05
- **Artifacts:** `bootstrap-manifest.json`, `architecture-principles.md`
- **Usage:** Load architecture patterns, constraints
- **Phase:** PHASE 1, STEP 1.1 & 1.3

## DOWNSTREAM OUTPUTS

### To Generic Workflow
- **Target:** Protocol 06 (.cursor/ai-driven-workflow/)
- **When:** Generic web application detected

### To AI Workflow
- **Target:** Protocol 06 (AI-project-workflow/)
- **When:** AI/ML components detected

### To Hybrid
- **Target:** Custom sequence from both
- **When:** Web app + AI components

## LATERAL INTEGRATIONS

### Protocol 0 (Bootstrap Context)
- **Called When:** Gap detected, new protocol needed
- **Flow:** 05b → Call Protocol 0 → Receive new protocol → Validate

### Validator System
- **Used When:** Validating new protocols
- **Command:** `validate_all_protocols.py --protocol-id {new_id}`
- **Requirement:** Score ≥0.95

## KEY ARTIFACTS FLOW

| Artifact | From | Used In 05b | Passed To |
|----------|------|-------------|-----------|
| PROJECT-BRIEF.md | Protocol 03 | Requirement parsing | Next protocol |
| architecture-principles.md | Protocol 05 | Architecture analysis | Next protocol |
| PROTOCOL-EXECUTION-PLAN.md | Generated | Output | Next protocol owner |
| PROTOCOL-CHECKLIST.md | Generated | Output | User tracking |

## INTEGRATION VALIDATION

### Pre-Integration Checklist
- [ ] Protocols 01-05 complete
- [ ] PROJECT-BRIEF.md approved
- [ ] architecture-principles.md complete
- [ ] Both workflow directories accessible

### Post-Integration Checklist
- [ ] PROTOCOL-EXECUTION-PLAN.md generated
- [ ] User approval obtained
- [ ] Next protocol identified
- [ ] Handoff package delivered
