from .pblefdef_pb2 import LibraryExchangeFormat as PbLef
from collections import OrderedDict

class LibraryExchangeFormat:
    def __init__(self, filename) -> None:
        self.lef = PbLef()
        with open(filename, 'rb') as fp:
            self.lef.ParseFromString(fp.read())
        self.macros = OrderedDict()
        for m in self.lef.macros:
            self.macros[m.name] = m
