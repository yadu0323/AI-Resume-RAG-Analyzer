"""
FAISS Vector Store
"""

import faiss
import numpy as np


class VectorStore:
    """
    Stores embeddings in a FAISS index and performs similarity search.
    """

    def __init__(self):
        self.index = None
        self.documents = []

    def build_index(self, embeddings: np.ndarray, documents: list[str]) -> None:
        """
        Build the FAISS index.
        """

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(
            embeddings.astype(np.float32)
        )

        self.documents = documents

    def search(self, query_embedding: np.ndarray, k: int = 3):
        """
        Search the FAISS index.
        """

        scores, indices = self.index.search(
            query_embedding.astype(np.float32),
            k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):
            results.append(
                {
                    "score": float(score),
                    "text": self.documents[idx]
                }
            )

        return results