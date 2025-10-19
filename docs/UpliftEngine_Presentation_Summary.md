# Uplift Engine 2.1 — Project Summary

Author: Team Uplift
Date: 2025-10-19

Executive summary
-----------------
Uplift Engine 2.1 is an operational causal-AI platform that finds customers whose behavior will change because of a promotion ("Persuadables") and chooses contacts to maximize incremental profit under budget constraints. This document translates the technical design, algorithms, and pilot economics into a concise, actionable proposal for VPBank stakeholders: product, engineering, marketing and risk.

Expected outcomes: measurable uplift in incremental conversions, a significant reduction in wasted marketing spend, and auditable treatment and measurement that supports regulatory and product governance.

1. Business context & goals
---------------------------
- Problem statement: Traditional propensity models yield low ROI because they do not measure the causal impact of interventions. Marketing budgets are wasted on "Sure Things" and "Lost Causes." The bank needs a system that identifies "Persuadables"—customers who will convert because of the promotion.
- Business objectives:
  - Maximize incremental conversion and profit per campaign.
  - Reduce wasted marketing spend by at least X% (pilot target: 20%).
  - Provide auditable treatment assignment and measurement for regulatory and business oversight.

2. Product goals
----------------
- Deliver a minimal viable product (MVP) within 4-6 weeks: data ingestion, feature engineering, uplift model training, API for scoring, and basic ROI/Qini dashboards.
- Deliver a production pilot in 3 months: hardened MLOps, Feature Store, automated retraining, monitoring and guardrails.

3. Key concepts and algorithms
------------------------------
- Uplift Modeling (Causal AI): focused on estimating treatment effect at individual level. Preferred algorithms:
  - UpliftRandomForestClassifier (causalml) — fast baseline and interpretable.
  - Double Robust Learner (DR-Learner) — reduces bias and variance with orthogonalization.
  - CatBoost Uplift — robust to categorical features and often performant on tabular data.
  - EconML (for advanced causal inference and heterogeneous treatment effect estimation).
- Knapsack Optimization: to select treatment population under budget constraints, maximizing expected incremental profit rather than naive top-K.
- Guardrails: confidence-interval-based thresholds, DNC lists, and business rules to ensure Do-No-Harm.

4. Architecture overview
------------------------
- Data Lake (S3): central raw and processed storage.
- Ingestion: API, batch ETL, Kinesis for near-real-time events.
- Feature Store: SageMaker Feature Store (or open-source alternative) for training-serving consistency.
- Training: SageMaker or local notebooks for prototyping; EMR Serverless for heavy Spark workloads.
- Orchestration: Step Functions for managing complex pipelines (optional).
- Serving: API Gateway + Lambda (Provisioned Concurrency) for real-time scoring; batch scoring via EMR/Glue for large-scale campaigns.
- Monitoring & Dashboarding: QuickSight (or Grafana + Prometheus) for ROI, Qini, and model performance.

5. Why these choices (trade-offs)
--------------------------------
- S3 + Feature Store: decouples storage and feature serving. Ensures training-serving parity and reproducibility.
- Lambda + Provisioned Concurrency: keeps the serving path serverless and low-latency; PC eliminates cold starts at the cost of reserved concurrency fees.
- Tiered batch (Glue / EMR Serverless): Glue for routine jobs (cost-effective), EMR Serverless for heavy feature engineering jobs (performance), balancing cost and performance.
- Causal algorithms: uplift models directly optimize incremental effect; DR-Learner and EconML reduce confounding bias and provide better uncertainty estimates, important for business trust.

6. Process & MLOps
-------------------
- Data validation & lineage: incoming events are validated and catalogued; Feature Store records feature versions.
- CI/CD for models: use GitHub Actions or CodePipeline to run unit tests, model training smoke tests, and package Lambda artifacts.
- Model registry & artifacts: version models in S3 or SageMaker Model Registry; keep metadata (training data hash, features used).
- Monitoring: data drift alerts, model performance degradation, campaign-level ROI tracking.
- Retraining policy: scheduled retraining weekly or trigger-based when drift exceeds threshold.

7. Security & compliance
------------------------
- Use IAM roles with least privilege; never check secrets into repo.
- Encrypt data at rest (S3 SSE) and in transit (HTTPS).
- Apply data retention and anonymization policies where required by regulation.

8. Risks and mitigations
------------------------
- Risk: Cold-start / latency affecting SLA. Mitigation: Provisioned Concurrency for Lambda; compute critical features in app layer.
- Risk: Glue job OOM/timeouts. Mitigation: tiered processing with EMR Serverless for heavy jobs.
- Risk: Model harming customer segments. Mitigation: Do-No-Harm guardrails, CI-based tests, and manual review for VIP segments.

9. Roadmap & milestones
-----------------------
- Week 0-2: Data integration & sample dataset; basic uplift baseline model.
- Week 3-4: Real-time scoring API + basic dashboard; MVP demo.
- Month 2: Feature Store + automated retraining; A/B pilot.
- Month 3: Production pilot with PC-enabled Lambda, tiered batch, and monitoring.

10. Deliverables for handoff
---------------------------
- `docs/VPBank_UpliftEngine_Guide.md` — full technical guide.
- `docs/presenter_notes.md` — slides + speaker notes.
- `docs/architecture_notes.md` — instructions for updating architecture diagram.
- `docs/UpliftEngine_Presentation_Summary.md` and (pending) `docs/UpliftEngine_Presentation_Summary.docx` — the Word summary.

Appendix A — Suggested slide structure for team presentation
- Title
- Problem & Context
- Architecture (diagram)
- Method & Models
- Demo (Qini / API call)
- Business Impact & ROI
- Roadmap & Ask

To-do for finishing the Word document
------------------------------------
1. Internal review & refine the markdown draft (this file). (assigned: Team Lead)
2. Add one-page case study (pilot numbers) with simulated ROI table. (assigned: ML Scientist)
3. Finalize language and citations (assigned: Team Lead / ML Scientist)
4. Convert to .docx and add TOC, headings, and company cover page. (assigned: Cloud Engineer)
5. Final review & sign-off. (assigned: Team Lead)

Case study — Simulated pilot (example)
-------------------------------------
This one-page example demonstrates how we compute expected uplift ROI for a pilot promotion targeted by the Uplift Engine. Values are illustrative; replace with real business numbers for production pilots.

Assumptions:
- Pilot population: 50,000 customers
- Treatment cost (per contact): 10,000 VND
- Average revenue per conversion: 200,000 VND

| Segment | N | Control conv rate | Treated conv rate | Incremental conv (est) | Revenue / conv (VND) | Incremental revenue (VND) | Cost (VND) | Net uplift profit (VND) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Persuadables (top decile) | 5,000 | 2.0% | 6.0% | 200 | 200,000 | 40,000,000 | 50,000,000 | -10,000,000 |
| High potential (next 20%) | 10,000 | 1.5% | 3.5% | 200 | 200,000 | 40,000,000 | 100,000,000 | -60,000,000 |
| Low potential (remaining) | 35,000 | 0.5% | 0.6% | 35 | 200,000 | 7,000,000 | 350,000,000 | -343,000,000 |

Interpretation:
- The table shows estimated incremental conversions and revenue per segment. For an early pilot, prioritize the top decile ('Persuadables') where uplift-per-contact is highest and ROI is most likely to be positive.
- Use a knapsack-style optimizer to convert model scores into a treatment list that maximizes net uplift profit under the available budget and business rules. Run an A/B pilot to measure realized uplift and recalibrate the model and cost assumptions.

Notes:
- Replace these sample numbers with real campaign estimates before final proposals. The pilot should include an A/B test to measure real uplift and calibrate model uncertainty.

Slide-ready one-page summary
----------------------------
One-slide handout for executives — impact, ask, and immediate next steps.

- Business goal: Increase incremental conversions and cut wasted marketing spend by targeting "Persuadables" with causal uplift models.
- Product goal: MVP in 4–6 weeks (ingest → features → uplift model → scoring API → ROI dashboard); production pilot in ~3 months with MLOps and monitoring.
- Architecture (summary): Serverless real-time API (API Gateway → Lambda w/ Provisioned Concurrency), Feature Store for training-serving parity, Data Lake on S3, tiered batch (Glue / EMR Serverless).
- Algorithms: UpliftRandomForest (baseline), DR-Learner / EconML (robust CATE & uncertainty), knapsack optimizer for budgeted selection.
- Pilot ask (example): 50k customers; pilot budget ~500M VND. Target: demonstrate >=20% reduction in wasted spend vs current propensity approach.
- Success metrics: Incremental conversions, Profit@K, Qini/AUUC, ROI uplift, CI-calibrated treatment effects.
- Key risks: latency (mitigate with Provisioned Concurrency), heavy ETL (use EMR Serverless), customer harm (DNC lists + CI thresholds + manual review).
- Immediate next steps: approve pilot budget, grant data access to the team, appoint a single product owner, start a 4-week MVP sprint focused on measurable A/B uplift.

Call to action
--------------
- Approve the pilot budget and data access (example ask: 500M VND and access to customer/event data stores).
- Assign a product owner and a single technical lead (cloud engineer) to unblock infra and permissions.
- Run a 4-week MVP sprint with a defined A/B pilot that measures uplift, ROI and recalibrates the model.

The team will deliver a pilot report with measured Qini/AUUC, incremental conversions, and a recommended scale-up plan within 6 weeks of pilot start.
