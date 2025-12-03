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
        "event_id": guest.event_id,
    }


def manage_guest(guest_id: int = None, action: str = "add", **data) -> int:
    """Add, update or delete a guest. Optionally assign to an event."""
    with SessionLocal() as session:
        if action == "add":
            guest = Guest(
                name=data.get("name"),
                email=data.get("email"),
                category=data.get("category"),
                event_id=data.get("event_id"),
            )
            session.add(guest)
            session.commit()
            session.refresh(guest)
            return guest.id
        elif action == "edit":
            guest = session.get(Guest, guest_id)
            if not guest:
                raise ValueError("Invalid action or guest_id")
            for key, value in data.items():
                if hasattr(guest, key):
                    setattr(guest, key, value)
            session.commit()
            return guest.id
        elif action == "delete":
            guest = session.get(Guest, guest_id)
            if not guest:
                raise ValueError("Invalid action or guest_id")
            session.delete(guest)
            session.commit()
            return guest_id
        else:
            raise ValueError("Invalid action or guest_id")


def categorize_guest(guest_id: int, category: str) -> bool:
    """Assign a category to a guest."""
    with SessionLocal() as session:
        guest = session.get(Guest, guest_id)
        if not guest:
            return False
        guest.category = category
        session.commit()
        return True


def assign_guest_to_event(guest_id: int, event_id: int) -> bool:
    """Assign an existing guest to an event."""
    with SessionLocal() as session:
        guest = session.get(Guest, guest_id)
        if not guest:
            return False
        guest.event_id = event_id
        session.commit()
        return True


def import_guestlist(csv_file: str) -> int:
    """Import guests from a CSV file. Columns: name,email,category"""
    count = 0
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            manage_guest(action="add", name=row.get("name"), email=row.get("email"), category=row.get("category"))
            count += 1
    return count


def get_all_guests(event_id: int | None = None) -> List[Dict]:
    """Return all guests as a list of dictionaries. Filter by event if provided."""
    with SessionLocal() as session:
        query = session.query(Guest)
        if event_id is not None:
            query = query.filter(Guest.event_id == event_id)
        return [_guest_to_dict(g) for g in query.all()]
