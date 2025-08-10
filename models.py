from sqlalchemy import Column, Integer, String, Float, Text
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
