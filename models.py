
"""Database models for the event management tool."""

from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, UniqueConstraint
from database import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(String)
    time = Column(String)
    location = Column(String)
    price = Column(Float)
    program = Column(Text)


class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    category = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))


class User(Base):
    """Simple user model with roles and password hash."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint("email"),)
