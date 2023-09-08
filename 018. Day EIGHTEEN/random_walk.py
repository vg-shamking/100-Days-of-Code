import turtle as t
import random

tim = t.Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.shapesize(1.5)
tim.shape("turtle")

for _ in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
