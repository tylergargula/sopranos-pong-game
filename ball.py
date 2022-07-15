from turtle import Turtle
import time
from turtle import Screen

screen = Screen()

gabagool = "images/gabagool.gif"
screen.addshape(gabagool)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(gabagool)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(new_x, new_y)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .75

    def refresh(self):
        self.goto(0, 0)
        time.sleep(2)
        self.move_speed = 0.1
        self.bounce_x()
