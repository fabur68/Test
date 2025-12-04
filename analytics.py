"""Analytics and reporting."""

from sqlalchemy import func
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Guest, RSVP, Payment, Seating


def dashboard_overview(event_id: int) -> dict:
    """Return a simple overview for an event."""
    with SessionLocal() as session:
        total_guests = session.query(Guest).filter(Guest.event_id == event_id).count()
        responses = {"Ja": 0, "Nein": 0, "Vielleicht": 0}
        for resp, count in (
            session.query(RSVP.response, func.count(RSVP.id))
            .filter(RSVP.event_id == event_id)
            .group_by(RSVP.response)
        ):
            responses[resp] = count
        paid = (
            session.query(Payment)
            .filter(Payment.event_id == event_id, Payment.status == "paid")
            .count()
        )
    return {
        "total_guests": total_guests,
        "responses": responses,
        "payments": paid,
    }


def generate_report(event_id: int) -> dict:
    """Generate a detailed report."""
    overview = dashboard_overview(event_id)
    with SessionLocal() as session:
        seats_assigned = (
            session.query(Seating)
            .filter(Seating.event_id == event_id, Seating.guest_id.isnot(None))
            .count()
        )
    overview["seats_assigned"] = seats_assigned
    return overview
