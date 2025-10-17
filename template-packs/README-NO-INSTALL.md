# Templates: Do NOT install dependencies here

This `template-packs/` directory contains source templates only.

Important rules:

- Do NOT run `npm install`, `npm update`, `pnpm`, or `yarn` in any folder under `template-packs/`.
- Do NOT commit `node_modules/` or any lockfiles (package-lock.json, pnpm-lock.yaml, yarn.lock) in templates.
- Install dependencies only in generated projects (e.g. `_generated/<project>/frontend/` or `/backend/`).
- Use lockfile installs for reliability and speed in generated projects:
  - `npm ci --no-audit --no-fund`
- If `node_modules/` appears inside `template-packs/`, delete it immediately. Templates must remain code-only.

Rationale:

- Installing inside templates can explode `node_modules/` size (tens of GB) and create deep nested paths that break tooling (e.g., `E2BIG`).
- Keeping templates clean ensures fast project generation and minimal repository size.
