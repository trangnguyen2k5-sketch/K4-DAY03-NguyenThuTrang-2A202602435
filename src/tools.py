"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
Chủ đề: Trợ lý Dịch vụ Khách hàng VinBus (Tra cứu lộ trình & Đăng ký vé tháng xe bus điện).
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu thông tin chi tiết lộ trình tuyến xe bus điện VinBus
    {
        "name": "get_route_details",
        "description": "Tra cứu chi tiết lộ trình di chuyển, điểm dừng, thời gian hoạt động và giá vé lượt của tuyến xe bus điện VinBus theo mã tuyến.",
        "parameters": {
            "type": "object",
            "properties": {
                "route_id": {
                    "type": "string",
                    "description": "Mã tuyến xe bus điện VinBus cần tra cứu (ví dụ: 'E01', 'E03', 'E05')."
                }
            },
            "required": ["route_id"]
        }
    },
    
    # Tool 2: Đăng ký vé tháng xe bus điện VinBus
    {
        "name": "register_monthly_pass",
        "description": "Đăng ký thẻ vé tháng xe bus điện VinBus (vé 1 tuyến hoặc vé liên tuyến toàn hệ thống).",
        "parameters": {
            "type": "object",
            "properties": {
                "route_id": {
                    "type": "string",
                    "description": "Mã tuyến đăng ký (ví dụ: 'E01', 'E03') hoặc 'inter_route' đối với vé tháng liên tuyến."
                },
                "customer_name": {
                    "type": "string",
                    "description": "Họ và tên người đăng ký vé tháng."
                },
                "phone": {
                    "type": "string",
                    "description": "Số điện thoại liên hệ của người đăng ký."
                },
                "pickup_location": {
                    "type": "string",
                    "description": "Địa điểm nhận thẻ vé tháng vật lý (ví dụ: 'Times City', 'Smart City', 'Ocean Park 1')."
                },
                "card_type": {
                    "type": "string",
                    "description": "Loại thẻ vé tháng: 'single_route' (1 tuyến cố định) hoặc 'inter_route' (vé liên tuyến tất cả các tuyến)."
                }
            },
            "required": ["customer_name", "phone", "card_type"]
        }
    },

    # Tool 3: Tìm kiếm lộ trình di chuyển nhanh nhất giữa 2 điểm
    {
        "name": "find_best_route",
        "description": "Tìm kiếm lộ trình chuyển tuyến xe bus điện VinBus tối ưu nhất giữa địa điểm xuất phát và điểm đến.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_location": {
                    "type": "string",
                    "description": "Địa điểm xuất phát (ví dụ: 'KĐT Smart City', 'Cầu Giấy')."
                },
                "destination": {
                    "type": "string",
                    "description": "Điểm đến (ví dụ: 'Vinhomes Ocean Park 1', 'Times City')."
                }
            },
            "required": ["start_location", "destination"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "routes": {
        "E01": {
            "route_name": "Tuyến E01: Bến xe Mỹ Đình - KĐT Vinhomes Ocean Park",
            "operating_hours": "05:00 - 21:00 (Tần suất 15-20 phút/chuyến)",
            "single_ticket_price": "8,000 VNĐ/lượt",
            "monthly_single_price": "100,000 VNĐ/tháng",
            "itinerary": "Bến xe Mỹ Đình -> Phạm Hùng -> Khuất Duy Tiến -> Nguyễn Trãi -> Trường Chinh -> Đại La -> Minh Khai -> Cầu Vĩnh Tuy -> Cổ Linh -> Vinhomes Ocean Park 1."
        },
        "E03": {
            "route_name": "Tuyến E03: KĐT Mỹ Đình (Hàm Nghi) - KĐT Vinhomes Ocean Park",
            "operating_hours": "05:05 - 21:00 (Tần suất 15-20 phút/chuyến)",
            "single_ticket_price": "9,000 VNĐ/lượt",
            "monthly_single_price": "100,000 VNĐ/tháng",
            "itinerary": "Hàm Nghi -> Nguyễn Hoàng -> Phạm Hùng -> Trần Duy Hưng -> Nguyễn Chí Thanh -> Huỳnh Thúc Kháng -> Thái Hà -> Chùa Bộc -> Phạm Ngọc Thạch -> Đào Duy Anh -> Đại Cổ Việt -> Trần Khát Chân -> Nguyễn Khoái -> Cầu Vĩnh Tuy -> Cổ Linh -> Vinhomes Ocean Park 1."
        },
        "E05": {
            "route_name": "Tuyến E05: Long Biên - KĐT Vinhomes Smart City",
            "operating_hours": "05:00 - 21:00 (Tần suất 15-20 phút/chuyến)",
            "single_ticket_price": "7,000 VNĐ/lượt",
            "monthly_single_price": "100,000 VNĐ/tháng",
            "itinerary": "Long Biên -> Yên Phụ -> Thanh Niên -> Thụy Khuê -> Văn Cao -> Liễu Giai -> Nguyễn Chí Thanh -> Đại lộ Thăng Long -> KĐT Smart City."
        }
    },
    "inter_route_monthly_price": "200,000 VNĐ/tháng"
}


def execute_get_route_details(route_id: str) -> str:
    """Thực thi tra cứu chi tiết lộ trình tuyến xe bus điện VinBus"""
    route_key = route_id.strip().upper()
    route = MOCK_DATABASE["routes"].get(route_key)
    if route:
        return json.dumps({
            "status": "SUCCESS",
            "route_id": route_key,
            "data": route
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Tuyến xe bus điện '{route_id}' không tồn tại hoặc chưa được đưa vào vận hành trên hệ thống VinBus."
        }, ensure_ascii=False)


def execute_register_monthly_pass(
    customer_name: str,
    phone: str,
    card_type: str = "single_route",
    route_id: str = "E01",
    pickup_location: str = "Times City"
) -> str:
    """Thực thi đăng ký vé tháng xe bus điện VinBus"""
    booking_code = f"VB-PASS-{phone[-4:] if len(phone)>=4 else '0000'}-2026"
    price = MOCK_DATABASE["inter_route_monthly_price"] if card_type == "inter_route" else "100,000 VNĐ/tháng"
    route_desc = "Tất cả các tuyến (Liên tuyến)" if card_type == "inter_route" else f"Tuyến {route_id.upper()}"
    
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": booking_code,
        "customer_name": customer_name,
        "phone": phone,
        "card_type": card_type,
        "route_id": route_id,
        "pickup_location": pickup_location,
        "price": price,
        "message": f"Đăng ký thẻ vé tháng VinBus thành công! Mã đăng ký: {booking_code}. Khách hàng: {customer_name} ({phone}). Phạm vi: {route_desc}. Giá vé: {price}. Địa điểm nhận thẻ: Điểm đón {pickup_location}."
    }, ensure_ascii=False)


def execute_find_best_route(start_location: str, destination: str) -> str:
    """Thực thi tìm kiếm lộ trình kết nối giữa 2 địa điểm"""
    return json.dumps({
        "status": "SUCCESS",
        "start_location": start_location,
        "destination": destination,
        "recommended_route": "Tuyến E05 (từ Smart City đến Nguyễn Chí Thanh) kết hợp chuyển tiếp sang tuyến E03 (đến Vinhomes Ocean Park 1)",
        "estimated_travel_time": "55 phút",
        "fare": "16,000 VNĐ (lượt) hoặc khuyên dùng Thẻ vé tháng liên tuyến (200,000 VNĐ/tháng)",
        "message": f"Lộ trình tối ưu đi từ '{start_location}' đến '{destination}': Đón tuyến E05 chuyển tiếp tuyến E03 tại điểm Nguyễn Chí Thanh để tới {destination}. Thời gian di chuyển ước tính: 55 phút."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "get_route_details": execute_get_route_details,
    "register_monthly_pass": execute_register_monthly_pass,
    "find_best_route": execute_find_best_route
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)

