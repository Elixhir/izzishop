from src.domain.interfaces.product import ProductInterface

class GetProductsByStore:
    def __init__(self, product_repository = ProductInterface):
        self.product_repository = product_repository

    def execute(self, store_id: int) -> list:
        return self.product_repository.get_products_by_store(store_id)