from src.domain.interfaces.product import ProductInterface

class GetProductsByCategoryAndStore:
    def __init__(self, product_interface: ProductInterface):
        self.product_interface = product_interface

    def execute(self, category_id: int, store_id: int) -> list:
        return self.product_interface.get_products_by_category_and_store(category_id, store_id)