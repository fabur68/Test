<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
"""Seating plan management backed by SQLAlchemy."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Seating
<<<<<<< HEAD
=======
=======
"""Seating plan management."""

from data_store import seating_plans
>>>>>>> main
>>>>>>> main


def create_seating_plan(event_id: int, seats: int) -> None:
    """Initialize a seating plan with a given number of seats."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    for n in range(1, seats + 1):
        session.add(Seating(event_id=event_id, seat_id=f"S{n}"))
    session.commit()
    session.close()
<<<<<<< HEAD
=======
=======
    seating_plans[event_id] = {f"S{n}": None for n in range(1, seats + 1)}
>>>>>>> main
>>>>>>> main


def select_seat(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Guest selects a seat if available."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
    if not seat or seat.guest_id is not None:
        session.close()
        return False
    seat.guest_id = guest_id
    session.commit()
    session.close()
<<<<<<< HEAD
=======
=======
    plan = seating_plans.get(event_id)
    if not plan or seat_id not in plan or plan[seat_id] is not None:
        return False
    plan[seat_id] = guest_id
>>>>>>> main
>>>>>>> main
    return True


def assign_seat_manually(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Organizer assigns a seat, overwriting existing assignment."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    seat = session.query(Seating).filter_by(event_id=event_id, seat_id=seat_id).first()
    if not seat:
        session.close()
        return False
    seat.guest_id = guest_id
    session.commit()
    session.close()
<<<<<<< HEAD
=======
=======
    plan = seating_plans.get(event_id)
    if not plan or seat_id not in plan:
        return False
    plan[seat_id] = guest_id
>>>>>>> main
>>>>>>> main
    return True
