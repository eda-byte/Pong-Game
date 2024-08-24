from turtle import Screen,Turtle
import time
import random
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
       # self.ball = Turtle()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.setpos(0,0)
        self.dx = 10  # Change in x (speed in x direction) x_move
        self.dy = 10  # Change in y (speed in y direction)
        self.move_speed=0.1
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
    def bounce_y(self):
        # Bounce off the top or bottom edges
        self.dy *= -1
    def bounce_x(self):
        self.dx *= -1
        self.move_speed*=0.9
    def miss(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

