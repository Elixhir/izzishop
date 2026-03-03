from src.domain.interfaces.store import StoreInterface
from src.domain.entities.store import Store

class CreateStoreUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self, store_data: Store) -> Store:
    
        store = Store(name=store_data.name)

        saved_store = self.store_repository.create_store(store)

        return saved_store