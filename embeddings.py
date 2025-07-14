# embed_context.py
from sentence_transformers import SentenceTransformer
from docx import Document
import pandas as pd
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load CSV
df = pd.read_csv("data/policy_navigator_qa.csv", encoding="ISO-8859-1").dropna()
csv_data = [f"Q: {q.strip()}\nA: {a.strip()}" for q, a in zip(df["question"], df["answer"])]

# Load DOCX
def read_docx(path):
    doc = Document(path)
    return [p.text.strip() for p in doc.paragraphs if len(p.text.strip()) > 20]

docx_data = read_docx("data/policies.docx")

# Combine
chunks = list(set(csv_data + docx_data))  # remove duplicates

# Save and embed
with open("embeddings/chunks.txt", "w", encoding="utf-8") as f:
    f.write("\n---\n".join(chunks))

embeddings = model.encode(chunks, show_progress_bar=True)
np.save("embeddings/context_embeddings.npy", embeddings)