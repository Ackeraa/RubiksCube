from manim import *
from rubiks_cube import RubiksCube


class Main(ThreeDScene):
    def construct(self):
        axes =ThreeDAxes()
        #self.add(axes)
        rubiks_cube = RubiksCube(dim=3)
        self.set_camera_orientation(phi=60*DEGREES, theta=160*DEGREES)

        
        rubiks_cube0 = rubiks_cube.copy()
        rubiks_cube.disarray()
        self.add(rubiks_cube0)
        self.play(ReplacementTransform(rubiks_cube0, rubiks_cube))
        for rotate in rubiks_cube.solve():
            self.play(rotate, run_time=0.4)

        '''
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        '''

class Test(ThreeDScene):
    def construct(self):
        print(str(RED))
