from manim import *
import numpy as np
import random
from kociemba import solver as sv

COLORS = {"U": WHITE, "R": "#B90000", "F": "#1DDF13",
          "D": "#FFD500", "L": "#F0720A", "B": "#0045AD"}

class Face(RoundedRectangle):
    def __init__(self, side_length, corner_radius, which):
        super().__init__(height=side_length, width=side_length, stroke_color=BLACK, stroke_width=4,
                shade_in_3d=True, corner_radius=corner_radius, fill_color=GRAY, fill_opacity=1)
        self.which = which

class Cube(VGroup):
    def __init__(self, side_length=2, corner_radius=0.1):
        self.side_length = side_length
        self.corner_radius = corner_radius
        self.face_map = { "F": (0, 1, 1), "B": (2, 1, 1), "R": (1, 0, 1), 
                           "L": (1, 2, 1), "U": (1, 1, 2), "D": (1, 1, 0) }
        sli = slice(None, None, None)
        self.faces_map = { "F": (1, sli, sli), "B": (1, sli, sli), "U": (sli, sli, 1),
                           "D": (sli, sli, 1), "L": (sli, 1, sli), "R": (sli, 1, sli) }
        self.faces = np.ndarray((3, 3, 3), dtype=object)

        super().__init__(fill_color=GRAY, fill_opacity=1, stroke_color=BLACK, stroke_width=4)

    def generate_points(self):
        for which, vect in ("F", LEFT), ("B", RIGHT), ("R", DOWN), ("L", UP), ("U", OUT), ("D", IN):
            face = Face(self.side_length, self.corner_radius, which)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
            self.faces[self.face_map[which]] = face

    def setcolor(self, which, color):
        self.get_face(which).set_fill(color)

    def get_face(self, which):
        return self.faces[self.face_map[which]]

    def turn(self, which, rot):
        self.faces[self.faces_map[which]] = np.rot90(self.faces[self.faces_map[which]], k=rot)

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
        self.face_map = { "F": (0, sli, sli), "B": (dim - 1, sli, sli), "U": (sli, sli, dim - 1),
                           "D": (sli, sli, 0), "L": (sli, dim - 1, sli), "R": (sli, 0, sli) }
        self.turn_axis = { "F": X_AXIS, "B": X_AXIS, "L": Y_AXIS,
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

        for which in self.face_map.keys():
            for cube in self.get_face(which):
                cube.get_face(which).set(fill_color=self.colors[which])

    def setcolor(self, pos, color):
        self.cubies[pos[1], pos[2], pos[3]].setcolor(pos[0], color)

    def get_face(self, which, flatten=True):
        face = self.cubies[self.face_map[which]]
        if flatten:
            return VGroup(*face.flatten())
        else:
            return face

    def turn(self, which, show=True):
        rot = 1 if which[0] in ["R", "F", "D"] else -1
        rot = rot * 2 if "2" in which else rot 
        rot = -rot if "'" in which else rot 
        np_rot = -rot if which[0] in ["L", "R"] else rot
        axis = self.turn_axis[which[0]]

        face = self.get_face(which[0])
        #VGroup(*self.cubies.flatten()).set_z_index(0)
        #face.set_z_index(-1)

        # turn face of each cube
        for cube in face:
            cube.turn(which[0], np_rot)
        # turn face of rubiks_cube
        self.cubies[self.face_map[which[0]]] = np.rot90(self.cubies[self.face_map[which[0]]], k=np_rot)

        if show:
            return Rotate(face, angle=rot*PI/2, axis=axis)
        else:
            face.rotate(angle=rot*PI/2, axis=axis)

    def disarray(self, moves=20, show=False, seed=None):
        rand = random.Random(seed)
        whichs = [i + j for i in self.face_map.keys() for j in ["", "2", "'"]]

        def show_disarray():
            for _ in range(moves):
                which = rand.choice(whichs)
                turn = self.turn(which, show=show)
                yield turn

        def hide_disarray():
            for _ in range(moves):
                which = rand.choice(whichs)
                self.turn(which, show=show)

        if show:
            return show_disarray()
        else:
            hide_disarray()
            return self

    def solve(self):
        # get state
        # UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
        state = ""
        for cube in np.rot90(self.get_face("U", False), 2).flatten():
            state += cube.get_face("U").which

        for cube in np.rot90(np.flip(self.get_face("R", False), (0, 1)), -1).flatten():
            state += cube.get_face("R").which

        for cube in np.rot90(np.flip(self.get_face("F", False), 0)).flatten():
            state += cube.get_face("F").which

        for cube in np.rot90(np.flip(self.get_face("D", False), 0), 2).flatten():
            state += cube.get_face("D").which

        for cube in np.rot90(np.flip(self.get_face("L", False), 0)).flatten():
            state += cube.get_face("L").which

        for cube in np.rot90(np.flip(self.get_face("B", False), (0, 1)), -1).flatten():
            state += cube.get_face("B").which

        turns = sv.solve(state).replace("3", "'").replace("1", "").split()
        for turn in turns:
            yield self.turn(turn)
