# Usage of variables
name = "John"
print(name)
name = input("What is your name? ")
print(name)
length = len(name)
print(length)
print("\n" + "*" * 20)
a = 5
b = 8
print(a)
print(b)
print("Change: ")
a, b = b, a
print(a)
print(b)
print("Change: ")
c = a
a = b
b = c
print(a)
print(b)
print("Goooood!")
