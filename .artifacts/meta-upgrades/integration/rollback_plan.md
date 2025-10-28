# Meta-Upgrade Rollback Plan (Analysis-Only)

- All upgrades are overlays that emit artifacts only; no protocol edits
- Disable order (if needed): Dashboard (UPG06) → Meta-Cog (UPG09) → Fabric (UPG10) → PEL (UPG03) → Temporal (UPG08) → PIK (UPG01) → DNA (UPG02) → Ledger (UPG04) → POP (UPG05 observer)
- Action: Stop emitting artifacts; archive generated files under `.artifacts/meta-upgrades/archive/` with timestamp
- Verification: Confirm no new artifacts created post-disable; POP observer logs zero events
