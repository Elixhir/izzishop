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