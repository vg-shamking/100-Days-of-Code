print("Welcome to Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
# print(name1.lower().count("a"))
combine_string = name1 + name2
small = combine_string.lower()
t = small.count("t")
r = small.count("r")
u = small.count("u")
# e = small.count("e")
ll = small.count("l")
o = small.count("o")
v = small.count("v")
e = small.count("e")
true = t + r + u + e
love = ll + o + v + e
love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 90:
    print(f"You love score is {love_score}")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Score: {love_score}")
else:
    print(love_score)
