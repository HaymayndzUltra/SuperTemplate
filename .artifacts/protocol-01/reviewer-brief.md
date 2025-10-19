# Protocol 01 Reviewer Brief

## Summary
- **Protocol:** Client Proposal Generation
- **Status:** Draft completed with manual validation artefacts.
- **Scope Alignment:** Proposal reflects zero-trust, post-quantum, and compliance requirements highlighted in JOB-POST.md.

## Key Decisions
- Adopted four-milestone structure aligning to eight-week budget cadence.
- Leveraged existing compliance accelerators for evidence ledger and policy automation references.
- Emphasized automation-first collaboration model with signed provenance workflows.

## Risks & Mitigations
1. **Missing Discovery Profile**: `.cursor/context-kit/project-profile.json` absent. → *Mitigation*: Request discovery lead upload before client submission; update proposal if preferences differ.
2. **Approval Gap**: Discovery lead confirmation not documented. → *Mitigation*: Block external delivery until approval recorded in governance tracker.
3. **Compliance Scripts Not Run**: HIPAA/gate scripts pending due to approval gap. → *Mitigation*: Schedule validation dry-run once approvals land.

## Pending Questions for Client
- Confirm availability of hardware security modules or interim enclaves.
- Validate partner readiness for PQ feature flags and downgrade workflow expectations.
- Identify preferred artefacts for risk acceptance matrix (spreadsheet vs. runbook).

## Next Actions
- Secure discovery lead sign-off.
- Run `scripts/analyze_jobpost.py`, `scripts/tone_mapper.py`, and `scripts/validate_proposal.py` once approvals granted.
- Prepare links to requested proof artefacts (PQ adoption, regulated payment runbooks) for inclusion in final package.
