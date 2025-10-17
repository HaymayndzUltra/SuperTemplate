# Project Generator

Ang folder na ito ay ang Python package na nagbibigay ng end-to-end na "project scaffolding" engine para sa AI Governor ecosystem. Pinagsasama nito ang template discovery, industry presets, at validation upang makagawa ng opinionated na codebases.

## Estruktura ng Direktoryo

| Path | Layunin |
| --- | --- |
| `core/` | Pangunahing domain logic tulad ng [`generator.py`](core/generator.py) para sa end-to-end project build at [`validator.py`](core/validator.py) para sa compatibility at compliance checks. |
| `core/brief_parser.py` | Utilities para basahin at i-normalize ang project brief input bago ito ipadala sa generator. |
| `core/industry_config.py` | Mga industry playbook (healthcare, fintech, atbp.) na nagma-map ng features at regolasyon. |
| `integrations/` | Mga helper para sa optional automation tulad ng [`ai_governor.py`](integrations/ai_governor.py) at [`git.py`](integrations/git.py). |
| `templates/` | Template engine at registry na naglilista ng assets mula sa `../template-packs`. Tingnan ang [`template_engine.py`](templates/template_engine.py) at [`registry.py`](templates/registry.py). |
| `template-packs/` | Shortcut patungo sa shared template library (tingnan din ang hiwalay na dokumentasyon sa `../../template-packs`). |
| `tests/` | Pytest-based regression suite gaya ng [`tests/test_validation.py`](tests/test_validation.py). |
| `__init__.py` | Package metadata (`__version__` at author). |

## Daloy ng Pagbuo

1. **Input parsing** – Tinatrabaho ng `brief_parser` ang raw brief o CLI args upang makuha ang project name, industriya, at stack choices.
2. **Industry configuration** – Gumagamit ng `IndustryConfig` upang i-merge ang default gates, compliance, at feature toggles para sa piniling industriya.
3. **Validation** – Ang `ProjectValidator` ay:
   - bumabasa ng compatibility matrix para sa frontend/backend/database/auth combos;
   - nag-e-enforce ng project-type requirements (hal. kailangan ng `frontend` + `backend` para sa `fullstack`);
   - nagva-validate ng compliance packs (HIPAA, SOC2, PCI, atbp.) at mga feature guardrail.
4. **Template discovery** – `TemplateRegistry` ang nag-i-scan ng `template-packs/*` para sa `template.manifest.json` at nagbabalik ng variant metadata.
5. **Generation** – `ProjectGenerator.generate()` ang naghahawak ng file system operations: gumagawa ng directory tree, humihingi ng frontend/backend/database templates mula sa `TemplateEngine`, kumokopya ng DevEx assets, CI/CD workflows, rules, at AI Governor tooling.
6. **Post-processing** – Opsyonal na nag-i-initialize ng Git repo, nag-i-install ng pre-commit hooks, at nagpi-print ng setup commands/next steps.

## Pag-gamit

```python
from argparse import Namespace
from project_generator.core.generator import ProjectGenerator
from project_generator.core.validator import ProjectValidator

args = Namespace(
    name="demo-app",
    industry="healthcare",
    project_type="fullstack",
    frontend="nextjs",
    backend="fastapi",
    database="postgres",
    auth="auth0",
    deploy="aws",
    compliance="hipaa",
    features="realtime,analytics",
    output_dir="./out",
    no_git=True,
    no_install=True,
)

validator = ProjectValidator()
report = validator.validate_comprehensive(args)
if not report["valid"]:
    raise SystemExit(report["errors"])

generator = ProjectGenerator(args=args, validator=validator)
result = generator.generate()
print(result["project_path"])
```

### Week 7 Documentation
- Consult the [Unified CLI Reference](../docs/operations/cli-reference.md) for the command routing table and telemetry expectations when invoking the generator via `python -m unified_workflow.cli generate-project`.
- Follow the [Migration Guide](../docs/operations/migration-guide.md) when replacing legacy generator scripts in downstream projects.
- Use the [Example Projects Catalog](../docs/operations/example-projects.md) to demonstrate generator capabilities during operator training.

### Mga Mahalagang Flag
- `no_cursor_assets` – i-exclude ang `.cursor` automation pack kung kailangan ng minimal output.
- `minimal_cursor` + `rules_manifest` – pumipili lamang ng enumerated policy files mula sa shared rules directory.
- `workers` – thread pool size para sa parallel template copy (default: `max(2, cpu_count*2)`).

## Pagsusulit

Patakbuhin ang unit tests gamit ang Pytest:

```bash
pytest secretflow/project_generator/tests
```

Ginama gamit ng tests ang `unittest.mock` para i-simulate ang external CLI checks (Node, Python, atbp.) upang manatiling deterministic.

## Pagdaragdag ng Template o Integrasyon

1. Maglagay ng bagong template sa `template-packs/<domain>/<name>` at magdagdag ng `template.manifest.json` upang ma-detect ng registry.
2. Kung may bagong industry rule set, i-extend ang `IndustryConfig` upang i-map ang defaults at gates.
3. Para sa automation (hal. evidence logging o git bootstrapping), idagdag ang helper sa `integrations/` at tawagin mula sa `ProjectGenerator` kung kinakailangan.

## Dependencies
- Python 3.10+
- Standard library lamang sa core modules; external CLIs (Node.js, Git, Docker) ay hina-handle bilang runtime prerequisites at naka-check sa `ProjectValidator`.

---

## Evidence: Registry, Generator, and Validator Hooks

### TemplateRegistry facade → Unified registry
```21:31:/home/haymayndz/ai-driven-template/project_generator/templates/registry.py
class TemplateRegistry:
    """Legacy template registry facade.
    ...
    def __init__(self, root: Optional[Path] = None):
        ...
        self._registry = UnifiedTemplateRegistry(root_path=root)
        self._registry.initialize()
```

### Generator uses TemplateEngine + TemplateRegistry
```16:23:/home/haymayndz/ai-driven-template/project_generator/core/generator.py
from ..templates.template_engine import TemplateEngine
from ..templates.registry import TemplateRegistry
...
class ProjectGenerator:
```

```67:75:/home/haymayndz/ai-driven-template/project_generator/core/generator.py
self.template_engine = TemplateEngine()
...
self.template_registry = TemplateRegistry()
```

### Validator comprehensive checks
```199:233:/home/haymayndz/ai-driven-template/project_generator/core/validator.py
def validate_comprehensive(self, args) -> Dict[str, Any]:
    # 1. Tech-stack compatibility checks
    config_result = self.validate_configuration(args)
    ...
    # 4. System dependency checks
```
