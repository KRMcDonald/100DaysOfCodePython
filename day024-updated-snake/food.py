from turtle import Turtle
import random
import time


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.colors_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown"]
        self.shape("turtle")
        self.penup()
        self.color(random.choice(self.colors_list))
        self.speed("fastest")
        self.teleport(random.randint(-250, 250), random.randint(-250, 250))
        self.messages_list = ["OM NOM NOM", "TURTLES ARE DELISH", "ESPECIALLY THE ENDANGERED ONES"]

    def new_location(self):
        self.color(random.choice(self.colors_list))
        self.teleport(random.randint(-250, 250), random.randint(-250, 250))

    def nom_message(self, score):
        if score <= 2:
            self.write(f"{self.messages_list[score]}", align="center", font=("Arial", 10, "normal"))
        else:
            self.write(f"{random.choice(self.messages_list)}", align="center", font=("Arial", 10, "normal"))


    def reset(self):
        self.clear()
