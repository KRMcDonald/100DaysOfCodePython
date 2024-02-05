from turtle import Turtle
import time
from scoreboard import Scoreboard


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.move_distance = 30

    def start_move(self):
        self.teleport(0, 0)
        self.setheading((self.towards(400, 200)))
        self.move_distance = 30
        # print(self.heading())
        self.forward(self.move_distance)
        time.sleep(0.15)

    def move(self):
        self.forward(self.move_distance)
        time.sleep(0.15)

    def detect_top_collision(self):
        if self.ycor() >= 285:
            # print("top collision detected")
            return True

    def detect_bottom_collision(self):
        if self.ycor() <= -285:
            return True

    def detect_point_scored(self):
        if self.xcor() >= 400:
            return "left"
        elif self.xcor() <= -400:
            return "right"

    def bounce(self, normal_angle):
        new_heading = (2*normal_angle - (self.heading()+180)) % 360
        # print(new_heading)
        self.setheading(new_heading)

    def detect_paddle(self, paddle):
        if self.distance(paddle.xcor(),paddle.ycor()) <= abs(50):
            self.move_distance += 5
            return True
