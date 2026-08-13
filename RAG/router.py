"""
Router

Routes questions either to Resume RAG or the general LLM.
"""

from RAG.classifier import IntentClassifier


class Router:
    def __init__(self, threshold: float = 0.65):
        self.threshold = threshold
        self.classifier = IntentClassifier()

    def route(self, question: str, similarity_score: float) -> str:
        """
        Decide whether to use Resume RAG or General LLM.
        """

        intent = self.classifier.classify(question)

        if similarity_score >= self.threshold and intent == "resume":
            return "resume"

        return "general"