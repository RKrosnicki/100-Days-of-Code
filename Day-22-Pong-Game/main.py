from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

ball = Ball()

scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_wall()

    if ball.distance(r_paddle) <= 50 and ball.xcor() > 330 or ball.distance(l_paddle) <= 50 and ball.xcor() < -330:
        ball.bounce_paddle()
    elif ball.xcor() > 390:
        scoreboard.point_for_left()
        ball.ball_reset()
    elif ball.xcor() < -390:
        scoreboard.point_for_right()
        ball.ball_reset()

    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        scoreboard.winner()
        game_is_on = False


screen.exitonclick()
