"""Feedback and surveys backed by the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Feedback


def submit_feedback(event_id: int, guest_id: int, rating: int, comment: str) -> None:
    """Store feedback from a guest."""
    session: Session = SessionLocal()
    entry = Feedback(event_id=event_id, guest_id=guest_id, rating=rating, comment=comment)
    session.add(entry)
    session.commit()
    session.close()


def track_survey(event_id: int, question: str, answers: dict) -> dict:
    """Return survey data for analysis (mock)."""
    return {"event_id": event_id, "question": question, "answers": answers}
