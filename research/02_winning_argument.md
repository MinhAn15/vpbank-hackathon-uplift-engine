# Luận Cứ Chiến Thắng: Từ Predictive đến Prescriptive AI

* **Assigned to:** [Tên ML Scientist]
* **Status:** In Progress

---

## 1. Sự khác biệt cốt lõi

Hầu hết các hệ thống hiện tại là **Predictive (Dự đoán)**. Chúng trả lời câu hỏi:
> *Ai có khả năng sẽ chuyển đổi?*

Hệ thống **Uplift Engine** của chúng ta là **Prescriptive (Chỉ định)**. Nó trả lời câu hỏi quan trọng hơn nhiều về mặt kinh doanh:
> *Chúng ta nên tác động vào ai để tối đa hóa lợi nhuận?*

Đây là sự thay đổi từ việc quan sát sang việc hành động có chủ đích.

## 2. Ma trận phân loại khách hàng

Chúng ta phân loại khách hàng dựa trên Tác động thuần (Incremental Uplift):

| Nhóm Khách Hàng         | Hành Động Của Uplift Engine                        | Lý Do Kinh Doanh                          |
| :---------------------- | :------------------------------------------------- | :---------------------------------------- |
| **Persuadables** | ✅ **NHẮM MỤC TIÊU** (Target)                      | Đây là nguồn ROI duy nhất của chiến dịch. |
| **Sure Things** | 🚫 **BỎ QUA** (Do Not Target)                      | Tiết kiệm chi phí, bảo vệ NIM.            |
| **Lost Causes** | 🚫 **BỎ QUA** (Do Not Target)                      | Tiết kiệm chi phí, tránh lãng phí.         |
| **Sleeping Dogs** | 🚫 **TUYỆT ĐỐI TRÁNH** (Actively Avoid) | Tránh làm phiền, giảm Churn Rate.     |

Ma trận này là trái tim trong bài trình bày của chúng ta.