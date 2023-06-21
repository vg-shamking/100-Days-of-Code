# states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
#
# num_states = len(states_of_america)
# # print(states_of_america[3])  # IndexError: list index out of range as list is 0-1-2
# print(states_of_america[num_states - 1])

fruits = ["Strawberries",
          " Nectarines",
          "Apples",
          "Grapes",
          "Peaches",
          "Cherries",
          "Pears"
          ]

vegetables = ["Spinach",
              "Kale",
              "Tomatoes",
              "Celery",
              "Potatoes"
              ]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[0][0])
print(dirty_dozen[1])
print(dirty_dozen[1][0])
