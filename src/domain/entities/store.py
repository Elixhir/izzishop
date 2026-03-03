from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import re
import unicodedata

def generate_slug(name: str) -> str:
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")

    name = name.lower()

    name = re.sub(r"\s+", "-", name)

    name = re.sub(r"[^a-z0-9\-]", "", name)

    name = re.sub(r"-+", "-", name)

    return name.strip("-")

@dataclass
class Store:
    name: str
    slug: str = field(init=False)
    active: bool = True
    id: Optional[int] = None
    
    def __post_init__(self):
        self.slug = generate_slug(self.name)