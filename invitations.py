<<<<<<< HEAD
"""Invitation and RSVP handling using the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Event, Guest, RSVP
=======
"""Invitation and RSVP handling."""

from data_store import events, guests, rsvps
>>>>>>> main


def send_invitation(event_id: int, guest_email: str) -> bool:
    """Mock sending an invitation by email."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    event = session.get(Event, event_id)
    session.close()
    if not event:
        return False
    print(f"Sending invitation for '{event.name}' to {guest_email}")
=======
    event = events.get(event_id)
    if not event:
        return False
    print(f"Sending invitation for '{event['name']}' to {guest_email}")
>>>>>>> main
    return True


def record_rsvp(event_id: int, guest_id: int, response: str) -> bool:
<<<<<<< HEAD
    """Record a guest's RSVP response in the database."""
    if response not in {"Ja", "Nein", "Vielleicht"}:
        raise ValueError("Response must be 'Ja', 'Nein' or 'Vielleicht'")
    session: Session = SessionLocal()
    rsvp = session.query(RSVP).filter_by(event_id=event_id, guest_id=guest_id).first()
    if rsvp:
        rsvp.response = response
    else:
        rsvp = RSVP(event_id=event_id, guest_id=guest_id, response=response)
        session.add(rsvp)
    session.commit()
    session.close()
    notify_organizer_rsvp(event_id, guest_id, response)
=======
    """Record a guest's RSVP response."""
    if response not in {"Ja", "Nein", "Vielleicht"}:
        raise ValueError("Response must be 'Ja', 'Nein' or 'Vielleicht'")
    rsvps[(event_id, guest_id)] = response
>>>>>>> main
    return True


def notify_organizer_rsvp(event_id: int, guest_id: int, response: str) -> None:
<<<<<<< HEAD
    """Notify organizer about a new RSVP (mock)."""
    session: Session = SessionLocal()
    event = session.get(Event, event_id)
    guest = session.get(Guest, guest_id)
    if event and guest:
        print(f"Organizer notified: {guest.name} responded '{response}' for '{event.name}'")
    session.close()
=======
    """Notify organizer about a new RSVP."""
    event = events.get(event_id)
    guest = guests.get(guest_id)
    if event and guest:
        print(f"Organizer notified: {guest['name']} responded '{response}' for '{event['name']}'")
>>>>>>> main
