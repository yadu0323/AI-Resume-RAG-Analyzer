import streamlit as st
from RAG.pipeline import ResumeRAGPipeline
from RAG.chat_memory import ChatMemory

st.set_page_config(
    page_title="Resume RAG Analyzer",
    page_icon="📄",
    layout="wide"
)

if "pipeline" not in st.session_state:
    st.session_state.pipeline = ResumeRAGPipeline()
    memory = ChatMemory()

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

    if st.session_state.resume_loaded:
        st.success("✅ Resume Loaded")
    else:
        st.warning("⚠️ No Resume Uploaded")


uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file and not st.session_state.resume_loaded:

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.pipeline.load_resume(save_path)

    st.session_state.resume_loaded = True

    st.success("Resume uploaded successfully!")

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