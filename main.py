from manim import *
from rubiks_cube import RubiksCube
from cube import Cube
from face_rotate import FaceRotate

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
        #self.play(CubeMove(cube, "R"), run_time=1.5)

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

        self.move_camera(phi=60*DEGREES, theta=205*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()
        axes = ThreeDAxes()
        self.add(cube)
        self.add(axes)
        '''
        vg2 = VGroup(*cube[:, 2, :].flatten())
        vg1 = VGroup(*cube[:, 0, :].flatten())
        vg = VGroup(*cube[:, 1, :].flatten())
        self.bring_to_back(vg2)
        self.bring_to_back(vg)
        face = Square(1, fill_color=RED, fill_opacity=1)
        face.flip()
        face.shift(1 * OUT / 2.0)
        face.apply_matrix(z_to_vector(RIGHT))
        face.shift(RIGHT + IN)
        self.play(FaceRotate(cube, "L"))
        self.play(FaceRotate(cube, "F"))
        '''
        self.play(cube.rotate("L"))
        self.play(cube.rotate("R"))
        self.play(cube.rotate("F"))
        self.play(cube.rotate("B"))
        self.play(cube.rotate("D"))
        self.play(cube.rotate("U"))

        # [-1.  0.  0.] [ 0.  0. -1.] [0. 1. 0.]
        # RIGHT, UP, OUT ---> X, Y, Z
        #cube[2, 1, 0][3].set(shade_in_3d=False)
        #self.play(Rotating(vg, radians=PI/2, axis=UP, about_point=cube[1][1][1].get_center()), run_time=0.5)
        self.wait()

class Test2(ThreeDScene):
    def construct(self):

        cube = Cube((1,2,3))
        cube1 = cube.copy().next_to(cube, UP, buff=0)
        self.move_camera(phi=60*DEGREES, theta=-30*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()
        self.begin_ambient_camera_rotation()
        axes = ThreeDAxes()
        self.add(cube)
        self.play(FadeIn(cube))
        self.interactive_embed()

class Test3(Scene):
    def construct(self):

        from manim.mobject.opengl.opengl_geometry import  OpenGLSquare

        '''
        self.move_camera(phi=60*DEGREES, theta=-30*DEGREES)
        self.begin_ambient_camera_rotation()
        '''
        face = OpenGLSquare(fill_color=BLUE, fill_opacity=1)
        face.apply_matrix(z_to_vector(RIGHT))
        face.apply_depth_test()
        face1 = face.copy().scale(0.5).move_to(LEFT)
        face1.set_fill(GREEN, opacity=1)
        face1.apply_depth_test()
        self.add(face, face1)
        self.interactive_embed()

class Test4(ThreeDScene):
    def construct(self):
        from manim.mobject.opengl.opengl_surface import  OpenGLSurface
        s = OpenGLSurface(depth_test=True)
        s.set(stroke_color=GREEN)
        s.apply_matrix(z_to_vector(RIGHT))
        s1 = OpenGLSurface(color=RED, depth_test=True).shift(IN).scale(0.5)
        s1.apply_matrix(z_to_vector(RIGHT))
        vg = OpenGLMobject()
        vg.add(s1, s)
        self.add(vg)
        self.interactive_embed()
