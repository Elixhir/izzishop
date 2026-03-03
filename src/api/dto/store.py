
class CreateStoreDTO:
    def __init__(self, name):
        self.name = name    
    
class DetailStoreDTO:

    def __init__(self, id, name, slug, active):
        self.id = id
        self.name = name
        self.slug = slug
        self.active = active

    @staticmethod
    def from_entity(store):
        return DetailStoreDTO(
            id=store.id,
            name=store.name,
            slug=store.slug,
            active=store.active,
        )