from manim import *

class FaceRotate(Animation):
    def __init__(self, mobject, action, **kwargs):
        self.action = action
        self.face = mobject.get_face(action[0])
        self.angle = PI / 2 if action[0] in ["R", "F", "D"] else PI / 2
        self.angle = self.angle * 2 if "2" in action else self.angle 
        self.angle = -self.angle if "'" in action else self.angle
        self.axis = self.get_axis(action[0])

        super().__init__(mobject, **kwargs)

    def create_starting_mobject(self):
        starting_mobject = self.mobject.copy()
        return starting_mobject

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.face.rotate(alpha * self.angle, self.axis)


    def finish(self):
        super().finish()
        self.mobject.set_indices(self.action)

    def get_axis(self, which):
        if which == "F" or which == "B":
            return X_AXIS
        elif which == "U" or which == "D":
            return Z_AXIS
        else:
            return Y_AXIS
