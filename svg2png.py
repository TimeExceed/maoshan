#!/usr/bin/python3
import argparse
import subprocess as sp
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Convert some svg's to png by rsvg-convert.")
    parser.add_argument('svg', metavar='svg', type=str, nargs='+',
                        help='svg files')
    args = parser.parse_args()
    return args

def convert(svg):
    svg_path = Path(svg)
    png_path = svg_path.with_suffix('.png')
    print('convert', svg_path, '->', png_path)
    with open(png_path, 'wb') as fp:
        sp.check_call(['rsvg-convert', svg_path], stdout=fp)

if __name__ == '__main__':
    args = parse_args()
    for svg in args.svg:
        convert(svg)
