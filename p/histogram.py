from math import ceil
from manim import *
from colours import hist_palette_hex

results = [0.1, 1, 1.5, 2, 2.5, 2.7, 3, 4, 5]

bins = list((ceil(results[x]) - 0.5) for x in range(len(results)))

coord_range = list(x + 1 for x in range(0, max(results)))

occurrences = [[x,bins.count(x)] for x in set(bins)]

x_max = max(results)
y_max = max([x[1] for x in occurrences])

def generate_coords(occ):
    x = occ[0]
    y = occ[1]
    o = []
    for z in range(1, y + 1):
        o.append([x, z])
    return(o)

point_coords = [x for y in list(map(generate_coords, occurrences)) for x in y]

config.background_color = hist_palette_hex["deepspace"]

class Histogram(Scene):
    def construct(self):

        grid = Axes(
            x_range=[0, x_max, 1],  # step size determines num_decimal_places.
            y_range=[0, y_max, 1],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": coord_range,
                "font_size": 24,
            },
            tips=False,
        )

        dots = VGroup()

        for x in point_coords:
            dots += Dot(point = grid.c2p(x[0], x[1] - 0.5, 0), radius = 0.7, color = hist_palette_hex["supernova"])

        self.add(grid)

        self.play(Create(dots))

        self.wait(2)

        squares = VGroup()

        for dot in dots:
            squares += Square(1).set_fill(hist_palette_hex["molten"], 1).set_stroke(width = 0).match_x(dot).match_y(dot)

        # self.play(TransformMatchingShapes(dots, squares), run_time = 2)

        # for sq in squares:
        #     self.play(sq.animate.scale(1.5), run_time = 0.01)

        for i, dot in enumerate(dots):
            self.play(Transform(dot, squares[i]), run_time = 0.1)
            self.play(squares[i].animate.scale(1.5), run_time = 0.1)
        
        self.wait(2)