from sentence_transformers import SentenceTransformer

class FinancialEmbeddings:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a list of texts.
        """
        return self.model.encode(texts, convert_to_tensor=True)

# Example usage
embedding_model = FinancialEmbeddings()
