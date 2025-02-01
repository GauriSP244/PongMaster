import turtle
from turtle import Turtle,Screen
from paddle import *
from ball import *
from scoreboard import *
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong :The Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
WINNING_SCORE = 5

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect missing r paddle
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect missing l paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Check if either player has won
    if scoreboard.l_score >= WINNING_SCORE:
        game_is_on = False
        scoreboard.game_over("Left Player Wins!")

    if scoreboard.r_score >= WINNING_SCORE:
        game_is_on = False
        scoreboard.game_over("Right Player Wins!")
screen.exitonclick()

