from datetime import datetime
from pydantic import BaseModel
# from typing import Optional


class QuestionRequest(BaseModel):
    """Request schema for submitting a question."""

    question: str
    user_id: str  # for future authentication


class AnswerResponse(BaseModel):
    """Response schema for AI answers."""

    answer: str
    model_used: str
    timestamp: datetime


class QuestionAnswer(BaseModel):
    """Combined Q&A schema for history."""

    question: str
    answer: str
    timestamp: datetime
    is_marketing_related: bool
