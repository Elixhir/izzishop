from dataclasses import dataclass, field
from typing import Optional
from src.domain.utilities.generate_slug import generate_slug

@dataclass
class Category:
    name: str
    slug: str = field(init=False)
    store_id: str
    active: bool = True
    id: Optional[int] = None
    
    def __post_init__(self):
        self.slug = generate_slug(self.name)