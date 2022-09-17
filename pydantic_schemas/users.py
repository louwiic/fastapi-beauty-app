from cgitb import text
from dataclasses import Field
from email.policy import default
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic_schemas.etablissements import Etablissement



class UserBase(BaseModel):
    firstname: str
    lastname: str
    role: int


class UserLogin(BaseModel):
    email: Optional[str]
    password: Optional[str]

class UserEditPassword(UserLogin):
    ...
    confirm_password: str    

class TokenJWT(BaseModel):
    token : str
 
class UserCreate(UserBase):
    ...
    password: str
    phone: int
    address: str
    city: str
    zipcode: int
    lat: float
    lng: float
    avatar: str
    email: EmailStr
    #fcmToken: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
