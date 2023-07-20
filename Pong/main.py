import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RIGHT_PADDLE_X = 350
LEFT_PADDLE_X = -350
TOP_WALL_Y = 280
BOTTOM_WALL_Y = -280
LEFT_PADDLE_X = -320
RIGHT_PADDLE_X = 320
PADDLE_Y = 0
LEFT_WALL_LIMIT = -380
RIGHT_WALL_LIMIT = 380
COLLISION_BUFFER = 50

screen = Screen()
screen.bgcolor("black")
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_X, PADDLE_Y)
left_paddle = Paddle(LEFT_PADDLE_X, PADDLE_Y)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

game_over = False

while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()    
    
    # Detect collision with upper/lower walls
    if ball.ycor() > TOP_WALL_Y or ball.ycor() < BOTTOM_WALL_Y:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < COLLISION_BUFFER and ball.xcor() > RIGHT_PADDLE_X or ball.distance(left_paddle) < COLLISION_BUFFER and ball.xcor() < LEFT_PADDLE_X:
        ball.bounce_x()

    # Detect when right paddle misses ball
    if ball.xcor() > RIGHT_WALL_LIMIT: 
        scoreboard.left_scored()
        ball.reset_position()

    # Detect when left paddle misses ball    
    if ball.xcor() < LEFT_WALL_LIMIT:
        scoreboard.right_scored()
        ball.reset_position()

screen.exitonclick()