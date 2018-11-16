class Rock(SolidEntity):

    destructible = false

    def __init__(self, id):
        SolidEntity.__init__(self, id)
