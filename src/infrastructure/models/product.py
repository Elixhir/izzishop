from src.infrastructure.database import db
from uuid import uuid4

class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    store_id = db.Column(db.String(36), db.ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    category_id = db.Column(db.String(36), db.ForeignKey("categories.id", ondelete="SET NULL"))

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "price": self.price,
            "stock": self.stock,
            "store_id": self.store_id,
            "category_id": self.category_id
        }
