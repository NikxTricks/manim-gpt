from manim import *

class IntegralVisualization(Scene):
    def construct(self):
        # Step 1: Draw the function y = x^2
        ax = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 15, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        def func(x):
            return x ** 2

        graph = ax.plot(func, color=YELLOW)

        self.add(ax, labels, graph)

        # Step 2: Shade the area under the curve from x = 0 to x = a
        area = ax.get_riemann_rectangles(graph, x_range=[0, 2], fill_opacity=0.3, fill_color=BLUE)
        self.play(FadeIn(area))

        # Step 3: Display the integral symbol, function, and limits of integration
        integral = MathTex(r"\int_0^a x^2 \, dx")
        integral.to_edge(UP)
        self.play(Write(integral))

        # Step 4: Calculate and display the result of the integral
        result = MathTex(r"= \frac{1}{3} a^3")
        result.next_to(integral, DOWN)
        self.play(Write(result))

        # Wait for a few seconds before ending the scene
        self.wait(3)