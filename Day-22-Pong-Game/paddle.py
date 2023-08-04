from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_x):
        super().__init__()

        self.starting_x = starting_x
        self.shape("square")
        self.penup()
        self.setx(self.starting_x)
        self.shapesize(5, 1)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


