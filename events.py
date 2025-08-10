<<<<<<< HEAD
"""Event management functions backed by SQLAlchemy."""

from typing import List, Dict
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Event


def _event_to_dict(event: Event) -> Dict:
    return {
        "id": event.id,
        "name": event.name,
        "date": event.date,
        "time": event.time,
        "location": event.location,
        "price": event.price,
        "program": event.program.split("|") if event.program else [],
    }
=======
"""Event management functions."""

from typing import List, Dict
from data_store import events

next_event_id = 1
>>>>>>> main


def create_event(name: str, date: str, time: str, location: str, price: float,
                 program_points: List[str]) -> int:
    """Create a new event and return its id."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    event = Event(name=name, date=date, time=time,
                  location=location, price=price,
                  program="|".join(program_points))
    session.add(event)
    session.commit()
    session.refresh(event)
    event_id = event.id
    session.close()
    return event_id


def update_event(event_id: int, **changes) -> Dict | None:
    """Update fields of an existing event. Return updated dict or None."""
    session: Session = SessionLocal()
    event = session.get(Event, event_id)
    if not event:
        session.close()
        return None
    for key, value in changes.items():
        if hasattr(event, key):
            if key == "program" and isinstance(value, list):
                value = "|".join(value)
            setattr(event, key, value)
    session.commit()
    session.refresh(event)
    data = _event_to_dict(event)
    session.close()
    return data
=======
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
>>>>>>> main


def delete_event(event_id: int) -> bool:
    """Delete an event by its id."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    event = session.get(Event, event_id)
    if not event:
        session.close()
        return False
    session.delete(event)
    session.commit()
    session.close()
    return True


def get_all_events() -> List[Dict]:
    """Return all events as a list of dictionaries."""
    session: Session = SessionLocal()
    data = [_event_to_dict(e) for e in session.query(Event).all()]
    session.close()
    return data
=======
    return events.pop(event_id, None) is not None
>>>>>>> main
