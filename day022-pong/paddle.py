from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(5.0, 1.0)
        self.penup()
        self.move_distance = 30
        if side == "right":
            self.color("blue")
            self.teleport(350, 0)
        elif side == "left":
            self.color("red")
            self.teleport(-350, 0)

    def move_up(self):
        cur_y = self.ycor()
        self.goto(self.xcor(), cur_y + self.move_distance)

    def move_down(self):
        cur_y = self.ycor()
        self.goto(self.xcor(), cur_y - self.move_distance)

