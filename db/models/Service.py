from email.policy import default
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Category, Etablissement, Booking_appointments

class Service(Timestamp, Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)
    is_boosted = Column(Boolean, nullable=True, default=False)
    description = Column(Text, unique=True, nullable=False)
    
    category_id =  Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category",back_populates='service')

    etablissement_id =  Column(Integer, ForeignKey("etablissements.id"))    
    etablissement = relationship("Etablissement",back_populates='service')
    
    