from .geom import Point, Rect
import svgwrite


class Region:
    def __init__(self, geo: Rect, color):
        self.geo = geo
        self.density = 0
        self.color = color
