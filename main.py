import time
from turtle import *
from turtle_ import *
import random
from capstone import *
from game import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

game = Game()
turtle = Tortoise()
cars_pos = []
capstones = []

for _ in range(0, 25):
    x = random.randint(-270, 270)
    y = random.randint(-250, 250)
    for car in cars_pos[0:len(cars_pos) - 1]:
        while car.distance((x, y)) < 70:
            x = random.randint(-270, 270)
            y = random.randint(-250, 250)
    car = Capstone((x, y))
    cars_pos.append(car)

screen.listen()
screen.onkeypress(turtle.move, "Up")
x = 0

while game.game_on:
    screen.update()
    time.sleep(game.game_speed)
    for capstone in cars_pos:
        capstone.move()
        if capstone.distance(turtle) < 23 and capstone.ycor() - turtle.ycor() < 0.5:
            game.game_on = False
            game.game_over()

    if turtle.ycor() > 300:
        turtle.reset()
        game.game_speed *= 0.7
        game.increase_level()
    if x % 5 == 0:
        new_y = random.randint(-250, 260)
        car = Capstone((300, new_y))
        cars_pos.append(car)
    x += 1

done()
