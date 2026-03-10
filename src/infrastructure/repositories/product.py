from src.domain.interfaces.product import ProductInterface
from src.infrastructure.models.product import ProductModel
from src.infrastructure.database import db
from src.domain.entities.product import Product

class ProductRepository(ProductInterface):

    def create_product(self, product: Product) -> Product:

        new_product = ProductModel(
            name=product.name,
            slug=product.slug,
            description=product.description,
            price=product.price,
            stock=product.stock,
            image_url=product.image_url,
            active=product.active,
            store_id=product.store_id,
            category_id=product.category_id
        )

        db.session.add(new_product)
        db.session.commit()
        db.session.refresh(new_product)

        return Product(
            id=new_product.id,
            name=new_product.name,
            price=new_product.price,
            stock=new_product.stock,
            store_id=new_product.store_id,
            category_id=new_product.category_id,
            description=new_product.description,
            image_url=new_product.image_url,
            active=new_product.active
        )
        
    def get_products_by_store(self, store_id: int) -> list[Product]:
        products = ProductModel.query.filter_by(store_id=store_id).all()
        return [
            Product(
                id=product.id,
                name=product.name,
                price=product.price,
                stock=product.stock,
                store_id=product.store_id,
                category_id=product.category_id,
                description=product.description,
                image_url=product.image_url,
                active=product.active
            ) for product in products
        ]
        
    def get_products_by_category_and_store(self, category_id, store_id):
        products = ProductModel.query.filter_by(category_id=category_id, store_id=store_id).all()
        return [
            Product(
                id=product.id,
                name=product.name,
                price=product.price,
                stock=product.stock,
                store_id=product.store_id,
                category_id=product.category_id,
                description=product.description,
                image_url=product.image_url,
                active=product.active
            ) for product in products
        ]