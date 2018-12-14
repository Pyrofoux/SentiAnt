from random import Random

from Sentiant.Model.Cfg import Cfg

class MapManager:
    def __init__(self, map=None, width=Cfg.WIDTH, height=Cfg.HEIGHT, \
                 rockRatio=.06, breadAmount=42, seed=None):
        self.rng = Random(seed) if seed else Random()

        self.map = map if map else Map(w=width, h=height)

        self.rockRatio = rockRatio
        self.breadAmount = breadAmount

        self.queens = []

    def RegisterQueen(self, queenTile, queenPos):
        """Register a queen to account for in generation"""
        self.queens.append((queenTile, queenPos))

    def ShouldBeRockAt(self, i, j):
        return self.rng.random() < self.rockRatio

    def Generate(self):
        """Generate and returns maps according to settings"""
        w, h = self.map.width, self.map.height

        # Generate dirt with a ratio of rock.
        for i in range(w):
            for j in range(h):
                isRock = self.ShouldBeRockAt(i, j)
                self.map.layerSolid[i, j] = Rock(-1) if isRock else Dirt(-1)

        # Generate ant nests around each queen positions.
        for tile, pos in self.queens:
            # Hollow area out.
            for i in range(-Cfg.NEST_RADIUS, Cfg.NEST_RADIUS*2 +1):
                for j in range(-Cfg.NEST_RADIUS, Cfg.NEST_RADIUS*2 +1):
                    if abs(i - .5) + abs(j - .5) < 5 \
                            and pos.x + i >= 0 and pos.x + i < self.map.layerSolid.GetWidth()\
                            and pos.y + j >= 0 and pos.y ++ j < self.map.layerSolid.GetHeight():
                        self.map.layerSolid[pos.x + i, pos.y + j] = None

            # Place starter bread pieces.
            around = [ (-1, +0), (-1, +1), (+0, -1), (+0, +2),
                        (+1, -1), (+1, +2), (+2, +0), (+2, +1) ]
            for i, j in around:
                self.map.layerFloor[pos.x + i, pos.y + j] = Bread(-1)

            # Set-up queen tiles in a 2 by 2.
            for i in range(2):
                for j in range(2):
                    self.map.layerSolid[pos.x + i, pos.y + j] = tile

        # Place THA COOKIE!
        self.map.layerFloor[w // 2, h // 2] = Cookie(-1)

        # Drop every left-overs bread pieces (deducts starter ones).
        for k in range(self.breadAmount - len(self.queens) * 8):
            i, j = self.rng.randrange(w), self.rng.randrange(h)
            while self.map.layerFloor[i, j] \
                  or isinstance(self.map.layerSolid[i, j], QueenTile):
                i, j = self.rng.randrange(w), self.rng.randrange(h)
            self.map.layerFloor[i, j] = Bread(-1)

        return self.map

    def Save(self, dirName):
        """Save a generated map"""
        from os import pathsep
        dirName+= "" if dirName.endswith(pathsep) else pathsep

        fileSolid = open(dirName + "layerSolid.txt", "w")
        fileFloor = open(dirName + "layerFloor.txt", "w")
        fileSettings = open(dirName + "settings.txt", "w")

        w, h = self.map.width, self.map.height

        for i in range(w):
            for j in range(h):
                fileSolid.write('r' if isinstance(self.map.layerSolid[i, j], Rock) \
                           else 'd' if isinstance(self.map.layerSolid[i, j], Dirt) \
                           else ' ')
                fileFloor.write('b' if isinstance(self.map.layerFloor[i, j], Bread) \
                           else 'c' if isinstance(self.map.layerFloor[i, j], Cookie) \
                           else ' ')
            fileSolid.write('\n')
            fileFloor.write('\n')

        fileSettings.write("w=" + str(w) + "\n")
        fileSettings.write("h=" + str(h) + "\n")

    def Load(self, dirName):
        """Load a generated map"""
        from os import pathsep
        dirName+= "" if dirName.endswith(pathsep) else pathsep

        bufferSolid = open(dirName + "layerSolid.txt", "w").readlines()
        bufferFloor = open(dirName + "layerFloor.txt", "w").readlines()
        settings = open(dirName + "settings.txt", "w").readlines()

        w = int(settings[0].split('=')[1].strip())
        h = int(settings[1].split('=')[1].strip())

        self.map = Map(w, h)

        for i in range(w):
            for j in range(h):
                self.map.layerSolid = bufferSolid[i][j]
                self.map.layerFloor = bufferFloor[i][j]

        return self.map

from Sentiant.Model.Map import Map
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Bread import Bread
from Sentiant.Model.Cookie import Cookie
from Sentiant.Model.QueenTile import QueenTile
