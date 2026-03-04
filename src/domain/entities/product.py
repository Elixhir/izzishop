from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field
from src.domain.utilities.generate_slug import generate_slug

@dataclass
class Product:
    name: str
    slug: str = field(init=False)
    price: float
    stock: int
    active: bool
    store_id: str
    category_id: Optional[str]
    image_url: Optional[str]
    description: Optional[str]
    id: Optional[int] = None
    
    def __post_init__(self):
        self.slug = generate_slug(self.name)
        
    