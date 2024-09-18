from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="user")

class CoWorkingSpace(Base):
    __tablename__ = 'co_working_spaces'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    description = Column(String)
    price_per_hour = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="co_working_space")

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    co_working_space_id = Column(Integer, ForeignKey('co_working_spaces.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    total_amount = Column(Float)
    
    user = relationship("User", back_populates="bookings")
    co_working_space = relationship("CoWorkingSpace", back_populates="bookings")

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    amount = Column(Float)
    payment_method = Column(String)
    payment_date = Column(DateTime, default=datetime.utcnow)
    
    booking = relationship("Booking")
