from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Store:
    id: Optional[int] = None
    name: str
    slug: str
    active: bool = True
    created_at: datetime = None
    updated_at: datetime = None