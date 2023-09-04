class User:

    def __init__(self, user_id, username, seats):
        self.seats = seats
        self.id = user_id
        self.username = username
        self.follower = 0
        print("new user being created...")


user_1 = User("001", "angela", 5)

print(user_1.seats)
print(user_1.id)
print(user_1.follower)

user_2 = User("002", "jack", 4)

print(user_2.seats)
print(user_2.id)
print(user_2.username)
