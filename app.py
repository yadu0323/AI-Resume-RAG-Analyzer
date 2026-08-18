import streamlit as st
from RAG.pipeline import ResumeRAGPipeline
from RAG.chat_memory import ChatMemory
from RAG.jd_matcher import JDMatcher
from RAG.skill_matcher import SkillMatcher

st.set_page_config(
    page_title="Resume RAG Analyzer",
    page_icon="📄",
    layout="wide"
)
memory = ChatMemory()

if "pipeline" not in st.session_state:
    st.session_state.pipeline = ResumeRAGPipeline()
    
if "skill_matcher" not in st.session_state:
    st.session_state.skill_matcher = SkillMatcher()

if "matcher" not in st.session_state:
    st.session_state.matcher = JDMatcher()

if "resume_loaded" not in st.session_state:
    st.session_state.resume_loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = memory.load()

st.title("📄 Resume RAG Analyzer")
with st.sidebar:

    st.title("Resume RAG")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader("📋 JD Matcher")
    jd_text = st.text_area("Paste Job Description",height=250)
    
    check_match = st.button("Check Match")

    if st.session_state.resume_loaded:
        st.success("✅ Resume Loaded")
    else:
        st.warning("⚠️ No Resume Uploaded")


uploaded_file = st.file_uploader("Upload Resume",type=["pdf"])

if uploaded_file and not st.session_state.resume_loaded:

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.pipeline.load_resume(save_path)

    st.session_state.resume_loaded = True

    st.success("Resume uploaded successfully!")

if check_match:

    if not st.session_state.resume_loaded:
        st.error("Upload a resume first.")

    elif not jd_text.strip():
        st.error("Paste a Job Description.")

    else:

        score = st.session_state.matcher.match(
            st.session_state.pipeline.resume_text,
            jd_text
        )
        skills = st.session_state.skill_matcher.compare(
        st.session_state.pipeline.resume_text,
        jd_text
        )

        with st.expander(
            "📊 JD Match Result",
            expanded=True
        ):

            st.metric(
                "Match Score",
                f"{score}%"
            )

            st.progress(score / 100)

            if score >= 80:
                st.success("✅ Strong Candidate - Recommended for Interview")

            elif score >= 60:
                st.warning("⚠️ Moderate Match - Review Resume Manually")

            else:
                st.error("❌ Low Match - Not Recommended")

            st.markdown("### ✅ Matched Skills")

            if skills["matched"]:
                for skill in skills["matched"]:
                    st.write(f"✓ {skill}")

            else:
                st.write("No matching skills found.")

            st.markdown("### ❌ Missing Skills")

            if skills["missing"]:
                for skill in skills["missing"]:
                    st.write(f"✗ {skill}")

            else:
                st.write("No missing skills.")

            summary = f"""
            Candidate matches {len(skills['matched'])} required skills and is missing {len(skills['missing'])} skills.
            Strong areas:
            {", ".join(skills['matched'][:6])}

            Missing:
            {", ".join(skills['missing'])}
            """
            st.info(summary)

            st.markdown("## 📧 Candidate Communication")
            candidate_email = st.text_input(
            "Candidate Email"
              )
            if st.button("Generate Interview Email"):
                email_body = f"""
                Subject: Interview Invitation

                Dear Candidate,

                We reviewed your resume and would like to invite you for an interview.

                Your profile achieved a match score of {score:.2f}% against our job requirements.

                Regards,
                HR Team
                """
                st.text_area(
                    "Generated Email",
                    email_body,
                    height=250
                )


# Chat History
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            intent = message.get("intent")
            score = message.get("score")

            if intent == "resume":
                st.caption("📄 Source: Uploaded Resume")

                if score is not None:
                    st.caption(
                        f"Similarity Score: {score:.3f}"
                    )

            elif intent == "general":
                st.caption("🌐 Source: General Knowledge")

# Chat Input
question = st.chat_input(
    "Ask anything about the resume..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    response = st.session_state.pipeline.ask(question)

    answer = response["answer"]
    intent = response["intent"]
    score = response["score"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

        if intent == "resume":
            st.caption("📄 Source: Uploaded Resume")
        else:
            st.caption("🌐 Source: General Knowledge")

        if intent == "resume" and score is not None:
            st.caption(f"Similarity Score: {score:.3f}")