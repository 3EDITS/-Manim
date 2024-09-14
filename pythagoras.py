from manim import *

class Pythagoras(Scene):
    def construct(self):
        rtriangle = Polygon(
            [0,0,0],
            [5,0,0],
            [0,4,0],
            color=BLUE,
            fill_opacity=0.5
        ).move_to(ORIGIN)
        label_a = Text("a").next_to(rtriangle, LEFT)
        label_b = Text("b").move_to([.8,0,0])
        label_c = Text("c").next_to(rtriangle, DOWN)

        self.play(DrawBorderThenFill(rtriangle))

        self.play(Write(label_a), Write(label_b), Write(label_c))

        group_Py = VGroup(rtriangle, label_a, label_b, label_c)

        self.play(group_Py.animate.to_edge(UL))

        format_a = MathTex("a = 3, b = 4, c=?").next_to(label_c, DOWN)
        self.play(Write(format_a))

        how_to_1 = MathTex("a^2 + b^2 = c^2").move_to([1,3,0])
        how_to_2 = MathTex("3^2 + 4^2 = c^2").move_to([1,2,0])

        how_to_3 = MathTex("9 + 16 = 25").move_to([1,1,0])
        how_to_4 = MathTex("c^2 = 25").move_to([1,0,0])
        how_to_5 = MathTex("c = \\sqrt{25}").move_to([1,-1,0])
        how_to_6 = MathTex("c = 5").move_to([1,-2,0])

        self.play(Write(how_to_1))
        self.wait(1.5)
        self.play(ReplacementTransform(how_to_1.copy(), how_to_2))
        self.wait(1.5)
        self.play(ReplacementTransform(how_to_2.copy(), how_to_3))
        self.wait(1.5)
        self.play(ReplacementTransform(how_to_3.copy(), how_to_4))
        self.wait(1.5)
        self.play(ReplacementTransform(how_to_4.copy(), how_to_5))
        self.wait(1.5)
        self.play(ReplacementTransform(how_to_5.copy(), how_to_6))

        self.wait(3)
