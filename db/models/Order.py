from email.policy import default
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp

class Order(Timestamp, Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False, default=False)
    
    user_id =  Column(Integer, ForeignKey("users.id"))
    booking_id =  Column(Integer, ForeignKey("bookings.id"))
    
    user_order = relationship("User",back_populates='order')
    user_booking = relationship("Booking",back_populates='order')

    
    