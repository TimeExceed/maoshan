from .geom import Distance, Point, Rect
import svgwrite


class Region:
    colors = [(230,25,75),(60,180,75),(255,225,25),(67,99,216),(245,130,49),(145,30,180),(66,212,244),(240,50,230),(191,239,69),(250,190,212),(70,153,144),(220,190,255),(154,99,36),(128,0,0),(170,255,195),(128,128,0),(255,216,177),(0,0,117)]
    def __init__(self, geo: Rect, color):
        self.geo = geo
        self.density = 0
        self.color = color

def parse_from_toml(raw_flow):
    regions = list()
    for i,rect in enumerate(raw_flow['rects']):
        llx = rect['lower-left']['x']['value']
        lly = rect['lower-left']['y']['value']
        urx = rect['upper-right']['x']['value']
        ury = rect['upper-right']['y']['value']
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
        r,g,b = Region.colors[i % len(Region.colors)]
        regions.append(Region(geo, color=svgwrite.utils.rgb(r,g,b)))
    return regions