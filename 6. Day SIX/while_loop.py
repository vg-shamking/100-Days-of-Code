"""
For

for item in list_of_items:
    #Do something to each item

for number in range (a, b):
    print(number)


While

while something_is_true:
    #Do something repeatedly
"""


def jump():
    pass


def at_goal():
    pass


number_of_hurdle = 6

while not at_goal() and number_of_hurdle > 0:
    jump()
    number_of_hurdle -= 1
    print(number_of_hurdle)
