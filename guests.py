"""Guest list management backed by PostgreSQL."""

import csv
from typing import Dict

from data_store import Guest, SessionLocal


def manage_guest(guest_id: int = None, action: str = "add", **data) -> int:
    """Add, update or delete a guest."""
    session = SessionLocal()
    if action == "add":
        guest = Guest(
            name=data.get("name"),
            email=data.get("email"),
            category=data.get("category"),
        )
        session.add(guest)
        session.commit()
        gid = guest.id
        session.close()
        return gid
    elif action == "edit":
        guest = session.get(Guest, guest_id)
        if not guest:
            session.close()
            raise ValueError("Invalid action or guest_id")
        guest.name = data.get("name", guest.name)
        guest.email = data.get("email", guest.email)
        guest.category = data.get("category", guest.category)
        session.commit()
        session.close()
        return guest_id
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
    session = SessionLocal()
    guest = session.get(Guest, guest_id)
    if not guest:
        session.close()
        return False
    guest.category = category
    session.commit()
    session.close()
    return True


def import_guestlist(csv_file: str) -> int:
    """Import guests from a CSV file. Columns: name,email,category"""
    count = 0
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            manage_guest(
                action="add",
                name=row.get("name"),
                email=row.get("email"),
                category=row.get("category"),
            )
            count += 1
    return count


def list_guests() -> Dict[int, Dict]:
    """Return all guests as a mapping of id to data."""
    session = SessionLocal()
    result = {
        g.id: {"name": g.name, "email": g.email, "category": g.category}
        for g in session.query(Guest).all()
    }
    session.close()
    return result

