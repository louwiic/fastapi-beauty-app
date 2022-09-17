from email.policy import default
import enum
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text, Boolean, Float
from sqlalchemy.orm import relationship
from ..db_setup import Base
from .mixins import Timestamp
from db.models import Etablissement, Review

class Role(enum.IntEnum):
    customer = 1
    staff = 2
    pro = 3


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(150), unique=True, nullable=False)
    lastname = Column(String(150), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), unique=True, nullable=False)
    phone = Column(Integer,unique=True, nullable=False)
    address = Column(String(200), unique=True, nullable=False)
    city = Column(String(200), nullable=False)
    zipcode = Column(Integer, nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    avatar = Column(String(200),  nullable=True)
    fcmToken = Column(String(200), nullable=True)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=True)
    
    etablissement = relationship("Etablissement", uselist=False, back_populates="etablissement_user")


    #etablissement = relationship(Etablissement, back_populates="user_etablissement", uselist=False)
    #rewiew = relationship(Review, back_populates="review_user")
    
