from src.domain.interfaces.store import StoreInterface

class CreateStoreUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self, store_data: dict) -> dict:
        return  self.store_repository.create_store(store_data)