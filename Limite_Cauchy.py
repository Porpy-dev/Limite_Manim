from manim import *
from math import *
global_scale = 10

class Demo(Scene):
    def construct(self):
        title = Tex("Limit of the cardinal sine :", font_size = 45).shift((0, global_scale, 0))
        exp_1 = MathTex(r"\lim_{x \to 0} \frac{\sin(x)}{x}").next_to(title, DOWN*3)

        exp_1_new = exp_1.copy()
        
        exp_2= MathTex(r"=\lim_{x \to 0} \frac{\sin(x)-0}{x-0}").next_to(exp_1, DOWN*3)
        
        exp_3= MathTex(r"=\lim_{x \to 0} \frac{\sin(x)-\sin(0)}{x-0}").next_to(exp_2, DOWN*3)
        
        def_derivative = MathTex(r"f'(h) = \lim_{x \to 0} \frac{f(h+x)-f(h)}{h+x-h}").next_to(exp_3, DOWN*3)
        
        def_derivative_new = def_derivative.copy()
        
        def_derivative_box = Rectangle(width= 7.8, height= 2, color= WHITE).move_to(def_derivative.get_center())
        
        derivative_at_0 = MathTex(r"\Leftrightarrow f'(0) = \lim_{x \to 0} \frac{f(x)-f(0)}{x-0}").next_to(def_derivative, DOWN*3.7)
        
        exp_4 = MathTex(r"\Leftrightarrow \lim_{x \to 0} \frac{\sin(x)-\sin(0)}{x-0} = \sin'(0)").next_to(derivative_at_0, DOWN*3)
        
        exp_5 = MathTex(r"\Leftrightarrow \lim_{x \to 0} \frac{\sin(x)}{x} = \cos(0)").next_to(exp_4, DOWN*3)
        
        exp_final = MathTex(r"\lim_{x \to 0} \frac{\sin(x)}{x} = 1").next_to(exp_5, DOWN*3.7)
        
        exp_final_box = Rectangle(width= 4.4, height= 2, color= WHITE).move_to(exp_final.get_center())
        
        if_and_only_if = MathTex(r"\Leftrightarrow").next_to(exp_final_box, LEFT)


        self.play(Create(title), run_time= 1.2)
        self.play(Create(exp_1), run_time= 1.2)
        self.wait(1)
        self.play(Transform(exp_1_new, exp_2), run_time= 1.2)
        self.wait(1)
        self.play(Transform(exp_2, exp_3), run_time= 1.2)
        self.wait(1)
        self.play(Create(def_derivative), Create(def_derivative_box), run_time= 1.2)
        self.wait(1)
        self.play(Transform(def_derivative_new, derivative_at_0), run_time= 1.2)
        self.wait(1)
        self.play(Transform(derivative_at_0, exp_4), run_time= 1.2)
        self.wait(1)
        self.play(Transform(exp_4, exp_5), run_time= 1.2)
        self.wait(1)
        self.play(Transform(exp_5, exp_final), Create(if_and_only_if), Create(exp_final_box), run_time= 1.2)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])