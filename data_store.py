"""Data storage layer backed by PostgreSQL using SQLAlchemy."""

import os

from sqlalchemy import Column, Float, Integer, String, create_engine, JSON
from sqlalchemy.orm import declarative_base, sessionmaker


# Database configuration via environment variable to allow flexible deployment.
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/postgres",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Event(Base):
    """Table representing an event."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String)
    time = Column(String)
    location = Column(String)
    price = Column(Float)
    program = Column(JSON)


class Guest(Base):
    """Table representing a guest."""

    __tablename__ = "guests"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    category = Column(String)


def init_db() -> None:
    """Create database tables if they do not exist."""
    Base.metadata.create_all(engine)


# Remaining in-memory stores for features not yet persisted
# RSVP responses keyed by (event_id, guest_id)
rsvps = {}

# Seating plans keyed by event_id, values are dict seat_id -> guest_id
seating_plans = {}

# Payments keyed by guest_id, value: dict(event_id -> status)
payments = {}

# Feedback keyed by (event_id, guest_id)
feedback = {}

# Offline cache keyed by user_id
offline_cache = {}

