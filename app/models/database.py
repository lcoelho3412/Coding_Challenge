# database.py
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# This is the database connection URL - using SQLite for simplicity since it stores data in a single file
SQLALCHEMY_DATABASE_URL = "sqlite:///./marketing_ai.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },  # Needed for SQLite to work with FastAPI's async nature
)

# SessionLocal will be our gateway to talk to the database - each request gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # Base class for all our database models


class DBQuestionAnswer(Base):
    """Database model for storing question-answer history."""

    __tablename__ = "qa_history"  # This determines the table name in SQLite

    # These columns define what data we store for each Q&A pair
    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing ID
    question = Column(String)  # The user's original question
    answer = Column(String)  # The AI's response
    timestamp = Column(
        DateTime, default=datetime.datetime.utcnow
    )  # Auto-filled timestamp


# This actually creates the database tables if they don't exist
Base.metadata.create_all(bind=engine)
