"""Communication utilities."""

from data_store import guests


def send_message(recipient_ids, subject: str, body: str) -> None:
    """Send a message to recipients (mock)."""
    if recipient_ids == "all":
        recipients = guests.values()
    else:
        recipients = [guests.get(gid) for gid in recipient_ids if gid in guests]
    for r in recipients:
        print(f"To {r['email']}: {subject}\n{body}\n")


def push_notification(guest_id: int, message: str) -> bool:
    """Send a push notification (mock)."""
    guest = guests.get(guest_id)
    if not guest:
        return False
    print(f"Push to {guest['name']}: {message}")
    return True


def send_reminder(event_id: int, guest_id: int = None) -> None:
    """Send reminder emails. If guest_id is None, send to all."""
    if guest_id:
        target_ids = [guest_id] if guest_id in guests else []
    else:
        target_ids = list(guests.keys())
    for gid in target_ids:
        print(f"Reminder sent to {guests[gid]['email']} for event {event_id}")
