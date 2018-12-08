from .Entity import Entity

class FloorEntity(Entity) :
    
    def __init__(self, id):
        super().__init__(id)
        self.id = id
