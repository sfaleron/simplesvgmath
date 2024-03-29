
# Will accept iterators or sequences of length two. Always returns Points.

from  __future__ import absolute_import
from  __future__ import division

# extra symbols for "chained" importing
from        math import sqrt, cos, sin, pi, atan2
from   mathtuple import mathtuple

import      attr

# corrections for coordinate system with inverted y-axis
import      math as _math

# negating the dependent vs independent variable amounts to the same thing,
# since sine is an odd function. The inverse tangent is also odd, which
# follows from sine being odd.

## ?? IVY ?? ##
#atan2 = lambda dy,dx: -_math.atan2(dy,dx)


@attr.s(cmp=False)
class IvyTransform(object):
    height = attr.ib()

    def __call__(self, x):
        return self.height-x

Point = mathtuple('Point', 2)

def dist(pt1, pt2):
    pt1, pt2 = Point.from_any(pt1, pt2)

    return pt1.dist(pt2)

def between(pt1, pt2, pos):
    pt1, pt2 = Point.from_any(pt1, pt2)

    return Point((pt2.x-pt1.x)*pos+pt1.x, (pt2.y-pt1.y)*pos+pt1.y)

def midpoint(pt1, pt2):
    pt1, pt2 = Point.from_any(pt1, pt2)

    return Point((pt1.x+pt2.x)/2, (pt1.y+pt2.y)/2)


def make_scaler(scale, cls=float):
    class Scale(cls):
        def __new__(cls_, x):
            return cls.__new__(cls_, x*scale)

        @property
        def px(self):
            return '{:f}px'.format(self)

    return Scale
