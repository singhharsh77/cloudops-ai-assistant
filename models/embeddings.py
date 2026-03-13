from sentence_transformers import SentenceTransformer

def get_embedding_model():
    """
    Returns a lightweight embedding model.
    """
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        return model
    except Exception as e:
        print("Embedding model error:", e)
        return None
