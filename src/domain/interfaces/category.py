from abc import ABC, abstractmethod
from src.domain.entities.category import Category

class CategoryInterface(ABC):
    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get_by_name_and_store(self, name: str, store_id: str) -> Category | None:
        pass

    @abstractmethod
    def get_by_id(self, category_id: str) -> Category | None:
        pass
    
    @abstractmethod
    def get_categories_by_store_id(self, store_id: str) -> list[Category]:
        pass
    
    @abstractmethod 
    def delete_category(self, category_id: str):
        pass