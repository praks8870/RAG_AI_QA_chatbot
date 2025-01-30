import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.embeddings = None
        self.text_chunks = []
        self.index = None

    def add_text_chunks(self, text_chunks):
        """Convert text chunks to embeddings and store them in FAISS."""
        if not text_chunks:
            print("❌ No text chunks to embed!")
            return
        
        self.text_chunks = text_chunks
        self.embeddings = self.model.encode(text_chunks, convert_to_numpy=True)
        
        if self.embeddings.shape[0] == 0:
            print("❌ No embeddings created!")
            return

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings, dtype=np.float32))

    def search(self, query, top_k=3):
        """Retrieve relevant text chunks for a given query."""
        if self.index is None or self.index.ntotal == 0:
            print("❌ No embeddings available for search!")
            return []
        
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        return [self.text_chunks[idx] for idx in indices[0]]

