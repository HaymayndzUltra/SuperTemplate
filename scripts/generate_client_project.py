#!/usr/bin/env python3
"""
Client Project Generator - Main CLI Script
Generates industry-specific, compliance-ready client projects
"""

import argparse
import sys
import os
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import subprocess

# Import via proper package path (scripts should be run from repo root)
# If running from elsewhere, use: python -m scripts.generate_client_project
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator
from project_generator.core.industry_config import IndustryConfig
from project_generator.templates.registry import TemplateRegistry


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Generate industry-specific client projects with compliance support',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Healthcare web application
  %(prog)s --name acme-health --industry healthcare --project-type web \\
           --frontend nextjs --backend fastapi --database postgres \\
           --auth auth0 --deploy aws --compliance hipaa

  # Financial API service
  %(prog)s --name fintech-api --industry finance --project-type api \\
           --backend go --database postgres --auth cognito \\
           --deploy azure --compliance sox,pci

  # E-commerce mobile app
  %(prog)s --name shop-mobile --industry ecommerce --project-type mobile \\
           --frontend expo --backend django --database mongodb \\
           --auth firebase --deploy gcp
        """
    )
    
    # Required arguments
    parser.add_argument('--name', required=True,
                        help='Client/project name (e.g., acme-health)')
    
    parser.add_argument('--industry', required=True,
                        choices=['healthcare', 'finance', 'ecommerce', 'saas', 'enterprise'],
                        help='Industry vertical')
    
    parser.add_argument('--project-type', required=True,
                        choices=['web', 'mobile', 'api', 'fullstack', 'microservices'],
                        help='Type of project')
    
    # Technology stack arguments
    parser.add_argument('--frontend',
                        choices=['nextjs', 'nuxt', 'angular', 'expo', 'none'],
                        default='none',
                        help='Frontend framework')
    
    parser.add_argument('--backend',
                        choices=['fastapi', 'django', 'nestjs', 'go', 'none'],
                        default='none',
                        help='Backend framework')
    
    # NestJS ORM selection (parallel templates: typeorm (default) or prisma)
    parser.add_argument('--nestjs-orm',
                        choices=['typeorm', 'prisma'],
                        default='typeorm',
                        help='Select ORM for NestJS backend (typeorm | prisma)')
    
    parser.add_argument('--database',
                        choices=['postgres', 'mongodb', 'firebase', 'none'],
                        default='none',
                        help='Database technology')
    
    parser.add_argument('--auth',
                        choices=['auth0', 'firebase', 'cognito', 'custom', 'none'],
                        default='none',
                        help='Authentication provider')
    
    parser.add_argument('--deploy',
                        choices=['aws', 'azure', 'gcp', 'vercel', 'self-hosted'],
                        default='aws',
                        help='Deployment target')
    
    # Optional arguments
    parser.add_argument('--features',
                        help='Comma-separated list of additional features')
    
    parser.add_argument('--compliance',
                        help='Comma-separated compliance requirements (hipaa,gdpr,sox,pci)')
    
    parser.add_argument('--output-dir', '-o',
                        default='.',
                        help='Output directory for generated project (default: current directory)')
    
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be generated without creating files')
    
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Run in interactive mode for missing options')
    
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose output')
    
    parser.add_argument('--no-git', action='store_true',
                        help='Skip git repository initialization')
    
    parser.add_argument('--no-install', action='store_true',
                        help='Skip dependency installation')

    parser.add_argument('--force', action='store_true',
                        help='Overwrite existing target directory if it exists (idempotent)')

    parser.add_argument('--config-out',
                        help='Path to write resolved generator config as JSON (default: ./generator-config.json)')

    parser.add_argument('--yes', action='store_true',
                        help='Proceed without interactive confirmation (non-interactive mode)')

    # Generator isolation: explicit opt-in to include .cursor assets even when a root .cursor exists
    parser.add_argument('--include-cursor-assets', '--ai-governor', dest='include_cursor_assets',
                        action='store_true',
                        help='Include .cursor assets (rules, tools) in the generated project even if a root .cursor exists')

    # Generator isolation: avoid emitting .cursor assets when running inside repos with root .cursor
    parser.add_argument('--no-cursor-assets', action='store_true',
                        help='Do not emit .cursor assets (rules, tools) into the generated project')
    
    # Include only specific project rules for the chosen stack (frontend/backend minimal set)
    parser.add_argument('--include-project-rules', action='store_true',
                        help='Include a minimal set of project rules for the chosen stack (e.g., nextjs/typescript, fastapi/python). If needed, this will implicitly enable --include-cursor-assets.')

    # Rules mode: control automatic inclusion of stack-specific rules
    parser.add_argument('--rules-mode', choices=['auto', 'minimal', 'none'], default='auto',
                        help='Rule inclusion mode: auto/minimal includes stack-specific rules by default; none skips project rules entirely.')
    
    # Explicit rules manifest: json array of filenames to copy from root .cursor/rules/project-rules into generated project
    parser.add_argument('--rules-manifest', dest='rules_manifest',
                        help='Path to JSON file listing project rule filenames to include (overrides --include-project-rules and --rules-mode).')
    
    # Minimal cursor assets: only write .cursor/project.json and .cursor/rules specified by manifest; skip ai-driven-workflow/tools
    parser.add_argument('--minimal-cursor', dest='minimal_cursor', action='store_true',
                        help='Emit only minimal .cursor assets (project.json and selected rules). Skips ai-driven-workflow and tools.')
    
    # Performance tuning
    parser.add_argument('--workers', type=int, default=0,
                        help='Number of worker threads for template processing (0=auto)')

    # System checks relaxation for CI/local environments
    parser.add_argument('--skip-system-checks', action='store_true',
                        help='Allow generation even if system deps (e.g., Docker) are not available')
    
    # In-place generation: bypass default redirect to ../_generated when a root .cursor exists
    parser.add_argument('--in-place', action='store_true',
                        help='Bypass output redirection and generate into --output-dir as-is (even if a root .cursor/ exists)')

    # No subdirectory: write directly into --output-dir instead of creating a project-name folder
    parser.add_argument('--no-subdir', action='store_true',
                        help='Place scaffold files directly under --output-dir (do not create <name>/ subfolder)')
    
    # Discovery / tooling
    parser.add_argument('--list-templates', action='store_true',
                        help='List available templates and exit')
    
    # Project categorization
    parser.add_argument('--category', choices=['test', 'example', 'demo', 'archived'], 
                        default='example',
                        help='Category for the generated project (test/example/demo/archived)')
    
    return parser.parse_args()


def interactive_mode(args):
    """Fill in missing arguments through interactive prompts"""
    print("\n🚀 Client Project Generator - Interactive Mode\n")
    
    # Helper function for choice prompts
    def prompt_choice(field, prompt, choices, current_value=None):
        if current_value and current_value != 'none':
            return current_value
            
        print(f"\n{prompt}")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice}")
        
        while True:
            try:
                selection = input(f"Select (1-{len(choices)}): ").strip()
                if selection.isdigit():
                    idx = int(selection) - 1
                    if 0 <= idx < len(choices):
                        return choices[idx]
                print("Invalid selection. Please try again.")
            except KeyboardInterrupt:
                print("\n\nOperation cancelled.")
                sys.exit(1)
    
    # Fill in missing technology choices based on project type
    if args.project_type in ['web', 'fullstack'] and args.frontend == 'none':
        args.frontend = prompt_choice(
            'frontend',
            "Select frontend framework:",
            ['nextjs', 'nuxt', 'angular', 'none'],
            args.frontend
        )
    
    if args.project_type in ['api', 'fullstack', 'microservices'] and args.backend == 'none':
        args.backend = prompt_choice(
            'backend',
            "Select backend framework:",
            ['fastapi', 'django', 'nestjs', 'go', 'none'],
            args.backend
        )
    
    if args.project_type == 'mobile' and args.frontend == 'none':
        args.frontend = 'expo'
        print(f"✓ Auto-selected frontend: {args.frontend}")
    
    # Database selection
    if args.backend != 'none' and args.database == 'none':
        args.database = prompt_choice(
            'database',
            "Select database:",
            ['postgres', 'mongodb', 'firebase', 'none'],
            args.database
        )
    
    # Auth selection based on industry
    if args.auth == 'none':
        auth_choices = ['auth0', 'firebase', 'cognito', 'custom', 'none']
        if args.industry == 'healthcare':
            print("\n⚕️ Healthcare detected - recommending Auth0 for HIPAA compliance")
            auth_choices.insert(0, auth_choices.pop(auth_choices.index('auth0')))
        elif args.industry == 'finance':
            print("\n💰 Finance detected - recommending Cognito for enterprise features")
            auth_choices.insert(0, auth_choices.pop(auth_choices.index('cognito')))
        
        args.auth = prompt_choice(
            'auth',
            "Select authentication provider:",
            auth_choices,
            args.auth
        )
    
    # Compliance requirements
    if not args.compliance:
        compliance_map = {
            'healthcare': ['hipaa', 'none'],
            'finance': ['sox', 'pci', 'none'],
            'ecommerce': ['pci', 'gdpr', 'none'],
            'saas': ['gdpr', 'soc2', 'none'],
            'enterprise': ['soc2', 'none']
        }
        
        available_compliance = compliance_map.get(args.industry, ['none'])
        if len(available_compliance) > 1:
            print(f"\n📋 Select compliance requirements for {args.industry}:")
            selected = []
            for comp in available_compliance[:-1]:  # Exclude 'none'
                response = input(f"  Include {comp.upper()}? (y/n): ").strip().lower()
                if response == 'y':
                    selected.append(comp)
            
            args.compliance = ','.join(selected) if selected else None
    
    # Features
    if not args.features:
        print("\n✨ Additional features (comma-separated, or press Enter to skip):")
        feature_suggestions = {
            'healthcare': "telehealth,patient-portal,ehr-integration",
            'finance': "reporting,analytics,trading",
            'ecommerce': "inventory,shipping,reviews",
            'saas': "billing,subscriptions,admin-panel",
            'enterprise': "sso,audit-logs,api-gateway"
        }
        
        print(f"  Suggestions: {feature_suggestions.get(args.industry, 'none')}")
        features_input = input("  Features: ").strip()
        if features_input:
            args.features = features_input
    
    # Persist resolved configuration for reproducibility
    try:
        config_path = args.config_out or os.path.join(os.getcwd(), 'generator-config.json')
        resolved = {
            'name': args.name,
            'industry': args.industry,
            'project_type': args.project_type,
            'frontend': args.frontend,
            'backend': args.backend,
            'database': args.database,
            'auth': args.auth,
            'deploy': args.deploy,
            'features': args.features,
            'compliance': args.compliance,
        }
        with open(config_path, 'w') as f:
            json.dump(resolved, f, indent=2, sort_keys=True)
        print(f"\n💾 Saved generator config to: {config_path}")
    except Exception as e:
        print(f"⚠️  Could not write generator config: {e}")

    return args


def check_dependencies(args) -> Dict[str, List[str]]:
    """Check required CLI dependencies are available. Returns {'missing': [...], 'warnings': [...]}"""
    from shutil import which

    missing: List[str] = []
    warnings: List[str] = []

    # Always required
    if which('docker') is None:
        missing.append('docker')

    # Frontend dependencies
    if args.frontend != 'none' or args.backend == 'nestjs':
        if which('node') is None:
            missing.append('node')
        if which('npm') is None:
            missing.append('npm')

    # Python backends
    if args.backend in ['fastapi', 'django']:
        if which('python3') is None and which('python') is None:
            missing.append('python3')
        else:
            # Optional but recommended
            if which('pip') is None and which('pip3') is None:
                warnings.append('pip/pip3 not found; ensure virtualenv can install requirements')

    # Go backend
    if args.backend == 'go' and which('go') is None:
        missing.append('go')

    return {'missing': missing, 'warnings': warnings}


def display_project_summary(args, generator):
    """Display a summary of what will be generated"""
    print("\n📊 Project Generation Summary")
    print("=" * 50)
    print(f"Project Name:     {args.name}")
    print(f"Industry:         {args.industry.upper()}")
    print(f"Project Type:     {args.project_type}")
    print(f"Frontend:         {args.frontend if args.frontend != 'none' else 'N/A'}")
    print(f"Backend:          {args.backend if args.backend != 'none' else 'N/A'}")
    print(f"Database:         {args.database if args.database != 'none' else 'N/A'}")
    print(f"Authentication:   {args.auth if args.auth != 'none' else 'N/A'}")
    print(f"Deployment:       {args.deploy}")
    print(f"Compliance:       {args.compliance.upper() if args.compliance else 'None'}")
    print(f"Features:         {args.features if args.features else 'None'}")
    print(f"Output Directory: {os.path.abspath(args.output_dir)}")
    print("=" * 50)


def main():
    """Main entry point"""
    args = parse_arguments()
    
    # List templates and exit
    if getattr(args, 'list_templates', False):
        reg = TemplateRegistry()
        entries = reg.list_all()
        print("\nAvailable templates:\n")
        for e in entries:
            print(f"- {e['type']}: {e['name']} (variants: {', '.join(e.get('variants') or ['base'])})")
        return
    
    # Safe defaults when a root .cursor/ exists in the current repo:
    # - Default output_dir to ../_generated (sibling outside repo) if user did not change from '.'
    # - Default to --no-cursor-assets to prevent nested rulesets unless --include-cursor-assets is set
    try:
        repo_root = os.getcwd()
        has_root_cursor = os.path.isdir(os.path.join(repo_root, '.cursor'))
        include_assets = bool(getattr(args, 'include_cursor_assets', False))
        if has_root_cursor and not getattr(args, 'in_place', False):
            if getattr(args, 'output_dir', '.') == '.':
                # Use sibling _generated directory one level outside the repo root
                default_out = os.path.abspath(os.path.join(repo_root, '..', '_generated'))
                os.makedirs(default_out, exist_ok=True)
                args.output_dir = default_out
                if getattr(args, 'verbose', False):
                    print(f"ℹ️  Detected root .cursor/. Defaulting output_dir to: {args.output_dir}")
            # Isolation defaults unless explicitly overridden
            if include_assets:
                args.no_cursor_assets = False
                if getattr(args, 'verbose', False):
                    print("ℹ️  --include-cursor-assets enabled. Emitting .cursor assets in generated project.")
            else:
                args.no_cursor_assets = True
                if getattr(args, 'verbose', False):
                    print("ℹ️  Detected root .cursor/. Enabling --no-cursor-assets by default.")
            # If user asked to include specific project rules, ensure cursor assets are included
            if getattr(args, 'include_project_rules', False) and getattr(args, 'no_cursor_assets', True):
                args.no_cursor_assets = False
                if not include_assets and getattr(args, 'verbose', False):
                    print("ℹ️  --include-project-rules requested. Implicitly enabling emission of .cursor assets.")
        else:
            # In-place defaults: if neither include nor no-cursor flag provided, avoid emitting cursor assets
            if not getattr(args, 'include_cursor_assets', False) and not getattr(args, 'no_cursor_assets', False):
                args.no_cursor_assets = True
        
        # Automatic project rules selection when requested by mode (auto/minimal)
        mode = getattr(args, 'rules_mode', 'auto')
        if mode in ('auto', 'minimal') and not getattr(args, 'include_project_rules', False):
            # If either frontend or backend is selected, include minimal project rules
            if (getattr(args, 'frontend', 'none') != 'none') or (getattr(args, 'backend', 'none') != 'none'):
                args.include_project_rules = True
                # Ensure .cursor assets are emitted if previously disabled due to isolation defaults
                if getattr(args, 'no_cursor_assets', False):
                    args.no_cursor_assets = False
                    if getattr(args, 'verbose', False):
                        print("ℹ️  rules-mode set to auto/minimal → enabling minimal stack-specific project rules and .cursor assets.")
    except Exception:
        pass
    
    # Apply category-based organization
    if hasattr(args, 'category') and args.category != 'example':
        category_dir = os.path.join(args.output_dir, f"{args.category}s")
        os.makedirs(category_dir, exist_ok=True)
        args.output_dir = category_dir
        if getattr(args, 'verbose', False):
            print(f"ℹ️  Using category directory: {args.output_dir}")
    
    # Run interactive mode if requested or if critical args are missing
    if args.interactive or (
        args.project_type in ['web', 'fullstack'] and args.frontend == 'none' and args.backend == 'none'
    ):
        args = interactive_mode(args)
    
    # Comprehensive validation (fail-fast with clear exit code 2)
    validator = ProjectValidator()
    validation = validator.validate_comprehensive(args)
    
    if validation['warnings']:
        print("\n⚠️  Configuration warnings:")
        for warning in validation['warnings']:
            print(f"  - {warning}")
    
    if not validation['valid']:
        print("\n❌ Configuration errors:")
        for error in validation['errors']:
            print(f"  - {error}")
        print("\nPlease fix configuration errors before proceeding.")
        sys.exit(2)

    print("\n🔍 Validating project configuration...")
    
    # Initialize components (validator already created above for comprehensive validation)
    config = IndustryConfig(args.industry)
    generator = ProjectGenerator(args, validator, config)
    
    # Display summary
    display_project_summary(args, generator)
    
    # Dry run mode
    if args.dry_run:
        print("\n🏃 DRY RUN MODE - No files will be created")
        structure = generator.get_project_structure()
        print("\n📁 Project Structure:")
        generator.display_structure(structure)
        return
    
    # Confirm generation unless --yes is provided
    if not args.yes:
        print("\n")
        response = input("Proceed with project generation? (y/n): ").strip().lower()
        if response != 'y':
            print("Generation cancelled.")
            return
    
    try:
        # Generate the project
        print("\n🔨 Generating project...")
        result = generator.generate()
        
        if result['success']:
            print("\n✅ Project generated successfully!")
            print(f"\n📁 Project location: {result['project_path']}")

            # If --no-subdir is requested and generator created a subdir, move contents up
            try:
                if getattr(args, 'no_subdir', False):
                    target_root = os.path.abspath(args.output_dir)
                    project_path = os.path.abspath(result.get('project_path') or target_root)
                    if project_path != target_root and os.path.isdir(project_path):
                        # Move all items (including hidden) from project_path to target_root
                        for entry in os.listdir(project_path):
                            src = os.path.join(project_path, entry)
                            dst = os.path.join(target_root, entry)
                            if os.path.exists(dst):
                                # Overwrite only if --force provided
                                if not getattr(args, 'force', False):
                                    continue
                                if os.path.isdir(dst) and not os.path.islink(dst):
                                    shutil.rmtree(dst)
                                else:
                                    try:
                                        os.remove(dst)
                                    except Exception:
                                        pass
                            shutil.move(src, dst)
                        # Remove now-empty project_path
                        try:
                            shutil.rmtree(project_path)
                        except Exception:
                            pass
                        # Update reported project_path
                        result['project_path'] = target_root
                        print(f"ℹ️  --no-subdir active. Moved scaffold into: {target_root}")
            except Exception as _e:
                if getattr(args, 'verbose', False):
                    print(f"⚠️  no-subdir move step encountered an issue: {_e}")
            
            # Display next steps
            print("\n📋 Next Steps:")
            for i, step in enumerate(result['next_steps'], 1):
                print(f"  {i}. {step}")
            
            # Offer to run setup commands
            if not args.no_install and result.get('setup_commands'):
                print("\n🚀 Run initial setup commands? (y/n): ", end='')
                if input().strip().lower() == 'y':
                    generator.run_setup_commands(result['project_path'], result['setup_commands'])
        else:
            print(f"\n❌ Generation failed: {result['error']}")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()