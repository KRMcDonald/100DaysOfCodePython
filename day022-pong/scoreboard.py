from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.shapesize(3.0, 3.0)
        if side == "right":
            self.color("blue")
            self.teleport(35, 250)
        elif side == "left":
            self.color("red")
            self.teleport(-35, 250)
        self.hideturtle()

    def add_to_score(self):
        self.score += 1