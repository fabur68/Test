"""Guest list management backed by SQLAlchemy."""

import csv
from typing import Dict, List
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Guest


def _guest_to_dict(guest: Guest) -> Dict:
    return {
        "id": guest.id,
        "name": guest.name,
        "email": guest.email,
        "category": guest.category,
<<<<<<< HEAD
        "event_id": guest.event_id,
=======
<<<<<<< HEAD
        "event_id": guest.event_id,
=======
>>>>>>> main
>>>>>>> main
    }


def manage_guest(guest_id: int = None, action: str = "add", **data) -> int:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    """Add, update or delete a guest. Optionally assign to an event."""
    session: Session = SessionLocal()
    if action == "add":
        guest = Guest(name=data.get("name"), email=data.get("email"), category=data.get("category"),
                      event_id=data.get("event_id"))
<<<<<<< HEAD
=======
=======
    """Add, update or delete a guest."""
    session: Session = SessionLocal()
    if action == "add":
        guest = Guest(name=data.get("name"), email=data.get("email"), category=data.get("category"))
>>>>>>> main
>>>>>>> main
        session.add(guest)
        session.commit()
        session.refresh(guest)
        gid = guest.id
        session.close()
        return gid
    elif action == "edit":
        guest = session.get(Guest, guest_id)
        if not guest:
            session.close()
            raise ValueError("Invalid action or guest_id")
        for key, value in data.items():
            if hasattr(guest, key):
                setattr(guest, key, value)
        session.commit()
        gid = guest.id
        session.close()
        return gid
    elif action == "delete":
        guest = session.get(Guest, guest_id)
        if not guest:
            session.close()
            raise ValueError("Invalid action or guest_id")
        session.delete(guest)
        session.commit()
        session.close()
        return guest_id
    else:
        session.close()
        raise ValueError("Invalid action or guest_id")


def categorize_guest(guest_id: int, category: str) -> bool:
    """Assign a category to a guest."""
    session: Session = SessionLocal()
    guest = session.get(Guest, guest_id)
    if not guest:
        session.close()
        return False
    guest.category = category
    session.commit()
    session.close()
    return True


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
def assign_guest_to_event(guest_id: int, event_id: int) -> bool:
    """Assign an existing guest to an event."""
    session: Session = SessionLocal()
    guest = session.get(Guest, guest_id)
    if not guest:
        session.close()
        return False
    guest.event_id = event_id
    session.commit()
    session.close()
    return True


<<<<<<< HEAD
=======
=======
>>>>>>> main
>>>>>>> main
def import_guestlist(csv_file: str) -> int:
    """Import guests from a CSV file. Columns: name,email,category"""
    count = 0
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            manage_guest(action="add", name=row.get("name"), email=row.get("email"), category=row.get("category"))
            count += 1
    return count


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
def get_all_guests(event_id: int | None = None) -> List[Dict]:
    """Return all guests as a list of dictionaries. Filter by event if provided."""
    session: Session = SessionLocal()
    query = session.query(Guest)
    if event_id is not None:
        query = query.filter(Guest.event_id == event_id)
    data = [_guest_to_dict(g) for g in query.all()]
<<<<<<< HEAD
=======
=======
def get_all_guests() -> List[Dict]:
    """Return all guests as a list of dictionaries."""
    session: Session = SessionLocal()
    data = [_guest_to_dict(g) for g in session.query(Guest).all()]
>>>>>>> main
>>>>>>> main
    session.close()
    return data
