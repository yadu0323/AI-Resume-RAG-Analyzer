# 📄 AI Resume RAG Analyzer & JD Matcher

An AI-powered Resume Analyzer and Job Description Matching System built with **Python**, **Streamlit**, **Ollama**, and **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload resumes, ask questions about candidates, compare resumes against job descriptions, identify skill gaps, generate recruiter summaries, and create interview invitation emails.

All processing runs locally using Ollama, ensuring privacy and zero dependency on paid APIs.

---

## ✨ Features

### 📄 Resume Analysis

- Upload PDF resumes
- Extract and process resume content
- Semantic search using embeddings
- Resume-based question answering
- Resume summarization

### 🤖 Intelligent Question Routing

- Detects whether a question is:
  - Resume-related
  - General knowledge
- Automatically routes queries to the appropriate response pipeline

### 💬 Conversational Chat Interface

- Streamlit chat UI
- Persistent chat history
- Clear chat functionality
- Source tracking for responses
- Interactive conversation flow

### 🧠 RAG Pipeline

- PDF Loading
- Text Cleaning
- Text Chunking
- Embedding Generation
- Vector Similarity Search
- Context Retrieval
- LLM Response Generation

### 🌐 General Knowledge Support

- Answers questions beyond the uploaded resume
- Uses local Ollama LLM
- Falls back to general knowledge when resume context is not relevant

### 📊 Job Description Matching

- Paste Job Descriptions directly into the application
- Compare resumes against job requirements
- Semantic similarity scoring
- Match percentage calculation
- Visual score representation

### ✅ Skill Gap Analysis

- Extract skills from resumes
- Extract skills from job descriptions
- Identify matched skills
- Identify missing skills
- Generate recruiter-friendly skill reports

### 🎯 Candidate Evaluation

- Strong Match recommendations
- Moderate Match recommendations
- Low Match recommendations
- Recruiter-focused candidate evaluation
- Skill match percentage analysis

### 📋 Recruiter Summary

- Automated candidate summary
- Highlight strengths
- Highlight missing skills
- Quick decision support for recruiters

### 📧 Interview Email Generation

- Generate interview invitation emails
- Dynamic email templates
- Candidate communication support
- Recruiter workflow assistance

### 🔒 Local AI

- Runs locally using Ollama
- No external API required
- Resume data remains private
- Fully offline AI workflow

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
                     Embeddings
          (BAAI/bge-small-en-v1.5)
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
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      Resume Question          General Question
             │                         │
             └────────► Ollama ◄───────┘
                           │
                           ▼
                     Final Answer


────────────────────────────────────────────

                      Resume
                         │
                         ▼
                 JD Matching Engine
                         │
                         ▼
                  Similarity Score
                         │
                         ▼
                 Skill Gap Analysis
                         │
                         ▼
               Candidate Evaluation
                         │
                         ▼
                 Recruiter Summary
                         │
                         ▼
            Interview Email Generation
```

---

## 🛠️ Tech Stack

### Backend

- Python

### Frontend

- Streamlit

### AI & NLP

- Ollama
- Qwen 2.5 Coder 7B
- Sentence Transformers
- BAAI/bge-small-en-v1.5

### Machine Learning

- Scikit-Learn
- Cosine Similarity

### Document Processing

- PyPDF

### Vector Search

- NumPy
- Semantic Embeddings
- Similarity Retrieval

---

## 📁 Project Structure

```text
AI-Resume-RAG-Analyzer/
│
├── app.py
├── test_loader.py
├── test_jd.py
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
    ├── chat_memory.py
    ├── jd_matcher.py
    └── skill_matcher.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yadu0323/AI-Resume-RAG-Analyzer.git

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

Download Ollama:

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

## 📋 Example Resume Questions

```text
What skills does the candidate have?

What projects has the candidate built?

Summarize the resume.

What technologies does the candidate know?

What experience does the candidate have?
```

---

## 🌐 Example General Questions

```text
Who won FIFA World Cup 2022?

Explain FastAPI dependency injection.

What is Retrieval-Augmented Generation?

What is Machine Learning?

How does Docker work?
```

---

## 📊 Example Job Description Analysis

### Sample JD

```text
AI/ML Engineer

Required Skills:
- Python
- Machine Learning
- Deep Learning
- NLP
- FastAPI
- Docker
- AWS
- Git
```

### System Output

```text
Match Score: 78.45%

Matched Skills:
✓ Python
✓ Machine Learning
✓ Deep Learning
✓ NLP
✓ FastAPI
✓ Git

Missing Skills:
✗ Docker
✗ AWS

Recommendation:
Moderate Match

Recruiter Summary:
Candidate demonstrates strong AI/ML skills and project experience.
Additional exposure to Docker and AWS would strengthen alignment with the role.
```

---

## 📧 Interview Email Example

```text
Subject: Interview Invitation

Dear Candidate,

We reviewed your resume and would like to invite you for an interview.

Your profile achieved a strong match against our job requirements.

We look forward to discussing your experience further.

Regards,
HR Team
```

---

## 🔮 Future Improvements

- ATS Resume Scoring
- Resume Improvement Suggestions
- Interview Question Generator
- Candidate Ranking System
- Multi-Resume Comparison
- Recruiter Dashboard
- Resume-to-JD Gap Analysis using LLMs
- Download Analysis Reports (PDF)
- FastAPI Backend
- Authentication System
- Multi-Resume Support
- FAISS Integration
- ChromaDB Integration
- Candidate Tracking System
- Email Sending Integration
- Analytics Dashboard
- Role-Based Evaluation System
- LLM-Powered Recruiter Assistant

---

## 👨‍💻 Author

**Yadu Krishna**

GitHub: https://github.com/yadu0323

---

## ⭐ Support

If you found this project useful:

- Give the repository a ⭐
- Fork the project
- Share feedback
- Contribute improvements

---

