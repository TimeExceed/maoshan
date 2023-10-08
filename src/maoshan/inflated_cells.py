from .cgr_pb2 import CGRStartParams
from .geom import *
from .design_exchange_format import unescape

def load_inflated_cells(cgr_file: str) -> dict[str, Point]:
    pb = CGRStartParams()
    with open(cgr_file, 'rb') as fp:
        pb.ParseFromString(fp.read())

    res = {}
    for cell in pb.cells:
        name = bytes(cell.name, encoding='UTF-8')
        name = unescape(name)
        res[name] = Point(
            Distance.from_pm(cell.dx * 1000),
            Distance.from_pm(cell.dy * 1000),
        )
    return res

