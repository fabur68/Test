"""Event management functions."""

from typing import List, Dict
from data_store import events

next_event_id = 1


def create_event(name: str, date: str, time: str, location: str, price: float,
                 program_points: List[str]) -> int:
    """Create a new event and return its id."""
    global next_event_id
    event_id = next_event_id
    next_event_id += 1
    events[event_id] = {
        "name": name,
        "date": date,
        "time": time,
        "location": location,
        "price": price,
        "program": program_points,
    }
    return event_id


def update_event(event_id: int, **changes) -> bool:
    """Update fields of an existing event."""
    if event_id not in events:
        return False
    events[event_id].update(changes)
    return True


def delete_event(event_id: int) -> bool:
    """Delete an event by its id."""
    return events.pop(event_id, None) is not None
