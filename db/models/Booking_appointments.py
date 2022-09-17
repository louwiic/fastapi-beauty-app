from enum import unique
from statistics import mode
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON, DateTime
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Service

class Appointment(Timestamp, Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    begins_at= Column(DateTime,nullable=False)
    ends_at= Column(DateTime, nullable=False)
    price= Column(Float, nullable=False)

    #booking = relationship("Booking_appointment", back_populates='appointment')


class Booking_appointment(Timestamp, Base):
    __tablename__ = "bookings_appointments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150),  nullable=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    bookings_id= Column(Integer, ForeignKey("bookings.id"))
    service_id= Column(Integer, ForeignKey("services.id"))
    
    
    #appointment = relationship("Appointment", back_populates='bookings_appointments')
    #booking_info= relationship("Booking", back_populates='bookings_appointments')
    #booking_appointement_service= relationship(Service, back_populates='bookings_appointments')
    

    

class Booking(Timestamp, Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    booking_ref = Column(String(150),  nullable=False)
    
    #appointment_infos = relationship("Booking_appointment", back_populates='booking_info')