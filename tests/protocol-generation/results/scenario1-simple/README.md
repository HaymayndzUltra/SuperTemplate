# Project-Specific Protocols: Artisans Corner Dashboard

**Generated**: 2025-11-10T18:29:26.685195Z  
**Project**: artisans-corner-dashboard  
**Protocols**: 5

## Overview

This directory contains customized protocol instances generated specifically for the **artisans-corner-dashboard** project. These protocols are derived from foundation templates in `.cursor/ai-driven-workflow/` with project-specific customizations applied.

## Tech Stack

- **Frontend**: Next.js
- **Backend**: FastAPI
- **Database**: PostgreSQL

## Protocols Generated

- **Protocol 06**: `06-create-prd-artisans-corner-dashboard.md`
- **Protocol 07**: `07-technical-design-artisans-corner-dashboard.md`
- **Protocol 08**: `08-task-generation-artisans-corner-dashboard.md`
- **Protocol 09**: `09-environment-setup-artisans-corner-dashboard.md`
- **Protocol 10**: `10-execute-tasks-artisans-corner-dashboard.md`

## Usage

Execute protocols in the order specified in `PROTOCOL-EXECUTION-PLAN.md`. Each protocol file contains:
- Project-specific workflow steps
- Customized validation gates
- Tech stack-specific automation scripts
- Project-specific artifact paths

## Customizations Applied

Total customizations: 5

## Regeneration

To regenerate protocols (e.g., after foundation template updates):

```bash
python scripts/orchestration/regenerate_protocols.py \
  --project-root . \
  --force
```

## Maintenance

- **DO NOT** manually edit generated protocols (changes will be lost on regeneration)
- **DO** update foundation templates in `.cursor/ai-driven-workflow/` and regenerate
- **DO** update PROJECT-BRIEF.md if project requirements change, then regenerate

## Manifest

See `.protocol-manifest.json` for complete generation details and traceability.
