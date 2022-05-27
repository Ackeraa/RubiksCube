from manimlib import *

class GlitchTest(Scene):

    def split_text(self, text, dy=0.3):
        text_width = text.get_width()
        for_split_recs = VGroup(*[Rectangle(height=dy+random.uniform(-0.05,0.05), width=text_width+0.1) for i in range(int(text.get_height()//dy+1))]).arrange(DOWN,buff=0).move_to(text)
        return VGroup(*[
            VGroup(*[Intersection(i,text).set_fill(color,1) for color in ["#FFFF00","#00FFFF","#FF00FF","#FF0000","#00FF00","#0000FF","#FFFFFF"]]) for i in for_split_recs 
        ])
    
    def construct(self):

        text1 = Text("fucj")
        text2 = Text("abcde")
        rec = Rectangle()
        text3 = Intersection(text1, text2)
        self.add(text3)
        '''
        text = Text("This is a glitchy animation.",font="Consolas",size=200)
        split = self.split_text(text).set_stroke(width=0).set_opacity(0.5)
        for i in split:
            i[-1].set_opacity(1)
        self.add(split)
        self.wait()
        split.save_state()
        def updater(split):
            m = 0
            if random.random() < 0.6:
                m = np.array([random.uniform(-.05,.05),random.uniform(-.05,.05),0])
            if random.random() < 0.6:
                split.restore()
                for i in split:
                    x = random.uniform(-.4,.4)*RIGHT + m
                    for j in i:
                        j.shift(np.array([random.uniform(-.05,.05),random.uniform(-.05,.05),0])+x)
            
        self.play(UpdateFromFunc(split,updater),run_time=0.5)
        split.restore()
        self.wait()
        '''
