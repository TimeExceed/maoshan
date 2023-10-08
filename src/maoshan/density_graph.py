from .design_exchange_format import DesignExchangeFormat
from .geom import *
import bisect
from collections.abc import *
from itertools import *

class Grid:
    def __init__(self, geo: Rect) -> None:
        self.geo = geo
        self.density = 0.0

class DensityGraph(Iterable[Grid]):
    def __init__(self, field: Rect, hor_n: int, ver_n: int) -> None:
        self._hor_n = hor_n
        self._ver_n = ver_n
        self._hor_ruler = _ruler(field.lower_left().x, field.upper_right().x, hor_n)
        self._ver_ruler = _ruler(field.lower_left().y, field.upper_right().y, ver_n)
        self._grids = []
        for lower, upper in zip(self._ver_ruler, islice(self._ver_ruler, 1, None)):
            row = []
            for left, right in zip(self._hor_ruler, islice(self._hor_ruler, 1, None)):
                geo = Rect(
                    Point(left, lower),
                    Point(right, upper)
                )
                grid = Grid(geo)
                row.append(grid)
            assert len(row) == hor_n
            self._grids.append(row)
        assert len(self._grids) == ver_n

    def point_query(self, pt: Point) -> Grid:
        row, col = self._start_grid(pt)
        return self._grids[row][col]

    def rect_query(self, rect: Rect) -> Iterable[Grid]:
        start_row, start_col = self._start_grid(rect.lower_left())
        end_row, end_col = self._end_grid(rect.upper_right())
        res = []
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                g = self._grids[r][c]
                res.append(g)
        return res

    def __iter__(self) -> Iterator[Grid]:
        return chain.from_iterable(self._grids)

    def _start_grid(self, pt: Point) -> (int, int):
        row = bisect.bisect_right(self._ver_ruler, pt.y) - 1
        if row >= self._ver_n:
            row = self._ver_n - 1
        if row < 0:
            row = 0
        col = bisect.bisect_right(self._hor_ruler, pt.x) - 1
        if col >= self._hor_n:
            col = self._hor_n - 1
        if col < 0:
            col = 0
        return row, col

    def _end_grid(self, pt: Point) -> (int, int):
        row = bisect.bisect_left(self._ver_ruler, pt.y) - 1
        if row >= self._ver_n:
            row = self._ver_n - 1
        if row < 0:
            row = 0
        col = bisect.bisect_left(self._hor_ruler, pt.x) - 1
        if col >= self._hor_n:
            col = self._hor_n - 1
        if col < 0:
            col = 0
        return row, col

def _ruler(lower: Distance, upper: Distance, n: int) -> list[Distance]:
    assert upper >= lower
    assert n > 0
    step = (upper - lower) / float(n)
    res = []
    start = lower
    for _ in range(n):
        res.append(start)
        start += step
    assert res[-1] < upper
    res.append(upper)
    assert len(res) == n + 1
    return res

def area_density(def_: DesignExchangeFormat, hor_n: int, ver_n: int) -> DensityGraph:
    res = DensityGraph(def_.core_area(), hor_n, ver_n)
    for cell in def_.cells.values():
        for grid in res.rect_query(cell.geo):
            if (overlap := cell.geo.overlap(grid.geo)) is not None:
                grid.density += overlap.area() / grid.geo.area()
    return res

def point_charge_density(
        def_: DesignExchangeFormat,
        hor_n: int,
        ver_n: int,
        pc_map: dict[str, float]
    ) -> DensityGraph:
    res = DensityGraph(def_.core_area(), hor_n, ver_n)
    for cell in def_.cells.values():
        grid = res.point_query(cell.geo.center())
        if (pc := pc_map.get(cell.name)) is not None:
            grid.density += pc / grid.geo.area().to_float()
        else:
            grid.density += cell.geo.area() / grid.geo.area()
    return res
