from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
# from typing import Optional

SQLALCHEMY_DATABASE_URL = "sqlite:///./marketing_ai.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # Needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class DBQuestionAnswer(Base):
    """Database model for storing question-answer history."""

    __tablename__ = "qa_history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<QA(id={self.id}, question='{self.question}', timestamp={self.timestamp})>"


# Create tables
Base.metadata.create_all(bind=engine)
