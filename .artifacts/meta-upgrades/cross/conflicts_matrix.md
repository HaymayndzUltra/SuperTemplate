# Cross-Upgrade Conflicts Matrix (Analysis-Only)

- UPG03 (PEL) ↔ UPG08 (Temporal): Potential contention on handoff retries vs. timeouts.
  - Mitigation: Bounded retries with backoff; temporal layer owns SLAs; PEL respects SLA budget.
- UPG05 (POP) ↔ UPG07 (Adaptive Mutation): Governance vs. mutation proposals.
  - Mitigation: POP remains observer until criteria met; mutations sandboxed with POP-gated promotion.
- UPG10 (Reasoning Fabric) ↔ UPG05 (POP): Global graph used for cycle detection could differ from POP local views.
  - Mitigation: POP requires corroboration from Fabric before Controller activation.
- UPG01 (PIK) ↔ existing protocol gates: Risk of duplicate or conflicting validations.
  - Mitigation: PIK only reads DNA+Ledger; emits advisory violations; never weakens gates.
