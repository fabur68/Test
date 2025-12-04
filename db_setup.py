"""Create database tables for the event management app."""

from database import ACTIVE_DATABASE_URL, USING_FALLBACK_DB, Base, engine
import models  # noqa: F401 to register models


def init_db():
    Base.metadata.create_all(bind=engine)
    if USING_FALLBACK_DB:
        print("Using in-memory fallback database (primary connection unavailable).")
    else:
        print(f"Database initialized at {ACTIVE_DATABASE_URL}.")


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
