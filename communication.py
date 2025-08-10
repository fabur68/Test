"""Communication utilities."""

<<<<<<< HEAD
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Guest
=======
from data_store import guests
>>>>>>> main


def send_message(recipient_ids, subject: str, body: str) -> None:
    """Send a message to recipients (mock)."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    if recipient_ids == "all":
        recipients = session.query(Guest).all()
    else:
        recipients = session.query(Guest).filter(Guest.id.in_(recipient_ids)).all()
    for r in recipients:
        print(f"To {r.email}: {subject}\n{body}\n")
    session.close()
=======
    if recipient_ids == "all":
        recipients = guests.values()
    else:
        recipients = [guests.get(gid) for gid in recipient_ids if gid in guests]
    for r in recipients:
        print(f"To {r['email']}: {subject}\n{body}\n")
>>>>>>> main


def push_notification(guest_id: int, message: str) -> bool:
    """Send a push notification (mock)."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    guest = session.get(Guest, guest_id)
    if not guest:
        session.close()
        return False
    print(f"Push to {guest.name}: {message}")
    session.close()
=======
    guest = guests.get(guest_id)
    if not guest:
        return False
    print(f"Push to {guest['name']}: {message}")
>>>>>>> main
    return True


def send_reminder(event_id: int, guest_id: int = None) -> None:
<<<<<<< HEAD
    """Send reminder emails. If guest_id is None, send to all guests."""
    session: Session = SessionLocal()
    query = session.query(Guest)
    if guest_id:
        query = query.filter(Guest.id == guest_id)
    for g in query.all():
        print(f"Reminder sent to {g.email} for event {event_id}")
    session.close()
=======
    """Send reminder emails. If guest_id is None, send to all."""
    if guest_id:
        target_ids = [guest_id] if guest_id in guests else []
    else:
        target_ids = list(guests.keys())
    for gid in target_ids:
        print(f"Reminder sent to {guests[gid]['email']} for event {event_id}")
>>>>>>> main
