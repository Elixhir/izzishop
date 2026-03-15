from src.domain.interfaces.category import CategoryInterface

class DeleteCategoryUseCase:
    def __init__(self, category_repository: CategoryInterface):
        self.category_repository = category_repository

    def execute(self, category_id: str):
        self.category_repository.delete_category(category_id)