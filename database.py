import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker


def _engine_kwargs(url: str) -> dict:
    """Return engine kwargs tailored to the backend."""
    kwargs = {"future": True, "pool_pre_ping": True}
    if url.startswith("sqlite"):
        # Allow SQLite to be used in-memory or from multiple threads.
        kwargs["connect_args"] = {"check_same_thread": False}
    return kwargs


def _build_engine(url: str):
    return create_engine(url, **_engine_kwargs(url))


def _create_engine_with_fallback():
    primary_url = os.getenv("DATABASE_URL")
    default_url = "sqlite:///events.db"
    candidate_url = primary_url or default_url

    try:
        engine = _build_engine(candidate_url)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine, candidate_url, False
    except Exception:
        # Fall back to an in-memory SQLite database when the configured
        # database is unreachable, keeping the app operational.
        fallback_url = "sqlite+pysqlite:///:memory:"
        engine = _build_engine(fallback_url)
        return engine, fallback_url, True


engine, ACTIVE_DATABASE_URL, USING_FALLBACK_DB = _create_engine_with_fallback()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()
