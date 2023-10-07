from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
import svgwrite
from itertools import *

LEF = '/media/data/work/tmp/tigris-0922/all-in-one.pblef'
DEF = '/media/data/work/tmp/tigris-0922/flow011-rdp/umc110-m3-15ns-1.2area-ctoolfp/gp-debug/banyan_1695714673583.cmap.pbdef'
CMAP = '/media/data/work/tmp/tigris-0922/flow011-rdp/umc110-m3-15ns-1.2area-ctoolfp/gp-debug/banyan_1695714673583.cmap'


if __name__ == '__main__':
    lef = maoshan.LibraryExchangeFormat(LEF)
    def_ = maoshan.DesignExchangeFormat(lef, DEF)
    def_.unescape()
    cmap = maoshan.CongestionMap(def_, CMAP)
    ratio = maoshan.svg_util.ratio(def_)
    palette = [
        (0.5, svgwrite.utils.rgb(255,204,204)),
        (0.8, svgwrite.utils.rgb(255,102,102)),
        (1.0, svgwrite.utils.rgb(204,0,0)),
        (2.0, svgwrite.utils.rgb(153,0,00)),
        (None, svgwrite.utils.rgb(102,0,0)),
    ]

    profiles = [
        ('banyan_1695714673583.vertical.svg', maoshan.cmap.Axis.VERTICAL),
        ('banyan_1695714673583.horizontal.svg', maoshan.cmap.Axis.HORIZONTAL),
    ]
    for out_file, axis in profiles:
        dwg = svgwrite.Drawing(out_file)
        for tile in cmap:
            supply = tile.supply(axis)
            demand = tile.demand(axis)
            for d, c in palette:
                if d is None or supply == 0:
                    color = c
                    break
                elif demand / supply < d:
                    color = c
                    break
            dwg.add(maoshan.svg_util.draw_rect(def_.die_area, tile.geo, ratio, stroke='none', fill=color))
        dwg.save()

    palette = [
        (0.5, svgwrite.utils.rgb(255,204,204)),
        (0.8, svgwrite.utils.rgb(255,102,102)),
        (1.0, svgwrite.utils.rgb(204,0,0)),
        (2.0, svgwrite.utils.rgb(153,0,00)),
        (None, svgwrite.utils.rgb(102,0,0)),
    ]
    dwg = svgwrite.Drawing('banyan_1695714673583.density.svg')
    dg = maoshan.DensityGraph(def_, 30, 30)
    for g in dg.iter_grids():
        for d, c in palette:
            if d is None:
                color = c
            elif g.density() < d:
                color = c
                break
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo(), ratio, stroke='none', fill=color))
    dwg.save()
