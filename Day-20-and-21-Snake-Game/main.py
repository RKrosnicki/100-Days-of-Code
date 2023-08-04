from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Radkowy snejk")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    scoreboard.type()
    time.sleep(0.1)
    snake.move()

    if abs(snake.segments[0].xcor()) >= 290 or abs(snake.segments[0].ycor()) >= 290:
        #game_is_on = False
        #scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset_snake()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.total_score += 1
        snake.extend()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()
