"""
Intent Classifier
"""

from RAG.llm import OllamaLLM


class IntentClassifier:
    def __init__(self):
        self.llm = OllamaLLM()

    def classify(self, question: str) -> str:
        prompt = f"""
You are an intent classifier.

Determine whether the user's question is asking about
the uploaded resume or is a general question.

Rules:
- Return ONLY one word.
- Allowed outputs:
resume
general

Question:
{question}
"""

        result = self.llm.generate(prompt)

        result = result.strip().lower()

        if "resume" in result:
            return "resume"

        return "general"