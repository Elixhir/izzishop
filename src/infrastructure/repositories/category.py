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
        
    def get_by_id(self, category_id: str) -> Category | None:

        category_model = CategoryModel.query.filter_by(
            id=category_id
        ).first()

        if not category_model:
            return None

        return Category(
            id=category_model.id,
            name=category_model.name,
            store_id=category_model.store_id,
            active=category_model.active
        )
        
    def get_categories_by_store_id(self, store_id):
        categories = CategoryModel.query.filter_by(store_id=store_id).all()
        return [
            Category(
                id=category.id,
                name=category.name,
                store_id=category.store_id,
                active=category.active
            ) for category in categories
        ]
        
    def delete_category(self, category_id):
        category = CategoryModel.query.get(category_id)
        if not category:
            raise Exception("Category not found")
        db.session.delete(category)
        db.session.commit()