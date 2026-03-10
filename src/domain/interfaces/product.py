from abc import ABC, abstractmethod
from src.domain.entities.product import Product

class ProductInterface(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass
    
    @abstractmethod
    def get_products_by_store(self, store_id: int) -> list[Product]:
        pass