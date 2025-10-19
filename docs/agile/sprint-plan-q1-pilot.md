# Sprint Plan — Q1 Pilot (Sprints 0–3)

Duration: 2-week sprints | Team capacity: define per role | Env: dev→uat→prod

## Sprint 0 — Foundations
- Goal: Running skeletons for data, model, realtime, and observability
- Scope:
  - Repo, IaC minimal (permissions, KMS), Feature Store skeleton, data contract
  - train.py baseline; Step Functions skeleton; base alarms & dashboard
  - API/Lambda hello-world; endpoints and paths reserved
- Risks: env access delays, data quality unknowns
- Exit criteria:
  - FeatureGroup (online+offline) created; point-in-time pattern documented
  - Step Functions state machine deployed
  - Dashboard + key alarms live

## Sprint 1 — Baseline E2E
- Goal: First E2E scoring path w/ UpliftRF
- Scope:
  - UpliftRF training job, deploy endpoint, Lambda invoke
  - Exposure logging to Kinesis; guardrails hard rules (DNC)
  - KPI dashboard MVP (AUUC, Profit@K sample)
- Risks: latency budget breach, feature gaps
- Exit criteria:
  - E2E request→decision<100ms (non-load conditions)
  - Baseline AUUC & Profit@K reported on validation

## Sprint 2 — Model Race + Optimization
- Goal: Select best model by Profit@K and add optimization
- Scope:
  - DR-Learner & CatBoostUplift parallel training; model selection by Profit@K
  - Guardrails soft rules (CI lower bound)
  - Knapsack optimizer (Lambda scale)
- Risks: training cost/time, uplift variance
- Exit criteria:
  - Best model promoted to prod endpoint (canary)
  - Optimizer returns feasible selection under budget

## Sprint 3 — Experiment & Governance
- Goal: Controlled A/B, governance ready to scale
- Scope:
  - A/B design + traffic allocation; outcome integration
  - Model Card v1; Human Approval gate
  - Security/compliance review & remediation items closed
- Risks: sample size, external dependencies
- Exit criteria:
  - Net Profit Uplift statistically significant vs. current policy
  - Release-ready runbook and rollback validated

## Phase (Pilot) success criteria
- Demonstrate Net Profit Uplift (VND) > current policy with 95% confidence
- Achieve E2E P95<100ms, Lambda error<1%, Endpoint p95<80ms
- Dashboard shows Profit@K, ROI, budget saved; alarms wired
