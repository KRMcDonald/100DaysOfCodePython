# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.starting_move_distance = 5
        self.move_increment = 10
        self.color(random.choice(self.colors_list))
        self.shape("square")
        self.shapesize(1,2,1)
        self.penup()
        self.setheading(180)
        self.teleport(300, random.randint(-250,250))

    def move_forward(self):
        self.forward(self.starting_move_distance)


    def level_up(self, level):
        self.starting_move_distance += (self.move_increment * level)
