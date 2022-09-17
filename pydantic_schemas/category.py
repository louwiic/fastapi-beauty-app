from typing import Any, List, Optional, Tuple
from pydantic import BaseModel
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: str
        
class CategoryCreate(CategoryBase):
    ...
    avatar: Optional[str] = None
    sku: str    

class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
