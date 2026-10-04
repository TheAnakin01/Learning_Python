import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, d):
        return cls(d/2)

    def area(self):
        return math.pi * self.radius * self.radius

a = Circle(5)
print(a.area())

b = Circle.from_diameter(10)
print(b.area())

