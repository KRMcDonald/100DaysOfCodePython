from turtle import Turtle, Screen
import pandas
import pyarrow

# define the screen
screen = Screen()
screen.title("US States Guessing Game")
map_image = "blank_states_img.gif"
screen.addshape(map_image)

# define the map
map_turtle = Turtle()
map_turtle.shape(map_image)

# read in the csv with the list of states and coordinates
df = pandas.read_csv("50_states.csv")
states = df["state"].tolist()

# store previous, correct guesses
already_guessed_states = []

# define the writer turtle
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")

# track the score
score = 0

while score < 50:
    answer_state = screen.textinput(title=f"Score: {score}/50", prompt="What's a state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missed_states_list = []
        for state in states:
            if state in already_guessed_states:
                pass
            else:
                missed_states_list.append(state)
        missed_states_df = pandas.DataFrame(data=missed_states_list)
        missed_states_df.to_csv("missed_states.csv", index=False)
        break
    elif answer_state in already_guessed_states:
        print("You already guessed that.")
    elif answer_state in states:
        print("Correct!")
        score += 1
        already_guessed_states.append(answer_state)
        state_row = df[df["state"] == answer_state]
        state_x_coor = state_row["x"].max()
        state_y_coor = state_row["y"].max()
        # print(f"{answer_state}: X: {state_x_coor}, Y: {state_y_coor}")
        writer.teleport(state_x_coor, state_y_coor)
        writer.write(f"{answer_state}", False, align="left")
    else:
        print(f"Incorrect. {answer_state} is not a state.")

# screen.mainloop()
