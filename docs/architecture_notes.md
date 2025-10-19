Architecture update notes — Uplift Engine 2.1

Please apply the following visual updates to `docs/architecture.drawio` and export a new `docs/architecture.png` (high-fidelity PNG):

1) Lambda (Real-time inference)
   - Add small caption under the Lambda icon: "w/ Provisioned Concurrency for low latency".
   - Optional: show a small gauge icon indicating "low-latency SLA".

2) Batch processing component
   - Rename the "AWS Glue" label to: "AWS Glue / EMR Serverless".
   - Add a subtitle or tooltip text: "Tiered processing for cost/performance optimization — Glue for day-to-day jobs, EMR Serverless for heavy Spark workloads".

3) Kinesis / Near-real-time
   - Near the Kinesis icon add: "near-real-time features (e.g., transactions in last 5 min). For instant features compute at application layer before API call.".

4) Legend
   - Add a short legend or callout describing "Tiered processing" and "Provisioned Concurrency" so reviewers/judges immediately grasp the production-readiness changes.

5) Version & Author
   - Update a small text box: "Architecture v2.1 — includes Provisioned Concurrency & Tiered Batch (Glue / EMR Serverless)" and add author/date.

Notes
- Keep icons and layout unchanged where possible. These are small annotations to demonstrate production-readiness trade-offs without changing overall architecture.
- If you prefer, add a dashed boundary labeled "High-throughput / low-latency path" around API Gateway -> Lambda -> Feature Store to emphasize the critical path.

Contact
- If you need a hand editing the .drawio, attach it here or tell me and I can attempt to modify the XML programmatically.

Version note
- Architecture v2.1 — includes Provisioned Concurrency & Tiered Batch (Glue / EMR Serverless). Add author/date box on the diagram.
