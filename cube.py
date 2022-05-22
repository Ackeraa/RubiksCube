from manim import *

class Cube(VGroup):
    def __init__(self, pos, side_length=2, corner_radius=0.2):
        self.pos = pos
        self.side_length = side_length
        self.corner_radius = corner_radius
        self.faces = [] 

        super().__init__()

    def generate_points(self):
        for vect in IN, OUT, LEFT, RIGHT, UP, DOWN:
            face = RoundedRectangle(height=self.side_length, width=self.side_length,
                    corner_radius=self.corner_radius, shade_in_3d=True)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)
