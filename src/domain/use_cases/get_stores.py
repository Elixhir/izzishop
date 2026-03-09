from src.domain.interfaces.store import StoreInterface
from src.domain.entities.store import Store

class GetAllActiveStoresUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self) -> list[Store]:
        return self.store_repository.get_all_active_stores()