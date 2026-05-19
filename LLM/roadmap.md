# Roadmap Học AI Và LLM Cho Người Mới

Roadmap này giúp bạn đi từ nền tảng đến khả năng hiểu, dùng, và xây dựng ứng dụng với LLM.

Mục tiêu không phải là học thuộc tất cả thuật ngữ. Mục tiêu là sau mỗi giai đoạn, bạn có thể giải thích được khái niệm bằng lời của mình, nhận ra nó trong sản phẩm thật, và làm được một bài thực hành nhỏ.

## Tổng Quan Lộ Trình

1. AI và Machine Learning nền tảng
2. Python và toán cơ bản cho Machine Learning
3. Neural Network
4. NLP cơ bản
5. Transformer và Attention
6. LLM internals
7. Prompting và sử dụng LLM
8. Embeddings và RAG
9. Agents và Tools
10. Evaluation, Safety, Security
11. Production và chủ đề nâng cao

---

## 1. AI Và Machine Learning Nền Tảng

### Mục tiêu

Hiểu AI là gì, Machine Learning là gì, và vì sao model có thể học từ dữ liệu.

### Cần học

- `Artificial Intelligence`
- `Machine Learning`
- `Deep Learning`
- `Model`
- `Dataset`
- `Training`
- `Inference`
- `Label`
- `Feature`
- `Loss Function`
- `Overfitting`
- `Generalization`

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Giải thích sự khác nhau giữa AI, Machine Learning, Deep Learning, và LLM.
- Hiểu model không “biết” theo kiểu con người, mà học mẫu từ dữ liệu.
- Biết vì sao dữ liệu huấn luyện ảnh hưởng rất lớn đến chất lượng model.
- Nhận ra khi nào model đang học thật và khi nào có thể đang overfit.

### Bài thực hành gợi ý

- Dùng `scikit-learn` để train một model phân loại đơn giản.
- Chia dữ liệu thành train/test set.
- So sánh kết quả trên dữ liệu train và dữ liệu test.

---

## 2. Python Và Toán Cơ Bản Cho Machine Learning

### Mục tiêu

Có đủ nền Python và toán trực giác để đọc hiểu tài liệu Machine Learning mà không bị “ngợp”.

### Cần học

- Python cơ bản
- `numpy`
- Vector
- Matrix
- Dot product
- Probability cơ bản
- Logarithm
- Derivative trực giác
- Gradient trực giác

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Hiểu vector là danh sách số biểu diễn dữ liệu.
- Hiểu dot product dùng để đo mức liên quan giữa hai vector.
- Hiểu gradient là hướng giúp model điều chỉnh để giảm sai số.
- Đọc code Machine Learning đơn giản mà không bị kẹt ở cú pháp hoặc ký hiệu toán.

### Bài thực hành gợi ý

- Viết hàm tính dot product bằng Python.
- Dùng `numpy` để tính cosine similarity giữa hai vector.
- Tự implement linear regression rất đơn giản.
- Vẽ biểu đồ loss giảm dần qua từng bước gradient descent.

---

## 3. Neural Network

### Mục tiêu

Hiểu cách neural network biến input thành output và học bằng cách điều chỉnh parameter.

### Cần học

- `Neural Network`
- `Layer`
- `Parameter`
- `Weight`
- `Bias`
- `Activation Function`
- `Forward Pass`
- `Backpropagation`
- `Gradient Descent`
- `Learning Rate`
- `Epoch`
- `Batch`

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Giải thích neural network như một chuỗi layer xử lý dữ liệu.
- Hiểu parameter/weight là các giá trị được học trong training.
- Hiểu loss giảm bằng cách điều chỉnh weight.
- Biết learning rate quá cao hoặc quá thấp có thể làm training kém.

### Bài thực hành gợi ý

- Dùng PyTorch train một neural network nhỏ.
- Thử thay đổi learning rate và quan sát kết quả.
- Train model phân loại ảnh đơn giản như MNIST.

---

## 4. NLP Cơ Bản

### Mục tiêu

Hiểu cách máy tính xử lý ngôn ngữ trước khi đến LLM hiện đại.

### Cần học

- `Natural Language Processing`
- Text preprocessing
- Tokenization
- Vocabulary
- One-hot encoding
- Word embedding
- Sequence
- Language model
- Next-word prediction

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Hiểu vì sao văn bản phải được biến thành số.
- Biết tokenization là bước chia văn bản thành đơn vị nhỏ hơn.
- Hiểu embedding giúp biểu diễn ý nghĩa gần/xa giữa các từ hoặc câu.
- Hiểu language model là model dự đoán hoặc sinh ngôn ngữ.

### Bài thực hành gợi ý

- Tự viết tokenizer đơn giản bằng cách tách từ.
- Đếm vocabulary trong một đoạn văn bản.
- Dùng embedding để tìm các câu có nghĩa gần nhau.

---

## 5. Transformer Và Attention

### Mục tiêu

Hiểu kiến trúc quan trọng đứng sau nhiều LLM hiện đại.

### Cần học

- `Transformer`
- `Attention`
- `Self-Attention`
- `Query`
- `Key`
- `Value`
- `Positional Encoding`
- `Feed-forward Layer`
- `Residual Connection`
- `Layer Normalization`

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Giải thích attention là cơ chế giúp model chọn phần quan trọng trong ngữ cảnh.
- Hiểu self-attention xem xét quan hệ giữa các token trong cùng một câu.
- Biết vì sao model cần positional encoding để hiểu thứ tự.
- Có trực giác rằng Transformer mạnh vì nó xử lý quan hệ dài trong văn bản tốt.

### Bài thực hành gợi ý

- Đọc và vẽ lại sơ đồ Transformer bằng lời của bạn.
- Tự viết một hàm attention rất nhỏ bằng `numpy`.
- Quan sát attention trên một câu đơn giản nếu dùng thư viện hỗ trợ visualization.

---

## 6. LLM Internals

### Mục tiêu

Hiểu LLM sinh câu trả lời như thế nào và những thành phần cốt lõi bên trong LLM.

### Cần học

- `Large Language Model`
- `Token`
- `Tokenizer`
- `Context Window`
- `Next-token Prediction`
- `Pretraining`
- `Instruction Tuning`
- `Post-training`
- `RLHF`
- `Sampling`
- `Temperature`
- `Top-p`
- `Hallucination`

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Hiểu LLM sinh văn bản bằng cách dự đoán token tiếp theo.
- Biết context window giới hạn lượng thông tin model có thể nhìn thấy.
- Hiểu tokenizer ảnh hưởng đến chi phí, độ dài prompt, và cách model đọc văn bản.
- Biết hallucination là giới hạn tự nhiên cần được thiết kế để giảm thiểu.

### Bài thực hành gợi ý

- Dùng tokenizer để xem một câu được chia thành token như thế nào.
- Gửi cùng một prompt với nhiều temperature khác nhau và so sánh output.
- Thử hỏi model một câu không có đủ ngữ cảnh và quan sát nguy cơ hallucination.

---

## 7. Prompting Và Sử Dụng LLM

### Mục tiêu

Biết cách giao việc rõ ràng cho LLM và kiểm soát định dạng output.

### Cần học

- `Prompt`
- `System Prompt`
- `User Prompt`
- `Prompt Engineering`
- `Zero-shot Prompting`
- `Few-shot Prompting`
- `Structured Output`
- JSON output
- Role prompting
- Context management

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Viết prompt rõ mục tiêu, ngữ cảnh, ràng buộc, và định dạng kết quả.
- Biết khi nào cần đưa ví dụ cho model.
- Yêu cầu model trả về JSON hoặc cấu trúc dễ parse.
- Tránh prompt quá mơ hồ gây output khó dùng.

### Bài thực hành gợi ý

- Viết prompt tóm tắt tài liệu.
- Viết prompt trích xuất thông tin thành JSON.
- So sánh output giữa prompt mơ hồ và prompt có cấu trúc.

---

## 8. Embeddings Và RAG

### Mục tiêu

Biết cách cho LLM trả lời dựa trên tài liệu hoặc dữ liệu riêng.

### Cần học

- `Embedding`
- `Vector`
- `Semantic Similarity`
- `Vector Database`
- `Retrieval`
- `Chunking`
- `RAG`
- `Grounding`
- `Re-ranking`
- Citation

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Hiểu embedding biến văn bản thành vector mang ý nghĩa.
- Hiểu vector search tìm theo nghĩa, không chỉ theo từ khóa.
- Biết RAG gồm bước tìm tài liệu rồi đưa tài liệu vào prompt.
- Hiểu vì sao chunking ảnh hưởng mạnh đến chất lượng câu trả lời.
- Biết RAG không tự đảm bảo đúng nếu tài liệu sai hoặc retrieval kém.

### Bài thực hành gợi ý

- Tạo embedding cho nhiều đoạn văn bản.
- Tìm đoạn gần nghĩa nhất với một câu hỏi.
- Xây chatbot hỏi đáp trên một vài file Markdown.
- Thử thay đổi chunk size và so sánh kết quả.

---

## 9. Agents Và Tools

### Mục tiêu

Hiểu cách LLM dùng công cụ và thực hiện tác vụ nhiều bước.

### Cần học

- `Tool Calling`
- `Function Calling`
- `Agent`
- `Workflow`
- `Planning`
- `Memory`
- `Human-in-the-loop`
- Tool permission
- Failure recovery

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Hiểu tool calling giúp LLM vượt giới hạn “chỉ sinh văn bản”.
- Phân biệt agent tự do với workflow có kiểm soát.
- Biết vì sao agent cần giới hạn quyền và kiểm tra kết quả.
- Thiết kế được một flow đơn giản có bước con người phê duyệt.

### Bài thực hành gợi ý

- Tạo một tool tính toán đơn giản cho LLM gọi.
- Xây assistant đọc file và trả lời câu hỏi.
- Tạo workflow gồm các bước: đọc dữ liệu, tóm tắt, tạo checklist, chờ duyệt.

---

## 10. Evaluation, Safety, Security

### Mục tiêu

Biết cách kiểm tra chất lượng và rủi ro của hệ thống LLM.

### Cần học

- `Evaluation`
- `Evals`
- `Benchmark`
- `Guardrails`
- `Bias`
- `Prompt Injection`
- `Data Leakage`
- `Privacy`
- `Red Teaming`
- Refusal behavior
- Groundedness

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Tạo bộ câu hỏi test cho chatbot hoặc ứng dụng LLM.
- Đánh giá câu trả lời theo độ đúng, độ đầy đủ, và độ bám nguồn.
- Nhận ra prompt injection trong tài liệu hoặc input người dùng.
- Biết dữ liệu nhạy cảm cần được bảo vệ ở nhiều lớp, không chỉ bằng prompt.

### Bài thực hành gợi ý

- Viết 50 câu test cho một chatbot RAG.
- Chấm câu trả lời theo thang điểm đơn giản.
- Thêm test cho trường hợp model phải nói “không biết”.
- Thử các prompt injection cơ bản trong môi trường an toàn.

---

## 11. Production Và Chủ Đề Nâng Cao

### Mục tiêu

Hiểu những vấn đề xuất hiện khi đưa LLM vào sản phẩm thật.

### Cần học

- `Latency`
- `Throughput`
- `Cost per Token`
- Logging
- Monitoring
- Rate limit
- Caching
- Fallback model
- `Fine-tuning`
- `Distillation`
- `Quantization`
- `Multimodal Model`
- `Mixture of Experts`

### Kết quả mong đợi

Sau phần này, bạn nên có thể:

- Biết chất lượng model chỉ là một phần của sản phẩm AI.
- Ước lượng chi phí dựa trên token input/output.
- Hiểu vì sao latency ảnh hưởng mạnh đến trải nghiệm người dùng.
- Biết khi nào nên dùng RAG, khi nào có thể cân nhắc fine-tuning.
- Có cái nhìn tổng quan về tối ưu model và triển khai thực tế.

### Bài thực hành gợi ý

- Ghi log token usage và thời gian phản hồi.
- Thử cache câu trả lời cho câu hỏi lặp lại.
- So sánh model lớn và model nhỏ trên cùng một bộ eval.
- Viết checklist production readiness cho một app LLM.

---

## Dự Án Tổng Hợp Đề Xuất

Sau khi học các giai đoạn trên, bạn nên làm một project nhỏ nhưng đầy đủ:

### Project: Chatbot Hỏi Đáp Tài Liệu Cá Nhân

Yêu cầu:

- Đọc nhiều file Markdown hoặc PDF.
- Chia tài liệu thành chunk.
- Tạo embedding.
- Tìm đoạn liên quan khi người dùng hỏi.
- Dùng LLM trả lời dựa trên nguồn.
- Trả lời “không biết” nếu tài liệu không có thông tin.
- Có bộ eval ít nhất 30 câu hỏi.
- Ghi log latency và token cost.

### Kết quả mong đợi của project

Khi hoàn thành, bạn sẽ hiểu được gần như toàn bộ flow thực tế của một ứng dụng LLM:

- Dữ liệu đi vào hệ thống như thế nào.
- LLM dùng ngữ cảnh ra sao.
- RAG giảm hallucination như thế nào.
- Evaluation giúp phát hiện lỗi ra sao.
- Production cần theo dõi chi phí và tốc độ thế nào.

---

## Checklist Tự Đánh Giá

Bạn có thể xem mình đã “hiểu LLM ở mức căn bản tốt” nếu trả lời được các câu này:

- LLM khác search engine như thế nào?
- Vì sao LLM có thể hallucinate?
- Token ảnh hưởng đến chi phí và context ra sao?
- Embedding dùng để làm gì?
- RAG khác fine-tuning như thế nào?
- Tool calling giúp LLM làm được gì?
- Prompt injection nguy hiểm ở đâu?
- Làm sao biết một chatbot LLM đang tốt lên hay tệ đi?
- Khi đưa LLM vào production, cần theo dõi những chỉ số nào?

