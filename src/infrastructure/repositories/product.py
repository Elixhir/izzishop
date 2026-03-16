from src.domain.interfaces.product import ProductInterface
from src.infrastructure.models.product import ProductModel
from src.infrastructure.database import db
from src.domain.entities.product import Product
from src.infrastructure.storage.supabase_storage import SupabaseStorage

class ProductRepository(ProductInterface):
    def __init__(self):
        self.storage = SupabaseStorage()

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
            category_id=product.category_id,
            size=product.size,        
            color=product.color,     
            quality=product.quality    
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
            active=new_product.active,
            size=new_product.size,        
            color=new_product.color,       
            quality=new_product.quality   
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
                active=product.active,
                size=product.size,     
                color=product.color,       
                quality=product.quality   
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
                active=product.active,
                size=product.size,       
                color=product.color,       
                quality=product.quality    
            ) for product in products
        ]
        
    def get_top_expensive_products(self, limit):
        products = ProductModel.query.order_by(ProductModel.price.desc()).limit(limit).all()
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
                active=product.active,
                size=product.size,      
                color=product.color,      
                quality=product.quality    
            ) for product in products
        ]
        
    def delete_product(self, product_id: int) -> bool:

        product = ProductModel.query.get(product_id)

        if product.image_url:
            self.storage.delete_file(product.image_url)

        db.session.delete(product)
        db.session.commit()

        return True