from manim import *

class Cube(VGroup):

    # RIGHT, UP, OUT ---> X, Y, Z
    def __init__(self, pos, side_length=2, corner_radius=0.2):
        self.pos = pos
        self.side_length = side_length
        self.corner_radius = corner_radius
        self.faces = {"F": (0, RIGHT), "B": (1, LEFT), "R": (2, UP), 
                      "L": (3, DOWN), "U": (4, OUT), "D": (5, IN)}

        super().__init__()

    def generate_points(self):
        for _, vect in self.faces.values():    # -> F, B, R, L, U, D
            face = RoundedRectangle(height=self.side_length, width=self.side_length, stroke_color=BLACK, stroke_width=4,
                    corner_radius=self.corner_radius, shade_in_3d=True, fill_color=BLUE, fill_opacity=1)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

    def __getitem__(self, key):
        return super(Cube, self).__getitem__(self.faces[key][0])
