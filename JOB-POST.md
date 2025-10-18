JOB-POST.md — Senior Freelance Solutions Architect (AI-orchestrated workflow welcome)
Company

Heliox Care Systems — B2B HealthTech SaaS for mid-market clinics (15–150 providers). Multi-tenant web app + mobile companion.

Goal (Why we’re hiring)

We need a 6–8 week engagement to deliver a phase-1, production-ready MVP of a “Pre-Visit Intake & Eligibility” module while laying the foundation for long-term architecture. We expect evidence-driven artifacts and an execution plan we can hand to our in-house team.

High-Level Objectives

Ship a minimal but billable Pre-Visit Intake flow that:

Collects demographics + insurance images

Verifies eligibility with clearinghouse

Schedules/updates an appointment

Pushes summary into EHR via FHIR

Establish multi-tenant boundaries, role-based access, audit logs, and data retention.

Replace our brittle cron scripts with event-driven jobs and idempotent workers.

Provide operational runbooks, quality gates, and evidence logs (we like protocolized workflows).

Current/Target Environment

Frontend: Next.js 14 (App Router, React Server Components), Tailwind, shadcn/ui

Edge/API: Cloudflare Workers + Durable Objects (new); legacy Node/Express monolith (to be carved out)

Backend services: FastAPI (Python 3.11) for data ops & FHIR adapter (greenfield)

Data: Postgres 15 (Supabase), RLS for tenancy; S3-compatible object store (R2) for uploads; OLAP in Snowflake (later)

Messaging: Kafka (Confluent Cloud) preferred, but open to Cloudflare Queues for edge workflows

Integrations: Stripe (PaymentIntents w/ ACH + cards), Clearinghouse (X12/270/271 over SFTP + REST), EHR (FHIR R4)

Infra as Code: Terraform; CI/CD: GitHub Actions; Observability: Datadog + OpenTelemetry

Auth/SSO: OIDC (Auth0) and SAML for enterprise orgs

Compliance & Security (hard requirements)

PHI present → follow HIPAA safeguards (logging, RBAC, transport/storage encryption).

Data residency split: US tenants → us-east; EEA tenants → eu-west. No cross-region PII.

PII minimization & RLS enforced on every table path.

Zero secrets in code, use CF/KV + Secrets Manager.

SOC 2 audit-ability: evidence trails for deployments, approvals, and access.

Threat model for file uploads (malware scanning, content-type validation, image exif stripping).

⚠️ Conflict to resolve: Product wants photo uploads at the edge for speed and server-side virus scanning before persistence. Propose a pattern that meets both.

Performance / SLOs

P95 intake submit < 600 ms (excluding third-party eligibility call; show fallback UX).

Zero-downtime deploys for the new module.

Background jobs must be idempotent and at-least-once safe.

Functional Scope (MVP)

Intake UI (patient link via SMS/email): demographics, insurance photos, consent, e-signature.

Eligibility check: async; show optimistic confirmation, reconcile later.

Appointment update: writeback to EHR (FHIR Appointment/Patient/Coverage).

Payments: pre-auth $1 (or zero-auth) & store pm for later (Stripe).

Admin console: tenant-scoped configuration (eligibility vendor creds, branding, allowed forms).

Non-Goals (Phase-1)

No clinician charting or clinical decision support.

No patient portal beyond intake link + status page.

No in-app chat.

Deliverables (must be evidence-backed)

PROJECT-BRIEF.md with risks, assumptions, and traceability to this post.

TECHNICAL-DESIGN.md with:

Multi-tenant data model (Postgres + RLS policies as code)

Event model & retry strategy (Kafka/Queues)

Edge ↔ core service routing & failure modes

FHIR mapping for Appointment/Patient/Coverage (tables + transforms)

PRD.md for the intake feature (personas, user stories, acceptance criteria).

Task plan (tasks-intake.md) with dependencies & WHY notes.

CI/CD pipelines (lint, typecheck, unit, smoke); preview env creation.

Runbooks: incident response, rollback, secrets rotation, data residency checks.

Evidence package: validation reports, checksums, and approval gates.

Acceptance Criteria (examples)

Security: RLS denies cross-tenant reads/writes in unit & integration tests; e2e proves enforcement.

Privacy: EEA tenant data never leaves EU region; build shows region-pinned resources.

Resilience: Killing the eligibility worker mid-process results in a retry that does not double-charge or duplicate EHR entries.

Observability: Each intake flow correlates logs/traces via trace-id across edge + core.

DX: Local dev with make up stands up all services; seed tenant + demo user provided.

Data & Schemas (starter constraints)

Tables: tenants, users, patients, intake_sessions, eligibility_requests, payments, audit_logs

RLS baseline: tenant_id enforced; admin bypass forbidden—use security definer functions.

Objects: Insurance images → R2 bucket with signed URLs; scan before finalize.

Events: intake.submitted, eligibility.requested|succeeded|failed, ehr.writeback.completed|failed.

Known Constraints / Gotchas

Legacy monolith still handles appointment scheduling; must co-exist during cutover.

Clearinghouse sandbox returns false positives on holidays; need circuit-breaker + manual override.

Some clinics require SAML only; others OIDC. Handle both without forking tenants.

Stripe ACH micro-deposits not acceptable for MVP; card tokenization allowed.

Timeline & Milestones

Week 1: Discovery & architecture baseline, runbooks sketched, spike for edge upload + scan.

Week 2–3: Data model + RLS + workers + intake UI skeleton; CI/CD + preview env.

Week 4–5: Integrations (Stripe, eligibility, FHIR adapter), observability, e2e tests.

Week 6: Hardening, load tests, UAT; feature flag rollout.

What We Provide

Access to staging Postgres, R2, Auth0, Stripe test, clearinghouse sandbox.

Sample FHIR fixtures and redacted Postman collections.

Read-only access to monolith repo for extraction points.

Submission Requirements (no fluff)

Short proposal referencing this post’s constraints; no fabricated experience.

Outline of your workflow/protocols (we like explicit quality gates, artifacts).

Risks you’ll refuse to accept without extra time/budget.

1–2 code or doc samples (RLS policies, Terraform, or runbooks).

Availability and timezone overlap.

Budget

$18–28k for 6–8 weeks, milestone-based. We pay for evidence + working software, not promises.

Evaluation Rubric

Architecture clarity & trade-offs (data residency, edge scanning conflict)

Security/compliance correctness (RLS, secrets, audit)

Operational maturity (runbooks, CI/CD, observability)

Evidence discipline (traceability, gates, artifacts)

Communication (direct, no filler; plan-first)

Anti-fabrication clause: Any unverifiable claim or templated buzzwords without concrete references is an auto-reject.