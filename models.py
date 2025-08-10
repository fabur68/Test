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


class RSVP(Base):
    __tablename__ = "rsvps"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    response = Column(String)
    __table_args__ = (UniqueConstraint("event_id", "guest_id"),)


class Seating(Base):
    __tablename__ = "seating"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    seat_id = Column(String)
    guest_id = Column(Integer, ForeignKey("guests.id"), nullable=True)
    __table_args__ = (UniqueConstraint("event_id", "seat_id"),)


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    amount = Column(Float)
    method = Column(String)
    status = Column(String)


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    guest_id = Column(Integer, ForeignKey("guests.id"))
    rating = Column(Integer)
    comment = Column(Text)


class User(Base):
    """Simple user model with roles and password hash."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint("email"),)
