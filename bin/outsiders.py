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
    regions = OrderedDict()
    ratio = maoshan.svg_util.ratio(b_def)
    for i,rect in enumerate(toml.load(FLOW).get('rects')):
        llx = rect.get('lower-left').get('x').get('value')
        lly = rect.get('lower-left').get('y').get('value')
        urx = rect.get('upper-right').get('x').get('value')
        ury = rect.get('upper-right').get('y').get('value')
        geo = Rect(
            Point(
                Distance.from_pm(llx),
                Distance.from_pm(lly)
            ),
            Point(
                Distance.from_pm(urx),
                Distance.from_pm(ury)
            )
        )
        regions[i] = Region(i, geo)
    
    print('label regions to cells')
    cell_in_which_region = OrderedDict()
    for i,cell_name in enumerate(b_def.cells):
        print(f"\r progress: {i}/{len(b_def.cells)}", flush=True, end="")
        for r_id in regions:
            region = regions[r_id]
            if region.contains(b_def.cells[cell_name].geo.center()):
                cell_in_which_region[cell_name] = r_id
                break
        else:
            cell_in_which_region[cell_name] = len(regions)
        
    
    print('\ndraw cells')
    for i, cell_name in enumerate(b_def.cells):
        print(f"\r progress: {i}/{len(b_def.cells)}", flush=True, end="")
        cell = a_def.cells[cell_name]
        r_id = cell_in_which_region[cell_name]
        elem = maoshan.svg_util.draw_rect(
            b_def.die_area,
            cell.geo,
            ratio,
            stroke= regions[r_id].color(),
            fill='none',
            fill_opacity="0",
        )
        elem.set_desc(title=str(cell_name, encoding='utf-8'))
        dwg.add(elem)
    print('\ndone.')