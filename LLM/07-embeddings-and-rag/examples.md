# Examples

## Chatbot tài liệu công ty

Người dùng hỏi: “Chính sách nghỉ phép năm nay thế nào?”

Hệ thống RAG tìm các đoạn trong handbook liên quan đến nghỉ phép, đưa vào prompt, rồi LLM trả lời có căn cứ.

## Tìm kiếm thông minh

Tìm “laptop chạy chậm” có thể trả về bài “cách xử lý máy tính bị đơ” dù không trùng từ khóa chính xác.

## Lỗi thường gặp

Nếu chunk quá dài, retrieval khó chính xác. Nếu chunk quá ngắn, mất ngữ cảnh. Nếu tài liệu sai, RAG vẫn có thể trả lời sai.

