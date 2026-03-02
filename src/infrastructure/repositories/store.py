from src.domain.interfaces.store import StoreInterface
from src.infrastructure.database import db
from src.infrastructure.models.store import StoreModel

class StoreRepository(StoreInterface):

    def create_store(self, store_data: dict) -> dict:
        new_store = StoreModel(**store_data)
        db.session.add(new_store)
        db.session.commit()
        db.session.refresh(new_store)
        return new_store