# Tuple () - immutable
# List [] - mutable
# Dict {}

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_clr = (r, g, b)
    return random_clr


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.shapesize(1.5)
tim.shape("turtle")

for _ in range(50):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
