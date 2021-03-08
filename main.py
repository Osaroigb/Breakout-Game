# import all libraries and modules
from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import ScoreBoard

# setting up the game screen
game_screen = Screen()
game_screen.setup(width=600, height=650)
game_screen.bgcolor("black")
game_screen.title("Breakout Game")
game_screen.tracer(0)
game_screen.listen()

# setup and display each game component
user_paddle = Paddle()
game_ball = Ball()
game_blocks = Blocks()
scores = ScoreBoard()
game_on = True


def end_game():
    """A function that ends the game abruptly"""

    global game_on
    game_on = False


# move the paddle up and down on key presses
game_screen.onkey(user_paddle.move_up, "Up")
game_screen.onkey(user_paddle.move_down, "Down")

# move the paddle left and right on key presses
game_screen.onkey(user_paddle.move_left, "Left")
game_screen.onkey(user_paddle.move_right, "Right")

# ens the game when the space bar is pressed
game_screen.onkey(end_game, "space")

while game_on:

    game_screen.update()
    sleep(0.1)

    if game_ball.ycor() < -300:

        scores.losing_message()
        sleep(2)

        game_screen.reset()

        # a new game ball
        game_ball.create_ball()

        # rebuild new block
        game_blocks.build_blocks()

        # reset the scoreboard
        scores.user_score = 0
        scores.display_score()

        # reset the user paddle
        user_paddle.create_paddle((0, -200))

    else:
        # keep the ball moving so far the game is on
        game_ball.move()

    # end the game once all the blocks have been destroyed
    if scores.user_score == 52 and len(game_blocks.block_list) == 0:

        game_on = False
        scores.winning_message()

    for block in game_blocks.block_list:

        if game_ball.distance(block) < 20:

            game_ball.paddle_bounce()  # bounce the ball off the block

            # and destroy any block the ball hit
            block_index = game_blocks.block_list.index(block)
            game_blocks.block_list.pop(block_index)
            block.hideturtle()

            scores.update_score()  # increase the user score by 1

    # bounce the ball off the left and right walls of the game screen
    if (game_ball.xcor() > 280) or (game_ball.xcor() < -280):
        game_ball.wall_bounce()

    # bounce the ball off the paddle of the user and the scoreboard
    if game_ball.distance(user_paddle) < 30 or game_ball.ycor() > 250:
        game_ball.paddle_bounce()


game_screen.exitonclick()
