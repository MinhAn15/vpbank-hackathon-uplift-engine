# AWS Architecture Choices

Assigned to: [Tên thành viên D]

## Lý do chọn dịch vụ (viết 2-3 gạch đầu dòng cho mỗi dịch vụ)
# Luận Cứ Kiến Trúc AWS: Tối ưu cho Tốc độ, Quy mô và Quản trị

* **Assigned to:** [Tên Cloud Engineer]
* **Status:** In Progress

---

## Checklist lựa chọn dịch vụ:

- [x] **Data Ingestion:** `Amazon Kinesis` (real-time) & `AWS Glue` (batch) -> `S3 Data Lake`
	* *Lý do:* Kiến trúc chuẩn, linh hoạt, và chi phí hiệu quả cho việc thu thập dữ liệu đa dạng.

- [x] **Feature Management:** `SageMaker Feature Store`
	* *Lý do:* Đây là lựa chọn **then chốt**. Nó giải quyết triệt để bài toán **training-serving skew**, đảm bảo tính nhất quán của feature. Đây là một điểm khác biệt ở cấp độ "Senior".

- [x] **ML Training & Deployment:** `AWS Step Functions` + `SageMaker Training/Endpoints`
	* *Lý do:* Step Functions giúp tự động hóa và điều phối (orchestrate) toàn bộ pipeline MLOps, mang lại tính minh bạch và khả năng lặp lại.

- [x] **Real-time Inference API:** `API Gateway` -> `Lambda` -> `SageMaker Endpoint`
	* *Lý do:* Kiến trúc Serverless tối ưu cho độ trễ thấp (<100ms), khả năng tự động co giãn và mô hình trả phí theo lần dùng (pay-per-use).

- [x] **BI & Analytics:** `Amazon Athena` & `Amazon QuickSight`
	* *Lý do:* Cho phép truy vấn dữ liệu trực tiếp trên S3 Data Lake mà không cần di

## Notes
- Expected env vars: `AWS_REGION`, `S3_BUCKET`, `MODEL_S3_PATH`
- Outline minimal IAM permissions required for prototypes.
- Outline minimal IAM permissions required for prototypes.