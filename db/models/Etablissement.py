from email.policy import default
import enum
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship

from db.models import Service, Review,Favorite,User
from ..db_setup import Base
from .mixins import Timestamp


class Etablissement(Timestamp, Base):
    __tablename__ = "etablissements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    address = Column(String(200), unique=True,  nullable=False)
    city = Column(String(100), nullable=False)
    logo = Column(String(200), nullable=True)
    phone =  Column(Integer, unique=True, nullable=False)
    banner = Column(String(200), nullable=True)
    zipcode = Column(Integer, nullable=False)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
    schedules = Column(JSON, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    etablissement_user = relationship("User", back_populates="etablissement")
    
    service = relationship("Service", back_populates='etablissement')

    #user_etablissement = relationship("User", back_populates='etablissements')
    
    #review = relationship(Review, back_populates='review_etablissement')
    #Favorite = relationship(Favorite)
    
