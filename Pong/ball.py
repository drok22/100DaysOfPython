from turtle import Turtle

BALL_DIAMETER = 1
MOVE_DISTANCE = 10
START_MOVE_SPEED = 0.1
MOVE_SPEED_DELTA = 0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_direction = MOVE_DISTANCE
        self.y_direction = MOVE_DISTANCE
        self.move_speed = START_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.move_speed *= MOVE_SPEED_DELTA

    def reset_position(self):
        self.move_speed = START_MOVE_SPEED
        self.goto(0,0)
        self.bounce_x()
