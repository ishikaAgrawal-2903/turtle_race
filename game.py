from turtle import *


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_on = True
        self.game_speed = 0.1
        self.level = 0
        self.increase_level()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.game_on = False
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.color("white")
        self.goto(-230, 270)
        self.write(f"Level - {self.level}", align="center", font=("Courier", 16, "normal"))