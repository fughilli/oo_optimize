from variable import Compound
from variable import Vector
import math


class Circle(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = self.V("r")
        self.circumfrence = self.radius * 2 * math.pi
        self.area = self.radius**2 * math.pi
        self.origin = Vector((self.V("o_x"), self.V("o_y")))


def Tangent(a, b):
    (a.origin - b.origin).Magnitude() == (a.radius + b.radius)


class Screw(Compound):
    def __init__(self, name):
        self.name = name
        self.radius = Compound.V("r")
        self.pitch = self.V("pitch")
