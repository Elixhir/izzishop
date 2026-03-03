from src.domain.interfaces.category import CategoryInterface
from src.domain.interfaces.store import StoreInterface
from src.domain.entities.category import Category


class CreateCategoryUseCase:

    def __init__(
        self,
        category_repository: CategoryInterface,
        store_repository: StoreInterface
    ):
        self.category_repository = category_repository
        self.store_repository = store_repository

    def execute(self, name: str, store_id: str) -> Category:

        store = self.store_repository.get_store_by_id(store_id)
        if not store:
            raise Exception("Store not found")

        category = Category(name=name, store_id=store_id)

        existing_category = self.category_repository.get_by_name_and_store(
            name=category.name,
            store_id=store_id
        )

        if existing_category:
            raise Exception("Category with this name already exists in this store")

        saved_category = self.category_repository.create_category(category)

        return saved_category