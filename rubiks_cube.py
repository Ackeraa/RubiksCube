from manim import *
from cube import Cube 

COLORS = [WHITE, "#B90000", "#009B48", "#FFD500", "#FF5900", "#0045AD"]
class RubiksCube(VGroup):
    
    def __init__(self, dim=3, cube_side_length=1, colors=COLORS):
        self.dim = dim
        self.cube_side_length = cube_side_length
        
        super().__init__(fill_color=BLUE, fill_opacity=1, stroke_color=BLACK, stroke_width=3)



    def generate_points(self):
        for x in range(self.dim):
            y_vg = VGroup()
            for y in range(self.dim):
                z_vg = VGroup()
                for z in range(self.dim):
                    cube = Cube((x, y, z), side_length=self.cube_side_length)
                    z_vg.add(cube)
                z_vg.arrange(IN, buff=0)
                y_vg.add(z_vg)
            y_vg.arrange(RIGHT, buff=0)
            self.add(y_vg)
        self.arrange(UP, buff=0)


