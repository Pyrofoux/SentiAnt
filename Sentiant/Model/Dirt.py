from Sentiant.Model import FloorEntity

class Dirt(FloorEntity):

    removable = True

    def __init__(self):
        super().__init__(self, id)

