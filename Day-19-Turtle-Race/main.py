from turtle import Turtle, Screen
import random

all_turtles = []
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_coord = -150


screen = Screen()
user_bet = screen.textinput("Place a bet", "Who's gonna win? (red/yellow/blue/orange/green/purple")

screen.setup(width=500, height=400)

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(-230, y_coord)
    all_turtles.append(tim)
    y_coord += 50

if user_bet:
    race_is_on = True

while race_is_on:
    for each_turtle in all_turtles:
        each_turtle.forward(random.randint(0, 10))
        if each_turtle.xcor() >= 230:
            race_is_on = False
            winner = each_turtle.pencolor()
            print(f"Winner is {winner} turtle! ")
            if user_bet == winner:
                print("You won!")
                break
            else:
                print("Better luck next time!")
                break

screen.exitonclick()
