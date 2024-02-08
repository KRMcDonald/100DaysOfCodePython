# TODO: create the snake (3 squares) - done
# TODO: make the snake automatically move forward - done
# TODO: control snake with arrows - can't get to work

# TODO: create food TODO: create scoreboard TODO: detect collision with wall - game over TODO: detect collision
#  between head and another part of the snake - game over - can't stop the snake from going backwards


# import modules
from turtle import Turtle, Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

# a function, it should probably go somewhere else
def game_over_message():
    go = Scoreboard(0, 0)
    go.write("Game Over", False, align="center", font=("Arial", 20, "bold"))
    screen.update()
    time.sleep(5)
    go.clear()
    fud.new_location()
    screen.update()


# initialize screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a scoreboard
sb = Scoreboard(0, 260)
sb.write_score()

# create a food
fud = Food()

# create a snake
ssss = Snake()

screen.listen()
screen.onkey(ssss.move_up, "Up")
screen.onkey(ssss.move_down, "Down")
screen.onkey(ssss.move_left, "Left")
screen.onkey(ssss.move_right, "Right")

game_on = True
sb.hs_file.close()

while game_on:
    screen.update()
    ssss.move()

    # detect collision with food
    if ssss.segments[0].distance(fud.xcor(), fud.ycor()) < 20:
        fud.nom_message(sb.score)
        fud.new_location()
        sb.score += 1
        sb.increase_high_score()
        sb.clear()
        sb.write_score()
        screen.update()
        ssss.add_segment()
        screen.update()

    # detect collision with wall
    if ssss.segments[0].xcor() < -280 or ssss.segments[0].xcor() > 280:
        sb.game_over()
        sb.clear()
        sb.write_score()
        screen.update()
        # game_on = False
        sb.reset()
        fud.reset()
        game_over_message()
        ssss.reset()

    elif ssss.segments[0].ycor() < -280 or ssss.segments[0].ycor() > 280:
        sb.game_over()
        sb.clear()
        sb.write_score()
        screen.update()
        # game_on = False
        sb.reset()
        fud.reset()
        game_over_message()
        ssss.reset()

    # detect collision with self
    if ssss.detect_collision_with_self() == False:
        sb.game_over()
        sb.clear()
        sb.write_score()
        screen.update()
        # game_on = False
        sb.reset()
        fud.reset()
        game_over_message()
        ssss.reset()

# Goes at end of file
screen.exitonclick()
