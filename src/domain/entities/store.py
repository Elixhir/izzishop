from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from src.domain.utilities.generate_slug import generate_slug

@dataclass
class Store:
    name: str
    slug: str = field(init=False)
    active: bool = True
    id: Optional[int] = None
    
    def __post_init__(self):
        self.slug = generate_slug(self.name)