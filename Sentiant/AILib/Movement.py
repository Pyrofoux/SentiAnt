from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from Sentiant.Model.Point import Point
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Ant import Ant

class Pathfind:
    def __init__(self, FOV, relativeDest, relativeStart=Point(0, 0)):
        self.start = relativeStart
        self.dest = relativeDest
        self.maps = FOV # = `[FOVSolid, FOVFloor]` from `Map.GetFOV`

    def Steps(self, obstacleClass=(Rock, Dirt, Ant)):
        matrix = []

        for i in range(len(self.maps[0])):
            matrix.append([])
            for j in range(len(self.maps[0][0])):
                matrix.append(0 if any([isinstance(m[i][j], obstacleClass) for m in self.maps]) else 1)

        grid = Grid(matrix=matrix)

        start = grid.node(self.start.x, self.start.y)
        end = grid.node(self.dest.x, self.dest.y)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        return [Point(n.x, n.y) for n in path]

    def __len__(self):
        return len(self.Steps())


if __name__ == '__main__':
    table = [[0] * 12 for k in range(12)]
    table[1][2] = 'v'

    def tprint(t):
        for row in t:
            for it in row:
                print(it, end="")
            print()

    tprint(table)
    print()

    path = Pathfind(table, Point(10, 10), Point(1, 1))

    for point in path.Steps(str):
        table[point.x][point.y] = 1

    tprint(table)
    print()
