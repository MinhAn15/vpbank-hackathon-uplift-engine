# Experiment Plan — Uplift Engine

## Hypothesis Template
- Hypothesis: <what do we expect to improve and why>
- Metric(s): Profit@K (K=?), ROI, AUUC, secondary (CTR/CVR)
- Segment: <target population>
- Duration & Sample: <est. to reach power>
- Risks/Ethics: <do-no-harm checks>

## Design
- Allocation: Control 10%, Treatment A (current best model) 45%, Treatment B (challenger) 45%
- Randomization unit: customer_id
- Exclusions: DNC, hard guardrails
- Outcome capture: exposure + outcome streams via Kinesis; delayed labels documented

## Analysis
- Primary: Profit@K (VND), ROI; tie-breakers AUUC/Qini
- Confidence: 95%; power ≥ 80% (approximate min sample using baseline CVR)
- Drift checks: feature/label drift during experiment; pause if triggered

## Decision
- Promote/Iterate/Stop
- Document in Model Card: version, metrics, caveats, decision, next steps
