import requests
import json
import time

BASE_URL = "http://myxza-34-50-170-58.run.pinggy-free.link" # Thay thế URL 

def print_result(title, response):
    """Hàm hỗ trợ in kết quả đẹp mắt."""
    print(f"\n{'='*40}")
    print(f"--- {title} ---")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=4, ensure_ascii=False)}")
    except Exception:
        # in text thô
        print(f"Response: {response.text}")
    print(f"{'='*40}")

def run_tests():
    print("BẮT ĐẦU KIỂM THỬ API")

    # =========================================================================
    # 1. Kiểm tra Endpoint gốc (GET /) [cite: 38]
    # Yêu cầu: Trả về thông tin giới thiệu ngắn gọn
    # =========================================================================
    try:
        res_root = requests.get(f"{BASE_URL}/", timeout=10)
        print_result("1. GET / (Giới thiệu)", res_root)
    except Exception as e:
         print(f"[LỖI] Không thể kết nối GET /: {e}")

    # =========================================================================
    # 2. Kiểm tra Health Check (GET /health) [cite: 39]
    # Yêu cầu: Kiểm tra trạng thái hoạt động
    # =========================================================================
    try:
        res_health = requests.get(f"{BASE_URL}/health", timeout=10)
        print_result("2. GET /health (Trạng thái)", res_health)
    except Exception as e:
         print(f"[LỖI] Không thể kết nối GET /health: {e}")

    # =========================================================================
    # 3. Kiểm tra Sinh văn bản (POST /generate) - Dữ liệu đầu vào 1 [cite: 40, 70]
    # Yêu cầu: Nhận dữ liệu đầu vào, gọi mô hình và trả về JSON rõ ràng
    # =========================================================================
    payload_1 = {
        "prompt": "Trí tuệ nhân tạo (AI) là gì? Hãy giải thích ngắn gọn trong 3 câu."
    }
    print(f"\nĐang gửi Request 1 (Hợp lệ): {json.dumps(payload_1, ensure_ascii=False)}")
    try:
        res_gen_1 = requests.post(f"{BASE_URL}/generate", json=payload_1, timeout=120)
        print_result("3. POST /generate (Dữ liệu hợp lệ 1)", res_gen_1)
    except Exception as e:
        print(f"[LỖI] POST /generate (1) thất bại: {e}")

    # Đợi một chút trước khi gửi request tiếp theo để tránh quá tải
    time.sleep(2)

    # =========================================================================
    # 4. Kiểm tra Sinh văn bản (POST /generate) - Dữ liệu đầu vào 2 [cite: 40, 70]
    # Yêu cầu: Thử nghiệm với ít nhất 2 dữ liệu đầu vào.
    # =========================================================================
    payload_2 = {
        "prompt": "Viết một đoạn mã Python in ra các số từ 1 đến 5."
    }
    print(f"\nĐang gửi Request 2 (Hợp lệ): {json.dumps(payload_2, ensure_ascii=False)}")
    try:
        res_gen_2 = requests.post(f"{BASE_URL}/generate", json=payload_2, timeout=120)
        print_result("4. POST /generate (Dữ liệu hợp lệ 2)", res_gen_2)
    except Exception as e:
        print(f"[LỖI] POST /generate (2) thất bại: {e}")

    # =========================================================================
    # 5. Kiểm tra Xử lý lỗi cơ bản (POST /generate) 
    # Yêu cầu: Kiểm tra dữ liệu đầu vào, xử lý thiếu dữ liệu/sai định dạng
    # =========================================================================
    
    # Lỗi 5.1: Thiếu trường 'prompt'
    payload_error_1 = {}
    print(f"\nĐang gửi Request 3 (Thiếu trường 'prompt'): {json.dumps(payload_error_1, ensure_ascii=False)}")
    try:
        res_err_1 = requests.post(f"{BASE_URL}/generate", json=payload_error_1, timeout=10)
        print_result("5.1 POST /generate (Lỗi: Thiếu 'prompt')", res_err_1)
    except Exception as e:
        print(f"[LỖI] POST /generate (Lỗi 1) thất bại: {e}")

    # Lỗi 5.2: 'prompt' rỗng (chuỗi rỗng)
    payload_error_2 = {
        "prompt": "   " # Chuỗi chỉ chứa khoảng trắng
    }
    print(f"\nĐang gửi Request 4 (Prompt rỗng): {json.dumps(payload_error_2, ensure_ascii=False)}")
    try:
        res_err_2 = requests.post(f"{BASE_URL}/generate", json=payload_error_2, timeout=10)
        print_result("5.2 POST /generate (Lỗi: Prompt rỗng)", res_err_2)
    except Exception as e:
        print(f"[LỖI] POST /generate (Lỗi 2) thất bại: {e}")

    print("\nKẾT THÚC KIỂM THỬ API")

if __name__ == "__main__":
    run_tests()