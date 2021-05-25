import turtle
from turtle import *
from colors import *
import random

turtle.colormode(255)

class Capstone(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed("slow")
        self.color(chose_color())
        self.penup()
        self.goto(pos)


    def move(self):
        self.backward(5)