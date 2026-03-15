from src.domain.interfaces.product import ProductInterface

class DeleteProductUseCase:
    def __init__(self, product_repository: ProductInterface):
        self.product_repository = product_repository

    def execute(self, product_id: str):
        self.product_repository.delete_product(product_id)