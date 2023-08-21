from .design_exchange_format import DesignExchangeFormat
from .geom import *
from collections.abc import *
import bisect

class Grid:
    def __init__(self, dg, row: int, col: int) -> None:
        self._density_graph: DensityGraph = dg
        self._row = row
        self._col = col

    def increase_density(self, density: float) -> None:
        self._density_graph._density_grids[self._row][self._col] += density

    def geo(self) -> Rect:
        llx = self._density_graph._hor_ruler[self._col]
        urx = self._density_graph._hor_ruler[self._col + 1]
        lly = self._density_graph._ver_ruler[self._row]
        ury = self._density_graph._ver_ruler[self._row + 1]
        return Rect(Point(llx, lly), Point(urx, ury))

    def density(self) -> float:
        return self._density_graph._density_grids[self._row][self._col]

class DensityGraph:
    def __init__(
            self,
            def_: DesignExchangeFormat,
            hor_n: int,
            ver_n: int) -> None:
        assert hor_n > 0
        assert ver_n > 0
        die = def_.die_area
        self._hor_n = hor_n
        self._ver_n = ver_n
        self._hor_ruler = _ruler(die.lower_left().x, die.upper_right().x, hor_n)
        assert len(self._hor_ruler) == self._hor_n + 1
        self._ver_ruler = _ruler(die.lower_left().y, die.upper_right().y, ver_n)
        assert len(self._ver_ruler) == self._ver_n + 1
        self._density_grids = _init_density_grids(hor_n, ver_n)
        assert len(self._density_grids) == self._ver_n
        assert len(self._density_grids[0]) == self._hor_n
        for cell in def_.cells.values():
            start_row, start_col = self._start_grid(cell.geo.lower_left())
            end_row, end_col = self._end_grid(cell.geo.upper_right())
            for r in range(start_row, end_row+1):
                for c in range(start_col, end_col+1):
                    g = self._grid(r, c)
                    if (overlap := g.geo().overlap(cell.geo)) is not None:
                        g.increase_density(overlap.area() / g.geo().area())

    def iter_grids(self) -> Iterator[Grid]:
        return (Grid(self, r, c) for r in range(self._ver_n) for c in range(self._hor_n))

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
        if row >= len(self._density_grids):
            row = len(self._density_grids) - 1
        if row < 0:
            row = 0
        col = bisect.bisect_left(self._hor_ruler, pt.x) - 1
        if col >= len(self._density_grids[0]):
            col = len(self._density_grids[0]) - 1
        if col < 0:
            col = 0
        return row, col

    def _grid(self, row: int, col: int) -> Grid:
        return Grid(self, row, col)

def _ruler(lower: Distance, upper: Distance, n: int) -> list[float]:
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
    return res

def _init_density_grids(hor_n: int, ver_n: int) -> list[list[float]]:
    ver = [0.0 for _ in range(ver_n)]
    return [ver.copy() for _ in range(hor_n)]

