from Sentiant.Model.FloorEntity import FloorEntity

class Dirt(FloorEntity):

    removable = True

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return "Dirt #" + str(self.id)
