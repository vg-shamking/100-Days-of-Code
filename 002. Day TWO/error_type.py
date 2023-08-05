# Possible Errors
#
# len(123)  # Gives TypeError: object of type 'int' has no len()
# num_char = len(input("What is your name? "))
# print(type(num_char))  # <class 'int'>
# new_num_char = str(num_char)
# print(type(new_num_char))  # <class 'str'>

a = 123
type(a)
print(type(a))

a = str(123)
type(a)
print(type(a))
b = (print(70 + float(100.5)))
print(type(b))  # <class 'NoneType'>
