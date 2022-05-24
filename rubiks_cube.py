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
        sli = slice(None, None, None)
        self.faces = {"F": (0, sli, sli), "B": (dim - 1, sli, sli), "U": (sli, sli, dim - 1),
                      "D": (sli, sli, 0), "L": (sli, dim - 1, sli), "R": (sli, 0, sli)}
        
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

    def rotate(self, which):
        rot = 1 if which[0] in ["R", "F", "D"] else -1
        rot = rot * 2 if "2" in which else rot 
        rot = -rot if "'" in which else rot 
        np_rot = -rot if which[0] in ["L", "R"] else rot
        axis = self.get_axis(which[0])

        face = self.get_face(which[0])
        face.set_z_index(-1)

        self.cubies[self.faces[which]] = np.rot90(self.cubies[self.faces[which]], k=np_rot)

        return Rotate(face, angle=rot*PI/2, axis=axis)

    def get_axis(self, which):
        if which == "F" or which == "B":
            return X_AXIS
        elif which == "U" or which == "D":
            return Z_AXIS
        else:
            return Y_AXIS

    def get_face(self, which):
        return VGroup(*self.cubies[self.faces[which]].flatten())

    def __getitem__(self, key):
        return VGroup(*self.cubies[self.faces[key]].flatten())
