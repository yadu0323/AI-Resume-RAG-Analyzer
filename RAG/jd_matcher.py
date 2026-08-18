from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class JDMatcher:

    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def match(self, resume_text: str, jd_text: str):

        resume_embedding = self.model.encode(
            [resume_text]
        )

        jd_embedding = self.model.encode(
            [jd_text]
        )

        score = cosine_similarity(
            resume_embedding,
            jd_embedding
        )[0][0]

        return round(float(score) * 100, 2)