from abc import ABC, abstractmethod
from src.domain.entities.category import Category

class CategoryInterface(ABC):
    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def list_categories(self) -> list[Category]:
        pass