from src.domain.use_cases.create_product import CreateProductUseCase
from src.domain.use_cases.create_store import CreateStoreUseCase
from src.domain.use_cases.delete_category import DeleteCategoryUseCase
from src.domain.use_cases.delete_product import DeleteProductUseCase
from src.domain.use_cases.delete_store import DeleteStoreUseCase
from src.domain.use_cases.get_categories_by_store_id import GetCategoriesByStoreId
from src.domain.use_cases.get_products_by_category_and_store import GetProductsByCategoryAndStore
from src.domain.use_cases.get_products_by_store import GetProductsByStore
from src.domain.use_cases.get_top_expensive_products import GetTopExpensiveProductsUseCase
from src.domain.use_cases.update_store import UpdateStoreUseCase
from src.infrastructure.repositories.product import ProductRepository
from src.infrastructure.repositories.store import StoreRepository
from src.domain.use_cases.get_store_by_id import GetStoreByIdUseCase
from src.domain.use_cases.create_category import CreateCategoryUseCase
from src.infrastructure.repositories.category import CategoryRepository
from src.domain.use_cases.get_stores import GetAllActiveStoresUseCase

def get_store_repository() -> StoreRepository:
    return StoreRepository()

def get_category_repository() -> CategoryRepository:
    return CategoryRepository()

def get_product_repository():
    return ProductRepository()


#Stores
def get_create_store_use_case() -> CreateStoreUseCase:
    store_repository = get_store_repository()
    return CreateStoreUseCase(store_repository)

def get_store_by_id_use_case() -> GetStoreByIdUseCase:
    store_repository = get_store_repository()
    return GetStoreByIdUseCase(store_repository)

def get_all_active_stores_use_case() -> GetAllActiveStoresUseCase:
    store_repository = get_store_repository()
    return GetAllActiveStoresUseCase(store_repository)

def get_delete_store_use_case() -> DeleteStoreUseCase:
    store_repository = get_store_repository()
    return DeleteStoreUseCase(store_repository)

def get_update_store_use_case() -> UpdateStoreUseCase:
    store_repository = get_store_repository()
    return UpdateStoreUseCase(store_repository)

#Categories
def get_create_category_use_case() -> CreateCategoryUseCase:
    category_repository = get_category_repository()
    return CreateCategoryUseCase(category_repository, get_store_repository())

def get_categories_by_store_id_use_case() -> GetCategoriesByStoreId:
    category_repository = get_category_repository()
    return GetCategoriesByStoreId(category_repository)

def get_delete_category_use_case() -> DeleteCategoryUseCase:
    category_repository = get_category_repository()
    return DeleteCategoryUseCase(category_repository)

#Products
def get_create_product_use_case():
    return CreateProductUseCase(
        product_repository=get_product_repository(),
        store_repository=StoreRepository(),
        category_repository=CategoryRepository()
    )
    
def get_products_by_store_use_case():
    return GetProductsByStore(
        product_repository=get_product_repository()
    )
    
def get_products_by_category_and_store_use_case():
    return GetProductsByCategoryAndStore(
        product_repository=get_product_repository()
    )  
    
def get_top_expensive_products_use_case():
    return GetTopExpensiveProductsUseCase(
        product_repository=get_product_repository()
    )
    
def get_delete_product_use_case():
    return DeleteProductUseCase(
        product_repository=get_product_repository()
    )