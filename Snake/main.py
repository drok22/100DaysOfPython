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

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def quit_game():
    screen.bye()

def start_game():
    game_over = False
    scoreboard.start_game()
    while not game_over:
        screen.update()
        time.sleep(0.1)
        snake.move()
    
        # detect snake eating food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.new_food()
            snake.extend()

        if snake.head.xcor() > MAXCOR or snake.head.xcor() < MINCOR or snake.head.ycor() > MAXCOR or snake.head.ycor() < MINCOR:
            scoreboard.reset()
            snake.reset()
            game_over = True
            scoreboard.game_over()
        
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                game_over = True
                scoreboard.game_over()

screen.onkey(start_game, "space")
screen.onkey(quit_game, "Escape")
#screen.exitonclick()
screen.mainloop()