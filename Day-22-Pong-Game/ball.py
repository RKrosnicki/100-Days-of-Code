from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.setheading(random.randint(0, 360))
        self.speed("slow")
        self.color("white")
        self.base_speed = 0.05

    def move(self):
        self.forward(self.base_speed)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.base_speed += 0.01

    def ball_reset(self):
        self.setposition(0, 0)
        self.base_speed = 0.1
        if 0 <= self.heading() <= 90 or 360 > self.heading() >= 270:
            self.setheading(random.randint(90, 270))
        else:
            right_headings = [random.randint(0, 90), random.randint(270, 360)]
            self.setheading(random.choice(right_headings))

