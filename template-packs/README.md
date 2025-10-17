# Template Packs

Ang direktoryong ito ang canonical source ng scaffolding assets na binabasa ng `project_generator.templates.TemplateRegistry`. Nakaayos ang mga pack ayon sa domain (frontend, backend, database, devex, CI/CD, policy) at bawat isa ay maaaring maglaman ng `template.manifest.json` para i-advertise ang mga variant at engine support.

## High-level Overview

| Sub-folder | Nilalaman | Halagang Punto |
| --- | --- | --- |
| `backend/` | Opinionated server templates para sa Django, FastAPI, NestJS, Go, at fallback na `none/`. | Bawat framework ay may `base/` skeleton (Dockerfile, dependencies, README) at manifest para sa variant metadata. |
| `frontend/` | SPA at mobile shells (Next.js, Nuxt, Angular, Expo). | Mga page/component scaffolds na ginagamit ng `TemplateEngine.generate_page_template`. |
| `database/` | Infra bootstrap para sa Postgres, MongoDB, Firebase, o placeholder `none`. | Kadalasang may docker compose snippets at seed scripts. |
| `devex/` | Developer experience kit: `devcontainer` setup, docker-compose, VS Code snippets, Makefile. | Pwedeng i-symlink sa generated project root para sa consistent tooling. |
| `cicd/` | GitHub workflow recipes (`ci-test.yml`, `ci-lint.yml`, `ci-security.yml`, `ci-deploy.yml`) at shared `gates_config.yaml`. | Hinahalo sa `.github/workflows` ng bagong proyekto. |
| `policy-dsl/` | YAML definitions gaya ng `client-generator-policies.yaml` na ginagamit ng policy engine. | Kapaki-pakinabang kapag nagpapatupad ng gating rules kasama ang `.cursor` assets. |
| `README-NO-INSTALL.md` | Quick note kung paano kopyahin ang DevEx tooling nang hindi nag-i-install ng buong template pack. | Reference lamang; hindi binabasa ng generator. |

## Pagdaragdag ng Bagong Pack

1. Gumawa ng folder sa ilalim ng naaangkop na domain (`frontend/<tech>`, `backend/<framework>`, atbp.).
2. Maglagay ng `template.manifest.json` para ilarawan ang pangalan, variants, at optional na template engines:
   ```json
   {
     "name": "FastAPI Starter",
     "variants": ["base"],
     "engines": ["jinja2"]
   }
   ```
3. Ilagay ang aktuwal na assets sa loob ng mga variant subdirectories (hal. `base/`). Kapag walang manifest, susubukan ng registry na hulaan ang variants base sa mga subfolder.
4. Kapag may DevEx o CI asset na gumagamit ng variable placeholders, tiyaking tugma ang syntax sa `TemplateEngine` (kasalukuyang naka-hardcode para sa Next.js, Nuxt, Angular, Expo, FastAPI, Django, NestJS, Go).

## Konsumo ng Generator

- **Discovery** – Tinutukoy ng `TemplateRegistry.list_all()` ang path ng pack at ibinabalik ang metadata sa generator.
- **Copying** – Si `ProjectGenerator._generate_frontend/_generate_backend/_setup_database` ang kumokopya ng mga file mula sa tinukoy na variant papunta sa output project.
- **Compliance & Policy** – Ang `policy-dsl` ay kasamang kino-copy kapag hindi naka-enable ang `--no-cursor-assets`. Maaari ding gumamit ng `--rules-manifest` upang pumili ng eksaktong policy files.

## Customization Tips

- Huwag maglagay ng binary o build artifacts sa loob ng packs; inaasahan ng generator na idempotent ang copy operations.
- Maaari kang magdagdag ng mga `.jinja` o iba pang templated files, ngunit kailangan mo ring i-extend ang `TemplateEngine` kung may bagong syntax.
- Kapag nagbago ang folder structure, i-update ang anumang automation scripts na umaasa sa relative paths (hal. smoke tests o DevEx scripts).

### Week 7 Notes
- Suriin ang [Migration Guide](../docs/operations/migration-guide.md) bago alisin o palitan ang legacy packs upang matiyak ang backward compatibility.
- I-refer ang [Example Projects Catalog](../docs/operations/example-projects.md) kapag nagpapakita kung paano ginagamit ng generator ang mga pack na ito sa training sessions.
- Kapag may deployment-specific asset, i-align sa [Deployment Runbook](../docs/operations/deployment-runbook.md) para maiwasan ang drift sa production procedures.

---

## Integration with Unified Template Registry (Evidence-Based)

Ang `TemplateRegistry` na ginagamit ng project generator ay facade lamang papunta sa unified registry:

```15:21:/home/haymayndz/ai-driven-template/project_generator/templates/registry.py
from unified_workflow.core.template_registry import (
    TemplateMetadata,
    UnifiedTemplateRegistry,
)
```

Ang facade ay nag-i-initialize at nagpo-proxy ng mga call sa unified registry:

```39:50:/home/haymayndz/ai-driven-template/project_generator/templates/registry.py
self._registry = UnifiedTemplateRegistry(root_path=root)
self._registry.initialize()
...
return [self._to_legacy_dict(template) for template in templates]
```

Ang unified registry ang tunay na nagdi-discover ng packs sa `template-packs/` at ibang legacy paths:

```80:85:/home/haymayndz/ai-driven-template/unified_workflow/core/template_registry.py
self.search_paths = [
    self.root / "template-packs",
    self.root / "project_generator" / "template-packs",
    self.root / "unified_workflow" / "templates",
]
```

At nire-register nito ang bawat template, variants, at manifest:

```228:240:/home/haymayndz/ai-driven-template/unified_workflow/core/template_registry.py
metadata = TemplateMetadata(
    name=manifest_data.get("name", template_path.name),
    type=template_type,
    path=template_path,
    variants=manifest_data.get("variants", variants),
    engines=manifest_data.get("engines"),
    ...
)
```

### Practical Usage

- Ilista ang lahat ng templates para sa audit o tooling:
```bash
python -c "from project_generator.templates.registry import TemplateRegistry; print(TemplateRegistry().list_all())"
```
- Kunin ang path ng isang variant:
```bash
python -c "from project_generator.templates.registry import TemplateRegistry; print(TemplateRegistry().get_template_path('backend','fastapi','base'))"
```
