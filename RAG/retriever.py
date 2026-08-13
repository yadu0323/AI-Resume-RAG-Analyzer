"""
Retriever

Searches the vector database and returns the most relevant chunks.
"""

from RAG.embeddings import EmbeddingGenerator
from RAG.vectorstore import VectorStore


class Retriever:
    def __init__(
        self,
        embedder: EmbeddingGenerator,
        vectorstore: VectorStore
    ):
        self.embedder = embedder
        self.vectorstore = vectorstore

    def retrieve(self, question: str, k: int = 3):
        """
        Retrieve the most relevant chunks.

        Returns:
            {
                "context": "...",
                "score": 0.81,
                "results": [...]
            }
        """

        query_embedding = self.embedder.embed_text(question).reshape(1, -1)

        results = self.vectorstore.search(
            query_embedding,
            k=k
        )

        context = "\n\n".join(
            result["text"]
            for result in results
        )

        highest_score = results[0]["score"] if results else 0.0

        return {
            "context": context,
            "score": highest_score,
            "results": results
        }