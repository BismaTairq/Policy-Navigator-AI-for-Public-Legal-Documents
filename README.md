# 🧠 Policy Navigator

**Policy Navigator** is an AI-powered assistant that helps users understand local laws, government policies, and public regulations. It uses a powerful combination of **LLMs (Large Language Models)** and **retrieval-augmented generation (RAG)** to provide answers grounded strictly in scraped, publicly available PDF documents.

---

## 📝 Purpose

Many citizens struggle to interpret legal documents or find answers to everyday policy-related questions. This tool acts as a virtual **legal policy advisor**, enabling users to ask natural language questions and receive AI-generated answers based **only on real, trustworthy public sources**.

Key goals of this project:
- Make public/legal information more accessible
- Answer user questions with context-aware AI
- Prevent hallucinations by grounding answers in retrieved documents

---

## ⚙️ How It Works

1. **Scraping & Chunking**: Publicly available policy docx and csv are scraped and split into readable text chunks.
2. **Embedding**: Each chunk is converted into a vector using `SentenceTransformer`.
3. **Indexing**: Vectors are stored in a FAISS index for efficient retrieval.
4. **LLM (Gemini)**: When a user asks a question, the top relevant chunks are retrieved and passed into Gemini for final answer generation.
---

## 💡 Technologies Used

- **Flask** – Lightweight Python backend
- **SentenceTransformer** – For vector embeddings
- **FAISS** – Fast Approximate Nearest Neighbor search
- **Google Gemini Pro** – LLM for context-aware answering

---

## 🚀 How to Run

1. **Clone the repo**
2. Place your `chunks.txt` and `context_embeddings.npy` in the project directory
3. Set your Gemini API key in the code:
   ```python
   genai.configure(api_key="your-gemini-api-key")


## ⚠️ Disclaimer
Policy Navigator is an informational tool. It does not provide legal advice. Always consult a licensed legal professional for official matters.

## 📄 Example Use Cases
“What is the minimum wage in California?”

“Do I need a permit to renovate my home in New York?”

“Can I vote after a felony conviction in Georgia?”

## 📬 Feedback or Contributions
For suggestions or to contribute new datasets (PDFs), feel free to open an issue or submit a pull request.


