from .pblefdef_pb2 import DesignExchangeFormat as PbDef
from .pblefdef_pb2 import Orient as PbOrient
from .geom import *
from collections import OrderedDict
from enum import Enum

class Orient(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'
    FN = 'FN'
    FS = 'FS'
    FE = 'FE'
    FW = 'FW'

    def __str__(self) -> str:
        return self.value

class Cell:
    def __init__(self, pb_cell, macros) -> None:
        self.name = pb_cell.name
        macro = macros[pb_cell.model_name]
        size = macro.size
        pl = pb_cell.place
        origin = Point(Distance.from_pm(pl.position.x), Distance.from_pm(pl.position.y))
        if pl.orient in (PbOrient.NORTH, PbOrient.SOUTH, PbOrient.FLIPPED_NORTH, PbOrient.FLIPPED_SOUTH):
            ur = Point(Distance.from_pm(size.width), Distance.from_pm(size.height))
            self.geo = Rect(Point.origin(), ur)
        else:
            ur = Point(Distance.from_pm(size.height), Distance.from_pm(size.width))
            self.geo = Rect(Point.origin(), ur)
        self.geo += origin
        if pl.orient == PbOrient.NORTH:
            self.orient = Orient.N
        elif pl.orient == PbOrient.SOUTH:
            self.orient = Orient.S
        elif pl.orient == PbOrient.EAST:
            self.orient = Orient.E
        elif pl.orient == PbOrient.WEST:
            self.orient = Orient.W
        elif pl.orient == PbOrient.FLIPPED_NORTH:
            self.orient = Orient.FN
        elif pl.orient == PbOrient.FLIPPED_SOUTH:
            self.orient = Orient.FS
        elif pl.orient == PbOrient.FLIPPED_EAST:
            self.orient = Orient.FE
        else:
            self.orient = Orient.FW

    def __str__(self) -> str:
        return "%s@%s|%s" % (self.name, self.geo, self.orient)

    def unescape(self) -> None:
        self.name = _unescape(self.name)

class DesignExchangeFormat:
    def __init__(self, lef, filename) -> None:
        self.def_ = PbDef()
        with open(filename, 'rb') as fp:
            self.def_.ParseFromString(fp.read())

        self.cells = OrderedDict()
        for c in self.def_.components:
            c = Cell(c, lef.macros)
            self.cells[c.name] = c

        assert len(self.def_.die_area.points) == 2
        self.die_area = Rect(
            Point(Distance.from_pm(self.def_.die_area.points[0].x), Distance.from_pm(self.def_.die_area.points[0].y)),
            Point(Distance.from_pm(self.def_.die_area.points[1].x), Distance.from_pm(self.def_.die_area.points[1].y)),
        )

    def unescape(self) -> None:
        res = OrderedDict()
        for c in self.cells.values():
            c.unescape()
            res[c.name] = c
        self.cells = res

def _unescape(name: bytes) -> bytes:
    return name.replace(b'\/', b'/').replace(b'\[', b'[').replace(b'\]', b']')

