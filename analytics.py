"""Analytics and reporting utilities."""

from data_store import Guest, SessionLocal, rsvps, payments, seating_plans


def dashboard_overview(event_id: int) -> dict:
    """Return a simple overview for an event."""
    session = SessionLocal()
    total_guests = session.query(Guest).count()
    session.close()
    responses = {"Ja": 0, "Nein": 0, "Vielleicht": 0}
    for (e_id, _), resp in rsvps.items():
        if e_id == event_id:
            responses[resp] += 1
    paid = sum(
        1
        for (g_id, e_id), status in [((g, e), p["status"]) for g, ev in payments.items() for e, p in ev.items()]
        if e_id == event_id and status == "paid"
    )
    return {
        "total_guests": total_guests,
        "responses": responses,
        "payments": paid,
    }


def generate_report(event_id: int) -> dict:
    """Generate a detailed report."""
    overview = dashboard_overview(event_id)
    seats = seating_plans.get(event_id, {})
    overview["seats_assigned"] = sum(1 for s in seats.values() if s is not None)
    return overview

