<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
"""Feedback and surveys backed by the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Feedback
<<<<<<< HEAD
=======
=======
"""Feedback and surveys."""

from data_store import feedback
>>>>>>> main
>>>>>>> main


def submit_feedback(event_id: int, guest_id: int, rating: int, comment: str) -> None:
    """Store feedback from a guest."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    entry = Feedback(event_id=event_id, guest_id=guest_id, rating=rating, comment=comment)
    session.add(entry)
    session.commit()
    session.close()
<<<<<<< HEAD
=======
=======
    feedback[(event_id, guest_id)] = {"rating": rating, "comment": comment}
>>>>>>> main
>>>>>>> main


def track_survey(event_id: int, question: str, answers: dict) -> dict:
    """Return survey data for analysis (mock)."""
    return {"event_id": event_id, "question": question, "answers": answers}
