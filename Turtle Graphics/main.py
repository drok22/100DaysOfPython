import random
import turtle as turtle_module

tim = turtle_module.Turtle()
turtle_module.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

'''
timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("green")
timmy_turtle.penup()
timmy_turtle.setposition(-32.5,375)
timmy_turtle.pendown()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy_turtle.forward(75)
        timmy_turtle.right(angle)

for shape_side_n in range(3, 30):
    draw_shape(shape_side_n)
'''
screen = turtle_module.Screen()
screen.exitonclick()