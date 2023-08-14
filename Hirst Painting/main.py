'''
# Used to get the color data used to create the 'random' dots from 'image.jpeg'

import colorgram

rgb_colors = []
colors = colorgram.extract('Hirst Painting/image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
'''
import turtle as turtle_module
import random
from constants import COLOR_LIST

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(COLOR_LIST))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
