from src.domain.interfaces.product import ProductInterface

class GetProductsByStore:
    def __init__(self, product_repository = ProductInterface):
        self.product_repository = product_repository

    def execute(self, store_id: str, page: int = 1, per_page: int = 10):
        
        products, total = self.product_repository.get_products_by_store(
            store_id=store_id,
            page=page,      
            per_page=per_page 
        )
        
        return products, total