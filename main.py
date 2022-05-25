from manim import *
from rubiks_cube import RubiksCube

class Main(ThreeDScene):
    def construct(self):
        rubiks_cube = RubiksCube(dim=3)
        self.add(rubiks_cube)

        self.move_camera(phi=60*DEGREES, theta=160*DEGREES)

        '''
        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state(state)
        self.play(FadeIn(cube))
        self.wait()
        #self.play(CubeMove(cube, "R"), run_time=1.5)

        for m in cube.solve_by_kociemba(state):
            self.play(CubeMove(cube, m), run_time=1)

        '''
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
