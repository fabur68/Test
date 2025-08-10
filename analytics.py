"""Analytics and reporting."""

<<<<<<< HEAD
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Guest, RSVP, Payment, Seating
=======
from data_store import events, guests, rsvps, payments, seating_plans
>>>>>>> main


def dashboard_overview(event_id: int) -> dict:
    """Return a simple overview for an event."""
<<<<<<< HEAD
    session: Session = SessionLocal()
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
    session.close()
=======
    total_guests = len(guests)
    responses = {"Ja": 0, "Nein": 0, "Vielleicht": 0}
    for (e_id, _), resp in rsvps.items():
        if e_id == event_id:
            responses[resp] += 1
    paid = sum(1 for (g_id, e_id), status in [((g, e), p["status"]) for g, ev in payments.items() for e, p in ev.items()] if e_id == event_id and status == "paid")
>>>>>>> main
    return {
        "total_guests": total_guests,
        "responses": responses,
        "payments": paid,
    }


def generate_report(event_id: int) -> dict:
    """Generate a detailed report."""
    overview = dashboard_overview(event_id)
<<<<<<< HEAD
    session: Session = SessionLocal()
    seats_assigned = (
        session.query(Seating)
        .filter(Seating.event_id == event_id, Seating.guest_id.isnot(None))
        .count()
    )
    session.close()
    overview["seats_assigned"] = seats_assigned
=======
    seats = seating_plans.get(event_id, {})
    overview["seats_assigned"] = sum(1 for s in seats.values() if s is not None)
>>>>>>> main
    return overview
