from datetime import datetime
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    user_id: str  # for future authentication

class AnswerResponse(BaseModel):
    answer: str
    model_used: str
    timestamp: datetime

class QuestionAnswer(BaseModel):
    question: str
    answer: str
    timestamp: datetime
    is_marketing_related: bool