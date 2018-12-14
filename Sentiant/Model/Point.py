class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __sub__(self, mate):
        return Point(self.x - mate.x, self.y - mate.y)

    def __add__(self, mate):
        return Point(self.x + mate.x, self.y + mate.y)

    def __len__(self):
        """Usage: len(a - b) = distance from a to b"""
        return (self.x**2 + self.y**2)**.5

    def StepDistance(self, dest=None):
        """Returns distance in number of steps to take"""
        if dest:
            return abs(self.x - dest.x) + abs(self.y - dest.y)
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return str(self.x) + "; " + str(self.y)

    def __getitem__(self, k):
        """So that point[0] = point.x and point[1] = point.y"""
        return self.y if k else self.x
