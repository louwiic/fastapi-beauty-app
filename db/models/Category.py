from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Service

class Category(Timestamp, Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    avatar =  Column(String(200), nullable=True)
    sku = Column(String(200), nullable=True)
    
    service = relationship("Service", back_populates='category')
    
