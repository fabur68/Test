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
    program_points = program_points or []
    with SessionLocal() as session:
        event = Event(
            name=name,
            date=date,
            time=time,
            location=location,
            price=price,
            program="|".join(program_points),
        )
        session.add(event)
        session.commit()
        session.refresh(event)
        return event.id


def update_event(event_id: int, **changes) -> Dict | None:
    """Update fields of an existing event. Return updated dict or None."""
    with SessionLocal() as session:
        event = session.get(Event, event_id)
        if not event:
            return None
        for key, value in changes.items():
            if hasattr(event, key):
                if key == "program" and isinstance(value, list):
                    value = "|".join(value)
                setattr(event, key, value)
        session.commit()
        session.refresh(event)
        return _event_to_dict(event)


def delete_event(event_id: int) -> bool:
    """Delete an event by its id."""
    with SessionLocal() as session:
        event = session.get(Event, event_id)
        if not event:
            return False
        session.delete(event)
        session.commit()
        return True


def get_all_events() -> List[Dict]:
    """Return all events as a list of dictionaries."""
    with SessionLocal() as session:
        return [_event_to_dict(e) for e in session.query(Event).all()]
