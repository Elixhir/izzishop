from src.api.dto import store
from src.domain.interfaces.store import StoreInterface
from src.infrastructure.database import db
from src.infrastructure.models.store import StoreModel
from src.domain.entities.store import Store

class StoreRepository(StoreInterface):

    def create_store(self, store: Store) -> Store:
        
        model = StoreModel(
                name=store.name,
                slug=store.slug,
            )
        db.session.add(model)
        db.session.commit()
        db.session.refresh(model)
        return model
    
    def get_store_by_id(self, store_id):
        store = StoreModel.query.get(store_id)
        if not store:
            raise Exception("Store not found")
        return store
    
    def get_all_active_stores(self):
        return StoreModel.query.filter(StoreModel.active == True).all()
    
    def delete_store(self, store_id):
        store = StoreModel.query.get(store_id)
        if not store:
            raise Exception("Store not found")
        db.session.delete(store)
        db.session.commit()
        
    def update_store(self, store_id, store):
        store_model = StoreModel.query.get(store_id)
        if not store_model:
            raise Exception("Store not found")
        
        store_model.name = store.name
        store_model.slug = store.slug
        store_model.active = store.active
        
        db.session.commit()
        db.session.refresh(store_model)
        return store_model
        