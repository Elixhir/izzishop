from datetime import datetime
from typing import Optional
from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    slug: str
    description: Optional[str]
    price: float
    stock: int
    image_url: Optional[str]
    active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None