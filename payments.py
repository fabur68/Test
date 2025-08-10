<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
"""Payment processing backed by the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment
<<<<<<< HEAD
=======
=======
"""Payment processing (mock)."""

from data_store import payments
>>>>>>> main
>>>>>>> main


def process_payment(guest_id: int, event_id: int, amount: float, method: str) -> None:
    """Record a payment for a guest."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    payment = Payment(guest_id=guest_id, event_id=event_id, amount=amount,
                      method=method, status="paid")
    session.add(payment)
    session.commit()
    session.close()
<<<<<<< HEAD
=======
=======
    payments.setdefault(guest_id, {})[event_id] = {
        "amount": amount,
        "method": method,
        "status": "paid",
    }
>>>>>>> main
>>>>>>> main


def payment_status(guest_id: int, event_id: int) -> str:
    """Return payment status for a guest."""
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
    session: Session = SessionLocal()
    payment = session.query(Payment).filter_by(guest_id=guest_id, event_id=event_id).first()
    status = payment.status if payment else "unpaid"
    session.close()
    return status
<<<<<<< HEAD
=======
=======
    return payments.get(guest_id, {}).get(event_id, {}).get("status", "unpaid")
>>>>>>> main
>>>>>>> main
