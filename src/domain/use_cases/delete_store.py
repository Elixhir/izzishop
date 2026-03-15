from src.domain.interfaces.store import StoreInterface

class DeleteStoreUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self, store_id: int) -> None:
        self.store_repository.delete_store(store_id=store_id)