import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

MAXCOR = 280
MINCOR = -280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) # Do not draw screen continuously.
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True

#-----------------------------------------------------
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
   
    # detect snake eating food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.new_food()
        snake.extend()

    if snake.head.xcor() > MAXCOR or snake.head.xcor() < MINCOR or snake.head.ycor() > MAXCOR or snake.head.ycor() < MINCOR:
        game_running = False
        scoreboard.game_over()
    
    for segment in snake.segments:
        if segment != snake.head and snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()

screen.exitonclick()