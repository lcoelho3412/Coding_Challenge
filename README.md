# 🧠 Marketing AI Agent (FastAPI + Ollama + SQLite)

This is a simple full-stack AI-powered question-answering system focused on **marketing-related questions**. It uses:

- `FastAPI` for the backend API
- `SQLite` for persistent storage
- `Ollama` running a local `llama3` model for responses

The project is ideal for developers exploring AI integrations, database persistence, and full-stack Python APIs.

---

## 🚀 Features

- Ask questions via `/ask` - AI generates an answer
- Retrieve past questions and answers via `/history`
- Stores each interaction in a local SQLite database

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourname/marketing-ai-agent.git
cd marketing-ai-agent
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic requests
```

### 3. Run Ollama locally
Make sure Ollama is installed and the model is available:
```bash
ollama run llama3  # Updated to llama3 to match project description
```

### 4. Start the FastAPI server
```bash
uvicorn main:app --reload
```
The API will be accessible at: http://localhost:8000

---

## 📂 File Structure
```
.
├── main.py                # FastAPI app with endpoints
├── database.py            # SQLAlchemy setup + data model
├── schemas.py             # Pydantic request/response models
├── app/
│   └── services/
│       └── ollama_client.py  # Wrapper to interact with Ollama API
└── marketing_ai.db        # (created after running, SQLite file)
```

---

## 🔄 API Endpoints

### POST /ask
Submit a question.

**Request body:**
```json
{
  "question": "How can I improve my email open rate?",
  "user_id": "user123"
}
```

**Response:**
```json
{
  "answer": "Here are some tips for improving your email open rates...",
  "model_used": "llama3",
  "timestamp": "2025-05-12T10:15:00.000Z"
}
```

### GET /history
Retrieve previous Q&A sessions.

**Response:**
```json
[
  {
    "question": "...",
    "answer": "...",
    "timestamp": "...",
    "is_marketing_related": true
  }
]
```

---

## 🧑‍💻 For Contributors / Learners
- The AI logic is centralized in `ollama_client.py`, making it easy to swap models or adjust prompt templates
- Data persistence is handled via SQLAlchemy and stored in `marketing_ai.db`
- The codebase is beginner-friendly and structured for modular learning

---

## 📌 Important Notes
- 🔒 **CORS** is fully open (`*`) - change in production
- 🔐 Authentication is not implemented yet but `user_id` is included for future use
- ⚠️ Ollama must be running locally for the API to function

---

## 📃 License
MIT License - feel free to use and modify!

---

Let me know if you'd like to add:
- Architecture diagram
- HTTP client collection (Postman/Insomnia)
- Next.js frontend scaffolding
- Environment variables configuration
- Testing instructions
- Deployment guide

