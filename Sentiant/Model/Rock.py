from Sentiant.Model import *

class Rock(SolidEntity):

    removable = True

    def __init__(self, id):
        super().__init__(self, id)
