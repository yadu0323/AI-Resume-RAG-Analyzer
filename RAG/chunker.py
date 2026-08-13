"""
Text Chunker

Splits cleaned resume text into overlapping chunks.
"""


class TextChunker:
    def __init__(self, chunk_size: int = 400, overlap: int = 80):
        if overlap >= chunk_size:
            raise ValueError("Overlap must be smaller than chunk size.")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> list[str]:
        """
        Split text into overlapping chunks.
        """

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size

            chunks.append(text[start:end])

            start += self.chunk_size - self.overlap

        return chunks