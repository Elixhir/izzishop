from src.domain.interfaces.category import CategoryInterface
from src.domain.entities.category import Category
from src.infrastructure.models.category import CategoryModel
from src.infrastructure.database import db


class CategoryRepository(CategoryInterface):

    def create_category(self, category: Category) -> Category:
        new_category = CategoryModel(
            name=category.name,
            slug=category.slug,
            store_id=category.store_id,
            active=category.active
        )

        db.session.add(new_category)
        db.session.commit()
        db.session.refresh(new_category)

        return Category(
            id=new_category.id,
            name=new_category.name,
            store_id=new_category.store_id,
            active=new_category.active
        )


    def get_by_name_and_store(self, name: str, store_id: str) -> Category | None:

        category_model = CategoryModel.query.filter_by(
            name=name,
            store_id=store_id
        ).first()

        if not category_model:
            return None

        return Category(
            id=category_model.id,
            name=category_model.name,
            store_id=category_model.store_id,
            active=category_model.active
        )