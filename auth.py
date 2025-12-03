"""User authentication helpers."""

from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User


def create_user(email: str, password: str, role: str) -> int:
    """Register a new user and return its id."""
    with SessionLocal() as session:
        existing = session.query(User).filter(User.email == email).first()
        if existing:
            raise ValueError("email already registered")
        user = User(email=email, password_hash=generate_password_hash(password), role=role)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id


def authenticate_user(email: str, password: str) -> Optional[User]:
    """Return user if credentials are valid."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.email == email).first()
        if user and check_password_hash(user.password_hash, password):
            session.expunge(user)
            return user
    return None


def request_password_reset(email: str) -> bool:
    """Placeholder password reset implementation."""
    with SessionLocal() as session:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return False
    print(f"Password reset link sent to {email}")
    return True


def verify_two_factor(code: str) -> bool:
    """Mock verification of a 2FA code."""
    return code == "123456"
