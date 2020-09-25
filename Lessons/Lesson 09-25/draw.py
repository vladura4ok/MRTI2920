# class Drawer:

#     def draw_line(self):
#         pass

#     def draw_shape(self):
#         pass

class LineDrawer:

    def draw_line(self):
        print("drawing line")

class ShapeDrawer:

    def draw_shape(self):
        print("drawing shape")

class CircleDrawer(ShapeDrawer):

    def draw_shape(self):
        print("drawing circle...")

class SquareDrawer(LineDrawer):

    def draw_square(self):
        for i in range(0, 4):
            LineDrawer.draw_line(self)

class FlagDrawer(LineDrawer, ShapeDrawer):

    def draw_flag(self):
        for i in range(0, 3):
            LineDrawer.draw_line(self)
        ShapeDrawer.draw_shape(self)

class CylinderDrawer(LineDrawer, CircleDrawer):

    def draw_cylinder(self):
        LineDrawer.draw_line(self)
        LineDrawer.draw_line(self)

        CircleDrawer.draw_shape(self)
        CircleDrawer.draw_shape(self)