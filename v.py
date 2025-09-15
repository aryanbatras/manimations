from manim import *

# PART 3
# Your computer’s memory can be broadly divided into two regions – the stack and the heap. The stack is used for fixed-size, short-lived data like local variables inside a function. It works like a stack of plates, where new items are placed on top and removed from the top. The heap, on the other hand, is used for dynamic, flexible data like objects, arrays, or anything that doesn’t have a fixed size at compile time. The stack is fast but limited in size, while the heap is larger but a little slower to access. So when you create a variable, depending on its type and the language you’re using, it may live in the stack or in the heap.

# PART 4
# C – In C, when you write int x = 5;, the compiler allocates space for x directly in the stack. If you use malloc to allocate memory, that memory comes from the heap, and you must manage it yourself, including freeing it when done. That’s why C gives you both power and responsibility.

# PART 5
# Java – In Java, things work a bit differently. Primitive types like int, float, or boolean are usually stored on the stack when they are local variables. But objects, like a String or a custom class, live in the heap. Variables on the stack hold only references or addresses to those objects, not the objects themselves.

# PART 6
# Python – Python simplifies things for you. Everything in Python is an object, whether it’s a number, a string, or a list. This means almost all variables are references to objects stored in the heap. When you write x = 10, you’re not storing the number 10 directly in x; instead, x is a reference pointing to an object in memory that represents the number 10.

# PART 7
# JavaScript – In JavaScript, it’s similar to Python. Primitives like numbers, strings, and booleans are stored directly, while objects and arrays are stored in the heap, and variables hold references to them. But JavaScript also has interesting behaviors with var, let, and const – which control the scope and mutability of variables. For example, let and const respect block scope, while var is function scoped.

# PART 8
# So, across languages, the core idea is the same – a variable is a way to give a name to something stored in memory. But the way that memory is managed, whether it’s automatic or manual, whether it’s value or reference, depends on the language you are working with.

# PART 9
# If you truly understand variables, you begin to see them not just as names, but as connections between human-readable code and the computer’s raw memory. And that understanding will give you a much deeper grasp of how programs actually work under the hood.

class V(Scene):
    def construct(self):

        # PART 1
        # "Let’s talk about one of the most fundamental concepts in programming – variables. At first glance, a variable might look like just a name that holds some value. For example, in Python, you write x = 10, and now x represents the number ten. But the truth is, a variable is much deeper than just a name and a value.

        # Narration
        self.add_sound("voices/voice-variables-01.mp3", time_offset=0)
        self.add_sound("voices/voice-variables-02.mp3", time_offset=47)
        self.add_sound("voices/voice-variables-03.mp3", time_offset=98)
        self.add_sound("voices/voice-variables-04.mp3", time_offset=125)
        self.add_sound("voices/voice-variables-05.mp3", time_offset=152)
        self.add_sound("voices/voice-variables-06.mp3", time_offset=182)
        self.add_sound("voices/voice-variables-07.mp3", time_offset=215)

        bg = Rectangle(width=16, height=9, stroke_width=0, fill_opacity=0.9)
        bg.set_fill(color=color_gradient([BLUE_E, TEAL_D], 5), opacity=0.9)
        self.add(bg)

        title = Text("The most fundamental concept\n in programming", weight=BOLD, font="Optima").scale(1.2).move_to(ORIGIN)
        self.play(TypeWithCursor(title, rate_func=linear, cursor=Rectangle(width=0.2, height=0.2).scale(1.2)) )

        dot = RoundedRectangle(color=color_gradient([YELLOW_B, YELLOW_E, BLUE, TEAL], 5)[0], height=3.8,
                               width=5.5).move_to(ORIGIN)
        underline = Line(LEFT * 1, RIGHT * 1, color=GOLD).next_to(title, DOWN)
        title2 = Text("Variable", weight=NORMAL, font="Optima").scale(1.5).move_to(ORIGIN)

        self.play(AnimationGroup(
                    ReplacementTransform(
                         title, title2
                     ),
                    Create(underline)
                )
            , run_time=2.5)

        self.play(
            AnimationGroup(
                DrawBorderThenFill(dot),
                underline.animate.shift(UP * 0.25).scale(0.8),
                lag_ratio=0.2
            ),
            run_time=1.5
        )

        title_down = Text("A name that holds some value", weight=NORMAL , font="Futura").scale(0.7).next_to(dot, DOWN)
        self.play(
            TransformFromCopy(title2, title_down),
            underline.animate.set_opacity(0),
            run_time=3, rate_func=smooth
        )

        python_logo = ImageMobject("assets/python-logo-removebg-preview.png").scale(0.6).next_to(dot, LEFT * 1.5)

        title3 = Text("x = 10", weight=NORMAL).scale(1.5).move_to(ORIGIN)
        self.play(AnimationGroup(
            GrowFromCenter(python_logo),
            FadeOut(title_down),
                FadeOut(underline),
                ReplacementTransform(title2, title3),
                Transform(dot, Circle(2.5, YELLOW),
                    run_time=1.5, rate_func=smooth)
             ),
            run_time=2.5, rate_func=linear)

        self.wait(4)

        # --- Final Deep Dive Animation ---
        self.play(FadeOut(python_logo))

        # Create concentric layers (representing depth)
        layers = VGroup(
            Circle(radius=2.8, color=BLUE_E, stroke_width=2),
            Circle(radius=3.3, color=TEAL_D, stroke_width=2),
            Circle(radius=3.8, color=PURPLE_B, stroke_width=2),
        ).move_to(dot.get_center())

        # Animate transition: circle expands into layers
        self.play(
            Transform(dot, layers[0]),
            run_time=2
        )
        self.play(LaggedStart(*[Create(layer) for layer in layers[1:]], lag_ratio=0.3), run_time=2)

        # Subtle glow effect
        self.play(Flash(layers[-1], color=YELLOW, flash_radius=1.5), run_time=1.2)

        self.wait(1)

        self.play(FadeOut(layers), FadeOut(title3), FadeOut(dot))


        # PART 1 Next-Step

        # Think of a variable as a container, or a label, that is connected to a specific location in memory. When you declare a variable, you’re essentially telling the computer: ‘Hey, reserve a spot for me in memory, and let me refer to it with this name.  Now, let’s dive into what really happens inside.


        # Container box for variable
        container = RoundedRectangle(corner_radius=0.2, width=2.5, height=1.5, color=TEAL).move_to(LEFT*3)
        label_x = Text("x", weight=BOLD).scale(0.8).next_to(container, UP)
        value = Text("10", font="Futura").scale(0.9).move_to(container.get_center())

        self.play(DrawBorderThenFill(container), FadeIn(label_x), run_time=1.5)
        self.play(Write(value), run_time=1.2)

        # Memory grid (a group of small squares)
        grid = VGroup(*[
            Square(0.5, color=GREY, fill_opacity=0.1)
            for _ in range(40)
        ])
        grid.arrange_in_grid(rows=5, cols=8, buff=0.15)
        grid.move_to(RIGHT*3)

        self.play(FadeIn(grid, shift=RIGHT*2), run_time=2)

        # Draw line from container to one memory cell
        target_cell = grid[18]  # pick one cell
        line = Line(container.get_right(), target_cell.get_left(), color=YELLOW)
        self.play(Create(line), run_time=1.2)

        # Highlight memory cell
        self.play(target_cell.animate.set_fill(YELLOW, opacity=0.6))
        self.play(Indicate(target_cell, color=TEAL_B))

        # Show value "10" appearing in memory
        mem_value = Text("10", font="Futura").scale(0.6).move_to(target_cell.get_center())
        self.play(Write(mem_value))


        # Cinematic zoom-in to the memory grid with epic shaking
        world = VGroup(container, label_x, value, grid, target_cell, line, mem_value)
        self.add(world)

        self.play(world.animate.scale(1.25), run_time=2, rate_func=smooth)

        # Subtitle explanation
        subtitle = Text(
            "A variable is just a label connected to a spot in memory",
            font="Futura", color=BLUE_B
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(subtitle), run_time=2)

        self.wait(4)

        self.play(FadeOut(world, subtitle))

        self.wait(4)

        # PART 2 Completely New

        # Your computer’s memory can be broadly divided into two regions – the stack and the heap. The stack is used for fixed-size, short-lived data like local variables inside a function. It works like a stack of plates, where new items are placed on top and removed from the top. The heap, on the other hand, is used for dynamic, flexible data like objects, arrays, or anything that doesn’t have a fixed size at compile time. The stack is fast but limited in size, while the heap is larger but a little slower to access. So when you create a variable, depending on its type and the language you’re using, it may live in the stack or in the heap.

        # Narration
        # Use a different audio file or check if the file is corrupted
        self.wait(2)

        # === PART 2 ===
        # Narration already queued above

        # Background shift for dramatic effect
        bg2 = Rectangle(width=16, height=9, stroke_width=0)
        bg2.set_fill(color=color_gradient([PURPLE_E, BLUE_E, TEAL_D], 7), opacity=0.85)
        self.play(FadeIn(bg2), run_time=1.5)

        # Titles for Stack & Heap
        stack_title = Text("STACK", weight=BOLD, color=YELLOW_B, font="Optima").scale(0.9).to_edge(UL, buff=1)
        heap_title = Text("HEAP", weight=BOLD, color=TEAL_B, font="Optima").scale(0.9).to_edge(UR, buff=1)

        self.play(Write(stack_title), Write(heap_title), run_time=1.5)

        # Create two memory regions
        stack_region = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.1) for _ in range(20)])
        heap_region = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.1) for _ in range(20)])

        stack_region.arrange_in_grid(rows=5, cols=4, buff=0.1).next_to(stack_title, DOWN, buff=0.5).shift(RIGHT * 0.5)
        heap_region.arrange_in_grid(rows=5, cols=4, buff=0.1).next_to(heap_title, DOWN, buff=0.5).shift(LEFT * 0.5)

        self.play(
            LaggedStart(
                *[FadeIn(sq, shift=DOWN * 0.5) for sq in stack_region],
                *[FadeIn(sq, shift=DOWN * 0.5) for sq in heap_region],
                lag_ratio=0.05
            ),
            run_time=2.5
        )

        # Decorative glowing borders
        stack_border = SurroundingRectangle(stack_region, color=YELLOW, buff=0.2, stroke_width=2)
        heap_border = SurroundingRectangle(heap_region, color=TEAL_A, buff=0.2, stroke_width=2)
        self.play(Create(stack_border), Create(heap_border))

        # --- Text Explanations ---
        stack_text = Text(
            "\nLocal variables\nFunction calls\nFixed size data",
            font="Avenir", color=LOGO_WHITE
        ).scale(1.2).move_to(ORIGIN)

        self.play(FadeIn(stack_text), run_time=2)

        self.play(Transform(stack_text, stack_text.copy().scale(0.5).next_to(stack_region, DOWN * 1.25, buff=0.2)), run_time=2)


        # --- Stack as plates ---
        plate1 = Rectangle(width=1, height=0.5, color=YELLOW_B, fill_opacity=0.8).next_to(stack_region, ORIGIN * 0.5, buff=0.5)
        plate2 = plate1.copy().next_to(plate1, UP, buff=0)
        plate3 = plate1.copy().next_to(plate2, UP, buff=0)

        self.play(FadeIn(plate1, shift=UP), run_time=1.8)
        self.play(FadeIn(plate2, shift=UP), run_time=1.8)
        self.play(FadeIn(plate3, shift=UP), run_time=1.8)

        # Highlight stack order (Last In First Out)
        self.play(Indicate(plate3, color=YELLOW_E), run_time=2)
        self.play(FadeOut(plate3, shift=UP), run_time=1.8)
        self.play(Indicate(plate2, color=YELLOW_E), run_time=2)

        heap_text = Text(
            "\nObjects\nArrays\nDynamic data",
            font="Avenir", color=LOGO_WHITE
        ).scale(1.2).move_to(ORIGIN)

        self.play(FadeIn(heap_text), run_time=2)
        self.play(Transform(heap_text, heap_text.copy().scale(0.5).next_to(heap_region, DOWN * 1.25, buff=0.2)),                  run_time=2)

        # --- Heap demonstration (dynamic allocation) ---
        obj1 = RoundedRectangle(width=1, height=0.6, corner_radius=0.2, color=TEAL_B, fill_opacity=0.7)
        obj2 = RoundedRectangle(width=1.3, height=0.8, corner_radius=0.2, color=BLUE_B, fill_opacity=0.7)
        obj3 = RoundedRectangle(width=0.8, height=0.8, corner_radius=0.2, color=PURPLE_B, fill_opacity=0.7)

        obj1.move_to(heap_region[6].get_center())
        obj2.move_to(heap_region[14].get_center())
        obj3.move_to(heap_region[16].get_center())

        self.play(GrowFromCenter(obj1), run_time=1.8)
        self.play(GrowFromCenter(obj2), run_time=1.8)
        self.play(GrowFromCenter(obj3), run_time=1.8)

        # Glow effect on heap allocation
        self.play(Flash(obj2, color=TEAL, flash_radius=1.2), run_time=1)

        # --- Subtitle ---
        subtitle2 = Text(
            "Stack → Fast, small, short-lived\nHeap → Flexible, larger, slower",
            font="Futura", color=WHITE
        ).scale(0.6).to_edge(DOWN)
        self.play(Write(subtitle2), run_time=3.5)

        self.wait(2)

        # --- Cleanup for next part ---
        self.play(
            FadeOut(stack_region), FadeOut(heap_region),
            FadeOut(stack_border), FadeOut(heap_border),
            FadeOut(plate1), FadeOut(plate2),
            FadeOut(obj1), FadeOut(obj2), FadeOut(obj3),
            FadeOut(subtitle2), FadeOut(bg2),
            run_time=2
        )

        self.play(AnimationGroup(
            Transform(stack_text, stack_text.copy().scale(1.5).move_to(UP)),
            Transform(heap_text, heap_text.copy().scale(1.5).move_to(DOWN)), run_time=2))

        self.play(AnimationGroup(Transform(stack_title, stack_title.copy().scale(1.5).next_to(stack_text, LEFT * 0.3)),
        Transform(heap_title, heap_title.copy().scale(1.5).next_to(heap_text, RIGHT * 0.3)), run_time=2))
        self.wait(2)

        self.play(FadeOut(stack_text),FadeOut(heap_text), FadeOut(stack_title), FadeOut(heap_title))

        self.wait(2)

        # PART 3 New Scene

        # C – In C, when you write int x = 5;, the compiler allocates space for x directly in the stack. If you use malloc to allocate memory, that memory comes from the heap, and you must manage it yourself, including freeing it when done. That’s why C gives you both power and responsibility.


        # === PART 3 ===
        # Narration already queued above


        # === PART 3 ===
        # Background reset
        bg3 = Rectangle(width=16, height=9, stroke_width=0)
        bg3.set_fill(color=color_gradient([BLACK, BLUE_E, GREY_E], 6), opacity=0.9)
        self.play(FadeIn(bg3), run_time=1.5)

        # Title
        c_title = Text("C Language", font="Futura", weight=BOLD, color=LOGO_WHITE).scale(1.2).to_edge(UP, buff=0.6)
        self.play(Write(c_title), run_time=1.5)

        # Code snippet (C style)
        c_code = VGroup(
            Text("int x = 5;", font="Monospace", color=WHITE, weight=LIGHT).scale(0.7),
            Text("int* p = malloc(sizeof(int));", font="Monospace", color=WHITE, weight=LIGHT).scale(0.7),
            Text("*p = 20;", font="Monospace", color=WHITE, weight=LIGHT).scale(0.7),
            Text("free(p);", font="Monospace", color=WHITE, weight=LIGHT).scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(LEFT, buff=1.2)

        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT) for line in c_code], lag_ratio=0.2), run_time=3)

        # Stack region (small grid on right-top)
        stack_region_c = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(12)])
        stack_region_c.arrange_in_grid(rows=3, cols=4, buff=0.1).to_edge(RIGHT, buff=2).shift(UP*2)

        stack_border_c = SurroundingRectangle(stack_region_c, color=YELLOW_B, buff=0.2, stroke_width=2)

        # Heap region (larger, bottom-right)
        heap_region_c = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(16)])
        heap_region_c.arrange_in_grid(rows=4, cols=4, buff=0.1).to_edge(RIGHT, buff=2).shift(DOWN*1.5)

        heap_border_c = SurroundingRectangle(heap_region_c, color=TEAL_A, buff=0.2, stroke_width=2)

        self.play(Create(stack_region_c), Create(heap_region_c), Create(stack_border_c), Create(heap_border_c), run_time=2)

        # Animate "int x = 5;" → goes to stack
        x_box = RoundedRectangle(corner_radius=0.15, width=0.8, height=0.6, fill_opacity=0.8, fill_color=YELLOW_D)
        x_text = Text("x:5", font="Futura", color=BLACK).scale(0.45).move_to(x_box.get_center())
        x_group = VGroup(x_box, x_text).move_to(stack_region_c[5].get_center())

        self.play(Indicate(c_code[0], color=GREEN_C), run_time=1.5)
        self.play(GrowFromCenter(x_group), run_time=2)
        self.play(Flash(x_group, color=GREEN_C, flash_radius=0.8), run_time=1)

        # Animate "malloc" → memory block in heap
        malloc_block = RoundedRectangle(corner_radius=0.15, width=1, height=0.7, fill_opacity=0.8, fill_color=TEAL_B)
        malloc_text = Text("p → ?", font="Futura", color=BLACK).scale(0.45).move_to(malloc_block.get_center())
        malloc_group = VGroup(malloc_block, malloc_text).move_to(heap_region_c[10].get_center())

        self.play(Indicate(c_code[1], color=TEAL_B), run_time=1.5)
        self.play(GrowFromCenter(malloc_group), run_time=2)

        # Show assignment "*p = 20;" → heap gets 20
        malloc_text_new = Text("p → 20", font="Futura", color=BLACK).scale(0.45).move_to(malloc_block.get_center())
        self.play(Indicate(c_code[2], color=TEAL_B), run_time=1.5)
        self.play(Transform(malloc_text, malloc_text_new), run_time=2)

        # Free(p) → fade out heap block
        self.play(Indicate(c_code[3], color=RED), run_time=1.5)
        self.play(FadeOut(malloc_group, shift=DOWN), run_time=2)

        # Subtitle
        subtitle3 = Text(
            "C → Stack for simple vars\nHeap for malloc (must free yourself)",
            font="Futura", color=WHITE
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(subtitle3), run_time=2.5)

        # Cleanup
        self.play(
            FadeOut(c_code), FadeOut(x_group),
            FadeOut(stack_region_c), FadeOut(heap_region_c),
            FadeOut(stack_border_c), FadeOut(heap_border_c),
            FadeOut(c_title), FadeOut(subtitle3), FadeOut(bg3),
            run_time=2
        )

        # PART 4 New Scene

        # Java – In Java, things work a bit differently. Primitive types like int, float, or boolean are usually stored on the stack when they are local variables. But objects, like a String or a custom class, live in the heap. Variables on the stack hold only references or addresses to those objects, not the objects themselves.


        # === PART 4 ===
        # Narration already queued above

        # === PART 4 ===
        # Background reset for Java scene
        bg4 = Rectangle(width=16, height=9, stroke_width=0)
        bg4.set_fill(color=color_gradient([BLACK, PURPLE_E, BLUE_E], 6), opacity=0.9)
        self.play(FadeIn(bg4), run_time=1.5)

        # Title
        java_title = Text("Java Language", font="Futura", weight=BOLD, color=LOGO_WHITE).scale(1).to_edge(UP, buff=0.6).shift(LEFT * 0.5)
        self.play(Write(java_title), run_time=1.5)

        # Code snippet (Java style)
        java_code = VGroup(
            Text("int x = 10;", font="Monospace", color=WHITE).scale(0.6),
            Text("String s = \"Hello\";", font="Monospace", color=WHITE).scale(0.6),
            Text("MyClass obj = new MyClass();", font="Monospace", color=WHITE).scale(0.6),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(LEFT, buff=1.2)

        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT) for line in java_code], lag_ratio=0.2), run_time=3)

        # Stack & Heap regions (similar to Part 2 & 3 for consistency)
        stack_region_j = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(12)])
        stack_region_j.arrange_in_grid(rows=3, cols=6, buff=0.1).to_edge(RIGHT, buff=2).shift(UP*2)
        stack_border_j = SurroundingRectangle(stack_region_j, color=YELLOW_B, buff=0.2, stroke_width=2)

        heap_region_j = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(18)])
        heap_region_j.arrange_in_grid(rows=4, cols=6, buff=0.1).to_edge(RIGHT, buff=2).shift(DOWN*1.5)
        heap_border_j = SurroundingRectangle(heap_region_j, color=TEAL_A, buff=0.2, stroke_width=2)

        self.play(Create(stack_region_j), Create(heap_region_j), Create(stack_border_j), Create(heap_border_j), run_time=2)

        # --- int x = 10; → goes to stack ---
        x_box_j = RoundedRectangle(corner_radius=0.15, width=0.8, height=0.6, fill_opacity=0.85, fill_color=YELLOW_D)
        x_text_j = Text("x:10", font="Futura", color=BLACK).scale(0.45).move_to(x_box_j.get_center())
        x_group_j = VGroup(x_box_j, x_text_j).move_to(stack_region_j[0].get_center())

        self.play(Indicate(java_code[0], color=GREEN_C), run_time=1.5)
        self.play(GrowFromCenter(x_group_j), run_time=2)
        self.play(Flash(x_group_j, color=GREEN_C, flash_radius=0.8), run_time=1)

        # --- String s = "Hello"; ---
        # Stack → reference, Heap → object
        s_box_stack = RoundedRectangle(corner_radius=0.15, width=1.1, height=0.6, fill_opacity=0.85, fill_color=BLUE_B)
        s_text_stack = Text("s → ?", font="Futura", color=BLACK).scale(0.45).move_to(s_box_stack.get_center())
        s_stack_group = VGroup(s_box_stack, s_text_stack).move_to(stack_region_j[2].get_center())

        s_heap_obj = RoundedRectangle(corner_radius=0.15, width=1.4, height=0.8, fill_opacity=0.85, fill_color=TEAL_B)
        s_heap_text = Text("\"Hello\"", font="Futura", color=BLACK).scale(0.45).move_to(s_heap_obj.get_center())
        s_heap_group = VGroup(s_heap_obj, s_heap_text).move_to(heap_region_j[1].get_center())

        self.play(Indicate(java_code[1], color=BLUE_B), run_time=1.5)
        self.play(GrowFromCenter(s_stack_group), GrowFromCenter(s_heap_group), run_time=2)

        # Reference arrow
        arrow_s = Arrow(s_stack_group.get_bottom(), s_heap_group.get_top(), buff=0.1, color=WHITE)
        self.play(Create(arrow_s), run_time=1)

        # --- MyClass obj = new MyClass(); ---
        obj_stack_box = RoundedRectangle(corner_radius=0.15, width=1.1, height=0.6, fill_opacity=0.85, fill_color=PURPLE_B)
        obj_stack_text = Text("obj → ?", font="Futura", color=BLACK).scale(0.45).move_to(obj_stack_box.get_center())
        obj_stack_group = VGroup(obj_stack_box, obj_stack_text).move_to(stack_region_j[4].get_center())

        obj_heap_obj = RoundedRectangle(corner_radius=0.15, width=1.5, height=1.0, fill_opacity=0.85, fill_color=ORANGE)
        obj_heap_text = Text("MyClass{}", font="Futura", color=BLACK).scale(0.45).move_to(obj_heap_obj.get_center())
        obj_heap_group = VGroup(obj_heap_obj, obj_heap_text).move_to(heap_region_j[10].get_center())

        self.play(Indicate(java_code[2], color=ORANGE), run_time=1.5)
        self.play(GrowFromCenter(obj_stack_group), GrowFromCenter(obj_heap_group), run_time=2)

        arrow_obj = Arrow(obj_stack_group.get_bottom(), obj_heap_group.get_top(), buff=0.1, color=WHITE)
        self.play(Create(arrow_obj), run_time=1)

        # Glow both reference arrows for emphasis
        self.play(Flash(arrow_s, color=YELLOW, flash_radius=1.2), Flash(arrow_obj, color=YELLOW, flash_radius=1.2), run_time=1)

        # Subtitle explanation
        subtitle4 = Text(
            "Java → Primitives on stack\nObjects live in heap, stack stores references",
            font="Futura", color=WHITE
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(subtitle4), run_time=1.5)

        # Cleanup
        self.play(
            FadeOut(java_code), FadeOut(x_group_j), FadeOut(s_stack_group), FadeOut(s_heap_group),
            FadeOut(obj_stack_group), FadeOut(obj_heap_group),
            FadeOut(arrow_s), FadeOut(arrow_obj),
            FadeOut(stack_region_j), FadeOut(heap_region_j),
            FadeOut(stack_border_j), FadeOut(heap_border_j),
            FadeOut(java_title), FadeOut(subtitle4), FadeOut(bg4),
            run_time=2
        )

        # PART 5 New Scene
        # Python – Python simplifies things for you. Everything in Python is an object, whether it’s a number, a string, or a list. This means almost all variables are references to objects stored in the heap. When you write x = 10, you’re not storing the number 10 directly in x; instead, x is a reference pointing to an object in memory that represents the number 10.

        # === PART 5 ===
        # Narration already queued above

        # === PART 5 ===
        # Python – Everything is an object. Variables are references to heap objects.

        # Background reset for Python scene
        bg5 = Rectangle(width=16, height=9, stroke_width=0)
        bg5.set_fill(color=color_gradient([BLACK, BLUE_D, TEAL_D], 6), opacity=0.9)
        self.play(FadeIn(bg5), run_time=1.5)

        # Title
        python_title = Text("Python Language", font="Futura", weight=BOLD, color=LOGO_WHITE).scale(1.1).to_edge(UP,
                                                                                                                buff=0.6)
        self.play(Write(python_title), run_time=1.5)

        # Code snippet (Python style)
        python_code = VGroup(
            Text("x = 10", font="Monospace", color=WHITE).scale(0.65),
            Text("s = \"Hello\"", font="Monospace", color=WHITE).scale(0.65),
            Text("arr = [1, 2, 3]", font="Monospace", color=WHITE).scale(0.65),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT, buff=1.2)

        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT) for line in python_code], lag_ratio=0.25), run_time=3)

        # Python: show Stack as just references, Heap for everything
        stack_region_p = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(8)])
        stack_region_p.arrange_in_grid(rows=2, cols=4, buff=0.1).to_edge(RIGHT, buff=2).shift(UP * 2)
        stack_border_p = SurroundingRectangle(stack_region_p, color=YELLOW_B, buff=0.2, stroke_width=2)

        heap_region_p = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(20)])
        heap_region_p.arrange_in_grid(rows=5, cols=4, buff=0.1).to_edge(RIGHT, buff=2).shift(DOWN * 1.5)
        heap_border_p = SurroundingRectangle(heap_region_p, color=TEAL_A, buff=0.2, stroke_width=2)

        self.play(Create(stack_region_p), Create(heap_region_p), Create(stack_border_p), Create(heap_border_p), run_time=2)

        # --- x = 10 ---
        x_box_p = RoundedRectangle(corner_radius=0.15, width=1.1, height=0.6, fill_opacity=0.85, fill_color=YELLOW_D)
        x_text_p = Text("x → ?", font="Futura", color=BLACK).scale(0.45).move_to(x_box_p.get_center())
        x_group_p = VGroup(x_box_p, x_text_p).move_to(stack_region_p[0].get_center())

        obj_x_heap = RoundedRectangle(corner_radius=0.15, width=1.2, height=0.7, fill_opacity=0.85, fill_color=TEAL_B)
        obj_x_text = Text("10 (int)", font="Futura", color=BLACK).scale(0.45).move_to(obj_x_heap.get_center())
        obj_x_group = VGroup(obj_x_heap, obj_x_text).move_to(heap_region_p[0].get_center())

        self.play(Indicate(python_code[0], color=YELLOW_B), run_time=1.5)
        self.play(GrowFromCenter(x_group_p), GrowFromCenter(obj_x_group), run_time=2)

        arrow_x = Arrow(x_group_p.get_bottom(), obj_x_group.get_top(), buff=0.1, color=WHITE)
        self.play(Create(arrow_x), run_time=1)

        # --- s = "Hello" ---
        s_box_p = RoundedRectangle(corner_radius=0.15, width=1.1, height=0.6, fill_opacity=0.85, fill_color=BLUE_B)
        s_text_p = Text("s → ?", font="Futura", color=BLACK).scale(0.45).move_to(s_box_p.get_center())
        s_group_p = VGroup(s_box_p, s_text_p).move_to(stack_region_p[2].get_center())

        obj_s_heap = RoundedRectangle(corner_radius=0.15, width=1.5, height=0.8, fill_opacity=0.85, fill_color=PURPLE_B)
        obj_s_text = Text("\"Hello\"", font="Futura", color=BLACK).scale(0.45).move_to(obj_s_heap.get_center())
        obj_s_group = VGroup(obj_s_heap, obj_s_text).move_to(heap_region_p[6].get_center())

        self.play(Indicate(python_code[1], color=BLUE_B), run_time=1.5)
        self.play(GrowFromCenter(s_group_p), GrowFromCenter(obj_s_group), run_time=2)

        arrow_s_p = Arrow(s_group_p.get_bottom(), obj_s_group.get_top(), buff=0.1, color=WHITE)
        self.play(Create(arrow_s_p), run_time=1)

        # --- arr = [1, 2, 3] ---
        arr_box_p = RoundedRectangle(corner_radius=0.15, width=1.2, height=0.6, fill_opacity=0.85, fill_color=ORANGE)
        arr_text_p = Text("arr → ?", font="Futura", color=BLACK).scale(0.45).move_to(arr_box_p.get_center())
        arr_group_p = VGroup(arr_box_p, arr_text_p).move_to(stack_region_p[4].get_center())

        obj_arr_heap = RoundedRectangle(corner_radius=0.15, width=2.5, height=1.0, fill_opacity=0.85, fill_color=GREEN_B)
        obj_arr_text = Text("[1,2,3]", font="Futura", color=BLACK).scale(0.45).move_to(obj_arr_heap.get_center())
        obj_arr_group = VGroup(obj_arr_heap, obj_arr_text).move_to(heap_region_p[12].get_center())

        self.play(Indicate(python_code[2], color=ORANGE), run_time=1.5)
        self.play(GrowFromCenter(arr_group_p), GrowFromCenter(obj_arr_group), run_time=2)

        arrow_arr = Arrow(arr_group_p.get_bottom(), obj_arr_group.get_top(), buff=0.1, color=WHITE)
        self.play(Create(arrow_arr), run_time=1)

        # Glow arrows simultaneously
        self.play(
            Flash(arrow_x, color=YELLOW, flash_radius=1.2),
            Flash(arrow_s_p, color=YELLOW, flash_radius=1.2),
            Flash(arrow_arr, color=YELLOW, flash_radius=1.2),
            run_time=1.5
        )

        # Subtitle explanation
        subtitle5 = Text(
            "Python → Everything is an object\nVariables are references pointing to heap",
            font="Futura", color=WHITE
        ).scale(0.6).to_edge(DOWN)

        self.play(Write(subtitle5), run_time=2)

        self.wait(3)

        # Cleanup
        self.play(
            FadeOut(python_code), FadeOut(x_group_p), FadeOut(obj_x_group),
            FadeOut(s_group_p), FadeOut(obj_s_group),
            FadeOut(arr_group_p), FadeOut(obj_arr_group),
            FadeOut(arrow_x), FadeOut(arrow_s_p), FadeOut(arrow_arr),
            FadeOut(stack_region_p), FadeOut(heap_region_p),
            FadeOut(stack_border_p), FadeOut(heap_border_p),
            FadeOut(python_title), FadeOut(subtitle5), FadeOut(bg5),
            run_time=2
        )

        # PART 6 New Scene !

        # JavaScript – In JavaScript, it’s similar to Python. Primitives like numbers, strings, and booleans are stored directly, while objects and arrays are stored in the heap, and variables hold references to them. But JavaScript also has interesting behaviors with var, let, and const – which control the scope and mutability of variables. For example, let and const respect block scope, while var is function scoped.

       # === PART 6 ===
        # Narration already queued above

        bg6 = Rectangle(width=16, height=9, stroke_width=0)
        bg6.set_fill(color=color_gradient([BLACK, BLUE_D, TEAL_E], 7), opacity=0.9)
        self.play(FadeIn(bg6), run_time=1.5)

        # Title
        js_title = Text("JavaScript Language", font="Futura", weight=BOLD, color=LOGO_WHITE).scale(1).to_edge(UP, buff=0.6)
        self.play(Write(js_title), run_time=1.5)

        # JS code snippet
        js_code = VGroup(
            Text("var a = 10;", font="Monospace", color=WHITE).scale(0.6),
            Text("let b = 20;", font="Monospace", color=WHITE).scale(0.6),
            Text("const c = 30;", font="Monospace", color=WHITE).scale(0.6),
            Text("function foo() { let x = 5; }", font="Monospace", color=WHITE).scale(0.6),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(LEFT, buff=1.2)

        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT) for line in js_code], lag_ratio=0.2), run_time=3)

        # Stack & Heap regions (JS execution context)
        exec_stack = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(14)])
        exec_stack.arrange_in_grid(rows=2, cols=7, buff=0.1).to_edge(RIGHT, buff=2).shift(UP * 2)
        stack_border_js = SurroundingRectangle(exec_stack, color=YELLOW, buff=0.2, stroke_width=2)

        heap_js = VGroup(*[Square(0.5, color=GREY, fill_opacity=0.35) for _ in range(16)])
        heap_js.arrange_in_grid(rows=4, cols=4, buff=0.1).to_edge(RIGHT, buff=2).shift(DOWN * 1.5)
        heap_border_js = SurroundingRectangle(heap_js, color=TEAL_A, buff=0.2, stroke_width=2)

        self.play(Create(exec_stack), Create(heap_js), Create(stack_border_js), Create(heap_border_js), run_time=2)

        self.wait(1)

        # --- var a = 10 ---
        a_stack = RoundedRectangle(corner_radius=0.15, width=0.75, height=0.5, fill_opacity=0.85, fill_color=YELLOW_D)
        a_text = Text("a:10", font="Futura", color=BLACK).scale(0.45).move_to(a_stack.get_center())
        a_group = VGroup(a_stack, a_text).move_to(exec_stack[0].get_center())

        self.play(Indicate(js_code[0], color=YELLOW_B), GrowFromCenter(a_group), run_time=2)

        self.wait(1)

        # --- let b = 20 ---
        b_stack = RoundedRectangle(corner_radius=0.15, width=0.9, height=0.6, fill_opacity=0.85, fill_color=BLUE_B)
        b_text = Text("b:20", font="Futura", color=BLACK).scale(0.45).move_to(b_stack.get_center())
        b_group = VGroup(b_stack, b_text).move_to(exec_stack[2].get_center())

        self.play(Indicate(js_code[1], color=BLUE_B), GrowFromCenter(b_group), run_time=2)

        self.wait(1)

        # --- const c = 30 ---
        c_stack = RoundedRectangle(corner_radius=0.15, width=1.0, height=0.6, fill_opacity=0.85, fill_color=PURPLE_B)
        c_text = Text("c:30 (const)", font="Futura", color=BLACK).scale(0.4).move_to(c_stack.get_center())
        c_group = VGroup(c_stack, c_text).move_to(exec_stack[8].get_center())

        self.play(Indicate(js_code[2], color=PURPLE_B), GrowFromCenter(c_group), run_time=2)

        self.wait(3)

        # --- function foo() { let x = 5; } ---
        foo_context = RoundedRectangle(corner_radius=0.15, width=1.4, height=0.5, fill_opacity=0.85, fill_color=TEAL_B)
        foo_text = Text("foo()", font="Futura", color=BLACK).scale(0.45).move_to(foo_context.get_center())
        foo_group = VGroup(foo_context, foo_text).move_to(exec_stack[12].get_center())

        self.play(Indicate(js_code[3], color=TEAL_B), GrowFromCenter(foo_group), run_time=2)

        # Animate closure (extra heap object for function)
        closure_obj = RoundedRectangle(corner_radius=0.15, width=1.75, height=0.8, fill_opacity=0.85, fill_color=TEAL_B)
        closure_text = Text("Closure env", font="Futura", color=BLACK).scale(0.45).move_to(closure_obj.get_center())
        closure_group = VGroup(closure_obj, closure_text).move_to(heap_js[10].get_center())

        arrow_closure = Arrow(foo_group.get_bottom(), closure_group.get_top(), buff=0.1, color=WHITE)

        self.play(GrowFromCenter(closure_group), Create(arrow_closure), run_time=2)

        # Subtitle explanation
        subtitle6 = Text(
            "JavaScript → var (function scoped), let/const (block scoped)\nClosures keep variables alive in the heap",
            font="Futura", color=WHITE
        ).scale(0.4).to_edge(DOWN)

        self.play(Write(subtitle6), run_time=4.5)

        self.wait(2)

        # Cleanup
        self.play(
            FadeOut(js_code), FadeOut(a_group), FadeOut(b_group), FadeOut(c_group), FadeOut(foo_group),
            FadeOut(closure_group), FadeOut(arrow_closure),
            FadeOut(exec_stack), FadeOut(heap_js),
            FadeOut(stack_border_js), FadeOut(heap_border_js),
            FadeOut(js_title), FadeOut(subtitle6), FadeOut(bg6),
            run_time=2
        )

        # PART 7
        # So, across languages, the core idea is the same – a variable is a way to give a name to something stored in memory. But the way that memory is managed, whether it’s automatic or manual, whether it’s value or reference, depends on the language you are working with.

        # === PART 7 ===
        # Narration already queued above

        # Cinematic gradient background (dynamic, not static)
        bg7 = Rectangle(width=16, height=9, stroke_width=0)
        bg7.set_fill(color_gradient([BLACK, BLUE_E, TEAL_D], 12), opacity=0.9)
        self.play(FadeIn(bg7, scale=1.2), run_time=1)

        # Core text fade in with zoom glow
        core_text = Text(
            "Across languages,\nthe core idea is the same –",
            font="Avenir Next", weight=BOLD, color=YELLOW
        ).scale(0.6).to_edge(UP, buff=1)

        self.play(
            FadeIn(core_text, shift=UP, scale=0.8),
            core_text.animate.set_color(WHITE),
            run_time=2
        )

        self.wait(2)

        self.play(Transform(core_text, core_text.copy().scale(0.55).move_to(ORIGIN)), run_time=2)

        # Central glowing orb (representing "Variable")
        circle = Circle(radius=1.8, color=TEAL_A, stroke_width=8)
        glow = circle.copy().set_stroke(width=0).set_fill(TEAL, opacity=0.4)

        self.play(
            Create(circle, run_time=1),
            FadeIn(glow, scale=1.5, run_time=2.5)
        )

        # Add pulsating animation to the glow
        self.play(
            glow.animate.scale(1.1).set_opacity(0.6),
            rate_func=there_and_back,
            run_time=3.5
        )

        # Keywords floating into orbit
        keywords = VGroup(
            Text("Automatic", font="Futura", color=BLUE_A).scale(0.8),
            Text("Manual", font="Futura", color=PURPLE_A).scale(0.8),
            Text("Value", font="Futura", color=GREEN_A).scale(0.8),
            Text("Reference", font="Futura", color=RED_A).scale(0.8),
        )

        # Place keywords in circular orbit positions
        for i, word in enumerate(keywords):
            angle = i * PI/2
            word.move_to(circle.get_center() + 3 * np.array([np.cos(angle), np.sin(angle), 0]))

        self.play(LaggedStart(*[FadeIn(k, scale=0.5) for k in keywords], lag_ratio=0.4), run_time=2.5)

        self.wait(1.5)

        self.play(
            circle.animate.scale(1.1).set_stroke(color=TEAL_B, width=10),
            run_time=2
        )

        self.wait(1.5)

        # Cinematic zoom-out outro
        self.play(
            FadeOut(core_text),
            FadeOut(circle),
            FadeOut(glow),
            FadeOut(keywords),
            FadeOut(bg7),
            run_time=2
        )
