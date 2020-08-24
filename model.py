from geometry import Vector, Circle, Tangent
from variable import Variable, registry
import math

c1 = Circle('circle1')
c1.radius > c1.area
c1.radius > 0
c1.area < 5
c1.origin == Vector((0, 0))
c2 = Circle('circle2')
c2.origin > Vector((-10, -10))
c2.origin < Vector((10, 10))
Tangent(c1, c2)
with open('/tmp/test.mzn', 'w+') as test_file:
    test_file.write(registry.Dump())
    print(registry.Dump())
    print("Wrote registry to", test_file.name)
