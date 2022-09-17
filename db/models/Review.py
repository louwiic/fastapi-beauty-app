from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON, DateTime
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Etablissement, User

class Review(Timestamp, Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String(150),  nullable=False)
    comment = Column(Text, nullable=False)
    
    user_id= Column(Integer, ForeignKey("users.id"))
    etablissement_id= Column(Integer, ForeignKey("etablissements.id"))
    
    
    #review_user = relationship(User, back_populates='reviews')
    #review_etablissement= relationship(Etablissement, back_populates='reviews')


    