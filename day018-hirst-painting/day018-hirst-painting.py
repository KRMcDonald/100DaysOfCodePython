# Extract colors from existing dot picture by Damien Hirst
import colorgram

colors_obj = colorgram.extract('image.jpg',15)
colors_tup_list = []
for n in range(0,15):
    cur_color = colors_obj[n]
    r = cur_color.rgb[0]
    g = cur_color.rgb[1]
    b = cur_color.rgb[2]
    colors_tup_list.append((r, g, b))

# Removing background (white-ish) colors from the list
del colors_tup_list[0]
del colors_tup_list[3]


# "Recreate" the art style
from turtle import Turtle, Screen
import random


bob = Turtle()
screen = Screen()
bob.color("green")
bob.shape("turtle")
bob.speed("fastest")
screen.colormode(255)


def get_random_color_tuple():
    num = random.randint(0, len(colors_tup_list) - 1)
    return colors_tup_list[num]


def across_row_9():
    bob.pendown()
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    bob.penup()
    bob.forward(50)


def right_edge():
    bob.pendown()
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    bob.penup()


# Main program starts here
bob.teleport(-250,-250)

for n in range(0,10):
    y = -200 + (n * 50)
    for i in range(0,10):
        tup = get_random_color_tuple()
        r = tup[0]
        g = tup[1]
        b = tup[2]
        bob.pencolor(r,g,b)
        bob.fillcolor(r,g,b)
        if i < 9:
            across_row_9()
        elif i == 9:
            right_edge()
            bob.teleport(-250, y)

bob.hideturtle()

# At End
screen.exitonclick()