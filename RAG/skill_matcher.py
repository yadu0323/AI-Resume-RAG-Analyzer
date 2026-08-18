class SkillMatcher:

    def extract_skills(self, text: str):

        skills_db = [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "PyTorch",
            "TensorFlow",
            "Scikit-Learn",
            "Pandas",
            "NumPy",
            "OpenCV",
            "Git",
            "GitHub",
            "Docker",
            "Kubernetes",
            "AWS",
            "FastAPI",
            "Flask",
            "SQL",
            "MongoDB",
            "Streamlit"
        ]

        found_skills = []

        text = text.lower()

        for skill in skills_db:
            if skill.lower() in text:
                found_skills.append(skill)

        return found_skills

    def compare(self, resume_text: str, jd_text: str):

        resume_skills = self.extract_skills(resume_text)
        jd_skills = self.extract_skills(jd_text)

        matched = [
            skill for skill in jd_skills
            if skill in resume_skills
        ]

        missing = [
            skill for skill in jd_skills
            if skill not in resume_skills
        ]

        return {
            "matched": matched,
            "missing": missing
        }