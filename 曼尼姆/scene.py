from manim import *
import numpy as np

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
        
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=5)

        self.play(Create(circle), Create(square))
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(
            ReplacementTransform(square, circle)
        )
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )
class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square()
        triangle = Triangle()

        self.play(Create(circle))
        self.play(circle.animate.shift(LEFT * 5))
        self.play(circle.animate.shift(UP*2, RIGHT*3))
        self.play(circle.animate.move_to(LEFT*3))
        self.play(FadeOut(circle))
        self.play(FadeIn(circle))
        self.play(circle.animate.scale(2))
        self.play(FadeOut(circle))
        self.play(Create(square))
        self.play(Rotate(square, 90*DEGREES, axis=OUT, about_point=np.array([0, 1, 0])))
        self.play(square.animate.stretch(2, 0), run_time=5)
        self.wait(1)

class Image(Scene):
	def construct(self):
		asix = NumberLine(
		x_range=[-2, 2, 1],
		include_tip=True,
		include_numbers=True,
		)
		self.play(Create(asix), run_time=2)
		self.wait(1)
		func = FunctionGraph(lambda x: 3*np.cos(x+1))
		self.play(Create(func))
        