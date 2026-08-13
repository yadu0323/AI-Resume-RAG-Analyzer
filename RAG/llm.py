"""
Ollama LLM Client
"""

import requests


class OllamaLLM:
    def __init__(
        self,
        model: str = "qwen2.5-coder:7b",
        base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.url = f"{base_url}/api/generate"

    def generate(self, prompt: str) -> str:
        """
        Generate a response using Ollama.
        """

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        response.raise_for_status()

        return response.json()["response"].strip()