from src.domain.use_cases.create_store import CreateStoreUseCase
from src.domain.interfaces.store import StoreInterface
from src.infrastructure.repositories.store import StoreRepository
from src.domain.use_cases.get_store_by_id import GetStoreByIdUseCase

def get_store_repository() -> StoreRepository:
    return StoreRepository()

def get_create_store_use_case() -> CreateStoreUseCase:
    store_repository = get_store_repository()
    return CreateStoreUseCase(store_repository)

def get_store_by_id_use_case() -> GetStoreByIdUseCase:
    store_repository = get_store_repository()
    return GetStoreByIdUseCase(store_repository)