# chatbot_terminal.py
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Gemini setup
genai.configure(api_key="API KEY")  # Replace with your key
model = genai.GenerativeModel("gemini-2.5-flash")

# Load chunks & embeddings
with open("embeddings/chunks.txt", encoding="utf-8") as f:
    chunks = f.read().split("\n---\n")
embeddings = np.load("embeddings/context_embeddings.npy")

# Load into FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Embedder
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def answer_question(question):
    q_embed = embedder.encode([question])
    _, I = index.search(np.array(q_embed), k=4)
    context = "\n\n".join([chunks[i] for i in I[0]])

    prompt = f"""You are a virtual legal policy advisor designed to help users understand public policies, government regulations, and legal guidelines. You must only answer using the information provided in the official company knowledge below.

    Company Knowledge Base:
    {context}

    User Question: {question}

    If the answer cannot be found in the above context, respond clearly and professionally with:
    "Sorry, I don't have information on that. You may consult a legal expert or contact the appropriate government office for further assistance."

    Please provide clear, accurate, and concise explanations, suitable for a general audience without legal training.
    Answer:"""


    response = model.generate_content(prompt)
    print("\n🔹 Answer:\n" + response.text.strip())

# Terminal loop
if __name__ == "__main__":
    print("💬 Chatbot Ready (type 'exit' to quit)")
    while True:
        q = input("\n🧑 You: ")
        if q.strip().lower() in ["exit", "quit"]:
            break
        answer_question(q)
