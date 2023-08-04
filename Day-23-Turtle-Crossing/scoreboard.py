from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.goto(280, 260)
        self.write(f"Lives left: {self.lives}", align="right", font=FONT)

    def game_over(self):
        self.home()

        self.write("GAME OVER", align="center", font=FONT)
