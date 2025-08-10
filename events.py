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


def create_event(name: str, date: str, time: str, location: str, price: float,
                 program_points: List[str]) -> int:
    """Create a new event and return its id."""
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


def delete_event(event_id: int) -> bool:
    """Delete an event by its id."""
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
