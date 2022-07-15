from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

r_paddle = Paddle((335, 0))
l_paddle = Paddle((-335, 0))
ball = Ball()

# TODO 1: Create Screen
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Rone's Pong Game")
screen.tracer(0)

# TODO 2: Create a Paddle that responds to Key Presses
screen.listen()

# keyboard-arrow events - right paddle
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# keyboard-arrow events - left paddle
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
scoreboard = Scoreboard()


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.update_score()
    ball.move()

    # TODO 3: Create ball bounce/dynamics
    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 325 or ball.xcor() < -325:
        if ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50:
            ball.bounce_x()



    # Detect r_paddle out of bounds
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    # Detect l_paddle out of bounds
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()




screen.exitonclick()
