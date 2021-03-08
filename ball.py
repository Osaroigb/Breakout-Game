from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """A class constructor """

        super().__init__()
        self.x_move = 10
        self.y_move = 10

        self.create_ball()

    def create_ball(self):
        """A function that creates a new ball for the game"""

        self.penup()
        self.shape("circle")
        self.color("white")
        self.y_move = 10
        self.setpos(0, 50)

    def move(self):
        """A function that moves the ball to a certain position"""

        self.clearstamps()
        axis_x = self.xcor() + self.x_move
        axis_y = self.ycor() - self.y_move
        self.setpos(axis_x, axis_y)

    def wall_bounce(self):
        """A function that makes the ball bounce off the left and right walls of the game screen"""

        self.x_move *= -1

    def paddle_bounce(self):
        """A function that makes the ball bounce off the paddle of the user and increase it's speed each time"""

        self.y_move *= -1

        # if self.y_move < 0:
        #     self.y_move -= 1
        # elif self.y_move > 0:
        #     self.y_move += 1

    def block_bounce(self):
        """A function that makes the ball bounce off a block"""

        self.y_move *= -1
