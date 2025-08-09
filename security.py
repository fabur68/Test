"""Security utilities."""


def ensure_gdpr_compliance(data: dict) -> bool:
    """Placeholder GDPR compliance check."""
    required = {"consent": True}
    return all(data.get(k) == v for k, v in required.items())


def enable_two_factor_auth(user_id: int) -> None:
    """Mock enabling of 2FA."""
    print(f"2FA enabled for user {user_id}")
