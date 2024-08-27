from manim import *

class QuadraticEquation(Scene):
    def construct(self):
        # ตั้งโจทย์สมการ
        equation = MathTex("2x^2 + 3x - 5 = 0")
        self.play(Write(equation))
        self.wait(1)

        # ย้ายสมการขึ้นไปข้างบน
        self.play(equation.animate.to_edge(UP))
        self.wait(1)

        # อธิบาย a b c
        explain_formula = MathTex("a = 2, b = 3, c = -5")
        explain_formula.next_to(equation, DOWN, buff=0.5)

        
        self.play(FadeIn(explain_formula))
        self.wait(1)

        self.play(Indicate(explain_formula))
        self.wait(1)

        # สูตร
        formula = MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")
        self.play(Write(formula))
        self.wait(1)

        # แก้สมการ
        substitution = MathTex("x = \\frac{-3 \\pm \\sqrt{3^2 - 4 \\ (2) \\ (-5)}}{2 (2)}")
        self.play(Transform(formula, substitution))
        self.wait(2)

      
        sqrt_simplify = MathTex("x = \\frac{-3 \\pm \\sqrt{9 + 40}}{4}")
        self.play(Transform(formula, sqrt_simplify))
        self.wait(2)

       
        sqrt_value = MathTex("x = \\frac{-3 \\pm \\sqrt{49}}{4}")
        self.play(Transform(formula, sqrt_value))
        self.wait(2)

        
        sqrt_result_plus = MathTex("x_1 = \\frac{-3 + 7}{4}")
        sqrt_result_minus = MathTex("x_2 = \\frac{-3 - 7}{4}")
        sqrt_result_all = VGroup(sqrt_result_plus, sqrt_result_minus).arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Transform(formula, sqrt_result_all))

        self.wait(2)

        final_result_plus = MathTex("x_1 = \\frac{4}{4}")
        final_result_minus = MathTex("x_2 = \\frac{-10}{4}")
        final_result_all = VGroup(final_result_plus, final_result_minus).arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Transform(formula, final_result_all))

        self.wait(2)


        # คำตอบ
        solution1 = MathTex("x_1 = 1")
        solution2 = MathTex("x_2 = -\\frac{5}{2}")
        solutions = VGroup(solution1, solution2).arrange(DOWN, center=False, aligned_edge=LEFT)
        self.play(Transform(formula, solutions))
        self.wait(2)

        self.play(Indicate(solution1))
        self.wait(1)
        self.play(Indicate(solution2))
        self.wait(1)
