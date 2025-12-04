"""Seating plan management backed by SQLAlchemy."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Seating


def create_seating_plan(event_id: int, seats: int) -> None:
    """Initialize a seating plan with a given number of seats."""
    with SessionLocal() as session:
        session.query(Seating).filter_by(event_id=event_id).delete()
        for n in range(1, seats + 1):
            session.add(Seating(event_id=event_id, seat_id=f"S{n}"))
        session.commit()


def select_seat(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Guest selects a seat if available."""
    with SessionLocal() as session:
        seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
        if not seat or seat.guest_id is not None:
            return False
        seat.guest_id = guest_id
        session.commit()
        return True


def assign_seat_manually(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Organizer assigns a seat, overwriting existing assignment."""
    with SessionLocal() as session:
        seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
        if not seat:
            return False
        seat.guest_id = guest_id
        session.commit()
        return True
