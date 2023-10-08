from pathlib import Path
import sys
sys.path.append('%s' % Path.cwd().joinpath('src').absolute())
import maoshan
import svgwrite
from itertools import *

# LEF = '/media/data/work/linden_cases/ispd18/ispd18_test1/all-in-one.pblef'
# DEF = '/media/data/work/linden_cases/ispd18/ispd18_test1/gp.pbdef'
LEF = '/media/data/work/tmp/b/all-in-one.pblef'
DEF = '/media/data/work/tmp/b/drv-fix.pbdef'
LDP_DEF = '/media/data/work/tmp/b/x.pbdef'
CTOOL_DEF = '/media/data/work/tmp/b/ctool.dp.pbdef'

CONCERNED_CELLS = [
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/addr_adder_in2_ex_reg_26_',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U775',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U776',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U366',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U873',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U874',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U880',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ahbintf/U883',
b'dpu_ahb_haddrd[30]_88_2',
b'dpu_ahb_haddrd[30]_87_1',
b'u_cm3_bus_matrix/u_cm3_mtx_input_stage_dcore/U17',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U33',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U152',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U7',
b'u_cm3_bus_matrix/dec_dcore_sel_bb_1_1',
b'u_cm3_bus_matrix/dec_dcore_sel_bb_n1_5_1',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U421',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U47',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U136',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U10',
b'u_cm3_bus_matrix/u_cm3_mtx_output_stage_dcode/U4',
b'u_cm3_bus_matrix/u_cm3_mtx_output_stage_dcode/n7_1_1',
b'u_cm3_bus_matrix/u_cm3_mtx_output_stage_dcode/U7',
b'u_cm3_bus_matrix/u_cm3_mtx_output_stage_dcode/U5',
b'u_cm3_bus_matrix/os_dcore_to_dcode_accept_8_1',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U45',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U139',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U74',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U44',
b'u_cm3_bus_matrix/u_cm3_mtx_bit_master/U244',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U18',
b'u_cm3_bus_matrix/u_cm3_mtx_decode_dcore/U9',
b'u_cm3_bus_matrix/u_cm3_mtx_input_stage_dcore/U67',
b'u_cm3_bus_matrix/u_cm3_mtx_input_stage_dcore/U3',
b'mtx_dpu_ahb_haddraccd_9_2',
b'mtx_dpu_ahb_haddraccd_8_1',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U104',
b'u_cm3_dpu/u_cm3_dpu_lsu/u_cm3_dpu_lsu_ctl/U64',
b'u_cm3_dpu/lsu_rf_wr_d_en_fast_ex_1_1',
b'u_cm3_dpu/u_cm3_dpu_exec/U31',
b'u_cm3_dpu/instr_br_pflush_ex[1]_18_1',
b'u_cm3_dpu/u_cm3_dpu_dec/U68',
b'u_cm3_dpu/u_cm3_dpu_dec/U71',
b'u_cm3_dpu/u_cm3_dpu_dec/U183',
b'u_cm3_dpu/u_cm3_dpu_dec/U34',
b'u_cm3_dpu/u_cm3_dpu_dec/U43',
b'u_cm3_dpu/u_cm3_dpu_dec/U65',
b'u_cm3_dpu/u_cm3_dpu_dec/U41',
b'u_cm3_dpu/u_cm3_dpu_dec/U215',
b'u_cm3_dpu/u_cm3_dpu_dec/U18',
b'u_cm3_dpu/u_cm3_dpu_dec/U32',
b'u_cm3_dpu/instr_used_word_de_25_2',
b'u_cm3_dpu/instr_used_word_de_24_1',
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
    def_.unescape()
    ldp = maoshan.DesignExchangeFormat(lef, LDP_DEF)
    ldp.unescape()
    ctool = maoshan.DesignExchangeFormat(lef, CTOOL_DEF)
    ctool.unescape()
    assert ldp.die_area == def_.die_area
    assert ctool.die_area == def_.die_area
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
    for g in dg:
        color = maoshan.density_color(palette, g.density)
        dwg.add(maoshan.svg_util.draw_rect(def_.die_area, g.geo, ratio, stroke='none', fill=color))
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
        dwg.add(maoshan.svg_util.draw_line(def_.die_area, cell0.geo.center(), cell1.geo.center(), ratio, stroke='blue', fill='none'))
        cell0 = ctool.cells[cell0_name]
        cell1 = ctool.cells[cell1_name]
        dwg.add(maoshan.svg_util.draw_line(def_.die_area, cell0.geo.center(), cell1.geo.center(), ratio, stroke='gray', fill='none'))
    dwg.save()
