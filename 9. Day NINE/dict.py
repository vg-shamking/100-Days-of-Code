# Dictionary consists of:
# {Key : Value}

programming_dictionary = {"Bug": "An error is a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again."}

# Retrieve
# print(programming_dictionary["Bug"])

# Add
# programming_dictionary["Recursion"] = "Something to be added"
# print(programming_dictionary)

# empty_dictionary = {}
# print(empty_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary
programming_dictionary["Bug"] = "New edited information for bug"
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)
