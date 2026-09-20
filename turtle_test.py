import turtle
import math


def polyline(t: turtle.Turtle, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)


def arc(t: turtle.Turtle, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t, n, length, step_angle)

def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def rectangle(t: turtle.Turtle, base, height):
    for length in (base, height, base, height):
        t.forward(length)
        t.left(90)
def square(t: turtle.Turtle, length):
    rectangle(t, length, length)

def draw_ribbon(t: turtle.Turtle, x, y, base, height, color="green"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base, height)
    t.end_fill()
def draw_bow(t: turtle.Turtle, x, y, bow_size, color="green"):
    jump(t, x, y)
    temp_color = t.color()
    t.pensize(5)
    t.color(color)
    t.right(15)
    arc(t, bow_size, 120)
    t.left(60)
    arc(t, bow_size, 120)
    t.right(195)
    arc(t, bow_size, 120)
    t.left(60)
    arc(t, bow_size, 120)
    # t.color(temp_color)

def draw_present(
    t: turtle.Turtle, x, y, base, height, ribbon_width, color="red"
):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base, height)
    t.end_fill()
    p_center = x + (base / 2)
    r_x = p_center - (ribbon_width / 2)
    draw_ribbon(t, r_x, y, ribbon_width, height)
    r_y = (y + (height / 2)) - (ribbon_width / 2)
    draw_ribbon(t, x, r_y, base, ribbon_width)
    draw_bow(t, p_center, y + height, base / 3)

#Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")

# Set the width and height of the screen
screen.setup(width=600, height=600)

# Clear the screen
t.clear()

t.color("white")

square(t, 100)
jump(t, 70, 70)
square(t, 200)
rectangle(t, 100, 200)

t.color("white")
draw_present(t, -10, -50, 69, 69, 5)








# Close the turtle graphics window when clicked
turtle.exitonclick()