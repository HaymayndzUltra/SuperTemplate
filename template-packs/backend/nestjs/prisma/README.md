# NestJS Prisma Variant

This is a Prisma-based variant of the NestJS backend template.

- ORM: Prisma (`@prisma/client`)
- Schema: `prisma/schema.prisma`
- Global `PrismaService` provided via `PrismaModule`

## Selecting this variant via the generator

Use the CLI flag when generating a project:

```bash
python3 scripts/generate_client_project.py \
  --name my-app \
  --industry saas \
  --project-type api \
  --backend nestjs \
  --nestjs-orm prisma \
  --yes
```

## Quick start

```bash
npm install
npm run prisma:generate
npm run start:dev
```

Ensure your `.env` has a valid `DATABASE_URL`.
