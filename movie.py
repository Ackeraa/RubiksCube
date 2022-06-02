from manim import *
from rubiks_cube import RubiksCube
import random

COLORS = {"U": WHITE, "R": "#B90000", "F": "#1DDF13",
          "D": "#FFD500", "L": "#F0720A", "B": "#0045AD"}

class Main(ThreeDScene):
    def construct(self):
        self.gray_colors = { face : GRAY for face in ["F", "B", "U", "D", "L", "R"] }
        self.begin()
        self.kociemba()
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        self.step6()
        self.step7()
        self.cfop()
    
    def begin(self):
        self.add_sound("bgm.mp3")
        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=240*DEGREES)
        self.cube0 = RubiksCube(dim=3)
        self.begin_ambient_camera_rotation(rate=-2)
        self.play(SpiralIn(VGroup(*self.cube0.cubies[:, :, :].flatten())), run_time=2.5)
        self.stop_ambient_camera_rotation()
        self.wait(0.6)

    def kociemba(self):
        self.begin_ambient_camera_rotation(rate=0)
        self.cube = self.cube0.copy()
        self.cube.disarray(moves=200)
        self.play(ReplacementTransform(self.cube0, self.cube))

        t = Text("kociemba 算法", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)
        self.play(t.animate.set(color=WHITE))
        self.wait(0.5)

        for rotate in self.cube.solve():
            self.play(rotate, run_time=0.4)

        anims = [FadeOut(self.cube), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(240+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=2)
        self.remove(self.cube, t)

    def step1(self):
        t = Text("C F O P 算法: I", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors).scale(0.5)

        cube1.setcolor(("U", 1, 0, 2), COLORS["U"])
        cube1.setcolor(("U", 1, 1, 2), COLORS["U"])
        cube1.setcolor(("U", 1, 2, 2), COLORS["U"])
        cube1.setcolor(("U", 2, 1, 2), COLORS["U"])
        cube1.setcolor(("U", 0, 1, 2), COLORS["F"])
        cube1.setcolor(("F", 0, 1, 1), COLORS["F"])
        cube1.setcolor(("F", 0, 1, 2), COLORS["U"])
        cube1.setcolor(("R", 1, 0, 1), COLORS["R"])
        cube1.setcolor(("R", 1, 0, 2), COLORS["R"])
        cube1.setcolor(("L", 1, 2, 1), COLORS["L"])
        cube1.setcolor(("L", 1, 2, 2), COLORS["L"])
        cube1.setcolor(("B", 2, 1, 1), COLORS["B"])
        cube1.setcolor(("B", 2, 1, 2), COLORS["B"])

        cube2 = cube1.copy()
        cube2.setcolor(("U", 0, 1, 2), GRAY)
        cube2.setcolor(("F", 0, 1, 2), GRAY)
        cube2.setcolor(("F", 0, 0, 1), COLORS["U"])
        cube2.setcolor(("R", 0, 0, 1), COLORS["F"])
        cube2.setcolor(("L", 1, 2, 1), COLORS["L"])
        cube2.setcolor(("L", 1, 2, 2), GRAY)

        cube3 = cube1.copy()
        cube3.setcolor(("U", 0, 1, 2), GRAY)
        cube3.setcolor(("F", 0, 1, 0), COLORS["U"])
        cube3.setcolor(("F", 0, 1, 2), GRAY)
        cube3.setcolor(("D", 0, 1, 0), COLORS["F"])

        vg = VGroup(cube3, cube1, cube2).arrange(UP+0.5*LEFT, buff=3)
        self.play(FadeIn(vg), t.animate.set(color=WHITE))
        self.play(cube1.animate.scale(2).move_to(ORIGIN))

        # case 1
        self.wait(1)
        for turn in ["F", "U'", "R", "U"]:
            self.play(cube1.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube1.animate.scale(0.5).move_to(cube2),
                  cube2.animate.scale(2).move_to(ORIGIN))

        # case 2
        self.wait(1)
        for turn in ["U'", "R", "U"]:
            self.play(cube2.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube2.animate.scale(0.5).move_to(cube3),
                  cube3.animate.scale(2).move_to(ORIGIN))

        # case 3
        self.wait(1)
        for turn in ["F'", "U'", "R", "U"]:
            self.play(cube3.turn(turn), run_time=0.6)
        self.wait(0.5)
        
        anims = [FadeOut(vg), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(240+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(vg)

    def step2(self):
        t = Text("C F O P 算法: II", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors)

        # case 1
        for i in range(3):
            for j in range(3):
                cube1.setcolor(("U", i, j, 2), COLORS["U"])
        cube1.setcolor(("U", 0, 0, 2), GRAY)

        cube1.setcolor(("F", 0, 1, 1), COLORS["F"])
        cube1.setcolor(("F", 0, 1, 2), COLORS["F"])
        cube1.setcolor(("F", 0, 2, 2), COLORS["F"])
        cube1.setcolor(("F", 0, 0, 0), COLORS["F"])
        cube1.setcolor(("R", 1, 0, 1), COLORS["R"])
        cube1.setcolor(("R", 1, 0, 2), COLORS["R"])
        cube1.setcolor(("R", 2, 0, 2), COLORS["R"])
        cube1.setcolor(("R", 0, 0, 0), COLORS["U"])
        cube1.setcolor(("D", 0, 0, 0), COLORS["R"])

        cube2 = cube1.copy().scale(0.4)
        cube2.setcolor(("F", 0, 0, 0), COLORS["U"])
        cube2.setcolor(("R", 0, 0, 0), COLORS["R"])
        cube2.setcolor(("D", 0, 0, 0), COLORS["F"])

        cube3 = cube1.copy().scale(0.5)
        cube3.setcolor(("F", 0, 0, 0), COLORS["R"])
        cube3.setcolor(("R", 0, 0, 0), COLORS["F"])
        cube3.setcolor(("D", 0, 0, 0), COLORS["U"])

        cube4 = cube1.copy().scale(0.5)
        cube4.setcolor(("F", 0, 0, 0), GRAY)
        cube4.setcolor(("R", 0, 0, 0), GRAY)
        cube4.setcolor(("D", 0, 0, 0), GRAY)
        cube4.setcolor(("F", 0, 2, 2), COLORS["R"])
        cube4.setcolor(("L", 0, 2, 2), COLORS["F"])

        cube1.scale(0.4)
        vg0 = VGroup(cube2, cube1).arrange(UP+0.5*LEFT, buff=5)
        vg1 = VGroup(cube4, cube3).arrange(UP+0.5*LEFT, buff=5)
        vg = VGroup(vg0, vg1).arrange(IN, buff=4)
        c1 = cube1.get_center()
        c2 = cube2.get_center()
        c3 = cube3.get_center()
        c4 = cube4.get_center()

        self.play(FadeIn(vg), t.animate.set(color=WHITE))

        self.play(cube1.animate.scale(2.5).move_to(ORIGIN))
        # case 1
        for turn in ["R'", "D'", "R"]:
            self.play(cube1.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube1.animate.scale(0.4).move_to(c1),
                  cube2.animate.scale(2.5).move_to(ORIGIN))

        # case 2
        for turn in ["F", "D", "F'"]:
            self.play(cube2.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube2.animate.scale(0.4).move_to(c2),
                  cube3.animate.scale(2).move_to(ORIGIN))

        # case 3
        for turn in ["R'", "D2'", "R", "D", "R'", "D'", "R"]:
            self.play(cube3.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube3.animate.scale(0.5).move_to(c3),
                  cube4.animate.scale(2).move_to(ORIGIN))

        # case 4
        for turn in ["L", "D", "L'", "R'", "D'", "R"]:
            self.play(cube4.turn(turn), run_time=0.6)
        self.wait(0.5)

        self.play(cube4.animate.scale(0.5).move_to(c4))

        anims = [FadeOut(vg), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(240+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(vg)

    def step3(self):
        t = Text("C F O P 算法: III", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
        cube1 = RubiksCube(dim=3, colors=self.gray_colors).scale(0.5)

        # case 1
        for i in range(3):
            for j in range(3):
                cube1.setcolor(("D", i, j, 0), COLORS["U"])

        for i in range(3):
            cube1.setcolor(("F", 0, i, 0), COLORS["B"])
            cube1.setcolor(("B", 2, i, 0), COLORS["F"])
            cube1.setcolor(("R", i, 0, 0), COLORS["L"])
            cube1.setcolor(("L", i, 2, 0), COLORS["R"])
        cube1.setcolor(("U", 1, 1, 2), COLORS["D"])
        cube1.setcolor(("F", 0, 1, 1), COLORS["B"])
        cube1.setcolor(("B", 2, 1, 1), COLORS["F"])
        cube1.setcolor(("L", 1, 2, 1), COLORS["R"])
        cube1.setcolor(("R", 1, 0, 1), COLORS["L"])
        cube1.setcolor(("F", 0, 1, 2), COLORS["B"])
        cube1.setcolor(("U", 0, 1, 2), COLORS["L"])

        cube2 = cube1.copy()
        cube2.setcolor(("F", 0, 1, 2), COLORS["B"])
        cube2.setcolor(("U", 0, 1, 2), COLORS["R"])

        vg = VGroup(cube2, cube1).arrange(LEFT*0.5+UP, buff=5)
        c1 = cube1.get_center()
        c2 = cube2.get_center()

        self.play(FadeIn(vg), t.animate.set(color=WHITE))

        self.play(cube1.animate.scale(2).move_to(ORIGIN))
        self.wait(0.5)

        d1 = Dot().move_to(cube1.cubies[0, 1, 2].get_face("F"))
        d2 = Dot(color=BLACK).move_to(cube1.cubies[0, 0, 1].get_face("F"))
        p1 = d1.get_center()
        p2 = d2.get_center()
        self.play(FadeIn(d1, d2))
        self.wait(0.5)
        self.play(d1.animate.move_to(p2), d2.animate.move_to(p1))
        self.play(FadeOut(d1, d2))

        turns = ["U", "R", "U'", "R'", "U'", "F'", "U", "F"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        ts.shift(UP*3.5)
        self.add_fixed_in_frame_mobjects(ts)
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube1.turn(turns[i]), run_time=0.6)

        self.play(cube1.animate.scale(0.5).move_to(c1),
                  cube2.animate.scale(2).move_to(ORIGIN),
                  FadeOut(ts))
        self.wait(0.5)

        # case 2
        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES)
        self.move_camera(phi=55*DEGREES, theta=160*DEGREES, rate_func=rate_functions.smooth)
        self.wait(0.5)

        d1 = Dot().move_to(cube2.cubies[0, 1, 2].get_face("F"))
        d2 = Dot(color=BLACK).move_to(cube2.cubies[0, 2, 1].get_face("F"))
        p1 = d1.get_center()
        p2 = d2.get_center()
        self.play(FadeIn(d1, d2))
        self.wait(0.5)
        self.play(d1.animate.move_to(p2), d2.animate.move_to(p1))
        self.play(FadeOut(d1, d2))

        turns = ["U'", "L'", "U", "L", "U", "F", "U'", "F'"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(ts)
        ts.shift(UP*3.5)
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube2.turn(turns[i]), run_time=0.6)
        self.wait(0.5)

        anims = [FadeOut(vg), FadeOut(ts), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(240+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(vg, ts)

    def step4(self):
        t = Text("C F O P 算法: IV", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)
        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)

        cube1 = RubiksCube(dim=3, colors=self.gray_colors)
        cube1.setcolor(("U", 1, 1, 2), COLORS["D"])
        cube1.setcolor(("F", 0, 1, 2), COLORS["D"])
        cube1.setcolor(("B", 2, 1, 2), COLORS["D"])
        cube1.setcolor(("L", 1, 2, 2), COLORS["D"])
        cube1.setcolor(("R", 1, 0, 2), COLORS["D"])
        self.play(FadeIn(cube1), t.animate.set(color=WHITE))

        css = VGroup()
        cs = VGroup()
        for _ in range(5):
            c = RoundedRectangle(height=1, width=1, stroke_color=BLACK, stroke_width=4,
                shade_in_3d=False, corner_radius=0.1, fill_color=GRAY, fill_opacity=1)
            c.scale(0.5)
            cs.add(c)

        cs[1].shift(RIGHT)
        cs[0].next_to(cs[1], UP, buff=0)
        cs[2].next_to(cs[1], DOWN, buff=0)
        cs[3].next_to(cs[1], LEFT, buff=0)
        cs[4].next_to(cs[1], RIGHT, buff=0)

        css = VGroup(*[cs.copy() for _ in range(4)]).arrange(DOWN, buff=0.5)
        css.shift(RIGHT*5)
        css[0][1].set_fill(COLORS["D"])

        css[1][1].set_fill(COLORS["D"])
        css[1][2].set_fill(COLORS["D"])
        css[1][4].set_fill(COLORS["D"])

        css[2][1].set_fill(COLORS["D"])
        css[2][3].set_fill(COLORS["D"])
        css[2][4].set_fill(COLORS["D"])

        css[3].set_fill(COLORS["D"])

        self.add_fixed_in_frame_mobjects(css)

        turns = ["F", "R", "U", "R'", "U'", "F'"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(ts)
        ts.shift(UP*3.5)
        self.play(Indicate(css[0], color=TEAL))
        css.set_z_index(-1)
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube1.turn(turns[i]), run_time=0.6)

        self.play(Indicate(css[1], color=TEAL))
        css.set_z_index(-1)
        self.wait(0.5)

        self.move_camera(phi=55*DEGREES, theta=30*DEGREES)
        turns = ["B", "L", "U", "L'", "U'", "B'"]
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube1.turn(turns[i]), run_time=0.6)

        self.play(Indicate(css[2], color=TEAL))
        css.set_z_index(-1)
        self.wait(0.5)

        turns = ["B", "L", "U", "L'", "U'", "B'"]
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube1.turn(turns[i]), run_time=0.6)

        self.play(Indicate(css[3], color=TEAL))
        css.set_z_index(-1)
        self.wait(0.5)

        anims = [FadeOut(cube1), FadeOut(css), FadeOut(ts), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(240+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(cube1, ts, css)

    def step5(self):
        t = Text("C F O P 算法: V", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=160*DEGREES, zoom=1)
        colors = {"U": COLORS["D"], "D": COLORS["U"], "L": COLORS["L"],
                  "R": COLORS["R"], "F": COLORS["B"], "B": COLORS["F"]}
        cube1 = RubiksCube(dim=3, colors=colors)
        cube1.cubies[0, 0, 2].set_fill(GRAY)
        cube1.cubies[0, 2, 2].set_fill(GRAY)
        cube1.cubies[2, 0, 2].set_fill(GRAY)
        cube1.cubies[2, 2, 2].set_fill(GRAY)

        cube1.setcolor(("F", 0, 1, 2), colors["L"])
        cube1.setcolor(("L", 1, 2, 2), colors["F"])
        self.play(FadeIn(cube1), t.animate.set(color=WHITE))

        d1 = Dot(color=RED).move_to(cube1.cubies[0, 1, 2].get_face("U"))
        d2 = Dot(color=BLACK).move_to(cube1.cubies[1, 2, 2].get_face("U"))
        p1 = d1.get_center()
        p2 = d2.get_center()
        self.play(FadeIn(d1, d2))
        self.wait(0.5)
        self.play(d1.animate.move_to(p2), d2.animate.move_to(p1))
        self.play(FadeOut(d1, d2))

        self.move_camera(phi=55*DEGREES, theta=(360+200)*DEGREES, run_time=4, rate_func=rate_functions.smooth)

        turns = ["R", "U", "R'", "U", "R", "U2", "R'", "U"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(ts)
        ts.shift(UP*3.5)
        for i in range(len(turns)):
            self.play(Indicate(ts[i], color=TEAL), cube1.turn(turns[i]), run_time=0.6)
        anims = [FadeOut(cube1), FadeOut(ts), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(200+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(cube1, ts)

    def step6(self):
        t = Text("C F O P 算法: VI", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
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
        self.play(FadeIn(cube1), t.animate.set(color=WHITE))

        turns = ["U", "R", "U'", "L'", "U", "R'", "U'", "L"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(ts)
        ts.shift(UP*3.5)
        for i in range(2):
            d1 = Dot(color=RED).move_to(cube1.cubies[0, 2, 2].get_face("U"))
            d2 = Dot(color=BLACK).move_to(cube1.cubies[2, 2, 2].get_face("U"))
            d3 = Dot(color=GREEN).move_to(cube1.cubies[2, 0, 2].get_face("U"))
            p1 = d1.get_center()
            p2 = d2.get_center()
            p3 = d3.get_center()
            self.play(FadeIn(d1, d2, d3))
            self.wait(0.5)
            self.play(d1.animate.move_to(p2), d2.animate.move_to(p3), d3.animate.move_to(p1))
            self.play(FadeOut(d1, d2, d3))
            for j in range(len(turns)):
                self.play(Indicate(ts[j], color=TEAL), cube1.turn(turns[j]), run_time=0.6)
            self.move_camera(phi=55*DEGREES, theta=(210+360*(i+1))*DEGREES, run_time=4, rate_func=rate_functions.smooth)

        anims = [FadeOut(cube1), FadeOut(ts), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(200+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(cube1, ts)

    def step7(self):
        t = Text("C F O P 算法: VII", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
        colors = {"U": COLORS["D"], "D": COLORS["U"], "L": COLORS["L"],
                  "R": COLORS["R"], "F": COLORS["B"], "B": COLORS["F"]}
        cube1 = RubiksCube(dim=3, colors=colors)
        cube1.setcolor(("F", 0, 0, 2), colors["U"])
        cube1.setcolor(("F", 0, 2, 2), colors["U"])
        cube1.setcolor(("R", 0, 0, 2), colors["F"])
        cube1.setcolor(("R", 2, 0, 2), colors["B"])
        cube1.setcolor(("L", 0, 2, 2), colors["F"])
        cube1.setcolor(("L", 2, 2, 2), colors["B"])
        cube1.setcolor(("B", 2, 0, 2), colors["U"])
        cube1.setcolor(("B", 2, 2, 2), colors["U"])
        cube1.setcolor(("U", 0, 0, 2), colors["R"])
        cube1.setcolor(("U", 0, 2, 2), colors["L"])
        cube1.setcolor(("U", 2, 0, 2), colors["R"])
        cube1.setcolor(("U", 2, 2, 2), colors["L"])
        self.play(FadeIn(cube1), t.animate.set(color=WHITE))

        turns = ["R'", "D'", "R", "D"]
        ts = VGroup(*[Text(turn, font_size=20, color=RED_E) for turn in turns]).arrange(RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(ts)
        ts.shift(UP*3.5)

        times = [4, 2, 4, 2]
        for i in range(4):
            for k in range(times[i]):
                if k % 2 == 0:
                    d1 = Dot(color=MAROON).move_to(cube1.cubies[0, 0, 2].get_face("U"))
                    d2 = Dot(color=BLACK).move_to(cube1.cubies[0, 0, 2].get_face("F"))
                    d3 = Dot(color=DARK_BROWN).move_to(cube1.cubies[0, 0, 2].get_face("R"))
                    p1 = d1.get_center()
                    p2 = d2.get_center()
                    p3 = d3.get_center()
                    self.play(FadeIn(d1, d2, d3))
                    self.play(d1.animate.move_to(p2), d2.animate.move_to(p3), d3.animate.move_to(p1))
                    self.play(FadeOut(d1, d2, d3))
                for j in range(len(turns)):
                    self.play(Indicate(ts[j], color=TEAL), cube1.turn(turns[j]), run_time=0.6)
            self.wait(1)
            self.play(cube1.turn("U"))

        anims = [FadeOut(cube1), FadeOut(ts), FadeOut(t)]
        self.move_camera(phi=55*DEGREES, theta=(210+180)*DEGREES, zoom=0.2, added_anims=anims, run_time=3)
        self.remove(cube1, ts)

    def cfop(self):
        t = Text("C F O P 算法", font_size=22, color=BLACK)
        t.to_corner(UL, buff=0).shift(RIGHT*0.5+DOWN*0.4)
        self.add_fixed_in_frame_mobjects(t)

        self.set_camera_orientation(should_apply_shading=False, phi=55*DEGREES, theta=210*DEGREES, zoom=1)
        cube = RubiksCube(dim=3)
        with open("in.txt", "r") as f:
            turns = list(map(lambda s: s.strip(), f.readlines()))
        change = { "L": "L", "R": "R", "U": "B", "F": "U", "D": "F", "B": "D" }
        for i in range(len(turns)):
            turns[i] = change[turns[i][0]] + turns[i][1:]

        reverse_turns = [turn[:-1] if "'" in turn else turn+"'" for turn in turns]
        reverse_turns.reverse()

        for turn in reverse_turns:
            cube.turn(turn, show=False)
        self.play(FadeIn(cube), t.animate.set(color=WHITE))
        self.wait(0.5)

        i = 0
        for turn in turns:
            i += 1
            self.play(cube.turn(turn), run_time=0.5)
            if i == 38:
                self.move_camera(phi=-120*DEGREES, theta=210*DEGREES)
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
            self.play(cube.turn(turn), run_time=0.5)

        self.move_camera(phi=-120*DEGREES, theta=-30*DEGREES)

        #step 6
        for _ in range(2):
            for turn in ["D", "L", "D'", "R'", "D", "L'", "D'", "R"]:
                self.play(cube.turn(turn), run_time=0.5)

        #step 7
        self.move_camera(phi=-120*DEGREES, theta=-30*DEGREES)
        for _ in range(2):
            for turn in ["L'", "U'", "L", "U"]:
                self.play(cube.turn(turn), run_time=0.5)

        self.play(cube.turn("D"))
        for _ in range(4):
            for turn in ["L'", "U'", "L", "U"]:
                self.play(cube.turn(turn), run_time=0.5)
        self.play(cube.turn("D'"), run_time=0.5)


        self.move_camera(phi=-120*DEGREES, theta=(-30+180)*DEGREES, run_time=4)

