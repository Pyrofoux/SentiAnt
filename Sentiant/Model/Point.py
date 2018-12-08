class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __sub__(self, mate):
        return Point(self.x - mate.x, self.y - mate.y)

    def __add__(self, mate):
        return Point(self.x + mate.x, self.y + mate.y)

    def __len__(self):
        """ Usage: len(a - b) = distance from a to b"""
        return (self.x**2 + self.y**2)**.5

    def StepDistance(self, dest):
        """Returns distance in number of steps to take"""
        return (self.x - dest.x) + (self.y - dest.y)
