from src.infrastructure.database import db
from uuid import uuid4

class CategoryModel(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=True)

    store_id = db.Column(db.String(36), db.ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)

    products = db.relationship("ProductModel", backref="category", lazy=True)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "store_id": self.store_id
        }
