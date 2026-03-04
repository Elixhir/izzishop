from abc import ABC, abstractmethod
from src.domain.entities.product import Product

class ProductInterface(ABC):
    @abstractmethod
    def create_product(self, product: Product) -> Product:
        pass