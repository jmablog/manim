from manim import *
from colours import joins_palette_hex

config.background_color = joins_palette_hex["deepspace"]

class LeftJoin(Scene):
    def construct(self):

        title = Text("Left Join", font = "Rubik", weight = "BOLD")
        title.scale(1.2).set_color(joins_palette_hex["whitedwarf"])

        description = Text(
            """
            •  All data from left is kept
            •  Matching data from right
               is kept
            •  Other data from right
               is dropped
            """,
            line_spacing = 1.3, font = "Inter", weight="MEDIUM",
            # t2c is a dict that you can choose color for different text
            t2c={"left": joins_palette_hex["molten"],
                 "right": joins_palette_hex["supernova"],
                 "Matching": joins_palette_hex["aurora"]}
        )

        description.set_width(config.frame_width / 3)

        left_circle = Circle().move_to(LEFT * 4.5).scale(1.85)
        right_circle = Circle().move_to(LEFT * 0.7).scale(1.85)

        left_circle.set_fill(color = joins_palette_hex["molten"], opacity = 0.9)
        left_circle.set_stroke(color = joins_palette_hex["deepspace"], width = 7)

        right_circle.set_fill(color = joins_palette_hex["supernova"], opacity = 0.9)
        right_circle.set_stroke(color = joins_palette_hex["deepspace"], width = 7)

        self.add(title.to_corner(LEFT + UP), left_circle, description.to_edge(RIGHT, 0.8)).wait(1)
        self.play(FadeIn(right_circle))
        self.play(right_circle.animate.move_to(LEFT * 2.5).set_fill(opacity = 0.8), run_time = 2)

        join = Intersection(left_circle, right_circle, fill_color = joins_palette_hex["aurora"], fill_opacity = 0.9, stroke_color = joins_palette_hex["deepspace"]).set_stroke(width = 7)

        self.play(FadeIn(join))
        self.wait(1)
        self.play(FadeOut(right_circle))

        final_circle = VGroup(left_circle, join)

        self.play(final_circle.animate.move_to(LEFT * 3).scale(1.3).set_stroke(width = 10))

        self.wait(5)


        # EXAMPLE TABLES ANIMATION
        self.next_section("Left Join Example")
        self.clear()
        self.add(title.to_corner(LEFT + UP))
        Text.set_default(font="Rubik")

        left_1 = Table(
            [["A1", "A2"],
            ["B1", "B2"]],
            row_labels=[Text("A", weight="BOLD"), Text("B", weight="BOLD")],
            col_labels=[Text("1", weight="BOLD"), Text("2", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["molten"],
            line_config={"color": joins_palette_hex["molten"], "stroke_width": 7}).scale(0.8).to_edge(LEFT, 1)
        
        left_2 = Table(
            [
            ["A1", "A2"],
            ["B1", "B2"]
            ],
            row_labels=[Text("A", weight="BOLD"), Text("B", weight="BOLD")],
            col_labels=[Text("1", weight="BOLD"), Text("2", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["molten"],
            line_config={"color": joins_palette_hex["molten"], "stroke_width": 7}).scale(0.8).to_edge(LEFT, 1)
        
        left_2.add_highlighted_cell((2,1), joins_palette_hex["aurora"])
        
        left_2.add_highlighted_cell((2,2), joins_palette_hex["aurora"])
        
        left_2.add_highlighted_cell((2,3), joins_palette_hex["aurora"])

        left_3 = Table(
            [
            ["A1", "A2", "A3", "A4"],
            ["B1", "B2", "NULL", "NULL"]
            ],
            row_labels=[Text("A", weight="BOLD"), Text("B", weight="BOLD")],
            col_labels=[Text("1", weight="BOLD"), Text("2", weight="BOLD"), Text("3", weight="BOLD"), Text("4", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["molten"],
            line_config={"color": joins_palette_hex["molten"], "stroke_width": 7}).scale(0.8)
        
        left_3.add_highlighted_cell((2,1), joins_palette_hex["aurora"])
        
        left_3.add_highlighted_cell((2,2), joins_palette_hex["aurora"])
        
        left_3.add_highlighted_cell((2,3), joins_palette_hex["aurora"])
        
        left_3.add_highlighted_cell((2,4), joins_palette_hex["aurora"])
        
        left_3.add_highlighted_cell((2,5), joins_palette_hex["aurora"])
        
        right_1 = Table(
            [
            ["A3", "A4"],
            ["C3", "C4"],
            ["D3", "D4"]
            ],
            row_labels=[Text("A", weight="BOLD"), Text("C", weight="BOLD"), Text("D", weight="BOLD")],
            col_labels=[Text("3", weight="BOLD"), Text("4", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["supernova"],
            line_config={"color": joins_palette_hex["supernova"], "stroke_width": 7}).scale(0.8).to_edge(RIGHT, 1)
        
        right_2 = Table(
            [
            ["A3", "A4"],
            ["C3", "C4"],
            ["D3", "D4"]
            ],
            row_labels=[Text("A", weight="BOLD"), Text("C", weight="BOLD"), Text("D", weight="BOLD")],
            col_labels=[Text("3", weight="BOLD"), Text("4", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["supernova"],
            line_config={"color": joins_palette_hex["supernova"], "stroke_width": 7}).scale(0.8).to_edge(RIGHT, 1)
        
        right_2.add_highlighted_cell((2,1), joins_palette_hex["aurora"])
        
        right_2.add_highlighted_cell((2,2), joins_palette_hex["aurora"])
        
        right_2.add_highlighted_cell((2,3), joins_palette_hex["aurora"])
        
        right_3 = Table(
            [
            ["A3", "A4"]
            ],
            row_labels=[Text("A", weight="BOLD")],
            col_labels=[Text("3", weight="BOLD"), Text("4", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["supernova"],
            line_config={"color": joins_palette_hex["supernova"], "stroke_width": 7}).scale(0.8).to_edge(RIGHT, 1)
        
        right_3.add_highlighted_cell((2,1), joins_palette_hex["aurora"])
        
        right_3.add_highlighted_cell((2,2), joins_palette_hex["aurora"])
        
        right_3.add_highlighted_cell((2,3), joins_palette_hex["aurora"])
        
        self.play(FadeIn(left_1, right_1))

        self.wait(2)
        
        self.play(TransformMatchingShapes(left_1, left_2), TransformMatchingShapes(right_1, right_2))
        
        self.wait(2)
        
        self.play(TransformMatchingShapes(right_2, right_3))
        
        self.wait(2)
        
        self.play(TransformMatchingShapes(left_2, left_3), TransformMatchingShapes(right_3, left_3))
        
        self.wait(5)
        
