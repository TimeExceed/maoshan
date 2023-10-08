from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
import svgwrite
from itertools import *

LEF = '/media/data/work/tmp/tigris-0922/all-in-one.pblef'
DEF = '/media/data/work/tmp/tigris-0922/flow011-rdp/umc110-m3-15ns-1.2area-ctoolfp/gp-debug/banyan_1696751021219.cmap.pbdef'
CGR = '/media/data/work/tmp/tigris-0922/flow011-rdp/umc110-m3-15ns-1.2area-ctoolfp/gp-debug/banyan_1696751021219.cmap.cgr'

if __name__ == '__main__':
    lef = maoshan.LibraryExchangeFormat(LEF)
    def_ = maoshan.DesignExchangeFormat(lef, DEF)
    def_.unescape()
    ratio = maoshan.svg_util.ratio(def_)
    palette = [
        (0.1, svgwrite.utils.rgb(255,204,204)),
        (0.5, svgwrite.utils.rgb(255,102,102)),
        (0.8, svgwrite.utils.rgb(204,0,0)),
        (0.9, svgwrite.utils.rgb(153,0,00)),
        (None, svgwrite.utils.rgb(102,0,0)),
    ]

    dg = maoshan.point_charge_density(def_, 30, 30, {})
    dwg = svgwrite.Drawing('banyan_1696751021219.density.svg')
    for g in dg:
        color = maoshan.density_color(palette, g.density)
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo, ratio, stroke='none', fill=color))
    dwg.save()

    inflated_cells = maoshan.load_inflated_cells(CGR)
    pc_map = dict([(name, p.x.to_float() * p.y.to_float()) for name, p in inflated_cells.items()])
    dg = maoshan.point_charge_density(def_, 30, 30, pc_map)
    dwg = svgwrite.Drawing('banyan_1696751021219.inflated_density.svg')
    for g in dg:
        color = maoshan.density_color(palette, g.density)
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo, ratio, stroke='none', fill=color))
    dwg.save()
