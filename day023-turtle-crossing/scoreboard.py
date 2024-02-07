from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.teleport(0,260)
        self.write(f"Score:{self.score}", False, "center", ("Courier", 24, "normal"))

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over.", False, "center", ("Courier", 24, "normal"))

