from abc import ABC, abstractmethod
from src.domain.entities.product import Product

class ProductInterface(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list_products(self) -> list[Product]:
        pass