# main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.models.database import SessionLocal, DBQuestionAnswer
from app.schemas.schemas import QuestionRequest, AnswerResponse
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Session
from app.services.ollama_client import OllamaClient
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import traceback


ollama_client = OllamaClient()

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


@app.get("/ping")
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        content={"status": "healthy", "version": "0.1.0"}, status_code=200
    )


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(
    question: QuestionRequest, db: Annotated[Session, Depends(get_db)]
):
    """Endpoint to ask marketing questions with real AI responses"""
    try:
        # Get AI response
        response = await ollama_client.ask_marketing_question(question)

        # Store in DB
        db_qa = DBQuestionAnswer(
            question=question.question,
            answer=response.answer,
            timestamp=response.timestamp,
        )
        db.add(db_qa)
        db.commit()

        return response

    except Exception as e:
        print("=== Exception in /ask ===")
        print(f"Type: {type(e).__name__}")
        print(f"Details: {e}")
        traceback.print_exc()  # prints full traceback to console/log
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")
