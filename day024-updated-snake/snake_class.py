# import other modules
from turtle import Turtle, Screen
import time
import random


# define Snake class
class Snake():

    def __init__(self):

        self.segments = []
        self.locations = []
        self.move_distance = 20
        self.sleep_time = 0.05
        self.colors_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue",
                            "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown"]

        for t in range(0, 3):
            x = t * -20
            y = 0
            new_seg = Turtle()
            new_seg.teleport(x, y)
            new_seg.speed("fastest")
            if t == 0:
                new_seg.color("white")
                new_seg.shape("arrow")
            else:
                new_seg.color(random.choice(self.colors_list))
                new_seg.shape("square")
            new_seg.penup()
            self.segments.append(new_seg)

    def move_up(self):
        cur_heading = self.segments[0].heading()
        if cur_heading != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        cur_heading = self.segments[0].heading()
        if cur_heading != 90:
            self.segments[0].setheading(270)

    def move_right(self):
        cur_heading = self.segments[0].heading()
        if cur_heading != 180:
            self.segments[0].setheading(0)

    def move_left(self):
        cur_heading = self.segments[0].heading()
        if cur_heading != 0:
            self.segments[0].setheading(180)

    def move(self):
        for i in range(0, len(self.segments)):
            time.sleep(self.sleep_time)
            self.locations.append(self.segments[i].xcor())
            self.locations.append(self.segments[i].ycor())
            if i == 0:
                self.segments[0].forward(self.move_distance)
            else:
                prev_x = self.locations[-4]
                prev_y = self.locations[-3]
                self.segments[i].goto(prev_x, prev_y)

    def add_segment(self):
        new_seg = Turtle()
        new_seg.speed("fastest")
        new_seg.color(random.choice(self.colors_list))
        new_seg.shape("square")
        new_seg.penup()

        prev_x = self.locations[-4]
        prev_y = self.locations[-3]

        new_seg.teleport(prev_x, prev_y)

        self.segments.append(new_seg)

    def detect_collision_with_self(self):
        for seg in self.segments[2:len(self.segments)]:
            if self.segments[0].distance(seg.xcor(), seg.ycor()) < 10:
                return False

    def reset(self):
        for seg in self.segments[3:]:
            seg.clear()
            seg.hideturtle()
        del self.segments[3:]
        # time.sleep(5)
        self.segments[0].teleport(0,0)
