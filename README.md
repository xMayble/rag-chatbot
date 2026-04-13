# 📄 AI Document Q&A Chatbot (RAG Pipeline)

A full-stack AI-powered chatbot that lets you upload any PDF and ask questions about it in plain English. Built with a Retrieval-Augmented Generation (RAG) pipeline using LangChain, ChromaDB, and Anthropic's Claude LLM — deployed on AWS.

---

## 🚀 Live Demo

> API: `http://35.173.238.199:8000/docs`

---

## 🧠 How It Works

Instead of asking an LLM to guess answers, this app first retrieves the most relevant content from your document, then passes it to Claude as context — so every answer is grounded in what's actually in the PDF.

```
Upload PDF → Extract & Chunk Text → Generate Embeddings → Store in ChromaDB
                                                                    ↓
                                          User Question → Semantic Search → Claude → Answer
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| Backend API | FastAPI + Uvicorn |
| AI Orchestration | LangChain |
| LLM | Anthropic Claude API |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| File Storage | AWS S3 |
| Deployment | AWS EC2 (Ubuntu) |
| Frontend | Streamlit |
| Environment | python-dotenv |

---

## 📁 Project Structure

```
rag-chatbot/
├── app/
│   ├── __init__.py
│   ├── ingest.py       # PDF loading, chunking, ChromaDB storage
│   ├── rag.py          # Semantic search + Claude integration
│   └── main.py         # FastAPI endpoints
├── uploads/            # Temporary local storage before S3 upload
├── .env                # API keys (never committed)
├── .gitignore
├── requirements.txt
└── streamlit_app.py    # Frontend chat UI
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com)
- An [AWS account](https://aws.amazon.com) with an S3 bucket

### 1. Clone the repo
```bash
git clone https://github.com/xMayble/rag-chatbot.git
cd rag-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install sentence-transformers
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
ANTHROPIC_API_KEY=your_anthropic_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_BUCKET_NAME=your_s3_bucket_name
AWS_REGION=us-east-1
```

### 5. Run the app

**Terminal 1 — Start the API:**
```bash
uvicorn app.main:app --reload
```

**Terminal 2 — Start the frontend:**
```bash
streamlit run streamlit_app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/upload` | Upload and ingest a PDF |
| `POST` | `/ask` | Ask a question about the document |

---

## ☁️ AWS Infrastructure

- **S3** — Stores uploaded PDFs for scalable, production-grade file handling
- **EC2 (t2.micro, Ubuntu)** — Hosts the FastAPI backend with a live public URL

---

## 📌 Key Concepts

**RAG (Retrieval-Augmented Generation)** — A technique that improves LLM accuracy by retrieving relevant context from a knowledge base before generating a response. This prevents hallucinations and grounds answers in real document content.

**Vector Embeddings** — Text chunks are converted into numerical vectors that capture semantic meaning. ChromaDB stores these and enables similarity search — finding relevant chunks by meaning, not just keywords.

---

## 🔮 Future Improvements

- [ ] Multi-PDF support
- [ ] Chat history / memory
- [ ] Source citations showing which page the answer came from
- [ ] User authentication
- [ ] Frontend rebuild in React

---

## 👤 Author

**Mehbub Rohit**  
[LinkedIn](https://linkedin.com/in/mehbubrohit) · [GitHub](https://github.com/xMayble)
