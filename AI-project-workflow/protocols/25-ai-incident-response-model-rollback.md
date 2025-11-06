# Protocol 25: AI Incident Response & Model Rollback

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: mlops_operations
phase: "Phase 6: Monitoring & Governance"
priority: critical
tags: [incident-response, rollback, emergency, postmortem, sre]
triggers: [production-incident, model-failure, critical-alert]
```

## 1. Protocol Overview

**Purpose**: Establish rapid incident response procedures and automated rollback mechanisms to minimize impact of model failures, maintain service reliability, and learn from incidents through structured postmortems.

**Critical Success Factors**:
- Rapid incident detection (< 5 minutes)
- Fast rollback capability (< 2 minutes)
- Clear escalation procedures
- Comprehensive incident documentation
- Continuous improvement from learnings

## 2. Incident Response Workflow

### Step 1: Incident Classification
**Duration**: < 5 minutes

**Incident Severity Levels**:
```yaml
# incident_response/incident-playbook.yaml

incident_severity_levels:
  P0_CRITICAL:
    description: "Complete service outage or data loss"
    examples:
      - Model serving endpoint completely down
      - Predictions returning all errors
      - Data corruption in production
      - Security breach
    response_time: "Immediate (< 5 min)"
    escalation: "Page on-call + ML lead + CTO"
    communication: "Status page + customer notifications"
    
  P1_HIGH:
    description: "Severe performance degradation affecting users"
    examples:
      - Model accuracy dropped > 20%
      - Latency increased > 200%
      - Error rate > 10%
      - Partial service degradation
    response_time: "< 15 minutes"
    escalation: "Page on-call + ML lead"
    communication: "Internal stakeholders + status page"
    
  P2_MEDIUM:
    description: "Moderate impact, workaround available"
    examples:
      - Model accuracy dropped 10-20%
      - Latency increased 50-200%
      - Error rate 5-10%
      - Non-critical feature broken
    response_time: "< 1 hour"
    escalation: "Notify on-call"
    communication: "Internal team notification"
    
  P3_LOW:
    description: "Minor issue, minimal user impact"
    examples:
      - Model accuracy dropped 5-10%
      - Latency increased 20-50%
      - Error rate 2-5%
      - Monitoring alert triggered
    response_time: "< 4 hours"
    escalation: "Ticket to team"
    communication: "Team chat notification"
    
  P4_INFORMATIONAL:
    description: "No immediate impact, proactive fix needed"
    examples:
      - Drift detected but within acceptable range
      - Resource utilization trending up
      - Minor configuration issue
    response_time: "< 24 hours"
    escalation: "None"
    communication: "Logged for review"
```

**Incident Classification Logic**:
```python
# incident_response/incident_classifier.py

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List

class IncidentSeverity(Enum):
    P0_CRITICAL = "P0"
    P1_HIGH = "P1"
    P2_MEDIUM = "P2"
    P3_LOW = "P3"
    P4_INFORMATIONAL = "P4"

@dataclass
class Incident:
    incident_id: str
    severity: IncidentSeverity
    title: str
    description: str
    detected_at: str
    affected_services: List[str]
    metrics: Dict
    
class IncidentClassifier:
    
    def classify_incident(self, alert_data: Dict) -> Incident:
        """Automatically classify incident severity."""
        
        severity = self._determine_severity(alert_data)
        
        incident = Incident(
            incident_id=self._generate_incident_id(),
            severity=severity,
            title=self._generate_title(alert_data),
            description=alert_data.get('description', ''),
            detected_at=datetime.now().isoformat(),
            affected_services=alert_data.get('affected_services', []),
            metrics=alert_data.get('metrics', {})
        )
        
        return incident
    
    def _determine_severity(self, alert_data: Dict) -> IncidentSeverity:
        """Determine incident severity based on metrics."""
        
        metrics = alert_data.get('metrics', {})
        
        # P0: Complete outage
        if metrics.get('availability', 1.0) < 0.5:
            return IncidentSeverity.P0_CRITICAL
        
        if metrics.get('error_rate', 0) > 0.5:
            return IncidentSeverity.P0_CRITICAL
        
        # P1: Severe degradation
        if metrics.get('accuracy_drop', 0) > 0.2:
            return IncidentSeverity.P1_HIGH
        
        if metrics.get('latency_increase_pct', 0) > 2.0:
            return IncidentSeverity.P1_HIGH
        
        if metrics.get('error_rate', 0) > 0.1:
            return IncidentSeverity.P1_HIGH
        
        # P2: Moderate impact
        if metrics.get('accuracy_drop', 0) > 0.1:
            return IncidentSeverity.P2_MEDIUM
        
        if metrics.get('latency_increase_pct', 0) > 0.5:
            return IncidentSeverity.P2_MEDIUM
        
        if metrics.get('error_rate', 0) > 0.05:
            return IncidentSeverity.P2_MEDIUM
        
        # P3: Minor issue
        if metrics.get('accuracy_drop', 0) > 0.05:
            return IncidentSeverity.P3_LOW
        
        # P4: Informational
        return IncidentSeverity.P4_INFORMATIONAL
    
    def _generate_incident_id(self) -> str:
        """Generate unique incident ID."""
        return f"INC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    def _generate_title(self, alert_data: Dict) -> str:
        """Generate incident title."""
        alert_name = alert_data.get('alert_name', 'Unknown Alert')
        return f"{alert_name} - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
```

### Step 2: Emergency Response Procedures
**Duration**: Immediate

**Response Runbook**:
```python
# incident_response/response_procedures.py

class IncidentResponseCoordinator:
    
    def __init__(self, config: Dict):
        self.config = config
        self.active_incidents = {}
    
    def handle_incident(self, incident: Incident):
        """Coordinate incident response."""
        
        # Log incident
        self._log_incident(incident)
        
        # Notify stakeholders
        self._notify_stakeholders(incident)
        
        # Execute response based on severity
        if incident.severity == IncidentSeverity.P0_CRITICAL:
            self._handle_p0_incident(incident)
        elif incident.severity == IncidentSeverity.P1_HIGH:
            self._handle_p1_incident(incident)
        else:
            self._handle_lower_priority_incident(incident)
        
        # Track incident
        self.active_incidents[incident.incident_id] = incident
    
    def _handle_p0_incident(self, incident: Incident):
        """Handle P0 critical incident."""
        
        logging.critical(f"P0 INCIDENT: {incident.title}")
        
        # 1. Immediate actions
        actions = [
            "Create incident war room",
            "Page on-call engineer",
            "Notify ML lead and CTO",
            "Update status page",
            "Initiate automatic rollback if applicable"
        ]
        
        # 2. Execute automatic rollback
        if self._should_auto_rollback(incident):
            logging.info("Initiating automatic rollback")
            rollback_result = self._execute_rollback()
            incident.metrics['rollback_executed'] = True
            incident.metrics['rollback_result'] = rollback_result
        
        # 3. Start incident timeline
        self._start_incident_timeline(incident)
        
        # 4. Engage incident commander
        self._assign_incident_commander(incident)
    
    def _handle_p1_incident(self, incident: Incident):
        """Handle P1 high severity incident."""
        
        logging.error(f"P1 INCIDENT: {incident.title}")
        
        # 1. Notify on-call and ML lead
        self._page_oncall(incident)
        
        # 2. Assess if rollback needed
        if self._assess_rollback_need(incident):
            self._execute_rollback()
        
        # 3. Start investigation
        self._start_investigation(incident)
    
    def _should_auto_rollback(self, incident: Incident) -> bool:
        """Determine if automatic rollback should be triggered."""
        
        auto_rollback_conditions = [
            incident.metrics.get('error_rate', 0) > 0.5,
            incident.metrics.get('availability', 1.0) < 0.5,
            incident.metrics.get('accuracy_drop', 0) > 0.3
        ]
        
        return any(auto_rollback_conditions)
```

### Step 3: Automated Rollback Mechanism
**Duration**: < 2 minutes

**Rollback Script**:
```bash
#!/bin/bash
# incident_response/rollback-script.sh

set -e

INCIDENT_ID=$1
ROLLBACK_VERSION=$2
ENVIRONMENT=${3:-production}

echo "=== EMERGENCY ROLLBACK INITIATED ==="
echo "Incident ID: $INCIDENT_ID"
echo "Rolling back to version: $ROLLBACK_VERSION"
echo "Environment: $ENVIRONMENT"
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# 1. Verify rollback version exists
echo "Step 1: Verifying rollback version..."
if ! kubectl get deployment model-serving-$ROLLBACK_VERSION -n $ENVIRONMENT &> /dev/null; then
    echo "ERROR: Rollback version $ROLLBACK_VERSION not found"
    exit 1
fi

# 2. Create rollback snapshot
echo "Step 2: Creating pre-rollback snapshot..."
kubectl get deployment model-serving -n $ENVIRONMENT -o yaml > /tmp/pre-rollback-snapshot-$INCIDENT_ID.yaml

# 3. Update traffic routing (immediate)
echo "Step 3: Routing 100% traffic to stable version..."
kubectl patch service model-serving -n $ENVIRONMENT -p '{"spec":{"selector":{"version":"'$ROLLBACK_VERSION'"}}}'

# 4. Scale down problematic version
echo "Step 4: Scaling down problematic deployment..."
kubectl scale deployment model-serving-current -n $ENVIRONMENT --replicas=0

# 5. Verify rollback success
echo "Step 5: Verifying rollback..."
sleep 10
ERROR_RATE=$(curl -s http://prometheus:9090/api/v1/query?query=rate(model_errors_total[1m]) | jq -r '.data.result[0].value[1]')

if (( $(echo "$ERROR_RATE < 0.05" | bc -l) )); then
    echo "✓ Rollback successful - Error rate: $ERROR_RATE"
else
    echo "⚠ Warning: Error rate still elevated: $ERROR_RATE"
fi

# 6. Log rollback event
echo "Step 6: Logging rollback event..."
curl -X POST http://audit-service/api/events \
    -H "Content-Type: application/json" \
    -d "{
        \"event_type\": \"model_rollback\",
        \"incident_id\": \"$INCIDENT_ID\",
        \"rollback_version\": \"$ROLLBACK_VERSION\",
        \"timestamp\": \"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\",
        \"environment\": \"$ENVIRONMENT\"
    }"

# 7. Notify stakeholders
echo "Step 7: Sending notifications..."
curl -X POST $SLACK_WEBHOOK_URL \
    -H "Content-Type: application/json" \
    -d "{
        \"text\": \"🔄 Emergency rollback completed for incident $INCIDENT_ID\",
        \"attachments\": [{
            \"color\": \"warning\",
            \"fields\": [
                {\"title\": \"Rollback Version\", \"value\": \"$ROLLBACK_VERSION\", \"short\": true},
                {\"title\": \"Environment\", \"value\": \"$ENVIRONMENT\", \"short\": true},
                {\"title\": \"Error Rate\", \"value\": \"$ERROR_RATE\", \"short\": true}
            ]
        }]
    }"

echo "=== ROLLBACK COMPLETE ==="
echo "Duration: $SECONDS seconds"
```

**Rollback Automation**:
```python
# incident_response/rollback_automation.py

import subprocess
import logging
from typing import Dict

class RollbackAutomation:
    
    def __init__(self, config: Dict):
        self.config = config
        self.rollback_history = []
    
    def execute_rollback(self, incident_id: str, target_version: str = None) -> Dict:
        """Execute automated rollback."""
        
        start_time = datetime.now()
        
        # Determine target version
        if not target_version:
            target_version = self._get_last_stable_version()
        
        logging.info(f"Executing rollback to version {target_version}")
        
        try:
            # Run rollback script
            result = subprocess.run(
                [
                    '/bin/bash',
                    'incident_response/rollback-script.sh',
                    incident_id,
                    target_version,
                    self.config['environment']
                ],
                capture_output=True,
                text=True,
                timeout=120  # 2 minute timeout
            )
            
            duration = (datetime.now() - start_time).total_seconds()
            
            if result.returncode == 0:
                rollback_record = {
                    'incident_id': incident_id,
                    'target_version': target_version,
                    'status': 'success',
                    'duration_seconds': duration,
                    'timestamp': start_time.isoformat(),
                    'output': result.stdout
                }
                
                self.rollback_history.append(rollback_record)
                
                logging.info(f"Rollback completed successfully in {duration:.2f}s")
                return rollback_record
            else:
                logging.error(f"Rollback failed: {result.stderr}")
                return {
                    'incident_id': incident_id,
                    'status': 'failed',
                    'error': result.stderr,
                    'duration_seconds': duration
                }
                
        except subprocess.TimeoutExpired:
            logging.error("Rollback timed out after 2 minutes")
            return {
                'incident_id': incident_id,
                'status': 'timeout',
                'error': 'Rollback exceeded 2 minute timeout'
            }
        except Exception as e:
            logging.error(f"Rollback exception: {str(e)}")
            return {
                'incident_id': incident_id,
                'status': 'error',
                'error': str(e)
            }
    
    def _get_last_stable_version(self) -> str:
        """Get the last known stable model version."""
        
        # Query model registry for last stable version
        # Check deployment history
        # Return version that was stable for > 24 hours
        pass
    
    def verify_rollback_success(self, incident_id: str) -> bool:
        """Verify that rollback resolved the issue."""
        
        # Wait for metrics to stabilize
        time.sleep(30)
        
        # Check current metrics
        current_metrics = self._get_current_metrics()
        
        # Compare with thresholds
        success_criteria = {
            'error_rate': current_metrics['error_rate'] < 0.05,
            'latency_p95': current_metrics['latency_p95'] < 200,
            'availability': current_metrics['availability'] > 0.99
        }
        
        return all(success_criteria.values())
```

### Step 4: Post-Incident Review
**Duration**: 1-2 hours (within 24 hours of resolution)

**Postmortem Template**:
```markdown
# incident_response/postmortem-template.md

# Incident Postmortem: [INCIDENT_ID]

## Incident Summary
- **Incident ID**: [INC-YYYYMMDD-HHMMSS]
- **Severity**: [P0/P1/P2/P3/P4]
- **Status**: [Resolved/Mitigated/Monitoring]
- **Date**: [YYYY-MM-DD]
- **Duration**: [X hours Y minutes]
- **Impact**: [Description of user/business impact]

## Timeline
| Time (UTC) | Event |
|------------|-------|
| HH:MM | Incident detected via [alert/manual report] |
| HH:MM | Incident classified as [severity] |
| HH:MM | On-call engineer paged |
| HH:MM | Investigation started |
| HH:MM | Root cause identified |
| HH:MM | Mitigation applied (rollback/fix) |
| HH:MM | Service restored |
| HH:MM | Incident resolved |

## Root Cause Analysis

### What Happened
[Detailed description of what went wrong]

### Why It Happened
[Root cause - technical, process, or human factors]

### Contributing Factors
- [Factor 1]
- [Factor 2]
- [Factor 3]

## Impact Assessment

### User Impact
- **Users Affected**: [number/percentage]
- **Duration**: [time period]
- **Severity**: [description]

### Business Impact
- **Revenue Impact**: [$amount or N/A]
- **SLA Breach**: [Yes/No - details]
- **Reputation**: [description]

### Technical Impact
- **Services Affected**: [list]
- **Data Loss**: [Yes/No - details]
- **Performance Degradation**: [metrics]

## Resolution

### Immediate Actions Taken
1. [Action 1 - who, what, when]
2. [Action 2]
3. [Action 3]

### Rollback Details
- **Rollback Version**: [version]
- **Rollback Duration**: [X minutes]
- **Rollback Success**: [Yes/No]

## Lessons Learned

### What Went Well
- [Positive aspect 1]
- [Positive aspect 2]

### What Went Wrong
- [Issue 1]
- [Issue 2]

### Where We Got Lucky
- [Lucky break 1]
- [Lucky break 2]

## Action Items

| Action | Owner | Priority | Due Date | Status |
|--------|-------|----------|----------|--------|
| [Preventive action 1] | [Name] | High | YYYY-MM-DD | Open |
| [Monitoring improvement] | [Name] | Medium | YYYY-MM-DD | Open |
| [Process update] | [Name] | Low | YYYY-MM-DD | Open |

## Prevention Measures

### Short-term (< 1 week)
- [ ] [Action 1]
- [ ] [Action 2]

### Medium-term (1-4 weeks)
- [ ] [Action 1]
- [ ] [Action 2]

### Long-term (> 1 month)
- [ ] [Action 1]
- [ ] [Action 2]

## Appendix

### Related Incidents
- [INC-XXXXXX] - [Brief description]

### Metrics & Graphs
[Attach relevant graphs and metrics]

### Communication Log
[Key communications during incident]

---
**Postmortem Completed By**: [Name]
**Date**: [YYYY-MM-DD]
**Reviewed By**: [Names]
```

## 3. Quality Gates

### Gate 1: Response Readiness
- [ ] Incident classification system configured
- [ ] On-call rotation established
- [ ] Escalation procedures documented
- [ ] Rollback scripts tested
- [ ] Communication channels configured

### Gate 2: Incident Handling
- [ ] Incident detected within SLA
- [ ] Appropriate severity assigned
- [ ] Stakeholders notified per procedure
- [ ] Mitigation actions executed
- [ ] Service restored within target time

### Gate 3: Post-Incident
- [ ] Postmortem completed within 24 hours
- [ ] Root cause identified
- [ ] Action items assigned with owners
- [ ] Lessons learned documented
- [ ] Prevention measures implemented

## 4. Deliverables

### Required Outputs
1. **Incident Playbook** (`incident-playbook.md`)
2. **Rollback Script** (`rollback-script.sh`)
3. **Postmortem Template** (`postmortem-template.md`)
4. **Incident Log** (`incident-log.json`)
5. **Response Metrics Dashboard** (`response-metrics.json`)

### Evidence Package Structure
```
evidence/protocol-25-incident-response/
├── playbooks/
│   ├── incident-playbook.md
│   ├── p0-response-procedure.md
│   └── p1-response-procedure.md
├── scripts/
│   ├── rollback-script.sh
│   ├── rollback_automation.py
│   └── incident_classifier.py
├── postmortems/
│   ├── postmortem-template.md
│   └── [incident-id]-postmortem.md
└── logs/
    ├── incident-log.json
    └── rollback-history.json
```

## 5. Success Criteria

- **Detection Time**: < 5 minutes for P0/P1 incidents
- **Rollback Time**: < 2 minutes execution
- **MTTR (Mean Time to Recovery)**: < 30 minutes for P0, < 2 hours for P1
- **Postmortem Completion**: 100% within 24 hours
- **Action Item Completion**: > 90% within due dates
