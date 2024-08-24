from turtle import Screen,Turtle
import time
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title(" Pong.")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#top_paddle=Paddle((100,100))
#down_paddle=Paddle((-122,-33))
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ((ball.distance(r_paddle)<50 and ball.xcor()>320)or
            ball.distance(l_paddle)<30 and ball.xcor()>-380):
        ball.speed(0)
        ball.bounce_x()
    #    time.sleep(0.00001)

    #detect R paddle misses


    if ball.xcor()>390 :
        ball.miss()
        scoreboard.l_point()

    # detect L paddle misses
    if ball.xcor()< -390:
        ball.miss()
        scoreboard.r_point()












screen.exitonclick()