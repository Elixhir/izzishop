from src.domain.interfaces.store import StoreInterface

class GetAllStoresUseCase:
    def __init__(self, store_repository: StoreInterface):
        self.store_repository = store_repository

    def execute(self) -> list:
        return self.store_repository.get_all_stores()