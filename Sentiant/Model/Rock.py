from .SolidEntity import SolidEntity

class Rock(SolidEntity):

    removable = True

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return "Rock #"+id