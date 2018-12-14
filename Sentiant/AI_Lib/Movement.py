from Sentiant.Model.Point import Point
from Sentiant.Model.Rock import Rock
from Sentiant.Model.Dirt import Dirt
from Sentiant.Model.Ant import Ant

class Pathfind:
    def __init__(self, FOV, relativeDest, relativeStart=Point(0, 0)):
        self.start = relativeStart
        self.dest = relativeDest
        self.map = FOV # `[FOVSolid, FOVFloor]` from `Map.GetFOV`

    def Steps(self, obstacleClass=(Rock, Dirt, Ant), steps=[]):
        if not steps:
            steps = [self.start]

        if steps[-1] == self.dest:
            return steps

        for next in sorted( [steps[-1] + Point( 0,  1), \
                             steps[-1] + Point( 0, -1), \
                             steps[-1] + Point( 1,  0), \
                             steps[-1] + Point(-1,  0)], \
                            key=lambda e: len(self.dest - e) ):
            if any([isinstance(t[next], obstacleClass) for t in self.maps]) \
                    or next == steps[-1]:
                continue

            #print(next)
            steps.append(next)

            nextSteps = self.Steps(obstacleClass, steps)
            if len(nextSteps) == len(steps):
                if steps[-1] == self.dest:
                    return steps
                steps.pop(-1)
            else:
                break

        return steps

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
