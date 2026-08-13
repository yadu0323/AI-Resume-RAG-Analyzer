# 📄 AI Resume RAG Analyzer

An AI-powered Resume Analyzer built with **Python**, **Streamlit**, **Ollama**, and **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload a resume, ask questions about the candidate, and receive accurate responses using semantic search and local LLMs. It can also answer general knowledge questions outside the resume context through intelligent intent routing.

---

## ✨ Features

### 📄 Resume Analysis
- Upload PDF resumes
- Extract and process resume content
- Semantic search using embeddings
- Resume-based question answering

### 🤖 Intelligent Question Routing
- Detects whether a question is:
  - Resume-related
  - General knowledge
- Automatically routes queries to the appropriate response pipeline

### 💬 Conversational Chat Interface
- Streamlit chat UI
- Chat history support
- Clear chat functionality
- Source tracking for responses

### 🧠 RAG Pipeline
- PDF Loading
- Text Cleaning
- Chunking
- Embedding Generation
- Vector Similarity Search
- Context Retrieval
- LLM Response Generation

### 🌐 General Knowledge Support
- Answers questions beyond the uploaded resume
- Uses local Ollama LLM

### 🔒 Local AI
- Runs locally using Ollama
- No external API required
- Resume data stays on your machine

---

## 🏗️ Architecture

```text
PDF Resume
     │
     ▼
 PDF Loader
     │
     ▼
 Text Cleaning
     │
     ▼
 Text Chunking
     │
     ▼
 Embeddings (BAAI/bge-small-en-v1.5)
     │
     ▼
 Vector Store
     │
     ▼
 Retriever
     │
     ▼
 Intent Detection
     │
 ┌───┴─────────────┐
 │                 │
 ▼                 ▼
Resume Q&A     General Q&A
 │                 │
 └──────► Ollama ◄─┘
            │
            ▼
       Final Answer
```

---

## 🛠️ Tech Stack

### Backend
- Python

### AI & NLP
- Ollama
- Qwen 2.5 Coder 7B
- Sentence Transformers
- BAAI/bge-small-en-v1.5

### Frontend
- Streamlit

### Document Processing
- PyPDF

### Vector Search
- NumPy
- Cosine Similarity

---

## 📁 Project Structure

```text
AI-Resume-RAG-Analyzer/
│
├── app.py
├── test_loader.py
├── requirements.txt
│
├── data/
│   ├── uploads/
│   └── chat_history/
│
└── RAG/
    ├── cleaner.py
    ├── chunker.py
    ├── embeddings.py
    ├── vectorstore.py
    ├── retriever.py
    ├── intent.py
    ├── classifier.py
    ├── router.py
    ├── llm.py
    ├── loader.py
    ├── prompts.py
    ├── pipeline.py
    └── chat_memory.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-RAG-Analyzer.git
cd AI-Resume-RAG-Analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv RA
```

### 3. Activate Virtual Environment

#### Windows

```bash
RA\Scripts\activate
```

#### Linux / macOS

```bash
source RA/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Install Ollama

Download and install Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull qwen2.5-coder:7b
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📋 Example Questions

### Resume Questions

```text
What skills does the candidate have?

What projects has the candidate built?

Summarize the resume.

What technologies does the candidate know?
```

### General Questions

```text
Who won FIFA World Cup 2022?

Explain FastAPI dependency injection.

What is Retrieval-Augmented Generation?
```

---

## 🔮 Future Improvements

- ATS Score Analysis
- Resume Improvement Suggestions
- Multi-Session Chats
- Download Chat History
- FastAPI Backend
- Authentication System
- Multi-Resume Support
- Vector Database Integration (FAISS/Chroma)

---

## 👨‍💻 Author

**Yadu Krishna**

GitHub: https://github.com/yadu0323

---

## ⭐ If you found this project useful

Give the repository a star and feel free to contribute.