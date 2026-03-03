from dataclasses import dataclass, field
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
class Category:
    name: str
    slug: str = field(init=False)
    store_id: str
    active: bool = True
    id: Optional[int] = None
    
    def __post_init__(self):
        self.slug = generate_slug(self.name)