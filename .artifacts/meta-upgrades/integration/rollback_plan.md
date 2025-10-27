# Meta-Upgrade Rollback Plan (Analysis Only)

- POP (UPG05): keep in Observer; if Controller activated later, rollback to Observer mode
- PEL (UPG03): disable negotiation hooks; fall back to direct handoffs
- PIK (UPG01): set halt_on_violation=false (read-only) while investigating
- DNA (UPG02): preserve existing artifacts; suspend schema enforcement
- Temporal (UPG08): disable time-bound escalations; retain manual SLAs
- Dashboard (UPG06): remove dashboard polling to cut overhead
- Fabric (UPG10): keep graph read-only; disconnect from POP checks
- Ledger (UPG04): never delete entries; pause appends if necessary
