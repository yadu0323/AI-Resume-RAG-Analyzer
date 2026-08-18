from RAG.jd_matcher import JDMatcher

matcher = JDMatcher()

resume = """
Python developer with machine learning,
deep learning and NLP experience.
"""

jd = """
Looking for a Python ML Engineer
with NLP and Deep Learning skills.
"""

score = matcher.match(
    resume,
    jd
)

print(f"Match Score: {score}%")