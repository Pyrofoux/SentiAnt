from Sentiant.Model.FloorEntity import FloorEntity

class Cookie(FloorEntity):

    def __init__(self, id):
        super().__init__(id)

    def __str__(self):
        return "Cookie #" + str(id)
