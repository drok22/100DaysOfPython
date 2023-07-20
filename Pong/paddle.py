from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
MOVEMENT_DISTANCE = 28

class Paddle(Turtle):
    def __init__(self, x:float, y:float):
        super().__init__()
        self.shape("square")
        self.color("white")
        #self.speed("fastest")
        self.shapesize(stretch_wid = PADDLE_WIDTH, stretch_len = PADDLE_LENGTH)
        self.penup()
        self.goto(x, y)

    def paddle_up(self):
        new_y = self.ycor() + MOVEMENT_DISTANCE
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - MOVEMENT_DISTANCE
        self.goto(self.xcor(), new_y)