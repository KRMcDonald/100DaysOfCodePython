from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.teleport(0, 260)

    def game_over(self, score):
        self.clear()
        self.teleport(0, 0)
        self.write(f"Game Over! Score: {score}", align="center", font=("Arial", 20, "bold"))
