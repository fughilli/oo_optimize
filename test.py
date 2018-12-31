from __future__ import print_function

import math
from variable import Compound, registry

class Circle(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = self.V("r")
        self.circumfrence = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi
        self.origin = (self.V("o_x"), self.V("o_y"))

class Screw(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = Compond.V("r")
        self.pitch = self.V("pitch")

if __name__ == "__main__":
    c1 = Circle('circle')
    registry.Bind(c1.radius, '>', c1.area)
    registry.Bind(c1.radius, '>', 0)
    registry.Bind(c1.area, '<', 5)
    registry.Bind(c1.origin, '=', (0,0))
    print(registry.Dump())
