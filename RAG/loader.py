"""
Document Loader

Loads PDF and DOCX resumes and extracts their text.
"""

from pathlib import Path

import fitz
from docx import Document


class DocumentLoader:
    """Loads resume documents and returns plain text."""

    SUPPORTED_FILES = {".pdf", ".docx"}

    def load_document(self, file_path: str) -> str:
        """
        Load a document and extract its text.

        Args:
            file_path: Path to PDF or DOCX file.

        Returns:
            Extracted text.

        Raises:
            FileNotFoundError
            ValueError
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = path.suffix.lower()

        if extension not in self.SUPPORTED_FILES:
            raise ValueError(f"Unsupported file type: {extension}")

        if extension == ".pdf":
            return self._read_pdf(path)

        return self._read_docx(path)

    def _read_pdf(self, path: Path) -> str:
        """Read a PDF file."""

        text = []

        with fitz.open(path) as pdf:
            for page in pdf:
                page_text = page.get_text("text")
                if page_text.strip():
                    text.append(page_text)

        return "\n".join(text)

    def _read_docx(self, path: Path) -> str:
        """Read a DOCX file."""

        document = Document(path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)