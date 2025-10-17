"""
AI Governor Framework Integration
Integrates the client project generator with the existing AI Governor Framework
"""

import os
import json
import yaml
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import subprocess


class AIGovernorIntegration:
    """Integrates with the AI Governor Framework for rule validation and workflow routing"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.governor_root = self._find_governor_root()
        self.rules_dir = self.governor_root / '.cursor' / 'rules' if self.governor_root else None
        self.workflows_dir = self.governor_root / '.cursor' / 'ai-driven-workflow' if self.governor_root else None
    
    def _find_governor_root(self) -> Optional[Path]:
        """Find the AI Governor Framework root directory"""
        # Check if we're within an AI Governor workspace
        current = Path.cwd()
        while current != current.parent:
            if (current / '.cursor' / 'rules' / 'master-rules').exists():
                return current
            current = current.parent
        
        # Check common locations
        common_paths = [
            Path.home() / 'ai-governor',
            Path('/opt/ai-governor'),
            Path('/usr/local/ai-governor')
        ]
        
        for path in common_paths:
            if path.exists() and (path / '.cursor' / 'rules').exists():
                return path
        
        return None
    
    def validate_project_config(self, project_config: Dict) -> Dict[str, Any]:
        """Validate project configuration against AI Governor policies"""
        if not self.governor_root:
            return {
                'valid': True,
                'warnings': ['AI Governor Framework not found - skipping policy validation']
            }
        
        # Load policy DSL
        policy_file = self.governor_root / '.cursor' / 'ai-driven-workflow' / 'policy-dsl' / 'client-generator-policies.yaml'
        if not policy_file.exists():
            policy_file = Path(__file__).parent.parent.parent / 'template-packs' / 'policy-dsl' / 'client-generator-policies.yaml'
        
        if not policy_file.exists():
            return {
                'valid': True,
                'warnings': ['Policy DSL file not found - skipping validation']
            }
        
        with open(policy_file, 'r') as f:
            policies = yaml.safe_load(f)
        
        # Run validation
        return self._run_policy_validation(project_config, policies)
    
    def _run_policy_validation(self, config: Dict, policies: Dict) -> Dict[str, Any]:
        """Execute policy validation rules"""
        errors = []
        warnings = []
        
        industry = config.get('industry')
        project_type = config.get('project_type')
        
        # Check industry policies
        if industry in policies.get('industry_policies', {}):
            industry_policy = policies['industry_policies'][industry]
            
            # Validate required stack
            stack_policy = industry_policy.get(f'{project_type}_stack', {})
            if not stack_policy:
                stack_policy = industry_policy.get('web_stack', {})
            
            required = stack_policy.get('required', {})
            prohibited = stack_policy.get('prohibited', {})
            
            # Check required technologies
            for tech_type, allowed_values in required.items():
                actual_value = config.get('stack', {}).get(tech_type)
                if actual_value and actual_value not in allowed_values:
                    errors.append(
                        f"{industry} requires {tech_type} to be one of: {', '.join(allowed_values)}"
                    )
            
            # Check prohibited technologies
            for tech_type, prohibited_values in prohibited.items():
                actual_value = config.get('stack', {}).get(tech_type)
                if actual_value in prohibited_values:
                    errors.append(
                        f"{industry} prohibits using {actual_value} for {tech_type}"
                    )
        
        # Run validation rules
        for rule in policies.get('validation_rules', []):
            if self._evaluate_condition(rule['condition'], config):
                if not self._evaluate_condition(rule['requirement'], config):
                    errors.append(rule['message'])
        
        return {
            'valid': len(errors) == 0,
            'errors': errors,
            'warnings': warnings
        }
    
    def _evaluate_condition(self, condition: str, config: Dict) -> bool:
        """Evaluate a policy condition without using eval.

        Supported grammar (boolean expressions):
          - equality/inequality: field == 'value', field != 'value'
          - membership: 'hipaa' in compliance, 'pci' not in compliance
          - conjunction/disjunction: and/or
          - parentheses for grouping

        Fields: industry, project_type, auth, frontend, backend, deploy, compliance (list)
        """
        import ast

        # Build context
        ctx: Dict[str, Union[str, List[str]]] = {
            'industry': config.get('industry'),
            'project_type': config.get('project_type'),
            'auth': config.get('stack', {}).get('auth'),
            'frontend': config.get('stack', {}).get('frontend'),
            'backend': config.get('stack', {}).get('backend'),
            'deploy': config.get('stack', {}).get('deploy'),
            'compliance': config.get('compliance', []) or [],
        }

        def _eval(node: ast.AST) -> bool:
            if isinstance(node, ast.BoolOp):
                if isinstance(node.op, ast.And):
                    return all(_eval(v) for v in node.values)
                if isinstance(node.op, ast.Or):
                    return any(_eval(v) for v in node.values)
                return False
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
                return not _eval(node.operand)
            if isinstance(node, ast.Compare):
                left = _eval(node.left)
                # Only support single comparator for simplicity
                if len(node.ops) != 1 or len(node.comparators) != 1:
                    return False
                op = node.ops[0]
                right = _eval(node.comparators[0])
                if isinstance(op, ast.Eq):
                    return left == right
                if isinstance(op, ast.NotEq):
                    return left != right
                if isinstance(op, ast.In):
                    try:
                        return left in right
                    except TypeError:
                        return False
                if isinstance(op, ast.NotIn):
                    try:
                        return left not in right
                    except TypeError:
                        return False
                return False
            if isinstance(node, ast.Name):
                return ctx.get(node.id)
            if isinstance(node, ast.Constant):
                return node.value
            if isinstance(node, ast.Str):  # py<3.8 compatibility if any
                return node.s
            if isinstance(node, ast.List):
                return [_eval(elt) for elt in node.elts]
            if isinstance(node, ast.Tuple):
                return tuple(_eval(elt) for elt in node.elts)
            return False

        try:
            tree = ast.parse(condition, mode='eval')
        except Exception:
            return False

        try:
            return bool(_eval(tree.body))
        except Exception:
            return False
    
    def copy_master_rules(self, target_project: Path) -> List[str]:
        """Copy relevant master rules to the new project"""
        copied_rules = []
        
        if not self.rules_dir:
            return copied_rules
        
        # Always copy essential master rules
        essential_rules = [
            '0-how-to-create-effective-rules.md',
            '2-master-rule-ai-collaboration-guidelines.md',
            '3-master-rule-code-quality-checklist.md',
            '4-master-rule-code-modification-safety-protocol.md',
            '5-master-rule-documentation-and-context-guidelines.md'
        ]
        
        master_rules_dir = self.rules_dir / 'master-rules'
        target_rules_dir = target_project / '.cursor' / 'rules' / 'master-rules'
        target_rules_dir.mkdir(parents=True, exist_ok=True)
        
        for rule_file in essential_rules:
            source = master_rules_dir / rule_file
            if source.exists():
                shutil.copy2(source, target_rules_dir / rule_file)
                copied_rules.append(f"master-rules/{rule_file}")
        
        return copied_rules
    
    def create_workflow_integration(self, project_config: Dict) -> Dict[str, str]:
        """Create workflow integration files"""
        workflows = {}
        
        # Create workflow router configuration
        router_config = {
            'version': '1.0',
            'project': project_config['name'],
            'workflows': {
                'analyze': 'ai-driven-workflow/1-analyze-and-plan-prd.md',
                'plan': 'ai-driven-workflow/2-create-actionable-plan.md',
                'execute': 'ai-driven-workflow/3-execute-tasks-parallel.md',
                'review': 'ai-driven-workflow/4-retrospective-learnings.md'
            },
            'rules': {
                'quality': '.cursor/rules/master-rules/3-master-rule-code-quality-checklist.md',
                'safety': '.cursor/rules/master-rules/4-master-rule-code-modification-safety-protocol.md',
                'compliance': f'.cursor/rules/industry-compliance-{project_config.get("compliance", ["none"])[0]}.mdc'
            }
        }
        
        workflows['router_config'] = json.dumps(router_config, indent=2)
        
        # Create project context for AI
        ai_context = {
            'project_name': project_config['name'],
            'industry': project_config['industry'],
            'technology_stack': project_config['stack'],
            'compliance_requirements': project_config.get('compliance', []),
            'features': project_config.get('features', []),
            'workflow_commands': {
                'analyze': 'Analyze requirements and create PRD',
                'plan': 'Create actionable development plan',
                'execute': 'Execute tasks in parallel',
                'review': 'Conduct retrospective and capture learnings'
            }
        }
        
        workflows['ai_context'] = json.dumps(ai_context, indent=2)
        
        return workflows
    
    def setup_pre_commit_hooks(self, project_root: Path, config: Dict) -> bool:
        """Setup pre-commit hooks for AI Governor compliance"""
        pre_commit_config = {
            'repos': [
                {
                    'repo': 'https://github.com/pre-commit/pre-commit-hooks',
                    'rev': 'v4.5.0',
                    'hooks': [
                        {'id': 'trailing-whitespace'},
                        {'id': 'end-of-file-fixer'},
                        {'id': 'check-yaml'},
                        {'id': 'check-added-large-files'}
                    ]
                }
            ]
        }
        
        # Add language-specific hooks
        if config['stack'].get('backend') in ['fastapi', 'django']:
            pre_commit_config['repos'].append({
                'repo': 'https://github.com/psf/black',
                'rev': '23.11.0',
                'hooks': [{'id': 'black'}]
            })
            pre_commit_config['repos'].append({
                'repo': 'https://github.com/pycqa/flake8',
                'rev': '6.1.0',
                'hooks': [{'id': 'flake8'}]
            })
        
        if config['stack'].get('frontend') != 'none':
            pre_commit_config['repos'].append({
                'repo': 'https://github.com/pre-commit/mirrors-eslint',
                'rev': 'v8.54.0',
                'hooks': [{'id': 'eslint'}]
            })
        
        # Add security hooks for compliance
        if config.get('compliance'):
            pre_commit_config['repos'].append({
                'repo': 'https://github.com/Yelp/detect-secrets',
                'rev': 'v1.4.0',
                'hooks': [{'id': 'detect-secrets'}]
            })
        
        # Write pre-commit config
        config_path = project_root / '.pre-commit-config.yaml'
        with open(config_path, 'w') as f:
            yaml.dump(pre_commit_config, f, default_flow_style=False)
        
        # Install pre-commit
        try:
            subprocess.run(['pre-commit', 'install'], cwd=project_root, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def generate_ai_instructions(self, project_config: Dict) -> str:
        """Generate AI-specific instructions for the project"""
        instructions = f"""# AI Development Instructions for {project_config['name']}

## Project Context
- **Industry**: {project_config['industry']}
- **Type**: {project_config['project_type']}
- **Stack**: {json.dumps(project_config['stack'], indent=2)}
- **Compliance**: {', '.join(project_config.get('compliance', ['None']))}

## Active Rules
The following AI Governor rules are active for this project:
- Client-specific rules: `.cursor/rules/client-specific-rules.mdc`
- Industry compliance: `.cursor/rules/industry-compliance-*.mdc`
- Master quality rules: `.cursor/rules/master-rules/`

## Workflow Commands
Use these commands to trigger AI workflows:

1. **Analyze Requirements**: `Apply instructions from .cursor/ai-driven-workflow/1-analyze-and-plan-prd.md`
2. **Create Plan**: `Apply instructions from .cursor/ai-driven-workflow/2-create-actionable-plan.md`
3. **Execute Tasks**: `Apply instructions from .cursor/ai-driven-workflow/3-execute-tasks-parallel.md`
4. **Review Progress**: `Apply instructions from .cursor/ai-driven-workflow/4-retrospective-learnings.md`

## Compliance Reminders
"""
        
        if 'hipaa' in project_config.get('compliance', []):
            instructions += """
### HIPAA Compliance
- All PHI must be encrypted at rest and in transit
- Implement audit logging for all PHI access
- Session timeout must be 15 minutes
- No PHI in logs or error messages
"""
        
        if 'gdpr' in project_config.get('compliance', []):
            instructions += """
### GDPR Compliance
- Implement consent management for all data collection
- Provide data export and deletion capabilities
- Document all data processing activities
- Implement privacy by design principles
"""
        
        instructions += """
## Development Best Practices
1. Always run tests before committing
2. Follow the coding standards in client-specific rules
3. Use semantic commit messages
4. Keep documentation up to date
5. Run security scans regularly

## Getting Help
- Review master rules for guidance
- Use the collaboration guidelines for working with AI
- Check compliance rules for industry-specific requirements
"""
        
        return instructions
    
    def create_integration_report(self, project_path: Path, integration_results: Dict) -> str:
        """Create a report of the integration results"""
        report = f"""# AI Governor Integration Report

**Project**: {project_path.name}
**Date**: {json.dumps(integration_results.get('timestamp', 'Unknown'))}

## Integration Summary

### ✅ Completed Steps
"""
        
        for step in integration_results.get('completed', []):
            report += f"- {step}\n"
        
        if integration_results.get('warnings'):
            report += "\n### ⚠️ Warnings\n"
            for warning in integration_results['warnings']:
                report += f"- {warning}\n"
        
        if integration_results.get('errors'):
            report += "\n### ❌ Errors\n"
            for error in integration_results['errors']:
                report += f"- {error}\n"
        
        report += f"""
## Configuration Validation
- **Valid**: {integration_results.get('validation', {}).get('valid', 'Unknown')}
- **Policy Compliance**: {integration_results.get('policy_compliance', 'Not checked')}

## Installed Components
- **Master Rules**: {len(integration_results.get('master_rules', []))} files
- **Workflows**: {len(integration_results.get('workflows', []))} workflows
- **Pre-commit Hooks**: {'Installed' if integration_results.get('pre_commit_installed') else 'Not installed'}

## Next Steps
1. Review the generated rules in `.cursor/rules/`
2. Customize client-specific rules as needed
3. Run `make setup` to complete project setup
4. Use workflow commands to start development

## Resources
- [AI Governor Documentation](https://ai-governor.docs)
- [Client Project Guide](.cursor/AI_INSTRUCTIONS.md)
- [Compliance Checklists](docs/COMPLIANCE.md)
"""
        
        return report