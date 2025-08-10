"""User authentication helpers."""

from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User


def create_user(email: str, password: str, role: str) -> int:
    """Register a new user and return its id."""
    session: Session = SessionLocal()
    user = User(email=email, password_hash=generate_password_hash(password), role=role)
    session.add(user)
    session.commit()
    session.refresh(user)
    uid = user.id
    session.close()
    return uid


def authenticate_user(email: str, password: str) -> Optional[User]:
    """Return user if credentials are valid."""
    session: Session = SessionLocal()
    user = session.query(User).filter(User.email == email).first()
    if user and check_password_hash(user.password_hash, password):
        session.expunge(user)
        session.close()
        return user
    session.close()
    return None


def request_password_reset(email: str) -> bool:
    """Placeholder password reset implementation."""
    session: Session = SessionLocal()
    user = session.query(User).filter(User.email == email).first()
    session.close()
    if not user:
        return False
    print(f"Password reset link sent to {email}")
    return True


def verify_two_factor(code: str) -> bool:
    """Mock verification of a 2FA code."""
    return code == "123456"
