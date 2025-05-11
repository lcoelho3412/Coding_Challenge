from fastapi import FastAPI
from schemas import QuestionRequest, AnswerResponse
from datetime import datetime

app = FastAPI(title="Marketing AI Assistant")

@app.get("/ping")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
  
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(question: QuestionRequest):
    # Mock response for now
    return AnswerResponse(
        answer="This is a mock response. Real AI integration coming soon.",
        model_used="mock",
        timestamp=datetime.now()
    )