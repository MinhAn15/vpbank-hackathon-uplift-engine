**VPBank Technology Hackathon 2025 – Senior Track**

General Brief

Tóm tắt ngắn gọn giúp hội đồng nắm được mục tiêu và phạm vi của giải pháp.

| **Challenge Statement** | Modernized Data Platform for Promotion Campaigns — Uplift Engine |
|-------------------------|-------------------------------------------|
| **Team Name**           | Uplift Engine |

**Elevator pitch (1–3 câu) — vì sao khác biệt**
- Bài toán: Ngân sách khuyến mãi bị lãng phí do nhắm nhầm (Sure Things/Lost Causes), thiếu realtime và thiếu explainability.
- Giải pháp: Rule Engine (no‑code) + Causal AI uplift, chạy serverless trên AWS (API Gateway, Lambda, SageMaker Feature Store/Endpoints, DynamoDB, ElastiCache Redis, Kinesis/MSK, Redshift) — đảm bảo P95 < 100ms cho realtime và batch 1M giao dịch ≤ 6h.
- Giá trị: Tối đa hóa Net Profit Uplift/Profit@K/ROI, minh bạch lý do (reason codes/SHAP), business tự publish rule trong phút, audit/versioning đầy đủ.

**Team Members**

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th><strong>Full Name</strong></th>
<th><strong>Role</strong></th>
<th><strong>Email Address</strong></th>
<th><p><strong>School Name</strong></p>
<p><strong>(if applicable)</strong></p></th>
<th><strong>Faculty / Area of Study</strong></th>
<th><strong>LinkedIn Profile URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Member 1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Member 2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Member 3</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Member 4</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Member 5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Content Outline**

<table style="width:70%;">
<colgroup>
<col style="width: 53%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: right;">Page No.</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Solutions Introduction</strong></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td><strong>Impact of Solution</strong></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td><strong>Deep Dive into Solution</strong></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td><strong>Architecture of Solution</strong></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

**DRAFTING (XÓA TRƯỚC KHI NỘP)**

- **Bài toán & Mục tiêu**

  - **Hệ thống khuyến mãi truyền thống chạy batch chậm, thiếu linh hoạt,
    hiệu quả thấp.**

  - **Mục tiêu: Nền tảng dữ liệu khuyến mãi hiện đại, cho phép business
    tự thiết kế/cấu hình campaign (no-code), hỗ trợ batch + near
    real-time + real-time, cá nhân hóa đúng lúc.**

- **Giá trị kinh doanh**

  - **Tối đa hóa Net Profit Uplift, giảm lãng phí nhắm nhầm Sure
    Things/Lost Causes.**

  - **Rút ngắn time-to-market (no-code rule changes), tăng hiệu quả
    chiến dịch.**

  - **Explainability minh bạch cho từng quyết định (lý do đủ điều
    kiện).**

- **Năng lực cốt lõi**

  - **Business User Configurability: Rule Builder UI (kéo-thả/form),
    versioning, audit, publish/rollback tức thì.**

  - **Rule Engine + Guardrails + Optimizer: Lọc eligibility → xếp hạng
    theo uplift → tối ưu ngân sách/ràng buộc.**

  - **Explainability (core): Trả về reason codes/SHAP top-K,
    threshold_met theo rule.**

  - **Xử lý dữ liệu end-to-end: Ingest, cleaning, enrichment,
    transformation; structured + unstructured.**

- **Kiến trúc tổng thể (đầy đủ)**

  - **Experience & Config**

    - **Campaign Configuration UI (AppSync GraphQL + Cognito)**

    - **Rule DSL (JSON/YAML), workflow phê duyệt, versioning**

  - **Rule Store & Cache**

    - **DynamoDB: RuleSets (versioned, compiled predicates)**

    - **ElastiCache Redis: Cache rule/feature, leaderboard, session
      (TTL)**

  - **Decisioning & ML**

    - **API Gateway → Lambda Decision Service (Provisioned
      Concurrency)**

    - **Rule Engine runtime (Lambda/EKS container)**

    - **Uplift Model Endpoint (SageMaker Endpoint; TreeSHAP inline)**

    - **Guardrails (caps/frequency/DNC) + Knapsack Optimizer (ngân
      sách/ràng buộc)**

  - **Feature Platform**

    - **SageMaker Feature Store: Online (low-latency) + Offline
      (S3/Parquet)**

    - **S3 Data Lake (raw, curated), Glue Catalog**

  - **Streaming & Events**

    - **Amazon MSK (Kafka) hoặc Kinesis (streams + Firehose)**

    - **Stream processing (Lambda/Glue Streaming) cập nhật aggregates**

  - **Batch & Analytics**

    - **Glue/EMR Serverless (Spark) cho cleaning/enrichment/transforms**

    - **Amazon Redshift (DWH) cho lịch sử campaign, phân tích,
      dashboard**

  - **MLOps & Orchestration**

    - **Step Functions: train/evaluate/deploy, Model Cards, approvals**

    - **SageMaker Model Monitor: data/concept drift → retrain**

  - **Monitoring & Alerting**

    - **CloudWatch Dashboards + Alarms (API P95/P99, Lambda errors,
      Endpoint latency)**

    - **Redshift (QueryDuration, WLMQueueLength), Redis (CacheHitRate)**

    - **SNS thông báo sự cố**

  - **Bảo mật & Tuân thủ**

    - **IAM least privilege, KMS, log bất biến, audit trail
      rules/models**

- **Luồng dữ liệu chính**

  - **Batch: S3/Redshift → Glue/EMR (clean/enrich/aggregate) → Offline
    FS → Scoring → Rule evaluate → Output Redshift/S3.**

  - **Real-time: MSK/Kinesis event → Aggregates/Redis → API GW →
    Decision Lambda (Rule → Uplift → Guardrails/Optimizer) → Explanation
    JSON → Notification/Leaderboard → Redshift.**

- **Data Handling (structured + unstructured)**

  - **Structured: profiles, balances, transactions; time windows
    7/30/90d; velocity/RFM/preferences.**

  - **Unstructured: call transcripts/email/social/clickstream JSON →
    embeddings/sentiment/topics → Feature Store; raw lưu S3.**

- **Explainability (MVP)**

  - **Response gồm: decision, uplift_score, explanation.primary_factors
    (SHAP/reason codes), threshold_met. P95 \< 100ms (TreeSHAP cho
    tree-based; fallback reason codes + SHAP async nếu cần).**

- **Performance & Benchmarks**

  - **Batch: 1M giao dịch ≤ 6h; E2E ≤ 8h; scale đến 10M/ngày (EMR
    Serverless).**

  - **Real-time: P95 \< 100ms, P99 \< 150ms; ≥ 10k RPS; ≥ 100k
    concurrent sessions.**

  - **Ingest: MSK/Kinesis ≥ 50k events/s; Feature Store writes ≥ 10k
    rec/s.**

- **Adaptability (đa dạng khuyến mãi, no-code)**

  - **Cashback %, fixed; Tiered rewards; Sales contest (leaderboard);
    Challenge; Flash sales; Merchant/category campaigns.**

  - **Rule change qua UI, lưu JSON/YAML ở DynamoDB, hiệu lực ngay (cache
    invalidation), versioning/audit.**

- **Demo Scenarios (để trình bày)**

  - **Scenario 1: Batch-driven Cashback (Dining ≥ 5M/tháng)**

    - **Dữ liệu: Redshift → Glue/EMR → FS → Scoring → Rules → Output +
      Explanation**

    - **Mục tiêu: 1M txn ~ 6h; báo cáo eligibility + reason**

  - **Scenario 2: Real-time Sales Contest (flash 2h, top 100)**

    - **Dữ liệu: Kafka/MSK → Decision (\<100ms) → Leaderboard (Redis) →
      Notification**

    - **Mục tiêu: P95 \< 100ms; refresh leaderboard ≤ 1s**

- **Tech stack**

  - **Languages: Python, Node.js/TypeScript**

  - **AWS: API Gateway, Lambda, SageMaker (Feature
    Store/Endpoint/Monitor), Step Functions, S3, Glue/EMR, Redshift,
    DynamoDB, ElastiCache Redis, MSK/Kinesis, CloudWatch, SNS, Cognito,
    AppSync**

  - **Containers: Docker; EKS cho rule/inference nâng cao khi cần**

- **Agile delivery (rút gọn)**

  - **Sprint 0–3 (pilot): baseline E2E, Rule UI, realtime + batch demo,
    monitoring.**

  - **Ceremonies 2 tuần; DoR/DoD ML/Data/Infra; KPI: Profit@K, ROI,
    latency, error rate.**

**Solutions Introduction**

Uplift Engine is a modern, configurable promotion data platform that
turns promotions into profit by targeting persuadable customers—those
who convert because of the treatment. It combines a no-code Rule Engine
(for business users) with Causal AI uplift modeling, low-latency
decisioning, and transparent explanations.

**Tóm lược (ngữ cảnh ngân hàng & mục tiêu kinh doanh)**
- Bối cảnh: Với sản phẩm thẻ tín dụng (ví dụ STEPUP) và tài khoản CASA, ngân hàng cần vừa tăng chuyển đổi, vừa giảm lãng phí ưu đãi. Phương pháp traditional propensity nhắm cả Sure Things/Lost Causes làm bào mòn lợi nhuận. Uplift Engine tập trung Persuadables, tối đa hóa Net Profit Uplift.
- Hai kịch bản demo đặc trưng ngành: (1) realtime voucher khi chi tiêu STEPUP tại siêu thị cho phân khúc AF/MAF (latency rất thấp), (2) hoàn phí số đẹp CASA khi duy trì số dư liên tục 30 ngày (batch/near real-time).
- Triết lý kỹ thuật: serverless-first trên AWS (API Gateway, Lambda, SageMaker Feature Store/Endpoints, DynamoDB, ElastiCache Redis, Kinesis/MSK, Redshift), đảm bảo low-latency, tính nhất quán feature, và khả năng mở rộng.

**Tiêu chí đánh giá thành công dự án (mở rộng)**

1. Ba Ràng Buộc Cốt Lõi (Triple Constraint) – "Cái Tam Giác"
  - Phạm vi (Scope): Sản phẩm/dịch vụ/kết quả đúng yêu cầu đã định nghĩa.
  - Thời gian (Time): Hoàn thành đúng hạn; yếu tố ít linh hoạt nhất.
  - Chi phí (Cost): Hoàn thành trong ngân sách được phê duyệt.
  - Lưu ý: Nhà tài trợ thường xếp hạng ưu tiên giữa Phạm vi–Thời gian–Chi phí để đội dự án cân bằng phù hợp.

2. Các Tiêu Chí Thành Công Mở Rộng
  - Sự hài lòng của Khách hàng/Nhà tài trợ: Chỉ số cảm nhận, mức độ tin tưởng và chấp nhận.
  - Đạt được Mục tiêu Chính: Tạo/tiết kiệm tiền, ROI, hoặc outcome đã cam kết.

3. Yếu Tố Quan Trọng cho Thành công Dự án CNTT
  - Quản lý các Bên liên quan (Stakeholder Management): Xác định–hiểu–đáp ứng kỳ vọng; bỏ qua stakeholder dễ dẫn đến thất bại.
  - Sponsorship cấp cao (Executive Sponsorship): Yếu tố thành công hàng đầu; bảo trợ/ra quyết định giải toả bế tắc.
  - Sự tham gia của Người dùng (User Involvement): Đồng thiết kế, phản hồi sớm; đảm bảo phù hợp nghiệp vụ.
  - Nguồn lực & Chuyên môn (Resources & Expertise): Vốn, con người đúng kỹ năng là nền tảng cho tiến độ/chất lượng.
  - Kỹ năng mềm & Giao tiếp (Soft skills & Communication): Truyền thông rõ ràng, thường xuyên; giảm hiểu nhầm/rủi ro.
  - Phương pháp Quản lý Dự án chính thức: Tổ chức vận hành tốt đạt tỷ lệ thành công cao vượt trội.

Tóm lại, thành công dự án CNTT không chỉ là “đủ tam giác” (Scope–Time–Cost) mà còn bao gồm sự hài lòng của khách hàng/bên liên quan và giá trị kinh doanh thực nhận (ROI). Nghiên cứu thực tiễn cho thấy nếu chỉ bám ba tiêu chí truyền thống, tỷ lệ thành công bền vững rất thấp; do đó cần bổ sung tiêu chí mở rộng và các yếu tố then chốt ở trên.

**Liên hệ với Uplift KPIs (Net Profit Uplift/Profit@K/ROI)**
- Scope: MVP phải chứng minh Profit@K (K% dân số) và Net Profit Uplift dương trên pilot, với explainability đủ để audit.
- Time: UC1 phải đạt P95 < 100ms trong giờ cao điểm (Provisioned Concurrency + Redis + Endpoint tối ưu). UC2 đạt SLO batch ≤ 6h cho 1M giao dịch.
- Cost: Ưu tiên Glue cho khối lượng vừa, nâng lên EMR Serverless khi lớn; cache/feature strategy giảm chi phí đọc; autoscaling endpoint theo RPS/CPU.

**Key features:**

- Business-user configurability: Campaign Configuration UI
  (React/Amplify) + AppSync GraphQL + DynamoDB for versioned rules;
  publish/rollback without deployments.

- Explainability-by-design: Every decision includes human-readable
  reason codes (e.g., "Customer spent 5M VND in Dining this week,
  reached Gold tier"). TreeSHAP for tree models; async SHAP fallback for
  complex learners.

- Full-spectrum processing: Batch (Glue/EMR), near real-time
  **message-queue** (Kinesis/MSK + Lambda), and real-time (\<100ms) via
  API Gateway + Lambda + SageMaker **<u>Feature Store</u>** + Endpoint +
  Redis cache.

- AWS-native, **<u>serverless-first</u>**: Lambda (Provisioned
  Concurrency), Step Functions, SageMaker (Feature Store, Training,
  Endpoints), DynamoDB, Redshift, ElastiCache Redis, Kinesis/MSK.

- Optimizer & guardrails: **<u>Knapsack optimizer</u>** for budget
  allocation; do-no-harm guardrails (DNC, confidence lower bound,
  frequency capping).

**Impact of Solution**

**Tác động kinh doanh (giải thích theo domain ngân hàng)**

- Tập trung pilot theo squad sản phẩm (Thẻ tín dụng hoặc CASA) để lượng hóa nhanh Net Profit Uplift; sau đó nhân rộng theo “internal platform”.
- Tăng ROI, giảm lãng phí: Ngân sách hướng vào Persuadables, tránh Sure Things/Lost Causes. Guardrails (DNC, confidence lower bound, frequency capping) bảo vệ thương hiệu và tuân thủ.
- Rút ngắn time-to-market: Business chỉnh rule trên UI (no-code), publish tức thì (versioning/audit/rollback) — phù hợp nhịp go-to-market nhanh của retail banking.
- Cá nhân hóa ở quy mô lớn: Eligibility + uplift scoring realtime (P95 < 100ms), cập nhật contest/leaderboard near real-time.

**Why this solution is better:**

**Vì sao phù hợp hơn (giải thích kỹ thuật + nghiệp vụ)**
- Causal AI tối ưu lợi nhuận thuần gia tăng, đúng mục tiêu kinh doanh (không nhầm với propensity).
- Consistency by design: SageMaker Feature Store loại bỏ training-serving skew; đảm bảo point-in-time correctness cho cả offline/online.
- Vận hành: Redis caching giảm độ trễ rule/feature; CloudWatch + Model Monitor giúp quan sát, phát hiện drift, và kích hoạt retrain.

**Differentiators (USP):**

- Explainability as a core MVP feature in inference (reason codes/SHAP).

- No-code Rule Engine tightly integrated with uplift/optimizer.

- Tiered architecture (Glue/EMR) for cost-performance balance,
  SERVERLESS, SCALABLE

**Deep Dive into Solution**

**End-to-end flows: INPUT DATASOURCE – UI INTERACTION**

- Data ingestion & features: Structured (profiles, transactions) và unstructured (text/clickstream) xử lý qua Glue/EMR; bắt buộc point-in-time correctness; lưu tại SageMaker Feature Store (Offline/Online).
  - Vì sao hợp lý: Tránh leakage khi huấn luyện dựa dữ liệu quá khứ; Online Store (DynamoDB backend) đảm bảo <10ms cho realtime.

- MLOps: Step Functions điều phối feature jobs và “model race” (CatBoostUplift, DR-Learner, CausalForest), chọn best theo Profit@K, register/deploy Endpoint.
  - Vì sao hợp lý: Tách biệt training pipeline chuẩn, có human approval khi cần; dễ audit và tái lập.

- Real-time decisioning: API Gateway → Lambda (Provisioned Concurrency) → Online Feature Store (GetRecord) → Uplift Endpoint → Guardrails → Optimizer → Response (explanation). Exposure/outcome log đẩy qua Kinesis/MSK vào Redshift.
  - Vì sao hợp lý: Chain ngắn, cache hợp lý, đảm bảo P95 < 100ms; degrade được nếu Endpoint lỗi (rule-only tạm thời).

- Rule Engine: UI → AppSync → DynamoDB (draft/publish) → Lambda CompileRule → Redis cache compiled rules; Decision Lambda evaluate ~1–5ms từ Redis.
  - Vì sao hợp lý: No-code cho business, publish/rollback tức thì; version pinning đảm bảo reproducibility.

- Streaming & near real-time: Kinesis/MSK cập nhật aggregates và kích hoạt logic eligibility/contest (leaderboard Redis/Redshift).
  - Vì sao hợp lý: Phản ứng nhanh theo sự kiện chi tiêu, phù hợp UC1/UC2.

Contract examples:

- Request (client → API): { customerId, context }

- Response: decision, offer, uplift_score, uplift_std_error,
  explanation.primary_factors, threshold_met

**Demo scenarios (prototype-ready):**

- Batch cashback: Weekly/monthly cap + rule threshold; batch evaluation
  via Glue/EMR; outputs to Redshift with explanations.

- Real-time sales contest: First N customers meeting spend within a time
  window; streaming updates + real-time rule evaluation and leaderboard
  refresh.

**Architecture of Solution**

**Kiến trúc và lựa chọn AWS services (kèm lý do)**

- API Gateway + Lambda (Provisioned Concurrency): Quyết định low-latency; loại bỏ cold start. Ưu tiên Lambda vì đơn giản, autoscale theo traffic.

- SageMaker Feature Store: Offline (S3/Parquet) cho training/analytics; Online (DynamoDB) cho đọc feature <10ms. Bắt buộc event_time và schema quản trị.

- SageMaker Endpoints: Uplift inference realtime; TreeSHAP inline với mô hình cây; autoscaling theo RPS/CPU, hỗ trợ canary/blue-green.

- AppSync + Cognito + S3/CloudFront (UI): Rule Builder UI auth an toàn; GraphQL mutation tạo/publish; audit trail qua Streams/Firehose.

- DynamoDB + Redis: Lưu versioned ruleset và cache compiled rules 1–5ms; invalidation sau publish/rollback; TTL cho leaderboard/state.

- Kinesis/MSK + Firehose: Exposure/outcome streams; đổ S3/Redshift phục vụ analytics/monitoring. Lựa chọn MSK khi cần exactly-once/đa hệ.

- Glue/EMR Serverless: Kiến trúc bậc thang tối ưu chi phí/hiệu năng; tự động chọn Glue vs EMR theo kích thước workload.

- Redshift: DWH phân tích campaign KPI, eligibility batches, explainability logs; sizing RA3 tùy workload, WLM queue chuẩn.

**Performance & Benchmarks:**

- Real-time decisioning: P95 \< 100ms, P99 \< 150ms (API Gateway + Lambda + Feature Store + Endpoint + Rule eval + Guardrails). Provisioned Concurrency + warm-up sau deploy.

- Batch processing: ≥ 1,000,000 transactions trong ≤ 6h (Glue/EMR Serverless); mở rộng 10,000,000/ngày qua autoscaling, partitioning, file size chuẩn Parquet (~128MB).

- Streaming ingest: Kinesis/MSK ≥ 50,000 events/sec; Feature Store writes ≥ 10,000 records/sec với parallel writers + backpressure/retry có kiểm soát.

**Degrade & Resilience (thực tế vận hành)**
- Khi Endpoint chậm/lỗi: degrade về rule-only với SLA tạm thời; bật DLQ (SQS) cho consumer; retry policy Step Functions/Firehose; WAF + throttling bảo vệ upstream.

Processing modes covered as required: Batch, Near real-time, and
Real-time.

**Architecture diagram:**

<img src="media/image3.png" style="width:10in;height:3.93308in"
alt="A computer screen shot of a diagram AI-generated content may be incorrect." />
