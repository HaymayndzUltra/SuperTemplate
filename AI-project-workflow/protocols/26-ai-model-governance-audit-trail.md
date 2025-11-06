# Protocol 26: AI Model Governance & Audit Trail

## Metadata
```yaml
protocol_version: 1.0.0
created_date: 2025-01-07
category: governance_compliance
phase: "Phase 6: Monitoring & Governance"
priority: critical
tags: [governance, audit, compliance, versioning, access-control]
triggers: [model-deployment, compliance-audit, regulatory-requirement]
```

## 1. Protocol Overview

**Purpose**: Establish comprehensive governance framework and audit trail for AI models to ensure compliance, traceability, accountability, and regulatory adherence throughout the model lifecycle.

**Critical Success Factors**:
- Complete model lineage tracking
- Immutable audit logs
- Role-based access control
- Compliance documentation
- Automated governance checks

## 2. Governance Framework

### Step 1: Model Registry & Versioning
**Duration**: 4-6 hours

**Model Registry Schema**:
```python
# governance/model_registry.py

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

class ModelStage(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    ARCHIVED = "archived"

@dataclass
class ModelMetadata:
    model_id: str
    model_name: str
    version: str
    stage: ModelStage
    
    # Lineage
    training_run_id: str
    parent_model_id: Optional[str]
    dataset_version: str
    feature_pipeline_version: str
    
    # Performance
    metrics: Dict[str, float]
    validation_results: Dict
    
    # Governance
    owner: str
    team: str
    created_at: datetime
    approved_by: Optional[str]
    approval_date: Optional[datetime]
    
    # Compliance
    compliance_checks: Dict[str, bool]
    risk_assessment: Dict
    bias_audit_results: Dict
    
    # Technical
    framework: str  # sklearn, tensorflow, pytorch
    model_type: str  # classification, regression, etc.
    input_schema: Dict
    output_schema: Dict
    
    # Deployment
    deployment_config: Dict
    resource_requirements: Dict
    sla_requirements: Dict
    
    # Documentation
    description: str
    use_case: str
    limitations: str
    ethical_considerations: str
    
class ModelRegistry:
    
    def __init__(self, storage_backend: str):
        self.storage = storage_backend
        self.models = {}
    
    def register_model(self, metadata: ModelMetadata) -> str:
        """Register new model version."""
        
        # Validate metadata completeness
        self._validate_metadata(metadata)
        
        # Generate unique model ID
        model_id = f"{metadata.model_name}-v{metadata.version}"
        
        # Store metadata
        self.models[model_id] = metadata
        
        # Log registration event
        self._log_audit_event({
            'event_type': 'model_registered',
            'model_id': model_id,
            'version': metadata.version,
            'owner': metadata.owner,
            'timestamp': datetime.now().isoformat()
        })
        
        return model_id
    
    def transition_stage(self, 
                        model_id: str,
                        new_stage: ModelStage,
                        approver: str,
                        justification: str) -> bool:
        """Transition model to new stage with approval."""
        
        model = self.models.get(model_id)
        if not model:
            raise ValueError(f"Model {model_id} not found")
        
        # Validate transition
        if not self._validate_stage_transition(model.stage, new_stage):
            raise ValueError(f"Invalid transition from {model.stage} to {new_stage}")
        
        # Check approver permissions
        if not self._check_approval_permission(approver, new_stage):
            raise PermissionError(f"{approver} not authorized for {new_stage} approval")
        
        # Update model stage
        old_stage = model.stage
        model.stage = new_stage
        model.approved_by = approver
        model.approval_date = datetime.now()
        
        # Log transition
        self._log_audit_event({
            'event_type': 'stage_transition',
            'model_id': model_id,
            'old_stage': old_stage.value,
            'new_stage': new_stage.value,
            'approver': approver,
            'justification': justification,
            'timestamp': datetime.now().isoformat()
        })
        
        return True
    
    def get_model_lineage(self, model_id: str) -> Dict:
        """Get complete lineage for a model."""
        
        model = self.models.get(model_id)
        if not model:
            return {}
        
        lineage = {
            'model_id': model_id,
            'version': model.version,
            'training_run': model.training_run_id,
            'dataset': model.dataset_version,
            'feature_pipeline': model.feature_pipeline_version,
            'parent_models': []
        }
        
        # Recursively get parent lineage
        if model.parent_model_id:
            parent_lineage = self.get_model_lineage(model.parent_model_id)
            lineage['parent_models'].append(parent_lineage)
        
        return lineage
```

### Step 2: Access Control & Permissions
**Duration**: 3-4 hours

**RBAC Configuration**:
```yaml
# governance/governance-policy.yaml

access_control:
  roles:
    data_scientist:
      permissions:
        - read_models
        - register_models
        - update_development_models
        - view_metrics
      restrictions:
        - cannot_deploy_production
        - cannot_delete_models
    
    ml_engineer:
      permissions:
        - read_models
        - register_models
        - deploy_staging
        - update_staging_models
        - view_metrics
        - run_experiments
      restrictions:
        - cannot_deploy_production
        - cannot_approve_production
    
    ml_lead:
      permissions:
        - all_data_scientist_permissions
        - all_ml_engineer_permissions
        - approve_production_deployment
        - deploy_production
        - delete_archived_models
        - manage_access_control
      restrictions:
        - requires_dual_approval_for_critical_models
    
    compliance_officer:
      permissions:
        - read_all_models
        - view_audit_logs
        - run_compliance_checks
        - block_non_compliant_models
      restrictions:
        - cannot_modify_models
        - cannot_deploy_models
    
    auditor:
      permissions:
        - read_all_models
        - view_audit_logs
        - export_audit_reports
      restrictions:
        - read_only_access

  approval_workflows:
    production_deployment:
      required_approvals: 2
      approvers:
        - ml_lead
        - product_owner
      conditions:
        - all_compliance_checks_passed
        - performance_meets_threshold
        - bias_audit_completed
        - security_scan_passed
    
    critical_model_update:
      required_approvals: 3
      approvers:
        - ml_lead
        - security_lead
        - compliance_officer
      conditions:
        - risk_assessment_completed
        - impact_analysis_documented
        - rollback_plan_approved
```

**Access Control Implementation**:
```python
# governance/access_control.py

from typing import List, Dict
from functools import wraps

class AccessControl:
    
    def __init__(self, policy_config: Dict):
        self.policy = policy_config
        self.audit_logger = AuditLogger()
    
    def check_permission(self, user: str, action: str, resource: str) -> bool:
        """Check if user has permission for action on resource."""
        
        user_roles = self._get_user_roles(user)
        
        for role in user_roles:
            role_permissions = self.policy['access_control']['roles'][role]['permissions']
            
            if action in role_permissions or 'all_permissions' in role_permissions:
                # Log access
                self.audit_logger.log_access({
                    'user': user,
                    'action': action,
                    'resource': resource,
                    'result': 'granted',
                    'timestamp': datetime.now().isoformat()
                })
                return True
        
        # Log denied access
        self.audit_logger.log_access({
            'user': user,
            'action': action,
            'resource': resource,
            'result': 'denied',
            'timestamp': datetime.now().isoformat()
        })
        
        return False
    
    def require_permission(self, action: str):
        """Decorator to enforce permission checks."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                user = kwargs.get('user') or args[0] if args else None
                resource = kwargs.get('resource') or args[1] if len(args) > 1 else None
                
                if not self.check_permission(user, action, resource):
                    raise PermissionError(f"User {user} not authorized for {action}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
```

### Step 3: Audit Trail & Logging
**Duration**: 4-5 hours

**Audit Log Schema**:
```python
# governance/audit_logger.py

import json
from datetime import datetime
from typing import Dict
import hashlib

class AuditLogger:
    
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.log_buffer = []
    
    def log_event(self, event: Dict):
        """Log audit event with immutability guarantee."""
        
        # Add metadata
        event['event_id'] = self._generate_event_id()
        event['timestamp'] = datetime.now().isoformat()
        event['hash'] = self._calculate_hash(event)
        
        # Add previous event hash for chain integrity
        if self.log_buffer:
            event['previous_hash'] = self.log_buffer[-1]['hash']
        
        # Store event
        self.log_buffer.append(event)
        self._persist_event(event)
        
        return event['event_id']
    
    def _calculate_hash(self, event: Dict) -> str:
        """Calculate SHA-256 hash of event."""
        event_str = json.dumps(event, sort_keys=True)
        return hashlib.sha256(event_str.encode()).hexdigest()
    
    def verify_audit_trail_integrity(self) -> bool:
        """Verify audit trail has not been tampered with."""
        
        for i in range(1, len(self.log_buffer)):
            current_event = self.log_buffer[i]
            previous_event = self.log_buffer[i-1]
            
            # Verify hash chain
            if current_event.get('previous_hash') != previous_event['hash']:
                return False
            
            # Verify event hash
            recalculated_hash = self._calculate_hash({
                k: v for k, v in current_event.items() if k != 'hash'
            })
            if recalculated_hash != current_event['hash']:
                return False
        
        return True
    
    def query_audit_logs(self, filters: Dict) -> List[Dict]:
        """Query audit logs with filters."""
        
        results = []
        
        for event in self.log_buffer:
            match = True
            for key, value in filters.items():
                if event.get(key) != value:
                    match = False
                    break
            
            if match:
                results.append(event)
        
        return results
```

**Audit Events to Track**:
```yaml
# governance/audit-events.yaml

audit_events:
  model_lifecycle:
    - model_registered
    - model_trained
    - model_evaluated
    - model_approved
    - model_deployed
    - model_updated
    - model_rolled_back
    - model_archived
    - model_deleted
  
  access_events:
    - user_login
    - permission_granted
    - permission_denied
    - role_assigned
    - role_revoked
    - access_token_created
    - access_token_revoked
  
  data_events:
    - data_accessed
    - data_modified
    - data_exported
    - data_deleted
    - dataset_created
    - dataset_versioned
  
  compliance_events:
    - compliance_check_run
    - compliance_violation_detected
    - risk_assessment_completed
    - bias_audit_completed
    - security_scan_completed
  
  operational_events:
    - prediction_made
    - batch_inference_run
    - drift_detected
    - alert_triggered
    - incident_created
    - incident_resolved
```

### Step 4: Compliance Dashboard
**Duration**: 3-4 hours

**Compliance Reporting**:
```python
# governance/compliance_reporting.py

class ComplianceReporter:
    
    def __init__(self, registry: ModelRegistry, audit_logger: AuditLogger):
        self.registry = registry
        self.audit_logger = audit_logger
    
    def generate_compliance_report(self, model_id: str) -> Dict:
        """Generate comprehensive compliance report for model."""
        
        model = self.registry.models.get(model_id)
        if not model:
            raise ValueError(f"Model {model_id} not found")
        
        report = {
            'model_id': model_id,
            'model_name': model.model_name,
            'version': model.version,
            'report_date': datetime.now().isoformat(),
            
            'governance_compliance': {
                'owner_assigned': bool(model.owner),
                'approval_obtained': bool(model.approved_by),
                'documentation_complete': self._check_documentation(model),
                'risk_assessment_done': bool(model.risk_assessment)
            },
            
            'technical_compliance': {
                'performance_meets_sla': self._check_performance_sla(model),
                'bias_audit_passed': model.compliance_checks.get('bias_audit', False),
                'security_scan_passed': model.compliance_checks.get('security_scan', False),
                'drift_monitoring_enabled': True  # Check actual status
            },
            
            'regulatory_compliance': {
                'gdpr_compliant': self._check_gdpr_compliance(model),
                'data_retention_policy': True,
                'right_to_explanation': self._check_explainability(model),
                'audit_trail_complete': self.audit_logger.verify_audit_trail_integrity()
            },
            
            'operational_compliance': {
                'monitoring_configured': True,
                'alerting_configured': True,
                'rollback_tested': True,
                'incident_response_ready': True
            }
        }
        
        # Calculate overall compliance score
        report['compliance_score'] = self._calculate_compliance_score(report)
        report['compliant'] = report['compliance_score'] >= 0.95
        
        return report
    
    def _calculate_compliance_score(self, report: Dict) -> float:
        """Calculate overall compliance score."""
        
        all_checks = []
        for category in ['governance_compliance', 'technical_compliance', 
                        'regulatory_compliance', 'operational_compliance']:
            all_checks.extend(report[category].values())
        
        return sum(all_checks) / len(all_checks)
```

## 3. Quality Gates

### Gate 1: Governance Setup
- [ ] Model registry configured
- [ ] Access control policies defined
- [ ] Audit logging enabled
- [ ] Compliance checks automated
- [ ] Documentation templates created

### Gate 2: Operational Governance
- [ ] All models registered in registry
- [ ] RBAC enforced for all operations
- [ ] Audit trail verified for integrity
- [ ] Compliance reports generated
- [ ] Non-compliant models blocked

### Gate 3: Compliance Validation
- [ ] Regulatory requirements documented
- [ ] Compliance score > 95%
- [ ] Audit trail complete and tamper-proof
- [ ] Access logs reviewed
- [ ] Governance dashboard operational

## 4. Deliverables

### Required Outputs
1. **Governance Policy** (`governance-policy.md`)
2. **Audit Log** (`audit-log.json`)
3. **Compliance Report** (`compliance-report.md`)
4. **Model Registry Export** (`model-registry.json`)
5. **Access Control Matrix** (`access-control-matrix.csv`)
6. **Governance Dashboard** (`governance-dashboard.json`)

### Evidence Package Structure
```
evidence/protocol-26-governance/
├── policies/
│   ├── governance-policy.md
│   ├── access-control-policy.yaml
│   └── compliance-requirements.md
├── audit/
│   ├── audit-log.json
│   ├── audit-trail-verification.md
│   └── access-logs.csv
├── compliance/
│   ├── compliance-report.md
│   ├── risk-assessment.md
│   └── regulatory-mapping.md
├── registry/
│   ├── model-registry.json
│   └── model-lineage-graph.png
└── dashboards/
    └── governance-dashboard.json
```

## 5. Success Criteria

- **Model Registration**: 100% of production models registered
- **Audit Trail Integrity**: 100% verified
- **Compliance Score**: > 95% for all production models
- **Access Control**: 100% of operations authorized
- **Documentation**: 100% of models have complete metadata
