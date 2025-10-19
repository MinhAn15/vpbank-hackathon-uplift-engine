# Ceremonies & Working Agreements

## Cadence
- Sprint: 2 weeks
- Daily Standup: 15 minutes, same time daily
- Backlog Refinement: weekly, 45–60 minutes
- Sprint Planning: 90 minutes
- Sprint Review + Demo: 45 minutes (focus on business value: Profit@K, ROI)
- Retrospective: 45 minutes (actions with owners & due dates)

## Agendas
- Daily: Yesterday/Today/Blockers; highlight risks to latency/ROI
- Planning: Scope, capacity, risks, Definition of Done; split stories to vertical slices
- Review: Show metrics and decisions; capture feedback into backlog
- Retro: What helped/hurt; pick 1–2 improvements only; confirm owners

## Working Agreements
- Decision logs in PRs; no PR > 500 LOC without rationale
- Code review SLA: 24h during working days
- Feature flags for risky changes; canary deploy by default
- Keep “definition of ready” before sprint commit; no mid-sprint scope creep
- WIP limits: 1 story per engineer; swarming allowed for blockers
- On-call rotation for prod issues; MTTR goal < 2h
