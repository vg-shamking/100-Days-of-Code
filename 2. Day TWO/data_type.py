two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print(first_digit)
print(second_digit)
result = int(first_digit) + int(second_digit)
another_result = int(first_digit + second_digit)
print(result)
print(another_result)
print(type(another_result))
