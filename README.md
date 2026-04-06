# Bài Thực Hành 1: Application Programming Interface

## 1. Thông tin sinh viên
- **Họ và tên:** Trần Ngọc Gia Hân
- **MSSV:** 24120178
- **Lớp:** Tư duy tính toán 24CTT3

## 2. Thông tin mô hình
- **Tên mô hình:** Qwen2.5-0.5B
- **Liên kết Hugging Face:** [https://huggingface.co/Qwen/Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B)

## 3. Mô tả ngắn về chức năng của hệ thống
Hệ thống cung cấp một Web API trung gian được xây dựng bằng cấu trúc FastAPI để giao tiếp với mô hình ngôn ngữ lớn Qwen2.5-0.5B (chạy qua nền tảng Ollama). Hệ thống cho phép người dùng gửi các yêu cầu bằng văn bản (prompt) dưới định dạng JSON, sau đó gọi mô hình để xử lý sinh văn bản và trả về kết quả cuối cùng cũng dưới định dạng JSON.

## 4. Hướng dẫn cài đặt thư viện
Hệ thống yêu cầu cài đặt Ollama và các thư viện Python liên quan. 
Để cài đặt, hãy mở terminal và chạy lệnh sau (hoặc chạy qua Cell trong Google Colab):

pip install fastapi nest-asyncio uvicorn omegaconf requests pydantic

## 5. Hướng dẫn chạy chương trình
Dự án được tối ưu hóa để triển khai trên Google Colab với cấu hình T4 GPU.

1. Upload file Notebook (`.ipynb`) chứa source code lên Google Colab.
2. Thiết lập môi trường: Chọn **Runtime** -> **Change runtime type** -> **T4 GPU**.
3. Chạy tuần tự các Cell từ trên xuống dưới để thực hiện:
   - Cài đặt hệ sinh thái Ollama và thư viện Python.
   - Kéo (pull) trọng số của mô hình `qwen2.5:0.5b` về máy.
   - Tạo file cấu hình `config.yaml`.
   - Khởi chạy máy chủ FastAPI chạy ngầm tại port 8000.
4. Ở Cell cuối cùng, chạy lệnh mở đường hầm (tunnel) bằng Pinggy (`!ssh -T -o StrictHostKeyChecking=no ...`).
5. Copy đường link Public URL do Pinggy cấp (Ví dụ: `https://xxxx.a.free.pinggy.link`) để làm `BASE_URL` khi gọi API.

## 6. Hướng dẫn gọi API và ví dụ request/response
Sử dụng Public URL (`BASE_URL`) lấy được từ bước 5 để kiểm thử.

**6.1. Endpoint Kiểm tra trạng thái (GET /health)**
- **Mô tả:** Kiểm tra xem hệ thống API có đang hoạt động ổn định hay không.
- **Ví dụ Request:**
GET [BASE_URL]/health
- **Ví dụ Response:**
{
  "status": "API is up and running"
}

**6.2. Endpoint Sinh văn bản (POST /generate)**
- **Mô tả:** Gửi yêu cầu đầu vào dạng văn bản để mô hình tiến hành suy luận và trả lời.
- **Ví dụ Request:**
POST [BASE_URL]/generate
Content-Type: application/json

{
  "prompt": "Trí tuệ nhân tạo (AI) là gì? Hãy giải thích ngắn gọn trong 2 câu."
}
- **Ví dụ Response:**
{
  "result": "Trí tuệ nhân tạo (AI) là một lĩnh vực của khoa học máy tính tập trung vào việc tạo ra các hệ thống thông minh có khả năng thực hiện các tác vụ thường đòi hỏi trí tuệ của con người. Những tác vụ này bao gồm học tập, lý luận, giải quyết vấn đề và hiểu ngôn ngữ tự nhiên."
}

## 7. Video demo

<p align="center">
  <a href="https://youtu.be/dSWQBkTsDvg">
    <img src="https://img.youtube.com/vi/dSWQBkTsDvg/0.jpg" width="600">
  </a>
</p>

<h2 align="center">Link video: https://youtu.be/dSWQBkTsDvg</h2>


