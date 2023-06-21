# fruits = [item1, item2]
#
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

print(states_of_america[0])
print(states_of_america[-1])
states_of_america[2] = "Chinatown"
print(states_of_america[-1])
print(states_of_america)
states_of_america.append("Volodymyr")
print(states_of_america)

states_of_america.extend(["Omarymyr", "Jack Bear"])
print(states_of_america)

states_of_america.pop()
print(states_of_america)
