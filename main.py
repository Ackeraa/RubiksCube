from manim import *
from rubiks_cube import Cube, RubiksCube


class Main(ThreeDScene):
    def construct(self):
        axes =ThreeDAxes()
        #self.add(axes)
        rubiks_cube = RubiksCube(dim=3)
        self.set_camera_orientation(phi=60*DEGREES, theta=160*DEGREES)

        self.add(rubiks_cube)
        for rotation in rubiks_cube.disarray(show=True, moves=2):
            self.play(rotation)
        
        #self.play(rubiks_cube.rotate("R"), run_time=0.3)
        vg = VGroup(*rubiks_cube.cubies.flatten())
        #self.play(SpiralIn(vg), run_time=2)

        '''
        self.play(rubiks_cube.rotate("R"), run_time=0.3)
        self.play(rubiks_cube.rotate("U"), run_time=0.3)
        self.play(rubiks_cube.rotate("F"), run_time=0.3)
        self.play(rubiks_cube.rotate("L"), run_time=0.3)
        self.play(rubiks_cube.rotate("D"), run_time=0.3)
        self.play(rubiks_cube.rotate("B"), run_time=0.3)

        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state(state)
        self.play(FadeIn(cube))
        self.wait()
        #self.play(CubeMove(cube, "R"), run_time=1.5)

        for m in cube.solve_by_kociemba(state):
            self.play(CubeMove(cube, m), run_time=1)

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        '''

class Test(ThreeDScene):
    def construct(self):
        c = Circle()
        self.play(FadeIn(c), Animation(c))
