# Block Scope:

# player_health = 10
#
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
#
# drink_potion()
#
# if 3 > 2:
#     a_variable = 10

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]


print(new_enemy)  # Error as print(new_enemy) is outside block
