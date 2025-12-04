"""Invitation and RSVP handling using the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Event, Guest, RSVP


def send_invitation(event_id: int, guest_email: str) -> bool:
    """Mock sending an invitation by email."""
    with SessionLocal() as session:
        event = session.get(Event, event_id)
        if not event:
            return False
    print(f"Sending invitation for '{event.name}' to {guest_email}")
    return True


def record_rsvp(event_id: int, guest_id: int, response: str) -> bool:
    """Record a guest's RSVP response in the database."""
    if response not in {"Ja", "Nein", "Vielleicht"}:
        raise ValueError("Response must be 'Ja', 'Nein' or 'Vielleicht'")
    with SessionLocal() as session:
        rsvp = session.query(RSVP).filter_by(event_id=event_id, guest_id=guest_id).first()
        if rsvp:
            rsvp.response = response
        else:
            rsvp = RSVP(event_id=event_id, guest_id=guest_id, response=response)
            session.add(rsvp)
        guest = session.get(Guest, guest_id)
        if guest and guest.event_id is None:
            guest.event_id = event_id
        session.commit()
    notify_organizer_rsvp(event_id, guest_id, response)
    return True


def notify_organizer_rsvp(event_id: int, guest_id: int, response: str) -> None:
    """Notify organizer about a new RSVP (mock)."""
    with SessionLocal() as session:
        event = session.get(Event, event_id)
        guest = session.get(Guest, guest_id)
        if event and guest:
            print(f"Organizer notified: {guest.name} responded '{response}' for '{event.name}'")
