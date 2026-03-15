from src.domain.interfaces.store import StoreInterface
from src.domain.entities.store import Store

class UpdateStoreUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self, store_id: int, store_data) -> Store:
        return self.store_repository.update_store(store_id, store_data)