# VPBank Uplift Engine — Modernized Data Platform for Promotion Campaigns

## Executive Summary
This guide details the end-to-end process for building a modernized, ROI-driven data platform for bank promotion campaigns, tailored for VPBank. It covers business context, technical architecture, AWS deployment, MLOps, Causal AI, and best practices for team execution and demo delivery.

---

## 1. Business Context & Pain Points
- **Traditional marketing** wastes budget on customers who would convert anyway (“Sure Things”) or never convert (“Lost Causes”).
- **Current predictive models** (propensity) only answer “Who will buy?” — not “Who should we target to maximize incremental profit?”
- **Goal:** Modernize the platform to maximize ROI, minimize waste, and deliver measurable uplift.

---

## 1.1. Ví dụ về tích hợp dữ liệu số hóa
- **Nguồn dữ liệu số hóa:**
  - Digital banking: Lịch sử giao dịch, hành vi sử dụng app, đăng nhập, chuyển tiền, mở tài khoản online.
  - Mobile app: Sự kiện click, đăng ký dịch vụ, phản hồi khách hàng, sử dụng sinh trắc học.
  - Sinh trắc học: Xác thực, bảo mật, hành vi đăng nhập.
- **Pipeline tích hợp:**
  - Dữ liệu từ các hệ thống số hóa được đồng bộ về Data Lake (S3) thông qua API hoặc batch ETL.
  - Feature Store lưu trữ các đặc trưng đã xử lý, đảm bảo nhất quán giữa huấn luyện và phục vụ mô hình.
  - Quy trình tự động hóa: Khi có dữ liệu mới, pipeline sẽ tự động cập nhật đặc trưng, huấn luyện lại mô hình nếu cần, và triển khai mô hình mới lên Lambda/API Gateway.
- **Khả năng mở rộng:**
  - Có thể bổ sung thêm nguồn dữ liệu số hóa mới (ví dụ: dịch vụ 24/7, sản phẩm tín chấp/thế chấp) mà không cần thay đổi kiến trúc tổng thể.

---

## 2. Solution Overview
- **Modernized Data Platform:** Combines AWS-native MLOps, Feature Store, Causal AI, and real-time API scoring.
- **Uplift Engine:** Uses Causal Forests and advanced uplift modeling to target “Persuadables” — those who convert because of the campaign.
- **End-to-end workflow:** Data simulation → model training → deployment → real-time scoring → business impact measurement.

---

## 2.1. Ví dụ use-case thực tế
- **Chiến dịch khuyến mãi cho khách hàng digital banking:**
  - Thu thập dữ liệu giao dịch, hành vi sử dụng app, lịch sử phản hồi khuyến mãi.
  - Mô hình AI phân tích và xác định nhóm khách hàng có khả năng bị ảnh hưởng tích cực bởi khuyến mãi (Persuadables).
  - Tối ưu hóa ngân sách, chỉ gửi khuyến mãi đến nhóm này, đo lường hiệu quả qua dashboard ROI/Qini.

---

## 3. Architecture (see docs/architecture.png)
- **Data Lake (S3):** Stores raw events, campaign data, and model artifacts.
- **Feature Store:** Ensures training-serving consistency, solves “training-serving skew.”
- **Model Training (SageMaker):** Batch retraining with Causal AI algorithms (Causal Forest, DR-Learner, CatBoost Uplift).
- **Real-time Scoring (API Gateway + Lambda):** Inference endpoint for campaign targeting.
- **Monitoring (QuickSight):** Dashboards for ROI, uplift, and business KPIs.

---

## 4. AWS Setup & Deployment
### 4.1 S3 Bucket
- Create S3 bucket (e.g., `vpbank-hackathon-uplift-model-store`).
- Upload trained model (`src/uplift_model.pkl`).

### 4.2 IAM Role
- Create IAM role for Lambda with S3 read permissions.
- Attach least-privilege policies.

### 4.3 Lambda Function
- Package code from `src/lambda/app.py` and dependencies (`src/lambda/requirements.txt`).
- Set environment variables: `MODEL_S3_BUCKET`, `MODEL_S3_KEY`.
- Lambda downloads model from S3 to `/tmp` and loads for inference.

### 4.4 API Gateway
- Create HTTP API trigger for Lambda.
- Obtain public endpoint URL for demo.

---

## 5. MLOps & Feature Store
- **Why Feature Store?** Ensures features used in training are identical to those used in production scoring.
- **Best Practice:** Use SageMaker Feature Store or open-source alternatives for both batch and real-time feature access.
- **Avoid:** Manual feature engineering in notebooks without versioning.

---

## 6. Causal AI & Uplift Modeling
- **Baseline:** UpliftRandomForestClassifier (causalml).
- **Upgrade:** DR-Learner, CatBoost Uplift, or EconML for advanced causal inference.
- **Business Impact:** Only target “Persuadables” to maximize incremental profit.
- **Guardrails:** Add “Do-No-Harm” filters (confidence intervals, DNC lists) to avoid negative impact on VIPs or sensitive customers.

---

## 7. Optimization & Budget Allocation
- **Knapsack Optimization:** Instead of top-K ranking, use knapsack algorithms to maximize profit under budget constraints.
- **Best Practice:** Integrate optimization logic into Lambda or a dedicated microservice.

---

## 8. Demo & Presentation
- **Dry-run:** Use `docs/dry_run_schedule.md` and `scripts/dry_run_timer.ps1` to rehearse.
- **Presenter notes:** See `docs/presenter_notes.md` for slide-by-slide guidance.
- **Demo commands:** Use `docs/demo_commands.md` to test API endpoint live.
- **Presentation:** `docs/presentation.pdf` — includes architecture, Qini curve, ROI bar chart, and business mantra.

---

## 9. Team Workflow & Best Practices
- **Roles:**
  - Team Lead: Business impact, ROI, presentation.
  - Cloud Engineer: AWS setup, Lambda, API Gateway, architecture diagram.
  - ML Scientist: Model training, causal uplift, dashboard.
- **Version control:** Use GitHub for all code, notebooks, and artifacts.
- **Security:** Never commit credentials; use IAM roles and environment variables.
- **Documentation:** Keep all steps, configs, and runbooks in `docs/`.
- **Testing:** Validate Lambda locally before AWS deploy; use sample payloads.
- **Cleanup:** Remove AWS resources post-demo to avoid charges.

---

## 10. Final Checklist
- [x] Data simulated and model trained (`data/sample_data.csv`, `src/uplift_model.pkl`).
- [x] Lambda handler supports S3 model loading.
- [x] API Gateway endpoint live and tested.
- [x] Architecture diagram (`docs/architecture.png`) finalized.
- [x] Presentation deck polished and ready.
- [x] Team rehearsed with dry-run scripts.
- [x] All code, configs, and docs committed and pushed.

---

## Appendix: Useful Commands
- **Local Lambda test:**
  ```powershell
  python -c "from src.lambda import app; print(app.lambda_handler({'body': '{\"customerId\":1,\"age\":30,\"income\":40000,\"number_of_transactions\":5}'}, None))"
  ```
- **AWS deploy script:**
  ```powershell
  .\deploy\aws_deploy.ps1 -BucketName vpbank-hackathon-uplift-model-store -Region ap-southeast-1 -LambdaName uplift-engine-demo -ModelKey models/uplift_model.pkl
  ```
- **Dry-run timer:**
  ```powershell
  .\scripts\dry_run_timer.ps1 -minutes 5
  ```

---

## References & Further Reading
- [CausalML documentation](https://causalml.readthedocs.io/)
- [AWS SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [EconML documentation](https://econml.azurewebsites.net/)
- [AWS Lambda deployment best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
