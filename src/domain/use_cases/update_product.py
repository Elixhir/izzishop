from src.domain.interfaces.product import ProductInterface
from src.domain.entities.product import Product

class UpdateProductUseCase:
    def __init__(self, product_interface: ProductInterface):
        self.product_interface = product_interface

    def execute(self, product_id: int, product_data: dict):
        existing_product = self.product_interface.get_by_id(product_id)
        if not existing_product:
            raise ValueError("Product not found")

        updated_product = Product(
            id=product_id,
            name=product_data.get('name', existing_product.name),
            description=product_data.get('description', existing_product.description),
            price=product_data.get('price', existing_product.price),
            store_id=product_data.get('store_id', existing_product.store_id),
            active=product_data.get('active', existing_product.active),
            stock=product_data.get('stock', existing_product.stock),
            image_url=product_data.get('image_url', existing_product.image_url),
            size=product_data.get('size', existing_product.size),
            color=product_data.get('color', existing_product.color),
            quality=product_data.get('quality', existing_product.quality)
        )
        self.product_interface.update_product(product_id, updated_product)