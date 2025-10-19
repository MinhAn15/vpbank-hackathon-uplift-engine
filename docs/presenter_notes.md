Presenter notes — Uplift Engine (VPBank Hackathon)

Slide order & speaker

1) Title (Team Lead) — 20s
   - One-line hook: "Chúng em là đội [Tên], và hôm nay chúng em sẽ trình bày Uplift Engine — một bộ nâng cấp cho nền tảng khuyến mãi của VPBank."

2) Problem & Mantra (Team Lead) — 45s
   - Acknowledge VPBank's Data Platform; state the gap: propensity != causal.
   - Deliver the team mantra (one-liner). Keep it crisp.

3) Architecture (Cloud Engineer) — 60s
   - Show `docs/architecture.png`.
   - Explain data flow: Features -> Feature Store -> Training & Serving -> Lambda/API.
   - Emphasize MLOps win: no training-serving skew.

4) Method & Model (ML Scientist) — 60s
   - Explain uplift modeling at a high level (Causal Forest / DR-Learner).
   - Mention guardrails (Do-No-Harm) and optimization (Knapsack).

5) Demo / Qini (Cloud Engineer + ML Scientist) — 60s
   - Run live scoring call (Cloud Engineer) -> show returned uplift score and recommendation.
   - ML Scientist: show `docs/qini_curve.png` explaining how we measure uplift and Profit@K.

6) Business Impact (Team Lead) — 45s
   - Show `docs/roi_bar.png` and the mantra.
   - Close with ask: trial campaign, pilot budget, next steps.

Tips for delivery
- Speak in business terms first (VND saved, %ROI), then briefly show the tech.
- Keep sentences short; rehearse transitions between speakers.
- If live demo fails, have a short recorded gif or screenshot flow ready.

Q&A prep (short answers)
- "How is this different from propensity models?" — Causal answers "Who to treat to create conversions", not "who will convert".
- "How do you avoid upsetting customers?" — We add Do-No-Harm guardrails: DNC lists + CI-based filters.
- "How long to deploy?" — With Feature Store + MLOps, a pilot can be deployed in weeks (data permitting).

7) Uplift Engine 2.1 (Cloud Engineer + Team Lead) — 60s
    - Slide title: "Uplift Engine 2.1 — production-readiness & cost/perf trade-offs"
    - Bullet points on slide:
       - "Provisioned Concurrency for Lambda inference — eliminates cold-starts, low-latency SLA"
       - "Kinesis for near-real-time features; instant features computed in-app before API call"
       - "Tiered batch: AWS Glue (default) + EMR Serverless for heavy Spark jobs"
    - Speaker notes (what to say):
       - Cloud Engineer: "We tuned the real-time path for SLA by using Provisioned Concurrency to remove cold starts; for near-real-time features we keep Kinesis, but for instant requirements we compute at the application layer before calling the API."
       - Team Lead: "For batch workloads we use a tiered approach — Glue for daily jobs and EMR Serverless for heavy feature engineering. This keeps costs predictable while enabling high-performance processing when needed."
    - Optional callouts: mention trade-offs — PC adds reserved cost; EMR Serverless costs when heavy jobs run but avoids OOM/timeouts on Glue.

Contact
- Team Lead: [name/email]
- Cloud Engineer: [name/email]
- ML Scientist: [name/email]
