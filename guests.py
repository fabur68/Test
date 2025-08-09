"""Guest list management."""

import csv
from typing import Dict
from data_store import guests

next_guest_id = 1


def manage_guest(guest_id: int = None, action: str = "add", **data) -> int:
    """Add, update or delete a guest."""
    global next_guest_id
    if action == "add":
        gid = next_guest_id
        next_guest_id += 1
        guests[gid] = {"name": data.get("name"), "email": data.get("email"), "category": data.get("category")}
        return gid
    elif action == "edit" and guest_id in guests:
        guests[guest_id].update(data)
        return guest_id
    elif action == "delete" and guest_id in guests:
        del guests[guest_id]
        return guest_id
    else:
        raise ValueError("Invalid action or guest_id")


def categorize_guest(guest_id: int, category: str) -> bool:
    """Assign a category to a guest."""
    if guest_id not in guests:
        return False
    guests[guest_id]["category"] = category
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
