import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model globally to avoid reloading multiple times
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
doc_names = []

def load_documents(folder="data/docs"):
    """
    Loads text documents from the specified folder.
    """
    global documents, doc_names
    documents = []
    doc_names = []
    try:
        if not os.path.exists(folder):
            print(f"Directory {folder} does not exist.")
            return
            
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                with open(os.path.join(folder, file), "r") as f:
                    text = f.read()
                    documents.append(text)
                    doc_names.append(file)
    except Exception as e:
        print("Document loading error:", e)

def create_vector_store():
    """
    Creates a FAISS index from the loaded documents.
    """
    try:
        if not documents:
            return None
            
        embeddings = model.encode(documents)
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings).astype('float32'))

        return index
    except Exception as e:
        print("Vector store error:", e)
        return None

def search_docs(query, index):
    """
    Searches the vector store for relevant document chunks.
    """
    try:
        if index is None or not documents:
            return ""
            
        query_vec = model.encode([query])
        distances, indices = index.search(np.array(query_vec).astype('float32'), k=2)

        results = [documents[i] for i in indices[0] if i < len(documents)]
        return "\n---\n".join(results)

    except Exception as e:
        print("Search error:", e)
        return ""
