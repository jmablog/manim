from manim import *
from colours import joins_palette_hex

config.background_color = joins_palette_hex["deepspace"]

class OuterJoin(Scene):
    def construct(self):

        title = Text("Outer Join", font = "Rubik", weight = "BOLD")
        title.scale(1.2).set_color(joins_palette_hex["whitedwarf"])

        description = Text(
            """
            •  Data from right is
                matched to left where
                possible
            •  Other data from left
                and right is kept
                with NULLs entered
            """,
            line_spacing = 1.3, font = "Inter", weight="MEDIUM",
            # t2c is a dict that you can choose color for different text
            t2c={"left": joins_palette_hex["molten"],
                 "right": joins_palette_hex["supernova"],
                 "matched": joins_palette_hex["aurora"]}
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

        self.play(left_circle.animate.move_to(LEFT * 3.5).set_fill(opacity = 0.8), right_circle.animate.move_to(LEFT * 2).set_fill(opacity = 0.8), run_time = 2)

        join = Intersection(left_circle, right_circle, fill_color = joins_palette_hex["aurora"], fill_opacity = 0.9, stroke_color = joins_palette_hex["deepspace"]).set_stroke(width = 7).set_z_index(3)

        self.play(FadeIn(join))
        self.wait(1)

        final_circle = VGroup(left_circle, right_circle, join)

        self.play(final_circle.animate.move_to(LEFT * 2.7).scale(1.3).set_stroke(width = 10))

        self.wait(5)
        
        # EXAMPLE TABLES ANIMATION
        self.next_section("Outer Join Example")
        self.clear()
        self.add(title.to_corner(LEFT + UP))
        Text.set_default(font="Rubik")

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

        final = Table(
            [
            ["A1", "A2", "A3", "A4"],
            ["B1", "B2", "NULL", "NULL"],
            ["NULL", "NULL", "C3", "C4"],
            ["NULL", "NULL", "D3", "D4"],
            ],
            row_labels=[Text("A", weight="BOLD"), Text("B", weight="BOLD"), Text("C", weight="BOLD"), Text("D", weight="BOLD")],
            col_labels=[Text("1", weight="BOLD"), Text("2", weight="BOLD"), Text("3", weight="BOLD"), Text("4", weight="BOLD")],
            top_left_entry = Text("Key", slant=ITALIC),
            include_outer_lines=True,
            include_background_rectangle=False,
            background_rectangle_color = joins_palette_hex["molten"],
            line_config={"color": joins_palette_hex["aurora"], "stroke_width": 7}).scale(0.8)
        
        final.add_highlighted_cell((2,1), joins_palette_hex["aurora"])
        
        final.add_highlighted_cell((2,2), joins_palette_hex["aurora"])
        
        final.add_highlighted_cell((2,3), joins_palette_hex["aurora"])
        
        final.add_highlighted_cell((2,4), joins_palette_hex["aurora"])
        
        final.add_highlighted_cell((2,5), joins_palette_hex["aurora"])
        
        final.add_highlighted_cell((3,1), joins_palette_hex["molten"])
        
        final.add_highlighted_cell((3,2), joins_palette_hex["molten"])
        
        final.add_highlighted_cell((3,3), joins_palette_hex["molten"])
        
        final.add_highlighted_cell((4,1), joins_palette_hex["supernova"])
        
        final.add_highlighted_cell((4,4), joins_palette_hex["supernova"])
        
        final.add_highlighted_cell((4,5), joins_palette_hex["supernova"])
        
        final.add_highlighted_cell((5,1), joins_palette_hex["supernova"])
        
        final.add_highlighted_cell((5,4), joins_palette_hex["supernova"])
        
        final.add_highlighted_cell((5,5), joins_palette_hex["supernova"])
        
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
        
        self.play(FadeIn(left_1, right_1))

        self.wait(2)
        
        self.play(TransformMatchingShapes(left_1, left_2), TransformMatchingShapes(right_1, right_2))
        
        self.wait(2)
        
        # self.play(TransformMatchingShapes(right_2, right_3))
        
        # self.wait(2)
        
        self.play(TransformMatchingShapes(left_2, final), TransformMatchingShapes(right_2, final))
        
        self.wait(5)