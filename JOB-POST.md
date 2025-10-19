JOB-POST.md — Principal Zero-Trust Payments Architect (Global, Post-Quantum Readiness)
Company

Aurelius Ledger Networks — Cross-border B2B payments network serving regulated financial institutions (Tier 1–3 banks, high-volume fintechs, and sovereign wealth funds).

Goal (Why we’re hiring)

We need an eight-week expert engagement to deliver a production-ready, compliance-audited MVP of a zero-trust payments orchestration layer that is quantum-resistant, regulator-auditable, and resilient across four continents. The outcome must include executable architecture, verified controls, and runbooks that internal teams can operate without external assistance.

High-Level Objectives

Launch a pilot-ready orchestration service that:

Handles real-time FX netting, settlement, and reconciliation with dual-ledger traceability.

Implements post-quantum cryptographic handshakes (CRYSTALS-Kyber + Dilithium) for interbank API sessions.

Enforces dynamic least-privilege policies across all microservices and partner integrations.

Provides end-to-end evidence trails for SWIFT CSP, PSD2 RTS, FedLine, and MAS TRM auditors.

Current/Target Environment

Platform core: Kubernetes (GKE + Anthos) spanning us-east1, eu-west1, ap-southeast1.

Service mesh: Istio with mTLS, SPIRE identity, gateway-API-based ingress.

Eventing: Kafka (Confluent), dual clusters per region, schema registry enforced.

Data layer: CockroachDB (regional survivability) + AWS QLDB for notarized settlement logs.

Edge connectivity: Cloudflare Workers for low-latency partner onboarding, hardware-backed tokens (YubiHSM2).

Languages: Rust (transaction engine), Go (policy microservices), Python (analytics pipeline).

Observability: OpenTelemetry + Prometheus + Grafana, bound to ISO 27001 controls.

CI/CD: GitHub Actions with in-toto provenance, Sigstore signing, and infrastructure deployment via Terraform + Pulumi hybrid.

Compliance & Security (hard requirements)

All crypto modules must leverage FIPS 140-3 validated libraries; post-quantum suites run behind feature flags with forced downgrade detection.

Zero standing credentials; adopt SPIFFE identities, HashiCorp Vault, and CloudHSM-backed signing for key material.

Multi-region data sovereignty: EU data pinned to eu-west1, APAC data to ap-southeast1, US data to us-east1; cross-border transfers require documented SCC workflows.

SWIFT CSP attestation pack: logging, transaction replay prevention, segregation of duties, and RBAC evidence.

Regulatory change window: MAS TRM 2023 addenda and FedLine security requirements must be reflected in controls catalogue.

Functional Scope (MVP)

Policy-driven orchestration engine that routes payments to compliant corridors with dynamic risk scoring.

FX netting microservice with deterministic reconciliation and audit-ready journal exports.

Partner onboarding workflow with post-quantum key exchange, attestation checks, and tamper-proof identity ledger entries.

Real-time compliance engine interfacing with sanctions list providers (Refinitiv, World-Check), storing decisions with non-repudiation.

Zero-trust access plane powering just-in-time secrets, command approval workflows, and SOC2 / PCI DSS evidence hooks.

Performance / SLOs

P99 round-trip settlement < 900 ms (excluding external clearing times) with circuit breakers and graceful degradation.

Automated failover between primary and DR regions within 45 seconds, zero data loss.

Real-time policy evaluation latency < 30 ms under 5k TPS sustained load.

Deliverables (must be evidence-backed)

Protocolized architecture dossier (threat model, trust boundaries, PQ crypto migration plan, data residency matrix).

Terraform/Pulumi stack definitions with drift detection and compliance guardrails.

Zero-trust policy pack (OPA/Rego + Cedar) with automated test fixtures.

Runbooks: quantum failback, SWIFT CSP audit prep, MAS TRM incident escalation, PQ key rotation.

Evidence manifest: Sigstore attestations, in-toto metadata, FedLine checklist coverage, policy drift dashboards.

Integration test suite proving multi-region failover, sanction rule accuracy, and policy enforcement.

Acceptance Criteria (examples)

Post-quantum handshake fallback fires alarms within 200 ms and records evidence for regulators.

Least-privilege enforcement confirmed via automated attack simulations (chaos & breach exercises) with audit logs attached.

Data residency validated through synthetic flow tests; any cross-border transfer emits SCC workflow tickets.

FX reconciliation demonstrates penny-perfect accuracy across three currencies and survives region failover tests.

Operational SRE drills (game days) prove recovery procedures for PQ certificate compromise and Kafka partition loss.

Known Constraints / Risks

Clearing partners only accept classic TLS 1.2 today; we must bridge while enforcing PQ viability.

Hardware security modules have 6-week lead times; need interim secure enclave strategy.

Interbank partners reside on-prem with strict firewall rules; must provide zero-trust gateways without exposing core mesh.

Upcoming MAS TRM update may tighten key rotation; expect mid-engagement requirement changes.

Submission Requirements (no fluff)

Concise proposal referencing this scope, highlighting verifiable zero-trust + financial compliance delivery.

Outline of workflow/protocols, quality gates, and evidence packages.

Explicit risk acceptance matrix (what will and will not be assumed within eight weeks).

Links to two proof artifacts: PQ cryptography adoption, regulated payment runbook, or zero-trust implementation.

Availability with timezone overlap across New York, Frankfurt, and Singapore.

Budget

$240–320k for eight weeks, milestone-based. Payment issued on evidence-backed deliverables and regulator-ready documentation.

Evaluation Rubric

Zero-trust architecture depth, PQ migration viability, and regional compliance coverage.

Operational rigor: automation-first approach, incident readiness, observability maturity.

Evidence discipline: traceability, attestations, regulator audit packages.

Risk transparency: clarity on assumptions, blockers, and mitigation pathways.

Communication: direct, regulator-ready documentation tone, alignment with executive steering committee.
