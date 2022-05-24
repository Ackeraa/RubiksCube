from manim import *
from cube import Cube 
import numpy as np

COLORS = [WHITE, "#B90000", "#009B48", "#FFD500", "#FF5900", "#0045AD"]
class RubiksCube(VGroup):
    
    def __init__(self, dim=3, cube_side_length=1, colors=COLORS):
        # IN, RIGHT, UP ---> X, Y, Z
        self.dim = dim
        self.cube_side_length = cube_side_length
        self.cubies = np.ndarray((dim, dim, dim), dtype=Cube)
        
        super().__init__(fill_color=BLUE, fill_opacity=1, stroke_color=BLACK, stroke_width=4)

    def generate_points(self):
        x_vg = VGroup()
        for x in range(self.dim):
            y_vg = VGroup()
            for y in range(self.dim):
                z_vg = VGroup()
                for z in range(self.dim):
                    cube = Cube((x, y, z), side_length=self.cube_side_length)
                    self.add(cube)
                    self.cubies[x][y][z] = cube
                    z_vg.add(cube)
                z_vg.arrange(OUT, buff=0)
                y_vg.add(z_vg)
            y_vg.arrange(UP, buff=0)
            x_vg.add(y_vg)
        x_vg.arrange(RIGHT, buff=0)

    def __getitem__(self, key):
        return self.cubies[key]

