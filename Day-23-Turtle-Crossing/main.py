import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
timer_flag = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

car = CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.drive()

    timer_flag += 1
    if timer_flag % 5 == 0:
        car.add_a_car()

    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.level += 1
        scoreboard.lives += 1
        player.reset_pos()
        car.accelerate()

    for c in car.cars:
        if -45 < c.xcor() < 45:
            if (player.ycor() < 0) and (player.ycor() + 20 > c.ycor() > player.ycor() - 20):
                scoreboard.lives -= 1
                player.reset_pos()
            elif (player.ycor() >= 0) and (player.ycor() - 20 < c.ycor() < player.ycor() + 20):
                scoreboard.lives -= 1
                player.reset_pos()

    if scoreboard.lives <= 0:
        game_is_on = False

    scoreboard.update_scoreboard()
    screen.update()

scoreboard.game_over()
screen.update()
screen.exitonclick()
