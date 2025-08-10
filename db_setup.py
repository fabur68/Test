"""Create database tables for the event management app."""

from database import engine, Base
import models  # noqa: F401 to register models


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database initialized.")
