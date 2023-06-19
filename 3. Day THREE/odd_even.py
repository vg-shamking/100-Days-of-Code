# Example of the 'modulo' usage %
# 7 % 2
# print(7 % 2)  # 2 + 2 + 2 + 1 - result 1
# print(7 % 3)  # 3 + 3 + 1 - result 1
# print(6 % 3)  # 3 + 3 + 0 - result 0

number = int(input("Which number do you want to check?"))
if number % 2 == 0:
    print("Chosen number is even!")
else:
    print("Chosen number is odd!")
