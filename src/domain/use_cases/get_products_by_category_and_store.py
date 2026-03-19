from src.domain.interfaces.product import ProductInterface

class GetProductsByCategoryAndStore:
    def __init__(self, product_repository: ProductInterface):
        self.product_repository = product_repository

    def execute(self, category_id: int, store_id: int, page: int = 1, per_page: int = 10) -> list:
        offset = (page - 1) * per_page
        
        products, total = self.product_repository.get_products_by_category_and_store(
            category_id=category_id,
            store_id=store_id,
            offset=offset,
            limit=per_page
        )
        return products, total