from manim import *
from rubiks_cube import RubiksCube
import random

COLORS = {"U": WHITE, "R": "#B90000", "F": "#009B48",
          "D": "#FFD500", "L": "#FF5900", "B": "#0045AD"}
class Main(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=160*DEGREES)
        self.gray_colors = { face : GRAY for face in ["F", "B", "U", "D", "L", "R"] }
        #self.begin()
        #self.kociemba()
        #self.step1()
        #self.step2()
        self.step3()
    
    def begin(self):
        self.cube0 = RubiksCube(dim=3)
        self.begin_ambient_camera_rotation(rate=-2)
        self.play(SpiralIn(VGroup(*self.cube0.cubies[:, :, :].flatten())), run_time=2)
        self.stop_ambient_camera_rotation()
        self.wait()

    def kociemba(self):
        self.cube = self.cube0.copy()
        self.cube.disarray()
        self.play(ReplacementTransform(self.cube0, self.cube))
        self.wait()
        for rotate in self.cube.solve():
            self.play(rotate, run_time=0.4)

    def step1(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        axes = ThreeDAxes()
        self.add(axes)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors)

        # case 1
        cube1.set_color(("U", 1, 0, 2), COLORS["U"])
        cube1.set_color(("U", 1, 1, 2), COLORS["U"])
        cube1.set_color(("U", 1, 2, 2), COLORS["U"])
        cube1.set_color(("U", 2, 1, 2), COLORS["U"])
        cube1.set_color(("U", 0, 1, 2), COLORS["F"])

        cube1.set_color(("F", 0, 1, 1), COLORS["F"])
        cube1.set_color(("F", 0, 1, 2), COLORS["U"])
        cube1.set_color(("R", 1, 0, 1), COLORS["R"])
        cube1.set_color(("R", 1, 0, 2), COLORS["R"])
        cube1.set_color(("L", 1, 2, 1), COLORS["L"])
        cube1.set_color(("L", 1, 2, 2), COLORS["L"])
        cube1.set_color(("B", 2, 1, 1), COLORS["B"])
        cube1.set_color(("B", 2, 1, 2), COLORS["B"])
        self.add(cube1)
        cube2 = cube1.copy()
        cube3 = cube1.copy()

        for turn in ["F", "U'", "R", "U"]:
            self.play(cube1.turn(turn))
        self.play(FadeOut(cube1))
        self.wait()

        # case 2
        cube2.set_color(("U", 0, 1, 2), GRAY)
        cube2.set_color(("F", 0, 1, 2), GRAY)
        cube2.set_color(("F", 0, 0, 1), COLORS["U"])
        cube2.set_color(("R", 0, 0, 1), COLORS["F"])
        cube2.set_color(("L", 1, 2, 1), COLORS["L"])
        cube2.set_color(("L", 1, 2, 2), GRAY)

        self.play(FadeIn(cube2))

        for turn in ["U'", "R", "U"]:
            self.play(cube2.turn(turn))
        self.play(FadeOut(cube2))
        self.wait()

        # case 3
        cube3.set_color(("U", 0, 1, 2), GRAY)
        cube3.set_color(("F", 0, 1, 0), COLORS["U"])
        cube3.set_color(("F", 0, 1, 2), GRAY)
        cube3.set_color(("D", 0, 1, 0), COLORS["F"])

        self.play(FadeIn(cube3))

        for turn in ["F'", "U'", "R", "U"]:
            self.play(cube3.turn(turn))
        self.play(FadeOut(cube3))
        self.wait()

    def step2(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        axes = ThreeDAxes()
        self.add(axes)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors)

        # case 1
        for i in range(3):
            for j in range(3):
                cube1.set_color(("U", i, j, 2), COLORS["U"])
        cube1.set_color(("U", 0, 0, 2), GRAY)

        cube1.set_color(("F", 0, 1, 1), COLORS["F"])
        cube1.set_color(("F", 0, 1, 2), COLORS["F"])
        cube1.set_color(("F", 0, 2, 2), COLORS["F"])
        cube1.set_color(("F", 0, 0, 0), COLORS["F"])
        cube1.set_color(("R", 1, 0, 1), COLORS["R"])
        cube1.set_color(("R", 1, 0, 2), COLORS["R"])
        cube1.set_color(("R", 2, 0, 2), COLORS["R"])
        cube1.set_color(("R", 0, 0, 0), COLORS["U"])
        cube1.set_color(("D", 0, 0, 0), COLORS["R"])
        self.add(cube1)
        cube2 = cube1.copy()
        cube3 = cube1.copy()
        cube4 = cube1.copy()

        for turn in ["R'", "D'", "R"]:
            self.play(cube1.turn(turn))
        self.play(FadeOut(cube1))
        self.wait()

        # case 2
        cube2.set_color(("F", 0, 0, 0), COLORS["U"])
        cube2.set_color(("R", 0, 0, 0), COLORS["R"])
        cube2.set_color(("D", 0, 0, 0), COLORS["F"])
        self.play(FadeIn(cube2))
        for turn in ["F", "D", "F'"]:
            self.play(cube2.turn(turn))
        self.play(FadeOut(cube2))
        self.wait()

        # case 3
        cube3.set_color(("F", 0, 0, 0), COLORS["R"])
        cube3.set_color(("R", 0, 0, 0), COLORS["F"])
        cube3.set_color(("D", 0, 0, 0), COLORS["U"])
        self.play(FadeIn(cube3))
        for turn in ["R'", "D2'", "R", "D", "R'", "D'", "R"]:
            self.play(cube3.turn(turn))
        self.play(FadeOut(cube3))
        self.wait()

        # case 4
        cube4.set_color(("F", 0, 0, 0), GRAY)
        cube4.set_color(("R", 0, 0, 0), GRAY)
        cube4.set_color(("D", 0, 0, 0), GRAY)
        cube4.set_color(("F", 0, 2, 2), COLORS["R"])
        cube4.set_color(("L", 0, 2, 2), COLORS["F"])
        self.play(FadeIn(cube4))
        for turn in ["L", "D", "L'", "R'", "D'", "R"]:
            self.play(cube4.turn(turn))
        self.play(FadeOut(cube4))
        self.wait()

    def step3(self):
        self.set_camera_orientation(phi=-120*DEGREES, theta=240*DEGREES)
        axes = ThreeDAxes()
        self.add(axes)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors)

        # case 1
        for i in range(3):
            for j in range(3):
                cube1.set_color(("D", i, j, 0), COLORS["U"])

        for i in range(3):
            cube1.set_color(("F", 0, i, 0), COLORS["B"])
            cube1.set_color(("B", 2, i, 0), COLORS["F"])
            cube1.set_color(("R", i, 0, 0), COLORS["L"])
            cube1.set_color(("L", i, 2, 0), COLORS["R"])
        cube1.set_color(("U", 1, 1, 2), COLORS["D"])
        cube1.set_color(("F", 0, 1, 1), COLORS["B"])
        cube1.set_color(("B", 2, 1, 1), COLORS["F"])
        cube1.set_color(("L", 1, 2, 1), COLORS["R"])
        cube1.set_color(("R", 1, 0, 1), COLORS["L"])
        cube1.set_color(("F", 0, 1, 2), COLORS["B"])
        cube1.set_color(("U", 0, 1, 2), COLORS["L"])

        self.add(cube1)
        cube2 = cube1.copy()

        self.move_camera(phi=55*DEGREES, theta=210*DEGREES)
        self.wait()
        for turn in ["U", "R", "U'", "R'", "U'", "F'", "U", "F"]:
            self.play(cube1.turn(turn))
        self.play(FadeOut(cube1))
        self.wait()

        # case 2
        cube2.set_color(("F", 0, 1, 2), COLORS["B"])
        cube2.set_color(("U", 0, 1, 2), COLORS["R"])
        self.play(FadeIn(cube2))
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        self.move_camera(phi=55*DEGREES, theta=160*DEGREES)
        self.wait()
        for turn in ["U'", "L'", "U", "L", "U", "F", "U'", "F'"]:
            self.play(cube2.turn(turn))
        self.play(FadeOut(cube2))
        self.wait()

    def step4(self):
        pass 

    def step5(self):
        pass

