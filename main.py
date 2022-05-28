from manim import *
from rubiks_cube import RubiksCube
import random

COLORS = {"U": WHITE, "R": "#B90000", "F": "#009B48",
          "D": "#FFD500", "L": "#FF5900", "B": "#0045AD"}
class Main(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=160*DEGREES)
        self.gray_colors = { face : GRAY for face in ["F", "B", "U", "D", "L", "R"] }
        self.begin()
        #self.kociemba()
        #self.step1()
        #self.step2()
        #self.step3()
        #self.step4()
        #self.step5()
        #self.step6()
        #self.step7()
        self.cfop()
        self.end()
    
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
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors)

        cube1.set_color(("U", 1, 1, 2), COLORS["D"])
        cube1.set_color(("F", 0, 1, 2), COLORS["D"])
        cube1.set_color(("B", 2, 1, 2), COLORS["D"])
        cube1.set_color(("L", 1, 2, 2), COLORS["D"])
        cube1.set_color(("R", 1, 0, 2), COLORS["D"])
        self.add(cube1)
        for turn in ["F", "R", "U", "R'", "U'", "F'"]:
            self.play(cube1.turn(turn))
        self.move_camera(phi=55*DEGREES, theta=30*DEGREES)
        for turn in ["B", "L", "U", "L'", "U'", "B'"]:
            self.play(cube1.turn(turn))
        self.move_camera(phi=55*DEGREES, theta=210*DEGREES)
        for turn in ["F", "R", "U", "R'", "U'", "F'"]:
            self.play(cube1.turn(turn))

        self.play(FadeOut(cube1))

    def step5(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        colors = {"U": COLORS["D"], "D": COLORS["U"], "L": COLORS["L"],
                  "R": COLORS["R"], "F": COLORS["B"], "B": COLORS["F"]}
        cube1 = RubiksCube(dim=3, colors=colors)
        cube1.cubies[0, 0, 2].set_fill(GRAY)
        cube1.cubies[0, 2, 2].set_fill(GRAY)
        cube1.cubies[2, 0, 2].set_fill(GRAY)
        cube1.cubies[2, 2, 2].set_fill(GRAY)
        cube2 = cube1.copy()

        cube1.set_color(("F", 0, 1, 2), colors["L"])
        cube1.set_color(("L", 1, 2, 2), colors["F"])
        self.add(cube1)
        self.move_camera(phi=55*DEGREES, theta=(360+160)*DEGREES, run_time=4)

        for turn in ["R", "U", "R'", "U", "R", "U2", "R'", "U"]:
            self.play(cube1.turn(turn))
        self.move_camera(phi=55*DEGREES, theta=(360+360+160)*DEGREES, run_time=4)
        self.play(FadeOut(cube1))

        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        cube2.set_color(("F", 0, 1, 2), colors["F"])
        cube2.set_color(("L", 1, 2, 2), colors["R"])
        cube2.set_color(("R", 0, 2, 2), colors["L"])
        cube2.set_color(("D", 2, 1, 2), colors["D"])
        self.play(FadeIn(cube2))
        
        for turn in ["U", "R", "U", "R'", "U", "R", "U2", "R'", "U"]:
            self.play(cube2.turn(turn))
        self.move_camera(phi=55*DEGREES, theta=30*DEGREES)
        for turn in ["L", "U", "L'", "U", "L", "U2", "L'", "U"]:
            self.play(cube2.turn(turn))
        self.play(FadeOut(cube2))

    def step6(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        colors = {"U": COLORS["D"], "D": COLORS["U"], "L": COLORS["L"],
                  "R": COLORS["R"], "F": COLORS["B"], "B": COLORS["F"]}
        cube1 = RubiksCube(dim=3, colors=colors)
        times = [2, 4, 2, 4]
        for i in range(4):
            for _ in range(times[i]):
                for turn in ["R'", "D'", "R", "D"]:
                    cube1.turn(turn, show=False)
            cube1.turn("U", show=False)
        for turn in ["U", "R", "U'", "L'", "U", "R'", "U'", "L"]:
            cube1.turn(turn, show=False)
        self.add(cube1)

        for i in range(2):
            for turn in ["U", "R", "U'", "L'", "U", "R'", "U'", "L"]:
                self.play(cube1.turn(turn))
            self.move_camera(phi=55*DEGREES, theta=(210+360*(i+1))*DEGREES, run_time=4)

    def step7(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        colors = {"U": COLORS["D"], "D": COLORS["U"], "L": COLORS["L"],
                  "R": COLORS["R"], "F": COLORS["B"], "B": COLORS["F"]}
        cube1 = RubiksCube(dim=3, colors=colors)
        cube1.set_color(("F", 0, 0, 2), colors["U"])
        cube1.set_color(("F", 0, 2, 2), colors["U"])
        cube1.set_color(("R", 0, 0, 2), colors["F"])
        cube1.set_color(("R", 2, 0, 2), colors["B"])
        cube1.set_color(("L", 0, 2, 2), colors["F"])
        cube1.set_color(("L", 2, 2, 2), colors["B"])
        cube1.set_color(("B", 2, 0, 2), colors["U"])
        cube1.set_color(("B", 2, 2, 2), colors["U"])
        cube1.set_color(("U", 0, 0, 2), colors["R"])
        cube1.set_color(("U", 0, 2, 2), colors["L"])
        cube1.set_color(("U", 2, 0, 2), colors["R"])
        cube1.set_color(("U", 2, 2, 2), colors["L"])
        self.add(cube1)

        times = [4, 2, 4, 2]
        for i in range(4):
            for _ in range(times[i]):
                for turn in ["R'", "D'", "R", "D"]:
                    self.play(cube1.turn(turn))
            self.wait(1)
            self.play(cube1.turn("U"))

    def cfop(self):
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        cube = RubiksCube(dim=3)
        #cube.disarray(moves=40, seed=114514)
        #self.move_camera(phi=55*DEGREES, theta=(360+210)*DEGREES, run_time=4)
        with open("in.txt", "r") as f:
            turns = list(map(lambda s: s.strip(), f.readlines()))
        change = { "L": "L", "R": "R", "U": "B", "F": "U", "D": "F", "B": "D" }
        for i in range(len(turns)):
            turns[i] = change[turns[i][0]] + turns[i][1:]

        reverse_turns = [turn[:-1] if "'" in turn else turn+"'" for turn in turns]
        reverse_turns.reverse()

        for turn in reverse_turns:
            cube.turn(turn, show=False)
        self.add(cube)

        i = 0
        for turn in turns:
            i += 1
            #self.play(cube.turn(turn))
            cube.turn(turn, show=False)
            if i == 38:
                self.move_camera(phi=-120*DEGREES, theta=240*DEGREES)
            if i == 46:
                self.move_camera(phi=-120*DEGREES, theta=60*DEGREES)
            if i == 54:
                self.move_camera(phi=-120*DEGREES, theta=150*DEGREES)
            if i == 62:
                self.move_camera(phi=-120*DEGREES, theta=60*DEGREES)
            if i == 70:
                self.move_camera(phi=-120*DEGREES, theta=150*DEGREES)
                break
        #step 5
        for turn in ["R", "D", "R'", "D", "R", "D2", "R'", "D"]:
            cube.turn(turn, show=False)

        self.move_camera(phi=-120*DEGREES, theta=-30*DEGREES)

        #step 6
        for _ in range(2):
            for turn in ["D", "L", "D'", "R'", "D", "L'", "D'", "R"]:
                cube.turn(turn, show=False)

        #step 7
        self.move_camera(phi=-120*DEGREES, theta=-30*DEGREES)
        for _ in range(2):
            for turn in ["L'", "U'", "L", "U"]:
                #self.play(cube.turn(turn))
                cube.turn(turn, show=False)

        self.play(cube.turn("D"))
        for _ in range(4):
            for turn in ["L'", "U'", "L", "U"]:
                cube.turn(turn, show=False)
                #self.play(cube.turn(turn))
        self.play(cube.turn("D'"))
        self.move_camera(phi=-120*DEGREES, theta=-120*DEGREES)

    def end(self):
        t = Text("The End.", font_size=24)
        self.play(Create(t))

class Test(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube = RubiksCube()
        self.add(axes, cube)
        self.set_camera_orientation(phi=55*DEGREES, theta=210*DEGREES)
        self.play(Rotate(cube, angle=PI/2, axis=Y_AXIS))
        for turn in ["U", "L", "D", "R", "F"]:
            self.play(cube.turn(turn))
        '''
        self.move_camera(phi=(55+0)*DEGREES, theta=(210-30)*DEGREES)
        self.move_camera(phi=(55-90)*DEGREES, theta=(210-30)*DEGREES)
        self.move_camera(phi=(55-90)*DEGREES, theta=(210-30-30)*DEGREES)
        '''
        self.wait()
