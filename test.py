from __future__ import print_function

import math
from variable import Compound, registry, Vector

class Circle(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = self.V("r")
        self.circumfrence = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi
        self.origin = Vector((self.V("o_x"), self.V("o_y")))

def Tangent(a, b):
    (a.origin - b.origin).Magnitude() == (a.radius + b.radius)

class Screw(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = Compound.V("r")
        self.pitch = self.V("pitch")

if __name__ == "__main__":
    c1 = Circle('circle1')
    c1.radius > c1.area
    c1.radius > 0
    c1.area < 5
    c1.origin == Vector((0,0))
    c2 = Circle('circle2')
    Tangent(c1, c2)
    print(registry.Dump())


