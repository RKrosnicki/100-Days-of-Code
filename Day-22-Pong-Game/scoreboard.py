from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def point_for_left(self):
        self.l_score += 1
        self.update_scoreboard()

    def point_for_right(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner(self):
        if self.l_score > self.r_score:
            self.goto(0, 0)
            self.write("Left player is the winner!", align="center", font=("Courier", 20, "normal"))
        else:
            self.goto(0, 0)
            self.write("Right player is the winner!", align="center", font=("Courier", 20, "normal"))
