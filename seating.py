"""Seating plan management."""

from data_store import seating_plans


def create_seating_plan(event_id: int, seats: int) -> None:
    """Initialize a seating plan with a given number of seats."""
    seating_plans[event_id] = {f"S{n}": None for n in range(1, seats + 1)}


def select_seat(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Guest selects a seat if available."""
    plan = seating_plans.get(event_id)
    if not plan or seat_id not in plan or plan[seat_id] is not None:
        return False
    plan[seat_id] = guest_id
    return True


def assign_seat_manually(event_id: int, guest_id: int, seat_id: str) -> bool:
    """Organizer assigns a seat, overwriting existing assignment."""
    plan = seating_plans.get(event_id)
    if not plan or seat_id not in plan:
        return False
    plan[seat_id] = guest_id
    return True
