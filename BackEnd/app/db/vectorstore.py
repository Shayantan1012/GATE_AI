from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import os

VECTOR_DIR = "vector_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vector_store():
    if os.path.exists(VECTOR_DIR):
        return FAISS.load_local(VECTOR_DIR, embedding_model)
    return FAISS.from_texts([], embedding_model)

def save_vector_store(vector_store):
    vector_store.save_local(VECTOR_DIR)
