# main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.models.database import SessionLocal, DBQuestionAnswer
from app.schemas.schemas import QuestionRequest, AnswerResponse
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from app.services.ollama_client import OllamaClient

app = FastAPI(title="Marketing AI Assistant")

# CORS settings - this allows our frontend to talk to the backend from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, you'd want to restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This dependency will provide a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db  # The session stays open during the request
    finally:
        db.close()  # And automatically closes afterward


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(
    question: QuestionRequest, db: Annotated[Session, Depends(get_db)]
):
    """Endpoint to ask marketing questions (currently mocked)."""
    # For now we're using a mock response, but later we'll call the Ollama client here
    response = AnswerResponse(
        answer="This is a mock response. Real AI integration coming soon.",
        model_used="mock",
        timestamp=datetime.now(),
    )

    # Saving to database - notice we create a DBQuestionAnswer instance
    db_qa = DBQuestionAnswer(
        question=question.question,
        answer=response.answer,
    )
    db.add(db_qa)  # Stage the change
    db.commit()  # Actually save to database

    return response
