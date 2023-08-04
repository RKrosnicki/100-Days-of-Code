import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

stamp = turtle.Turtle()
stamp.penup()
stamp.hideturtle()

states = pd.read_csv("50_states.csv")
states_list = states["state"].to_list()

while len(states_list) > 0:
    answer_state = screen.textinput(title=f"{50 - len(states_list)}/50) Guess the State",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    for state in states_list:
        if answer_state == state:

            answers_x = states["x"][states.state == state].iloc[0]
            answers_y = states["y"][states.state == state].iloc[0]
            stamp.goto(answers_x, answers_y)
            states_list.remove(state)
            answer = states["state"][states.state == state].iloc[0]
            stamp.write(answer, align="center", font=("Courier", 8, "normal"))

with open("states_to_learn.csv", "w") as states_to_learn:
    for state in states_list:
        states_to_learn.write(f"{state}\n")
