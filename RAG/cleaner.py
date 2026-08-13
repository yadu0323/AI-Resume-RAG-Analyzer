"""
Text Cleaner

Cleans extracted resume text.
"""

import re


class TextCleaner:
    """Clean extracted resume text."""

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean extracted text.

        Args:
            text: Raw extracted text.

        Returns:
            Cleaned text.
        """

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]+", " ", text)

        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Remove extra blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()