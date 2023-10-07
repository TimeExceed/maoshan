from .banyan_cmap_pb2 import Cmap as PbCmap
from .banyan_cmap_pb2 import Tile as PbTile
from .design_exchange_format import DesignExchangeFormat
from .geom import *
from typing import Iterable, Iterator
from enum import Enum

class Axis(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

class Tile:
    def __init__(
            self,
            core_area: Rect,
            pb_cmap: PbCmap,
            row: int,
            col: int) -> None:
        ll = core_area.lower_left()
        w = pb_cmap.tileWidth * 1000
        h = pb_cmap.tileHeight * 1000
        self.geo = Rect(
            Point(Distance.from_pm(w * col), Distance.from_pm(h * row)),
            Point(Distance.from_pm(w * (col + 1)), Distance.from_pm(h * (row + 1))),
        ) + ll

        vtile = pb_cmap.vtiles[row * pb_cmap.wgrids + col]
        self.v_supply = vtile.supply
        self.v_demand = vtile.demand
        self.v_active = vtile.active

        htile = pb_cmap.htiles[row * pb_cmap.wgrids + col]
        self.h_supply = htile.supply
        self.h_demand = htile.demand
        self.h_active = htile.active

    def supply(self, axis: Axis) -> float:
        match axis:
            case Axis.HORIZONTAL:
                return self.h_supply
            case Axis.VERTICAL:
                return self.v_supply

    def demand(self, axis: Axis) -> float:
        match axis:
            case Axis.HORIZONTAL:
                return self.h_demand
            case Axis.VERTICAL:
                return self.v_demand

    def active(self, axis: Axis) -> bool:
        match axis:
            case Axis.HORIZONTAL:
                return self.h_active
            case Axis.VERTICAL:
                return self.v_active

class CongestionMap(Iterable[Tile]):
    def __init__(
            self,
            def_: DesignExchangeFormat,
            cmap_file: str) -> None:
        self._cmap = PbCmap()
        with open(cmap_file, 'rb') as fp:
            self._cmap.ParseFromString(fp.read())

        core_area = def_.core_area()
        self._tiles = []
        for row in range(self._cmap.hgrids):
            for col in range(self._cmap.wgrids):
                self._tiles.append(Tile(core_area, self._cmap, row, col))

    def __iter__(self) -> Iterator[Tile]:
        return iter(self._tiles)

