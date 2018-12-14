from Sentiant.Model.Layer.Layer import Layer
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.QueenTile import QueenTile
from Sentiant.Model.Point import Point

class LayerSolid(Layer):

    def DiggyDiggyHole(self, coords):

        if type(self[coords.x, coords.y]) is Dirt:
            self[coords.x, coords.y] = None

        pass #TODO: log error

    def GetQueenTiles(self, team):

        for i in range(self.GetWidth()):
            for j in range(self.GetHeight()):
                if(type(self[i,j]) is QueenTile and self[i,j].team == team):

                    if(type(self[i+1,j]) is QueenTile):

                        if(type(self[i,j+1]) is QueenTile):
                            return [Point(i, j), Point(i+1, j), Point(i, j+1), Point(i+1, j+1)]
                        else:
                            return [Point(i, j-1), Point(i + 1, j-1), Point(i, j), Point(i + 1, j)]

                    else:

                        if (type(self[i, j + 1]) is QueenTile):
                            return [Point(i-1, j), Point(i, j), Point(i-1, j + 1), Point(i, j + 1)]
                        else:
                            return [Point(i-1, j-1), Point(i, j-1), Point(i-1, j), Point(i, j)]
        pass
