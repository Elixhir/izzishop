from src.domain.interfaces.category import CategoryInterface

class UpdateCategoryUseCase:
    def __init__(self, category_interface: CategoryInterface):
        self.category_interface = category_interface

    def execute(self, category_id: int, name: str):
        category = self.category_interface.get_by_id(category_id)
        if not category:
            raise ValueError("Category not found")

        category.name = name
        self.category_interface.update_category(category_id, name)