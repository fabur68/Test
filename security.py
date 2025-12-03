"""Security utilities and access control helpers."""

from functools import wraps
from flask import session, abort


def ensure_gdpr_compliance(data: dict) -> bool:
    """Placeholder GDPR compliance check."""
    required = {"consent": True}
    return all(data.get(k) == v for k, v in required.items())


def enable_two_factor_auth(user_id: int) -> None:
    """Mock enabling of 2FA."""
    print(f"2FA enabled for user {user_id}")


def require_roles(*roles):
    """Decorator to limit access to users with given roles."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = session.get("role")
            if user_role is None:
                abort(401)
            if user_role not in roles:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
