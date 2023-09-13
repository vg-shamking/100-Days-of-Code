from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.goto(position)

snake_head = Turtle()
snake_head.color("white")
snake_head.shape("square")
snake_head.goto(0, 20)

snake_body = Turtle()
snake_body.color("white")
snake_body.shape("square")
snake_body.goto(-20, 20)

snake_tail = Turtle()
snake_tail.color("white")
snake_tail.shape("square")
snake_tail.goto(-40, 20)


screen.exitonclick()
