# Product Backlog — Uplift Engine (Pilot → Platform)

Version: 2025-10-20
Owner: Product Owner (VPBank Credit Cards)
Agile Master: (this repo)

Legend
- Prio: 1 highest
- Est: Story points (Fibonacci)
- Trace: Link to whitepaper section(s)

## Epics
- E1: Model & Evaluation (Causal AI, Profit@K)
- E2: Feature Store & Data Contracts
- E3: Realtime Decisioning (API, Lambda, Endpoint)
- E4: Guardrails & Optimizer
- E5: MLOps Pipeline & Governance
- E6: Observability & Cost Control
- E7: Experimentation & Reporting

## Backlog (prioritized)

1. [Prio 1][E3] Realtime API skeleton (API GW + Lambda)
   - Est: 3
   - AC:
     - POST /decision returns 200 OK with stub JSON
     - Basic auth in place (placeholder)
   - Trace: 4.2

2. [Prio 1][E2] Feature Store skeleton (FeatureGroup, schema, point-in-time)
   - Est: 5
   - AC:
     - FeatureGroup created (online+offline), KMS enabled
     - Data contract with key features and event_time conventions
   - Trace: 3.3

3. [Prio 1][E1] UpliftRF baseline model training (script mode)
   - Est: 5
   - AC:
     - train.py runs in SageMaker, saves model artifact
     - Validation outputs AUUC + Profit@K
   - Trace: 2.2, 2.4

4. [Prio 2][E3] Deploy realtime endpoint (SageMaker) and invoke from Lambda
   - Est: 5
   - AC:
     - Lambda invokes endpoint and returns uplift_score, uplift_std_error
   - Trace: 4.2

5. [Prio 2][E4] Guardrails v1 — Hard rules (DNC)
   - Est: 3
   - AC:
     - DynamoDB DNC table; Lambda blocks DNC and logs reason
   - Trace: 5.2

6. [Prio 2][E6] CloudWatch dashboard + base alarms (API/Lambda/Endpoint)
   - Est: 3
   - AC:
     - Dashboard deployed; alarms: Lambda error>1%, p95 latency>80ms, API 5XX>0.5%
   - Trace: 4.2.1, Appendix A

7. [Prio 2][E5] Step Functions pipeline skeleton
   - Est: 5
   - AC:
     - State machine deployed; artifacts + metadata logged to S3
   - Trace: 4.1

8. [Prio 3][E1] Model race — DR-Learner & CatBoostUplift
   - Est: 8
   - AC:
     - Parallel jobs run; selection by Profit@K on validation
   - Trace: 2.2, 2.4, 4.1

9. [Prio 3][E4] Guardrails v2 — Soft rules (CI lower bound)
   - Est: 3
   - AC:
     - Lambda computes 95% lower bound; blocks when <=0; logs
   - Trace: 5.2

10. [Prio 3][E4] Knapsack optimizer (Lambda scale)
    - Est: 5
    - AC:
      - Given candidate offers, returns max-profit selection under budget
    - Trace: 5.1

11. [Prio 3][E7] Exposure/outcome logging and A/B design
    - Est: 5
    - AC:
      - Exposure to Kinesis; outcome ingestion; A/B group allocation documented
    - Trace: 4.2, 5.3

12. [Prio 4][E5] Human Approval gate + Model Card v1
    - Est: 3
    - AC:
      - Approval step wired; Model Card stored per version
    - Trace: 4.1, 6.3

13. [Prio 4][E7] KPI dashboard (Profit@K, ROI, budget saved)
    - Est: 5
    - AC:
      - QuickSight or interim dashboard with core KPIs, refreshed daily
    - Trace: 2.3, 6.1

14. [Prio 4][E6] Cost governance (S3 lifecycle, PC utilization)
    - Est: 3
    - AC:
      - Offline store lifecycle policy applied; PC alarms set
    - Trace: 3.3, 4.2.1

15. [Prio 5][E5] Blue/green + rollback automation
    - Est: 5
    - AC:
      - Endpoint and Lambda canary/blue-green with auto rollback on alarm
    - Trace: 4.1, 4.2

16. [Prio 5][E7] Bandits pilot (creative selection)
    - Est: 8
    - AC:
      - Thompson Sampling with DynamoDB state; periodic updates
    - Trace: 5.3

### Dependencies
- 1→4, 2→3→4, 3→8, 4→5/9/10/11, 7→12/15
