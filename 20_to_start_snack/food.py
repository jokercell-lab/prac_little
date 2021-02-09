from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(1000)
        self.renew()

    def renew(self):
        ran_x = random.randint(-380, 380)
        ran_y = random.randint(-380, 380)
        self.goto(ran_x, ran_y)