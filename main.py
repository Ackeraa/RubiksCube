from manim import *
from rubiks_cube import RubiksCube
from cube import Cube

class Main(ThreeDScene):
    def construct(self):
        cube = RubiksCube().scale(0.6).shift(DOWN*2.6 + LEFT*2)

        self.move_camera(phi=60*DEGREES, theta=160*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

        for plain in cube:
            for row in plain:
                for c in row:
                    c.set(stroke_color=BLACK)

        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube.set_state(state)
        self.play(FadeIn(cube))
        self.wait()
        self.play(CubeMove(cube, "R"), run_time=1.5)

        '''
        for m in cube.solve_by_kociemba(state):
            self.play(CubeMove(cube, m), run_time=1)

        self.play(Rotating(cube, radians=2*PI, run_time=2))

        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        '''

class Test(ThreeDScene):
    def construct(self):
        cube = Cube((1, 2, 3))
        cube = RubiksCube()

        self.move_camera(phi=60*DEGREES, theta=160*DEGREES)
        #self.renderer.camera.frame_center = cube.get_center()
        self.add(cube)
        self.wait()


