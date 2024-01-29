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
B_DEF = '/home/yongqi/repo/linden_cases/tigris/incr_dp/tigris231027-umc110-m3-10ns-cts_opt-setup/in/aio.pbdef'
A_DEF = '/home/yongqi/repo/linden_detailed_placer/target/aio.pbdef'
FLOW = '/home/yongqi/repo/linden_detailed_placer/1_FLOW_INFO.toml'

if __name__ == '__main__':
    
    dwg = svgwrite.Drawing('outsider.svg')
    lef = maoshan.LibraryExchangeFormat(LEF)
    b_def = maoshan.DesignExchangeFormat(lef, B_DEF) # Before Def
    b_def.unescape()
    a_def = maoshan.DesignExchangeFormat(lef, A_DEF) # After Def
    a_def.unescape()
    regions = list()
    ratio = maoshan.svg_util.ratio(b_def)
    regions = parse_from_toml((toml.load(FLOW)['rects']))
    print('label regions to cells')
    cell_in_which_region = OrderedDict()
    for i,cell_name in enumerate(b_def.cells):
        print(f"\r progress: {i+1}/{len(b_def.cells)}", flush=True, end="")
        for region in regions:
            if b_def.cells[cell_name].geo.center().in_rect(region.geo):
                cell_in_which_region[cell_name] = region
                break
        else:
            cell_in_which_region[cell_name] = len(regions)
        
    print('\ndraw cells')
    for i, cell_name in enumerate(b_def.cells):
        print(f"\r progress: {i+1}/{len(b_def.cells)}", flush=True, end="")
        cell = a_def.cells[cell_name]
        region = cell_in_which_region[cell_name]
        if cell.fixed == True:
            color = svgwrite.utils.rgb(150,150,150)
        else:
            color = region.color
        elem = maoshan.svg_util.draw_rect(
            b_def.die_area,
            cell.geo,
            ratio,
            stroke=color,
            fill='black',
            fill_opacity="0.02",
            stroke_width=0.5,
        )
        elem.set_desc(title=str(cell_name, encoding='utf-8'))
        dwg.add(elem)
    print('\ndone.')
    dwg.save()