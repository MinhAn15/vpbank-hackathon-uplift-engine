# Tổng Quan Kỹ Thuật & Chiến Lược: Uplift Engine 2.1

## 1. Tuyên Bố Sứ Mệnh (Mission Statement)

**"Uplift Engine"** không phải là một nền tảng dữ liệu thụ động. Đây là một **cỗ máy tối ưu hóa lợi nhuận** được xây dựng để trả lời câu hỏi kinh doanh cốt lõi: *"Nên tác động vào khách hàng nào, với khuyến mãi nào, và với ngân sách bao nhiêu để tối đa hóa Lợi Nhuận Thuần Gia Tăng (Net Profit Uplift)?"*

Chúng ta chuyển dịch từ AI **Dự đoán (Predictive)** sang AI **Chỉ định Hành động (Prescriptive)**.

---

## 2. Kiến Trúc Hệ Thống "Uplift Engine 2.1"

Kiến trúc này được thiết kế dựa trên 4 nguyên tắc: **Tự động hóa MLOps**, **Độ trễ cực thấp**, **Tối ưu Chi phí & Hiệu năng**, và **Quản trị Rủi ro**.

*(Tham khảo `docs/architecture.png`)*

### **Các Thành Phần Cốt Lõi:**

* **Lõi Thu Thập & Xử Lý Dữ Liệu:**
  * **S3 Data Lake:** Nguồn chân lý duy nhất cho dữ liệu thô và đã qua xử lý.
  * **Kinesis Data Streams:** Thu thập dữ liệu sự kiện (clicks, transactions) trong thời gian thực.
  * **Kiến trúc Xử lý Bậc thang (Tiered Architecture):**
    * **AWS Glue:** Xử lý các job ETL/feature engineering hàng ngày với quy mô vừa.
    * **Amazon EMR Serverless:** Tự động được kích hoạt cho các tác vụ Big Data cực lớn, đảm bảo hiệu năng mà không cần quản lý cluster.

* **Lõi MLOps & Quản Trị Mô Hình:**
  * **SageMaker Feature Store:** **Trái tim của nền tảng**, giải quyết triệt để vấn đề training-serving skew, cung cấp feature nhất quán cho cả online và offline.
  * **SageMaker Training Jobs:** Tự động hóa việc huấn luyện các mô hình Causal AI ở quy mô lớn.
  * **SageMaker Model Registry:** Quản lý phiên bản và vòng đời của các mô hình, hỗ trợ A/B testing.
  * **AWS Step Functions:** "Tổng quản lý" điều phối toàn bộ pipeline MLOps từ xử lý dữ liệu, huấn luyện, đăng ký, đến triển khai.

* **Lõi Ra Quyết Định Thời Gian Thực:**
  * **API Gateway:** Cổng giao tiếp, nhận request từ các ứng dụng (VPBank NEO app).
  * **AWS Lambda (w/ Provisioned Concurrency):** Nơi thực thi logic nghiệp vụ. Việc sử dụng **Provisioned Concurrency** giúp loại bỏ hoàn toàn vấn đề cold start, đảm bảo độ trễ ổn định dưới 100ms.
  * **SageMaker Real-time Endpoint:** Nơi triển khai "bộ não AI" để cung cấp `upliftScore` với độ trễ thấp.
  * **DynamoDB:** Lưu trữ trạng thái của Contextual Bandits và các quyết định policy.

---

## 3. Luồng Kỹ Thuật Chi Tiết (Step-by-Step)

### A. Luồng Dự Đoán Thời Gian Thực (Real-time Inference Flow)

Đây là luồng hoạt động khi khách hàng tương tác với app VPBank, được thiết kế để hoàn thành trong dưới 100ms.

1.  **Request:** Ứng dụng VPBank NEO gửi một request chứa `customerId` đến **API Gateway**.
2.  **Trigger & Logic:** API Gateway kích hoạt hàm **AWS Lambda** (đã được "làm nóng" bởi Provisioned Concurrency).
3.  **Lấy Feature:** Lambda gọi đến **SageMaker Online Feature Store**, lấy ra feature vector mới nhất của `customerId`.
4.  **Lấy Uplift Score:** Lambda gửi feature vector đến **SageMaker Endpoint**. Endpoint trả về `upliftScore` và khoảng tin cậy (confidence interval).
5.  **Kiểm Tra Guardrails:** Lambda thực thi bộ lọc **"Do-No-Harm"**:
  * *Hard Rule:* Kiểm tra khách hàng có trong danh sách DNC không.
  * *Soft Rule:* Kiểm tra `Lower_Bound_Uplift(95%)` có > 0 không. Nếu không, hủy bỏ.
6.  **Tối Ưu Hóa (Knapsack & Bandit):** Nếu vượt qua Guardrails:
  * Thông tin `upliftScore` (value) và `cost` của các khuyến mãi khả dụng được gửi đến **bộ tối ưu Knapsack** (logic bên trong Lambda) để chọn ra khuyến mãi tối ưu nhất trong giới hạn ngân sách.
  * **Contextual Bandit** (trạng thái trên DynamoDB) có thể được dùng để chọn ra `creative/offer` cụ thể.
7.  **Response:** Lambda trả về quyết định khuyến mãi cuối cùng cho ứng dụng.

### B. Luồng Tự Động Hóa Huấn Luyện (MLOps Pipeline Flow)

Luồng này được **AWS Step Functions** điều phối, chạy tự động theo lịch (hàng tuần/tháng).

1.  **Trigger:** Lịch trình kích hoạt State Machine của Step Functions.
2.  **Xử Lý Dữ Liệu:** Step Functions khởi chạy một job **AWS Glue** (hoặc **EMR Serverless** nếu dữ liệu lớn) để:
  * Đọc dữ liệu thô từ **S3 Data Lake**.
  * Thực hiện feature engineering.
  * Ingest các feature mới vào **SageMaker Offline/Online Feature Store**.
3.  **Huấn Luyện Mô Hình:** Sau khi job Glue hoàn thành, Step Functions khởi chạy một **SageMaker Training Job**.
  * Job này đọc dữ liệu từ **Offline Feature Store**.
  * Huấn luyện một mô hình Causal AI (ví dụ: `CausalForest` hoặc `CatBoost Uplift`).
4.  **Đánh Giá & Đăng Ký:** Mô hình sau khi huấn luyện sẽ được đánh giá tự động (dựa trên **Profit@K (VND)**). Nếu đạt ngưỡng chất lượng, nó sẽ được đăng ký vào **SageMaker Model Registry**.
5.  **Triển Khai (Tùy chọn có Phê duyệt):** Một bước phê duyệt thủ công (human approval) có thể được tích hợp. Sau khi được duyệt, Step Functions sẽ tự động triển khai mô hình mới ra **SageMaker Endpoint**, có thể theo pattern Blue/Green deployment để đảm bảo an toàn.

---

## 4. Bằng Chứng & Kết Quả

Dựa trên các thực thi trong repo:
* **Mô hình:** `src/uplift_model.pkl` đã được huấn luyện.
* **Hiệu quả kỹ thuật:** `docs/qini_curve.png` cho thấy mô hình có khả năng phân loại tốt hơn nhiều so với ngẫu nhiên.
* **Tác động kinh doanh:** `docs/roi.csv` và `docs/roi_bar.png` chứng minh giải pháp có khả năng **tăng 308% ROI** và **tiết kiệm 70% ngân sách** so với cách làm truyền thống.

