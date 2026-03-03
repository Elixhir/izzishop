from abc import ABC, abstractmethod
from src.domain.entities.category import Category

class CategoryInterface(ABC):
    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get_by_name_and_store(self, name: str, store_id: str) -> Category | None:
        pass
