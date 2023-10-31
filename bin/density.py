from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
import svgwrite
from itertools import *

LEF = '/media/data/work/tmp/rdp-aniso/all-in-one.pblef'
DEF = '/media/data/work/tmp/rdp-aniso/place_before_dp.pbdef'

if __name__ == '__main__':
    lef = maoshan.LibraryExchangeFormat(LEF)
    def_ = maoshan.DesignExchangeFormat(lef, DEF)
    def_.unescape()
    dg = maoshan.area_density(def_, 30, 30)
    palette = [
        (0.1, svgwrite.utils.rgb(255,204,204)),
        (0.5, svgwrite.utils.rgb(255,102,102)),
        (0.8, svgwrite.utils.rgb(204,0,0)),
        (0.9, svgwrite.utils.rgb(153,0,00)),
        (1.0, svgwrite.utils.rgb(102,0,0)),
        (None, svgwrite.utils.rgb(0,0,0)),
    ]
    dwg = svgwrite.Drawing('place_before_dp.rdp-aniso.density.svg')
    ratio = maoshan.svg_util.ratio(def_)
    for g in dg:
        color = maoshan.density_color(palette, g.density)
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo, ratio, stroke='none', fill=color))
    maoshan.svg_util.draw_palette(dwg, def_.die_area, ratio, palette)
    dwg.save()
