"""Seating plan management backed by SQLAlchemy."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Seating


def create_seating_plan(event_id: int, seats: int) -> None:
    """Initialize a seating plan with a given number of seats."""
    session: Session = SessionLocal()
    for n in range(1, seats + 1):
        session.add(Seating(event_id=event_id, seat_id=f"S{n}"))
    session.commit()
    session.close()


def select_seat(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Guest selects a seat if available."""
    session: Session = SessionLocal()
    seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
    if not seat or seat.guest_id is not None:
        session.close()
        return False
    seat.guest_id = guest_id
    session.commit()
    session.close()
    return True


def assign_seat_manually(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Organizer assigns a seat, overwriting existing assignment."""
    session: Session = SessionLocal()
    seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
    if not seat:
        session.close()
        return False
    seat.guest_id = guest_id
    session.commit()
    session.close()
    return True
