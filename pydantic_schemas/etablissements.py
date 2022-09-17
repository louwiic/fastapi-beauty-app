from typing import Any, List, Optional, Tuple
from pydantic import BaseModel
from datetime import datetime


class EtablissementBase(BaseModel):
    name: str
    description: str
    

class Schedules(BaseModel):
    day: str
    is_open: bool
    
class EtablissementCreate(EtablissementBase):
    ...
    address: str
    city: str
    lat: float
    lng: float
    phone: int
    logo: Optional[str] = None
    banner: str
    zipcode: int
    schedules: Optional[list] = None
    user_id: int

class Etablissement(EtablissementBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
