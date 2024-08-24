from turtle import Screen,Turtle
import time
import random

class Paddle(Turtle):#inherit from Turtle class so paddle obj becomes turtle obj



    def __init__(self, position):#paddle classes parameter
        super().__init__()
        self.create_paddle(position)
        self.go_up()
        self.go_down()

    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        # if y < 250:  # Prevent moving off the screen
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        # if y> -250:
        self.goto(self.xcor(), new_y)

    # Creating a paddle
