students_heights = input("Input a list of student heights ").split()  # 156 178 165 171 187
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

# print(len(students_heights))
# print(sum(students_heights))

# total_height = sum(students_heights)
# number_of_students = len(students_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

total_height = 0
for height in students_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in students_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
