from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime

class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    updated_at: Optional[datetime]
