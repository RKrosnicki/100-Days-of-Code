from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.hideturtle()
        self.color("white")
        self.sety(270)
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def type(self):
        self.clear()
        self.write(f"Score: {self.total_score} High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            with open("data.txt", "w") as data:
                data.write(str(self.total_score))

        self.total_score = 0
        self.type()

    # def game_over(self):
    #     self.sety(0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
