import random
import turtle
from turtle import Turtle


MOVE_DISTANCE = 20
HEADING = 90
screen = turtle.Screen()

tony = "images/tony.gif"
paulie = "images/paulie.gif"
christopher = "images/christopher.gif"

screen.addshape(tony)
screen.addshape(paulie)
screen.addshape(christopher)

icons = [tony, paulie, christopher]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(random.choice(icons))
        self.shapesize(stretch_len=10)
        self.color("white")
        self.penup()
        self.setheading(HEADING)
        self.goto(position)

    def up(self):
        new_y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_pos)

    def down(self):
        new_y_pos = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y_pos)
