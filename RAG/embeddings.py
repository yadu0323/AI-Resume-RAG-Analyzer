"""
Embedding Generator
"""

from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingGenerator:
    """
    Generate embeddings for text using BGE.
    """

    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def embed_text(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text.
        """
        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding

    def embed_documents(self, documents: list[str]) -> np.ndarray:
        """
        Generate embeddings for multiple chunks.
        """
        embeddings = self.model.encode(
            documents,
            normalize_embeddings=True
        )

        return embeddings