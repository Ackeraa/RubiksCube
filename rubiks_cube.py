from manim import *
import numpy as np
import random

COLORS = {"U": WHITE, "R": "#B90000", "F": "#009B48",
          "D": "#FFD500", "L": "#FF5900", "B": "#0045AD"}

class Cube(VGroup):
    def __init__(self, side_length=2, corner_radius=0.1):
        self.side_length = side_length
        self.corner_radius = corner_radius
        self.faces_map = { "F": (0, LEFT), "B": (1, RIGHT), "R": (2, DOWN), 
                           "L": (3, UP), "U": (4, OUT), "D": (5, IN) }

        super().__init__(fill_color=BLACK, fill_opacity=1, stroke_color=BLACK, stroke_width=4)

    def generate_points(self):
        for _, vect in sorted(self.faces_map.values(), key=lambda value:value[0]):    # -> F, B, R, L, U, D
            face = RoundedRectangle(height=self.side_length, width=self.side_length, stroke_color=BLACK, stroke_width=4,
                    corner_radius=self.corner_radius, shade_in_3d=True, fill_color=BLACK, fill_opacity=1, sheen_factor=1)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

    def set_color(self, which, color):
        self.get_face(which).set_fill(color)

    def get_face(self, which):
        return self[self.faces_map[which][0]]

class RubiksCube(VGroup):
    
    def __init__(self, dim=3, cube_side_length=1, colors=COLORS):
        # IN, RIGHT, UP ---> X, Y, Z
        super().__init__()
        self.dim = dim
        self.cube_side_length = cube_side_length
        self.colors =  colors
        self.cubies = np.ndarray((dim, dim, dim), dtype=Cube)
        self.fixed_face = []
        sli = slice(None, None, None)
        self.faces_map = { "F": (0, sli, sli), "B": (dim - 1, sli, sli), "U": (sli, sli, dim - 1),
                           "D": (sli, sli, 0), "L": (sli, dim - 1, sli), "R": (sli, 0, sli) }
        self.rotate_axis = { "F": X_AXIS, "B": X_AXIS, "L": Y_AXIS,
                             "R": Y_AXIS, "U": Z_AXIS, "D": Z_AXIS }
        
        self.generate_cubies()

    def generate_cubies(self):
        x_vg = VGroup()
        for x in range(self.dim):
            y_vg = VGroup()
            for y in range(self.dim):
                z_vg = VGroup()
                for z in range(self.dim):
                    cube = Cube(side_length=self.cube_side_length)
                    self.add(cube)
                    self.cubies[x][y][z] = cube
                    z_vg.add(cube)
                z_vg.arrange(OUT, buff=0)
                y_vg.add(z_vg)
            y_vg.arrange(UP, buff=0)
            x_vg.add(y_vg)
        x_vg.arrange(RIGHT, buff=0)

        for which in self.faces_map.keys():
            for cube in self.get_face(which):
                cube.get_face(which).set(fill_color=self.colors[which])

    def set_color(self, pos, color):
        cube = self.get_face(pos[0])[pos[1]*self.dim+pos[2]]
        cube.set_color(pos[0], color)

    def get_face(self, which):
        return VGroup(*self.cubies[self.faces_map[which]].flatten())

    def rotate(self, which, show=True):
        rot = 1 if which[0] in ["R", "F", "D"] else -1
        rot = rot * 2 if "2" in which else rot 
        rot = -rot if "'" in which else rot 
        np_rot = -rot if which[0] in ["L", "R"] else rot
        axis = self.rotate_axis[which[0]]

        face = self.get_face(which[0])
        VGroup(*self.cubies.flatten()).set_z_index(0)
        face.set_z_index(-1)

        self.cubies[self.faces_map[which[0]]] = np.rot90(self.cubies[self.faces_map[which[0]]], k=np_rot)

        #self.fix_render_bug(which[0])
        if show:
            return Rotate(face, angle=rot*PI/2, axis=axis)
        else:
            face.rotate(angle=rot*PI/2, axis=axis)

    def disarray(self, moves=20, show=False):
        whichs = [i + j for i in self.faces_map.keys() for j in ["", "2", "'"]]

        def show_disarray():
            for _ in range(moves):
                which = random.choice(whichs)
                rotate = self.rotate(which, show=show)
                yield rotate

        def hide_disarray():
            for _ in range(moves):
                which = random.choice(whichs)
                self.rotate(which, show=show)

        if show:
            return show_disarray()
        else:
            hide_disarray()

