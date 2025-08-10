"""Payment processing (mock)."""

from data_store import payments


def process_payment(guest_id: int, event_id: int, amount: float, method: str) -> None:
    """Record a payment for a guest."""
    payments.setdefault(guest_id, {})[event_id] = {
        "amount": amount,
        "method": method,
        "status": "paid",
    }


def payment_status(guest_id: int, event_id: int) -> str:
    """Return payment status for a guest."""
    return payments.get(guest_id, {}).get(event_id, {}).get("status", "unpaid")
