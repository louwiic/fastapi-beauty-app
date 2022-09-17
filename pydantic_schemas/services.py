from typing import Any, List, Optional, Tuple
from unicodedata import category
from pydantic import BaseModel
from datetime import datetime


class ServiceBase(BaseModel):
    name: str
    description: Optional[str]= None
        
class ServiceCreate(ServiceBase):
    ...
    is_boosted: Optional[bool] = None
    category_id: int
    etablissement_id: int    

class Service(ServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
