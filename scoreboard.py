from turtle import Turtle

STYLE = ('Courier', 50, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()

        self.color("White")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, font=STYLE, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(self.r_score, font=STYLE, align=ALIGNMENT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()
