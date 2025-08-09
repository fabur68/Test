"""Invitation and RSVP handling."""

from data_store import events, guests, rsvps


def send_invitation(event_id: int, guest_email: str) -> bool:
    """Mock sending an invitation by email."""
    event = events.get(event_id)
    if not event:
        return False
    print(f"Sending invitation for '{event['name']}' to {guest_email}")
    return True


def record_rsvp(event_id: int, guest_id: int, response: str) -> bool:
    """Record a guest's RSVP response."""
    if response not in {"Ja", "Nein", "Vielleicht"}:
        raise ValueError("Response must be 'Ja', 'Nein' or 'Vielleicht'")
    rsvps[(event_id, guest_id)] = response
    return True


def notify_organizer_rsvp(event_id: int, guest_id: int, response: str) -> None:
    """Notify organizer about a new RSVP."""
    event = events.get(event_id)
    guest = guests.get(guest_id)
    if event and guest:
        print(f"Organizer notified: {guest['name']} responded '{response}' for '{event['name']}'")
