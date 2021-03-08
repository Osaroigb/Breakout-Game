from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):

        super().__init__()
        self.create_paddle((0, -200))

    def create_paddle(self, pos):
        """A function that creates the user paddle"""

        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setpos(pos)

    def move_up(self):
        """A function that move the paddle up when the 'Up' arrow key is pressed"""

        if self.ycor() > 115:
            self.sety(130)
        else:
            new_y = self.ycor() + 40
            self.sety(new_y)

    def move_down(self):
        """A function that move the paddle down when the 'Down' arrow key is pressed"""

        if self.ycor() < -280:
            self.sety(-300)
        else:
            new_y = self.ycor() - 40
            self.sety(new_y)

    def move_left(self):
        """A function that move the paddle left when the 'Left' arrow key is pressed"""

        if self.xcor() < -230:
            self.setx(-255)
        else:
            new_x = self.xcor() - 40
            self.setx(new_x)

    def move_right(self):
        """A function that move the paddle right when the 'Right' arrow key is pressed"""

        if self.xcor() > 230:
            self.setx(250)
        else:
            new_x = self.xcor() + 40
            self.setx(new_x)
