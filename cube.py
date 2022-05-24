from manim import *

class Cube(VGroup):

    def __init__(self, pos, side_length=2, corner_radius=0.2):
        self.pos = pos
        self.side_length = side_length
        self.corner_radius = corner_radius
        self.faces = [] 

        super().__init__(fill_color=BLUE, fill_opacity=1, stroke_color=BLACK, stroke_width=4)

    def generate_points(self):
        for vect in UP, DOWN, OUT, RIGHT, IN, LEFT:
            face = RoundedRectangle(height=self.side_length, width=self.side_length, stroke_color=BLACK, stroke_width=4,
                    corner_radius=self.corner_radius, shade_in_3d=True, fill_color=BLUE, fill_opacity=1)
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))
            self.add(face)

