class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __sub__(self, mate):
        return Point(self.x - mate.x, self.y - mate.y)

    def __add__(self, mate):
        return Point(self.x + mate.x, self.y + mate.y)

    def __len__(self, dest=None):
        """Usage: len(a - b) = distance from a to b"""
        if dest:
            return abs(self.x - dest.x) + abs(self.y - dest.y)
        return abs(self.x) + abs(self.y)

    def StepDistance(self, dest=None):
        """Returns distance in number of steps to take"""
        if dest:
            return ( (self.x-dest.x)**2 + (self.y-dest.y)**2 )**.5
        return (self.x**2 + self.y**2)**.5

    def __str__(self):
        return str(self.x) + "; " + str(self.y)

    def __getitem__(self, k):
        """So that point[0] = point.x and point[1] = point.y"""
        return self.y if k else self.x

    def InRange(self, xMin, xMax, yMin=None, yMax=None):
        if yMin and yMax:
            return self.x in range(xMin, xMax) and self.y in range(yMin, yMax)
        return self.x in range(xMin) and self.y in range(xMax)

    def __eq__(self, mate):
        if not isinstance(mate, Point):
            return False
        return self.x == mate.x and self.y == mate.y
