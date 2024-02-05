# TODO: keep score
# TODO: move paddles
# TODO: register when ball hits a paddle
# TODO: register when a ball hits a side wall
# TODO: register when the ball hits a back wall
# TODO: calculate the trajectory of the ball
# TODO: scoreboard, ball, and paddles could probably all be their own classes

# TODO: (add) create the screen
# TODO: have a scoreboard object and class, which keeps to scores, and can call a function to increment each side
# TODO: class for paddles, and two paddles, class should tell how to control them
# TODO: ball class, probably most of the functions and explains how the ball moves

# import modules
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

# initialize the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# initialize both scoreboards
sb_right = Scoreboard("right")
sb_left = Scoreboard("left")
sb_right.write(sb_right.score, False, "center", ("Arial", 20, "bold"))
sb_left.write(sb_left.score, False, "center", ("Arial", 20, "bold"))
screen.update()

# initialize the paddles
right_paddle = Paddle("right")
left_paddle = Paddle("left")
screen.update()

# Creating paddle controls
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.update()

# create the ball
ball = Ball()

game_on = True

ball.start_move()
screen.update()

while game_on == True:
    ball.move()
    screen.update()
    if ball.detect_paddle(right_paddle) == True:
        ball.bounce(180)
        screen.update()
    elif ball.detect_paddle(left_paddle) == True:
        ball.bounce(0)
        screen.update()
    elif ball.detect_point_scored() == "right":
        sb_right.add_to_score()
        sb_right.clear()
        sb_right.write(sb_right.score, False, "center", ("Arial", 20, "bold"))
        ball.start_move()
        screen.update()
    elif ball.detect_point_scored() == "left":
        sb_left.add_to_score()
        sb_left.clear()
        sb_left.write(sb_left.score, False, "center", ("Arial", 20, "bold"))
        ball.start_move()
        screen.update()
    elif ball.detect_top_collision() == True:
        ball.bounce(270)
        screen.update()
    elif ball.detect_bottom_collision() == True:
        ball.bounce(90)
        screen.update()
    screen.update()

# Goes at end of file
screen.exitonclick()
