"""Feedback and surveys."""

from data_store import feedback


def submit_feedback(event_id: int, guest_id: int, rating: int, comment: str) -> None:
    """Store feedback from a guest."""
    feedback[(event_id, guest_id)] = {"rating": rating, "comment": comment}


def track_survey(event_id: int, question: str, answers: dict) -> dict:
    """Return survey data for analysis (mock)."""
    return {"event_id": event_id, "question": question, "answers": answers}
