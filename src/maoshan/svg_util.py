from .design_exchange_format import DesignExchangeFormat
from .geom import Distance, Rect, Point
import svgwrite

def ratio(def_: DesignExchangeFormat) -> Distance:
    die_w = def_.die_area.width()
    die_h = def_.die_area.height()
    return min(die_w, die_h) / 1000.0

def draw_rect(die: Rect, to_draw: Rect, ratio: Distance, **kwargs) -> svgwrite.shapes.Rect:
    x = (to_draw.upper_left().x - die.lower_left().x) / ratio
    y = (die.upper_right().y - to_draw.upper_left().y) / ratio
    w = to_draw.width() / ratio
    h = to_draw.height() / ratio
    return svgwrite.shapes.Rect((x, y), (w, h), **kwargs)

def draw_line(die: Rect, start: Point, end: Point, ratio: Distance, **kwargs) -> svgwrite.shapes.Line:
    sx = (start.x - die.lower_left().x) / ratio
    sy = (die.upper_right().y - start.y) / ratio
    ex = (end.x - die.lower_left().x) / ratio
    ey = (die.upper_right().y - end.y) / ratio
    return svgwrite.shapes.Line((sx, sy), (ex, ey), **kwargs)

def density_color(palette, density):
    for d, c in palette:
        if d is None:
            return c
        elif density < d:
            return c
    assert False
