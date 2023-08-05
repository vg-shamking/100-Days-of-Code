import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# EASY LEVEL
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#     # print(password)
#
# for numb in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#     # print(password)
#
# for symb in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#     # print(password)

# print(f"Here is your password: {password}")

# HARD LEVEL
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    # print(password)

for numb in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    # print(password)

for symb in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
    # print(password)

print(f"Here is your password list before shuffle: {password_list}")
random.shuffle(password_list)
print(f"Here is your password list with shuffle: {password_list}")

password = ""
for let in password_list:
    password += let
print(type(password))
print(f"Here is your password string after shuffle: {password}")
