"""
Project Generator Core
Main project generation logic
"""

import os
import json
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

from .validator import ProjectValidator
from .industry_config import IndustryConfig
from ..templates.template_engine import TemplateEngine
from ..templates.registry import TemplateRegistry


class ProjectGenerator:
    """Main project generator class"""
    
    def __init__(self, args=None, validator: ProjectValidator = None, config: IndustryConfig = None,
                 output_dir=None, template_dir=None, template_registry=None):
        # Support old test interface
        if output_dir is not None and template_dir is not None:
            # Legacy test constructor
            from argparse import Namespace
            self.output_dir = output_dir
            self.template_dir = template_dir
            self.project_name = None
            # Create minimal args for compatibility
            self.args = Namespace(
                name='test-project',
                industry='healthcare',
                project_type='fullstack',
                frontend='nextjs',
                backend='fastapi',
                database='postgres',
                auth='auth0',
                deploy='aws',
                compliance='',
                features='',
                output_dir=str(output_dir),
                no_git=True,
                no_install=True,
                workers=2
            )
            self.validator = validator or ProjectValidator()
            self.config = {}  # Legacy tests expect dict, not IndustryConfig
        else:
            # New production constructor
            self.args = args
            self.validator = validator
            self.config = config or IndustryConfig(getattr(args, 'industry', 'healthcare'))

        # Legacy tests previously expected a dict here; preserve functionality while
        # keeping an object that exposes merge_features(). If a dict slipped in,
        # replace it with an IndustryConfig based on the requested industry.
        if not hasattr(self, 'config') or self.config is None:
            self.config = IndustryConfig(getattr(self.args, 'industry', 'healthcare'))
        elif isinstance(self.config, dict):
            self.config = IndustryConfig(getattr(self.args, 'industry', 'healthcare'))
            
        self.template_engine = TemplateEngine()
        # Use provided template registry or fall back to legacy
        if template_registry is not None:
            self.template_registry = template_registry
        else:
            self.template_registry = TemplateRegistry()
        # When True, do not emit any .cursor assets (rules, tools, ai-governor) into generated projects
        self.no_cursor_assets = bool(getattr(self.args, 'no_cursor_assets', False))
        # Minimal cursor mode: only project.json and selected rules (via rules manifest)
        self.minimal_cursor = bool(getattr(self.args, 'minimal_cursor', False))
        # Optional rules manifest file listing .mdc names to include from root project-rules
        self.rules_manifest_path: Optional[str] = getattr(self.args, 'rules_manifest', None)
        self.project_root = None
        # Determine workers
        auto_workers = max(2, (os.cpu_count() or 2) * 2)
        self.workers = getattr(self.args, 'workers', 0) or auto_workers
        # Precompile placeholder regexes
        self._placeholder_map = None
        self._placeholder_regex = None
        # Rules manifest/telemetry containers
        self._rules_included_from_manifest: list[str] = []
        self._rules_selected_includes: list[str] = []
        self._rules_fallbacks_written: list[str] = []
        self._rules_emitted: list[str] = []
        self._included_master_rules: bool = False
        self._included_common_rules: bool = False
    
    def generate(self) -> Dict[str, Any]:
        """Generate the complete project"""
        try:
            # Create project directory
            self.project_root = Path(self.args.output_dir) / self.args.name
            if self.project_root.exists():
                if getattr(self.args, 'force', False):
                    shutil.rmtree(self.project_root)
                else:
                    return {
                        'success': False,
                        'error': f"Directory {self.project_root} already exists (use --force to overwrite)"
                    }
            
            self.project_root.mkdir(parents=True, exist_ok=True)
            
            # Generate base structure
            self._create_base_structure()
            
            # Generate technology-specific components
            if self.args.frontend != 'none':
                self._generate_frontend()
            
            if self.args.backend != 'none':
                self._generate_backend()
            
            if self.args.database != 'none':
                self._setup_database()
            
            # Generate DevEx assets
            self._generate_devex_assets()
            
            # Generate CI/CD workflows
            self._generate_cicd_workflows()
            
            # Generate compliance and rules
            self._generate_compliance_rules()
            
            # Prepare AI Governor assets (tools, router config, sample logs)
            self._prepare_ai_governor_assets()
            
            # Generate industry gates
            self._generate_industry_gates()
            
            # Generate documentation
            self._generate_documentation()
            
            # Initialize git repository
            if not self.args.no_git:
                self._initialize_git()
                # Install pre-commit hook ONLY when .cursor assets are included
                # and the tools directory exists in the generated project
                tools_dir = self.project_root / '.cursor' / 'tools'
                if (not self.no_cursor_assets) and tools_dir.exists():
                    self._install_precommit_hook()
            
            # Generate setup commands
            setup_commands = self._generate_setup_commands()
            
            return {
                'success': True,
                'project_path': str(self.project_root),
                'setup_commands': setup_commands,
                'next_steps': self._generate_next_steps()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _create_base_structure(self):
        """Create the base project structure"""
        directories = [
            '.devcontainer',
            '.github/workflows',
            '.vscode',
            'docs',
            'scripts',
            'tests'
        ]
        if not self.no_cursor_assets and not self.minimal_cursor:
            directories.extend(['.cursor/rules', '.cursor/ai-driven-workflow'])
        elif not self.no_cursor_assets and self.minimal_cursor:
            directories.extend(['.cursor/rules'])
        
        for directory in directories:
            (self.project_root / directory).mkdir(parents=True, exist_ok=True)
        
        # If repo has ai-driven-workflow docs, copy them into the project for in-editor triggers
        try:
            if (not self.no_cursor_assets) and (not self.minimal_cursor):
                repo_root = Path(__file__).resolve().parents[2]
                source_ai_workflow = repo_root / '.cursor' / 'ai-driven-workflow'
                if source_devwf.exists():
                    shutil.copytree(source_ai_workflow, self.project_root / '.cursor' / 'ai-driven-workflow', dirs_exist_ok=True)
        except Exception:
            pass

        # Copy master-rules and common-rules into generated project when present
        try:
            if not self.no_cursor_assets:
                repo_root = Path(__file__).resolve().parents[2]
                source_rules_root = repo_root / '.cursor' / 'rules'
                dest_rules_root = self.project_root / '.cursor' / 'rules'
                # master-rules
                src_master = source_rules_root / 'master-rules'
                if src_master.exists() and src_master.is_dir():
                    shutil.copytree(src_master, dest_rules_root / 'master-rules', dirs_exist_ok=True)
                    self._included_master_rules = True
                # common-rules
                src_common = source_rules_root / 'common-rules'
                if src_common.exists() and src_common.is_dir():
                    shutil.copytree(src_common, dest_rules_root / 'common-rules', dirs_exist_ok=True)
                    self._included_common_rules = True
        except Exception:
            # Non-fatal; copying rules should not break generation
            pass
        
        # Create .gitignore
        gitignore_content = self._generate_gitignore()
        (self.project_root / '.gitignore').write_text(gitignore_content)
        
        # Create README.md
        readme_content = self._generate_readme()
        (self.project_root / 'README.md').write_text(readme_content)
        
        # Create project configuration
        project_config = {
            'name': self.args.name,
            'industry': self.args.industry,
            'project_type': self.args.project_type,
            'stack': {
                'frontend': self.args.frontend,
                'backend': self.args.backend,
                'database': self.args.database,
                'auth': self.args.auth,
                'deploy': self.args.deploy
            },
            'features': self.config.merge_features(self.args.features),
            'compliance': self.args.compliance.split(',') if self.args.compliance else []
        }
        
        if not self.no_cursor_assets:
            cursor_root = self.project_root / '.cursor'
            cursor_root.mkdir(parents=True, exist_ok=True)
            (cursor_root / 'project.json').write_text(
                json.dumps(project_config, indent=2)
            )
            index_path = cursor_root / 'index.mdc'
            index_path.write_text(self._render_cursor_index(project_config))

    def _render_cursor_index(self, project_config: Dict[str, Any]) -> str:
        """Build the contents of .cursor/index.mdc using project metadata."""
        name = project_config.get('name', 'Project')
        industry = project_config.get('industry', 'general')
        project_type = project_config.get('project_type', 'application')
        stack = project_config.get('stack', {}) or {}
        features: List[str] = project_config.get('features') or []
        compliance: List[str] = project_config.get('compliance') or []

        # Build glob list based on generated directories and stack choices
        stack_glob_map = {
            'frontend': 'frontend/**/*',
            'backend': 'backend/**/*',
            'database': 'database/**/*',
        }
        globs: List[str] = []
        for key, pattern in stack_glob_map.items():
            value = stack.get(key)
            if value and str(value).lower() != 'none' and pattern not in globs:
                globs.append(pattern)

        # Include common directories created during bootstrap
        for default_glob in ['docs/**/*', 'scripts/**/*', 'tests/**/*']:
            if default_glob not in globs:
                globs.append(default_glob)

        if not globs:
            globs.append('**/*')

        frontend_desc = stack.get('frontend') if stack.get('frontend') else 'no-frontend'
        backend_desc = stack.get('backend') if stack.get('backend') else 'no-backend'
        if isinstance(frontend_desc, str) and frontend_desc.lower() == 'none':
            frontend_desc = 'no-frontend'
        if isinstance(backend_desc, str) and backend_desc.lower() == 'none':
            backend_desc = 'no-backend'

        if frontend_desc == 'no-frontend':
            frontend_phrase = 'without a dedicated frontend'
        else:
            frontend_phrase = f"with a {frontend_desc} frontend"

        if backend_desc == 'no-backend':
            backend_phrase = 'and without a backend service'
        else:
            backend_phrase = f"and {backend_desc} backend"

        description = (
            f"{name} {project_type} project for the {industry} industry "
            f"{frontend_phrase} {backend_phrase}."
        )

        frontmatter_lines = [
            '---',
            f'description: "{description}"',
            'globs:'
        ]
        for glob in globs:
            frontmatter_lines.append(f'  - "{glob}"')
        frontmatter_lines.append('alwaysApply: true')
        frontmatter_lines.append('---')

        stack_lines = []
        for label in ['frontend', 'backend', 'database', 'auth', 'deploy']:
            value = stack.get(label)
            if value and str(value).strip() and str(value).lower() != 'none':
                stack_lines.append(f"- **{label.capitalize()}:** {value}")

        if not stack_lines:
            stack_lines.append("- Stack details were not specified.")

        feature_text = ', '.join(features) if features else 'None specified'

        compliance_lines: List[str] = []
        if compliance:
            for flag in compliance:
                compliance_lines.append(
                    f"- Adhere to {flag.upper()} controls across all services and data flows."
                )
        else:
            compliance_lines.append("- No additional regulatory frameworks were selected.")

        rule_lines: List[str] = []
        if stack.get('frontend') and str(stack.get('frontend')).lower() != 'none':
            rule_lines.append(
                f"- Keep the `{stack['frontend']}` frontend synchronized with backend contracts and shared APIs."
            )
        if stack.get('backend') and str(stack.get('backend')).lower() != 'none':
            rule_lines.append(
                f"- Structure the `{stack['backend']}` backend with clear domain boundaries and automated testing."
            )
        if stack.get('database') and str(stack.get('database')).lower() != 'none':
            rule_lines.append(
                f"- Manage the `{stack['database']}` data layer with migrations and backups aligned to compliance needs."
            )
        if features:
            rule_lines.append(
                f"- Prioritize delivery of key features: {', '.join(features)}."
            )
        if compliance:
            for flag in compliance:
                rule_lines.append(
                    f"- Document how {flag.upper()} obligations are met in infrastructure, code, and operations."
                )
        if not rule_lines:
            rule_lines.append("- Follow established engineering best practices and keep documentation current.")

        body_lines = [
            f"# {name} Project Overview",
            '',
            f"- **Industry:** {industry}",
            f"- **Project Type:** {project_type}",
            f"- **Features:** {feature_text}",
            '',
            '## Technology Stack',
            '',
        ]
        body_lines.extend(stack_lines)
        body_lines.extend([
            '',
            '## Compliance Considerations',
            '',
        ])
        body_lines.extend(compliance_lines)
        body_lines.extend([
            '',
            '## Project Rules',
            '',
        ])
        body_lines.extend(rule_lines)
        body_lines.append('')

        return '\n'.join(frontmatter_lines + [''] + body_lines)
    
    def _generate_frontend(self):
        """Generate frontend application"""
        frontend_dir = self.project_root / 'frontend'
        frontend_dir.mkdir(exist_ok=True)
        
        # Copy template files using manifest/registry if available
        template_root = Path(__file__).parent.parent.parent / 'template-packs' / 'frontend' / self.args.frontend
        variant = 'enterprise' if self.args.industry in ['healthcare', 'finance', 'enterprise'] else 'base'
        variant_path = template_root / variant
        if variant_path.exists():
            shutil.copytree(variant_path, frontend_dir, dirs_exist_ok=True)
        else:
            base_path = template_root / 'base'
            if base_path.exists():
                shutil.copytree(base_path, frontend_dir, dirs_exist_ok=True)
        
        # Process templates with project-specific values
        self._process_templates(frontend_dir)
        
        # Add industry-specific components
        self._add_industry_components(frontend_dir, 'frontend')
    
    def _generate_backend(self):
        """Generate backend application"""
        backend_dir = self.project_root / 'backend'
        backend_dir.mkdir(exist_ok=True)
        
        # Copy template files
        template_path = Path(__file__).parent.parent.parent / 'template-packs' / 'backend' / self.args.backend
        
        if template_path.exists():
            # Special-case: NestJS Prisma variant selection via --nestjs-orm
            if self.args.backend == 'nestjs' and getattr(self.args, 'nestjs_orm', 'typeorm') == 'prisma':
                prisma_path = template_path / 'prisma'
                if prisma_path.exists():
                    shutil.copytree(prisma_path, backend_dir, dirs_exist_ok=True)
                else:
                    # Fallback to base if prisma variant missing
                    base_path = template_path / 'base'
                    if base_path.exists():
                        shutil.copytree(base_path, backend_dir, dirs_exist_ok=True)
            else:
                # Use the appropriate template variant for other backends
                variant = 'microservice' if self.args.project_type == 'microservices' else 'base'
                variant = 'enterprise' if self.args.industry in ['healthcare', 'finance', 'enterprise'] else variant
                
                variant_path = template_path / variant
                if variant_path.exists():
                    shutil.copytree(variant_path, backend_dir, dirs_exist_ok=True)
                else:
                    # Fallback to base template
                    base_path = template_path / 'base'
                    if base_path.exists():
                        shutil.copytree(base_path, backend_dir, dirs_exist_ok=True)
        
        # Process templates
        self._process_templates(backend_dir)
        
        # Add industry-specific APIs
        self._add_industry_components(backend_dir, 'backend')
    
    def _setup_database(self):
        """Setup database configuration"""
        db_dir = self.project_root / 'database'
        db_dir.mkdir(exist_ok=True)
        
        # Copy database templates
        template_path = Path(__file__).parent.parent.parent / 'template-packs' / 'database' / self.args.database
        
        if template_path.exists():
            shutil.copytree(template_path, db_dir, dirs_exist_ok=True)
        
        # Process templates with project-specific values
        self._process_templates(db_dir)
        
        # Create docker-compose for database
        if self.args.database in ['postgres', 'mongodb']:
            self._add_database_to_docker_compose()

    def _process_templates(self, root: Path):
        """Process text templates by replacing simple placeholders with project values using a thread pool."""
        mapping = {
            '{{PROJECT_NAME}}': self.args.name,
            '{{INDUSTRY}}': self.args.industry,
            '{{PROJECT_TYPE}}': self.args.project_type,
            '{{FRONTEND}}': self.args.frontend,
            '{{BACKEND}}': self.args.backend,
            '{{DATABASE}}': self.args.database,
            '{{AUTH}}': self.args.auth,
            '{{DEPLOY}}': self.args.deploy,
        }
        # cache compiled regex
        if self._placeholder_map is None:
            self._placeholder_map = mapping
            pattern = re.compile('|'.join(map(re.escape, mapping.keys())))
            self._placeholder_regex = pattern
        text_exts = {
            '.md', '.mdc', '.txt', '.json', '.yml', '.yaml', '.toml', '.ini', '.env',
            '.js', '.jsx', '.ts', '.tsx', '.py', '.go', '.html', '.css', '.scss', '.sh',
            '.sql', '.example'
        }
        files: list[Path] = [p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in text_exts]

        def _process_one(p: Path):
            try:
                content = p.read_text()
                content = self._placeholder_regex.sub(lambda m: str(self._placeholder_map[m.group(0)]), content)
                p.write_text(content)
                return True
            except Exception:
                return False

        with ThreadPoolExecutor(max_workers=self.workers) as ex:
            list(as_completed(ex.submit(_process_one, f) for f in files))

    def _add_industry_components(self, target_dir: Path, component_type: str):
        """Add industry-specific components (placeholder no-op)."""
        # Intentionally minimal for now; templates already include industry variants.
        return

    def _add_database_to_docker_compose(self):
        """Ensure database service is present in docker-compose (handled by _generate_docker_compose)."""
        # No action required: _generate_docker_compose already includes DB services
        # for postgres/mongodb based on self.args.database.
        return
    
    def _generate_devex_assets(self):
        """Generate developer experience assets"""
        # .devcontainer/devcontainer.json
        devcontainer_config = self._generate_devcontainer_config()
        (self.project_root / '.devcontainer' / 'devcontainer.json').write_text(
            json.dumps(devcontainer_config, indent=2)
        )
        
        # docker-compose.yml
        docker_compose = self._generate_docker_compose()
        (self.project_root / 'docker-compose.yml').write_text(docker_compose)
        
        # Makefile
        makefile = self._generate_makefile()
        (self.project_root / 'Makefile').write_text(makefile)
        
        # .vscode snippets
        self._generate_vscode_snippets()
    
    def _generate_cicd_workflows(self):
        """Generate CI/CD workflow files"""
        workflows_dir = self.project_root / '.github' / 'workflows'
        
        # CI Lint workflow
        lint_workflow = self._generate_lint_workflow()
        (workflows_dir / 'ci-lint.yml').write_text(lint_workflow)
        
        # CI Test workflow
        test_workflow = self._generate_test_workflow()
        (workflows_dir / 'ci-test.yml').write_text(test_workflow)
        
        # Security scan workflow
        security_workflow = self._generate_security_workflow()
        (workflows_dir / 'ci-security.yml').write_text(security_workflow)
        
        # Deploy workflow
        if self.args.deploy != 'self-hosted':
            deploy_workflow = self._generate_deploy_workflow()
            (workflows_dir / 'ci-deploy.yml').write_text(deploy_workflow)
        
        # Gates configuration
        gates_config = self._generate_gates_config()
        (self.project_root / 'gates_config.yaml').write_text(gates_config)
        
        # Minimal PCI/SOX overlays: add simple job triggers when selected
        if self.args.compliance:
            comps = [c.strip().lower() for c in self.args.compliance.split(',')]
            if 'pci' in comps or 'sox' in comps:
                base_ci = self._generate_base_ci_overlays(comps)
                (workflows_dir / 'ci-compliance-overlays.yml').write_text(base_ci)
    
    def _generate_compliance_rules(self):
        """Generate compliance and project-specific rules"""
        if self.no_cursor_assets:
            return
        rules_root_dir = self.project_root / '.cursor' / 'rules'
        rules_dir = rules_root_dir / 'project-rules'
        
        # Minimal-cursor: only include manifest-specified project rules and explicit compliance rules; skip client-specific.
        if self.minimal_cursor:
            self._include_rules_from_manifest(rules_dir)
        else:
            # Client-specific rules
            client_rules = self._generate_client_rules()
            rules_dir.mkdir(parents=True, exist_ok=True)
            (rules_dir / 'client-specific-rules.mdc').write_text(client_rules)
            self._rules_emitted.append('project-rules/client-specific-rules.mdc')
        
        # Industry compliance rules
        if self.args.compliance:
            for compliance in self.args.compliance.split(','):
                compliance_rules = self._generate_compliance_rules_content(compliance.strip())
                (rules_dir / f'industry-compliance-{compliance}.mdc').write_text(compliance_rules)
                self._rules_emitted.append(f'project-rules/industry-compliance-{compliance}.mdc')
        
        # Project workflow rules
        workflow_rules = self._generate_workflow_rules()
        (rules_dir / 'project-workflow.mdc').write_text(workflow_rules)
        self._rules_emitted.append('project-rules/project-workflow.mdc')

        # Optionally include a minimal set of technology-specific project rules (legacy path)
        if not self.minimal_cursor:
            self._include_selected_project_rules(rules_dir)

        # Write rules manifest/telemetry
        try:
            import json as _json
            manifest = {
                'mode': 'minimal' if self.minimal_cursor else 'full',
                'included_master_rules': self._included_master_rules,
                'included_common_rules': self._included_common_rules,
                'emitted_project_rules': sorted(self._rules_emitted),
                'manifest_includes': sorted(self._rules_included_from_manifest),
                'selected_includes': sorted(self._rules_selected_includes),
                'fallbacks_written': sorted(self._rules_fallbacks_written),
            }
            (rules_root_dir / 'manifest.json').write_text(_json.dumps(manifest, indent=2))
        except Exception:
            pass

    def _include_rules_from_manifest(self, rules_dir: Path) -> None:
        """Copy only rules listed in the JSON manifest from root .cursor/rules/project-rules.

        If the manifest path is missing or invalid, fall back to curated stack-based rules.
        """
        try:
            if not self.rules_manifest_path:
                curated = self._collect_curated_project_rules()
                if curated:
                    self._emit_rule_files(rules_dir, curated, self._rules_selected_includes)
                return

            import json as _json

            manifest_path = Path(self.rules_manifest_path)
            names: list[str] = []
            if manifest_path.exists():
                try:
                    payload = _json.loads(manifest_path.read_text(encoding='utf-8'))
                    if isinstance(payload, list):
                        names = [str(item).strip() for item in payload if str(item).strip().endswith('.mdc')]
                except Exception:
                    names = []

            if not names:
                curated = self._collect_curated_project_rules()
                if curated:
                    self._emit_rule_files(rules_dir, curated, self._rules_selected_includes)
                return

            self._emit_rule_files(rules_dir, names, self._rules_included_from_manifest)
        except Exception:
            return

    def _resolve_template_rule_source(self, template_root: Path, fname: str) -> Optional[Path]:
        """Return a matching rule path from template-packs when available."""
        mapping: dict[str, Path] = {
            'nextjs.mdc': template_root / 'frontend' / 'nextjs' / 'nextjs.mdc',
            'nextjs-formatting.mdc': template_root / 'frontend' / 'nextjs' / 'formatting.mdc',
            'typescript.mdc': template_root / 'frontend' / 'nextjs' / 'typescript.mdc',
            'fastapi.mdc': template_root / 'backend' / 'fastapi' / 'fastapi.mdc',
        }
        candidate = mapping.get(fname)
        if candidate and candidate.exists():
            return candidate
        return None

    def _write_fallback_rule_if_known(self, rules_dir: Path, fname: str) -> None:
        """Write a minimal embedded rule if we recognize the filename."""
        mapping: dict[str, str] = {
            'nextjs.mdc': self._rule_min_nextjs(),
            'nextjs-formatting.mdc': self._rule_min_nextjs_formatting(),
            'nextjs-rsc-and-client.mdc': self._rule_min_nextjs_rsc(),
            'nextjs-a11y.mdc': self._rule_min_nextjs_a11y(),
            'typescript.mdc': self._rule_min_typescript(),
            'accessibility.mdc': self._rule_min_accessibility(),
            'fastapi.mdc': self._rule_min_fastapi(),
            'django.mdc': self._rule_min_django(),
            'python.mdc': self._rule_min_python(),
            'rest-api.mdc': self._rule_min_rest_api(),
            'open-api.mdc': self._rule_min_open_api(),
            'golang.mdc': self._rule_min_golang(),
            'nethttp.mdc': self._rule_min_nethttp(),
            'angular.mdc': self._rule_min_angular(),
            'vue.mdc': self._rule_min_vue(),
            'expo.mdc': self._rule_min_expo(),
            'react-native.mdc': self._rule_min_react_native(),
            'nodejs.mdc': self._rule_min_nodejs(),
            'mongodb.mdc': self._rule_min_mongodb(),
            'firebase.mdc': self._rule_min_firebase(),
            'best-practices.mdc': self._rule_min_best_practices(),
            'web-development.mdc': self._rule_min_web_development(),
            'performance.mdc': self._rule_min_performance(),
            'observability.mdc': self._rule_min_observability(),
            'webshop.mdc': self._rule_min_webshop(),
        }
        content = mapping.get(fname)
        if content:
            try:
                # Normalize SCOPE to project:<slug>
                try:
                    slug = getattr(self.args, 'name', '')
                except Exception:
                    slug = ''
                scope_replacement = f"SCOPE: project:{slug}"
                content = content.replace("SCOPE: project-rules", scope_replacement)
                dest = rules_dir / fname
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding='utf-8')
                try:
                    self._rules_fallbacks_written.append(str(Path('project-rules') / fname))
                except Exception:
                    pass
            except Exception:
                pass

    # ---- Embedded minimal rule generators (compact, non-ceremonial) ----
    def _rule_min_nextjs(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [frontend,nextjs] | TRIGGERS: component,page,route,build | SCOPE: project-rules | DESCRIPTION: Minimal Next.js guidance for build-ready components."\n'
            '---\n\n'
            '# Next.js Minimal Rules\n\n'
            '- Use App Router; colocate server actions.\n'
            '- Prefer streaming/SSR for data-heavy pages; cache fetches.\n'
            '- Environment via process.env only on server; never expose secrets.\n'
        )

    def _rule_min_nextjs_formatting(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [frontend,nextjs,format] | TRIGGERS: lint,format | SCOPE: project-rules | DESCRIPTION: Formatting conventions for Next.js."\n'
            '---\n\n'
            '# Next.js Formatting\n\n'
            '- Use Prettier + ESLint; no unused vars; import order standardized.\n'
        )

    def _rule_min_nextjs_rsc(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [frontend,nextjs,rsc] | TRIGGERS: server,client | SCOPE: project-rules | DESCRIPTION: RSC vs Client component guidelines."\n'
            '---\n\n'
            '# RSC and Client Components\n\n'
            '- Default to RSC; use Client only for stateful/interactive UI.\n'
        )

    def _rule_min_nextjs_a11y(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [frontend,nextjs,a11y] | TRIGGERS: accessibility,audit | SCOPE: project-rules | DESCRIPTION: Next.js accessibility guardrails."\n'
            '---\n\n'
            '# Next.js Accessibility\n\n'
            '- Provide visible focus states and keyboard support for interactive components.\n'
            '- Prefer semantic HTML landmarks; keep aria usage purposeful.\n'
            '- Run eslint-plugin-jsx-a11y before merging UI changes.\n'
        )

    def _rule_min_typescript(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [typescript] | TRIGGERS: build,typecheck | SCOPE: project-rules | DESCRIPTION: Minimal TS guidance."\n'
            '---\n\n'
            '# TypeScript Minimal\n\n'
            '- Strict true; no implicit any; clear function and public API types.\n'
        )

    def _rule_min_accessibility(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [frontend,accessibility] | TRIGGERS: audit,a11y | SCOPE: project-rules | DESCRIPTION: Baseline accessibility checklist."\n'
            '---\n\n'
            '# Accessibility Checklist\n\n'
            '- Meet WCAG 2.1 AA contrast and keyboard navigation requirements.\n'
            '- Supply meaningful alt text and aria labels for non-text UI elements.\n'
            '- Validate with axe or Lighthouse during QA.\n'
        )

    def _rule_min_fastapi(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [backend,fastapi] | TRIGGERS: endpoint,router,build | SCOPE: project-rules | DESCRIPTION: Minimal FastAPI rules."\n'
            '---\n\n'
            '# FastAPI Minimal\n\n'
            '- Pydantic v2; typed request/response models; dependency injection for DB.\n'
        )

    def _rule_min_django(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [backend,django] | TRIGGERS: view,model | SCOPE: project-rules | DESCRIPTION: Minimal Django service rules."\n'
            '---\n\n'
            '# Django Minimal\n\n'
            '- Use class-based views and DRF viewsets for APIs; keep business logic in services.\n'
            '- Configure settings via environment variables; enable security middleware in production.\n'
            '- Maintain migrations per change set and cover critical paths with pytest.\n'
        )

    def _rule_min_python(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [python] | TRIGGERS: lint,test | SCOPE: project-rules | DESCRIPTION: Minimal Python guidelines."\n'
            '---\n\n'
            '# Python Minimal\n\n'
            '- Use black + flake8; avoid global state; prefer dataclasses for simple data.\n'
        )

    def _rule_min_rest_api(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [api,rest] | TRIGGERS: endpoint,contract | SCOPE: project-rules | DESCRIPTION: Minimal REST API practices."\n'
            '---\n\n'
            '# REST API Minimal\n\n'
            '- Consistent error shape; status codes; idempotent PUT; validation on input.\n'
        )

    def _rule_min_open_api(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [openapi] | TRIGGERS: schema,contract | SCOPE: project-rules | DESCRIPTION: Minimal OpenAPI usage."\n'
            '---\n\n'
            '# OpenAPI Minimal\n\n'
            '- Keep spec near code; generate clients only for stable endpoints.\n'
        )

    def _rule_min_golang(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [golang] | TRIGGERS: build,test | SCOPE: project-rules | DESCRIPTION: Minimal Go rules."\n---\n\n'
            '# Go Minimal\n\n- Modules tidy; context everywhere; errors wrapped with %w.\n'
        )

    def _rule_min_nethttp(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [nethttp] | TRIGGERS: handler,router | SCOPE: project-rules | DESCRIPTION: Minimal net/http rules."\n---\n\n'
            '# net/http Minimal\n\n- Context cancel checks; timeouts; structured logging.\n'
        )

    def _rule_min_nodejs(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [backend,nodejs] | TRIGGERS: api,build | SCOPE: project-rules | DESCRIPTION: Minimal Node.js service guidance."\n'
            '---\n\n'
            '# Node.js Service\n\n'
            '- Use structured logging and graceful shutdown hooks for long-lived processes.\n'
            '- Keep configuration in environment variables with runtime validation.\n'
            '- Enforce eslint and unit tests via npm scripts before deployment.\n'
        )

    def _rule_min_angular(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [frontend,angular] | TRIGGERS: component,service | SCOPE: project-rules | DESCRIPTION: Minimal Angular rules."\n---\n\n'
            '# Angular Minimal\n\n- Standalone components; OnPush; typed forms.\n'
        )

    def _rule_min_vue(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [frontend,vue] | TRIGGERS: component,store | SCOPE: project-rules | DESCRIPTION: Minimal Vue rules."\n---\n\n'
            '# Vue Minimal\n\n- SFC script setup; Pinia; lazy routes.\n'
        )

    def _rule_min_expo(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [frontend,expo] | TRIGGERS: screen,navigation | SCOPE: project-rules | DESCRIPTION: Minimal Expo rules."\n---\n\n'
            '# Expo Minimal\n\n- Expo Router; platform-safe APIs; offline-ready assets.\n'
        )

    def _rule_min_react_native(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [frontend,react-native] | TRIGGERS: component,screen | SCOPE: project-rules | DESCRIPTION: Minimal React Native rules."\n---\n\n'
            '# React Native Minimal\n\n- Use SafeAreaView; avoid heavy re-renders; memoize lists.\n'
        )

    def _rule_min_mongodb(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [database,mongodb] | TRIGGERS: schema,index | SCOPE: project-rules | DESCRIPTION: Minimal MongoDB rules."\n---\n\n'
            '# MongoDB Minimal\n\n- Define indexes early; validate schemas; limit unbounded queries.\n'
        )

    def _rule_min_firebase(self) -> str:
        return (
            '---\nalwaysApply: false\n'
            'description: "TAGS: [database,firebase] | TRIGGERS: rules,security | SCOPE: project-rules | DESCRIPTION: Minimal Firebase rules."\n---\n\n'
            '# Firebase Minimal\n\n- Security rules first; limit public reads; version configs.\n'
        )

    def _rule_min_best_practices(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [best-practices] | TRIGGERS: review,refactor | SCOPE: project-rules | DESCRIPTION: Minimal engineering best practices."\n'
            '---\n\n'
            '# Best Practices\n\n- Small PRs; meaningful names; tests first for critical paths.\n'
        )

    def _rule_min_web_development(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [web] | TRIGGERS: build,ci | SCOPE: project-rules | DESCRIPTION: Minimal web development rules."\n'
            '---\n\n'
            '# Web Development\n\n- Avoid blocking main thread; lazy-load heavy assets; a11y AA.\n'
        )

    def _rule_min_performance(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [performance] | TRIGGERS: profile,optimize | SCOPE: project-rules | DESCRIPTION: Minimal performance rules."\n'
            '---\n\n'
            '# Performance\n\n- Measure p95; cache wisely; batch I/O; paginate large queries.\n'
        )

    def _rule_min_observability(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [observability] | TRIGGERS: log,trace,metric | SCOPE: project-rules | DESCRIPTION: Minimal observability rules."\n'
            '---\n\n'
            '# Observability\n\n- Structured logs with correlation IDs; basic traces and key metrics.\n'
        )

    def _rule_min_webshop(self) -> str:
        return (
            '---\n'
            'alwaysApply: false\n'
            'description: "TAGS: [ecommerce,webshop] | TRIGGERS: cart,checkout | SCOPE: project-rules | DESCRIPTION: Minimal ecommerce/webshop rules."\n'
            '---\n\n'
            '# Webshop\n\n- Guard cart/checkout flows; currency/locale aware; idempotent payments.\n'
        )

    def _include_selected_project_rules(self, rules_dir: Path):
        """Copy a minimal set of project rules (.mdc) for the chosen stack into the generated project."""
        try:
            if not getattr(self.args, 'include_project_rules', False):
                return
            selected = self._collect_curated_project_rules()
            if not selected:
                return
            self._emit_rule_files(rules_dir, selected, self._rules_selected_includes)
        except Exception:
            # Non-fatal: rule inclusion should never break generation
            return

    def _collect_curated_project_rules(self) -> list[str]:
        fe = (getattr(self.args, 'frontend', 'none') or 'none').lower()
        be = (getattr(self.args, 'backend', 'none') or 'none').lower()
        db = (getattr(self.args, 'database', 'none') or 'none').lower()

        frontend_rules = {
            'nextjs': ['nextjs.mdc', 'nextjs-formatting.mdc', 'nextjs-rsc-and-client.mdc', 'typescript.mdc', 'accessibility.mdc', 'nextjs-a11y.mdc'],
            'angular': ['angular.mdc', 'typescript.mdc', 'accessibility.mdc'],
            'expo': ['expo.mdc', 'react-native.mdc', 'typescript.mdc', 'accessibility.mdc'],
            'nuxt': ['vue.mdc', 'typescript.mdc', 'accessibility.mdc'],
        }

        backend_rules = {
            'fastapi': ['fastapi.mdc', 'python.mdc', 'rest-api.mdc', 'open-api.mdc', 'performance.mdc', 'observability.mdc'],
            'django': ['django.mdc', 'python.mdc', 'rest-api.mdc', 'open-api.mdc', 'performance.mdc', 'observability.mdc'],
            'nestjs': ['nodejs.mdc', 'typescript.mdc', 'rest-api.mdc', 'open-api.mdc', 'performance.mdc', 'observability.mdc'],
            'go': ['golang.mdc', 'nethttp.mdc', 'rest-api.mdc', 'open-api.mdc', 'performance.mdc', 'observability.mdc'],
        }

        db_addons: dict[str, list[str]] = {
            'mongodb': ['mongodb.mdc'],
            'firebase': ['firebase.mdc'],
        }

        selected: list[str] = []
        selected += frontend_rules.get(fe, [])
        selected += backend_rules.get(be, [])
        selected += db_addons.get(db, [])

        # Deduplicate while preserving order
        seen: set[str] = set()
        filtered: list[str] = []
        for name in selected:
            if name and name not in seen:
                seen.add(name)
                filtered.append(name)
        return filtered

    def _emit_rule_files(self, rules_dir: Path, filenames: list[str], tracking: list[str]) -> None:
        repo_root = Path(__file__).resolve().parents[2]
        source_dir = repo_root / '.cursor' / 'rules' / 'project-rules'
        template_rules_root = repo_root / 'template-packs' / 'rules'

        rules_dir.mkdir(parents=True, exist_ok=True)

        seen: set[str] = set()
        for fname in filenames:
            if not fname or fname in seen:
                continue
            seen.add(fname)

            dest = rules_dir / fname
            dest.parent.mkdir(parents=True, exist_ok=True)

            produced = False
            src = source_dir / fname
            if src.exists() and src.is_file():
                shutil.copy(src, dest)
                produced = True
            else:
                template_src = self._resolve_template_rule_source(template_rules_root, fname)
                if template_src and template_src.exists():
                    shutil.copy(template_src, dest)
                    produced = True

            if not produced:
                self._write_fallback_rule_if_known(rules_dir, fname)
                produced = dest.exists()

            if produced:
                try:
                    entry = str(Path('project-rules') / fname)
                    if entry not in tracking:
                        tracking.append(entry)
                except Exception:
                    pass


    def _generate_compliance_rules_content(self, compliance: str) -> str:
        """Generate Cursor-style .mdc content with YAML frontmatter for a compliance standard."""
        c = (compliance or '').strip().lower()
        title_map = {
            'hipaa': 'HIPAA Compliance Rules',
            'gdpr': 'GDPR Compliance Rules',
            'sox': 'SOX Compliance Rules',
            'pci': 'PCI DSS Compliance Rules',
        }
        desc_map = {
            'hipaa': 'Healthcare PHI protection: encryption, access control, audit logging, session timeout',
            'gdpr': 'EU data protection: consent, right to erasure, data export, privacy by design',
            'sox': 'Financial reporting integrity: change control, audit trail, access reviews',
            'pci': 'Cardholder data security: no PAN storage, tokenization, segmentation, encryption',
        }
        title = title_map.get(c, f"{c.upper()} Compliance Rules")
        # Extended triggers to work with Cursor AI workflows (includes update/refresh/sync and planning/execution verbs)
        triggers = [
            'commit', 'ci', 'update all', 'refresh all', 'sync all', 'reload all',
            'bootstrap', 'setup', 'initialize', 'project start', 'master plan',
            'framework ecosystem', 'background agents', 'prd', 'requirements',
            'feature planning', 'product spec', 'task generation', 'technical planning',
            'implementation plan', 'execute', 'implement', 'process tasks', 'development',
            'retrospective', 'review', 'improvement', 'post-implementation',
            'parallel execution', 'coordination', 'multi-agent', 'analyze'
        ]
        triggers_str = ','.join(triggers)
        description_meta = (
            f"TAGS: [compliance,{c}] | TRIGGERS: {triggers_str} | SCOPE: {self.args.name} | DESCRIPTION: {desc_map.get(c, title)}"
        )

        # Minimal control checklist per compliance
        if c == 'hipaa':
            body_lines = [
                f"# {title}",
                "", 
                "## Required Controls [STRICT]",
                "- PHI encrypted at rest (AES-256) and in transit (TLS 1.2+)",
                "- Audit logging for all PHI access and changes",
                "- Minimum necessary access (RBAC) with reviews",
                "- 15-minute session timeout and re-authentication",
                "- No PHI in logs or error messages",
                "",
                "## CI Gates",
                "- Block merge if security scan reports critical vulns",
                "- Enforce unit tests for PHI-related modules",
                "- Validate presence of HIPAA rules in .cursor/rules/",
            ]
        elif c == 'gdpr':
            body_lines = [
                f"# {title}",
                "",
                "## Required Controls [STRICT]",
                "- Consent collection and management",
                "- Data export (access) and deletion workflows",
                "- Data minimization and retention policies",
                "- Privacy by design reviews",
                "",
                "## CI Gates",
                "- Verify privacy endpoints present in API",
                "- Ensure no PII in logs",
            ]
        elif c == 'sox':
            body_lines = [
                f"# {title}",
                "",
                "## Required Controls [STRICT]",
                "- Change control with approvals and rollback",
                "- Audit trail for financial data changes",
                "- Segregation of duties",
                "- Quarterly access reviews",
                "",
                "## CI Gates",
                "- Block merge without migrations audit approval",
                "- Enforce coverage for critical financial modules",
            ]
        elif c == 'pci':
            body_lines = [
                f"# {title}",
                "",
                "## Required Controls [STRICT]",
                "- No storage of sensitive authentication data",
                "- Tokenization of cardholder data",
                "- Network segmentation of CDE",
                "- Encryption at rest and in transit",
                "",
                "## CI Gates",
                "- Secret scanning must pass",
                "- Dependency scan must have no critical issues",
            ]
        else:
            body_lines = [f"# {title}", "", "- Define controls for this standard"]

        frontmatter = [
            "---",
            "alwaysApply: true",
            f"description: \"{description_meta}\"",
            "---",
            "",
        ]
        return "\n".join(frontmatter + body_lines)
    
    def _prepare_ai_governor_assets(self):
        """Prepare AI Governor assets (.cursor/tools and router config)"""
        if self.no_cursor_assets:
            return
        tools_dir = self.project_root / '.cursor' / 'tools'
        tools_dir.mkdir(parents=True, exist_ok=True)

        # Enhanced validate_rules.py with frontmatter parsing and trigger uniqueness checks
        validate_rules = '''#!/usr/bin/env python3
import os, sys, re, json
from typing import Dict, List, Tuple, DefaultDict
from collections import defaultdict

RULES_ROOT = os.path.join('.cursor','rules')
REPORT_DIR = os.path.join('.cursor','tools','reports')

def iter_mdc(root: str) -> List[str]:
    out: List[str] = []
    for base, _, files in os.walk(root):
        for f in files:
            if f.lower().endswith('.mdc'):
                out.append(os.path.join(base, f))
    return out

def parse_frontmatter(content: str) -> Tuple[Dict[str,str], str]:
    if not content.startswith('---'):
        return {}, content
    parts = content.split('\n')
    try:
        end_idx = None
        for i in range(1, min(len(parts), 200)):
            if parts[i].strip() == '---':
                end_idx = i
                break
        if end_idx is None:
            return {}, content
        header_lines = parts[1:end_idx]
        body = '\n'.join(parts[end_idx+1:])
        meta: Dict[str,str] = {}
        for line in header_lines:
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
        return meta, body
    except Exception:
        return {}, content

def extract_triggers_and_scope(description: str) -> Tuple[List[str], str]:
    if not description:
        return [], ''
    triggers: List[str] = []
    scope = ''
    try:
        m_trg = re.search(r'TRIGGERS:\s*([^|]+)', description, flags=re.IGNORECASE)
        if m_trg:
            triggers = [t.strip() for t in m_trg.group(1).split(',') if t.strip()]
        m_scope = re.search(r'SCOPE:\s*([^|]+)', description, flags=re.IGNORECASE)
        if m_scope:
            scope = m_scope.group(1).strip()
    except Exception:
        pass
    return triggers, scope

def write_report(data: Dict[str, object]) -> None:
    try:
        os.makedirs(REPORT_DIR, exist_ok=True)
        with open(os.path.join(REPORT_DIR, 'rules_validation.json'), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def main() -> int:
    if not os.path.isdir(RULES_ROOT):
        print('[RULES] .cursor/rules not found; failing.')
        return 1
    files = iter_mdc(RULES_ROOT)
    if not files:
        print('[RULES] No .mdc rules found; failing.')
        return 1

    triggers_by_scope: DefaultDict[str, DefaultDict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    missing: List[str] = []
    missing_scope: List[str] = []

    for p in files:
        try:
            content = open(p, 'r', encoding='utf-8', errors='ignore').read()
        except Exception:
            missing.append(p)
            continue
        meta, _ = parse_frontmatter(content)
        desc = meta.get('description','')
        triggers, scope = extract_triggers_and_scope(desc)
        if not desc:
            print(f"[WARN] {p}: missing description frontmatter")
        if not scope:
            missing_scope.append(p)
            continue
        scope_key = scope.lower()
        for t in triggers:
            tkey = t.lower()
            triggers_by_scope[scope_key][tkey].append(p)

    duplicates_by_scope: Dict[str, Dict[str, List[str]]] = {}
    global_duplicates: Dict[str, List[str]] = {}

    # Build duplicates per scope and compute global duplicates (flattened) as warnings
    all_trigger_to_paths: DefaultDict[str, List[str]] = defaultdict(list)
    for scope_key, trig_map in triggers_by_scope.items():
        for tkey, paths in trig_map.items():
            if len(paths) > 1:
                duplicates_by_scope.setdefault(scope_key, {})[tkey] = paths
            all_trigger_to_paths[tkey].extend(paths)

    for tkey, paths in all_trigger_to_paths.items():
        if len(paths) > 1:
            global_duplicates[tkey] = paths

    if global_duplicates:
        print('[RULES] Global duplicate TRIGGERS detected (warning only):')
        for k, paths in global_duplicates.items():
            print(f"  - {k} ({len(paths)} occurrences)")

    if duplicates_by_scope:
        print('[RULES] Duplicate TRIGGERS detected within the same SCOPE (failing):')
        for scope_key, trig_map in duplicates_by_scope.items():
            print(f"  SCOPE: {scope_key}")
            for tkey, paths in trig_map.items():
                print(f"    - {tkey}:")
                for pp in paths:
                    print(f"      * {pp}")

    report_data = {
        'files_count': len(files),
        'scopes_count': len(triggers_by_scope),
        'triggers_by_scope': {k: {kk: len(vv) for kk, vv in v.items()} for k, v in triggers_by_scope.items()},
        'duplicates_by_scope': {k: list(v.keys()) for k, v in duplicates_by_scope.items()},
        'missing_scope_files': missing_scope,
        'missing_files': missing,
    }
    write_report(report_data)

    if duplicates_by_scope or missing or missing_scope:
        return 1
    print(f"[RULES] OK: {len(files)} rule files; scopes={len(triggers_by_scope)}; no intra-scope duplicates; all have SCOPE.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
'''
        (tools_dir / 'validate_rules.py').write_text(validate_rules)

        # Minimal check_compliance.py
        check_compliance = '''#!/usr/bin/env python3
import json, os, sys
proj_json = os.path.join('.cursor','project.json')
if not os.path.exists(proj_json):
    print('[COMPLIANCE] project.json missing; skipping.'); sys.exit(0)
cfg = json.load(open(proj_json))
req = set((cfg.get('compliance') or []))
missing = [c for c in req if not os.path.exists(os.path.join('.cursor','rules', f'industry-compliance-{c}.mdc'))]
if missing:
    print('[COMPLIANCE] Missing compliance rules:', ', '.join(missing))
    sys.exit(1)
print('[COMPLIANCE] All required compliance rules present.')
'''
        (tools_dir / 'check_compliance.py').write_text(check_compliance)

        # Router config and logs
        ai_dir = self.project_root / '.cursor' / 'ai-governor'
        ai_dir.mkdir(parents=True, exist_ok=True)
        (ai_dir / 'router-config.json').write_text(
            json.dumps(self._generate_ai_governor_router_config(), indent=2, sort_keys=True)
        )
        (ai_dir / 'sample-logs.json').write_text(
            json.dumps(self._generate_ai_governor_sample_logs(), indent=2, sort_keys=True)
        )
    
    def _generate_industry_gates(self):
        """Generate only the industry-specific gates overlay matching selected industry"""
        import yaml
        industry = (self.args.industry or '').lower()
        # Map known industries to their overlay content and filenames
        overlays = {
            'healthcare': ('gates_config_healthcare.yaml', self._generate_healthcare_gates()),
            'finance': ('gates_config_finance.yaml', self._generate_finance_gates()),
            'ecommerce': ('gates_config_ecommerce.yaml', self._generate_ecommerce_gates()),
        }
        if industry in overlays:
            fname, cfg = overlays[industry]
        else:
            # Sensible default overlay for other industries (saas, enterprise, etc.)
            cfg = {
                'quality_gates': {
                    'coverage': {'min': 90},
                    'critical_vulns': 0,
                    'high_vulns': 0,
                }
            }
            fname = f'gates_config_{industry or "general"}.yaml'
        (self.project_root / fname).write_text(
            yaml.dump(cfg, default_flow_style=False, sort_keys=True)
        )
    
    def _generate_documentation(self):
        """Generate project documentation"""
        docs_dir = self.project_root / 'docs'
        
        # API documentation template
        if self.args.backend != 'none':
            api_docs = self._generate_api_docs_template()
            (docs_dir / 'API.md').write_text(api_docs)
        
        # Deployment guide
        deployment_guide = self._generate_deployment_guide()
        (docs_dir / 'DEPLOYMENT.md').write_text(deployment_guide)
        
        # Development guide
        dev_guide = self._generate_development_guide()
        (docs_dir / 'DEVELOPMENT.md').write_text(dev_guide)
        
        # Compliance documentation
        if self.args.compliance:
            compliance_docs = self._generate_compliance_documentation()
            (docs_dir / 'COMPLIANCE.md').write_text(compliance_docs)

    def _generate_api_docs_template(self) -> str:
        """Generate API.md template content based on backend selection"""
        lines: List[str] = []
        lines.append("# API Documentation")
        lines.append("")
        lines.append("## Overview")
        lines.append(f"This document describes the API endpoints for the {self.args.name} backend.")
        lines.append("")
        if self.args.backend == 'fastapi':
            lines.append("### FastAPI")
            lines.append("- Interactive docs available at /docs (Swagger UI)")
            lines.append("- Alternative docs at /redoc")
            lines.append("")
            lines.append("## Authentication")
            lines.append("- Bearer JWT via Authorization header")
            lines.append("")
            lines.append("## Example Endpoints")
            lines.append("- GET /health")
            lines.append("- GET /items?skip=0&limit=100")
            lines.append("- POST /items")
        elif self.args.backend == 'django':
            lines.append("### Django REST Framework")
            lines.append("- API root available at /api/")
            lines.append("- Browsable API if enabled")
            lines.append("")
            lines.append("## Authentication")
            lines.append("- Session or Token depending on setup")
            lines.append("")
            lines.append("## Example Endpoints")
            lines.append("- GET /api/health/")
            lines.append("- GET /api/items/?page=1")
            lines.append("- POST /api/items/")
        elif self.args.backend == 'nestjs':
            lines.append("### NestJS")
            lines.append("- Swagger docs at /api by default if configured")
            lines.append("")
            lines.append("## Authentication")
            lines.append("- JWT / Passport strategies depending on setup")
        elif self.args.backend == 'go':
            lines.append("### Go HTTP")
            lines.append("- Swagger/OpenAPI if configured")
        else:
            lines.append("No backend endpoints defined.")
        lines.append("")
        lines.append("## Error Handling")
        lines.append("- Errors follow a standard JSON shape with `message` and optional `code`.")
        return "\n".join(lines)
    def _generate_deployment_guide(self) -> str:
        """Generate DEPLOYMENT.md content (text-only; no external side-effects)."""
        lines: List[str] = []
        lines.append("# Deployment Guide")
        lines.append("")
        lines.append("## Environments")
        lines.append("- Development (docker-compose)\n- Staging\n- Production")
        lines.append("")
        lines.append("## Prerequisites")
        lines.append("- Docker and Docker Compose installed")
        if self.args.frontend != 'none':
            lines.append("- Node.js 18+ for frontend build")
        if self.args.backend in ['fastapi', 'django']:
            lines.append("- Python 3.11+ for backend tasks")
        if self.args.backend == 'nestjs':
            lines.append("- Node.js 18+ (NestJS)")
        if self.args.backend == 'go':
            lines.append("- Go 1.21+ (Go backend)")
        lines.append("")
        lines.append("## Local Development")
        lines.append("```bash\nmake setup\nmake dev\n```")
        lines.append("")
        lines.append("## Build")
        lines.append("```bash\nmake build\n```")
        lines.append("")
        lines.append("## Deployment Targets")
        target = (self.args.deploy or 'self-hosted').lower()
        if target == 'aws':
            lines.append("### AWS (ECS/Fargate) - Outline")
            lines.append("1. Build and push images to ECR\n2. Provision ECS service and Task Definition\n3. Configure load balancer and target group\n4. Attach IAM roles and secrets\n5. Run database migrations")
        elif target == 'azure':
            lines.append("### Azure (AKS/App Service) - Outline")
            lines.append("1. Build and push images to ACR\n2. Deploy to AKS with manifests or Bicep\n3. Configure Ingress and secrets\n4. Run migrations")
        elif target == 'gcp':
            lines.append("### GCP (Cloud Run/GKE) - Outline")
            lines.append("1. Build and push images to Artifact Registry\n2. Deploy to Cloud Run or GKE\n3. Configure IAM and secrets\n4. Run migrations")
        elif target == 'vercel':
            lines.append("### Vercel (Frontend) - Outline")
            lines.append("1. Connect repository to Vercel\n2. Configure environment variables\n3. Deploy via Git push")
        else:
            lines.append("### Self-hosted - Outline")
            lines.append("1. Provision VM\n2. Install Docker\n3. Use docker-compose to run services\n4. Configure reverse proxy and TLS")
        lines.append("")
        lines.append("## Post-Deployment")
        lines.append("- Health checks\n- Log aggregation\n- Metrics and alerts\n- Backup and restore checks")
        return "\n".join(lines)

    def _generate_ai_governor_router_config(self) -> Dict[str, Any]:
        return {
            'routing': {
                'industry': self.args.industry,
                'project_type': self.args.project_type,
                'rules': [
                    '1-master-rule-context-discovery',
                    '3-master-rule-code-quality-checklist'
                ]
            }
        }

    def _generate_ai_governor_sample_logs(self) -> Dict[str, Any]:
        return {
            'decisions': [
                {'timestamp': 'T+0', 'action': 'load_rules', 'rules_loaded': 2},
                {'timestamp': 'T+1', 'action': 'route', 'target': 'backend'},
            ]
        }

    def _generate_healthcare_gates(self) -> Dict[str, Any]:
        return {
            'quality_gates': {
                'coverage': {'min': 90},
                'critical_vulns': 0,
                'high_vulns': 0
            },
            'compliance': {'hipaa': True}
        }

    def _generate_finance_gates(self) -> Dict[str, Any]:
        return {
            'quality_gates': {
                'coverage': {'min': 90},
                'critical_vulns': 0,
                'high_vulns': 0
            },
            'compliance': {'sox': True, 'pci': True}
        }

    def _generate_ecommerce_gates(self) -> Dict[str, Any]:
        return {
            'quality_gates': {
                'coverage': {'min': 80},
                'critical_vulns': 0,
                'high_vulns': 2
            },
            'compliance': {'gdpr': True}
        }
    
    def _initialize_git(self):
        """Initialize git repository"""
        subprocess.run(['git', 'init'], cwd=self.project_root, capture_output=True)
        subprocess.run(['git', 'add', '.'], cwd=self.project_root, capture_output=True)
        subprocess.run(
            ['git', 'commit', '-m', f'Initial commit for {self.args.name}'],
            cwd=self.project_root,
            capture_output=True
        )
    
    def _install_precommit_hook(self):
        """Install pre-commit hook"""
        hook_path = self.project_root / '.git' / 'hooks' / 'pre-commit'
        hook_path.parent.mkdir(parents=True, exist_ok=True)
        hook_script = (
            "#!/usr/bin/env bash\n"
            "set -euo pipefail\n"
            "command -v python >/dev/null 2>&1 || { echo '[HOOK] python not found; skipping rules checks'; exit 0; }\n"
            "python .cursor/tools/validate_rules.py\n"
            "python .cursor/tools/check_compliance.py\n"
        )
        hook_path.write_text(hook_script)
        try:
            os.chmod(hook_path, 0o755)
        except Exception:
            pass
    
    def _generate_setup_commands(self) -> List[str]:
        """Generate setup commands for the project"""
        commands = []
        
        # Frontend setup
        if self.args.frontend != 'none':
            if self.args.frontend in ['nextjs', 'nuxt', 'angular']:
                commands.append('cd frontend && npm install')
            elif self.args.frontend == 'expo':
                commands.append('cd frontend && npm install && npx expo install')
        
        # Backend setup
        if self.args.backend != 'none':
            if self.args.backend == 'fastapi':
                commands.append('cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt')
            elif self.args.backend == 'django':
                commands.append('cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate')
            elif self.args.backend == 'nestjs':
                commands.append('cd backend && npm install')
            elif self.args.backend == 'go':
                commands.append('cd backend && go mod download')
        
        # Docker setup
        if self.args.database != 'none':
            commands.append('docker-compose up -d')
        
        return commands
    
    def _generate_next_steps(self) -> List[str]:
        """Generate next steps for the user"""
        steps = [
            f"cd {self.args.name}",
            "Review the generated project structure",
            "Update environment variables in .env files"
        ]
        
        if not self.args.no_install:
            steps.append("Run 'make setup' to install dependencies")
        
        steps.extend([
            "Run 'make dev' to start the development environment",
            "Review documentation in the docs/ directory"
        ])
        
        if self.args.compliance:
            steps.append("Review compliance requirements in docs/COMPLIANCE.md")
        
        return steps
    
    def get_project_structure(self) -> Dict[str, Any]:
        """Get the project structure for dry-run display"""
        structure = {
            'name': self.args.name,
            'children': []
        }
        
        # Add main directories
        if self.args.frontend != 'none':
            structure['children'].append({
                'name': 'frontend/',
                'children': [
                    {'name': 'src/'},
                    {'name': 'public/'},
                    {'name': 'package.json'}
                ]
            })
        
        if self.args.backend != 'none':
            structure['children'].append({
                'name': 'backend/',
                'children': [
                    {'name': 'src/'},
                    {'name': 'tests/'},
                    {'name': 'requirements.txt' if self.args.backend in ['fastapi', 'django'] else 'package.json'}
                ]
            })
        
        extras: List[Dict[str, Any]] = []
        if not self.no_cursor_assets:
            extras.append({
                'name': '.cursor/',
                'children': [
                    {'name': 'rules/'},
                    {'name': 'project.json'}
                ]
            })
        extras.append({
                'name': '.github/',
                'children': [
                    {'name': 'workflows/'}
                ]
            })
        extras.extend([
            {'name': 'docs/'},
            {'name': 'docker-compose.yml'},
            {'name': 'Makefile'},
            {'name': 'README.md'}
        ])
        structure['children'].extend(extras)
        
        return structure
    
    def display_structure(self, structure: Dict[str, Any], prefix: str = ""):
        """Display project structure in tree format"""
        print(f"{prefix}{structure['name']}")
        
        if 'children' in structure:
            for i, child in enumerate(structure['children']):
                is_last = i == len(structure['children']) - 1
                child_prefix = prefix + ("└── " if is_last else "├── ")
                self.display_structure(child, prefix + ("    " if is_last else "│   "))
    
    def run_setup_commands(self, project_path: str, commands: List[str]):
        """Run setup commands for the project"""
        print("\n🚀 Running setup commands...")
        
        for command in commands:
            print(f"\n  ▶ {command}")
            
            # Handle cd commands
            if command.startswith('cd '):
                parts = command.split(' && ')
                working_dir = os.path.join(project_path, parts[0].replace('cd ', ''))
                actual_command = ' && '.join(parts[1:]) if len(parts) > 1 else 'echo "Changed directory"'
                
                result = subprocess.run(
                    actual_command,
                    shell=True,
                    cwd=working_dir,
                    capture_output=True,
                    text=True
                )
            else:
                result = subprocess.run(
                    command,
                    shell=True,
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
            
            if result.returncode == 0:
                print("    ✅ Success")
            else:
                print(f"    ❌ Failed: {result.stderr}")
    
    # Template generation methods (simplified versions)
    def _generate_gitignore(self) -> str:
        """Generate .gitignore content"""
        return """# Dependencies
node_modules/
venv/
__pycache__/
*.pyc

# Environment
.env
.env.local
.env.*.local

# Build outputs
dist/
build/
.next/
.nuxt/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Testing
coverage/
.coverage
htmlcov/
.pytest_cache/

# Docker
*.pid
"""
    
    def _generate_readme(self) -> str:
        """Generate README.md content"""
        features_block = '\n'.join(['- ' + feature for feature in self.config.merge_features(self.args.features)])
        compliance_list = (self.args.compliance.split(',') if self.args.compliance else ['None'])
        compliance_block = '\n'.join(['- ' + c.upper() for c in compliance_list])
        comp_doc_line = '- [Compliance Documentation](docs/COMPLIANCE.md)' if self.args.compliance else ''
        return f"""# {self.args.name}

## Overview
{self.args.industry.title()} {self.args.project_type} application built with modern technologies.

## Technology Stack
- **Frontend**: {self.args.frontend if self.args.frontend != 'none' else 'N/A'}
- **Backend**: {self.args.backend if self.args.backend != 'none' else 'N/A'}
- **Database**: {self.args.database if self.args.database != 'none' else 'N/A'}
- **Authentication**: {self.args.auth if self.args.auth != 'none' else 'N/A'}
- **Deployment**: {self.args.deploy}

## Features
{features_block}

## Compliance
{compliance_block}

## Quick Start

1. Install dependencies:
   ```bash
   make setup
   ```

2. Start development environment:
   ```bash
   make dev
   ```

3. Run tests:
   ```bash
   make test
   ```

## Documentation
- [Development Guide](docs/DEVELOPMENT.md)
- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
{comp_doc_line}

## License
Proprietary - All rights reserved
"""
    
    def _generate_devcontainer_config(self) -> Dict[str, Any]:
        """Generate devcontainer configuration"""
        config = {
            "name": f"{self.args.name} Dev Container",
            "dockerComposeFile": "../docker-compose.yml",
            "service": "dev",
            "workspaceFolder": "/workspace",
            "features": {},
            "customizations": {
                "vscode": {
                    "extensions": [],
                    "settings": {}
                }
            }
        }
        
        # Add language-specific extensions
        if self.args.frontend in ['nextjs', 'nuxt', 'angular']:
            config["customizations"]["vscode"]["extensions"].extend([
                "dbaeumer.vscode-eslint",
                "esbenp.prettier-vscode",
                "bradlc.vscode-tailwindcss"
            ])
        
        if self.args.backend == 'fastapi' or self.args.backend == 'django':
            config["customizations"]["vscode"]["extensions"].extend([
                "ms-python.python",
                "ms-python.vscode-pylance",
                "ms-python.black-formatter"
            ])
        
        return config
    
    def _generate_docker_compose(self) -> str:
        """Generate docker-compose.yml content"""
        services = {
            "dev": {
                "build": ".",
                "volumes": [".:/workspace"],
                "ports": [],
                "environment": ["NODE_ENV=development"]
            }
        }
        
        # Add frontend ports
        if self.args.frontend != 'none':
            services["dev"]["ports"].append("3000:3000")
        
        # Add backend ports
        if self.args.backend != 'none':
            services["dev"]["ports"].append("8000:8000")
        
        # Add database service
        if self.args.database == 'postgres':
            services["postgres"] = {
                "image": "postgres:15",
                "environment": [
                    "POSTGRES_DB=myapp",
                    "POSTGRES_USER=postgres",
                    "POSTGRES_PASSWORD=postgres"
                ],
                "ports": ["5432:5432"],
                "volumes": ["postgres_data:/var/lib/postgresql/data"]
            }
        elif self.args.database == 'mongodb':
            services["mongodb"] = {
                "image": "mongo:6",
                "environment": [
                    "MONGO_INITDB_ROOT_USERNAME=admin",
                    "MONGO_INITDB_ROOT_PASSWORD=admin"
                ],
                "ports": ["27017:27017"],
                "volumes": ["mongo_data:/data/db"]
            }
        
        # Convert to YAML format (simplified)
        compose = "version: '3.8'\n\nservices:\n"
        for service, config in services.items():
            compose += f"  {service}:\n"
            for key, value in config.items():
                if isinstance(value, list):
                    compose += f"    {key}:\n"
                    for item in value:
                        compose += f"      - {item}\n"
                else:
                    compose += f"    {key}: {value}\n"
        
        if self.args.database in ['postgres', 'mongodb']:
            compose += "\nvolumes:\n"
            if self.args.database == 'postgres':
                compose += "  postgres_data:\n"
            else:
                compose += "  mongo_data:\n"
        
        return compose
    
    def _generate_makefile(self) -> str:
        """Generate Makefile content"""
        return f""".PHONY: setup dev test lint build deploy clean

# Setup project
setup:
	@echo "Setting up {self.args.name}..."
{'	cd frontend && npm install' if self.args.frontend != 'none' else ''}
{'	cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt' if self.args.backend in ['fastapi', 'django'] else ''}
{'	cd backend && npm install' if self.args.backend == 'nestjs' else ''}
{'	cd backend && go mod download' if self.args.backend == 'go' else ''}
	@echo "Setup complete!"

# Start development environment
dev:
	docker-compose up -d
{'	cd frontend && npm run dev &' if self.args.frontend != 'none' else ''}
{'	cd backend && python main.py' if self.args.backend == 'fastapi' else ''}
{'	cd backend && python manage.py runserver' if self.args.backend == 'django' else ''}
{'	cd backend && npm run start:dev' if self.args.backend == 'nestjs' else ''}
{'	cd backend && go run main.go' if self.args.backend == 'go' else ''}

# Run tests
test:
{'	cd frontend && npm test' if self.args.frontend != 'none' else ''}
{'	cd backend && pytest' if self.args.backend in ['fastapi', 'django'] else ''}
{'	cd backend && npm test' if self.args.backend == 'nestjs' else ''}
{'	cd backend && go test ./...' if self.args.backend == 'go' else ''}

# Run linters
lint:
{'	cd frontend && npm run lint' if self.args.frontend != 'none' else ''}
{'	cd backend && black . && flake8' if self.args.backend in ['fastapi', 'django'] else ''}
{'	cd backend && npm run lint' if self.args.backend == 'nestjs' else ''}
{'	cd backend && golangci-lint run' if self.args.backend == 'go' else ''}

# Build for production
build:
{'	cd frontend && npm run build' if self.args.frontend != 'none' else ''}
{'	cd backend && python -m build' if self.args.backend in ['fastapi', 'django'] else ''}
{'	cd backend && npm run build' if self.args.backend == 'nestjs' else ''}
{'	cd backend && go build -o app' if self.args.backend == 'go' else ''}

# Deploy application
deploy:
	@echo "Deploying to {self.args.deploy}..."
	# Add deployment commands here

# Clean build artifacts
clean:
	rm -rf node_modules/
	rm -rf venv/
	rm -rf __pycache__/
	rm -rf dist/
	rm -rf build/
	docker-compose down -v
"""
    
    def _generate_vscode_snippets(self):
        """Generate VS Code snippets"""
        snippets_dir = self.project_root / '.vscode'
        
        # Language-specific snippets
        if self.args.frontend in ['nextjs', 'nuxt']:
            snippets = {
                "React Component": {
                    "prefix": "rfc",
                    "body": [
                        "import React from 'react';",
                        "",
                        "interface ${1:ComponentName}Props {",
                        "  $2",
                        "}",
                        "",
                        "export const ${1:ComponentName}: React.FC<${1:ComponentName}Props> = ({$3}) => {",
                        "  return (",
                        "    <div>",
                        "      $0",
                        "    </div>",
                        "  );",
                        "};",
                        ""
                    ],
                    "description": "Create a React functional component"
                }
            }
            (snippets_dir / 'typescript.json').write_text(json.dumps(snippets, indent=2))
        
        if self.args.backend == 'fastapi':
            snippets = {
                "FastAPI Endpoint": {
                    "prefix": "endpoint",
                    "body": [
                        "@router.${1|get,post,put,delete|}('/${2:path}')",
                        "async def ${3:function_name}(",
                        "    $4",
                        ") -> ${5:dict}:",
                        '    """',
                        "    ${6:Description}",
                        '    """',
                        "    $0",
                        "    return {}"
                    ],
                    "description": "Create a FastAPI endpoint"
                }
            }
            (snippets_dir / 'python.json').write_text(json.dumps(snippets, indent=2))
    
    def _generate_lint_workflow(self) -> str:
        """Generate lint workflow"""
        frontend_block = ""
        if self.args.frontend != 'none':
            frontend_block = (
                "    - name: Setup Node.js\n"
                "      uses: actions/setup-node@v3\n"
                "      with:\n"
                "        node-version: '18'\n"
                "        cache: 'npm'\n"
                "        cache-dependency-path: frontend/package-lock.json\n\n"
                "    - name: Install frontend dependencies\n"
                "      run: cd frontend && npm ci\n\n"
                "    - name: Run frontend lint\n"
                "      run: cd frontend && npm run lint\n"
            )

        backend_block = ""
        if self.args.backend in ['fastapi', 'django']:
            backend_block = (
                "    - name: Setup Python\n"
                "      uses: actions/setup-python@v4\n"
                "      with:\n"
                "        python-version: '3.11'\n\n"
                "    - name: Install backend dependencies\n"
                "      run: |\n"
                "        cd backend\n"
                "        pip install -r requirements-dev.txt\n\n"
                "    - name: Run backend lint\n"
                "      run: |\n"
                "        cd backend\n"
                "        black --check .\n"
                "        flake8 .\n"
            )

        return (
            "name: Lint\n\n"
            "on:\n"
            "  push:\n"
            "    branches: [main, develop]\n"
            "  pull_request:\n"
            "    branches: [main, develop]\n\n"
            "jobs:\n"
            "  lint:\n"
            "    runs-on: ubuntu-latest\n\n"
            "    steps:\n"
            "    - uses: actions/checkout@v3\n\n"
            f"{frontend_block}"
            f"{backend_block}"
        )
    
    def _generate_test_workflow(self) -> str:
        """Generate test workflow"""
        services_block = ""
        if self.args.database == 'postgres':
            services_block = (
                "    services:\n"
                "      postgres:\n"
                "        image: postgres:15\n"
                "        env:\n"
                "          POSTGRES_PASSWORD: postgres\n"
                "        options: >-\n"
                "          --health-cmd pg_isready\n"
                "          --health-interval 10s\n"
                "          --health-timeout 5s\n"
                "          --health-retries 5\n"
                "        ports:\n"
                "          - 5432:5432\n"
            )

        frontend_block = ""
        if self.args.frontend != 'none':
            frontend_block = (
                "    - name: Setup Node.js\n"
                "      uses: actions/setup-node@v3\n"
                "      with:\n"
                "        node-version: '18'\n\n"
                "    - name: Install and test frontend\n"
                "      run: |\n"
                "        cd frontend\n"
                "        npm ci\n"
                "        npm test -- --coverage\n"
            )

        backend_block = ""
        if self.args.backend in ['fastapi', 'django']:
            backend_block = (
                "    - name: Setup Python\n"
                "      uses: actions/setup-python@v4\n"
                "      with:\n"
                "        python-version: '3.11'\n\n"
                "    - name: Install and test backend\n"
                "      run: |\n"
                "        cd backend\n"
                "        pip install -r requirements-test.txt\n"
                "        pytest --cov=. --cov-report=xml\n"
            )

        return (
            "name: Test\n\n"
            "on:\n"
            "  push:\n"
            "    branches: [main, develop]\n"
            "  pull_request:\n"
            "    branches: [main, develop]\n\n"
            "jobs:\n"
            "  test:\n"
            "    runs-on: ubuntu-latest\n\n"
            f"{services_block if services_block else ''}"
            "    steps:\n"
            "    - uses: actions/checkout@v3\n\n"
            f"{frontend_block}"
            f"{backend_block}"
            "    - name: Upload coverage\n"
            "      uses: codecov/codecov-action@v3\n"
        )
    
    def _generate_security_workflow(self) -> str:
        """Generate security scan workflow"""
        return """name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday

jobs:
  security:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: '.'
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload Trivy scan results
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'
    
    - name: Run dependency check
      uses: dependency-check/Dependency-Check_Action@main
      with:
        project: '${{ github.repository }}'
        path: '.'
        format: 'HTML'
"""
    
    def _generate_deploy_workflow(self) -> str:
        """Generate deployment workflow"""
        deploy_steps = {
            'aws': """    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
    
    - name: Deploy to AWS
      run: |
        # Add AWS deployment commands""",
            
            'azure': """    - name: Login to Azure
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}
    
    - name: Deploy to Azure
      run: |
        # Add Azure deployment commands""",
            
            'gcp': """    - name: Setup Cloud SDK
      uses: google-github-actions/setup-gcloud@v1
      with:
        service_account_key: ${{ secrets.GCP_SA_KEY }}
        project_id: ${{ secrets.GCP_PROJECT_ID }}
    
    - name: Deploy to GCP
      run: |
        # Add GCP deployment commands""",
            
            'vercel': """    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v20
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}"""
        }
        
        return f"""name: Deploy

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    
    steps:
    - uses: actions/checkout@v3
    
{deploy_steps.get(self.args.deploy, '    # Add deployment steps')}
"""
    
    def _generate_gates_config(self) -> str:
        """Generate gates configuration"""
        config = {
            'quality_gates': {
                'lint': {
                    'required': True,
                    'threshold': 0
                },
                'test_coverage': {
                    'required': True,
                    'threshold': 80 if self.args.industry in ['healthcare', 'finance'] else 70
                },
                'security_scan': {
                    'required': True,
                    'critical_threshold': 0,
                    'high_threshold': 0 if self.args.industry in ['healthcare', 'finance'] else 5
                }
            },
            'compliance_gates': {}
        }
        
        # Add compliance-specific gates
        if self.args.compliance:
            for compliance in self.args.compliance.split(','):
                if compliance.strip() == 'hipaa':
                    config['compliance_gates']['hipaa'] = {
                        'encryption_check': True,
                        'audit_logging': True,
                        'access_control_review': True
                    }
                elif compliance.strip() == 'gdpr':
                    config['compliance_gates']['gdpr'] = {
                        'privacy_impact': True,
                        'consent_tracking': True,
                        'data_retention_check': True
                    }
                elif compliance.strip() == 'sox':
                    config['compliance_gates']['sox'] = {
                        'change_control': True,
                        'segregation_of_duties': True,
                        'audit_trail_validation': True
                    }
                elif compliance.strip() == 'pci':
                    config['compliance_gates']['pci'] = {
                        'cardholder_data_check': True,
                        'network_segmentation': True,
                        'encryption_validation': True
                    }
        # Convert to YAML format (deterministic)
        import yaml
        return yaml.dump(config, default_flow_style=False, sort_keys=True)
        
    def _generate_client_rules(self) -> str:
        """Generate client-specific rules (safe builder)"""
        uptime = '>99.99%' if self.args.industry in ['healthcare', 'finance'] else '>99.9%'
        if self.args.backend != 'none':
            rt_threshold = '200ms' if self.args.industry == 'finance' else '500ms'
            response_time = f"<{rt_threshold}"
        else:
            response_time = 'N/A'
        coverage = 80 if self.args.industry in ['healthcare', 'finance'] else 70
        ecommerce_extra = []
        if self.args.industry == 'ecommerce':
            ecommerce_extra = [
                '## E-commerce Enhancements',
                '- Mobile-first design approach',
                '- A/B testing infrastructure'
            ]
        lines: List[str] = []
        lines.append("---")
        lines.append("alwaysApply: true")
        # Extended triggers consistent with ai-driven-workflow
        client_triggers = [
            'development', 'coding', 'implementation', 'update all', 'refresh all', 'sync all', 'reload all',
            'bootstrap', 'setup', 'initialize', 'project start', 'master plan', 'framework ecosystem',
            'background agents', 'prd', 'requirements', 'feature planning', 'product spec', 'task generation',
            'technical planning', 'implementation plan', 'execute', 'implement', 'process tasks',
            'retrospective', 'review', 'improvement', 'post-implementation', 'parallel execution',
            'coordination', 'multi-agent', 'analyze'
        ]
        lines.append(
            f"description: \"TAGS: [project,client,standards] | TRIGGERS: {','.join(client_triggers)} | SCOPE: project:{self.args.name} | DESCRIPTION: Client-specific rules and standards for {self.args.name}\""
        )
        lines.append("---")
        lines.append("")
        lines.append(f"# Client-Specific Rules: {self.args.name}")
        lines.append("")
        lines.append("## Project Context")
        lines.append(f"- **Industry**: {self.args.industry}")
        lines.append(f"- **Project Type**: {self.args.project_type}")
        lines.append(f"- **Technology Stack**: {self.args.frontend}/{self.args.backend}/{self.args.database}")
        lines.append(f"- **Compliance Requirements**: {self.args.compliance or 'None'}")
        lines.append("")
        lines.extend(ecommerce_extra)
        if ecommerce_extra:
            lines.append("")
        lines.append("## Communication Protocols")
        lines.append("- Daily standup: 9:00 AM")
        lines.append("- Sprint planning: Bi-weekly")
        lines.append("- Retrospectives: End of each sprint")
        lines.append("- Emergency contact: On-call rotation")
        lines.append("")
        lines.append("## Success Metrics")
        lines.append(f"- Uptime: {uptime}")
        lines.append(f"- Response time: {response_time}")
        lines.append("- Error rate: <0.1%")
        lines.append(f"- Test coverage: >{coverage}%")
        return "\n".join(lines)

    def _generate_workflow_rules(self) -> str:
        """Generate process/workflow rules with extended triggers and Cursor frontmatter."""
        triggers = [
            'update all', 'refresh all', 'sync all', 'reload all', 'execute', 'implement', 'process tasks',
            'bootstrap', 'setup', 'initialize', 'project start', 'master plan', 'framework ecosystem',
            'background agents', 'prd', 'requirements', 'feature planning', 'product spec', 'task generation',
            'technical planning', 'implementation plan', 'development', 'retrospective', 'review', 'improvement',
            'post-implementation', 'parallel execution', 'coordination', 'multi-agent', 'analyze'
        ]
        frontmatter = [
            '---',
            'alwaysApply: false',
            f"description: \"TAGS: [workflow,process,project] | TRIGGERS: {','.join(triggers)} | SCOPE: project:{self.args.name} | DESCRIPTION: Project workflow and process rules for {self.args.name}\"",
            '---',
            ''
        ]
        body = [
            f"# Project Workflow Rules: {self.args.name}",
            "",
            "## Process Gates",
            "- Run pre-commit compliance checks",
            "- Enforce lint and test passes in CI",
            "- Block release if gates_config thresholds fail",
            "",
            "## Execution Protocols",
            "- Use 'update all' to normalize rule formatting",
            "- Use 'execute' to process tasks per implementation plan",
            "- Use 'refresh all' to resync generated assets",
        ]
        return "\n".join(frontmatter + body)

    # Public API methods for test compatibility
    def set_config(self, config: Dict[str, Any]):
        """Set and validate project configuration"""
        is_valid, errors = self.validator.validate_config(config)
        if not is_valid:
            raise ValueError(f"Invalid configuration: {errors}")
        self.config = config.copy()
        self.project_name = config.get('name')
    
    def get_template_path(self, component: str, technology: str) -> Path:
        """Get template path for component and technology using unified registry"""
        try:
            # Try to get template from unified registry first
            if hasattr(self.template_registry, 'get_template_path'):
                # This is the unified template registry
                template_path = self.template_registry.get_template_path(component, technology, 'base')
                if template_path and template_path.exists():
                    return template_path
            else:
                # Fall back to legacy registry method
                template_info = self.template_registry.get_template(component, technology)
                if template_info:
                    return Path(template_info['path'])
        except Exception:
            pass

        # Fallback to hardcoded paths for backward compatibility
        if hasattr(self, 'template_dir'):
            # Legacy test interface
            template_path = self.template_dir / component / technology / 'base'
        else:
            # Production interface
            template_path = Path(__file__).parent.parent.parent / 'template-packs' / component / technology / 'base'

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        return template_path
    
    def copy_template(self, source_dir: Path, target_dir: Path):
        """Copy template directory with ignore patterns"""
        import shutil
        
        def ignore_patterns(dir, files):
            return [f for f in files if f in {'__pycache__', '.pytest_cache', '.DS_Store', '.git', 'node_modules'}]
        
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        if target_dir.exists():
            shutil.rmtree(target_dir)
        shutil.copytree(source_dir, target_dir, ignore=ignore_patterns)
    
    def process_template_file(self, content: str) -> str:
        """Process template file content with variable substitution"""
        variables = self.get_template_variables()
        for var, value in variables.items():
            content = content.replace(f'{{{{{var}}}}}', str(value))
        return content
    
    def get_template_variables(self) -> Dict[str, str]:
        """Get template variables for substitution"""
        config = self.config if isinstance(self.config, dict) else {}
        
        def list_to_string(value):
            if isinstance(value, list):
                return ','.join(str(v) for v in value)
            return str(value) if value else ''
        
        return {
            'PROJECT_NAME': config.get('name', getattr(self.args, 'name', 'test-project')),
            'INDUSTRY': config.get('industry', getattr(self.args, 'industry', 'healthcare')),
            'PROJECT_TYPE': config.get('project_type', getattr(self.args, 'project_type', 'fullstack')),
            'FRONTEND': config.get('frontend', getattr(self.args, 'frontend', 'nextjs')),
            'BACKEND': config.get('backend', getattr(self.args, 'backend', 'fastapi')),
            'DATABASE': config.get('database', getattr(self.args, 'database', 'postgres')),
            'AUTH': config.get('auth', getattr(self.args, 'auth', 'auth0')),
            'DEPLOY': config.get('deploy', getattr(self.args, 'deploy', 'aws')),
            'COMPLIANCE': list_to_string(config.get('compliance', getattr(self.args, 'compliance', ''))),
            'FEATURES': list_to_string(config.get('features', getattr(self.args, 'features', '')))
        }
    
    def create_project_structure(self, project_dir: Path):
        """Create project structure and copy templates"""
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Create .gitignore
        gitignore_content = self._generate_gitignore()
        (project_dir / '.gitignore').write_text(gitignore_content)
        
        config = self.config if isinstance(self.config, dict) else {}
        frontend = config.get('frontend', getattr(self.args, 'frontend', 'none'))
        backend = config.get('backend', getattr(self.args, 'backend', 'none'))
        database = config.get('database', getattr(self.args, 'database', 'none'))
        
        # Copy templates conditionally
        if frontend and frontend != 'none':
            try:
                source = self.get_template_path('frontend', frontend)
                target = project_dir / 'frontend'
                self.copy_template(source, target)
            except FileNotFoundError:
                pass  # Template not found, skip
        
        if backend and backend != 'none':
            try:
                source = self.get_template_path('backend', backend)
                target = project_dir / 'backend'
                self.copy_template(source, target)
            except FileNotFoundError:
                pass  # Template not found, skip
        
        if database and database != 'none':
            try:
                source = self.get_template_path('database', database)
                target = project_dir / 'database'
                self.copy_template(source, target)
            except FileNotFoundError:
                pass  # Template not found, skip
    
    def run_setup_script(self, project_dir: Path) -> bool:
        """Run setup script if it exists"""
        setup_script = project_dir / 'setup.sh'
        if not setup_script.exists():
            return True
        
        try:
            result = subprocess.run(['bash', str(setup_script)], 
                                  cwd=project_dir, 
                                  capture_output=True, 
                                  timeout=300)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def generate_readme(self, project_dir: Path):
        """Generate README with meta, commands, and health URLs"""
        variables = self.get_template_variables()
        health_urls = self.get_health_check_urls()
        
        readme_content = f"""# {variables['PROJECT_NAME']}

## Project Information
- **Name**: {variables['PROJECT_NAME']}
- **Industry**: {variables['INDUSTRY']}
- **Project Type**: {variables['PROJECT_TYPE']}
- **Frontend**: {variables['FRONTEND']}
- **Backend**: {variables['BACKEND']}
- **Database**: {variables['DATABASE']}
- **Auth**: {variables['AUTH']}
- **Deploy**: {variables['DEPLOY']}

## Makefile Commands
- `setup` - Install dependencies
- `dev` - Start development environment
- `test` - Run tests
- `build` - Build for production

## Health Check URLs
- **Frontend**: {health_urls.get('frontend', 'N/A')}
- **Backend**: {health_urls.get('backend', 'N/A')}
- **Database**: {health_urls.get('database', 'N/A')}
"""
        (project_dir / 'README.md').write_text(readme_content)
    
    def generate_docker_compose(self, project_dir: Path):
        """Generate docker-compose.yml"""
        content = self._generate_docker_compose()
        (project_dir / 'docker-compose.yml').write_text(content)
    
    def generate_makefile(self, project_dir: Path):
        """Generate Makefile"""
        content = self._generate_makefile()
        (project_dir / 'Makefile').write_text(content)
    
    def validate_dependencies(self) -> bool:
        """Validate required system dependencies"""
        from shutil import which
        
        # Check Docker
        if which('docker') is None:
            return False
        
        # Check Node if frontend configured
        config = self.config if isinstance(self.config, dict) else {}
        frontend = config.get('frontend', getattr(self.args, 'frontend', 'none'))
        backend = config.get('backend', getattr(self.args, 'backend', 'none'))
        
        if (frontend and frontend != 'none') or backend == 'nestjs':
            if which('node') is None:
                return False
        
        return True
    
    def get_health_check_urls(self) -> Dict[str, str]:
        """Get health check URLs for services"""
        variables = self.get_template_variables()
        project_name = variables['PROJECT_NAME']
        
        return {
            'frontend': 'http://localhost:3000/api/health',
            'backend': 'http://localhost:8000/health',
            'database': f'postgresql://postgres:postgres@localhost:5432/{project_name}'
        }
    
    def cleanup_on_failure(self, project_dir: Path):
        """Clean up project directory on failure"""
        import shutil
        try:
            if project_dir.exists():
                shutil.rmtree(project_dir)
        except Exception:
            pass  # Best effort cleanup
    
    def generate_project(self) -> Dict[str, Any]:
        """Generate complete project with error handling"""
        if hasattr(self, 'output_dir'):
            # Legacy test interface
            project_dir = self.output_dir / self.config.get('name', 'test-project')
        else:
            # Production interface
            project_dir = Path(self.args.output_dir) / self.args.name
        
        try:
            # Orchestrate generation
            self.create_project_structure(project_dir)
            self.generate_docker_compose(project_dir)
            self.generate_makefile(project_dir)
            self.generate_readme(project_dir)
            
            setup_success = self.run_setup_script(project_dir)
            
            return True  # Tests expect boolean return
        except Exception as e:
            self.cleanup_on_failure(project_dir)
            raise e

    def _generate_development_guide_legacy(self) -> str:
        """Legacy development guide (disabled)"""
        return ""

    def _generate_development_guide(self) -> str:
        """Generate development guide (safe builder)"""
        lines: List[str] = []
        lines.append("# Development Guide")
        lines.append("")
        lines.append("## Getting Started")
        lines.append("")
        lines.append("### Prerequisites")
        if self.args.frontend != 'none' or self.args.backend == 'nestjs':
            lines.append("- Node.js 18+")
        if self.args.backend in ['fastapi', 'django']:
            lines.append("- Python 3.11+")
        if self.args.backend == 'go':
            lines.append("- Go 1.21+")
        lines.append("- Docker and Docker Compose")
        lines.append("- Git")
        lines.append("")
        lines.append("### Initial Setup")
        lines.append("")
        lines.append("1. **Clone the repository**")
        lines.append("   ```bash")
        lines.append(f"   git clone https://github.com/yourorg/{self.args.name}.git")
        lines.append(f"   cd {self.args.name}")
        lines.append("   ```")
        lines.append("")
        lines.append("2. **Install dependencies**")
        lines.append("   ```bash")
        lines.append("   make setup")
        lines.append("   ```")
        lines.append("")
        lines.append("3. **Configure environment**")
        lines.append("   ```bash")
        lines.append("   cp .env.example .env")
        lines.append("   # Edit .env with your values")
        lines.append("   ```")
        lines.append("")
        lines.append("4. **Start development environment**")
        lines.append("   ```bash")
        lines.append("   make dev")
        lines.append("   ```")
        lines.append("")
        lines.append("## Development Workflow")
        lines.append("")
        lines.append("1. Pull latest changes: `git pull origin develop`")
        lines.append("2. Create a feature branch: `git checkout -b feature/TICKET-description`")
        lines.append("3. Implement changes, add tests, update docs")
        lines.append("4. Run tests: `make test` and linters: `make lint`")
        lines.append("5. Commit and push: `git add . && git commit -m \"feat: ...\" && git push`")
        lines.append("6. Open a Pull Request and request review")
        lines.append("")
        lines.append("## Testing")
        lines.append("")
        lines.append("### Test Structure")
        lines.append("```")
        lines.append("tests/")
        lines.append("├── unit/")
        lines.append("├── integration/")
        lines.append("├── e2e/")
        lines.append("└── fixtures/")
        lines.append("```")
        lines.append("")
        lines.append("### Running Tests")
        lines.append("```bash")
        lines.append("make test")
        lines.append("```")
        lines.append("")
        lines.append("## Security Best Practices")
        lines.append("- Never commit secrets")
        lines.append("- Validate all inputs")
        lines.append("- Use parameterized queries")
        lines.append("- Implement rate limiting")
        lines.append("- Keep dependencies updated")
        lines.append("")
        lines.append("## Resources")
        lines.append("### Documentation")
        if self.args.frontend != 'none':
            lines.append(f"- {self.args.frontend} Docs: https://docs.{self.args.frontend}.com")
        if self.args.backend != 'none':
            lines.append(f"- {self.args.backend} Docs: https://docs.{self.args.backend}.com")
        lines.append(f"- Project Wiki: https://github.com/yourorg/{self.args.name}/wiki")
        return "\n".join(lines)

    def _generate_compliance_documentation(self) -> str:
        """Generate compliance documentation"""
        sections = []
        
        if self.args.compliance:
            for compliance in self.args.compliance.split(','):
                compliance = compliance.strip().lower()
                if compliance == 'hipaa':
                    sections.append("""## HIPAA Compliance

### Overview
This application is designed to be HIPAA-compliant for handling Protected Health Information (PHI).

### Technical Safeguards
1. **Encryption**
   - AES-256 encryption at rest
   - TLS 1.2+ for data in transit
   - Key management via AWS KMS

2. **Access Control**
   - Multi-factor authentication required
   - Role-based access control (RBAC)
   - Session timeout after 15 minutes
   - Audit logging of all PHI access

3. **Audit Controls**
   - Comprehensive audit logs
   - Log retention for 6 years
   - Regular audit log reviews
   - Automated anomaly detection

### Administrative Safeguards
1. **Training**
   - Annual HIPAA training required
   - Access granted only after training completion
   - Regular security awareness updates

2. **Access Management**
   - Minimum necessary access principle
   - Regular access reviews
   - Immediate termination procedures
   - Business Associate Agreements (BAAs)

### Physical Safeguards
1. **Data Center Security**
   - SOC 2 certified facilities
   - 24/7 physical security
   - Environmental controls
   - Redundant power and cooling

### Incident Response
1. **Breach Notification**
   - 60-day notification requirement
   - Documented incident response plan
   - Regular drills and updates
   - Chain of custody procedures""")
                
                elif compliance == 'gdpr':
                    sections.append("""## GDPR Compliance

### Overview
This application complies with the General Data Protection Regulation (GDPR) for EU data subjects.

### Data Protection Principles
1. **Lawfulness and Transparency**
   - Clear privacy policy
   - Explicit consent mechanisms
   - Lawful basis documented

2. **Purpose Limitation**
   - Data collected for specific purposes
   - No secondary use without consent
   - Purpose documentation maintained

3. **Data Minimization**
   - Only necessary data collected
   - Regular data audits
   - Automatic data deletion

### Individual Rights
1. **Right to Access**
   - Data export functionality
   - 30-day response time
   - Self-service portal

2. **Right to Rectification**
   - User profile editing
   - Admin correction tools
   - Audit trail of changes

3. **Right to Erasure**
   - Complete deletion workflow
   - Backup handling procedures
   - Confirmation mechanisms

4. **Right to Data Portability**
   - JSON/CSV export formats
   - API access for data retrieval
   - Documented data schemas

### Technical Measures
1. **Privacy by Design**
   - Data protection impact assessments
   - Privacy-first architecture
   - Regular privacy reviews

2. **Security Measures**
   - Encryption standards
   - Access controls
   - Regular security testing
   - Incident response procedures""")
                
                elif compliance == 'sox':
                    sections.append("""## SOX Compliance

### Overview
This application maintains Sarbanes-Oxley (SOX) compliance for financial reporting integrity.

### IT General Controls
1. **Access Controls**
   - Role-based permissions
   - Segregation of duties
   - Quarterly access reviews
   - Privileged access management

2. **Change Management**
   - Formal change process
   - Approval workflows
   - Testing requirements
   - Rollback procedures

3. **Operations**
   - Job scheduling controls
   - Backup procedures
   - Monitoring and alerts
   - Incident management

### Application Controls
1. **Input Controls**
   - Data validation rules
   - Duplicate detection
   - Error handling procedures
   - Reconciliation processes

2. **Processing Controls**
   - Calculation accuracy checks
   - Data integrity validation
   - Exception reporting
   - Audit trails

3. **Output Controls**
   - Report access controls
   - Distribution logs
   - Data classification
   - Retention policies

### Documentation
1. **Process Documentation**
   - Detailed procedures
   - Control matrices
   - Risk assessments
   - Test evidence

2. **Audit Support**
   - Control testing
   - Evidence collection
   - Management assertions
   - Remediation tracking""")
                
                elif compliance == 'pci':
                    sections.append("""## PCI DSS Compliance

### Overview
This application complies with Payment Card Industry Data Security Standards (PCI DSS) Level 1.

### Network Security
1. **Segmentation**
   - Cardholder data environment (CDE) isolated
   - Network segmentation validated
   - Regular penetration testing
   - Firewall rule reviews

2. **Access Control**
   - Two-factor authentication
   - Unique user IDs
   - Quarterly access reviews
   - Visitor logs maintained

### Data Protection
1. **Encryption**
   - AES-256 for data at rest
   - TLS 1.2+ for transmission
   - Key rotation procedures
   - Hardware security modules (HSM)

2. **Data Retention**
   - Minimal retention periods
   - Secure deletion procedures
   - No storage of sensitive authentication data
   - Tokenization implemented

### Vulnerability Management
1. **Patching**
   - Monthly security updates
   - Critical patches within 24 hours
   - Patch testing procedures
   - Rollback capabilities

2. **Scanning**
   - Quarterly vulnerability scans
   - Annual penetration tests
   - Code security reviews
   - Web application firewall (WAF)

### Monitoring
1. **Logging**
   - Centralized log management
   - 1-year retention minimum
   - Daily log reviews
   - Automated alerts

2. **File Integrity**
   - FIM tools deployed
   - Critical file monitoring
   - Change detection alerts
   - Regular baseline updates""")
        
        return f"""# Compliance Documentation

## Overview
This document outlines the compliance measures implemented in {self.args.name}.

## Compliance Standards
{', '.join([c.upper() for c in self.args.compliance.split(',')]) if self.args.compliance else 'No specific compliance requirements'}

{''.join(sections)}

## Compliance Checklist

### Development Phase
- [ ] Security requirements defined
- [ ] Compliance controls identified
- [ ] Risk assessment completed
- [ ] Privacy impact assessment (if applicable)

### Implementation Phase
- [ ] Security controls implemented
- [ ] Audit logging configured
- [ ] Access controls established
- [ ] Encryption enabled

### Testing Phase
- [ ] Security testing completed
- [ ] Penetration testing performed
- [ ] Compliance validation done
- [ ] Audit trail verified

### Deployment Phase
- [ ] Production security hardening
- [ ] Monitoring configured
- [ ] Incident response tested
- [ ] Documentation updated

### Operational Phase
- [ ] Regular security scans
- [ ] Access reviews conducted
- [ ] Audit logs reviewed
- [ ] Compliance reports generated

## Audit Requirements

### Internal Audits
- Frequency: Quarterly
- Scope: All compliance controls
- Documentation: Audit reports and remediation plans

### External Audits
- Frequency: Annually
- Scope: Full compliance assessment
- Certifications: Maintain current certifications

## Training Requirements

### Developer Training
- Security best practices
- Compliance requirements
- Secure coding standards
- Incident response procedures

### Operations Training
- Security operations
- Monitoring and alerting
- Incident handling
- Compliance reporting

## Incident Response

### Response Team
- Security Lead
- Development Lead
- Operations Lead
- Legal/Compliance

### Response Procedures
1. Detect and analyze
2. Contain and eradicate
3. Recover and restore
4. Post-incident review

### Notification Requirements
- Internal: Within 1 hour
- Customers: Per contractual requirements
- Regulators: Per compliance requirements

## Contact Information

### Compliance Officer
- Name: [Compliance Officer Name]
- Email: compliance@company.com
- Phone: +1-xxx-xxx-xxxx

### Security Team
- Email: security@company.com
- 24/7 Hotline: +1-xxx-xxx-xxxx

### Legal Team
- Email: legal@company.com
- Phone: +1-xxx-xxx-xxxx
"""

    def _generate_base_ci_overlays(self, comps: List[str]) -> str:
        jobs: List[str] = []
        if 'pci' in comps:
            jobs.append(
                """
  pci-min-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: PCI minimal check (dependency vulns)
        run: |
          if [ -f package.json ]; then npm audit --audit-level=high; else echo "no node"; fi
          if [ -f requirements.txt ]; then python -m pip install --upgrade pip pip-audit && pip-audit -r requirements.txt || true; fi
                """.rstrip()
            )
        if 'sox' in comps:
            jobs.append(
                """
  sox-min-audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: SOX minimal audit trail check (git metadata)
        run: |
          git log -1 --pretty=fuller | cat
                """.rstrip()
            )
        body = "\n\n".join(jobs) if jobs else ""
        return f"""name: Compliance Overlays\n\non:\n  pull_request:\n    branches: [ main, develop, integration ]\n  push:\n    branches: [ main, develop, integration ]\n\njobs:{body}\n"""
