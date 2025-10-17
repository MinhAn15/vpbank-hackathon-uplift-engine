# Technical Deep Dive: Uplift Modeling & Causal AI

Assigned to: [Tên thành viên C]

## Nội dung cần thu thập

## Mẫu code (gợi ý)
 "Vũ Khí" Kỹ Thuật: Causal Forest & Qini Curve

* **Assigned to:** [Tên ML Scientist]
* **Status:** In Progress

---

## 1. Lựa chọn thuật toán: Causal Forest

Sau khi nghiên cứu, chúng ta quyết định chọn **Causal Forest** (từ thư viện `causalml` hoặc `econml` trên Python).

* **Lý do lựa chọn:**
	* **Hiệu quả:** Được thiết kế đặc biệt để ước lượng CATE (Uplift Score) cho từng cá nhân.
	* **Mạnh mẽ:** Xử lý tốt dữ liệu có nhiều chiều (nhiều features), tìm ra các mối quan hệ phi tuyến tính phức tạp.
	* **Sẵn có:** Có các implementation chất lượng cao, sẵn sàng cho production.

## 2. Thước đo thành công: Qini Curve

Chúng ta sẽ không dùng AUC-ROC hay F1-Score. Thước đo của chúng ta là **Qini Curve**.

* **Cách diễn giải:** Đường cong Qini càng cao, mô hình của chúng ta càng hiệu quả trong việc tìm ra nhóm "Persuadables" so với việc nhắm mục tiêu ngẫu nhiên. Nó trực tiếp đo lường lợi ích kinh doanh gia tăng.

* **Gợi ý code (để tham khảo):**
	```python
	from causalml.metrics import plot_qini
	# Giả sử 'preds' là uplift score từ mô hình
	plot_qini(preds, treatment, outcome)
	```