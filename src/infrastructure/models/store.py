from src.infrastructure.database import db
from uuid import uuid4

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(80), nullable=False, unique=True)
    slug = db.Column(db.String(120), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)

    categories = db.relationship("CategoryModel", backref="store", lazy=True, cascade="all, delete")
    products = db.relationship("ProductModel", backref="store", lazy=True, cascade="all, delete")

    def __init__(self, name, slug):
        self.name = name
        self.slug = slug

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "active": self.active
        }
