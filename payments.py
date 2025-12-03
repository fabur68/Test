"""Payment processing backed by the database."""

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment


def process_payment(guest_id: int, event_id: int, amount: float, method: str) -> None:
    """Record a payment for a guest."""
    with SessionLocal() as session:
        payment = Payment(
            guest_id=guest_id,
            event_id=event_id,
            amount=amount,
            method=method,
            status="paid",
        )
        session.add(payment)
        session.commit()


def payment_status(guest_id: int, event_id: int) -> str:
    """Return payment status for a guest."""
    with SessionLocal() as session:
        payment = session.query(Payment).filter_by(guest_id=guest_id, event_id=event_id).first()
        return payment.status if payment else "unpaid"
