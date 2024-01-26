from .geom import Point, Rect
import svgwrite


class Region:
    region_color = [(230,25,75),(60,180,75),(255,225,25),(67,99,216),(245,130,49),(145,30,180),(66,212,244),(240,50,230),(191,239,69),(250,190,212),(70,153,144),(220,190,255),(154,99,36),(128,0,0),(170,255,195),(128,128,0),(255,216,177),(0,0,117),(169,169,169)]
    def __init__(self, id: int, geo: Rect):
        self.id = id
        self.geo = geo
        self.density = 0
        
    def color(self):
        r,g,b = Region.region_color[self.id % len(Region.region_color)]
        return svgwrite.utils.rgb(r,g,b)

    def contains(self,p: Point):
        r = self.geo
        if r.lower_left().x <= p.x and p.x <= r.upper_right().x and r.lower_left().y <= p.y and p.y <= r.upper_right().y:
            return True
        else:
            return False