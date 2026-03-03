from abc import ABC, abstractmethod
from src.domain.entities.store import Store

class StoreInterface(ABC):
    @abstractmethod
    def create_store(self, store: Store) -> Store:
        pass
    
    @abstractmethod
    def get_store_by_id(self, store_id: int) -> Store:
        pass