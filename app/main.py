from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.models.database import SessionLocal, DBQuestionAnswer
from app.schemas.schemas import QuestionRequest, AnswerResponse
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI(title="Marketing AI Assistant")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(
    question: QuestionRequest, db: Annotated[Session, Depends(get_db)]
):
    """Endpoint to ask marketing questions (currently mocked)."""
    # Mock response for now
    response = AnswerResponse(
        answer="This is a mock response. Real AI integration coming soon.",
        model_used="mock",
        timestamp=datetime.now(),
    )

    # Store in DB (we'll implement this properly later)
    db_qa = DBQuestionAnswer(
        question=question.question,
        answer=response.answer,
    )
    db.add(db_qa)
    db.commit()

    return response
