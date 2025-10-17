"""Scripts package for the Unified Developer Workflow."""

from importlib import import_module

from . import lifecycle_tasks

_LAZY_EXPORTS = {
    'AIExecutor': ('scripts.ai_executor', 'AIExecutor'),
    'AIOrchestrator': ('scripts.ai_orchestrator', 'AIOrchestrator'),
    'UnifiedBriefProcessor': ('scripts.brief_processor', 'UnifiedBriefProcessor'),
    'ComplianceValidator': ('scripts.compliance_validator', 'ComplianceValidator'),
    'EvidenceManager': ('scripts.evidence_manager', 'EvidenceManager'),
    'EvidenceSchemaConverter': ('scripts.evidence_schema_converter', 'EvidenceSchemaConverter'),
    'EvidenceMigrator': ('scripts.evidence_schema_converter', 'EvidenceMigrator'),
    'ExternalServicesManager': ('scripts.external_services', 'ExternalServicesManager'),
    'UnifiedProjectGenerator': ('scripts.project_generator_orchestration', 'UnifiedProjectGenerator'),
    'QualityGates': ('scripts.quality_gates', 'QualityGates'),
    'ReviewProtocol': ('scripts.review_protocol_loader', 'ReviewProtocol'),
    'ReviewProtocolLoader': ('scripts.review_protocol_loader', 'ReviewProtocolLoader'),
    'SystemInstructionFormatter': ('scripts.system_instruction_formatter', 'SystemInstructionFormatter'),
    'ValidationGates': ('scripts.validation_gates', 'ValidationGates'),
    'UnifiedWorkflowAutomation': ('scripts.workflow_automation', 'UnifiedWorkflowAutomation'),
}

__all__ = list(_LAZY_EXPORTS.keys()) + ['lifecycle_tasks']


def __getattr__(name):
    if name == 'lifecycle_tasks':
        return lifecycle_tasks
    if name in _LAZY_EXPORTS:
        module_name, attr_name = _LAZY_EXPORTS[name]
        module = import_module(module_name)
        value = getattr(module, attr_name)
        globals()[name] = value
        return value
    raise AttributeError(f"module 'scripts' has no attribute '{name}'")
