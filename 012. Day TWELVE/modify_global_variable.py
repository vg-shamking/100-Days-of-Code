# Modifying Global Scope

enemies = 1


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


increase_enemies()
print(f"Enemies outside function: {enemies}")
