from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
import svgwrite
from itertools import *

# LEF = '/media/data/work/linden_cases/ispd18/ispd18_test1/all-in-one.pblef'
# DEF = '/media/data/work/linden_cases/ispd18/ispd18_test1/gp.pbdef'
LEF = '/media/data/work/tmp/f/all-in-one.pblef'
DEF = '/media/data/work/tmp/f/place_after_drv_before_dp.pbdef'
LDP_DEF = '/media/data/work/tmp/f/dp.pbdef'
CTOOLS_DEF = '/media/data/work/tmp/f/ctool.dp.pbdef'

CONCERNED_CELLS = [
    b'u_cm3_dpu/u_cm3_dpu_fetch/u_cm3_dpu_fetch_ahbintf/instr_de_reg_13_',
    b'u_cm3_dpu/u_cm3_dpu_dec/U127',
    b'u_cm3_dpu/u_cm3_dpu_dec/U66',
    b'u_cm3_dpu/u_cm3_dpu_dec/U37',
    b'u_cm3_dpu/u_cm3_dpu_dec/U72',
    b'u_cm3_dpu/u_cm3_dpu_dec/U80',
    b'u_cm3_dpu/u_cm3_dpu_dec/U92',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U135',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U189',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U190',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U359',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U244',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U243',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U194',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U198',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U204',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U205',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U34',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U222',
    b'u_cm3_dpu/u_cm3_dpu_dec/u_cm3_dpu_32bit_dec/U218',
    b'u_cm3_dpu/u_cm3_dpu_dec/U145',
    b'u_cm3_dpu/u_cm3_dpu_dec/U314',
    b'u_cm3_dpu/u_cm3_dpu_dec/U315',
    b'u_cm3_dpu/u_cm3_dpu_dec/U319',
    b'u_cm3_dpu/u_cm3_dpu_dec/U322',
    b'u_cm3_dpu/u_cm3_dpu_dec/U90',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U362',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U350',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U467',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U471',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U472',
    b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U129',
    b'u_cm3_dpu/u_cm3_dpu_exec/U158',
    b'u_cm3_dpu/u_cm3_dpu_dec/U42',
    b'u_cm3_dpu/u_cm3_dpu_dec/U41',
    b'u_cm3_dpu/u_cm3_dpu_dec/U215',
    b'u_cm3_dpu/u_cm3_dpu_dec/U18',
    b'u_cm3_dpu/u_cm3_dpu_dec/U32',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U256',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U257',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U237',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U127',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U139',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U173',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U189',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U99',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U190',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U174',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U310',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U114',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U88',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U87',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U246',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U175',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U211',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U96',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U236',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U179',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U191',
    b'u_cm3_dpu/u_cm3_dpu_regbank/U244',
    b'u_cm3_dpu/u_cm3_dpu_regbank/rf_pc_fwd_ex_reg_31_',
]

if __name__ == '__main__':
    lef = maoshan.LibraryExchangeFormat(LEF)
    def_ = maoshan.DesignExchangeFormat(lef, DEF)
    ldp = maoshan.DesignExchangeFormat(lef, LDP_DEF)
    ctool = maoshan.DesignExchangeFormat(lef, CTOOLS_DEF)
    assert ldp.die_area == def_.die_area
    assert ctool.die_area == def_.die_area
    ctool.unescape()
    dg = maoshan.DensityGraph(def_, 30, 30)
    ratio = maoshan.svg_util.ratio(def_)
    palette = [
        (0.1, svgwrite.utils.rgb(255,204,204)),
        (0.5, svgwrite.utils.rgb(255,102,102)),
        (0.8, svgwrite.utils.rgb(204,0,0)),
        (0.9, svgwrite.utils.rgb(153,0,00)),
        (None, svgwrite.utils.rgb(102,0,0)),
    ]
    dwg = svgwrite.Drawing('test.svg')
    for g in dg.iter_grids():
        for d, c in palette:
            if d is None:
                color = c
            elif g.density() < d:
                color = c
                break
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo(), ratio, stroke='none', fill=color))
    for cell_name in CONCERNED_CELLS:
        cell = def_.cells[cell_name]
        ldp_cell = ldp.cells[cell_name]
        elem = maoshan.svg_util.draw_rect(
            def_.die_area,
            ldp_cell.geo,
            ratio,
            stroke='white',
            fill='white',
            fill_opacity="0",
        )
        elem.set_desc(title=str(cell_name, encoding='utf-8'))
        dwg.add(elem)
        dwg.add(maoshan.svg_util.draw_line(def_.die_area, cell.geo.center(), ldp_cell.geo.center(), ratio, stroke='white', fill='none'))
        if (ctool_cell := ctool.cells.get(cell_name)) is not None:
            elem = maoshan.svg_util.draw_rect(
                def_.die_area,
                ctool_cell.geo,
                ratio,
                stroke='green',
                fill='green',
                fill_opacity="0",
            )
            elem.set_desc(title=str(cell_name, encoding='utf-8'))
            dwg.add(elem)
            dwg.add(maoshan.svg_util.draw_line(def_.die_area, cell.geo.center(), ctool_cell.geo.center(), ratio, stroke='green', fill='none'))
        else:
            print("%s is missing in ctool's result" % cell_name)
    for cell0_name, cell1_name in zip(CONCERNED_CELLS, islice(CONCERNED_CELLS, 1, None)):
        cell0 = ldp.cells[cell0_name]
        cell1 = ldp.cells[cell1_name]
        # cell0 = ctool.cells[cell0_name]
        # cell1 = ctool.cells[cell1_name]
        dwg.add(maoshan.svg_util.draw_line(def_.die_area, cell0.geo.center(), cell1.geo.center(), ratio, stroke='blue', fill='none'))
    dwg.save()
