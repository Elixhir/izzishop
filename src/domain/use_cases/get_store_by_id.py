from src.domain.interfaces.store import StoreInterface

class GetStoreByIdUseCase:

    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self, store_id: int):
        return self.store_repository.get_store_by_id(store_id)