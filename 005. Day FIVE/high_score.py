students_score = input("Input a list of student scores ").split()  # 78 65 89 86 55 91 64 89
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)

# print(max(students_score))
# print(min(students_score))

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(highest_score)
