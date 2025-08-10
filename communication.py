"""Communication utilities."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Guest


def send_message(recipient_ids, subject: str, body: str) -> None:
    """Send a message to recipients (mock)."""
    session: Session = SessionLocal()
    if recipient_ids == "all":
        recipients = session.query(Guest).all()
    else:
        recipients = session.query(Guest).filter(Guest.id.in_(recipient_ids)).all()
    for r in recipients:
        print(f"To {r.email}: {subject}\n{body}\n")
    session.close()


def push_notification(guest_id: int, message: str) -> bool:
    """Send a push notification (mock)."""
    session: Session = SessionLocal()
    guest = session.get(Guest, guest_id)
    if not guest:
        session.close()
        return False
    print(f"Push to {guest.name}: {message}")
    session.close()
    return True


def send_reminder(event_id: int, guest_id: int = None) -> None:
    """Send reminder emails. If guest_id is None, send to all guests."""
    session: Session = SessionLocal()
    query = session.query(Guest)
    if guest_id:
        query = query.filter(Guest.id == guest_id)
    for g in query.all():
        print(f"Reminder sent to {g.email} for event {event_id}")
    session.close()
