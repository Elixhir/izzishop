from src.domain.interfaces.product import ProductInterface
from src.domain.interfaces.store import StoreInterface
from src.domain.interfaces.category import CategoryInterface
from src.domain.entities.product import Product


class CreateProductUseCase:

    def __init__(
        self,
        product_repository: ProductInterface,
        store_repository: StoreInterface,
        category_repository: CategoryInterface
    ):
        self.product_repository = product_repository
        self.store_repository = store_repository
        self.category_repository = category_repository

    def execute(
        self,
        name: str,
        price: float,
        stock: int,
        store_id: str,
        category_id: str | None = None,
        description: str | None = None,
        image_url: str | None = None,
        active: bool = True
    ) -> Product:

        store = self.store_repository.get_store_by_id(store_id)
        if not store:
            raise Exception("Store not found")

        if category_id:
            category = self.category_repository.get_by_id(category_id)
            if not category:
                raise Exception("Category not found")

            if category.store_id != store_id:
                raise Exception("Category does not belong to this store")

        product = Product(
            name=name,
            price=price,
            stock=stock,
            store_id=store_id,
            category_id=category_id,
            description=description,
            image_url=image_url,
            active=active
        )

        saved_product = self.product_repository.create_product(product)

        return saved_product