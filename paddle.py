import random
import turtle
from turtle import Turtle


MOVE_DISTANCE = 20
HEADING = 90
screen = turtle.Screen()

tony = "images/tony.gif"
paulie = "images/paulie.gif"
christopher = "images/christopher.gif"
bada_bing ="images/bada-bing.gif"


screen.addshape(bada_bing)
screen.addshape(tony)
screen.addshape(paulie)
screen.addshape(christopher)
turtle.shape(bada_bing)

icons = [tony, paulie, christopher]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(random.choice(icons))
        self.shapesize(stretch_len=15, stretch_wid=50)
        self.color("White")
        self.penup()
        self.setheading(HEADING)
        self.goto(position)

    def up(self):
        new_y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_pos)

    def down(self):
        new_y_pos = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y_pos)
