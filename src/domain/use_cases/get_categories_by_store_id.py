from src.domain.interfaces.category import CategoryInterface

class GetCategoriesByStoreId:
    def __init__(self, category_interface: CategoryInterface):
        self.category_interface = category_interface

    def execute(self, store_id: str) -> list:
        return self.category_interface.get_categories_by_store_id(store_id)