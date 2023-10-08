from functools import total_ordering
from cmath import sqrt

@total_ordering
class Distance:
    def __init__(self) -> None:
        self._dist = 0.0

    def __str__(self) -> str:
        return str(self._dist)

    def to_float(self) -> float:
        return self._dist

    @classmethod
    def from_pm(cls, pm: float) -> "Distance":
        res = cls()
        res._dist = pm
        return res

    @staticmethod
    def zero() -> "Distance":
        return Distance()

    def copy(self) -> "Distance":
        res = Distance()
        res._dist = self._dist
        return res

    def __eq__(self, v: object) -> bool:
        if not isinstance(v, Distance):
            return NotImplemented
        return self._dist == v._dist

    def __lt__(self, rhs: object) -> bool:
        if not isinstance(rhs, Distance):
            return NotImplemented
        return self._dist < rhs._dist

    def __add__(self, rhs):
        x = self.copy()
        x._dist += rhs._dist
        return x

    def __sub__(self, rhs):
        x = self.copy()
        x._dist -= rhs._dist
        return x

    def __mul__(self, rhs):
        if isinstance(rhs, float):
            x = self.copy()
            x._dist *= rhs
            return x
        elif isinstance(rhs, Distance):
            return Area.from_pm2(self._dist * rhs._dist)
        else:
            return NotImplemented

    def __truediv__(self, rhs):
        if isinstance(rhs, float):
            x = self.copy()
            x._dist /= rhs
            return x
        elif isinstance(rhs, Distance):
            return self._dist / rhs._dist
        else:
            return NotImplemented

@total_ordering
class Area:
    def __init__(self) -> None:
        self._area = 0.0

    def __str__(self) -> str:
        return str(self._area)

    def to_float(self) -> float:
        return self._area

    @classmethod
    def from_pm2(cls, pm2: float):
        res = cls()
        res._area = pm2
        return res

    @staticmethod
    def zero():
        return Area()

    def copy(self):
        res = Area()
        res._area = self._area
        return res

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Area):
            return NotImplemented
        return self._area == rhs._area

    def __lt__(self, rhs: object) -> bool:
        if not isinstance(rhs, Area):
            return NotImplemented
        return self._area < rhs._area

    def __add__(self, rhs):
        x = self.copy()
        x._area += rhs._area
        return x

    def __sub__(self, rhs):
        x = self.copy()
        x._area -= rhs._area
        return x

    def __mul__(self, rhs: float):
        x = self.copy()
        x._area *= rhs
        return x

    def __truediv__(self, rhs: object):
        if isinstance(rhs, float):
            x = self.copy()
            x._area /= rhs
            return x
        elif isinstance(rhs, Area):
            return self._area / rhs._area
        else:
            return NotImplemented

@total_ordering
class Point:
    def __init__(self, x: Distance, y: Distance) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(%s,%s)' % (self.x, self.y)

    @staticmethod
    def origin():
        return Point(Distance.zero(), Distance.zero())

    def euclid(self) -> Distance:
        return sqrt(self.x * self.x + self.y * self.y)

    def manhattan(self) -> Distance:
        return abs(self.x) + abs(self.y)

    def copy(self):
        return Point(self.x.copy(), self.y.copy())

    def __eq__(self, v) -> bool:
        return self.x == v.x and self.y == v.y

    def __lt__(self, v) -> bool:
        if self.x < v.x:
            return True
        elif self.x == v.x and self.y < v.y:
            return True
        else:
            return False

    def __add__(self, rhs):
        res = self.copy()
        res.x += rhs.x
        res.y += rhs.y
        return res

    def __sub__(self, rhs):
        res = self.copy()
        res.x -= rhs.x
        res.y -= rhs.y
        return res

    def __mul__(self, rhs: float):
        res = self.copy()
        res.x *= rhs
        res.y *= rhs
        return res

    def __truediv__(self, rhs: float):
        res = self.copy()
        res.x /= rhs
        res.y /= rhs
        return res

class Rect:
    def __init__(self, ll: Point, ur: Point) -> None:
        assert ll.x <= ur.x
        assert ll.y <= ur.y
        self.ll = ll
        self.ur = ur

    def __str__(self) -> str:
        return '%s>%s' % (self.ll, self.ur)

    def copy(self):
        return Rect(self.ll.copy(), self.ur.copy())

    def lower_left(self) -> Point:
        return self.ll.copy()

    def upper_right(self) -> Point:
        return self.ur.copy()

    def lower_right(self) -> Point:
        return Point(self.ur.x.copy(), self.ll.y.copy())

    def upper_left(self) -> Point:
        return Point(self.ll.x.copy(), self.ur.y.copy())

    def center(self) -> Point:
        return (self.ll + self.ur) / 2.0

    def width(self) -> Distance:
        return self.ur.x - self.ll.x

    def height(self) -> Distance:
        return self.ur.y - self.ll.y

    def __add__(self, pt: Point):
        r = self.copy()
        r.ll += pt
        r.ur += pt
        return r

    def __sub__(self, pt: Point):
        r = self.copy()
        r.ll -= pt
        r.ur -= pt
        return r

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, Rect):
            return NotImplemented
        return self.ll == rhs.ll and self.ur == rhs.ur

    def overlap(self, rhs):
        llx = max(self.lower_left().x, rhs.lower_left().x)
        lly = max(self.lower_left().y, rhs.lower_left().y)
        urx = min(self.upper_right().x, rhs.upper_right().x)
        ury = min(self.upper_right().y, rhs.upper_right().y)
        if llx > urx or lly > ury:
            return None
        return Rect(Point(llx, lly), Point(urx, ury))

    def area(self) -> Area:
        w = self.width()._dist
        h = self.height()._dist
        res = Area()
        res._area = w * h
        return res
