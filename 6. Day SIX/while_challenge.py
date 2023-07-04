def jump():
    pass


def move():
    pass


def front_is_clear():
    pass


def wall_in_front():
    pass


def at_goal():
    pass


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
