from src.domain.interfaces.product import ProductInterface

class GetTopExpensiveProductsUseCase:
    def __init__(self, product_repository: ProductInterface):
        self.product_repository = product_repository

    def execute(self, limit: int = 3) -> list:
        return self.product_repository.get_top_expensive_products(limit = limit)