import random
from turtle import Turtle

LOCATION_LIMIT = 270

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto(random.randint(-LOCATION_LIMIT, LOCATION_LIMIT), random.randint(-LOCATION_LIMIT, LOCATION_LIMIT))

    def new_food(self):
        self.goto(random.randint(-LOCATION_LIMIT, LOCATION_LIMIT), random.randint(-LOCATION_LIMIT, LOCATION_LIMIT))
