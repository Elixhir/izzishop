from src.domain.interfaces.product import ProductInterface
from src.domain.entities.product import Product

class UpdateProductUseCase:
    def __init__(self, product_repository: ProductInterface):
        self.product_repository = product_repository

    def execute(self, product_id: str, **kwargs): 
        
        existing_product = self.product_repository.get_by_id(product_id)
        if not existing_product:
            raise ValueError("Product not found")

        updated_product = Product(
            id=product_id,
            name=kwargs.get('name', existing_product.name),
            price=kwargs.get('price', existing_product.price),
            description=kwargs.get('description', existing_product.description),
            stock=kwargs.get('stock', existing_product.stock),
            image_url=kwargs.get('image_url', existing_product.image_url),
            active=kwargs.get('active', existing_product.active),
            store_id=existing_product.store_id,
            category_id=existing_product.category_id,
            size=kwargs.get('size', existing_product.size),
            color=kwargs.get('color', existing_product.color),
            quality=kwargs.get('quality', existing_product.quality)
        )

        return self.product_repository.update_product(product_id, updated_product)  