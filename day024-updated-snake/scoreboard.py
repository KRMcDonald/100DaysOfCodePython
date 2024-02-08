from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color("white")
        self.teleport(x, y)
        self.score = 0
        self.hs_file = open("high_score.txt", "r")
        self.high_score = int(self.hs_file.read())
        self.hideturtle()

    def reset(self):
        self.score = 0
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.hs_file = open("high_score.txt", "w")
        if self.score > self.high_score:
            self.high_score = self.score
            self.hs_file.write(str(self.high_score))
            self.hs_file.close()

    def increase_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.hs_file = open("high_score.txt", "w")
            self.hs_file.write(str(self.high_score))
            self.hs_file.close()


    def write_score(self):
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="center", font=("Arial", 20, "bold"))
