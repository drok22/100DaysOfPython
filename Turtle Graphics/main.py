import random
import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.bgcolor("black")

'''
turtle_module.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
'''

tim.shape("turtle")
tim.color("green")
tim.penup()
tim.setposition(-32.5,375)
tim.pendown()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(75)
        tim.right(angle)

for shape_side_n in range(3, 30):
    draw_shape(shape_side_n)

screen.exitonclick()