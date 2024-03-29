from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
from maoshan.svg_util import *
from maoshan.region import *
import toml
from itertools import *
from collections import OrderedDict

LEF = '/home/yongqi/repo/linden_cases/tigris/incr_dp/tigris231027-umc110-m3-10ns-cts_opt-setup/in/aio.pblef'
DEF = '/home/yongqi/repo/linden_cases/tigris/incr_dp/tigris231027-umc110-m3-10ns-cts_opt-setup/in/aio.pbdef'
FLOW = '/home/yongqi/repo/linden_detailed_placer/1_FLOW_INFO.toml'

if __name__ == '__main__':
    lef = maoshan.LibraryExchangeFormat(LEF)
    def_ = maoshan.DesignExchangeFormat(lef, DEF)
    def_.unescape()
    dwg = svgwrite.Drawing('flow.svg')
    marker = dwg.marker(insert=(5,5),size=(6,6),orient='auto',fill='white')
    marker.viewbox(0,0,10,10)
    marker.add(dwg.path(d="M 0 0 L 10 5 L 0 10 z"))
    dwg.defs.add(marker)
    raw_flow = toml.load(FLOW)
    print('parsing region info')
    regions = list()
    ratio = maoshan.svg_util.ratio(def_)
    regions = parse_from_toml(raw_flow)

    print('calculating density on region')
    for cell_name in def_.cells:
        cell = def_.cells[cell_name]
        for region in regions:
            if (overlap := cell.geo.overlap(region.geo)) is not None:
                region.density += overlap.area() / region.geo.area()
    
    palette = [
        (0.1, svgwrite.utils.rgb(255,204,204)),
        (0.5, svgwrite.utils.rgb(255,102,102)),
        (0.8, svgwrite.utils.rgb(204,0,0)),
        (0.9, svgwrite.utils.rgb(153,0,00)),
        (1.0, svgwrite.utils.rgb(102,0,0)),
        (None, svgwrite.utils.rgb(0,0,0)),
    ]

    print('drawing regions')
    for region in regions:
        color = maoshan.density_color(palette, region.density)
        elem = maoshan.svg_util.draw_rect(
            def_.die_area,
            region.geo,
            ratio,
            stroke='none',
            fill=color,
        )
        dwg.add(elem)


    print('drawing flows')
    normalize = 10
    for arrow in raw_flow['arrows']:
        normalize = min(5 / arrow['flow'], normalize)
    for arrow in raw_flow['arrows']:
        sx = arrow['from']['x']['value']
        sy = arrow['from']['y']['value']
        ex = arrow['to']['x']['value']
        ey = arrow['to']['y']['value']
        s = Point(Distance.from_pm(sx),Distance.from_pm(sy))
        e = Point(Distance.from_pm(ex),Distance.from_pm(ey))
        elem = maoshan.svg_util.draw_line(
            def_.die_area,
            s,
            e,
            ratio,
            stroke = 'white',
            fill = 'none',
            stroke_width = max(arrow['flow'] * normalize, 1),
        )
        elem.set_desc(title=str(arrow['flow']))
        line = dwg.add(elem)
        line['marker-end'] = marker.get_funciri()
    dwg.save()
