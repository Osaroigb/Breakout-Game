from turtle import Turtle


class Blocks:

    def __init__(self):

        self.width = 1
        self.block_list = []
        self.build_blocks()

    def create_block(self, axis_x, axis_y, color):
        """A function that creates a block with a specified color at a specified position"""

        self.block_list.append(Turtle("square"))
        self.block_list[-1].penup()
        self.block_list[-1].color(color)
        self.block_list[-1].shapesize(stretch_wid=self.width, stretch_len=2)
        self.block_list[-1].setpos(axis_x, axis_y)

    def build_blocks(self):
        """A function that builds out all the blocks for a new game"""

        self.block_list.clear()
        x_pos = -275

        for i in range(13):
            self.create_block(x_pos, 250, "red")
            self.create_block(x_pos, 220, "orange")
            self.create_block(x_pos, 190, "green")
            self.create_block(x_pos, 160, "yellow")

            x_pos += 45
