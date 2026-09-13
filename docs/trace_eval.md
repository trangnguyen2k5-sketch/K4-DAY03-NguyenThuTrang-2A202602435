# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Thu Trang
> **Mã Sinh Viên / Mã Học viên:** 2A202602435
> **Chủ đề Lựa chọn:** *Trợ lý Dịch vụ Khách hàng VinBus:* Tra cứu lộ trình tuyến xe bus điện và đăng ký vé tháng.  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán có yêu cầu chia nhỏ nhiều bước suy luận nối tiếp nhau không? |
| **2. Tool Interaction** | 5 / 5 | Hệ thống có cần kết nối với MCP Server / Cơ sở dữ liệu bên ngoài không? |
| **3. Dynamic Decision** | 4 / 5 | Bước tiếp theo có phụ thuộc vào kết quả quan sát bước trước không? |
| **4. Long Horizon Goal** | 4 / 5 | Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý không? |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tuyến xe bus điện E03 có lộ trình di chuyển và giá vé lượt cụ thể như thế nào?",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "get_route_details",
    "arguments": {
      "route_id": "E03"
    },
    "observation": {
      "status": "SUCCESS",
      "route_id": "E03",
      "data": {
        "route_name": "Tuyến E03: KĐT Mỹ Đình (Hàm Nghi) - KĐT Vinhomes Ocean Park",
        "operating_hours": "05:05 - 21:00 (Tần suất 15-20 phút/chuyến)",
        "single_ticket_price": "9,000 VNĐ/lượt",
        "monthly_single_price": "100,000 VNĐ/tháng",
        "itinerary": "Hàm Nghi -> Nguyễn Hoàng -> Phạm Hùng -> Trần Duy Hưng -> Nguyễn Chí Thanh -> Huỳnh Thúc Kháng -> Thái Hà -> Chùa Bộc -> Phạm Ngọc Thạch -> Đào Duy Anh -> Đại Cổ Việt -> Trần Khát Chân -> Nguyễn Khoái -> Cầu Vĩnh Tuy -> Cổ Linh -> Vinhomes Ocean Park 1."
      }
    },
    "latency_ms": 0.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
