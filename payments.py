<<<<<<< HEAD
"""Payment processing backed by the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment
=======
"""Payment processing (mock)."""

from data_store import payments
>>>>>>> main


def process_payment(guest_id: int, event_id: int, amount: float, method: str) -> None:
    """Record a payment for a guest."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    payment = Payment(guest_id=guest_id, event_id=event_id, amount=amount,
                      method=method, status="paid")
    session.add(payment)
    session.commit()
    session.close()
=======
    payments.setdefault(guest_id, {})[event_id] = {
        "amount": amount,
        "method": method,
        "status": "paid",
    }
>>>>>>> main


def payment_status(guest_id: int, event_id: int) -> str:
    """Return payment status for a guest."""
<<<<<<< HEAD
    session: Session = SessionLocal()
    payment = session.query(Payment).filter_by(guest_id=guest_id, event_id=event_id).first()
    status = payment.status if payment else "unpaid"
    session.close()
    return status
=======
    return payments.get(guest_id, {}).get(event_id, {}).get("status", "unpaid")
>>>>>>> main
