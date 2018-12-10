from .FloorEntity import FloorEntity

class Bread(FloorEntity):

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return "Bread #"+id