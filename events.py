"""Event management functions backed by PostgreSQL."""

from typing import List, Dict

from data_store import Event, SessionLocal


def create_event(name: str, date: str, time: str, location: str, price: float,
                 program_points: List[str]) -> int:
    """Create a new event and return its id."""
    session = SessionLocal()
    event = Event(
        name=name,
        date=date,
        time=time,
        location=location,
        price=price,
        program=program_points,
    )
    session.add(event)
    session.commit()
    event_id = event.id
    session.close()
    return event_id


def update_event(event_id: int, **changes) -> bool:
    """Update fields of an existing event."""
    session = SessionLocal()
    event = session.get(Event, event_id)
    if not event:
        session.close()
        return False
    for key, value in changes.items():
        if hasattr(event, key):
            setattr(event, key, value)
    session.commit()
    session.close()
    return True


def delete_event(event_id: int) -> bool:
    """Delete an event by its id."""
    session = SessionLocal()
    event = session.get(Event, event_id)
    if not event:
        session.close()
        return False
    session.delete(event)
    session.commit()
    session.close()
    return True


def list_events() -> Dict[int, Dict]:
    """Return all events as a mapping of id to data."""
    session = SessionLocal()
    result = {
        e.id: {
            "name": e.name,
            "date": e.date,
            "time": e.time,
            "location": e.location,
            "price": e.price,
            "program": e.program,
        }
        for e in session.query(Event).all()
    }
    session.close()
    return result

