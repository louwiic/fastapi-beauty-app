from email.policy import default
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Etablissement, User

class Favorite(Timestamp, Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id =  Column(Integer, ForeignKey("users.id"))
    etablissement_id =  Column(Integer, ForeignKey("etablissements.id"))
    
    #favorite_user = relationship(User, back_populates='favorites')
    #favorite_etablissement = relationship(Etablissement, back_populates='favorites')
    
    