#!/usr/bin/env python3
"""
Validator Pre-Check System for Protocol Creation

Provides real-time validator compliance scoring during protocol creation,
allowing early identification and resolution of compliance issues.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

class ValidatorPreChecker:
    """Real-time validator compliance checking during protocol creation"""
    
    def __init__(self, protocol_number: str = "unknown"):
        self.protocol_number = protocol_number
        self.validator_weights = {
            'validator_1_protocol_identity': 0.10,
            'validator_2_ai_role': 0.10,
            'validator_3_workflow_algorithm': 0.10,
            'validator_4_quality_gates': 0.10,
            'validator_5_script_integration': 0.10,
            'validator_6_communication_protocol': 0.10,
            'validator_7_evidence_package': 0.10,
            'validator_8_handoff_checklist': 0.10,
            'validator_9_cognitive_reasoning': 0.05,
            'validator_10_meta_reflection': 0.05
        }
        
        # Section to validator mapping
        self.section_validator_map = {
            'frontmatter': ['validator_1_protocol_identity'],
            'prerequisites': ['validator_1_protocol_identity'],
            'ai_role': ['validator_2_ai_role'],
            'workflow': ['validator_3_workflow_algorithm'],
            'quality_gates': ['validator_4_quality_gates'],
            'automation_hooks': ['validator_5_script_integration'],
            'communication_protocols': ['validator_6_communication_protocol'],
            'evidence_summary': ['validator_7_evidence_package'],
            'handoff_checklist': ['validator_8_handoff_checklist'],
            'reasoning_blocks': ['validator_9_cognitive_reasoning'],
            'meta_reflection': ['validator_10_meta_reflection']
        }

    def check_protocol_identity(self, content: str) -> Dict[str, Any]:
        """Check Validator 1: Protocol Identity compliance"""
        score = 0.0
        checks = {
            'protocol_number_present': False,
            'protocol_name_present': False,
            'mission_statement_present': False,
            'prerequisites_present': False,
            'integration_points_present': False
        }
        
        # Check protocol number
        if re.search(r'PROTOCOL\s+\d+:', content, re.IGNORECASE):
            checks['protocol_number_present'] = True
            score += 0.2
        
        # Check protocol name
        if re.search(r'PROTOCOL\s+\d+:\s+[^-\n]+', content, re.IGNORECASE):
            checks['protocol_name_present'] = True
            score += 0.2
        
        # Check mission statement
        if re.search(r'Mission:|Purpose:', content, re.IGNORECASE):
            checks['mission_statement_present'] = True
            score += 0.2
        
        # Check prerequisites
        if re.search(r'##\s*PREREQUISITES', content, re.IGNORECASE):
            checks['prerequisites_present'] = True
            score += 0.2
        
        # Check integration points
        if re.search(r'##\s*INTEGRATION\s+POINTS|Inputs From|Outputs To', content, re.IGNORECASE):
            checks['integration_points_present'] = True
            score += 0.2
        
        return {
            'validator': 'validator_1_protocol_identity',
            'score': score,
            'checks': checks,
            'recommendations': self._get_protocol_identity_recommendations(checks)
        }

    def check_ai_role(self, content: str) -> Dict[str, Any]:
        """Check Validator 2: AI Role compliance"""
        score = 0.0
        checks = {
            'role_title_present': False,
            'mission_statement_present': False,
            'capabilities_present': False,
            'constraints_present': False,
            'behavioral_patterns_present': False
        }
        
        # Check AI role section
        ai_role_match = re.search(r'##\s*AI\s+ROLE.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if ai_role_match:
            ai_role_content = ai_role_match.group(0)
            
            # Check role title
            if re.search(r'You are a|Role:|Persona:', ai_role_content, re.IGNORECASE):
                checks['role_title_present'] = True
                score += 0.2
            
            # Check mission statement
            if re.search(r'Mission:|Your mission is|objective:', ai_role_content, re.IGNORECASE):
                checks['mission_statement_present'] = True
                score += 0.2
            
            # Check capabilities
            if re.search(r'Capabilities:|Core capabilities|Skills:', ai_role_content, re.IGNORECASE):
                checks['capabilities_present'] = True
                score += 0.2
            
            # Check constraints
            if re.search(r'\[STRICT\]|\[CRITICAL\]|Constraints:|must not|cannot', ai_role_content, re.IGNORECASE):
                checks['constraints_present'] = True
                score += 0.2
            
            # Check behavioral patterns
            if re.search(r'Communication style|Decision authority|Behavior:', ai_role_content, re.IGNORECASE):
                checks['behavioral_patterns_present'] = True
                score += 0.2
        
        return {
            'validator': 'validator_2_ai_role',
            'score': score,
            'checks': checks,
            'recommendations': self._get_ai_role_recommendations(checks)
        }

    def check_workflow_algorithm(self, content: str) -> Dict[str, Any]:
        """Check Validator 3: Workflow Algorithm compliance"""
        score = 0.0
        checks = {
            'phases_present': False,
            'steps_numbered': False,
            'directives_used': False,
            'halt_conditions_present': False,
            'evidence_specified': False
        }
        
        # Check workflow section
        workflow_match = re.search(r'##\s*WORKFLOW.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if workflow_match:
            workflow_content = workflow_match.group(0)
            
            # Check phases
            phases = re.findall(r'###\s*PHASE\s+\d+:', workflow_content, re.IGNORECASE)
            if len(phases) >= 2:
                checks['phases_present'] = True
                score += 0.2
            
            # Check numbered steps
            steps = re.findall(r'^\s*\d+\.\s+\*\*\[.*?\]\*', workflow_content, re.MULTILINE)
            if len(steps) >= 3:
                checks['steps_numbered'] = True
                score += 0.2
            
            # Check directives
            directives = re.findall(r'\*\*\[(CRITICAL|MUST|GUIDELINE)\]\*', workflow_content)
            if len(directives) >= 2:
                checks['directives_used'] = True
                score += 0.2
            
            # Check halt conditions
            if re.search(r'HALT\s+AND\s+AWAIT|await.*confirmation', workflow_content, re.IGNORECASE):
                checks['halt_conditions_present'] = True
                score += 0.2
            
            # Check evidence specification
            if re.search(r'Evidence:|evidence.*\.md|\.json|\.yaml', workflow_content, re.IGNORECASE):
                checks['evidence_specified'] = True
                score += 0.2
        
        return {
            'validator': 'validator_3_workflow_algorithm',
            'score': score,
            'checks': checks,
            'recommendations': self._get_workflow_recommendations(checks)
        }

    def check_quality_gates(self, content: str) -> Dict[str, Any]:
        """Check Validator 4: Quality Gates compliance"""
        score = 0.0
        checks = {
            'gates_defined': False,
            'criteria_specified': False,
            'thresholds_measurable': False,
            'failure_actions_defined': False,
            'automation_referenced': False
        }
        
        # Check quality gates section
        qg_match = re.search(r'##\s*QUALITY\s+GATES.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if qg_match:
            qg_content = qg_match.group(0)
            
            # Check gates defined
            gates = re.findall(r'###\s*Gate\s+\d+:', qg_content, re.IGNORECASE)
            if len(gates) >= 2:
                checks['gates_defined'] = True
                score += 0.2
            
            # Check criteria specified
            criteria = re.findall(r'-\s*\*\*Criteria:\*\*', qg_content, re.IGNORECASE)
            if len(criteria) >= 1:
                checks['criteria_specified'] = True
                score += 0.2
            
            # Check thresholds measurable
            thresholds = re.findall(r'-\s*\*\*Threshold:\*\*.*?\d+%', qg_content, re.IGNORECASE)
            if len(thresholds) >= 1:
                checks['thresholds_measurable'] = True
                score += 0.2
            
            # Check failure actions
            actions = re.findall(r'-\s*\*\*Action\s+on\s+Failure:\*\*', qg_content, re.IGNORECASE)
            if len(actions) >= 1:
                checks['failure_actions_defined'] = True
                score += 0.2
            
            # Check automation referenced
            if re.search(r'automation|script|validator', qg_content, re.IGNORECASE):
                checks['automation_referenced'] = True
                score += 0.2
        
        return {
            'validator': 'validator_4_quality_gates',
            'score': score,
            'checks': checks,
            'recommendations': self._get_quality_gates_recommendations(checks)
        }

    def check_script_integration(self, content: str) -> Dict[str, Any]:
        """Check Validator 5: Script Integration compliance"""
        score = 0.0
        checks = {
            'scripts_referenced': False,
            'command_syntax_correct': False,
            'parameters_documented': False,
            'manual_fallback_present': False,
            'error_handling_mentioned': False
        }
        
        # Check automation hooks section
        ah_match = re.search(r'##\s*AUTOMATION\s+HOOKS.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if ah_match:
            ah_content = ah_match.group(0)
            
            # Check scripts referenced
            scripts = re.findall(r'python\s+.*?\.py', ah_content, re.IGNORECASE)
            if len(scripts) >= 1:
                checks['scripts_referenced'] = True
                score += 0.2
            
            # Check command syntax
            if re.search(r'--\w+\s+\[.*?\]', ah_content):
                checks['command_syntax_correct'] = True
                score += 0.2
            
            # Check parameters documented
            if re.search(r'--input|--output|--optional', ah_content, re.IGNORECASE):
                checks['parameters_documented'] = True
                score += 0.2
            
            # Check manual fallback
            if re.search(r'Manual\s+Fallback|fallback.*manual', ah_content, re.IGNORECASE):
                checks['manual_fallback_present'] = True
                score += 0.2
            
            # Check error handling
            if re.search(r'error|fail|exception', ah_content, re.IGNORECASE):
                checks['error_handling_mentioned'] = True
                score += 0.2
        
        return {
            'validator': 'validator_5_script_integration',
            'score': score,
            'checks': checks,
            'recommendations': self._get_script_integration_recommendations(checks)
        }

    def check_communication_protocol(self, content: str) -> Dict[str, Any]:
        """Check Validator 6: Communication Protocol compliance"""
        score = 0.0
        checks = {
            'status_announcements_defined': False,
            'user_interaction_templates': False,
            'error_messaging_specified': False,
            'progress_updates_included': False,
            'phase_transitions_marked': False
        }
        
        # Check communication protocols section
        cp_match = re.search(r'##\s*COMMUNICATION\s+PROTOCOLS.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if cp_match:
            cp_content = cp_match.group(0)
            
            # Check status announcements
            if re.search(r'Status\s+Announcements|Phase\s+Start|PHASE.*START', cp_content, re.IGNORECASE):
                checks['status_announcements_defined'] = True
                score += 0.2
            
            # Check user interaction templates
            if re.search(r'User\s+Interaction|Reply.*to.*continue|confirmation', cp_content, re.IGNORECASE):
                checks['user_interaction_templates'] = True
                score += 0.2
            
            # Check error messaging
            if re.search(r'Error\s+Messaging|CRITICAL.*Issue|WARNING', cp_content, re.IGNORECASE):
                checks['error_messaging_specified'] = True
                score += 0.2
            
            # Check progress updates
            if re.search(r'Progress\s+Updates|PHASE.*current|evidence.*created', cp_content, re.IGNORECASE):
                checks['progress_updates_included'] = True
                score += 0.2
            
            # Check phase transitions
            if re.search(r'Phase.*COMPLETE|HALT.*AND.*AWAIT|checkpoint', cp_content, re.IGNORECASE):
                checks['phase_transitions_marked'] = True
                score += 0.2
        
        return {
            'validator': 'validator_6_communication_protocol',
            'score': score,
            'checks': checks,
            'recommendations': self._get_communication_recommendations(checks)
        }

    def check_evidence_package(self, content: str) -> Dict[str, Any]:
        """Check Validator 7: Evidence Package compliance"""
        score = 0.0
        checks = {
            'artifacts_specified': False,
            'manifest_structure_defined': False,
            'validation_reports_included': False,
            'storage_locations_specified': False,
            'audit_trail_present': False
        }
        
        # Check evidence summary section
        es_match = re.search(r'##\s*EVIDENCE\s+SUMMARY.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if es_match:
            es_content = es_match.group(0)
            
            # Check artifacts specified
            if re.search(r'Generated\s+Artifacts|Artifact.*Purpose.*Format', es_content, re.IGNORECASE):
                checks['artifacts_specified'] = True
                score += 0.2
            
            # Check manifest structure
            if re.search(r'Evidence\s+Manifest|manifest.*structure|execution_id', es_content, re.IGNORECASE):
                checks['manifest_structure_defined'] = True
                score += 0.2
            
            # Check validation reports
            if re.search(r'Validation\s+Reports|validation.*report|compliance.*review', es_content, re.IGNORECASE):
                checks['validation_reports_included'] = True
                score += 0.2
            
            # Check storage locations
            if re.search(r'Storage\s+Locations|\.artifacts.*protocol|phase.*directory', es_content, re.IGNORECASE):
                checks['storage_locations_specified'] = True
                score += 0.2
            
            # Check audit trail
            if re.search(r'audit.*trail|checksum|timestamp', es_content, re.IGNORECASE):
                checks['audit_trail_present'] = True
                score += 0.2
        
        return {
            'validator': 'validator_7_evidence_package',
            'score': score,
            'checks': checks,
            'recommendations': self._get_evidence_recommendations(checks)
        }

    def check_handoff_checklist(self, content: str) -> Dict[str, Any]:
        """Check Validator 8: Handoff Checklist compliance"""
        score = 0.0
        checks = {
            'verification_procedures': False,
            'stakeholder_signoffs': False,
            'transition_support': False,
            'completion_criteria': False,
            'rollback_mentioned': False
        }
        
        # Check handoff checklist section
        hc_match = re.search(r'##\s*HANDOFF\s+CHECKLIST.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if hc_match:
            hc_content = hc_match.group(0)
            
            # Check verification procedures
            if re.search(r'Verification\s+Procedures|Phase.*Complete', hc_content, re.IGNORECASE):
                checks['verification_procedures'] = True
                score += 0.2
            
            # Check stakeholder sign-offs
            if re.search(r'Stakeholder\s+Sign-off|sign.*off.*requirements', hc_content, re.IGNORECASE):
                checks['stakeholder_signoffs'] = True
                score += 0.2
            
            # Check transition support
            if re.search(r'Transition\s+Support|documentation.*artifacts', hc_content, re.IGNORECASE):
                checks['transition_support'] = True
                score += 0.2
            
            # Check completion criteria
            if re.search(r'Completion\s+Criteria|Minimum.*signoffs', hc_content, re.IGNORECASE):
                checks['completion_criteria'] = True
                score += 0.2
            
            # Check rollback mentioned
            if re.search(r'rollback|recovery|emergency', hc_content, re.IGNORECASE):
                checks['rollback_mentioned'] = True
                score += 0.2
        
        return {
            'validator': 'validator_8_handoff_checklist',
            'score': score,
            'checks': checks,
            'recommendations': self._get_handoff_recommendations(checks)
        }

    def check_cognitive_reasoning(self, content: str) -> Dict[str, Any]:
        """Check Validator 9: Cognitive Reasoning compliance"""
        score = 0.0
        checks = {
            'reasoning_blocks_present': False,
            'decision_documentation': False,
            'alternatives_considered': False,
            'risk_assessment': False,
            'evidence_based_decisions': False
        }
        
        # Check for reasoning blocks
        reasoning_blocks = re.findall(r'\*\*\[REASONING\]\*', content, re.IGNORECASE)
        if len(reasoning_blocks) >= 1:
            checks['reasoning_blocks_present'] = True
            score += 0.2
        
        # Check decision documentation
        if re.search(r'Decision:|chosen.*approach|selected.*method', content, re.IGNORECASE):
            checks['decision_documentation'] = True
            score += 0.2
        
        # Check alternatives considered
        if re.search(r'Alternatives\s+Considered:|other.*options|alternative.*approach', content, re.IGNORECASE):
            checks['alternatives_considered'] = True
            score += 0.2
        
        # Check risk assessment
        if re.search(r'Risks.*Mitigations:|risk.*assessment|mitigation.*strategy', content, re.IGNORECASE):
            checks['risk_assessment'] = True
            score += 0.2
        
        # Check evidence-based decisions
        if re.search(r'Evidence:|based.*on.*evidence|supported.*by', content, re.IGNORECASE):
            checks['evidence_based_decisions'] = True
            score += 0.2
        
        return {
            'validator': 'validator_9_cognitive_reasoning',
            'score': score,
            'checks': checks,
            'recommendations': self._get_cognitive_reasoning_recommendations(checks)
        }

    def check_meta_reflection(self, content: str) -> Dict[str, Any]:
        """Check Validator 10: Meta-Reflection compliance"""
        score = 0.0
        checks = {
            'lessons_learned_present': False,
            'process_improvement_loop': False,
            'future_considerations': False,
            'adaptation_mechanisms': False,
            'retrospective_framework': False
        }
        
        # Check meta-reflection section
        mr_match = re.search(r'##\s*META-REFLECTION.*?(?=##|$)', content, re.DOTALL | re.IGNORECASE)
        if mr_match:
            mr_content = mr_match.group(0)
            
            # Check lessons learned
            if re.search(r'Lessons\s+Learned|challenges.*discovered', mr_content, re.IGNORECASE):
                checks['lessons_learned_present'] = True
                score += 0.2
            
            # Check process improvement loop
            if re.search(r'Process\s+Improvement|continuous.*improvement|feedback.*loop', mr_content, re.IGNORECASE):
                checks['process_improvement_loop'] = True
                score += 0.2
            
            # Check future considerations
            if re.search(r'Future.*Protocol|downstream.*protocol|next.*protocol', mr_content, re.IGNORECASE):
                checks['future_considerations'] = True
                score += 0.2
            
            # Check adaptation mechanisms
            if re.search(r'Adaptation\s+Mechanisms|dynamic.*adjustment|rollback.*procedures', mr_content, re.IGNORECASE):
                checks['adaptation_mechanisms'] = True
                score += 0.2
            
            # Check retrospective framework
            if re.search(r'Retrospective\s+Framework|structured.*retrospective|what.*went.*well', mr_content, re.IGNORECASE):
                checks['retrospective_framework'] = True
                score += 0.2
        
        return {
            'validator': 'validator_10_meta_reflection',
            'score': score,
            'checks': checks,
            'recommendations': self._get_meta_reflection_recommendations(checks)
        }

    def run_partial_validation(self, content: str, sections_completed: List[str]) -> Dict[str, Any]:
        """Run validation on completed sections only"""
        results = {
            'timestamp': datetime.now().isoformat(),
            'protocol_number': self.protocol_number,
            'sections_completed': sections_completed,
            'validator_scores': {},
            'overall_score': 0.0,
            'risk_assessment': {},
            'recommendations': []
        }
        
        total_weighted_score = 0.0
        total_weight = 0.0
        high_risk_validators = []
        
        # Run relevant validators based on completed sections
        for section in sections_completed:
            relevant_validators = self.section_validator_map.get(section, [])
            
            for validator in relevant_validators:
                if validator not in results['validator_scores']:
                    # Run the validator check
                    validator_result = self._run_validator_check(validator, content)
                    results['validator_scores'][validator] = validator_result
                    
                    # Add to overall score
                    weight = self.validator_weights.get(validator, 0.1)
                    total_weighted_score += validator_result['score'] * weight
                    total_weight += weight
                    
                    # Check for high risk
                    if validator_result['score'] < 0.8:
                        high_risk_validators.append(validator)
        
        # Calculate overall score
        if total_weight > 0:
            results['overall_score'] = total_weighted_score / total_weight
        
        # Risk assessment
        results['risk_assessment'] = {
            'high_risk_validators': high_risk_validators,
            'risk_level': 'high' if len(high_risk_validators) >= 2 else 'medium' if high_risk_validators else 'low',
            'estimated_final_score': results['overall_score'] * 0.9 if high_risk_validators else results['overall_score']
        }
        
        # Generate recommendations
        results['recommendations'] = self._generate_overall_recommendations(results)
        
        return results

    def _run_validator_check(self, validator: str, content: str) -> Dict[str, Any]:
        """Run specific validator check"""
        validator_methods = {
            'validator_1_protocol_identity': self.check_protocol_identity,
            'validator_2_ai_role': self.check_ai_role,
            'validator_3_workflow_algorithm': self.check_workflow_algorithm,
            'validator_4_quality_gates': self.check_quality_gates,
            'validator_5_script_integration': self.check_script_integration,
            'validator_6_communication_protocol': self.check_communication_protocol,
            'validator_7_evidence_package': self.check_evidence_package,
            'validator_8_handoff_checklist': self.check_handoff_checklist,
            'validator_9_cognitive_reasoning': self.check_cognitive_reasoning,
            'validator_10_meta_reflection': self.check_meta_reflection
        }
        
        method = validator_methods.get(validator)
        if method:
            return method(content)
        else:
            return {
                'validator': validator,
                'score': 0.0,
                'error': f'Unknown validator: {validator}'
            }

    def _generate_overall_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Generate overall recommendations based on validation results"""
        recommendations = []
        
        # High-priority recommendations
        if results['risk_assessment']['risk_level'] == 'high':
            recommendations.append("🚨 HIGH RISK: Multiple validators scoring below 80%")
            recommendations.append("Address critical issues before proceeding to next sections")
        
        # Medium-priority recommendations
        if results['overall_score'] < 0.9:
            recommendations.append("⚠️ MEDIUM RISK: Overall score below 90%")
            recommendations.append("Focus on improving lowest-scoring validators")
        
        # Specific validator recommendations
        for validator, result in results['validator_scores'].items():
            if result['score'] < 0.8:
                recommendations.extend(result.get('recommendations', []))
        
        # Progress recommendations
        completed_sections = len(results['sections_completed'])
        if completed_sections >= 3 and results['overall_score'] >= 0.95:
            recommendations.append("✅ EXCELLENT PROGRESS: On track for production readiness")
        elif completed_sections >= 6 and results['overall_score'] < 0.9:
            recommendations.append("📊 CONSIDER REFACTORING: Many sections complete but score low")
        
        return recommendations

    # Recommendation generation methods (simplified for brevity)
    def _get_protocol_identity_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['protocol_number_present']:
            recommendations.append("Add protocol number in header (e.g., 'PROTOCOL 07:')")
        if not checks['mission_statement_present']:
            recommendations.append("Include clear mission statement after protocol header")
        if not checks['prerequisites_present']:
            recommendations.append("Add PREREQUISITES section with required artifacts")
        return recommendations

    def _get_ai_role_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['role_title_present']:
            recommendations.append("Define clear AI role title (e.g., 'You are a Data Strategy Architect')")
        if not checks['constraints_present']:
            recommendations.append("Add [STRICT] and [GUIDELINE] behavioral constraints")
        return recommendations

    def _get_workflow_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['phases_present']:
            recommendations.append("Define at least 2 workflow phases with clear numbering")
        if not checks['directives_used']:
            recommendations.append("Add [CRITICAL], [MUST], and [GUIDELINE] markers to steps")
        if not checks['halt_conditions_present']:
            recommendations.append("Include 'HALT AND AWAIT' checkpoints for user validation")
        return recommendations

    def _get_quality_gates_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['gates_defined']:
            recommendations.append("Define at least 2 quality gates with clear criteria")
        if not checks['thresholds_measurable']:
            recommendations.append("Add measurable thresholds (e.g., '≥95% coverage')")
        return recommendations

    def _get_script_integration_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['scripts_referenced']:
            recommendations.append("Reference specific automation scripts with paths")
        if not checks['manual_fallback_present']:
            recommendations.append("Include manual fallback procedures for script failures")
        return recommendations

    def _get_communication_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['status_announcements_defined']:
            recommendations.append("Define standard status announcement templates")
        if not checks['user_interaction_templates']:
            recommendations.append("Specify user interaction prompts and confirmation patterns")
        return recommendations

    def _get_evidence_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['artifacts_specified']:
            recommendations.append("List all required artifacts with formats and locations")
        if not checks['manifest_structure_defined']:
            recommendations.append("Define evidence manifest structure with execution IDs")
        return recommendations

    def _get_handoff_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['stakeholder_signoffs']:
            recommendations.append("Define stakeholder sign-off requirements and roles")
        if not checks['completion_criteria']:
            recommendations.append("Specify clear completion criteria with checkboxes")
        return recommendations

    def _get_cognitive_reasoning_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['reasoning_blocks_present']:
            recommendations.append("Add [REASONING] blocks for complex decisions")
        if not checks['alternatives_considered']:
            recommendations.append("Document alternatives considered with rationale")
        return recommendations

    def _get_meta_reflection_recommendations(self, checks: Dict[str, bool]) -> List[str]:
        recommendations = []
        if not checks['lessons_learned_present']:
            recommendations.append("Add lessons learned capture section")
        if not checks['process_improvement_loop']:
            recommendations.append("Include process improvement feedback mechanisms")
        return recommendations

def main():
    parser = argparse.ArgumentParser(description='Run validator pre-checks during protocol creation')
    parser.add_argument('--protocol', default='unknown', help='Protocol number being created')
    parser.add_argument('--file', required=True, help='Protocol file to check')
    parser.add_argument('--sections', nargs='+', help='Completed sections to validate')
    parser.add_argument('--output', help='Output JSON file for validation results')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Load protocol content
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error loading protocol file: {e}")
        sys.exit(1)
    
    # Initialize pre-checker
    checker = ValidatorPreChecker(args.protocol)
    
    # Run validation
    results = checker.run_partial_validation(content, args.sections or [])
    
    # Display results
    if args.verbose:
        print(f"=== VALIDATOR PRE-CHECK RESULTS ===")
        print(f"Protocol: {args.protocol}")
        print(f"Sections Completed: {', '.join(results['sections_completed'])}")
        print(f"Overall Score: {results['overall_score']:.1%}")
        print(f"Risk Level: {results['risk_assessment']['risk_level'].upper()}")
        print()
        
        print("VALIDATOR SCORES:")
        for validator, result in results['validator_scores'].items():
            status = "✅" if result['score'] >= 0.9 else "⚠️" if result['score'] >= 0.8 else "❌"
            print(f"  {status} {validator}: {result['score']:.1%}")
        
        print()
        print("RECOMMENDATIONS:")
        for rec in results['recommendations']:
            print(f"  {rec}")
    
    # Save results
    if args.output:
        try:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            if args.verbose:
                print(f"\n📄 Results saved to: {args.output}")
        except Exception as e:
            print(f"Error saving results: {e}")
    
    # Exit with appropriate code
    if results['risk_assessment']['risk_level'] == 'high':
        sys.exit(2)  # High risk
    elif results['overall_score'] < 0.9:
        sys.exit(1)  # Medium risk
    else:
        sys.exit(0)  # Low risk

if __name__ == '__main__':
    main()
