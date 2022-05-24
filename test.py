from manimlib import *

class Main(Scene):
    def construct(self):
        face = Square(stroke_color=RED, fill_color=BLUE, fill_opacity=1)
        self.add(face)
        self.wait()
