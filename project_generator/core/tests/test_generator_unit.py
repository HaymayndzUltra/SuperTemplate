import types
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator
from project_generator.core.industry_config import IndustryConfig


def _mk_args():
    class A: pass
    a = A()
    a.name = 'unit-proj'
    a.industry = 'healthcare'
    a.project_type = 'api'
    a.frontend = 'none'
    a.backend = 'fastapi'
    a.database = 'postgres'
    a.auth = 'auth0'
    a.deploy = 'self-hosted'
    a.compliance = ''
    a.features = ''
    a.output_dir = '/tmp'
    a.no_git = True
    a.no_install = True
    a.workers = 0
    a.rules_manifest = None
    a.no_cursor_assets = True
    a.minimal_cursor = False
    return a


def test_generator_initializes_with_industry_config():
    args = _mk_args()
    gen = ProjectGenerator(args, ProjectValidator(), IndustryConfig(args.industry))
    # ensure config exposes merge_features
    features = gen.config.merge_features('a,b')
    assert isinstance(features, list)


def test_generate_cicd_includes_gates_config(tmp_path):
    args = _mk_args()
    args.output_dir = str(tmp_path)
    gen = ProjectGenerator(args, ProjectValidator(), IndustryConfig(args.industry))
    # create minimal structure and call _generate_cicd_workflows
    gen.project_root = tmp_path / args.name
    gen.project_root.mkdir(parents=True, exist_ok=True)
    (gen.project_root / '.github' / 'workflows').mkdir(parents=True, exist_ok=True)
    gen._generate_cicd_workflows()
    assert (gen.project_root / 'gates_config.yaml').exists()


def test_create_base_structure_writes_cursor_index(tmp_path):
    args = _mk_args()
    args.output_dir = str(tmp_path)
    args.no_cursor_assets = False
    gen = ProjectGenerator(args, ProjectValidator(), IndustryConfig(args.industry))
    gen.project_root = tmp_path / args.name
    gen.project_root.mkdir(parents=True, exist_ok=True)

    gen._create_base_structure()

    index_path = gen.project_root / '.cursor' / 'index.mdc'
    assert index_path.exists()

    content = index_path.read_text()
    assert 'description: "unit-proj api project for the healthcare industry' in content
    assert '- **Project Type:** api' in content
    assert 'alwaysApply: true' in content
    assert '## Project Rules' in content
