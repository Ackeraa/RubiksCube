from manim import *
from rubiks_cube import Cube
import numpy as np

class Main(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=240*DEGREES)
        cubes = VGroup()
        cubies = np.ndarray((3, 3), dtype=object)
        for i in range(3):
            vg = VGroup()
            for j in range(3):
                cube = Cube(side_length=1)
                cube.set(fill_color=BLUE)
                vg.add(cube)
                cubies[i, j] = cube
            vg.arrange(UP)
            cubes.add(vg)
        cubes.arrange(RIGHT)
        self.add(cubes)

        for i in range(3):
            cubes[0][i].get_face("F").set(fill_color=GREEN)
            cubes[i][0].get_face("R").set(fill_color=RED)
        
        self.wait()


