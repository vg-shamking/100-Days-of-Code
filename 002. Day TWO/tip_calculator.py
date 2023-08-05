print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to add? 10,12 or 15? %"))
people = int(input("How many people to split the bill? "))
bill_with_tip = (tip / 100) * bill + bill
print(f"Bill with tips: {bill_with_tip}")
bill_divided = round(float(bill_with_tip / people), 3)
print(f"Bill per person: ${bill_divided}")
bill_divided1 = "{:.2f}".format(bill_divided)
print(bill_divided1)
test = bill_divided * people
print(f"Test: {test}")
