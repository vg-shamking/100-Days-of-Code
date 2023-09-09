import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_clr = (r, g, b)
    return random_clr


def draw_spinograph(size_of_gap):
    for _ in range(int(180 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)
        tim.circle(100)


tim.pensize(3)
tim.shapesize(1)
tim.shape("turtle")

# for _ in range(36):
#     tim.speed("fastest")
#     tim.color(random_color())
#     tim.circle(100)
#     current_heading = tim.heading()
#     tim.setheading(current_heading + 10)
#     tim.circle(100)

draw_spinograph(5)

screen = t.Screen()
screen.exitonclick()
