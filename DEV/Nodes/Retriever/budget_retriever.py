from DEV.Embedding.financial_embeddings import FinancialEmbeddings

class BudgetRetriever:
    def __init__(self, financial_data: list[str]):
        self.embedding_model = FinancialEmbeddings()
        self.data = financial_data
        self.embeddings = self.embedding_model.encode(financial_data)

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        """
        Retrieve the top-k most relevant pieces of financial data for a given query.
        """
        query_embedding = self.embedding_model.encode([query])
        similarities = [
            (i, (embedding @ query_embedding.T).item())
            for i, embedding in enumerate(self.embeddings)
        ]
        top_indices = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
        return [self.data[i[0]] for i in top_indices]

# Example data
financial_data = [
    "Save at least 20% of your income",
    "Cut discretionary spending",
    "Invest in low-risk mutual funds"
]

retriever = BudgetRetriever(financial_data)
results = retriever.retrieve("How to save more?")
print(results)
