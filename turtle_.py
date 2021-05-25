from turtle import *


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fast")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.reset()

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)