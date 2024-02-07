import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
player.teleport(player.start_x,player.start_y)

screen.listen()
screen.onkey(player.move_up,"Up")

sb = Scoreboard()

# stores car objects that all have the same name
list_of_cars = []

# tracks the six loops to generate a new car
loop_counter = 5

game_is_on = True

while game_is_on:
    if loop_counter == 5:
        loop_counter = 0
        car = CarManager()
        car.level_up(sb.score)
        list_of_cars.append(car)
    for car in list_of_cars:
        car.move_forward()
    if player.detect_car_collision(list_of_cars):
        sb.game_over()
        game_is_on = False
    if player.detect_top_reached():
        sb.clear()
        sb.score += 1
        sb.write(f"Score:{sb.score}", False, "center", ("Courier", 24, "normal"))
        player.level_up()
    loop_counter += 1
    time.sleep(0.1)
    screen.update()

screen.exitonclick()