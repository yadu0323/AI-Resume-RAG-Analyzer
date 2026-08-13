class IntentDetector:
    def __init__(self):
        self.resume_keywords = {
            "resume",
            "candidate",
            "applicant",
            "experience",
            "education",
            "project",
            "projects",
            "skill",
            "skills",
            "worked",
            "employment",
            "qualification",
            "summary",
            "summarize",
            "github",
            "portfolio",
            "internship",
            "certification",
            "certifications",
            "strength",
            "strengths",
            "weakness",
            "weaknesses"
        }

    def detect(self, question: str) -> str:
        question = question.lower()

        for keyword in self.resume_keywords:
            if keyword in question:
                return "resume"

        return "general"