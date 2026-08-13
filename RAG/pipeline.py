from RAG.loader import DocumentLoader
from RAG.cleaner import TextCleaner
from RAG.chunker import TextChunker
from RAG.embeddings import EmbeddingGenerator
from RAG.vectorstore import VectorStore
from RAG.retriever import Retriever
# from RAG.router import Router
from RAG.llm import OllamaLLM
from RAG.prompts import SYSTEM_PROMPT
from RAG.intent import IntentDetector


class ResumeRAGPipeline:
    def __init__(self):
        self.loader = DocumentLoader()
        self.cleaner = TextCleaner()
        self.chunker = TextChunker()

        self.embedder = EmbeddingGenerator()
        self.vectorstore = VectorStore()

        self.retriever = Retriever(
            self.embedder,
            self.vectorstore
        )

        # self.router = Router()
        self.intent_detector = IntentDetector()

        self.llm = OllamaLLM()

    def load_resume(self, path: str):
        """
        Load a resume and build the vector database.
        """

        text = self.loader.load_document(path)

        text = self.cleaner.clean(text)

        chunks = self.chunker.split_text(text)

        embeddings = self.embedder.embed_documents(chunks)

        self.vectorstore.build_index(embeddings,chunks)

    def ask(self, question: str):

        intent = self.intent_detector.detect(question)

        if intent == "general":

            answer = self.llm.generate(question)

            return {
                "intent": "general",
                "score": None,
                "answer": answer
            }

        retrieved = self.retriever.retrieve(question)

        prompt = SYSTEM_PROMPT.format(context=retrieved["context"],question=question)
        answer = self.llm.generate(prompt)

        return {
            "intent": "resume",
            "score": retrieved["score"],
            "answer": answer
        }