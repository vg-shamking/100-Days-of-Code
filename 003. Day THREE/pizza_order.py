bill = 0
print(f"Please order Pizza following size:")
print("Small Pizza: S ")
print("Medium Pizza: M ")
print("Large Pizza: L ")
choice = input("Your choice: ")

if choice == "S":
    bill += 15
elif choice == "M":
    bill += 20
elif choice == "L":
    bill += 25
else:
    print("Incorrect choice")
print(f"Total bill is ${bill}")
