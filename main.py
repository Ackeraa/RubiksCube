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

        '''
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)


class Test(ThreeDScene):
    def construct(self):
        cube = RubiksCube()

        self.move_camera(phi=60*DEGREES, theta=30*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()
        axes = ThreeDAxes()
        self.add(cube)
        self.add(axes)
        vg = VGroup(*cube[:, 2, :].flatten())
        vg1 = VGroup(*cube[:, 0, :].flatten())
        vg2 = VGroup(*cube[:, 1, :].flatten())
        self.bring_to_back(vg2)
        self.bring_to_back(vg)
        self.play(Rotating(vg, radians=PI/2, axis=UP, about_point=cube[1][2][1].get_center()))

        self.interactive_embed()


class Test2(ThreeDScene):
    def construct(self):

        cube = Cube((1,2,3))
        cube.set(fill_color=BLUE, stroke_color=BLACK, fill_opacity=1)
        cube.set_fill(BLUE, 1.0)
        cube1 = cube.copy().next_to(cube, UP, buff=0)
        self.move_camera(phi=60*DEGREES, theta=-30*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()
        axes = ThreeDAxes()
        self.add(cube)
        self.bring_to_back(cube[4])
        self.play(FadeIn(cube))
        self.interactive_embed()

class Test3(ThreeDScene):
    def construct(self):
        self.move_3d_camera(phi=60*DEGREES, theta=-30*DEGREES)
        self.begin_ambient_camera_rotation()
        face = Square(stroke_color=RED, fill_color=BLUE, fill_opacity=1, shade_in_3d=True)
        face.apply_matrix(z_to_vector(RIGHT))
        face1 = face.copy().scale(0.5).move_to(LEFT)
        self.bring_to_back(face1)
        self.add(face, face1)
        self.interactive_embed()

